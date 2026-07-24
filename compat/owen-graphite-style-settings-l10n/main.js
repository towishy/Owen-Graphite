"use strict";

const LANGUAGE_ID = "ogd-style-settings-language";
const AUTO_CLASS = "ogd-language-auto";
const EN_CLASS = "ogd-language-en";
const KO_CLASS = "ogd-language-ko";
const FENCE_RE = /^(\s{0,3})(`{3,}|~{3,})([^\r\n]*)$/;
const TITLE_ATTRIBUTE_RE = /(?:^|\s)title=("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')(?=\s|$)/i;

const CODE_LANGUAGE_LABELS = {
  bash: "Shell",
  sh: "Shell",
  shell: "Shell",
  zsh: "Shell",
  powershell: "PowerShell",
  ps1: "PowerShell",
  pwsh: "PowerShell",
  py: "Python",
  python: "Python",
  js: "JavaScript",
  javascript: "JavaScript",
  ts: "TypeScript",
  typescript: "TypeScript",
  md: "Markdown",
  markdown: "Markdown",
  txt: "Text",
  text: "Text",
  plain: "Text",
  plaintext: "Text",
  kql: "Kusto",
  "kql-query": "Kusto",
  kusto: "Kusto",
};

function localeFromClasses(classList, obsidianLocale = "en") {
  if (classList.contains(KO_CLASS)) return "ko";
  if (classList.contains(EN_CLASS)) return "en";
  return /^ko(?:[-_]|$)/i.test(obsidianLocale) ? "ko" : "en";
}

function localizedEntry(catalog, id, locale) {
  const entry = catalog[id];
  return entry ? entry[locale] : undefined;
}

function translateModel(catalog, id, locale, optionValues = []) {
  const entry = localizedEntry(catalog, id, locale);
  if (!entry) return undefined;
  return {
    title: entry.title,
    description: entry.description || "",
    options: optionValues.map((value) => entry.options?.[value] ?? value),
  };
}

function decodeTitle(value) {
  if (value.startsWith('"')) {
    try {
      return JSON.parse(value);
    } catch (_error) {
      return value.slice(1, -1);
    }
  }
  return value.slice(1, -1).replace(/\\'/g, "'").replace(/\\\\/g, "\\");
}

function parseFenceLine(line) {
  const match = String(line).match(FENCE_RE);
  if (!match) return undefined;
  const info = match[3].trim();
  const titleMatch = info.match(TITLE_ATTRIBUTE_RE);
  const infoWithoutTitle = info.replace(TITLE_ATTRIBUTE_RE, " ").trim();
  return {
    fence: match[2],
    hasTitle: Boolean(titleMatch),
    language: infoWithoutTitle.split(/\s+/, 1)[0] || "",
    title: titleMatch ? decodeTitle(titleMatch[1]) : "",
  };
}

function codeLanguageLabel(language) {
  const normalized = String(language || "").toLowerCase();
  if (!normalized) return "";
  return CODE_LANGUAGE_LABELS[normalized] || normalized.replace(/(^|[-_])(\w)/g, (_match, _separator, letter) => letter.toUpperCase());
}

function updateFenceTitle(line, title) {
  const match = String(line).match(FENCE_RE);
  if (!match) throw new Error("The target line is not a fenced code block opener.");
  const info = match[3].trim().replace(TITLE_ATTRIBUTE_RE, " ").replace(/\s+/g, " ").trim();
  const normalizedTitle = String(title).replace(/[\r\n]+/g, " ");
  const updatedInfo = [info, `title=${JSON.stringify(normalizedTitle)}`].filter(Boolean).join(" ");
  return `${match[1]}${match[2]} ${updatedInfo}`;
}

function findFenceOpeners(source) {
  const lines = String(source).split(/\r?\n/);
  const openers = [];
  let activeFence;
  for (let lineNumber = 0; lineNumber < lines.length; lineNumber += 1) {
    const line = lines[lineNumber];
    if (activeFence) {
      const trimmed = line.trim();
      const run = trimmed.match(/^(`+|~+)/)?.[0] || "";
      if (run[0] === activeFence.character && run.length >= activeFence.length && trimmed.slice(run.length).trim() === "") {
        activeFence = undefined;
      }
      continue;
    }
    const parsed = parseFenceLine(line);
    if (!parsed) continue;
    openers.push({ ...parsed, line: lineNumber, source: line });
    activeFence = { character: parsed.fence[0], length: parsed.fence.length };
  }
  return openers;
}

