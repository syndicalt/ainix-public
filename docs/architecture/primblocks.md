# Primblocks: Canonical Data

Primblocks is the canonical data-block layer beneath Ainix. Its job is
deliberately small: import ordinary files as stable content blocks, preserve byte
identity and metadata, and let higher layers reconstruct the original artifacts.

Ainix then layers policy, provenance, semantic lattice records, agents, and
canvas projection **above** those canonical blocks.

## Why it matters

Many agent systems ingest data by turning files or messages directly into
embeddings, summaries, or ad-hoc JSON. That is useful for retrieval but weak as a
source of truth.

Ainix keeps a canonical backing record for imported material *before* it becomes
semantic context. The result is a clean, auditable chain:

```text
source material
  → canonical content block (byte-preserving)
  → semantic lattice node
  → provenance / event record
  → semantic index and cited context
  → canvas projection
  → agent proposal with cited context
```

The point is not that content-addressed blocks are novel. The point is that Ainix
treats canonical blocks as the **base truth layer** and keeps all derived
semantic state rebuildable and auditable from it.

## Where the boundary sits

Primblocks stays *below* product policy. It does not own identity, permissions,
agent orchestration, UI state, or any application-specific schema — those belong
to the Ainix runtime layers above it. That separation is what lets imported
material remain a stable, verifiable record while the semantic and product layers
evolve independently.

This page describes the role of primblocks in Ainix at a high level. Concrete
data shapes, APIs, and connector work live in the private implementation
repository.
