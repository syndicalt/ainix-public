# Roadmap

This roadmap is intentionally high-level. Milestone details remain in the private implementation repo until the runtime is ready for broader review.

## Current Checkpoint

As of the 2026-06-05 internal roadmap checkpoint, the private implementation has
validated the hosted userspace substrate through brokered runtime authority,
event provenance, semantic lattice import, persistent canvas projection, hosted
shell UI contracts, spatial renderer adapters, and public-preview release-gate
tooling.

The project is still private preview only. The public-preview release claim is
`not_claimed` until final release controls, clean release-candidate validation,
external evidence, and announcement preflight are complete.

See the current public-safe update:
[2026-06-05 Development Update](../updates/2026-06-05-development-update.md).

## Phase 1: Hosted Runtime

Validate the local-first agentic substrate above existing operating systems.

- Identity and delegation
- Capability kernel
- Event provenance
- Semantic lattice
- Agent delegation
- Extension execution
- Local API and CLI
- Hosted shell/canvas prototype
- Renderer-neutral canvas projection with DOM and opt-in Three.js adapters
- Single-executable semantic shell demo scaffold

## Phase 2: Private UAT

Exercise the runtime with real workflows before expanding the audience.

- Clean local install path
- Repeatable smoke tests
- Dogfood workflows
- Crash/replay recovery checks
- Security review of extension trust and local API transport
- Prototype screenshots from real hosted shell behavior
- Demo video/GIF from real runtime behavior when release controls allow it

## Phase 3: Public Preview Surface

Expose a limited developer-facing story without publishing the full private implementation.

- Public explainer material
- Architecture excerpts
- Development updates and prototype screenshots
- Demo media from bounded runtime flows
- Selected docs
- Preview invitation path
- Partner/reference-device outreach

## Phase 4: Canvas Shell

Move beyond CLI/admin surfaces toward the primary user experience.

- Infinite canvas shell
- Touch-first control surface
- Agent presence and delegation view
- Semantic node/lattice navigation
- Cross-device continuity
- Accessibility and offline-first flows

## Phase 5: Native OS Research

After the hosted runtime proves the primitive model, begin deeper native-system work.

- Session manager
- Shell/compositor boundary
- IPC/syscall-style contracts
- Storage substrate
- Device boundary
- Kernel and scheduler research
