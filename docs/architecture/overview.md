# Architecture Overview

Ainix is organized as a staged operating-system project.

## Hosted Userspace Phase

The current private implementation is a Rust userspace runtime that runs on existing host operating systems. This phase validates the primitive model without taking on kernel, driver, compositor, or hardware support too early.

Core runtime concerns:

- Identity and delegation
- Capability and policy enforcement
- Event log and provenance chain
- Semantic lattice storage
- Agent and extension execution
- Local API and CLI control surfaces
- Hosted shell/canvas experiments

## Semantic OS Substrate

The substrate is intended to make agent work explicit and auditable instead of forcing agents to scrape arbitrary app windows or infer state from unstructured files.

Key primitives:

- `identity`: cryptographic actors for users, devices, agents, and shared spaces
- `capabilities`: explicit, scoped authority grants
- `events`: append-only history of meaningful mutations and actions
- `lattice`: versioned semantic state with provenance
- `agents`: delegated computational actors
- `extensions`: brokered tools with policy and replay protection
- `canvas`: a future shell surface for people, agents, knowledge, and work

## Native OS Trajectory

Ainix is not only an application runtime. The hosted version should preserve the option to move below the userspace boundary later:

- Native shell and session manager
- System IPC contracts
- Storage and event substrate
- Capability security boundary
- Device/session abstractions
- Kernel and scheduler research

The short-term goal is proof of the primitive model. The long-term goal is a general-purpose agentic OS.

