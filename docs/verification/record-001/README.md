# Evidence Register 001

Status: DRAFT v0.1
Purpose: Illustrative governance evidence inventory only — not yet ratified for production use.

Important notice

> All records and artifacts in this document are illustrative examples only. They do not represent actual governance events, approvals, activations, or verified runtime evidence.

Purpose

This register provides a canonical example of an evidence inventory for a governance event. It is intended to demonstrate how the system should record and map evidence for a compliance review.

Register metadata

- register_id: EVIDENCE-REGISTER-001
- version: v0.1
- status: DRAFT
- owner: Governance / Audit
- scope: Constitutional compliance checks

Tracked proposal

- proposal_id: PROPOSAL-0001
- title: Example governance change for protocol configuration review
- domain: Protocol / Governance

Evidence table

| Evidence type | ID | Source | Linked to | Status |
|---|---|---|---|---|
| Proposal | PROP-0001 | proposal.json | Proposal lifecycle | Available |
| Review | REV-0001 | review.json | PROP-0001 | Available |
| Decision | DEC-0001 | decision.json | PROP-0001 | Available |
| Activation | ACT-0001 | activation.json | DEC-0001 | Available |
| Verification | VER-0001 | verification.json | ACT-0001 | Available |
| Post-mortem | PM-0001 | emergency review file | EMG-0001 | Pending |

Required evidence fields

- id
- type
- issuer or actor
- timestamp
- parent_id or source proposal id
- link to artifact or immutable storage reference
- result state (PASS / FAIL / INDETERMINATE)

Record retention rules

- Evidence must not be deleted without an audit log entry
- Evidence can be superseded, but not silently overwritten
- When evidence is amended, the prior record must remain queryable

Minimum quality gate

An evidence record only qualifies for PASS if all of the following are true:

- identity is attributable
- timestamp exists
- source is present
- link to proposal or decision exists
- verification status is explicit
- no missing data blocks the test outcome

Result semantics

- PASS — evidence is complete and the corresponding condition is satisfied
- FAIL — evidence is complete and the condition is not satisfied
- INDETERMINATE — evidence is incomplete, conflicting, or insufficient to determine PASS or FAIL

> INDETERMINATE MUST NOT be treated as PASS for governance or activation decisions.

Review note

This register is a starter artifact for governance evidence management. Actual production deployments should define:

- the immutable storage layer (on-chain registry, IPFS, signed logs, or controlled repository storage)
- data retention policy
- trusted identity registry
- access policy for confidential evidence
