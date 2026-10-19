"use strict";

const { Plugin, moment, setIcon } = require("obsidian");
const catalog = require("./catalog.generated.json");
const { localeFromClasses, localizedEntry, splitTooltipText } = require("./core.js");
const dropdowns = new WeakMap();
const dropdownControllers = new Set();
let dropdownId = 0;

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
  const document = element.ownerDocument;
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
  enhanceDropdown(select, entry.title);
}

function enhanceDropdown(select, label) {
  const existing = dropdowns.get(select);
  if (existing) {
    existing.refresh(label);
    return;
  }
  if (select.multiple) return;
  const document = select.ownerDocument;
  const view = document.defaultView;
  if (!view?.HTMLElement.prototype.showPopover) return;
  const events = new view.AbortController();
  const listenerOptions = { signal: events.signal };
  const originalAttributes = new Map(
    ["aria-haspopup", "aria-controls", "aria-expanded", "aria-activedescendant"]
      .map(name => [name, select.getAttribute(name)]),
  );

  const id = `ogd-settings-dropdown-${++dropdownId}`;
  const menu = document.createElement("div");
  menu.id = id;
  menu.className = "owen-settings-dropdown-popover";
  menu.dataset.owenGraphiteDropdown = "true";
  menu.setAttribute("popover", "manual");
  menu.setAttribute("role", "listbox");
  if (label) menu.setAttribute("aria-label", label);

  let activeIndex = select.selectedIndex;
  let rows = [];
  let typeahead = "";
  let typeaheadTimer = 0;
  let listeningForPosition = false;
  let listeningForDismissal = false;
  const isOpen = () => menu.matches(":popover-open");
  const options = () => Array.from(select.options);
  const setActive = (index) => {
    const currentOptions = options();
    if (!currentOptions.length) {
      select.removeAttribute("aria-activedescendant");
      return;
    }
    let candidate = Number.isInteger(index) && index >= 0 && index < currentOptions.length
      ? index
      : currentOptions.findIndex((option) => !option.disabled);
    if (candidate < 0) {
      rows.forEach((row) => row.classList.remove("is-active"));
      select.removeAttribute("aria-activedescendant");
      return;
    }
    for (let offset = 0; offset < currentOptions.length && currentOptions[candidate]?.disabled; offset += 1) {
      candidate = (candidate + 1) % currentOptions.length;
    }
    if (currentOptions[candidate]?.disabled) return;
    activeIndex = candidate;
    rows.forEach((row, rowIndex) => row.classList.toggle("is-active", rowIndex === activeIndex));
    const row = rows[activeIndex];
    if (row) {
      select.setAttribute("aria-activedescendant", row.id);
      row.scrollIntoView({ block: "nearest" });
    }
  };
  const refresh = (nextLabel = label) => {
    label = nextLabel;
    if (label) menu.setAttribute("aria-label", label);
    const currentOptions = options();
    if (currentOptions.length !== rows.length) {
      rows = currentOptions.map((_option, index) => {
        const row = document.createElement("div");
        row.id = `${id}-option-${index}`;
        row.className = "owen-settings-dropdown-option";
        row.setAttribute("role", "option");
        row.addEventListener("pointerdown", (event) => event.preventDefault());
        row.addEventListener("click", (event) => {
          event.preventDefault();
          if (!options()[index]?.disabled) commit(index);
        });
        const text = document.createElement("span");
        text.className = "owen-settings-dropdown-label";
        const check = document.createElement("span");
        check.className = "owen-settings-dropdown-check";
        check.setAttribute("aria-hidden", "true");
        setIcon(check, "check");
        row.append(text, check);
        return row;
      });
      menu.replaceChildren(...rows);
    }
    currentOptions.forEach((option, index) => {
      const row = rows[index];
      const text = row.querySelector(".owen-settings-dropdown-label");
      const optionLabel = option.label || option.textContent || "";
      if (text && text.textContent !== optionLabel) text.textContent = optionLabel;
      row.classList.toggle("is-selected", option.selected);
      row.classList.toggle("is-disabled", option.disabled);
      row.setAttribute("aria-selected", String(option.selected));
      row.setAttribute("aria-disabled", String(option.disabled));
    });
    if (isOpen()) setActive(activeIndex);
  };
  const updatePosition = () => {
    const rect = select.getBoundingClientRect();
    const width = Math.min(Math.max(180, rect.width), view.innerWidth - 16);
    const desiredHeight = Math.min(options().length * 44 + 12, 320);
    const below = view.innerHeight - rect.bottom - 8;
    const above = rect.top - 8;
    const openBelow = below >= Math.min(desiredHeight, 132) || below >= above;
    const available = Math.max(48, Math.min(desiredHeight, openBelow ? below : above));
    menu.style.width = `${width}px`;
    menu.style.left = `${Math.max(8, Math.min(rect.left, view.innerWidth - width - 8))}px`;
    menu.style.maxHeight = `${available}px`;
    menu.style.top = openBelow ? `${rect.bottom + 4}px` : `${Math.max(8, rect.top - available - 4)}px`;
  };
  const close = () => {
    if (isOpen()) menu.hidePopover();
    select.setAttribute("aria-expanded", "false");
    select.removeAttribute("aria-activedescendant");
    view.clearTimeout(typeaheadTimer);
    typeahead = "";
    if (listeningForDismissal) {
      document.removeEventListener("pointerdown", dismissOutside);
      listeningForDismissal = false;
    }
    if (listeningForPosition) {
      view.removeEventListener("resize", updatePosition);
      document.removeEventListener("scroll", updatePosition, true);
      listeningForPosition = false;
    }
  };
  const dismissOutside = (event) => {
    const path = event.composedPath();
    if (!path.includes(select) && !path.includes(menu)) close();
  };
  const open = () => {
    if (select.disabled || isOpen()) return;
    activeIndex = select.selectedIndex;
    if (options()[activeIndex]?.disabled) activeIndex = options().findIndex((option) => !option.disabled);
    refresh();
    updatePosition();
    menu.showPopover();
    select.setAttribute("aria-expanded", "true");
    setActive(activeIndex);
    if (!listeningForDismissal) {
      document.addEventListener("pointerdown", dismissOutside);
      listeningForDismissal = true;
    }
    if (!listeningForPosition) {
      view.addEventListener("resize", updatePosition);
      document.addEventListener("scroll", updatePosition, true);
      listeningForPosition = true;
    }
  };
  function commit(index) {
    const option = options()[index];
    if (!option || option.disabled) return;
    if (select.selectedIndex !== index) {
      select.selectedIndex = index;
      select.dispatchEvent(new view.Event("input", { bubbles: true }));
      select.dispatchEvent(new view.Event("change", { bubbles: true }));
    }
    close();
    select.focus();
  }
  const moveActive = (direction) => {
    const currentOptions = options();
    if (!currentOptions.length) return;
    let index = activeIndex;
    for (let offset = 0; offset < currentOptions.length; offset += 1) {
      index = (index + direction + currentOptions.length) % currentOptions.length;
      if (!currentOptions[index].disabled) {
        setActive(index);
        return;
      }
    }
  };

  refresh();
  select.setAttribute("aria-haspopup", "listbox");
  select.setAttribute("aria-controls", id);
  select.setAttribute("aria-expanded", "false");
  select.insertAdjacentElement("afterend", menu);
  menu.addEventListener("toggle", () => {
    if (!isOpen()) close();
  }, listenerOptions);
  select.addEventListener("change", () => refresh(), listenerOptions);
  select.addEventListener("pointerdown", (event) => {
    if (!event.isPrimary || (event.button !== 0 && event.pointerType !== "touch")) return;
    event.preventDefault();
    select.focus();
    if (isOpen()) close();
    else open();
  }, listenerOptions);
  select.addEventListener("click", (event) => event.preventDefault(), listenerOptions);
  select.addEventListener("keydown", (event) => {
    if (!isOpen()) {
      if ((event.altKey && event.key === "ArrowDown") || event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        open();
      }
      return;
    }
    if (event.key === "Escape" || (event.altKey && event.key === "ArrowUp")) {
      event.preventDefault();
      close();
    } else if (event.key === "Tab") close();
    else if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      commit(activeIndex);
    } else if (["ArrowDown", "ArrowUp", "Home", "End", "PageDown", "PageUp"].includes(event.key)) {
      event.preventDefault();
      if (event.key === "Home") setActive(0);
      else if (event.key === "End") setActive(options().length - 1);
      else moveActive((event.key === "ArrowUp" || event.key === "PageUp" ? -1 : 1) * (event.key.startsWith("Page") ? 5 : 1));
    } else if (event.key.length === 1 && !event.altKey && !event.ctrlKey && !event.metaKey) {
      typeahead = `${typeahead}${event.key}`.toLocaleLowerCase();
      view.clearTimeout(typeaheadTimer);
      typeaheadTimer = view.setTimeout(() => { typeahead = ""; }, 700);
      const match = options().findIndex((option) => !option.disabled && (option.label || option.textContent || "").toLocaleLowerCase().startsWith(typeahead));
      if (match >= 0) {
        event.preventDefault();
        setActive(match);
      }
    }
  }, listenerOptions);

  const controller = {
    select,
    refresh,
    destroy() {
      close();
      events.abort();
      menu.remove();
      for (const [name, value] of originalAttributes) {
        if (value === null) select.removeAttribute(name);
        else select.setAttribute(name, value);
      }
      dropdowns.delete(select);
      dropdownControllers.delete(controller);
    },
  };
  dropdowns.set(select, controller);
  dropdownControllers.add(controller);
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
  const document = tooltip.ownerDocument;
  const textNodes = Array.from(tooltip.childNodes).filter((node) => node.nodeType === 3);
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
  const document = root.nodeType === 9 ? root : root.ownerDocument;
  if (document.body.classList.contains("is-mobile")) return;
  if (root.nodeType === 1 && root.matches(".tooltip")) structureTooltip(root);
  root.querySelectorAll(".tooltip").forEach(structureTooltip);
}

