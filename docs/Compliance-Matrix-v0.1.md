# Compliance Matrix v0.1 (artifact-ready)

This document captures compliance tests in a machine/actionable-friendly format so that engineering, QA และผู้ตรวจสอบอิสระสามารถรันการตรวจสอบได้จริง

Governance

- GOV-001: Proposer must not be Final Approver — Evidence: Proposal metadata, Approval signatures
- GOV-002: Review must come from authorized Reviewer(s) — Evidence: Review records, reviewer IDs
- GOV-003: Activation must match Approval — Evidence: Approval record ↔ activation tx
- GOV-004: Proposal must have unique ID — Evidence: Proposal registry
- GOV-005: Change history must be complete — Evidence: changelog, signed commits

Separation of Powers

- SOP-001: Proposer ≠ Final Approver — check role assignments
- SOP-002: Reviewer ≠ Sole Activator
- SOP-003: Developer ≠ Sole Reviewer
- SOP-004: Council ≠ Unlimited Authority
- SOP-005: Verify Layer separated from Activate Layer

Security

- SEC-001: Protocol changes require Governance-approved Proposal
- SEC-002: No bypass channel exists to change protocol without Approval
- SEC-003: Admin actions are auditable and recorded
- SEC-004: High-privilege grants are logged and reviewable
- SEC-005: Runtime behavior matches approved configuration

Auditability

- AUD-001: Proposal ↔ Review linkage exists
- AUD-002: Review ↔ Approval linkage exists
- AUD-003: Approval ↔ Activation linkage exists
- AUD-004: Activation ↔ Verification linkage exists
- AUD-005: Full evidence trail retrievable for a given Proposal ID

Emergency

- EMG-001: Emergency action has documented rationale
- EMG-002: Emergency action has explicit approver(s)
- EMG-003: Emergency action has expiry
- EMG-004: Post-incident review produced and linked
- EMG-005: Emergency did not produce permanent authority changes without governance flow

Test artifacts & automation

- Define canonical artifact names: proposal.json, review.json, decision.json, activation.json, verification.json
- Define storage / discovery: IPFS / on-chain registry / signed logs
- Define automated checks: role checks, signature checks, activation vs approval matching, evidence completeness

Next steps

- แปลงข้อทดสอบเป็นชุด script/queries (e.g., SQL/duckdb / on-chain queries) และ CI checks
- สร้างตัวอย่าง artifact และ runner สำหรับทีม QA
