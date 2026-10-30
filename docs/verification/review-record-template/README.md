# Review Record Template

Status: DRAFT v0.1

Purpose

This template is used to record actual review results for the MeeChain Verification Framework. It is intentionally separate from the static checklist template so that review outcomes remain traceable, attributable, and auditable.

Important notice

> This is a template only. It is not an actual review record or proof of a completed review unless populated by a reviewer with a real reviewer ID, review timestamp, evidence reference, and review outcome.

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
  "review_id": "REV-001",
  "review_date": "2026-10-30T00:00:00Z",
  "reviewer_id": "did:meechain:reviewer-001",
  "reviewed_document": "MeeChain Verification Framework",
  "document_version": "DRAFT v0.1",
  "criterion_id": "A-01",
  "criterion_title": "Document status and classification",
  "status": "MET",
  "evidence_reference": [
    "docs/verification/README.md",
    "docs/verification/reviewer-checklist/README.md"
  ],
  "reviewer_note": "Document clearly states DRAFT and not ratified; production authorization boundary is explicit.",
  "follow_up_required": false,
  "owner": "Governance Review Team",
  "target_milestone": "Phase 1 Closure Review",
  "acceptance_criteria": [
    "Status remains DRAFT",
    "Production authorization remains excluded"
  ]
}
```

Rules

- Every review result must have reviewer identity and review date.
- Every non-N/A result should reference evidence or file paths.
- Deferred items must state owner and milestone.
- Result status must not be inferred without a review record.
- A review record does not replace the framework template; it supplements it with actual decisions.
- The example above is illustrative only and not evidence that a reviewer actually completed the review.
