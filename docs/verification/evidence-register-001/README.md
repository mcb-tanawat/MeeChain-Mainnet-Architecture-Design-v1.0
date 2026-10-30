# Verification Framework Overview

Status: DRAFT v0.1
Purpose: Illustrative governance verification framework only — not yet ratified for production use.

Important notice

> All records and artifacts in this directory are illustrative examples only. They do not represent actual governance events, approvals, activations, or verified runtime evidence.

This directory defines the evidence-first verification model for MeeChain governance and operational compliance.

Purpose

- Make every governance decision traceable to evidence
- Separate policy, code, runtime behavior, and independent audit records
- Provide a consistent record for Proposal → Review → Decision → Activation → Verification

Core rule

> No PASS result is valid without sufficient evidence.

Result semantics

- PASS — sufficient evidence exists, the check is verifiable, and the relevant condition is satisfied.
- FAIL — sufficient evidence exists and the condition is not satisfied.
- INDETERMINATE — evidence is missing, inconsistent, or insufficient to determine PASS or FAIL safely.

> INDETERMINATE MUST NOT be treated as PASS for CI, governance approval, or production activation.

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
   - Signature and authorization evidence
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
   - Proves the runtime behavior matches the approved change

5. Independent Evidence Layer
   - Evidence registers
   - Verification records
   - Audit logs
   - Proves the outcome without relying only on the actor or operator statements

Evidence model details

1. Proposal evidence
   - proposal_id
   - proposer identity
   - change brief
   - links to design, review context, and policy references

2. Review evidence
   - reviewer identity
   - review type (technical / security / economics / governance)
   - result
   - timestamp
   - evidence links and notes

3. Decision evidence
   - decision_id
   - approver identity
   - threshold used
   - final decision outcome
   - signature or equivalent approval record

4. Activation evidence
   - activation_id
   - activation transaction or operation reference
   - target system/component
   - status and timestamp

5. Verification evidence
   - verification_id
   - verifier identity
   - checks performed
   - runtime comparison results
   - report and timestamp

Document lifecycle

- DRAFT → REVIEW → RATIFIED → ACTIVE → SUPERSEDED → ARCHIVED
- Evidence artifacts must preserve the proposal lifecycle and remain queryable by proposal_id or decision_id.

Required evidence quality controls

- Evidence must be attributable to an actor or system identity
- Evidence must include timestamp and source reference
- Evidence must be linked to the governing Proposal or Decision
- Missing evidence cannot be silently treated as PASS
- If evidence is incomplete, the result must be INDETERMINATE

Signature verification policy (draft)

The verification framework distinguishes between cryptographic validity and authority validity.

- signature_is_cryptographically_valid
  - verifies the signature structure and cryptographic validity
- signer_is_authorized_for_decision
  - verifies that the signer identity is authorized to perform the relevant governance action under the governance charter / powers matrix

These checks must be kept separate. A cryptographically valid signature does not by itself prove governance authority.

Reference documents

- docs/Compliance-Matrix-v0.1.md
- docs/templates/README.md
- docs/automation/compliance_runner.py
