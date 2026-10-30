# MeeChain Verification Framework

Status: DRAFT v0.1  
Not ratified.

Purpose

This directory defines the evidence-first verification model for MeeChain governance and operational compliance. It is intended to provide a reviewable baseline for governance evidence, identity authority, runtime verification, and independent audit.

Important notice

> All records and artifacts in this directory are illustrative examples or previously reported observations only. They do not represent actual governance approvals, live network authorization, or verified runtime evidence unless explicitly attached and independently reviewed.

Core principles

- Governance must be proven by evidence, not by declaration alone.
- Identity authority must be distinct from signature validity.
- Evidence status must be separated from finding status.
- INDETERMINATE must not be treated as PASS.
- Draft review does not authorize production operations.

Result semantics

- PASS — sufficient evidence exists; the condition is satisfied and is verifiable.
- FAIL — sufficient evidence exists; the condition is not satisfied.
- INDETERMINATE — evidence is missing, conflicting, or insufficient; it cannot safely be treated as PASS.

> INDETERMINATE MUST NOT be treated as PASS in CI, governance approval, or production activation.

Evidence status semantics

- AVAILABLE — evidence object exists and is identifiable
- ATTACHED — evidence is linked to the relevant record or artifact
- VERIFIED — evidence has been validated against the review criteria
- NOT AVAILABLE — evidence is missing or not yet collected

Important distinction

- Evidence status is not the same as finding status.
- A record may have evidence status = ATTACHED but finding result = PASS — LIMITED or INDETERMINATE depending on review scope and sufficiency.

Review package overview

This verification package contains the following documents:

- README.md — overview and framework description
- reviewer-checklist/README.md — review criteria A–L for governance evidence and enforcement readiness
- review-metadata/README.md — metadata for a specific review cycle
- deferred-work-register/README.md — tracking unresolved or deferred items
- approval-boundary/README.md — explains the boundary between Draft approval, ratification, and production authorization
- record-001/README.md — sample record of observations and evaluation findings
- evidence-register-001/README.md — evidence tracking register for proposal-linked records

Evidence model

1. Policy Layer
   - Constitution
   - Governance Charter
   - Governance Powers Matrix
   - Defines who is authorized to do what

2. Decision Layer
   - Proposal
   - Review
   - Decision / approval record
   - Signature and authority evidence
   - Proves the decision was made through the required governance process

3. Execution Layer
   - Code repository state
   - CI checks
   - Deployment records
   - Activation logs
   - Proves the approved decision was implemented in the actual system

4. Runtime Layer
   - Node state
   - Configuration state
   - Runtime behavior and observability data
   - Proves runtime behavior matches the approved change

5. Independent Evidence Layer
   - Evidence register
   - Verification records
   - Audit logs
   - Proves outcomes without relying only on actor statements or operator reports

Required evidence quality controls

- Evidence must be attributable to an actor or system identity
- Evidence must include timestamp and source reference
- Evidence must be linked to the governing proposal or decision
- Missing evidence cannot be silently treated as PASS
- If evidence is incomplete, the result must be INDETERMINATE
- A signer may be cryptographically valid but still not authorized for the relevant decision

Signature verification policy (draft)

The verification framework distinguishes between cryptographic validity and governance authority.

- signature_is_cryptographically_valid
  - verifies the signature structure and cryptographic validity
- signer_is_authorized_for_decision
  - verifies that the signer identity is authorized to perform the relevant governance action under the governance charter / powers matrix

These checks must remain separate. A cryptographically valid signature does not by itself prove governance authority.

Document lifecycle

- DRAFT → REVIEW → RATIFIED → ACTIVE → SUPERSEDED → ARCHIVED

Evidence records must preserve the proposal lifecycle and remain queryable by proposal_id, decision_id, or activation_id.

Approval boundary summary

- APPROVE AS DRAFT
  - suitable as a design baseline, review tool, or framework iteration artifact
  - does not authorize production operations

- RATIFIED
  - formally accepted through governance process
  - requires evidence readiness and operational implementation before enforcement

- PRODUCTION AUTHORIZED
  - a system or operation has passed the required governance and operational controls
  - requires evidence beyond document approval alone

Reference documents

- docs/Compliance-Matrix-v0.1.md
- docs/templates/README.md
- docs/automation/compliance_runner.py
- docs/verification/reviewer-checklist/README.md
- docs/verification/review-metadata/README.md
- docs/verification/deferred-work-register/README.md
- docs/verification/approval-boundary/README.md

Status note

This directory is a DRAFT review package for governance evidence and verification. It is not yet ratified and must not be construed as production authorization, Mainnet authorization, or a declaration that the network has passed governance or security review.
