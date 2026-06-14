# UI Direction

A from-scratch reimagining of the Ainix desktop surface, grounded in how people
actually want to supervise agents. The full set of mockups lives in
[`assets/ui-deck/`](../../assets/ui-deck/) (open `index.html`).

> Mockups, not screenshots of shipping software. Verifiability language is kept
> honest: a signature attests *custody and identity*, never *correctness*.

## Principles

- **Desktop 2D only.** Spatial/AR/VR, touch, and mobile are out of scope.
- **Calm and lightweight.** In the spirit of Pop!_OS COSMIC and elementaryOS:
  generous whitespace on a 6px grid, one type family, depth through layered
  surfaces rather than hard borders, rounded corners and soft shadows, subtle
  motion. Idle footprint and startup are treated as design specs.
- **Timeline first, graph on demand, proof one click deep.** The chronological,
  signed, append-only timeline is the default audit view; a relationship graph is
  a focused secondary lens; cryptographic proof lives in a drill-down behind an
  ambient integrity badge.
- **Spend attention where it's scarce.** Auto-handle low-risk, reversible actions;
  route only the consequential ones to a human; make evidence verbatim and
  one-click-verifiable; reserve real friction for irreversible moments. "Signed"
  must never mean "prompts every time."
- **Honesty over polish.** Surface broken chains, gaps, and uncertainty rather
  than hiding them.

## The two halves

One loop — **propose → approve → apply → record → verify** — from two ends.

### Act — where actions are born

- **Summon** — an ambient, screen-aware work surface (not a chat box). Declarative
  screen context shown as removable chips (structured signals, nothing scraped),
  multimodal ingest, and a dynamic working area of *gated proposals* and
  *semantic-filesystem matches* — not a scrolling transcript. Its output is a
  signed, gated action that becomes a run.
- **Semantic filesystem** — your content (code, documents, notes, runs, artifacts)
  unified by meaning and provenance, not folders. Every object is signed and
  provenance-linked; operations route through the gate.

### Verify — where actions are checked

- **Run timeline** — a causal waterfall of signed steps; integrity ambient, proof
  one click deep; destructive steps gated.
- **Approval inbox** — risk-sorted triage; self-contained decision cards.
- **Diff-first review** — approve the exact delta, with sentence-granular verbatim
  citations and a live precondition checklist.
- **Policy & capabilities** — allowlists, reversibility-aware gating, blast-radius
  classes, scoped time-bounded capability tokens.
- **Provenance explorer** — faceted, search-driven audit; honest about a broken
  chain.
- **Event proof** — a single event's record plus its hash-chain and external anchor.
- **Relationship graph** — focused, expand-on-demand; never the whole-run hairball.

## A design system, not concept art

The deck is built on a real design-token layer (OKLCH-derived theming, the 6px
grid, light/dark, one font), so the renders double as a faithful preview *and* a
head start on the implementation.
