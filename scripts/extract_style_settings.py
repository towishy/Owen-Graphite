"""Extract the Style Settings contract from dev/00-settings.css.

dev/00-settings.css carries the Style Settings YAML schema inside a
`/* @settings ... */` block. This script parses that block (with PyYAML
when available, falling back to a minimal hand parser) and emits:

- docs/v3/style-settings-contract.md (human-readable table)
- docs/v3/style-settings-contract.json (programmatic)

The v3-rewrite must declare exactly the same option ids with the same
types and defaults so existing user vault configurations keep working.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTINGS_CSS = ROOT / "dev" / "00-settings.css"
OUT_DIR = ROOT / "docs" / "v3"
OUT_DIR.mkdir(parents=True, exist_ok=True)

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


SETTINGS_BLOCK_RE = re.compile(r"/\*\s*@settings\s*(.*?)\*/", re.DOTALL)


def extract_yaml(css_text: str) -> str:
    match = SETTINGS_BLOCK_RE.search(css_text)
    if not match:
        raise SystemExit("No @settings block found in dev/00-settings.css")
    return match.group(1)


def parse_minimal(yaml_text: str) -> dict:
    """Fallback minimal parser if PyYAML is not available.

    Owen Graphite's @settings block uses a flat list of dict entries
    separated by `-` markers; values are simple scalars. This parser is
    NOT a general-purpose YAML parser — it's just enough to extract id,
    title, description, type, default and other scalar fields.
    """
    out: dict = {"name": None, "id": None, "settings": []}
    current: dict | None = None
    current_options_field: str | None = None
    for raw in yaml_text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith("name:"):
            out["name"] = line.split(":", 1)[1].strip()
            continue
        if line.startswith("id:") and out["id"] is None and current is None:
            out["id"] = line.split(":", 1)[1].strip()
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if stripped.startswith("-"):
            # New list entry
            if current is not None:
                out["settings"].append(current)
            current = {}
            current_options_field = None
            payload = stripped[1:].strip()
            if payload:
                # Inline `- key: value`
                if ":" in payload:
                    k, _, v = payload.partition(":")
                    current[k.strip()] = v.strip().strip("'\"")
            continue
        if current is None:
            continue
        if ":" in stripped:
            k, _, v = stripped.partition(":")
            k = k.strip()
            v = v.strip()
            if v == "":
                current_options_field = k
                current[k] = []
                continue
            current[k] = v.strip("'\"")
            current_options_field = None
    if current is not None:
        out["settings"].append(current)
    return out


def parse(yaml_text: str) -> dict:
    if yaml is not None:
        try:
            return yaml.safe_load(yaml_text)
        except Exception:
            pass
    return parse_minimal(yaml_text)


def main() -> None:
    css_text = SETTINGS_CSS.read_text(encoding="utf-8")
    yaml_text = extract_yaml(css_text)
    data = parse(yaml_text)
    settings = data.get("settings") or []

    # Filter only functional options (skip headings/info blocks)
    functional_types = {
        "class-toggle",
        "variable-text",
        "variable-number",
        "variable-number-slider",
        "variable-select",
        "variable-color",
        "class-select",
    }
    functional = [
        s for s in settings if isinstance(s, dict) and s.get("type") in functional_types
    ]

    json_out = OUT_DIR / "style-settings-contract.json"
    json_out.write_text(
        json.dumps(
            {
                "schema_name": data.get("name"),
                "schema_id": data.get("id"),
                "total_entries": len(settings),
                "functional_options": len(functional),
                "options": functional,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    md = [
        "# v3 Style Settings Contract (extracted from v2.30.14)",
        "",
        "이 문서는 `scripts/extract_style_settings.py`가 자동 생성합니다.",
        "v3-rewrite는 아래 모든 기능 옵션의 `id`/`type`/`default`/`title`을 그대로 유지해야 합니다.",
        "사용자 vault에 저장된 기존 설정이 v3.0 설치 후에도 동일하게 적용됩니다.",
        "",
        f"- 스키마 이름: `{data.get('name')}`",
        f"- 스키마 id: `{data.get('id')}`",
        f"- 전체 엔트리(heading 포함): **{len(settings)}**",
        f"- 기능 옵션 수(`class-toggle` / `variable-*` / `class-select`): **{len(functional)}**",
        "",
        "## 기능 옵션 목록",
        "",
        "| id | type | default | title |",
        "| --- | --- | --- | --- |",
    ]
    for opt in functional:
        opt_id = opt.get("id", "—")
        opt_type = opt.get("type", "—")
        default = opt.get("default", "—")
        title = (opt.get("title") or "—").replace("|", "\\|")
        md.append(f"| `{opt_id}` | `{opt_type}` | `{default}` | {title} |")

    md.append("")
    md.append("## 비기능 엔트리 (heading / info)")
    md.append("")
    md.append("| id | type | title |")
    md.append("| --- | --- | --- |")
    for opt in settings:
        if not isinstance(opt, dict):
            continue
        if opt.get("type") in functional_types:
            continue
        opt_id = opt.get("id", "—")
        opt_type = opt.get("type", "—")
        title = (opt.get("title") or "—").replace("|", "\\|")
        md.append(f"| `{opt_id}` | `{opt_type}` | {title} |")

    md_out = OUT_DIR / "style-settings-contract.md"
    md_out.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"Wrote {md_out.relative_to(ROOT)}")
    print(f"Wrote {json_out.relative_to(ROOT)}")
    print(f"Functional options: {len(functional)}")


if __name__ == "__main__":
    main()