function findFencedCodeBlocks(source) {
  const lines = String(source).split(/\r?\n/);
  const blocks = [];
  for (let lineNumber = 0; lineNumber < lines.length; lineNumber += 1) {
    const opener = parseFenceLine(lines[lineNumber]);
    if (!opener) continue;
    for (let closingLine = lineNumber + 1; closingLine < lines.length; closingLine += 1) {
      const trimmed = lines[closingLine].trim();
      const run = trimmed.match(/^(`+|~+)/)?.[0] || "";
      if (run[0] !== opener.fence[0] || run.length < opener.fence.length || trimmed.slice(run.length).trim() !== "") continue;
      blocks.push({ ...opener, code: lines.slice(lineNumber + 1, closingLine).join("\n"), line: lineNumber, source: lines[lineNumber] });
      lineNumber = closingLine;
      break;
    }
  }
  return blocks;
}

function normalizeCodeText(value) {
  return String(value).replace(/\r\n/g, "\n").replace(/\n+$/, "");
}

function findFencedCodeBlockForCode(source, expectedCode, expectedLanguage = "") {
  const normalizedCode = normalizeCodeText(expectedCode);
  const normalizedLanguage = String(expectedLanguage).toLowerCase();
  const matches = findFencedCodeBlocks(source).filter(
    (block) => normalizeCodeText(block.code) === normalizedCode
      && (!normalizedLanguage || block.language.toLowerCase() === normalizedLanguage),
  );
  return matches.length === 1 ? matches[0] : undefined;
}

function replaceFenceTitleAtLine(source, lineNumber, title, expectedLine) {
  const eol = source.includes("\r\n") ? "\r\n" : "\n";
  const lines = source.split(/\r?\n/);
  if (!Number.isInteger(lineNumber) || lineNumber < 0 || lineNumber >= lines.length) {
    throw new Error("The code block line is no longer available.");
  }
  if (expectedLine !== undefined && lines[lineNumber] !== expectedLine) {
    throw new Error("The code block changed before its title could be saved.");
  }
  lines[lineNumber] = updateFenceTitle(lines[lineNumber], title);
  return lines.join(eol);
}

function replaceFenceTitleNearLine(source, lineNumber, title, expectedLine) {
  const lines = source.split(/\r?\n/);
  if (lines[lineNumber] === expectedLine) {
    return replaceFenceTitleAtLine(source, lineNumber, title, expectedLine);
  }
  const adjacent = [lineNumber - 1, lineNumber + 1].filter((candidate) => lines[candidate] === expectedLine);
  if (adjacent.length !== 1) {
    throw new Error("The code block changed before its title could be saved.");
  }
  return replaceFenceTitleAtLine(source, adjacent[0], title, expectedLine);
}

function replaceFenceTitleForCode(source, expectedCode, title, expectedLanguage = "") {
  const block = findFencedCodeBlockForCode(source, expectedCode, expectedLanguage);
  if (!block) {
    throw new Error("The code block changed or is not unique.");
  }
  return replaceFenceTitleAtLine(source, block.line, title, block.source);
}


const catalog = {"ogd-settings-interface":{"ko":{"title":"인터페이스","description":"Owen Graphite 전체에서 사용할 언어를 선택합니다.","options":{},"default":""},"en":{"title":"Interface","description":"Choose the language used throughout Owen Graphite.","options":{},"default":""}},"ogd-style-settings-language":{"ko":{"title":"언어","description":"Obsidian 언어를 따르거나 Owen Graphite Style Settings에 표시할 언어를 재정의합니다.","options":{"ogd-language-auto":"자동 (Obsidian)","ogd-language-ko":"한국어","ogd-language-en":"English"},"default":"ogd-language-auto"},"en":{"title":"Language","description":"Follow Obsidian's language or override it for Owen Graphite Style Settings.","options":{"ogd-language-auto":"Automatic (Obsidian)","ogd-language-ko":"Korean","ogd-language-en":"English"},"default":"ogd-language-auto"}},"ogd-settings-reading":{"ko":{"title":"읽기와 본문","description":"","options":{},"default":""},"en":{"title":"Reading and body","description":"","options":{},"default":""}},"ogd-body-size":{"ko":{"title":"본문 폰트 크기","description":"본문(p, li 등) 기본 글자 크기","options":{},"default":"15"},"en":{"title":"Body font size","description":"Base font size for body text such as paragraphs and list items.","options":{},"default":"15"}},"ogd-line-height":{"ko":{"title":"본문 줄간격","description":"","options":{"1.35":"1.35","1.45":"1.45","1.5":"1.5","1.6":"1.6","1.7":"1.7"},"default":"1.5"},"en":{"title":"Body line height","description":"","options":{"1.35":"1.35","1.45":"1.45","1.5":"1.5","1.6":"1.6","1.7":"1.7"},"default":"1.5"}},"ogd-max-width":{"ko":{"title":"본문 최대 폭","description":"긴 문단은 읽기 문서 폭을, 넓은 표·보고서는 와이드 폭을 선택하세요.","options":{"210mm":"읽기 문서 · 210mm","297mm":"보고서 · 297mm","360mm":"와이드 보고서 · 360mm","420mm":"대형 표 · 420mm","100%":"전체 폭 · 100%"},"default":"420mm"},"en":{"title":"Maximum content width","description":"Choose a reading width for long prose or a wider width for tables and reports.","options":{"210mm":"Reading document · 210mm","297mm":"Report · 297mm","360mm":"Wide report · 360mm","420mm":"Large table · 420mm","100%":"Full width · 100%"},"default":"420mm"}},"ogd-accent":{"ko":{"title":"헤더 강조 색상","description":"","options":{},"default":"#4b5563"},"en":{"title":"Heading accent color","description":"","options":{},"default":"#4b5563"}},"ogd-settings-tables":{"ko":{"title":"표와 코드","description":"","options":{},"default":""},"en":{"title":"Tables and code","description":"","options":{},"default":""}},"ogd-modern-tables":{"ko":{"title":"표 모던 스타일 강화","description":"표 헤더, 첫 컬럼, hover, PDF border를 보고서형 톤으로 강화","options":{},"default":"true"},"en":{"title":"Enhanced modern table style","description":"Strengthens table headers, first columns, hover states, and PDF borders with a report-oriented treatment.","options":{},"default":"true"}},"ogd-print-avoid-breaks":{"ko":{"title":"PDF 블록 분할 방지 강화","description":"callout, 표, mermaid, 코드블록, 이미지가 페이지 중간에서 잘리는 것을 완화","options":{},"default":"true"},"en":{"title":"Prevent PDF block splitting","description":"Reduces page breaks inside callouts, tables, Mermaid diagrams, code blocks, and images.","options":{},"default":"true"}},"ogd-settings-report":{"ko":{"title":"보고서와 PDF","description":"","options":{},"default":""},"en":{"title":"Reports and PDF","description":"","options":{},"default":""}},"ogd-report-mode":{"ko":{"title":"보고서 모드 (헤더 자동 넘버링 + 본문 들여쓰기 + 세리프)","description":"표지/넘버링/들여쓰기/세리프 본문을 한 번에 적용","options":{},"default":"false"},"en":{"title":"Report mode (numbered headings + indentation + serif)","description":"Applies cover, numbering, indentation, and serif body settings together.","options":{},"default":"false"}},"ogd-pdf-compact":{"ko":{"title":"PDF Compact Report","description":"PDF 출력 시 제목·본문·callout·표·참고 문헌 간격을 압축해 공백을 줄이고 정보 밀도를 높입니다.","options":{},"default":"false"},"en":{"title":"PDF compact report","description":"Reduces spacing between headings, body text, callouts, tables, and references for denser PDF output.","options":{},"default":"false"}},"ogd-pdf-visibility":{"ko":{"title":"PDF 보고서 가시성 강화","description":"PDF 출력에서 문서 상태 라벨, callout, 문서 끝 신호의 대비를 높입니다. 제목 계층과 표 디자인은 변경하지 않습니다.","options":{},"default":"false"},"en":{"title":"Enhanced PDF report visibility","description":"Increases contrast for document status labels, callouts, and end markers without changing heading hierarchy or table design.","options":{},"default":"false"}},"ogd-pdf-screen-delivery":{"ko":{"title":"PDF 고객 전달용 화면 가시성","description":"메일, Teams, 브라우저 미리보기에서 바로 읽히도록 제목 위계, 본문·표 크기, callout 구분, 라벨 톤을 조정합니다.","options":{},"default":"false"},"en":{"title":"PDF screen-delivery visibility","description":"Adjusts heading hierarchy, body and table sizes, callout separation, and label tone for email, Teams, and browser previews.","options":{},"default":"false"}},"ogd-pdf-client-delivery":{"ko":{"title":"PDF 고객 전달 권장 프리셋","description":"고객 공유용 PDF에 맞춰 본문·표·callout·코드·링크를 한 번에 읽기 좋은 톤으로 조정합니다.","options":{},"default":"false"},"en":{"title":"Recommended client PDF preset","description":"Tunes body text, tables, callouts, code, and links together for client-facing PDFs.","options":{},"default":"false"}},"ogd-pdf-font-size":{"ko":{"title":"PDF 글자 크기","description":"PDF 출력에서 본문, 목록, callout, 코드, 헤더/푸터 라벨 크기를 조정합니다. 제목 계층과 표 디자인은 변경하지 않습니다.","options":{"ogd-pdf-font-standard":"기본","ogd-pdf-font-comfortable":"편안하게","ogd-pdf-font-large":"크게"},"default":"ogd-pdf-font-standard"},"en":{"title":"PDF font size","description":"Adjusts body, list, callout, code, and header/footer label sizes without changing heading hierarchy or table design.","options":{"ogd-pdf-font-standard":"Standard","ogd-pdf-font-comfortable":"Comfortable","ogd-pdf-font-large":"Large"},"default":"ogd-pdf-font-standard"}},"ogd-pdf-link-mode":{"ko":{"title":"PDF 링크 출력 방식","description":"PDF export에서 외부 URL을 본문 뒤에 표시할지, 숨길지, 참고문헌 중심으로 정리할지 선택합니다.","options":{"ogd-pdf-links-inline":"Inline URL","ogd-pdf-links-clean":"Clean Reading","ogd-pdf-links-reference":"Reference First"},"default":"ogd-pdf-links-inline"},"en":{"title":"PDF link output mode","description":"Choose whether external URLs appear inline, stay hidden, or are organized around references in PDF exports.","options":{"ogd-pdf-links-inline":"Inline URL","ogd-pdf-links-clean":"Clean Reading","ogd-pdf-links-reference":"Reference First"},"default":"ogd-pdf-links-inline"}},"ogd-serif-body":{"ko":{"title":"본문 세리프 글꼴","description":"본문만 Noto Serif KR로 전환 (긴 보고서 가독성)","options":{},"default":"false"},"en":{"title":"Serif body font","description":"Switches body text to Noto Serif KR for long-report readability.","options":{},"default":"false"}},"ogd-indent-paragraph":{"ko":{"title":"첫 줄 들여쓰기","description":"한국 보고서 스타일 1em 들여쓰기","options":{},"default":"false"},"en":{"title":"First-line indentation","description":"Applies a 1em first-line indent for Korean report styling.","options":{},"default":"false"}},"ogd-auto-number-headings":{"ko":{"title":"헤더 자동 넘버링 (1. 1.1 1.1.1)","description":"","options":{},"default":"false"},"en":{"title":"Automatic heading numbering (1. 1.1 1.1.1)","description":"","options":{},"default":"false"}},"ogd-heading-template":{"ko":{"title":"헤더 디자인 템플릿","description":"H1-H4 디자인을 Live Preview와 PDF 출력에 함께 적용합니다.","options":{"ogd-heading-printclean":"프린트 클린","ogd-heading-keyline":"코발트 키라인","ogd-heading-bracket":"브래킷 챕터","ogd-heading-quiet-ledger":"조용한 장부","ogd-heading-focus-bar":"포커스 바","ogd-heading-double-rule":"더블룰 클래식","ogd-heading-tag-ribbon":"태그 리본","ogd-heading-number-stamp":"넘버 스탬프","ogd-heading-grid-index":"그리드 인덱스"},"default":"ogd-heading-printclean"},"en":{"title":"Heading design template","description":"Applies the H1-H4 design to Live Preview and PDF output.","options":{"ogd-heading-printclean":"Print Clean","ogd-heading-keyline":"Cobalt Keyline","ogd-heading-bracket":"Bracket Chapter","ogd-heading-quiet-ledger":"Quiet Ledger","ogd-heading-focus-bar":"Focus Bar","ogd-heading-double-rule":"Double-rule Classic","ogd-heading-tag-ribbon":"Tag Ribbon","ogd-heading-number-stamp":"Number Stamp","ogd-heading-grid-index":"Grid Index"},"default":"ogd-heading-printclean"}},"ogd-drop-cap":{"ko":{"title":"드롭 캡 (첫 문단 첫 글자 크게)","description":"","options":{},"default":"false"},"en":{"title":"Drop cap (enlarge first paragraph initial)","description":"","options":{},"default":"false"}},"ogd-spacing-preset":{"ko":{"title":"간격 프리셋","description":"","options":{"ogd-spacing-compact":"컴팩트","ogd-spacing-standard":"표준","ogd-spacing-relaxed":"여유"},"default":"ogd-spacing-standard"},"en":{"title":"Spacing preset","description":"","options":{"ogd-spacing-compact":"Compact","ogd-spacing-standard":"Standard","ogd-spacing-relaxed":"Relaxed"},"default":"ogd-spacing-standard"}},"ogd-accent-preset":{"ko":{"title":"액센트 컬러 프리셋","description":"","options":{"ogd-accent-graphite":"Graphite (기본)","ogd-accent-blue":"Blue","ogd-accent-teal":"Teal","ogd-accent-violet":"Violet","ogd-accent-amber":"Amber"},"default":"ogd-accent-graphite"},"en":{"title":"Accent color preset","description":"","options":{"ogd-accent-graphite":"Graphite (default)","ogd-accent-blue":"Blue","ogd-accent-teal":"Teal","ogd-accent-violet":"Violet","ogd-accent-amber":"Amber"},"default":"ogd-accent-graphite"}},"ogd-code-theme":{"ko":{"title":"코드블록 테마","description":"","options":{"ogd-code-light":"Light (기본)","ogd-code-solarized":"Solarized","ogd-code-nord":"Nord","ogd-code-dracula":"Dracula (다크 전용)"},"default":"ogd-code-light"},"en":{"title":"Code block theme","description":"","options":{"ogd-code-light":"Light (default)","ogd-code-solarized":"Solarized","ogd-code-nord":"Nord","ogd-code-dracula":"Dracula (dark only)"},"default":"ogd-code-light"}},"ogd-settings-workspace":{"ko":{"title":"워크스페이스와 접근성","description":"","options":{},"default":""},"en":{"title":"Workspace and accessibility","description":"","options":{},"default":""}},"ogd-eye-care":{"ko":{"title":"시선 보호 모드 (베이지 배경)","description":"","options":{},"default":"false"},"en":{"title":"Eye-care mode (beige background)","description":"","options":{},"default":"false"}},"ogd-auto-dark":{"ko":{"title":"OS 다크 모드 자동 추종","description":"시스템 다크 모드일 때 자동으로 다크 테마 변수 적용","options":{},"default":"false"},"en":{"title":"Follow OS dark mode automatically","description":"Applies dark theme variables when the operating system uses dark mode.","options":{},"default":"false"}},"ogd-glass-intensity":{"ko":{"title":"데스크톱 Glass 강도","description":"데스크톱 UI chrome의 투명 유리/그림자 강도를 조정합니다. Reduced는 blur를 줄여 배터리와 저성능 환경에 적합합니다.","options":{"ogd-glass-off":"Off","ogd-glass-reduced":"Reduced","ogd-glass-subtle":"Subtle","ogd-glass-standard":"Standard","ogd-glass-strong":"Strong"},"default":"ogd-glass-standard"},"en":{"title":"Desktop glass intensity","description":"Adjusts transparency and shadow intensity for desktop UI chrome. Reduced lowers blur for battery life and lower-performance devices.","options":{"ogd-glass-off":"Off","ogd-glass-reduced":"Reduced","ogd-glass-subtle":"Subtle","ogd-glass-standard":"Standard","ogd-glass-strong":"Strong"},"default":"ogd-glass-standard"}},"ogd-motion-intensity":{"ko":{"title":"데스크톱 Hover 움직임","description":"버튼, 메뉴 항목, 설정 row의 hover/press lift 움직임을 조정합니다. Off는 움직임 없이 색과 그림자만 유지합니다.","options":{"ogd-motion-off":"Off","ogd-motion-subtle":"Subtle","ogd-motion-standard":"Standard"},"default":"ogd-motion-standard"},"en":{"title":"Desktop hover motion","description":"Adjusts hover and press lift for buttons, menu items, and setting rows. Off preserves color and shadow feedback without movement.","options":{"ogd-motion-off":"Off","ogd-motion-subtle":"Subtle","ogd-motion-standard":"Standard"},"default":"ogd-motion-standard"}},"ogd-cjk-boost":{"ko":{"title":"한글/CJK 폰트 +0.5px 자동 보정","description":"","options":{},"default":"true"},"en":{"title":"Automatic +0.5px Korean/CJK font adjustment","description":"","options":{},"default":"true"}},"ogd-settings-fonts":{"ko":{"title":"폰트 적용","description":"","options":{},"default":""},"en":{"title":"Font application","description":"","options":{},"default":""}},"ogd-interface-font-stack":{"ko":{"title":"인터페이스 폰트 직접 입력","description":"비워두면 Obsidian 외형 설정의 인터페이스 폰트를 따릅니다. 예시는 \"Malgun Gothic\", Pretendard, sans-serif 입니다.","options":{},"default":""},"en":{"title":"Custom interface font","description":"Leave empty to follow Obsidian's interface font. Example: \"Malgun Gothic\", Pretendard, sans-serif.","options":{},"default":""}},"ogd-reading-font-stack":{"ko":{"title":"본문 폰트 직접 입력","description":"비워두면 Obsidian 외형 설정의 텍스트 폰트를 따릅니다. 예시는 \"Noto Serif KR\", serif 입니다.","options":{},"default":""},"en":{"title":"Custom reading font","description":"Leave empty to follow Obsidian's text font. Example: \"Noto Serif KR\", serif.","options":{},"default":""}},"ogd-code-font-stack":{"ko":{"title":"코드 폰트 직접 입력","description":"비워두면 Obsidian 외형 설정의 모노스페이스 폰트를 따릅니다. 예시는 \"D2Coding\", \"JetBrains Mono\", monospace 입니다.","options":{},"default":""},"en":{"title":"Custom code font","description":"Leave empty to follow Obsidian's monospace font. Example: \"D2Coding\", \"JetBrains Mono\", monospace.","options":{},"default":""}},"ogd-status-font-stack":{"ko":{"title":"하단 상태바 폰트 직접 입력","description":"비워두면 인터페이스 폰트를 따릅니다. 예시는 \"Malgun Gothic\", sans-serif 입니다.","options":{},"default":""},"en":{"title":"Custom status bar font","description":"Leave empty to follow the interface font. Example: \"Malgun Gothic\", sans-serif.","options":{},"default":""}},"ogd-settings-pdf-marginalia":{"ko":{"title":"PDF 헤더/푸터 작은 라벨","description":"PDF 출력에만 첫 페이지 헤더와 마지막 페이지 푸터 라벨을 표시합니다. 화면 Reading View에는 노출하지 않습니다.","options":{},"default":""},"en":{"title":"Small PDF header/footer labels","description":"Shows header and footer labels only in PDF output, not in on-screen Reading View.","options":{},"default":""}},"ogd-pdf-header-enabled":{"ko":{"title":"첫 페이지 헤더 라벨 표시","description":"PDF 첫 페이지 상단에 한 줄 라벨을 표시합니다. 끄면 문구나 프리셋이 있어도 출력하지 않습니다.","options":{},"default":"false"},"en":{"title":"Show first-page header label","description":"Shows one label at the top of the first PDF page. Turning this off hides it even when text or a preset is configured.","options":{},"default":"false"}},"ogd-pdf-footer-enabled":{"ko":{"title":"마지막 페이지 푸터 라벨 표시","description":"PDF 마지막 콘텐츠 아래 중앙에 한 줄 라벨을 표시합니다. 끄면 문구나 프리셋이 있어도 출력하지 않습니다.","options":{},"default":"false"},"en":{"title":"Show last-page footer label","description":"Shows one centered label below the final PDF content. Turning this off hides it even when text or a preset is configured.","options":{},"default":"false"}},"ogd-pdf-label-layout":{"ko":{"title":"PDF 라벨 구성","description":"단일 라벨은 기존처럼 한 문구만 표시합니다. Key/Value는 `Prepared by` + `Owen Lee`처럼 붙어 있는 1쌍으로 표시합니다.","options":{"ogd-pdf-label-single":"단일 라벨","ogd-pdf-label-segmented":"Key/Value 1쌍","ogd-pdf-label-segmented-dual":"Key/Value 2쌍"},"default":"ogd-pdf-label-single"},"en":{"title":"PDF label layout","description":"Single label shows one phrase. Key/Value joins a pair such as `Prepared by` + `Owen Lee`.","options":{"ogd-pdf-label-single":"Single label","ogd-pdf-label-segmented":"One Key/Value pair","ogd-pdf-label-segmented-dual":"Two Key/Value pairs"},"default":"ogd-pdf-label-single"}},"ogd-pdf-settings-common":{"ko":{"title":"공통 구성","description":"","options":{},"default":""},"en":{"title":"Common configuration","description":"","options":{},"default":""}},"ogd-pdf-marginalia-preset":{"ko":{"title":"헤더/푸터 빠른 문구","description":"직접 문구를 비워둘 때 쓰는 출력용 조합입니다. 직접 입력한 헤더/푸터 문구가 있으면 입력값이 우선됩니다.","options":{"ogd-pdf-preset-custom":"직접 입력","ogd-pdf-preset-prepared-confidential":"준비본 + 기밀","ogd-pdf-preset-draft-internal":"초안 + 내부용","ogd-pdf-preset-final-end":"최종본 + 문서 끝","ogd-pdf-preset-status-end":"상태 + 문서 끝"},"default":"ogd-pdf-preset-custom"},"en":{"title":"Header/footer quick text","description":"Output combinations used when custom text is empty. Custom header or footer text takes precedence.","options":{"ogd-pdf-preset-custom":"Custom text","ogd-pdf-preset-prepared-confidential":"Prepared + Confidential","ogd-pdf-preset-draft-internal":"Draft + Internal","ogd-pdf-preset-final-end":"Final + End of Document","ogd-pdf-preset-status-end":"Status + End of Document"},"default":"ogd-pdf-preset-custom"}},"ogd-pdf-marginalia-accent":{"ko":{"title":"헤더/푸터 글자 색상","description":"두 라벨 공통 글자 색상입니다. 기본값은 출력물에 어울리는 graphite 톤입니다.","options":{},"default":"#475569"},"en":{"title":"Header/footer text color","description":"Shared text color for both labels. The default is a graphite tone suited to printed output.","options":{},"default":"#475569"}},"ogd-pdf-marginalia-style":{"ko":{"title":"헤더/푸터 라벨 스타일","description":"PDF 엔진에서 안정적인 표면만 제공합니다. 위치나 페이지 흐름은 바꾸지 않습니다.","options":{"ogd-pdf-label-minimal":"텍스트만","ogd-pdf-label-bordered":"은은한 테두리","ogd-pdf-label-filled":"은은한 채움","ogd-pdf-label-badge":"붙은 배지"},"default":"ogd-pdf-label-bordered"},"en":{"title":"Header/footer label style","description":"Provides surfaces that remain stable in PDF engines without changing position or page flow.","options":{"ogd-pdf-label-minimal":"Text only","ogd-pdf-label-bordered":"Subtle border","ogd-pdf-label-filled":"Subtle fill","ogd-pdf-label-badge":"Joined badge"},"default":"ogd-pdf-label-bordered"}},"ogd-pdf-marginalia-size":{"ko":{"title":"헤더/푸터 라벨 크기","description":"글자와 내부 여백을 조정합니다. 출력 안정성을 위해 두 단계만 제공합니다.","options":{"ogd-pdf-label-compact":"작게","ogd-pdf-label-standard":"표준"},"default":"ogd-pdf-label-standard"},"en":{"title":"Header/footer label size","description":"Adjusts text and internal padding with two print-stable sizes.","options":{"ogd-pdf-label-compact":"Compact","ogd-pdf-label-standard":"Standard"},"default":"ogd-pdf-label-standard"}},"ogd-pdf-settings-header":{"ko":{"title":"헤더 설정","description":"","options":{},"default":""},"en":{"title":"Header settings","description":"","options":{},"default":""}},"ogd-pdf-header-key-palette":{"ko":{"title":"헤더 Key 색상","description":"첫 페이지 헤더의 왼쪽 key 영역 색상입니다. 예 `Prepared by` 쪽 색상입니다.","options":{"ogd-pdf-header-key-graphite":"Graphite","ogd-pdf-header-key-slate":"Slate","ogd-pdf-header-key-sky":"Sky","ogd-pdf-header-key-teal":"Teal","ogd-pdf-header-key-mint":"Mint","ogd-pdf-header-key-violet":"Violet","ogd-pdf-header-key-rose":"Rose","ogd-pdf-header-key-amber":"Amber","ogd-pdf-header-key-blue":"Blue","ogd-pdf-header-key-indigo":"Indigo","ogd-pdf-header-key-cyan":"Cyan","ogd-pdf-header-key-emerald":"Emerald","ogd-pdf-header-key-lime":"Lime","ogd-pdf-header-key-orange":"Orange","ogd-pdf-header-key-red":"Red","ogd-pdf-header-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-header-key-graphite"},"en":{"title":"Header key color","description":"Color of the left key area in the first-page header, such as `Prepared by`.","options":{"ogd-pdf-header-key-graphite":"Graphite","ogd-pdf-header-key-slate":"Slate","ogd-pdf-header-key-sky":"Sky","ogd-pdf-header-key-teal":"Teal","ogd-pdf-header-key-mint":"Mint","ogd-pdf-header-key-violet":"Violet","ogd-pdf-header-key-rose":"Rose","ogd-pdf-header-key-amber":"Amber","ogd-pdf-header-key-blue":"Blue","ogd-pdf-header-key-indigo":"Indigo","ogd-pdf-header-key-cyan":"Cyan","ogd-pdf-header-key-emerald":"Emerald","ogd-pdf-header-key-lime":"Lime","ogd-pdf-header-key-orange":"Orange","ogd-pdf-header-key-red":"Red","ogd-pdf-header-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-header-key-graphite"}},"ogd-pdf-header-value-palette":{"ko":{"title":"헤더 Value 색상","description":"첫 페이지 헤더의 오른쪽 value 영역 색상입니다. 예 `Owen Lee - Sr. CSA` 쪽 색상입니다.","options":{"ogd-pdf-header-value-graphite":"Graphite","ogd-pdf-header-value-slate":"Slate","ogd-pdf-header-value-sky":"Sky","ogd-pdf-header-value-teal":"Teal","ogd-pdf-header-value-mint":"Mint","ogd-pdf-header-value-violet":"Violet","ogd-pdf-header-value-rose":"Rose","ogd-pdf-header-value-amber":"Amber","ogd-pdf-header-value-blue":"Blue","ogd-pdf-header-value-indigo":"Indigo","ogd-pdf-header-value-cyan":"Cyan","ogd-pdf-header-value-emerald":"Emerald","ogd-pdf-header-value-lime":"Lime","ogd-pdf-header-value-orange":"Orange","ogd-pdf-header-value-red":"Red","ogd-pdf-header-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-header-value-sky"},"en":{"title":"Header value color","description":"Color of the right value area in the first-page header, such as `Owen Lee - Sr. CSA`.","options":{"ogd-pdf-header-value-graphite":"Graphite","ogd-pdf-header-value-slate":"Slate","ogd-pdf-header-value-sky":"Sky","ogd-pdf-header-value-teal":"Teal","ogd-pdf-header-value-mint":"Mint","ogd-pdf-header-value-violet":"Violet","ogd-pdf-header-value-rose":"Rose","ogd-pdf-header-value-amber":"Amber","ogd-pdf-header-value-blue":"Blue","ogd-pdf-header-value-indigo":"Indigo","ogd-pdf-header-value-cyan":"Cyan","ogd-pdf-header-value-emerald":"Emerald","ogd-pdf-header-value-lime":"Lime","ogd-pdf-header-value-orange":"Orange","ogd-pdf-header-value-red":"Red","ogd-pdf-header-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-header-value-sky"}},"ogd-pdf-header-text":{"ko":{"title":"첫 페이지 헤더 1번 Key 문구","description":"단일 라벨에서는 전체 문구, Key/Value에서는 1번 왼쪽 key입니다. 예 `Prepared by`.","options":{},"default":""},"en":{"title":"First-page header pair 1 key text","description":"The full phrase in single-label layout or the left key in pair 1. Example: `Prepared by`.","options":{},"default":""}},"ogd-pdf-header-value":{"ko":{"title":"첫 페이지 헤더 1번 Value 문구","description":"Key/Value 구성에서 1번 오른쪽 value로 표시됩니다. 예 `Owen Lee` 또는 `Sr. CSA`. 단일 라벨 구성에서는 사용하지 않습니다.","options":{},"default":""},"en":{"title":"First-page header pair 1 value text","description":"The right value in pair 1, such as `Owen Lee` or `Sr. CSA`. Not used by single-label layout.","options":{},"default":""}},"ogd-pdf-header-dual-pair":{"ko":{"title":"첫 페이지 헤더 2번 Key/Value 표시","description":"기존 Key/Value 1쌍 구성에서 두 번째 key/value 쌍만 추가로 켭니다. PDF 라벨 구성에서 `Key/Value 2쌍`을 선택해도 같은 출력이 적용됩니다.","options":{},"default":"false"},"en":{"title":"Show first-page header pair 2","description":"Adds only the second key/value pair to the existing one-pair layout. Selecting `Two Key/Value pairs` in PDF label layout has the same effect.","options":{},"default":"false"}},"ogd-pdf-header2-key-palette":{"ko":{"title":"헤더 2번 Key 색상","description":"첫 페이지 헤더의 2번 key segment 색상입니다. 예 `Reviewed by` 쪽 색상입니다.","options":{"ogd-pdf-header2-key-graphite":"Graphite","ogd-pdf-header2-key-slate":"Slate","ogd-pdf-header2-key-sky":"Sky","ogd-pdf-header2-key-teal":"Teal","ogd-pdf-header2-key-mint":"Mint","ogd-pdf-header2-key-violet":"Violet","ogd-pdf-header2-key-rose":"Rose","ogd-pdf-header2-key-amber":"Amber","ogd-pdf-header2-key-blue":"Blue","ogd-pdf-header2-key-indigo":"Indigo","ogd-pdf-header2-key-cyan":"Cyan","ogd-pdf-header2-key-emerald":"Emerald","ogd-pdf-header2-key-lime":"Lime","ogd-pdf-header2-key-orange":"Orange","ogd-pdf-header2-key-red":"Red","ogd-pdf-header2-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-header2-key-graphite"},"en":{"title":"Header pair 2 key color","description":"Color of the second header key segment, such as `Reviewed by`.","options":{"ogd-pdf-header2-key-graphite":"Graphite","ogd-pdf-header2-key-slate":"Slate","ogd-pdf-header2-key-sky":"Sky","ogd-pdf-header2-key-teal":"Teal","ogd-pdf-header2-key-mint":"Mint","ogd-pdf-header2-key-violet":"Violet","ogd-pdf-header2-key-rose":"Rose","ogd-pdf-header2-key-amber":"Amber","ogd-pdf-header2-key-blue":"Blue","ogd-pdf-header2-key-indigo":"Indigo","ogd-pdf-header2-key-cyan":"Cyan","ogd-pdf-header2-key-emerald":"Emerald","ogd-pdf-header2-key-lime":"Lime","ogd-pdf-header2-key-orange":"Orange","ogd-pdf-header2-key-red":"Red","ogd-pdf-header2-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-header2-key-graphite"}},"ogd-pdf-header2-value-palette":{"ko":{"title":"헤더 2번 Value 색상","description":"첫 페이지 헤더의 2번 value segment 색상입니다. 예 `Graphite QA` 쪽 색상입니다.","options":{"ogd-pdf-header2-value-graphite":"Graphite","ogd-pdf-header2-value-slate":"Slate","ogd-pdf-header2-value-sky":"Sky","ogd-pdf-header2-value-teal":"Teal","ogd-pdf-header2-value-mint":"Mint","ogd-pdf-header2-value-violet":"Violet","ogd-pdf-header2-value-rose":"Rose","ogd-pdf-header2-value-amber":"Amber","ogd-pdf-header2-value-blue":"Blue","ogd-pdf-header2-value-indigo":"Indigo","ogd-pdf-header2-value-cyan":"Cyan","ogd-pdf-header2-value-emerald":"Emerald","ogd-pdf-header2-value-lime":"Lime","ogd-pdf-header2-value-orange":"Orange","ogd-pdf-header2-value-red":"Red","ogd-pdf-header2-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-header2-value-sky"},"en":{"title":"Header pair 2 value color","description":"Color of the second header value segment, such as `Graphite QA`.","options":{"ogd-pdf-header2-value-graphite":"Graphite","ogd-pdf-header2-value-slate":"Slate","ogd-pdf-header2-value-sky":"Sky","ogd-pdf-header2-value-teal":"Teal","ogd-pdf-header2-value-mint":"Mint","ogd-pdf-header2-value-violet":"Violet","ogd-pdf-header2-value-rose":"Rose","ogd-pdf-header2-value-amber":"Amber","ogd-pdf-header2-value-blue":"Blue","ogd-pdf-header2-value-indigo":"Indigo","ogd-pdf-header2-value-cyan":"Cyan","ogd-pdf-header2-value-emerald":"Emerald","ogd-pdf-header2-value-lime":"Lime","ogd-pdf-header2-value-orange":"Orange","ogd-pdf-header2-value-red":"Red","ogd-pdf-header2-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-header2-value-sky"}},"ogd-pdf-header-text-2":{"ko":{"title":"첫 페이지 헤더 2번 Key 문구","description":"2번 key segment입니다. 예 `Reviewed by`.","options":{},"default":""},"en":{"title":"First-page header pair 2 key text","description":"The second key segment. Example: `Reviewed by`.","options":{},"default":""}},"ogd-pdf-header-value-2":{"ko":{"title":"첫 페이지 헤더 2번 Value 문구","description":"2번 value segment입니다. 예 `Design QA` 또는 `2026-05-17`.","options":{},"default":""},"en":{"title":"First-page header pair 2 value text","description":"The second value segment. Example: `Design QA` or `2026-05-17`.","options":{},"default":""}},"ogd-pdf-header-position":{"ko":{"title":"첫 페이지 헤더 위치","description":"첫 페이지 헤더 라벨 위치를 선택합니다. Key/Value 구성에서는 두 segment가 같은 기준점에 붙어서 배치됩니다. 마지막 페이지 푸터는 안정성을 위해 중앙 하단으로 고정됩니다.","options":{"ogd-pdf-header-top-right":"우측 상단","ogd-pdf-header-top-center":"중앙 상단"},"default":"ogd-pdf-header-top-right"},"en":{"title":"First-page header position","description":"Choose the first-page header position. Key/value segments stay joined at the same anchor. The last-page footer remains fixed at bottom center for stability.","options":{"ogd-pdf-header-top-right":"Top right","ogd-pdf-header-top-center":"Top center"},"default":"ogd-pdf-header-top-right"}},"ogd-pdf-settings-footer":{"ko":{"title":"푸터 설정","description":"","options":{},"default":""},"en":{"title":"Footer settings","description":"","options":{},"default":""}},"ogd-pdf-footer-key-palette":{"ko":{"title":"푸터 Key 색상","description":"마지막 페이지 푸터의 왼쪽 key segment 색상입니다. 예 `Confidential` 쪽 색상입니다.","options":{"ogd-pdf-footer-key-graphite":"Graphite","ogd-pdf-footer-key-slate":"Slate","ogd-pdf-footer-key-sky":"Sky","ogd-pdf-footer-key-teal":"Teal","ogd-pdf-footer-key-mint":"Mint","ogd-pdf-footer-key-violet":"Violet","ogd-pdf-footer-key-rose":"Rose","ogd-pdf-footer-key-amber":"Amber","ogd-pdf-footer-key-blue":"Blue","ogd-pdf-footer-key-indigo":"Indigo","ogd-pdf-footer-key-cyan":"Cyan","ogd-pdf-footer-key-emerald":"Emerald","ogd-pdf-footer-key-lime":"Lime","ogd-pdf-footer-key-orange":"Orange","ogd-pdf-footer-key-red":"Red","ogd-pdf-footer-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-footer-key-graphite"},"en":{"title":"Footer key color","description":"Color of the left key segment in the last-page footer, such as `Confidential`.","options":{"ogd-pdf-footer-key-graphite":"Graphite","ogd-pdf-footer-key-slate":"Slate","ogd-pdf-footer-key-sky":"Sky","ogd-pdf-footer-key-teal":"Teal","ogd-pdf-footer-key-mint":"Mint","ogd-pdf-footer-key-violet":"Violet","ogd-pdf-footer-key-rose":"Rose","ogd-pdf-footer-key-amber":"Amber","ogd-pdf-footer-key-blue":"Blue","ogd-pdf-footer-key-indigo":"Indigo","ogd-pdf-footer-key-cyan":"Cyan","ogd-pdf-footer-key-emerald":"Emerald","ogd-pdf-footer-key-lime":"Lime","ogd-pdf-footer-key-orange":"Orange","ogd-pdf-footer-key-red":"Red","ogd-pdf-footer-key-fuchsia":"Fuchsia"},"default":"ogd-pdf-footer-key-graphite"}},"ogd-pdf-footer-value-palette":{"ko":{"title":"푸터 Value 색상","description":"마지막 페이지 푸터의 오른쪽 value segment 색상입니다. 예 `End of Document` 쪽 색상입니다.","options":{"ogd-pdf-footer-value-graphite":"Graphite","ogd-pdf-footer-value-slate":"Slate","ogd-pdf-footer-value-sky":"Sky","ogd-pdf-footer-value-teal":"Teal","ogd-pdf-footer-value-mint":"Mint","ogd-pdf-footer-value-violet":"Violet","ogd-pdf-footer-value-rose":"Rose","ogd-pdf-footer-value-amber":"Amber","ogd-pdf-footer-value-blue":"Blue","ogd-pdf-footer-value-indigo":"Indigo","ogd-pdf-footer-value-cyan":"Cyan","ogd-pdf-footer-value-emerald":"Emerald","ogd-pdf-footer-value-lime":"Lime","ogd-pdf-footer-value-orange":"Orange","ogd-pdf-footer-value-red":"Red","ogd-pdf-footer-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-footer-value-sky"},"en":{"title":"Footer value color","description":"Color of the right value segment in the last-page footer, such as `End of Document`.","options":{"ogd-pdf-footer-value-graphite":"Graphite","ogd-pdf-footer-value-slate":"Slate","ogd-pdf-footer-value-sky":"Sky","ogd-pdf-footer-value-teal":"Teal","ogd-pdf-footer-value-mint":"Mint","ogd-pdf-footer-value-violet":"Violet","ogd-pdf-footer-value-rose":"Rose","ogd-pdf-footer-value-amber":"Amber","ogd-pdf-footer-value-blue":"Blue","ogd-pdf-footer-value-indigo":"Indigo","ogd-pdf-footer-value-cyan":"Cyan","ogd-pdf-footer-value-emerald":"Emerald","ogd-pdf-footer-value-lime":"Lime","ogd-pdf-footer-value-orange":"Orange","ogd-pdf-footer-value-red":"Red","ogd-pdf-footer-value-fuchsia":"Fuchsia"},"default":"ogd-pdf-footer-value-sky"}},"ogd-pdf-footer-text":{"ko":{"title":"마지막 페이지 푸터 Key 문구","description":"단일 라벨에서는 전체 문구, Key/Value에서는 왼쪽 key입니다. 예 `Confidential`.","options":{},"default":""},"en":{"title":"Last-page footer key text","description":"The full phrase in single-label layout or the left key in key/value layout. Example: `Confidential`.","options":{},"default":""}},"ogd-pdf-footer-value":{"ko":{"title":"마지막 페이지 푸터 Value 문구","description":"Key/Value 구성에서 오른쪽 value로 표시됩니다. 예 `Internal Use Only` 또는 `End of Document`. 단일 라벨 구성에서는 사용하지 않습니다.","options":{},"default":""},"en":{"title":"Last-page footer value text","description":"The right value in key/value layout, such as `Internal Use Only` or `End of Document`. Not used by single-label layout.","options":{},"default":""}}};

const { MarkdownView, Notice, Plugin, moment } = require("obsidian");

const CODE_TITLE_CHROME = {
  en: {
    edit: "Edit code block title",
    saveError: "The code block title could not be saved because the block changed.",
  },
  ko: {
    edit: "코드 블록 제목 편집",
    saveError: "코드 블록이 변경되어 제목을 저장하지 못했습니다.",
  },
};

const CHROME = {
  en: {
    "Search Style Settings...": "Search Style Settings...",
    Import: "Import",
    Export: "Export",
    "No style settings found": "No style settings found",
    "Style settings configured by theme and plugin authors will show up here. You can": "Style settings configured by theme and plugin authors will show up here. You can",
    "Import style setting": "Import style setting",
    "Import an entire or partial configuration. Warning: this may override existing settings": "Import an entire or partial configuration. Warning: this may override existing settings",
    "Import from file": "Import from file",
    "Paste config here...": "Paste config here...",
    Save: "Save",
    "Copy to clipboard": "Copy to clipboard",
    Download: "Download",
    "Reset all settings to default": "Reset all settings to default",
    "Export settings": "Export settings"
  },
  ko: {
    "Search Style Settings...": "Style Settings 검색...",
    Import: "가져오기",
    Export: "내보내기",
    "No style settings found": "Style Settings 항목이 없습니다",
    "Style settings configured by theme and plugin authors will show up here. You can": "테마와 플러그인에서 제공하는 Style Settings 항목이 여기에 표시됩니다.",
    "Import style setting": "Style Settings 가져오기",
    "Import an entire or partial configuration. Warning: this may override existing settings": "전체 또는 일부 설정을 가져옵니다. 기존 설정을 덮어쓸 수 있습니다.",
    "Import from file": "파일에서 가져오기",
    "Paste config here...": "설정 JSON을 여기에 붙여넣으세요...",
    Save: "저장",
    "Copy to clipboard": "클립보드에 복사",
    Download: "다운로드",
    "Reset all settings to default": "모든 설정을 기본값으로 초기화",
    "Export settings": "설정 내보내기"
  }
};

function translateChromeText(source, locale) {
  const dictionary = CHROME[locale];
  if (dictionary[source]) return dictionary[source];
  if (source.startsWith("Export settings for: ")) {
    return locale === "ko" ? `설정 내보내기: ${source.slice(21)}` : source;
  }
  if (source.startsWith("Error importing style settings:")) {
    return locale === "ko" ? `Style Settings 가져오기 오류:${source.slice(31)}` : source;
  }
  return source;
}

function setText(element, text) {
  if (element && element.textContent !== text) element.textContent = text;
}

function localizedDescription(entry, locale) {
  const defaultValue = entry.default;
  if (defaultValue === undefined || defaultValue === "") return entry.description || "";
  const defaultLabel = entry.options?.[defaultValue] ?? defaultValue;
  const prefix = locale === "ko" ? "기본값:" : "Default:";
  return [entry.description, `${prefix} ${defaultLabel}`].filter(Boolean).join("\n");
}

function translateRow(row, locale) {
  const id = row.dataset.id;
  const entry = localizedEntry(catalog, id, locale);
  if (!entry) return;
  setText(row.querySelector(".setting-item-name"), entry.title);
  setText(row.querySelector(".setting-item-description"), localizedDescription(entry, locale));
  const select = row.querySelector("select");
  if (select && entry.options) {
    for (const option of select.options) {
      if (entry.options[option.value]) option.textContent = entry.options[option.value];
    }
  }
}

function translateChrome(root, locale) {
  const dictionary = CHROME[locale];
  root.querySelectorAll('input[placeholder], textarea[placeholder]').forEach((element) => {
    const source = element.dataset.ogdL10nSource || element.getAttribute("placeholder");
    element.dataset.ogdL10nSource = source;
    element.setAttribute("placeholder", translateChromeText(source, locale));
  });
  root.querySelectorAll('[aria-label], [data-tooltip-position]').forEach((element) => {
    for (const attribute of ["aria-label", "data-tooltip-position"]) {
      const value = element.getAttribute(attribute);
      if (value) element.setAttribute(attribute, translateChromeText(value, locale));
    }
  });
  root.querySelectorAll("a, button, label, .style-settings-empty-name, .style-settings-empty-desc, .setting-item-name, .setting-item-description").forEach((element) => {
    if (element.matches(".ogd-codeblock-title")) return;
    if (element.closest('[data-id^="ogd-"]')) return;
    const source = element.dataset.ogdL10nSource || element.textContent.trim();
    if (!source) return;
    element.dataset.ogdL10nSource = source;
    setText(element, translateChromeText(source, locale));
  });
}

function translateDocument(root = document) {
  const locale = localeFromClasses(document.body.classList, moment.locale());
  root.querySelectorAll('[data-id^="ogd-"]').forEach((row) => translateRow(row, locale));
  translateChrome(root, locale);
}

function codeTitleChrome() {
  return CODE_TITLE_CHROME[localeFromClasses(document.body.classList, moment.locale())];
}

function codeTitleKey(sourcePath, codeText, language) {
  const normalizedCode = String(codeText).replace(/\r\n/g, "\n").replace(/\n+$/, "");
  return `${sourcePath}\u0000${String(language).toLowerCase()}\u0000${normalizedCode}`;
}

function markdownViewForElement(app, element) {
  return app.workspace
    .getLeavesOfType("markdown")
    .map((leaf) => leaf.view)
    .find((view) => view instanceof MarkdownView && view.containerEl.contains(element));
}

function livePreviewLineInfo(app, lineElement) {
  const view = markdownViewForElement(app, lineElement);
  const editorView = view?.editor?.cm;
  if (!view || typeof editorView?.posAtDOM !== "function") return undefined;
  try {
    const position = view.editor.offsetToPos(editorView.posAtDOM(lineElement, 0));
    return { lineNumber: position.line, view };
  } catch (_error) {
    return undefined;
  }
}

function createTitleInput(container, value, onSave, onCancel) {
  const input = document.createElement("input");
  input.className = "ogd-codeblock-title-input";
  input.type = "text";
  input.value = value;
  input.setAttribute("aria-label", codeTitleChrome().edit);
  container.appendChild(input);
  let finished = false;
  const cancel = () => {
    if (finished) return;
    finished = true;
    input.remove();
    onCancel?.();
  };
  const save = async () => {
    if (finished) return;
    finished = true;
    input.disabled = true;
    try {
      await onSave(input.value.trim());
      input.remove();
    } catch (error) {
      input.remove();
      onCancel?.();
      console.error("Owen Graphite code block title save failed", error);
      new Notice(codeTitleChrome().saveError);
    }
  };
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      void save();
    } else if (event.key === "Escape") {
      event.preventDefault();
      cancel();
    }
  });
  input.addEventListener("blur", () => void save(), { once: true });
  requestAnimationFrame(() => {
    input.focus();
    input.select();
  });
  return input;
}

async function enhanceReadingCodeBlocks(plugin, root, context) {
  const codeBlocks = root.matches?.("pre") ? [root] : [...root.querySelectorAll("pre")];
  const file = plugin.app.vault.getAbstractFileByPath(context.sourcePath);
  if (!file || typeof file.extension !== "string") return;
  const source = await plugin.app.vault.read(file);
  for (const pre of codeBlocks) {
    if (pre.classList.contains("ogd-codeblock-title-ready")) continue;
    const codeText = pre.querySelector("code")?.textContent ?? pre.textContent;
    const renderedLanguage = [...pre.classList]
      .find((className) => className.startsWith("language-"))
      ?.slice("language-".length) ?? "";
    const opener = findFencedCodeBlockForCode(source, codeText, renderedLanguage);
    if (!opener) continue;
    const titleKey = codeTitleKey(context.sourcePath, codeText, opener.language);
    const trigger = document.createElement("button");
    trigger.className = "ogd-codeblock-title";
    trigger.type = "button";
    trigger.dataset.ogdCodeblockSource = context.sourcePath;
    if (plugin.codeTitleOverrides.has(titleKey)) {
      const override = plugin.codeTitleOverrides.get(titleKey);
      trigger.textContent = override;
      if (opener.hasTitle && opener.title === override) plugin.codeTitleOverrides.delete(titleKey);
    } else {
      trigger.textContent = opener.hasTitle ? opener.title : codeLanguageLabel(opener.language);
    }
    trigger.setAttribute("aria-label", codeTitleChrome().edit);
    trigger.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      if (pre.querySelector(".ogd-codeblock-title-input")) return;
      trigger.hidden = true;
      createTitleInput(
        pre,
        trigger.textContent,
        async (title) => {
          const currentFile = plugin.app.vault.getAbstractFileByPath(context.sourcePath);
          if (!currentFile || typeof currentFile.extension !== "string") throw new Error("Markdown file not found.");
          const hadOverride = plugin.codeTitleOverrides.has(titleKey);
          const previousOverride = plugin.codeTitleOverrides.get(titleKey);
          plugin.codeTitleOverrides.set(titleKey, title);
          try {
            await plugin.app.vault.process(currentFile, (source) => replaceFenceTitleForCode(source, codeText, title, opener.language));
          } catch (error) {
            if (hadOverride) plugin.codeTitleOverrides.set(titleKey, previousOverride);
            else plugin.codeTitleOverrides.delete(titleKey);
            throw error;
          }
          trigger.textContent = title;
          trigger.hidden = false;
        },
        () => {
          trigger.hidden = false;
        },
      );
    });
    pre.classList.add("ogd-codeblock-title-ready");
    pre.appendChild(trigger);
  }
}

function decorateLivePreviewCodeTitles(app, root = document) {
  root.querySelectorAll?.(".markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock-begin").forEach((lineElement) => {
    const trigger = lineElement.querySelector(".code-block-flair");
    const lineInfo = trigger ? livePreviewLineInfo(app, lineElement) : undefined;
    if (!trigger || !lineInfo) return;
    const opener = parseFenceLine(lineInfo.view.editor.getLine(lineInfo.lineNumber));
    if (!opener) return;
    const title = opener.hasTitle ? opener.title : codeLanguageLabel(opener.language);
    if (trigger.textContent !== title) trigger.textContent = title;
    trigger.classList.add("ogd-codeblock-title-trigger");
    trigger.setAttribute("aria-label", codeTitleChrome().edit);
    trigger.setAttribute("role", "button");
    trigger.tabIndex = 0;
  });
}

function editLivePreviewTitle(app, trigger) {
  const lineElement = trigger.closest(".cm-line.HyperMD-codeblock-begin");
  const lineInfo = lineElement ? livePreviewLineInfo(app, lineElement) : undefined;
  if (!lineElement || !lineInfo || lineElement.querySelector(".ogd-codeblock-title-input")) return;
  const expectedLine = lineInfo.view.editor.getLine(lineInfo.lineNumber);
  if (!parseFenceLine(expectedLine)) return;
  lineElement.classList.add("ogd-codeblock-title-editing");
  createTitleInput(
    lineElement,
    trigger.textContent,
    async (title) => {
      if (lineInfo.view.editor.getLine(lineInfo.lineNumber) !== expectedLine) throw new Error("Code block changed.");
      lineInfo.view.editor.setLine(lineInfo.lineNumber, updateFenceTitle(expectedLine, title));
      lineElement.classList.remove("ogd-codeblock-title-editing");
    },
    () => lineElement.classList.remove("ogd-codeblock-title-editing"),
  );
}

module.exports = class OwenGraphiteCompanion extends Plugin {
  onload() {
    this.codeTitleOverrides = new Map();
    let queued = false;
    const update = () => {
      if (queued) return;
      queued = true;
      requestAnimationFrame(() => {
        queued = false;
        translateDocument();
        decorateLivePreviewCodeTitles(this.app);
      });
    };
    this.observer = new MutationObserver(update);
    this.observer.observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ["class"] });
    this.registerMarkdownPostProcessor((root, context) => enhanceReadingCodeBlocks(this, root, context));
    const editFromEvent = (event) => {
      if (!(event.target instanceof Element)) return;
      const trigger = event.target.closest(".markdown-source-view.mod-cm6 .ogd-codeblock-title-trigger");
      if (!trigger) return;
      if (event.type === "keydown" && !["Enter", "F2"].includes(event.key)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      editLivePreviewTitle(this.app, trigger);
    };
    document.addEventListener("click", editFromEvent, true);
    document.addEventListener("keydown", editFromEvent, true);
    this.register(() => {
      document.removeEventListener("click", editFromEvent, true);
      document.removeEventListener("keydown", editFromEvent, true);
    });
    this.registerEvent(this.app.workspace.on("css-change", update));
    this.app.workspace.onLayoutReady(update);
  }

  onunload() {
    this.observer?.disconnect();
  }
};

module.exports.translateDocument = translateDocument;
module.exports.CHROME = CHROME;
module.exports.translateChromeText = translateChromeText;
module.exports.localizedDescription = localizedDescription;