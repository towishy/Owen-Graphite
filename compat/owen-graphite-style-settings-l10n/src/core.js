"use strict";

const AUTO_CLASS = "ogd-language-auto";
const EN_CLASS = "ogd-language-en";
const KO_CLASS = "ogd-language-ko";

function localeFromClasses(classList, obsidianLocale = "en") {
  if (classList.contains(KO_CLASS)) return "ko";
  if (classList.contains(EN_CLASS)) return "en";
  return /^ko(?:[-_]|$)/i.test(obsidianLocale) ? "ko" : "en";
}

function localizedEntry(catalog, id, locale) {
  return catalog[id]?.[locale];
}

function splitTooltipText(text) {
  const normalized = String(text ?? "").replace(/\r\n?/g, "\n").trim();
  const separator = normalized.match(/\n[ \t]*\n/);
  if (!separator || separator.index === undefined) return null;
  const title = normalized.slice(0, separator.index).trim();
  const meta = normalized.slice(separator.index + separator[0].length).trim();
  return title && meta ? { title, meta } : null;
}

module.exports = {
  AUTO_CLASS,
  EN_CLASS,
  KO_CLASS,
  localeFromClasses,
  localizedEntry,
  splitTooltipText,
};