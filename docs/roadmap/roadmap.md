# Roadmap

This roadmap is intentionally high-level. Detailed execution plans live in the
private implementation repository while the runtime matures.

The strategy is simple: **prove the verifiable agent loop as a hosted userspace
layer on existing operating systems, make it legible through the control surface,
and move lower in the stack only where the hosted layer proves deeper enforcement
is required.**

## 1. Hosted runtime — done / now

Validate the local-first agentic substrate above existing operating systems.

- Cryptographic identity and delegated authority
- Capability and policy enforcement
- Append-only, signed event provenance
- Semantic state over canonical, byte-preserving source records
- Agent and extension execution through typed brokers
- An asynchronous, multi-session supervisor: a budget-aware scheduler
  (provider-slot admission, cooperative preemption) and real mid-flight cancellation
- Local API and CLI control surfaces

This stage is working internally today. Its surface is kept honest: every exposed
command does real work.

## 2. The verify surface — next

Make the wedge visible. Build the observability half on the real signed event log.

- The run timeline: a chronological, causal record of what an agent did
- An approval inbox and diff-first review with verbatim citations
- Policy & capability controls — the answer to approval fatigue
- A provenance explorer and per-event cryptographic proof
- An on-demand relationship graph

## 3. The act surface — then

Where actions are born, feeding the same gated pipeline.

- A screen-aware, multimodal work surface ("Summon") — ambient, not a chat box
- A semantic filesystem: content unified by meaning and provenance, not folders
- A real agent loop end to end: intent → context → proposal → human approval →
  apply → full provenance, under capability and budget control

## 4. Ambient layer & beyond — later

Grow from a focused app into an always-present layer, and research native work.

- An ambient verification layer: a status panel, a global approval gate that
  surfaces wherever an agent wants to act, and a command palette
- Non-destructive steering and post-apply drift detection
- Selective native-system research — session/shell boundaries, storage and event
  substrate, capability enforcement closer to the kernel — **only where it earns
  its place**

## What this roadmap does not promise

No custom kernel, full hardware driver stack, AR/VR or touch interface, public
agent marketplace, or universal compatibility layer in the near term. The current
surface is **desktop 2D**. The focus is proving the verifiable agent loop and
making it legible.

See the latest [development updates](../updates/README.md) for current status.
