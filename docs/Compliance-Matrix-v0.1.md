# Compliance Matrix v0.1 (artifact-ready)

This document captures compliance tests in a machine/actionable-friendly format so engineering, QA, and independent reviewers can validate whether MeeChain is operating according to the Constitution and governance requirements.

Key principles

- PASS only when the required evidence and operational checks are present and verifiable.
- INDETERMINATE means the evidence is insufficient to conclude PASS or FAIL.
- FAIL means the evidence is missing, inconsistent, or a rule violation is identified.
- This matrix is not a blanket security certification; it only confirms whether the test criteria below are satisfied for the tested scope.

Required Charter changes (policy gap tracking)

- RC-001: Governance Council override / rollback authority must be explicitly scoped, time-bounded, and reviewable; Council must not act as a general veto authority.
- RC-002: Key separation must be defined for each role (proposer, reviewer, approver, activator, verifier); no single operating key or system may bypass role separation.
- RC-003: Deployment separation must be defined so that activation authority is independent from approval authority and runtime verification authority.

| Test ID | Requirement | Evidence required | Owner / responsible role | Run frequency | Automation level | Initial status | Pass criteria |
|---------|-------------|------------------|-------------------------|----------------|----------------|----------------|---------------|
| GOV-001 | Proposer must not be Final Approver | Proposal ID, proposer identity, approval record, approver identity | Governance / Approver role | Each proposal | Semi-automated | Not started | Proposal author and final approver are different identities and the approval record is linked to the proposal |
| GOV-002 | Review must come from authorized Reviewer(s) | Review record, reviewer identity, reviewer role assignment | Reviewer / Governance | Each proposal | Semi-automated | Not started | Reviewer identity is authorized and review artifacts are tied to the proposal |
| GOV-003 | Activation must match Approval | Approval record, activation record, proposal ID, decision hash | Validator / Governance | Each activation | Automated | Not started | Activation references the same proposal and approved decision/version |
| GOV-004 | Proposal must have unique ID | Proposal registry or signed artifact with proposal_id | Governance | Each proposal | Automated | Not started | proposal_id is unique and immutable for the reviewed change |
| GOV-005 | Change history must be complete | Proposal log, decision log, activation log, verification log | Governance / Audit | Each proposal | Semi-automated | Not started | The full lifecycle from proposal to verification can be reconstructed |
| SOP-001 | Proposer ≠ Final Approver | Proposal record + final approval record | Governance / Compliance | Each proposal | Automated | Not started | The proposer identity and final approver identity are distinct |
| SOP-002 | Reviewer ≠ Sole Activator | Review record + activation record | Governance / Validator | Each activation | Automated | Not started | Activation is not performed by the same single reviewer without independent approval |
| SOP-003 | Developer ≠ Sole Reviewer | Contributor identity + reviewer identity | Governance / Compliance | Periodic + each review | Semi-automated | Not started | A contributor cannot be the sole reviewer for their own change |
| SOP-004 | Council ≠ Unlimited Authority | Council charter, authority registry, override logs | Governance / Council | Periodic / Triggered | Semi-automated | Not started | Council authority is explicitly scoped and does not self-expand |
| SOP-005 | Verify Layer separated from Activate Layer | Activation artifact, verification artifact, role maps | Validator / Auditor | Each activation | Automated | Not started | Verification is independent from activation and can attest runtime truth |
| SEC-001 | Protocol changes require Governance-approved Proposal | Proposal, decision, code diff, activation log | Governance / Security | Each change | Automated | Not started | Protocol modifications are linked to an approved proposal and decision |
| SEC-002 | No bypass channel exists to change protocol without Approval | Permission registry, admin log, deployment record | Security / Governance | Periodic + triggered | Automated | Not started | There is no path that skips the approval flow |
| SEC-003 | Admin actions are auditable and recorded | Admin logs, identity records, timestamps | Security / Ops | Continuous | Automated | Not started | Security/admin actions are attributable and stored |
| SEC-004 | High-privilege grants are logged and reviewable | Grant logs, approvals, revocation records | Security / Governance | Continuous | Automated | Not started | Privilege changes are logged and restorable for review |
| SEC-005 | Runtime behavior matches approved configuration | Approved config hash, runtime config report, verification logs | Runtime / Audit | Continuous / periodic | Automated | Not started | Runtime state is consistent with approved configuration and change records |
| AUD-001 | Proposal ↔ Review linkage exists | Proposal ID + review record ID | Governance / Audit | Each proposal | Automated | Not started | Every review references a proposal ID |
| AUD-002 | Review ↔ Approval linkage exists | Review ID + decision ID | Governance / Audit | Each proposal | Automated | Not started | Every approval references the review(s) that informed it |
| AUD-003 | Approval ↔ Activation linkage exists | Decision ID + activation ID | Governance / Audit | Each activation | Automated | Not started | Each activation references an approved decision |
| AUD-004 | Activation ↔ Verification linkage exists | Activation ID + verification ID | Governance / Audit | Each activation | Automated | Not started | Each verification references an activation event |
| AUD-005 | Full evidence trail retrievable for a given Proposal ID | Proposal registry, logs, linked artifacts | Governance / Audit | Each proposal | Automated | Not started | All lifecycle artifacts can be retrieved via Proposal ID |
| EMG-001 | Emergency action has documented rationale | Emergency action log, rationale, metadata | Governance / Security | Triggered | Automated | Not started | Emergency action includes a recorded reason and time |
| EMG-002 | Emergency action has explicit approver(s) | Approver identity, decision log | Governance / Security | Triggered | Automated | Not started | Action must identify who approved it |
| EMG-003 | Emergency action has expiry | Expiration timestamp and review window | Governance / Security | Triggered | Automated | Not started | Action has a defined expiry and cannot continue past it without review |
| EMG-004 | Post-incident review produced and linked | Postmortem document, review ID, sign-off | Governance / Security | Triggered | Semi-automated | Not started | A post-incident review exists and is linked to the emergency event |
| EMG-005 | Emergency did not create permanent authority changes without governance flow | Emergency decision log, governance approval log, charter changes | Governance / Security | Triggered | Automated | Not started | Emergency actions do not create permanent authority changes without normal governance processing |

Evidence model and automation notes

- Canonical artifacts (starter set):
  - proposal.json
  - review.json
  - decision.json
  - activation.json
  - verification.json
- Each artifact should include at least:
  - unique ID
  - proposal_id or decision_id/activation_id as applicable
  - signer or actor identity
  - timestamp
  - evidence_links or storage references
  - verification result field or pass/fail status where applicable
- For any artifact containing a signature, the runner must validate that:
  - the signature field exists
  - the signature is structurally valid
  - the signer is recognized under the trust policy
  - the signer identity matches the expected role for the action
  - signature verification is not treated as PASS without identity trust or signature validity

Required automated checks

- Proposal uniqueness and immutability check
- Role consistency check (proposal author != final approver)
- Activation contract check (activation references approved proposal)
- Runtime verification check (runtime state can be compared to approved configuration)
- COI classification logic with explicit INDETERMINATE handling when evidence is insufficient
- Missing evidence detection: if required evidence links are missing, the test fails or is marked INDETERMINATE depending on severity

Next steps

- Turn these tests into CI rules in a dedicated compliance workflow
- Add a trusted identity registry specification before enabling signature verification in automation
- Add a public charter for Council authorization and emergency permissions before treating these checks as binding governance controls

Important note

- PASS under this matrix demonstrates only that the artifact and governance condition for a specific test is satisfied at the current time.
- It is not equivalent to a broader conclusion that the overall MeeChain implementation is secure, stable, or production-ready.

"""

