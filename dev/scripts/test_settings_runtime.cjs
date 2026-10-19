"use strict";

// Run only against an explicitly selected disposable Obsidian vault.
const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const path = require("node:path");
const [playwrightPath, endpoint, expectedVault, evidenceDirectory] = process.argv.slice(2);
assert(playwrightPath && endpoint && expectedVault && evidenceDirectory,
  "Usage: node test_settings_runtime.cjs <playwright-core> <CDP URL> <disposable vault> <evidence directory>");
const { chromium } = require(playwrightPath);
const companion = "owen-graphite-style-settings-l10n";

(async () => {
  const browser = await chromium.connectOverCDP(endpoint);
  try {
    const context = browser.contexts()[0];
    const main = context.pages().find(page => page.url().startsWith("app://obsidian.md"));
    assert(main, "Obsidian renderer was not found");
    const vault = await main.evaluate(() => app.vault.adapter.basePath);
    assert.equal(path.resolve(vault).toLowerCase(), path.resolve(expectedVault).toLowerCase(),
      "Refusing to modify an unexpected vault");
    await fs.cp(path.resolve(__dirname, "..", "fixtures", "settings-regression-plugin"),
      path.join(expectedVault, ".obsidian", "plugins", "graphite-settings-fixture"), { recursive: true });
    await fs.mkdir(evidenceDirectory, { recursive: true });
    await main.evaluate(async id => {
      await app.plugins.loadManifests();
      await app.plugins.setEnable(true);
      await app.plugins.enablePlugin("graphite-settings-fixture");
      await app.plugins.enablePlugin(id);
      app.setting.open();
    }, companion);
    await main.waitForTimeout(500);
    let settings = context.pages().find(page => page.url() === "about:blank");
    assert(settings, "Native settings popout was not found");
    await main.evaluate(async () => {
      const plugin = app.plugins.plugins["owen-editor"];
      if (!plugin) throw new Error("Owen Editor is required for toolbar regression checks");
      const file = app.vault.getAbstractFileByPath("settings-toolbar-regression.md")
        ?? await app.vault.create("settings-toolbar-regression.md", "# Toolbar regression\n\nMarkdown document content.");
      const leaf = app.workspace.getLeaf(false);
      await leaf.openFile(file);
      plugin.refreshFloatingToolbar();
      plugin.refreshSelectionToolbar();
      if (!plugin.toolbarEl?.isShown()) throw new Error("Markdown document toolbar is missing");
      if (plugin.toolbarEl.ownerDocument !== leaf.view.contentEl.ownerDocument)
        throw new Error("Toolbar does not belong to the Markdown document window");
      await leaf.setViewState({ type: "empty" });
      plugin.updateToolbarContentOffset();
      plugin.updateSelectionToolbar();
      if (plugin.toolbarEl?.isShown()) throw new Error("Toolbar remains visible in a non-Markdown view");
      if (plugin.toolbarBody?.classList.contains("owen-editor-toolbar-offset"))
        throw new Error("Non-Markdown view retains toolbar clearance");
      await leaf.openFile(file);
      plugin.updateToolbarContentOffset();
      if (!plugin.toolbarEl?.isShown()) throw new Error("Returning to Markdown did not restore the toolbar");
    });
    assert.equal(await settings.locator(".owen-editor-glass-toolbar, .owen-editor-selection-toolbar").count(), 0,
      "Settings must never contain document editing toolbars");
    const choose = async id => {
      const search = settings.locator(".vertical-tab-header .setting-search-container input");
      if (await search.inputValue()) await search.fill("");
      await settings.locator(`.vertical-tab-nav-item[data-setting-id="${id}"]`).click();
      await settings.waitForTimeout(80);
    };
    const setMode = async mode => {
      await choose("appearance");
      await settings.locator('select:has(option[value="moonstone"])').selectOption(mode === "dark" ? "obsidian" : "moonstone");
      await settings.locator(`body.theme-${mode}`).waitFor();
    };
    const capture = name => settings.screenshot({ path: path.join(evidenceDirectory, `${name}.png`), scale: "css" });
    const cdp = await context.newCDPSession(settings);
    await cdp.send("DOM.enable");
    const flatten = node => [node, ...(node.children || []).flatMap(flatten), ...(node.shadowRoots || []).flatMap(flatten)];
    const attribute = (node, name) => {
      const index = node.attributes?.indexOf(name) ?? -1;
      return index >= 0 ? node.attributes[index + 1] : null;
    };
    const checkSliderGeometry = async () => {
      const { root } = await cdp.send("DOM.getDocument", { depth: -1, pierce: true });
      for (const input of flatten(root).filter(node => node.nodeName === "INPUT" && attribute(node, "type") === "range")) {
        const { object } = await cdp.send("DOM.resolveNode", { nodeId: input.nodeId });
        const { result } = await cdp.send("Runtime.callFunctionOn", {
          objectId: object.objectId,
          functionDeclaration: "function() { return this.getBoundingClientRect().height > 0; }",
          returnByValue: true,
        });
        if (!result.value) continue;
        const nodes = flatten(input);
        const track = nodes.find(node => attribute(node, "id") === "track");
        const thumb = nodes.find(node => attribute(node, "id") === "thumb");
        assert(track && thumb, "Chromium native slider geometry is unavailable");
        const trackBox = (await cdp.send("DOM.getBoxModel", { nodeId: track.nodeId })).model.border;
        const thumbBox = (await cdp.send("DOM.getBoxModel", { nodeId: thumb.nodeId })).model.border;
        assert(Math.abs(trackBox[5] - trackBox[1] - 4) < 0.6, "Slider track must be 4px");
        assert(Math.abs(thumbBox[5] - thumbBox[1] - 16) < 0.6, "Slider thumb must be 16px");
        assert(Math.abs((trackBox[1] + trackBox[5] - thumbBox[1] - thumbBox[5]) / 2) < 0.6,
          "Slider thumb must be vertically centered on its track");
        await cdp.send("Runtime.releaseObject", { objectId: object.objectId });
      }
    };
    const inventory = [];
    const ids = await settings.locator(".vertical-tab-nav-item[data-setting-id]").evaluateAll(
      elements => elements.map(element => element.dataset.settingId),
    );
    for (const mode of ["light", "dark"]) {
      await setMode(mode);
      for (const id of ids) {
        await choose(id);
        const result = await settings.locator(".vertical-tab-content").evaluate(root => ({
          custom: root.classList.contains("owen-settings-design"),
          groups: [...root.querySelectorAll(":scope > .setting-group")].map(group => ({
            border: getComputedStyle(group).borderStyle,
            radius: getComputedStyle(group).borderRadius,
            headings: group.querySelectorAll(".setting-item-heading, .owen-mermaid-settings-section").length,
          })),
          sliders: [...root.querySelectorAll('input[type="range"]')].filter(element => element.getBoundingClientRect().height).map(element => ({
            background: getComputedStyle(element).backgroundColor,
            image: getComputedStyle(element).backgroundImage,
            height: element.getBoundingClientRect().height,
          })),
          searches: [...document.querySelectorAll('.search-input-container input[type="search"]')].map(element => ({
            padding: parseFloat(getComputedStyle(element).paddingInlineStart),
            height: element.getBoundingClientRect().height,
          })),
          overflow: root.scrollWidth - root.clientWidth,
          alignment: [...document.querySelectorAll(".vertical-tab-nav-item")].filter(element => element.getBoundingClientRect().height).map(element => {
            const icon = element.querySelector(".vertical-tab-nav-item-icon");
            const title = element.querySelector(".vertical-tab-nav-item-title");
            if (!icon || !title) return 0;
            const a = icon.getBoundingClientRect(), b = title.getBoundingClientRect();
            return Math.abs(a.y + a.height / 2 - b.y - b.height / 2);
          }),
          selected: [...root.querySelectorAll(".setting-group-filter.is-active, button.mod-cta:not(.mod-warning):not(.mod-destructive)")].filter(element => element.getBoundingClientRect().height && !element.disabled).map(element => ({
            text: element.textContent,
            color: getComputedStyle(element).color,
            background: getComputedStyle(element).backgroundColor,
          })),
        }));
        for (const group of result.groups) {
          assert.equal(group.border, "solid", `${mode}/${id}: missing card border`);
          assert.equal(group.radius, "8px", `${mode}/${id}: wrong card radius`);
          if (result.custom) assert(group.headings >= 1, `${mode}/${id}: missing custom section heading`);
          else assert.equal(group.headings, 1, `${mode}/${id}: missing or duplicate section heading`);
        }
        for (const slider of result.sliders) {
          assert.equal(slider.background, "rgba(0, 0, 0, 0)", `${mode}/${id}: rectangular slider background`);
          assert.equal(slider.image, "none", `${mode}/${id}: slider fill must belong to track, not hit area`);
          assert(slider.height >= 43.9, `${mode}/${id}: slider hit area is too small`);
        }
        for (const search of result.searches) {
          assert(search.padding >= 36, `${mode}/${id}: search icon overlaps text`);
          assert(search.height >= 43.9, `${mode}/${id}: search hit area is too small`);
        }
        assert(result.alignment.every(delta => delta < 1), `${mode}/${id}: sidebar title is not vertically centered`);
        const luminance = color => {
          const channels = color.match(/[\d.]+/g).slice(0, 3).map(Number).map(value => {
            const linear = value / 255;
            return linear <= 0.04045 ? linear / 12.92 : ((linear + 0.055) / 1.055) ** 2.4;
          });
          return channels[0] * 0.2126 + channels[1] * 0.7152 + channels[2] * 0.0722;
        };
        for (const selected of result.selected) {
          const a = luminance(selected.color), b = luminance(selected.background);
          assert((Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05) >= 4.5,
            `${mode}/${id}: selected text contrast is below 4.5:1 (${selected.text})`);
        }
        assert(result.overflow <= 1, `${mode}/${id}: horizontal overflow`);
        if (result.sliders.length) await checkSliderGeometry();
        inventory.push({ mode, id, ...result });
        if (["about", "appearance", "interface", "editor", "hotkeys", "canvas", "graphite-settings-fixture", "owen-editor", "owen-mermaid", "owen-exporter", "obsidian-style-settings"].includes(id)) {
          await capture(`${mode}-${id}`);
        }
      }
    }
    await setMode("light");
    await choose("graphite-settings-fixture");
    const before = await main.evaluate(() => ({ ...app.plugins.plugins["graphite-settings-fixture"].state }));
    const select = settings.locator("select").first();
    await select.focus();
    await select.press("Enter");
    await settings.locator(".owen-settings-dropdown-popover:popover-open").waitFor();
    await select.press("ArrowDown");
    await select.press("Enter");
    assert.equal(await select.inputValue(), "b");
    const state = await main.evaluate(() => app.plugins.plugins["graphite-settings-fixture"].state);
    assert.deepEqual(state, { value: "b", changes: before.changes + 1, inputs: before.inputs + 1 });
    await select.press("Enter");
    await select.press("End");
    await select.press("Enter");
    assert.equal(await select.inputValue(), "a", "Disabled last option must be skipped");
    await select.click();
    await settings.locator(".owen-settings-dropdown-popover:popover-open").waitFor();
    await capture("dropdown");
    await settings.locator(".setting-item-name").first().click();
    assert.equal(await settings.locator(".owen-settings-dropdown-popover:popover-open").count(), 0);
    await select.focus();
    await select.press("Enter");
    await select.press("Escape");
    assert.equal(await select.getAttribute("aria-expanded"), "false");
    const toggle = settings.locator(".checkbox-container").first();
    const checked = await toggle.locator("input").isChecked();
    await toggle.click();
    assert.equal(await toggle.locator("input").isChecked(), !checked);
    await toggle.click();
    const slider = settings.locator('input[type="range"]').first();
    const original = Number(await slider.inputValue());
    await slider.focus();
    await slider.press("ArrowRight");
    assert.equal(Number(await slider.inputValue()), original + 1);
    await slider.press("ArrowLeft");
    await settings.setViewportSize({ width: 700, height: 800 });
    await choose("editor");
    assert(await settings.locator(".vertical-tab-content").evaluate(root => root.scrollWidth <= root.clientWidth + 1));
    await capture("narrow-editor");
    await settings.setViewportSize({ width: 1100, height: 850 });
    await choose("interface");
    await capture("final-interface");
    await main.evaluate(async id => app.plugins.disablePlugin(id), companion);
    await main.evaluate(async () => app.plugins.disablePlugin("obsidian-style-settings"));
    assert.equal(await settings.locator("body.css-settings-manager").count(), 0);
    assert.equal(await settings.locator("[data-owen-graphite-dropdown], .ogd-settings-generated-heading").count(), 0, "Companion unload leaked owned DOM");
    assert.equal(await settings.locator("select[aria-controls]").count(), 0, "Companion unload leaked ARIA");
    assert.equal(await settings.locator(".setting-group").first().evaluate(element => getComputedStyle(element).borderStyle), "solid", "CSS-only cards require no plugin");
    await main.evaluate(async id => app.plugins.enablePlugin(id), companion);
    await main.evaluate(async () => app.plugins.enablePlugin("obsidian-style-settings"));
    await settings.locator("select[aria-controls]").first().waitFor();
    await main.evaluate(() => app.setting.close());
    await main.waitForTimeout(150);
    await main.evaluate(() => app.setting.open());
    await main.waitForTimeout(500);
    settings = context.pages().find(page => page.url() === "about:blank");
    await choose("about");
    await settings.locator("select[aria-controls]").first().waitFor();
    await capture("final-about");
    const rail = settings.locator(".owen-editor-frosted-scroll-overlay:not([hidden]) .owen-frosted-scroll__rail").last();
    await rail.waitFor();
    const sidebarGrip = settings.locator(".owen-editor-frosted-scroll-overlay.mod-settings-sidebar:not([hidden]) .owen-frosted-scroll__grip");
    const sidebarRight = await settings.locator(".vertical-tab-header").evaluate(element => element.getBoundingClientRect().right);
    const sidebarBox = await sidebarGrip.boundingBox();
    assert(sidebarRight - sidebarBox.x - sidebarBox.width >= 0
      && sidebarRight - sidebarBox.x - sidebarBox.width <= 5,
    "Sidebar scrollbar must sit within 5px of the panel's right edge");
    const grip = rail.locator(".owen-frosted-scroll__grip");
    assert.equal(await grip.evaluate(element => getComputedStyle(element).width), "6px");
    assert.equal(await grip.evaluate(element => getComputedStyle(element).height), "44px");
    assert.equal(await rail.evaluate(element => getComputedStyle(element, "::before").width), "2px");
    await grip.hover();
    assert.equal(await grip.evaluate(element => getComputedStyle(element).width), "10px");
    const gripBox = await grip.boundingBox();
    await settings.mouse.move(gripBox.x + gripBox.width / 2, gripBox.y + gripBox.height / 2);
    await settings.mouse.down();
    await settings.mouse.move(gripBox.x + gripBox.width / 2, gripBox.y + 160, { steps: 8 });
    await settings.mouse.up();
    assert(await settings.locator(".owen-editor-frosted-scroll-viewport").evaluateAll(
      elements => elements.some(element => element.scrollTop > 0),
    ), "Frosted grip dragging did not scroll a viewport");
    await settings.locator(".owen-editor-frosted-scroll-viewport").evaluateAll(elements => elements.forEach(element => { element.scrollTop = 0; }));
    await capture("global-frosted-scrollbars");
    await main.evaluate(async () => app.plugins.disablePlugin("owen-editor"));
    assert.equal(await settings.locator(".owen-editor-frosted-scroll-overlay").count(), 0);
    assert.equal(await settings.locator(".vertical-tab-content-container").evaluate(
      element => getComputedStyle(element, "::-webkit-scrollbar").width,
    ), "14px", "Native scrollbar fallback does not match the Portal rail hit area");
    await capture("native-scrollbar-fallback");
    await main.evaluate(async () => app.plugins.enablePlugin("owen-editor"));
    await settings.locator(".owen-editor-frosted-scroll-overlay:not([hidden])").first().waitFor();
    assert.equal(await settings.locator(".owen-editor-glass-toolbar, .owen-editor-selection-toolbar").count(), 0,
      "Re-enabling Editor from settings must not create editing toolbars there");
    await main.evaluate(async () => {
      const plugin = app.plugins.plugins["owen-editor"];
      const leaf = app.workspace.getLeaf(false);
      const mainDocument = app.workspace.rootSplit.doc;
      app.workspace.moveLeafToPopout(leaf);
      for (let attempt = 0; attempt < 100 && leaf.view.contentEl.ownerDocument === mainDocument; attempt += 1)
        await new Promise(resolve => setTimeout(resolve, 50));
      const doc = leaf.view.contentEl.ownerDocument;
      if (doc === mainDocument) throw new Error("Markdown popout did not adopt the document");
      try {
        app.workspace.setActiveLeaf(leaf, { focus: true });
        plugin.updateToolbarContentOffset();
        plugin.refreshSelectionToolbar();
        if (!plugin.toolbarEl?.isShown() || plugin.toolbarEl.ownerDocument !== doc)
          throw new Error("Markdown popout did not receive its editing toolbar");
        if (plugin.selectionToolbarEl?.ownerDocument !== doc)
          throw new Error("Selection toolbar does not belong to the Markdown popout");
        if (mainDocument.body.classList.contains("owen-editor-toolbar-offset"))
          throw new Error("Moving to a document popout left stale toolbar clearance in the main window");
      } finally {
        doc.defaultView.close();
      }
    });
    await fs.writeFile(path.join(evidenceDirectory, "settings-results.json"), JSON.stringify(inventory, null, 2));
    console.log(`PASS: ${ids.length} settings pages in light/dark; Markdown-only toolbars and document popouts; centered navigation, searches, slider geometry, dropdown events/keyboard/dismissal, narrow layout, unload/popout reopen, Frosted rail/grip/drag and native fallback`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
