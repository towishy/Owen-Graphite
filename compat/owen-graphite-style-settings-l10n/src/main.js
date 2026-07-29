"use strict";

const { Plugin, moment } = require("obsidian");
const catalog = require("./catalog.generated.json");
const { localeFromClasses, localizedEntry, splitTooltipText } = require("./core.js");

const CHROME = {
  en: {
    "Search Style Settings...": "Search Style Settings...",
    Import: "Import",
    Export: "Export",
    "No style settings found": "No style settings found",
    "Import style setting": "Import style setting",
    "Import from file": "Import from file",
    "Paste config here...": "Paste config here...",
    Save: "Save",
    "Copy to clipboard": "Copy to clipboard",
    Download: "Download",
    "Reset all settings to default": "Reset all settings to default",
    "Export settings": "Export settings",
  },
  ko: {
    "Search Style Settings...": "Style Settings 검색...",
    Import: "가져오기",
    Export: "내보내기",
    "No style settings found": "Style Settings 항목이 없습니다",
    "Import style setting": "Style Settings 가져오기",
    "Import from file": "파일에서 가져오기",
    "Paste config here...": "설정 JSON을 여기에 붙여넣으세요...",
    Save: "저장",
    "Copy to clipboard": "클립보드에 복사",
    Download: "다운로드",
    "Reset all settings to default": "모든 설정을 기본값으로 초기화",
    "Export settings": "설정 내보내기",
  },
};

function translateChromeText(source, locale) {
  const translated = CHROME[locale][source];
  if (translated) return translated;
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

function renderDescription(element, entry, locale) {
  if (!element || element.dataset.ogdL10nLocale === locale) return;
  element.dataset.ogdL10nLocale = locale;
  element.replaceChildren();
  if (entry.description) element.append(document.createTextNode(entry.description));
  if (entry.default === undefined || entry.default === "") return;
  const defaultLabel = entry.options?.[entry.default] ?? entry.default;
  const small = document.createElement("small");
  const strong = document.createElement("strong");
  strong.textContent = locale === "ko" ? "기본값: " : "Default: ";
  small.append(strong, document.createTextNode(defaultLabel));
  element.append(small);
}

function translateRow(row, locale) {
  const entry = localizedEntry(catalog, row.dataset.id, locale);
  if (!entry) return;
  setText(row.querySelector(".setting-item-name"), entry.title);
  renderDescription(row.querySelector(".setting-item-description"), entry, locale);
  const select = row.querySelector("select");
  if (!select || !entry.options) return;
  for (const option of select.options) {
    setText(option, entry.options[option.value] ?? option.textContent);
  }
}

function translateChrome(root, locale) {
  root.querySelectorAll('input[placeholder], textarea[placeholder]').forEach((element) => {
    const source = element.dataset.ogdL10nSource || element.getAttribute("placeholder");
    element.dataset.ogdL10nSource = source;
    element.setAttribute("placeholder", translateChromeText(source, locale));
  });
  root.querySelectorAll("a, button, label, .style-settings-empty-name, .style-settings-empty-desc").forEach((element) => {
    if (element.closest('[data-id^="ogd-"]')) return;
    const source = element.dataset.ogdL10nSource || element.textContent.trim();
    if (!source) return;
    element.dataset.ogdL10nSource = source;
    setText(element, translateChromeText(source, locale));
  });
}

function structureTooltip(tooltip) {
  if (tooltip.dataset.ogdStructuredTooltip === "true") return;
  const textNodes = Array.from(tooltip.childNodes).filter((node) => node.nodeType === Node.TEXT_NODE);
  const parsed = splitTooltipText(textNodes.map((node) => node.textContent).join(""));
  if (!parsed || textNodes.length === 0) return;

  const title = document.createElement("span");
  title.className = "ogd-tooltip-title";
  title.textContent = parsed.title;
  const meta = document.createElement("span");
  meta.className = "ogd-tooltip-meta";
  meta.textContent = parsed.meta;
  textNodes[0].replaceWith(title, meta);
  textNodes.slice(1).forEach((node) => node.remove());
  tooltip.dataset.ogdStructuredTooltip = "true";
}

function structureTooltips(root) {
  if (document.body.classList.contains("is-mobile")) return;
  if (root instanceof Element && root.matches(".tooltip")) structureTooltip(root);
  root.querySelectorAll(".tooltip").forEach(structureTooltip);
}

function translateDocument(root = document) {
  const locale = localeFromClasses(document.body.classList, moment.locale());
  root.querySelectorAll('[data-id^="ogd-"]').forEach((row) => translateRow(row, locale));
  translateChrome(root, locale);
  structureTooltips(root);
}

module.exports = class OwenGraphiteLocalizationBridge extends Plugin {
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
    this.observer.observe(document.body, {
      subtree: true,
      childList: true,
      attributes: true,
      attributeFilter: ["class"],
    });
    this.registerEvent(this.app.workspace.on("css-change", update));
    this.app.workspace.onLayoutReady(update);
  }

  onunload() {
    this.observer?.disconnect();
  }
};

module.exports.translateDocument = translateDocument;
module.exports.translateChromeText = translateChromeText;
module.exports.structureTooltip = structureTooltip;