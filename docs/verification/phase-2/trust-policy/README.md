# MeeChain Phase 2 — Trust Policy Draft

Status: DRAFT v0.1  
Not ratified.

Purpose

This document defines the initial design baseline for MeeChain Trust Policy. It describes the conditions under which an identity or signer is considered eligible to act within governance and operational processes.

Trust policy baseline principles

- Trust must be explicit, reviewable, and auditable.
- Identity is not the same as authority.
- A signer may be validly identified and still be unauthorized for a specific decision.
- Authority must be checked against the relevant governance context.
- Trust policy must support revocation, recovery, and evidence traceability.

Minimum policy elements

- policy purpose
- eligible identity classes
- trust framework and trust levels
- policy ownership and review authority
- policy versioning and change history
- recovery and revocation rules
- evidence requirements for policy updates

Draft trust model

1. Identity classes:
   - human actor
   - organization actor
   - service account / automation identity
   - validator or network participant

2. Trust levels:
   - self-attested
   - externally validated
   - formally recognized
   - governance-authorized

3. Required checks:
   - identity is registered
   - identity is active
   - public key is linked and active
   - signer is authorized for the decision type
   - policy version is valid for the decision context

4. Policy change controls:
   - proposal required
   - review required
   - approval required
   - versioned record required
   - evidence trace required

Trust policy design status

This document documents a design baseline only. No identity registry or key issuance is authorized by this document.

