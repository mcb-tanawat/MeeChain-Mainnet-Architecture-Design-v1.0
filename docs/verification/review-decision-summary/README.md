# Review Decision Summary Template

Status: DRAFT v0.1

Purpose

This template is used to summarize the final outcome of a review cycle. It is intended to keep review results concise while remaining evidence-based and traceable.

Important notice

> This is a template and example only. It is not an actual review decision unless filled by a reviewer with real evidence references, real review timestamps, and a real review outcome.

Required fields

- review_id
- review_date
- reviewer_id
- reviewed_document
- version
- review_scope
- overall_result
- summary
- deferred_items
- not_met_items
- evidence_reference
- next_review_target

Allowed result values

- APPROVE AS DRAFT
- REQUEST CHANGES BEFORE CLOSURE
- REJECT

Example

```json
{
  "review_id": "REV-SUMMARY-001",
  "review_date": "2026-10-30T00:00:00Z",
  "reviewer_id": "did:meechain:reviewer-001",
  "reviewed_document": "MeeChain Verification Framework",
  "version": "DRAFT v0.1",
  "review_scope": "Review package completeness and governance boundary review",
  "overall_result": "REQUEST CHANGES BEFORE CLOSURE",
  "summary": "Package structure is largely in place, but missing closure items remain before Phase 1 can be closed.",
  "deferred_items": [
    "Trust & Identity Policy Review",
    "Evidence Storage & Retention Policy Review"
  ],
  "not_met_items": [
    "Reviewer Checklist still requires review-record traceability",
    "Deferred work register needs owner/milestone mapping"
  ],
  "evidence_reference": [
    "docs/verification/README.md",
    "docs/verification/reviewer-checklist/README.md",
    "docs/verification/deferred-work-register/README.md"
  ],
  "next_review_target": "Phase 1 closure review after package completeness and metadata alignment"
}
```

Rules

- Overall review decision must be based on the actual review records, not on the checklist template alone.
- A review summary must not infer production authorization.
- Deferred items and not-met items must remain traceable to their corresponding review records.
- The example above is illustrative only and must not be treated as an actual review decision without a valid review record and evidence reference.
