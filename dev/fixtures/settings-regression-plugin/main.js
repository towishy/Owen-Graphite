"use strict";

const { Plugin, PluginSettingTab, Setting } = require("obsidian");

module.exports = class extends Plugin {
  onload() {
    this.state = { value: "a", changes: 0, inputs: 0 };
    this.addSettingTab(new class extends PluginSettingTab {
      display() {
        this.containerEl.empty();
        new Setting(this.containerEl).setName("Legacy text field").setDesc("Descriptions and links remain visible.").addText(text => text.setValue("Sample"));
        new Setting(this.containerEl).setName("Legacy toggle").addToggle(toggle => toggle.setValue(true));
        new Setting(this.containerEl).setName("Legacy dropdown").addDropdown(dropdown => {
          dropdown.addOptions({ a: "Alpha", b: "Beta", c: "Disabled" }).setValue("a");
          dropdown.selectEl.options[2].disabled = true;
          dropdown.onChange(value => {
            this.plugin.state.value = value;
            this.plugin.state.changes += 1;
          });
          dropdown.selectEl.addEventListener("input", () => this.plugin.state.inputs += 1);
        });
        new Setting(this.containerEl).setName("Legacy slider").addSlider(slider => slider.setLimits(0, 10, 1).setValue(4).setDynamicTooltip());
      }
    }(this.app, this));
  }
};
