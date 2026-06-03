# Ainix

**Ainix is a private-preview research prototype for an agent-native computing environment.**

The project explores a staged path from a hosted userspace runtime on existing operating systems toward a general-purpose agentic OS: identity, capabilities, event provenance, semantic memory, agents, extensions, and an eventual canvas-first shell.

This public repository is intentionally limited. It contains high-level architecture notes, a roadmap, selected SPEC excerpts, and concept renders. The implementation repo is private while the runtime, security model, and developer surfaces mature.

## Status

- Research prototype
- Private preview only
- Runtime implementation is private
- Current work focuses on the hosted userspace substrate
- Future UI renders are conceptual, not current product screenshots

## What Ainix Is Exploring

Ainix treats these as operating-system primitives:

- Cryptographic identity and delegated authority
- Capability-scoped agents and extensions
- Append-only event provenance
- Semantic lattice storage and retrieval
- Local-first operation
- Composable control surfaces
- A canvas/shell model for humans, agents, tools, and knowledge

The first implementation runs above existing operating systems. The long-term architecture keeps a path open to native shell, session manager, storage, IPC, and kernel work after the primitive model proves itself.

## Public Materials

- [Architecture overview](docs/architecture/overview.md)
- [SPEC excerpt](docs/spec/spec-excerpt.md)
- [Roadmap](docs/roadmap/roadmap.md)
- [Demo media note](docs/demo/README.md)
- [Concept render captions](assets/concept-renders/README.md)
- [GUI concept captions](assets/gui-concepts/README.md)

## Private Preview Language

Ainix is not currently a consumer product, public SDK, operating-system replacement, or downloadable desktop environment. It is a private research prototype for validating agent-native OS primitives before exposing source code, package boundaries, or extension APIs publicly.

## Visual Assets

Concept renders are provided to communicate direction. They should be described as future UI concepts or product vision renders, not screenshots of the current runtime.
