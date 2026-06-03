# SPEC Excerpt

This excerpt is adapted from the private Ainix SPEC and is provided for public positioning only.

## Mission

Ainix is an agent-native operating system for personal and collaborative computing. The first implementation deliberately starts as a userspace runtime on existing kernels, but the architecture is oriented toward operating-system primitives rather than a conventional assistant shell.

Ainix treats intent, knowledge, agents, relationships, provenance, and presence as first-class computing primitives.

## Core Thesis

Traditional operating systems organize computation around files, processes, applications, windows, users, permissions, and devices.

Ainix organizes computation around:

- Identities: cryptographic actors with delegated authority
- Knowledge: semantic, versioned, queryable, provenance-rich state
- Agents: persistent goal-directed computational actors
- Intent: user meaning rather than literal commands
- Relationships: links between people, agents, nodes, devices, and contexts
- Presence: real-time inhabitation of shared semantic spaces
- Provenance: tamper-evident history for meaningful mutations

Files, processes, apps, windows, and command lines may exist as compatibility bridges, but they are not the root model.

## Non-Negotiable Principles

- User sovereignty
- Local-first operation
- Cryptographic accountability
- Agent-native substrate
- Human sovereignty over automation
- Composable primitives
- Progressive realization from hosted runtime to native OS

## First Phase Boundary

The first implementation phase does not include a custom kernel, full hardware driver stack, complete AR interface, public agent marketplace, or universal compatibility layer. It focuses on proving the runtime substrate.

