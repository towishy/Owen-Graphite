"use strict";

const LANGUAGE_ID = "ogd-style-settings-language";
const AUTO_CLASS = "ogd-language-auto";
const EN_CLASS = "ogd-language-en";
const KO_CLASS = "ogd-language-ko";

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

module.exports = { AUTO_CLASS, EN_CLASS, KO_CLASS, LANGUAGE_ID, localeFromClasses, localizedEntry, translateModel };