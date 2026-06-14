# Architecture Overview

Ainix is a verifiable agent control surface built on a hosted userspace runtime
today, with a deliberate path toward an ambient, system-level layer — and,
eventually, native-system work — later. This overview stays at the level of roles
and direction; mechanism-level design lives in the private implementation
repository.

## The core idea

When an agent acts on your behalf, the action should be **authorized, recorded,
gated, and verifiable** — not taken on trust. Ainix makes agent work explicit and
auditable instead of forcing agents to scrape arbitrary windows or infer state
from unstructured files. The architecture exists to support one loop:

> **propose → approve → apply → record → verify**

## Hosted userspace stage (now)

The current implementation is a Rust userspace runtime that runs on existing host
operating systems. This stage validates the primitive model without taking on
kernel, driver, compositor, or hardware support too early.

Core runtime concerns:

- Identity and delegated authority
- Capability and policy enforcement (no ambient authority)
- An append-only, signed event log and provenance chain
- Canonical, byte-preserving import of source material
- Semantic state over those canonical records
- Agent and extension execution through typed brokers
- An asynchronous, multi-session supervisor with a budget-aware scheduler and
  real mid-flight cancellation
- Local API and CLI control surfaces

## Primitives

- **identity** — cryptographic actors for users, devices, agents, and shared spaces
- **canonical blocks** — byte-preserving records for imported source material
  (see [Primblocks](primblocks.md)); everything derived stays rebuildable
- **capabilities** — explicit, scoped, time-bounded authority grants; no ambient power
- **events** — an append-only, signed history of meaningful actions; tamper-evident
  and independently verifiable
- **semantic state** — versioned, queryable state with provenance, over canonical records
- **agents** — delegated computational actors operating under capability and budget
- **extensions** — brokered tools with policy and replay protection

## Surfaces: act + verify

The user-facing surface is two halves of the same loop:

- **Act** — a screen-aware work surface for tasking agents, and a semantic
  filesystem for working with content by meaning and provenance. Outputs are
  proposed, gated actions — never silent mutations.
- **Verify** — a run timeline, approval queue, diff-first review with citations,
  policy and capability controls, a provenance explorer, per-event cryptographic
  proof, and an on-demand relationship graph.

See the [UI direction](../design/ui.md) and the
[vision deck](../../assets/ui-deck/).

## Trajectory: toward an ambient layer, and an agent-native OS

Ainix is built to grow without over-reaching:

- **Near term** — a focused control-surface application you can actually use.
- **Then** — an ambient verification *layer*: an always-present status panel, a
  global approval gate that surfaces wherever an agent wants to act, and a command
  palette to launch verified actions from anywhere.
- **Long arc** — selective native-system work (session/shell boundaries, storage
  and event substrate, capability enforcement closer to the kernel) **only where
  the hosted layer proves it is required.**

The short-term goal is proof of the verifiable agent loop. The long-term goal is
an agent-native operating environment — approached one earned step at a time.
