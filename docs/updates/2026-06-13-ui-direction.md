# 2026-06-13: A UI direction — act + verify

We sharpened what Ainix *is* and what its surface should be.

## The sharpening

Ainix is a **verifiable agent control surface** — the place to task agents and to
see, approve, and prove everything they do — on the path to an agent-native OS.
That is the wedge: not "an operating system" in the abstract, but the narrow,
useful thing underneath it. The full operating-environment ambition remains the
long arc, approached one earned step at a time rather than promised up front.

## Two halves of one loop

Everything is one loop — **propose → approve → apply → record → verify** — from
two ends:

- **Act** — a screen-aware work surface ("Summon", deliberately *not* a chat box)
  and a semantic filesystem (content unified by meaning + provenance, not folders).
- **Verify** — the run timeline, approval inbox, diff-first review, policy &
  capabilities, provenance explorer, per-event proof, and an on-demand graph.

## A real design system

We built the surface as a from-scratch vision on a real design-token system
(OKLCH-derived theming, a 6px grid, one font, layered surfaces) in the spirit of
Pop!_OS COSMIC and elementaryOS — calm, modern, deliberately lightweight. Ten
high-fidelity mockups now live in [the UI deck](../../assets/ui-deck/); see the
[UI direction](../design/ui.md) for the principles.

The earlier exploratory concept art (AR/VR, touch, mobile, infinite canvas) has
been retired to [`assets/archive/`](../../assets/archive/). The current surface is
**desktop 2D**.

> The interface images are mockups, not shipping software. As always, the
> verifiability language is kept honest: a signature attests custody and
> identity, never that an action was correct.
