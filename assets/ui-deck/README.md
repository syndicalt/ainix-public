# Ainix — UI Vision Deck

High-fidelity mockups of the Ainix desktop surface. These are **not** AI-art
concepts — they are built on a real design-token system (OKLCH-derived theming, a
6px spacing grid, one type family, layered surfaces, rounded corners + soft
shadows), in the spirit of Pop!_OS COSMIC and elementaryOS: calm, modern, and
deliberately lightweight.

> Mockups, not screenshots of shipping software. Illustrative content. The
> verifiability language is kept honest: a signature attests *custody and
> identity* — that an action was recorded by a known signer in order — never that
> the action was *correct*.

## View it

Open `index.html` in a browser. Arrow keys / space to navigate, `G` for the
overview grid, `Esc` to close it. Each slide is captioned with its design
rationale. Individual screens are standalone `*.html` files; static renders live
in `shots/`.

## Two halves of one loop

Everything is the same loop — **propose → approve → apply → record → verify** —
seen from two ends:

- **Act** — where actions are *born*: the **Summon** work surface (an ambient,
  screen-aware, multimodal overlay — not a chat box) and the **semantic
  filesystem** (your content unified by meaning + provenance, not folders).
- **Verify** — where actions are *checked*: the run timeline, approval inbox,
  diff-first review, policy & capabilities, provenance explorer, event proof, and
  an on-demand relationship graph.

## Design language

- **OKLCH-derived theming** — one accent color, surfaces and text derived by
  varying lightness so contrast targets are always met; first-class light & dark.
- **6px spacing grid**, one UI font, depth via layered surfaces rather than hard
  borders, rounded corners + soft shadows, subtle purposeful motion.
- **Lightness as a design value** — idle footprint and startup are treated as
  specs, not afterthoughts.
