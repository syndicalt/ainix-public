# Architecture Overview

Ainix is organized as a staged operating-system project: a hosted semantic-OS
substrate today, with a deliberate path toward native-system work later.

## Hosted userspace stage

The current implementation is a Rust userspace runtime that runs on existing host
operating systems. This stage validates the primitive model without taking on
kernel, driver, compositor, or hardware support too early.

Core runtime concerns:

- Identity and delegated authority
- Capability and policy enforcement
- Event log and provenance chain
- Semantic lattice storage
- Agent and extension execution
- Local API and CLI control surfaces
- A hosted canvas-shell prototype

## Semantic OS substrate

The substrate makes agent work explicit and auditable instead of forcing agents
to scrape arbitrary application windows or infer state from unstructured files.

Key primitives:

- **identity** — cryptographic actors for users, devices, agents, and shared spaces
- **canonical blocks** — byte-preserving records for imported source material
  (see [Primblocks](primblocks.md))
- **capabilities** — explicit, scoped authority grants; no ambient power
- **events** — an append-only history of meaningful mutations and actions
- **lattice** — versioned semantic state with provenance
- **agents** — delegated computational actors
- **extensions** — brokered tools with policy and replay protection
- **canvas** — the future shell surface for people, agents, knowledge, and work

## Native OS trajectory

Ainix is not only an application runtime. The hosted version preserves the option
to move below the userspace boundary later:

- Native shell and session manager
- System IPC contracts
- Storage and event substrate
- Capability security boundary enforced by the kernel
- Device and session abstractions
- Kernel and scheduler research

The short-term goal is proof of the primitive model. The long-term goal is a
general-purpose agentic OS. This public overview stays at the level of roles and
direction; mechanism-level design lives in the private implementation repository.
