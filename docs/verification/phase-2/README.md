# MeeChain Phase 2 — Trust Policy & Identity Registry

Status: DRAFT v0.1  
Not ratified.

Purpose

This directory defines the Phase 2 review package for MeeChain Trust Policy and Identity Registry design. It is intended to support a design-baseline review only, before any actual identity registry is created, any key material is generated, or any production system is configured.

Important notice

> This package is a design review artifact only. It does not authorize production identity registration, on-chain identity deployment, validator key generation, or Mainnet activation.

Core principles

- Governance must prove authority before it accepts a decision as valid.
- Identity and authority must be distinguishable from cryptographic validity alone.
- INDETERMINATE must not be treated as PASS.
- Draft review does not authorize production use.
- Trust policy, registry structure, role mapping, and revocation controls must remain auditable.

Phase 2 package contents

- README.md — phase overview and scope
- trust-identity-review-checklist/README.md — review checklist A–J for Phase 2
- trust-policy/README.md — conceptual trust policy baseline
- identity-registry/README.md — registry design baseline
- role-authority-matrix/README.md — identity-to-role-to-authority mapping
- deferred-work-register/README.md — deferred items and required actions
- review-record-template/README.md — per-item review record format
- review-decision-summary/README.md — review outcome summary format

Scope

This phase covers:

- Trust Policy design
- Identity Registry structure
- Role and authority mapping
- Signature and authorization verification separation
- Revocation and recovery lifecycle
- Auditability and evidence traceability

This phase does not cover:

- production identity deployment
- validator key issuance
- network activation
- public RPC enablement
- Mainnet authorization

Status model

- MET: requirements satisfied with evidence
- NOT MET: requirement not satisfied
- DEFERRED: requirement deliberately postponed with owner and milestone
- N/A: not applicable
- INDETERMINATE: evidence missing, conflicting, or insufficient

Important rule

> INDETERMINATE must not be treated as PASS in governance decisions, CI validation, or production activation.

Review flow

1. Review checklist
2. Review record capture
3. Deferred work register update
4. Review decision summary
5. Proposal for next phase only after auditability and ownership are clear

Proposal review lifecycle for Phase 2

Proposal → Review → Decision → Identity/Authority Validation → Runtime Evidence → Independent Audit

