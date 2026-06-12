# Roadmap

This roadmap is intentionally high-level. Detailed execution plans live in the
private implementation repository while the runtime matures.

The strategy is simple: **prove the agent-native computing model as a hosted
userspace layer on existing operating systems first, then move lower in the
stack only where the hosted layer proves deeper enforcement is required.**

## 1. Hosted runtime — now

Validate the local-first agentic substrate above existing operating systems.

- Cryptographic identity and delegated authority
- Capability and policy enforcement
- Append-only event provenance
- Semantic lattice over canonical, byte-preserving source records
- Agent and extension execution through typed brokers
- Local API and CLI control surfaces
- A hosted canvas-shell prototype with a renderer-neutral projection layer

This stage is working internally today. Its surface is kept honest: every
exposed command does real work.

## 2. First real agent — next

Drive one full agent loop with a real local model, end to end.

- A local model adapter under capability and budget control
- Intent → context query → inference → cited proposal → human approval → apply
- Full provenance for every inference and tool call
- Budget and cancellation guarantees

This is the phase that answers the project's central question: are the
identity / capability / proposal contracts ergonomic under a real agent?

## 3. Supervised OS — then

Turn the runtime into a real agent supervisor.

- Asynchronous, multi-session daemon
- Sandboxed agent sessions with kernel-enforced boundaries
- Durable storage with rebuildable indexes
- A scheduler with budget accounting and preemption

## 4. Canvas & native — later

Bring the primary user experience forward, and research native-system work.

- Infinite canvas shell as the primary surface, not an admin panel
- Touch-first control, agent presence, timeline replay, private sharing
- Cross-device continuity; eventually spatial (AR/VR) work surfaces
- Selective native-system research: session manager, shell/compositor boundary,
  storage substrate, and kernel/scheduler work where it earns its place

## What this roadmap does not promise

No custom kernel, full hardware driver stack, production AR interface, public
agent marketplace, or universal compatibility layer in the near term. The focus
is proving the runtime substrate and then the first real agent loop.

See the latest [development updates](../updates/README.md) for current status.
