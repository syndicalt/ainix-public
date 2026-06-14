# Vision Excerpt

This excerpt is adapted from the Ainix design notes and is provided for public
positioning. It describes direction and principles, not implementation detail.

## Mission

Ainix is a verifiable agent control surface: a place to task software agents and
to see, approve, and prove everything they do. The first implementation
deliberately starts as a userspace runtime on existing operating systems, but the
architecture is oriented toward operating-system primitives — identity,
authority, provenance — rather than a conventional assistant shell, so the
focused product can grow into an agent-native operating environment over time.

Ainix treats intent, knowledge, agents, authority, provenance, and presence as
first-class computing primitives.

## Core Thesis

You cannot trust an agent's own account of what it did. So Ainix organizes
computation around an independent, verifiable record of authorized action:

- **Identities** — cryptographic actors with delegated authority
- **Authority** — explicit, scoped, time-bounded capabilities; no ambient power
- **Provenance** — a tamper-evident, signed history of meaningful action
- **Knowledge** — semantic, versioned, queryable, provenance-rich state
- **Agents** — goal-directed actors operating under capability and budget
- **Intent** — user meaning, expressed through an ambient work surface
- **Presence** — real-time inhabitation of shared semantic spaces

Traditional operating systems organize computation around files, processes,
applications, windows, users, permissions, and devices. Those may exist as
compatibility bridges, but they are not the root model.

## Non-Negotiable Principles

- User sovereignty
- Local-first operation
- Cryptographic accountability — and honesty: a signature attests custody and
  identity, never that an action was correct
- Capability-scoped authority; no ambient power
- Human sovereignty over automation; gating that resists rubber-stamping
- Composable primitives
- Progressive realization — from a focused control surface to an ambient layer,
  and only then toward native-system work where it earns its place

## First Phase Boundary

The current phase does not include a custom kernel, full hardware driver stack,
AR/VR or touch interface, public agent marketplace, or universal compatibility
layer. The surface is desktop 2D. The focus is proving the verifiable agent loop
and making it legible.
