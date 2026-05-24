# State Token Map

Use this to keep resting, hover, active, focus, and print states consistent.

| State | Visual Intent | Token/Owner Route | Notes |
| --- | --- | --- | --- |
| Resting glass | white/gray frosted surface, subtle rim | tokens + owner module | Default state should stay quiet. |
| Hover | brighter surface, soft downward shadow | owner state rule using existing shadow/rim tokens | No layout shift. |
| Active | shallow sky tint or clearer rim | owner state rule, top chrome contract when chrome | Use only for meaningful selection. |
| Focus | accessible but restrained ring | owner focus rule, runtime evidence | Avoid strong cyan block. |
| Disabled | muted but legible | token/text owner | Do not remove affordance. |
| Print | document-safe contrast | PDF/print owner and PDF tokens | Keep screen chrome out. |
| Dark | dark-specific parity | `src/themes/50-dark.css` | Do not move base behavior here. |
| Reduced motion | stable interaction | `src/themes/51-accessibility-motion-contrast.css` | Preserve function without motion. |

If a state needs a new token, update `TOKENS/usage-guide.md` and verify Light/Dark/PDF impact.
