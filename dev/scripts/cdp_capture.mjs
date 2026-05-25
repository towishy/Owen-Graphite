#!/usr/bin/env node
import { writeFile } from "node:fs/promises";

const args = new Map();
for (let index = 2; index < process.argv.length; index += 1) {
  const key = process.argv[index];
  if (!key.startsWith("--")) continue;
  const next = process.argv[index + 1] || "";
  if (next && !next.startsWith("--")) {
    args.set(key.slice(2), next);
    index += 1;
  } else {
    args.set(key.slice(2), "true");
  }
}

const endpoint = args.get("endpoint") || "http://127.0.0.1:9222/json";
const selector = args.get("selector") || "body";
const scenario = args.get("scenario") || "resting";
const pseudo = (args.get("pseudo") || "").split(",").map((item) => item.trim()).filter(Boolean);
const outPath = args.get("out") || "";
const expressionArg = args.get("expr") || "";
const mouseAction = args.get("mouse") || "";
const actionSelector = args.get("action-selector") || selector;
const statusOnly = args.get("status") === "true";
const requireVault = args.get("require-vault") || "";
const requireVersion = args.get("require-version") || "";
const requireTheme = args.get("require-theme") || "";

const assertRequirements = (output) => {
  const actual = output || {};
  const checks = [
    ["vaultName", requireVault],
    ["obsidianVersion", requireVersion],
    ["themeName", requireTheme],
  ];
  for (const [key, expected] of checks) {
    if (expected && actual[key] !== expected) {
      throw new Error(`Requirement failed: ${key} expected ${JSON.stringify(expected)} but got ${JSON.stringify(actual[key] || "")}`);
    }
  }
};

const loadTargets = async () => {
  try {
    const response = await fetch(endpoint);
    return await response.json();
  } catch (error) {
    throw new Error(`Cannot reach Obsidian CDP endpoint ${endpoint}. Start Obsidian with --remote-debugging-port=9222. ${error.message || error}`);
  }
};

const targets = await loadTargets();
const target = targets.find((item) => item.type === "page" && item.url.startsWith("app://obsidian.md/"));
if (!target) throw new Error("No Obsidian CDP page target found. Start Obsidian with --remote-debugging-port=9222.");

const socket = new WebSocket(target.webSocketDebuggerUrl);
let nextId = 1;
const pending = new Map();

socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  const waiter = pending.get(message.id);
  if (!waiter) return;
  pending.delete(message.id);
  if (message.error) waiter.reject(new Error(JSON.stringify(message.error)));
  else waiter.resolve(message.result);
});

await new Promise((resolve, reject) => {
  socket.addEventListener("open", resolve, { once: true });
  socket.addEventListener("error", reject, { once: true });
});

const send = (method, params = {}) => new Promise((resolve, reject) => {
  const id = nextId;
  nextId += 1;
  pending.set(id, { resolve, reject });
  socket.send(JSON.stringify({ id, method, params }));
});

const evaluate = async (expression) => {
  const result = await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true });
  if (result.exceptionDetails) throw new Error(result.exceptionDetails.text || "Runtime.evaluate failed");
  return result.result.value;
};

await send("Runtime.enable");
await send("DOM.enable");
await send("CSS.enable");

if (statusOnly) {
  const output = await evaluate(`(async () => {
    const appRef = window.app || globalThis.app;
    const titleVersion = (document.title.match(/Obsidian\\s+([0-9.]+)/) || [])[1] || "";
    let themeName = "";
    try {
      const raw = appRef && appRef.vault && appRef.vault.adapter && appRef.vault.adapter.read ? await appRef.vault.adapter.read(".obsidian/appearance.json") : "";
      themeName = raw ? (JSON.parse(raw).cssTheme || "") : "";
    } catch {}
    return {
      schema: "owen-graphite/cdp-status/1",
      ok: true,
      capturedAt: new Date().toISOString(),
      url: location.href,
      title: document.title,
      obsidianVersion: appRef && appRef.getVersion ? appRef.getVersion() : titleVersion,
      vaultName: appRef && appRef.vault ? appRef.vault.getName() : "",
      themeName,
      bodyClasses: String(document.body.className || "")
    };
  })()`);
  assertRequirements(output);
  if (outPath) await writeFile(outPath, JSON.stringify(output, null, 2) + "\n", "utf8");
  else console.log(JSON.stringify(output, null, 2));
  socket.close();
  process.exit(0);
}

if (expressionArg) {
  const output = await evaluate(expressionArg);
  if (output && typeof output === "object") assertRequirements(output);
  if (outPath) await writeFile(outPath, JSON.stringify(output, null, 2) + "\n", "utf8");
  else console.log(JSON.stringify(output, null, 2));
  socket.close();
  process.exit(0);
}

if (pseudo.length) {
  const documentResult = await send("DOM.getDocument", { depth: -1, pierce: true });
  const queryResult = await send("DOM.querySelector", { nodeId: documentResult.root.nodeId, selector });
  if (queryResult.nodeId) await send("CSS.forcePseudoState", { nodeId: queryResult.nodeId, forcedPseudoClasses: pseudo });
}

