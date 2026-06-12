# Primblocks: Canonical Data

Primblocks is the canonical data-block layer beneath Ainix, and one of the pieces
of engineering the project is most deliberate about. Its job is small and
systems-oriented: import ordinary workspace files into stable content blocks,
preserve byte identity and metadata, and export them back to **byte-identical**
files. Everything Ainix builds on top — policy, provenance, the semantic lattice,
agents, canvas projection — sits *above* this layer.

The bet is simple: most agent systems ingest data by turning files straight into
embeddings, summaries, or ad-hoc JSON. That is fine for retrieval but weak as a
source of truth. Ainix keeps a canonical, verifiable backing record *before*
anything derived exists, so derived state stays rebuildable and auditable from a
stable base.

## The core invariant

Import a directory, export it, and get back the exact same bytes — including the
awkward cases that break naive tooling: CRLF line endings, files with no trailing
newline, empty files, and binary payloads that are not valid UTF-8. Round-trip
byte-exactness is the property the rest of the system is allowed to depend on.

## What makes it trustworthy

The value is in the execution, not in content-addressing being novel. Concretely:

- **Deterministic, content-derived identity.** A block's id is a domain-separated
  hash over its kind, normalized path, identity-bearing metadata, and payload
  bytes. Same content and identity metadata → same id, every time, on any machine.

- **Identity vs. descriptive metadata.** Only an explicit allowlist of fields
  participates in identity. Volatile filesystem metadata — modification time,
  change time — is recorded but provably *never* changes a block's id. Re-import
  an unchanged file tomorrow and it is the same block.

- **Adversarial path safety, both directions.** Paths are normalized to POSIX
  relative form with traversal (`..`), absolute, and non-normalized paths
  rejected. Import skips symlinks (so a link can't leak a file from outside the
  workspace). Export resolves each destination and refuses any path that escapes
  the export root, refuses to overwrite existing files or directories, and
  preflights conflicts so a failed export never leaves partial writes behind.

- **Reproducible workspace semantics.** Deterministic ordering and conflict
  detection (a file path can't shadow another file's parent directory) make
  import → lookup → export stable and predictable.

- **A clean, enforced boundary.** Primblocks does not own identity, signing,
  authorization, agent orchestration, UI state, or product schemas — those belong
  to the layers above. A Rust core is the canonical source of truth, with a Python
  package kept as a behavioral parity reference.

## The chain it anchors

```text
source file (exact bytes)
  → canonical block      ·  deterministic id, byte-preserving payload
  → semantic lattice node
  → provenance / event record
  → semantic index + cited context
  → canvas projection
  → agent proposal, traceable back to the canonical block
```

Because the base layer is canonical and verifiable, every step above it can be
re-derived and audited — and any agent proposal can be traced back to the exact
source bytes it came from.

This page describes the role and guarantees of primblocks at a high level.
Concrete formats, APIs, and the layers that consume it live in the private
implementation repository.
