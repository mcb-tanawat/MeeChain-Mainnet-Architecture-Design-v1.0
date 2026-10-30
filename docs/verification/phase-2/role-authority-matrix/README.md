# MeeChain Phase 2 — Role and Authority Matrix

Status: DRAFT v0.1  
Not ratified.

Purpose

This document defines the role-to-authority baseline for governance review during Phase 2. It demonstrates the required separation between identity, role, and decision authority.

Conceptual matrix

| Role | Identity | Authority Type | Typical Decision Scope | Notes |
|---|---|---|---|---|
| Proposal Author | registered identity | proposal creation | proposal drafting | cannot be sole final approver |
| Reviewer | registered identity with review role | review authority | review and assessment | independent review expected |
| Approver | registered identity with approval role | decision authorization | approve / reject | must be checked against authority scope |
| Activator | registered identity with activation role | operational activation | activation or deployment | must be separate from approver |
| Verifier | registered identity with verification role | evidence validation | audit / verification | must remain independent |
| Registry Admin | registered identity | registry administration | identity lifecycle admin | must not be the sole approval authority |

Required checks

- identity is registered and active
- signer role is valid for action type
- authority scope covers the decision context
- key is active and not revoked
- decision time is within the valid role period

Design rule

A valid identity alone is insufficient to prove governance authority. Authority must be evaluated against the specific decision context and active policy version.

