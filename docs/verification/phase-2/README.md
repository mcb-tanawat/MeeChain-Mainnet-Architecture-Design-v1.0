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
- review-record-template/README.md — template for actual review record capture; not itself a review outcome
- review-decision-summary/README.md — template for a review decision summary; not itself an approval decision
- deferred-work-register/README.md — deferred items and required actions
- review-record-instance/README.md — example instance for workflow demonstration only; not a verified review record
- review-decision-summary-instance/README.md — example instance for workflow demonstration only; not an official review decision

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
3. Review record instance and review decision summary instance for workflow demonstration
4. Deferred work register update
5. Review decision summary
6. Proposal for next phase only after auditability and ownership are clear

Proposal review lifecycle for Phase 2

Proposal → Review → Decision → Identity/Authority Validation → Runtime Evidence → Independent Audit

Template and example notice

> The review record template, review decision summary template, and example instance files in this directory are templates or example artifacts only. They are not approval records, verified review decisions, or evidence of a completed governance action unless populated by an actual reviewer with an actual evidence reference and timestamp.
