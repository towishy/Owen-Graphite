#!/usr/bin/env python3
"""Small CSS scanning helpers shared by Owen Graphite audits."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterator

COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
BLOCK_RE = re.compile(r"(?P<selectors>[^{}]+)\{(?P<body>[^{}]*)\}", re.DOTALL)


@dataclass(frozen=True)
class CssRuleBlock:
    selectors: str
    body: str
    start: int
    end: int
    line: int

    @property
    def normalized_selectors(self) -> str:
        return " ".join(self.selectors.split())

    def declarations(self) -> Iterator[tuple[str, str]]:
        for declaration in self.body.split(";"):
            prop, _, value = declaration.partition(":")
            prop = prop.strip()
            if prop:
                yield prop, value.strip()


def strip_comments(text: str) -> str:
    return COMMENT_RE.sub(lambda match: "".join("\n" if char == "\n" else " " for char in match.group(0)), text)


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def iter_comments(text: str) -> Iterator[re.Match[str]]:
    yield from COMMENT_RE.finditer(text)


def iter_rule_blocks(text: str, start: int = 0, end: int | None = None) -> Iterator[CssRuleBlock]:
    searchable = strip_comments(text)
    for match in BLOCK_RE.finditer(searchable, start, len(searchable) if end is None else end):
        yield CssRuleBlock(
            selectors=match.group("selectors"),
            body=match.group("body"),
            start=match.start(),
            end=match.end(),
            line=line_for_offset(searchable, match.start()),
        )