if (mouseAction) {
  const actionRect = await evaluate(`(() => { const target = document.querySelector(${JSON.stringify(actionSelector)}); if (!target) return null; const rect = target.getBoundingClientRect(); return { x: rect.x + rect.width / 2, y: rect.y + rect.height / 2 }; })()`);
  if (!actionRect) throw new Error(`No action target found for ${actionSelector}`);
  const button = mouseAction === "context" ? "right" : "left";
  if (mouseAction === "hover") {
    await send("Input.dispatchMouseEvent", { type: "mouseMoved", x: actionRect.x, y: actionRect.y });
  } else if (["click", "context"].includes(mouseAction)) {
    await send("Input.dispatchMouseEvent", { type: "mousePressed", button, x: actionRect.x, y: actionRect.y, clickCount: 1 });
    await send("Input.dispatchMouseEvent", { type: "mouseReleased", button, x: actionRect.x, y: actionRect.y, clickCount: 1 });
  } else {
    throw new Error(`Unsupported mouse action: ${mouseAction}`);
  }
}

const captureExpression = `(async () => {
  const selector = ${JSON.stringify(selector)};
  const scenario = ${JSON.stringify(scenario)};
  const target = document.querySelector(selector);
  if (!target) return { scenario, selector, error: "NO_TARGET_FOUND", bodyClasses: String(document.body.className || "") };
  const computedProps = ["display", "position", "width", "height", "minHeight", "maxHeight", "margin", "padding", "lineHeight", "overflow", "transform", "background", "backgroundColor", "border", "borderRadius", "boxShadow", "outline", "outlineOffset", "opacity", "zIndex", "color", "fontSize"];
  const labelFor = (element) => { const id = element.id ? '#' + element.id : ''; const className = String(element.className || '').trim().replace(/\\s+/g, '.'); return element.tagName.toLowerCase() + id + (className ? '.' + className : ''); };
  const previewFor = (element) => String(element.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 80);
  const readComputed = (element) => { const computed = getComputedStyle(element); return Object.fromEntries(computedProps.map((prop) => [prop, computed[prop]])); };
  const readRect = (element) => { const rect = element.getBoundingClientRect(); return { x: Number(rect.x.toFixed(2)), y: Number(rect.y.toFixed(2)), width: Number(rect.width.toFixed(2)), height: Number(rect.height.toFixed(2)) }; };
  const shouldKeepRule = (rule) => /hover|focus|active|selected|is-active|background|box-shadow|outline|border|transform|height|padding|display|position|z-index|opacity|color|font-size/i.test(rule.cssText);
  const walkRules = (rules, element, out) => { for (const rule of Array.from(rules)) { if (rule.cssRules) { walkRules(rule.cssRules, element, out); continue; } if (!rule.selectorText || !shouldKeepRule(rule)) continue; try { if (element.matches(rule.selectorText)) out.push({ selector: rule.selectorText, css: rule.style.cssText, stylesheet: rule.parentStyleSheet && rule.parentStyleSheet.href }); } catch {} } };
  const matchedRulesFor = (element) => { const matched = []; for (const sheet of Array.from(document.styleSheets)) { try { walkRules(sheet.cssRules, element, matched); } catch {} } return matched.slice(-120); };
  const chain = [];
  for (let element = target; element && chain.length < 10; element = element.parentElement) chain.push(element);
  const appRef = window.app || globalThis.app;
  const titleVersion = (document.title.match(/Obsidian\\s+([0-9.]+)/) || [])[1] || "";
  let themeName = "";
  try {
    const raw = appRef && appRef.vault && appRef.vault.adapter && appRef.vault.adapter.read ? await appRef.vault.adapter.read(".obsidian/appearance.json") : "";
    themeName = raw ? (JSON.parse(raw).cssTheme || "") : "";
  } catch {}
  return { schema: "owen-graphite/runtime-capture-fragment/1", scenario, selector, capturedAt: new Date().toISOString(), url: location.href, title: document.title, obsidianVersion: appRef && appRef.getVersion ? appRef.getVersion() : titleVersion, vaultName: appRef && appRef.vault ? appRef.vault.getName() : "", themeName, bodyClasses: String(document.body.className || ""), target: labelFor(target), activeElement: document.activeElement ? labelFor(document.activeElement) : "", domChain: chain.map((element) => ({ node: labelFor(element), inlineStyle: element.getAttribute("style") || "", textPreview: previewFor(element) })), rectChain: chain.map((element) => ({ node: labelFor(element), rect: readRect(element) })), computedGeometry: Object.fromEntries(chain.map((element) => [labelFor(element), readComputed(element)])), matchedRules: chain.map((element) => ({ node: labelFor(element), rules: matchedRulesFor(element) })), inlineStyle: target.getAttribute("style") || "" };
})()`;

const output = await evaluate(captureExpression);
assertRequirements(output);
if (outPath) await writeFile(outPath, JSON.stringify(output, null, 2) + "\n", "utf8");
else console.log(JSON.stringify(output, null, 2));
socket.close();
