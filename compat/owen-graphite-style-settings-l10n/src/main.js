"use strict";

const { Plugin, moment } = require("obsidian");
const catalog = require("./catalog.generated.json");
const { localeFromClasses, localizedEntry } = require("./core.js");

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

module.exports = class OwenGraphiteStyleSettingsLanguage extends Plugin {
  onload() {
    let queued = false;
    const update = () => {
      if (queued) return;
      queued = true;
      requestAnimationFrame(() => {
        queued = false;
        translateDocument();
      });
    };
    this.observer = new MutationObserver(update);
    this.observer.observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ["class"] });
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