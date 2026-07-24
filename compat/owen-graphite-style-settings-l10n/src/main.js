"use strict";

const { MarkdownView, Notice, Plugin, moment } = require("obsidian");
const catalog = require("./catalog.generated.json");
const {
  codeLanguageLabel,
  findFencedCodeBlockForCode,
  localeFromClasses,
  localizedEntry,
  parseFenceLine,
  replaceFenceTitleForCode,
  updateFenceTitle,
} = require("./core.js");

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

const HEADING_PREVIEW_COPY = {
  en: {
    label: "Selected report heading template preview",
    h1: "Report title",
    h2: "Section heading",
    h3: "Detail heading",
  },
  ko: {
    label: "선택한 보고서 제목 템플릿 미리보기",
    h1: "보고서 제목",
    h2: "섹션 제목",
    h3: "세부 항목",
  },
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

function ensureHeadingTemplatePreview(row, locale) {
  const copy = HEADING_PREVIEW_COPY[locale];
  let preview = row.querySelector(":scope > .ogd-heading-template-preview");
  if (!preview) {
    preview = document.createElement("div");
    preview.className = "ogd-heading-template-preview";
    preview.setAttribute("role", "img");
    for (const level of ["h1", "h2", "h3"]) {
      const line = document.createElement("span");
      line.className = `ogd-heading-template-preview-${level}`;
      preview.appendChild(line);
    }
    row.appendChild(preview);
  }
  preview.setAttribute("aria-label", copy.label);
  for (const level of ["h1", "h2", "h3"]) {
    setText(preview.querySelector(`.ogd-heading-template-preview-${level}`), copy[level]);
  }
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
  if (id === "ogd-heading-template") ensureHeadingTemplatePreview(row, locale);
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