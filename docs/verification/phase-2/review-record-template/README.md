# Review Record Template

Status: DRAFT v0.1

Purpose

This template is used to record actual review results for the Phase 2 review package. Each item must include status, evidence reference, reviewer identity, and review timestamp.

Record structure

- review_id
- review_date
- reviewer_id
- reviewed_document
- document_version
- criterion_id
- criterion_title
- status
- evidence_reference
- reviewer_note
- follow_up_required
- owner
- target_milestone
- acceptance_criteria

Status values

- NOT STARTED
- PENDING REVIEW
- MET
- NOT MET
- DEFERRED
- N/A

Example

```json
{
  "review_id": "REV-TR-001",
  "review_date": "2026-10-30T00:00:00Z",
  "reviewer_id": "did:meechain:reviewer-001",
  "reviewed_document": "MeeChain Phase 2 Trust Policy & Identity Registry Review Checklist",
  "document_version": "DRAFT v0.1",
  "criterion_id": "D-01",
  "criterion_title": "Cryptographic Signature vs Governance Authority",
  "status": "PENDING REVIEW",
  "evidence_reference": [
    "docs/verification/phase-2/trust-identity-review-checklist/README.md"
  ],
  "reviewer_note": "Separation of signature validity and authority validation is defined, but evidence and enforcement details remain pending.",
  "follow_up_required": true,
  "owner": "Security Review Team",
  "target_milestone": "Cryptographic Trust Review",
  "acceptance_criteria": [
    "Signature validation and authority validation are modeled separately",
    "Authority checks are mapped to governance context"
  ]
}
```

Rules

- Every review result must include reviewer identity and review date.
- Every non-N/A result should reference evidence or file paths.
- Deferred items must specify owner and milestone.
- Result status must not be inferred without a review record.