function enhanceSettings(root) {
  root.querySelectorAll(".modal.mod-settings .vertical-tab-content").forEach(container => {
    if (container.classList.contains("owen-settings-design")) return;
    const document = container.ownerDocument;
    const navigation = container.closest(".mod-settings").querySelector(".vertical-tab-nav-item.is-active");
    const title = navigation?.textContent.trim();
    if (!title) return;
    const tones = { about: "sky", appearance: "violet", interface: "sky", editor: "mint", file: "teal", hotkeys: "amber", keychain: "amber", plugins: "violet", "community-plugins": "teal" };
    const addHeading = parent => {
      const native = parent.querySelector(":scope > .setting-item-heading:not(.ogd-settings-generated-heading), :scope > h1, :scope > h2, :scope > h3");
      let heading = parent.querySelector(":scope > .ogd-settings-generated-heading");
      if (native) {
        heading?.remove();
        return;
      }
      if (!heading) {
        heading = document.createElement("div");
        heading.className = "setting-item setting-item-heading owen-settings-heading ogd-settings-generated-heading";
        heading.setAttribute("role", "heading");
        heading.setAttribute("aria-level", "2");
        heading.dataset.owenTone = tones[navigation.dataset.settingId] || "neutral";
        const glyph = document.createElement("span");
        glyph.className = "ogd-settings-section-glyph";
        glyph.setAttribute("aria-hidden", "true");
        const icon = navigation.querySelector("svg");
        if (icon) glyph.append(icon.cloneNode(true));
        else setIcon(glyph, "settings-2");
        const info = document.createElement("div");
        info.className = "setting-item-info";
        const name = document.createElement("div");
        name.className = "setting-item-name";
        info.append(name);
        heading.append(glyph, info);
        parent.prepend(heading);
      }
      setText(heading.querySelector(".setting-item-name"), title);
    };
    container.querySelectorAll(":scope > .setting-group").forEach(addHeading);
    const firstRow = container.querySelector(":scope > .setting-item");
    if (firstRow && (!firstRow.classList.contains("setting-item-heading") || firstRow.classList.contains("ogd-settings-generated-heading"))) addHeading(container);
    container.querySelectorAll("select").forEach(select => {
      if (select.hasAttribute("aria-controls") && !dropdowns.has(select)) return;
      const label = select.closest(".setting-item")?.querySelector(".setting-item-name")?.textContent.trim()
        || select.getAttribute("aria-label") || title;
      enhanceDropdown(select, label);
    });
  });
}

