# MeeChain Phase 2 — Deferred Work Register

Status: DRAFT v0.1

Purpose

This register records deferred items for Phase 2. Deferred items are not treated as passed. Each record must include owner, milestone, acceptance criteria, and review authority.

Items

| ID | Deferred Work | Owner | Target Milestone | Acceptance Criteria | Review Authority |
|---|---|---|---|---|---|
| DEFER-TR-001 | Trust Policy Definition | Governance / Policy Team | Trust Policy Review | Policy purpose, ownership, review process, versioning defined | Governance Council / Review Board |
| DEFER-TR-002 | Identity Registry Architecture | Identity Governance Team | Registry Design Review | Registry model, data elements, lifecycle rules defined | Governance Review Board |
| DEFER-TR-003 | Role and Authority Matrix | Governance Review Team | Governance Authority Review | Roles, authority mappings, context checks defined | Review Authority |
| DEFER-TR-004 | Signature Verification Policy | Security / Crypto Review | Cryptographic Trust Review | Signature validity vs authority separation defined | Security Review Board |
| DEFER-TR-005 | Revocation and Recovery Policy | Identity Governance Team | Identity Lifecycle Review | Recovery, revocation, and evidence rules defined | Governance Council |
| DEFER-TR-006 | Evidence Storage and Retention | Governance / Audit Team | Evidence Governance Review | Storage, retention, access rules defined | Audit Review Board |
| DEFER-TR-007 | Canonical Identity and Authority Schema | Architecture / Data Team | Schema Review | Identity, authority, and decision schema defined | Architecture Review Group |
| DEFER-TR-008 | Governance Enforcement Rules | Governance / Enforcement Team | Enforcement Design Review | Enforcement boundaries and audit triggers defined | Governance Council |

Rules

- Every deferred item must have owner and milestone.
- Deferred items must not be counted as pass.
- Deferred items must be reviewed again in the next review cycle.
- If owner is unknown, status must be UNASSIGNED — OWNER REQUIRED.

