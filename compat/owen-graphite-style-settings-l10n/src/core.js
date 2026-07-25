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

module.exports = {
  AUTO_CLASS,
  EN_CLASS,
  KO_CLASS,
  localeFromClasses,
  localizedEntry,
};