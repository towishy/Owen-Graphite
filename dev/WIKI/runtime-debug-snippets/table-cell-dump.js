(() => {
    const cell = [...document.querySelectorAll('td, th')]
        .find(el => el.getBoundingClientRect().height > 90) ||
        document.activeElement?.closest?.('td, th');
    if (!cell) { copy('NO_CELL_FOUND'); return 'NO_CELL_FOUND'; }
    const nodes = [];
    for (let el = cell; el && nodes.length < 12; el = el.parentElement) nodes.push(el);
    const out = nodes.map(el => {
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return {
            tag: el.tagName,
            cls: String(el.className || ''),
            text: el.textContent?.trim().slice(0, 80),
            style: el.getAttribute('style'),
            rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
            computed: {
                display: cs.display,
                position: cs.position,
                width: cs.width,
                height: cs.height,
                minHeight: cs.minHeight,
                maxHeight: cs.maxHeight,
                padding: cs.padding,
                margin: cs.margin,
                lineHeight: cs.lineHeight,
                verticalAlign: cs.verticalAlign,
                overflow: cs.overflow,
                transform: cs.transform
            }
        };
    });
    copy(JSON.stringify(out, null, 2));
    return out;
})();
