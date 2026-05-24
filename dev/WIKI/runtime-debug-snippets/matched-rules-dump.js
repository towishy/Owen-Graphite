(() => {
    const target = [...document.querySelectorAll('td, th')]
        .find(el => el.getBoundingClientRect().height > 90) ||
        document.activeElement?.closest?.('td, th') ||
        document.activeElement;
    if (!target) { copy('NO_TARGET_FOUND'); return 'NO_TARGET_FOUND'; }
    const nodes = [target, ...target.querySelectorAll?.('*') || []].slice(0, 20);
    const out = nodes.map(el => {
        const matched = [];
        for (const sheet of [...document.styleSheets]) {
            let rules;
            try { rules = sheet.cssRules; } catch { continue; }
            for (const rule of [...rules]) {
                if (!rule.selectorText) continue;
                try {
                    if (el.matches(rule.selectorText) && /height|min-height|max-height|vertical-align|padding|line-height|display|position|transform|width|max-width/.test(rule.style.cssText)) {
                        matched.push({ selector: rule.selectorText, css: rule.style.cssText });
                    }
                } catch {}
            }
        }
        const cs = getComputedStyle(el);
        return {
            tag: el.tagName,
            cls: String(el.className || ''),
            style: el.getAttribute('style'),
            computed: { height: cs.height, minHeight: cs.minHeight, maxHeight: cs.maxHeight, padding: cs.padding, lineHeight: cs.lineHeight, display: cs.display, position: cs.position, verticalAlign: cs.verticalAlign, width: cs.width, maxWidth: cs.maxWidth },
            matched: matched.slice(-50)
        };
    });
    copy(JSON.stringify(out, null, 2));
    return out;
})();
