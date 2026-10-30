# MeeChain Verification Documentation

Status: Draft
Version: v0.1

This folder captures the verification and evidence record for the MeeChain repository in a way that is transparent, reviewable, and safe for public publication.

## Scope

This folder is intentionally limited to documentation and evidence tracking. It does not contain:

- genesis material
- node private keys
- validator private keys
- deployment secrets
- any confidential operational data

## Purpose

The purpose of this folder is to record the evidence chain and verification process in a traceable draft form while preserving the repository's existing public documentation and governance materials.

## Rules

1. This is a draft only and is not a ratified governance artifact.
2. Evidence items already present in the project record remain unchanged unless explicitly reviewed and approved.
3. No new evidence, secret material, or system configuration data is introduced in this public repository.
4. Any future revision must clearly state what was added, changed, or superseded.
5. The `record-001` and `evidence-register-001` directories are intended to be used as traceable evidence containers for review.

## Document Structure

```text
docs/
└── verification/
    ├── README.md
    ├── record-001/
    │   └── README.md
    └── evidence-register-001/
        └── README.md
```

## Review Status

- Record 001: Draft v0.2
- Evidence Register 001: Draft v0.1
- Evidence items EV-001 through EV-007: retained as existing project evidence and not re-created or modified in this public record
- Reviewer identity: intentionally not specified in this public branch

## Governance Note

This documentation is aligned with the repository's stated principles of:

- Rule First
- Evidence First
- Verification Everywhere

It is intended as a traceability layer for review and discussion, not as a replacement for the primary governance or architecture documents already present in the repository.
