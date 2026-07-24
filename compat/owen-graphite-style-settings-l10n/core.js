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

module.exports = {
  AUTO_CLASS,
  EN_CLASS,
  KO_CLASS,
  LANGUAGE_ID,
  codeLanguageLabel,
  findFencedCodeBlockForCode,
  findFencedCodeBlocks,
  findFenceOpeners,
  localeFromClasses,
  localizedEntry,
  parseFenceLine,
  replaceFenceTitleAtLine,
  replaceFenceTitleForCode,
  replaceFenceTitleNearLine,
  translateModel,
  updateFenceTitle,
};