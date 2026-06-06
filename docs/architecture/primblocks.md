# Primblocks And Canonical Data

Status: current private implementation primitive. This page describes the
public-safe role of primblocks in Ainix; it is not a standalone public product
release.

Primblocks is the canonical data-block layer under Ainix. Its job is deliberately
small: import ordinary files as stable content blocks, preserve byte identity
and metadata, and let higher layers reconstruct the original artifacts.

Ainix then layers policy, provenance, semantic lattice records, agents, and shell
projection above those canonical blocks.

## Why It Matters

Many agent systems ingest data by turning files or messages directly into
embeddings, summaries, or ad hoc JSON. That is useful for retrieval, but weak as
a source of truth.

Ainix uses primblocks so imported material keeps a canonical backing record
before it becomes semantic context. The result is a cleaner chain:

```text
ordinary file or future connector payload
-> primblocks canonical block
-> Ainix lattice node
-> provenance/event record
-> semantic index and context refs
-> shell/canvas projection
-> agent proposal with cited context
```

The technical distinction is not that content-addressed blocks are novel by
themselves. The distinction is that Ainix treats canonical blocks as the base
truth layer and keeps derived semantic state rebuildable and auditable.

## Current Artifact

The following excerpt is from a scratch private-runtime demo using a small
`pipeline-note.md` file. It shows the implemented chain from primblocks import
to semantic shell projection. IDs are deterministic hashes from the local demo
run; the source content was synthetic.

```json
{
  "import_id": "import_39980a15bc7d346edcaa35f8731df8d141aa47038470f0329e58c12ad4e8304e",
  "adapter": "primblocks",
  "blocks": [
    {
      "source_path": "pipeline-note.md",
      "block_id": "block_a99957901d81eaa5474fccf4f6ecde8c5f9755195c9383d48266f528460f6e2a",
      "blake3_hex": "a99957901d81eaa5474fccf4f6ecde8c5f9755195c9383d48266f528460f6e2a",
      "byte_len": 141,
      "media_type": "text/markdown",
      "canonical": true
    }
  ],
  "nodes": [
    {
      "node_id": "node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b",
      "node_type": "file_artifact",
      "source_path": "pipeline-note.md",
      "block_id": "block_a99957901d81eaa5474fccf4f6ecde8c5f9755195c9383d48266f528460f6e2a"
    }
  ],
  "relationships": [
    {
      "source_node_id": "node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b",
      "kind": "backed_by_block",
      "target": "block:block_a99957901d81eaa5474fccf4f6ecde8c5f9755195c9383d48266f528460f6e2a"
    }
  ]
}
```

The same run projected that lattice node into the shell:

```json
{
  "object_id": "canvas_object_a70eaa9fee8a77ebec0e36ae7a7dabc4bf79300e9f662d2b2f96cc8ccfc10756",
  "object_type": "node_view",
  "source_ref": "node:node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b",
  "layout_semantics": ["entrypoint"],
  "persistence_class": "persistent",
  "visibility_policy": "private"
}
```

And the context-agent proposal cited the semantic node before applying a
contextual connection:

```json
{
  "relationship_kind": "contextual_connection",
  "source_ref": "lattice:nodes/node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b",
  "target_ref": "lattice:nodes/node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b",
  "cited_context_refs": [
    "lattice:nodes/node_0651cff3304defab9ddbda157245f6e4e6ceb72d3f93595b9bf7a2258986a24b"
  ]
}
```

The demo store's event chain verified after the import, semantic index, semantic
query, context-connection proposal, approval, apply, and shell launch records.

## Product Boundary

Primblocks should stay below product policy. It should not own identity,
permissions, agent orchestration, CRM semantics, UI state, or connector-specific
schemas. Those belong to Ainix runtime layers above it.

That boundary is useful for future workflows such as a relationship-memory
agent. Slack, email, CRM, meeting notes, and professional-network data can become
canonical imported records first, then semantic timeline/context records second.
Follow-up reminders and proposed actions can cite the semantic records without
losing the ability to trace back to canonical source material.

## Current Limits

- Public docs show the primitive and artifact shape, not a public connector SDK.
- Connector ingestion for Slack, email, CRM, meeting notes, and professional
  networks remains future product integration work.
- Public-preview release availability remains `not_claimed`.
- Primblocks is a canonical data primitive, not an agent runtime or GUI.