function translateDocument(root = document) {
  const owner = root.nodeType === 9 ? root : root.ownerDocument;
  const locale = localeFromClasses(owner.body.classList, moment.locale());
  root.querySelectorAll('[data-id^="ogd-"]').forEach((row) => translateRow(row, locale));
  translateChrome(root, locale);
  structureTooltips(root);
  enhanceSettings(root);
}

module.exports = class OwenGraphiteLocalizationBridge extends Plugin {
  onload() {
    this.documents = new Map();
    let queued = false;
    let unloaded = false;
    let settingsElement;
    const settingsObserver = new MutationObserver(() => update());
    const watchDocument = document => {
      if (!document?.body || !document.defaultView || this.documents.has(document)) return;
      const observer = new document.defaultView.MutationObserver(mutations => {
        if (mutations.some(mutation => mutation.type === "childList" || mutation.target === document.body)) update();
      });
      observer.observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ["class"] });
      this.documents.set(document, observer);
      this.registerDomEvent(document.defaultView, "unload", () => {
        observer.disconnect();
        this.documents.delete(document);
      });
    };
    const update = () => {
      if (queued) return;
      queued = true;
      queueMicrotask(() => {
        if (unloaded) return;
        queued = false;
        watchDocument(document);
        if (typeof activeDocument !== "undefined") watchDocument(activeDocument);
        // Native settings popouts do not emit workspace "window-open".
        const modal = this.app.setting?.modalEl;
        if (modal && modal !== settingsElement) {
          settingsObserver.disconnect();
          settingsObserver.observe(modal, { subtree: true, childList: true });
          settingsElement = modal;
        }
        watchDocument(modal?.ownerDocument);
        for (const [owner, observer] of this.documents) {
          if (!owner.defaultView || owner.defaultView.closed) {
            observer.disconnect();
            this.documents.delete(owner);
          } else translateDocument(owner);
        }
        for (const controller of dropdownControllers) {
          const view = controller.select.ownerDocument.defaultView;
          if (!controller.select.isConnected || !view || view.closed) controller.destroy();
        }
      });
    };
    this.register(() => { unloaded = true; });
    this.register(() => settingsObserver.disconnect());
    watchDocument(document);
    this.registerDomEvent(window, "focus", update);
    this.registerDomEvent(window, "blur", update);
    this.registerEvent(this.app.workspace.on("window-open", (_container, window) => {
      watchDocument(window.document);
      update();
    }));
    this.registerEvent(this.app.workspace.on("css-change", update));
    this.app.workspace.onLayoutReady(update);
  }

  onunload() {
    for (const [document, observer] of this.documents) {
      observer.disconnect();
      document.querySelectorAll(".ogd-settings-generated-heading").forEach(heading => heading.remove());
    }
    this.documents.clear();
    for (const controller of dropdownControllers) controller.destroy();
  }
};

module.exports.translateDocument = translateDocument;
module.exports.translateChromeText = translateChromeText;
module.exports.structureTooltip = structureTooltip;
module.exports.enhanceSettings = enhanceSettings;