# Review Metadata

Status: DRAFT v0.1

Purpose

This document records the metadata for a peer review of the MeeChain Verification Framework. It is intended to document who reviewed the draft, when the review occurred, which version was reviewed, and what scope was assessed.

Important notice

> This document is a metadata template and example only. It must not be treated as an actual review approval record, evidence of a ratified decision, or proof that a review occurred unless it is populated by an actual reviewer with an actual review date, reviewer identity, evidence references, and review outcome.

Required metadata fields

- review_id: unique identifier for the review record
- reviewed_document: title and version of the reviewed framework
- reviewer_id: identity of the reviewer or review team
- review_date: date and time of review
- review_scope: explicit scope of review
- review_result: APPROVE AS DRAFT / REQUEST CHANGES / REJECT
- review_status: DRAFT / IN REVIEW / COMPLETE
- evidence_reference: links to evidence or record artifacts reviewed
- assumptions: any scope limitations or assumptions
- owner: governance or documentation owner for next actions

Example

```json
{
  "review_id": "REVIEW-META-001",
  "reviewed_document": "MeeChain Verification Framework",
  "document_version": "DRAFT v0.1",
  "reviewer_id": "did:meechain:reviewer-001",
  "review_date": "2026-10-30T00:00:00Z",
  "review_scope": "Framework design baseline review; not a production assurance review",
  "review_result": "APPROVE AS DRAFT",
  "review_status": "COMPLETE",
  "evidence_reference": [
    "docs/verification/README.md",
    "docs/verification/record-001/README.md",
    "docs/verification/evidence-register-001/README.md"
  ],
  "assumptions": [
    "This review is limited to framework design and evidence traceability",
    "Production authorization is explicitly out of scope"
  ],
  "owner": "Governance Review Team"
}
```

Review metadata must not replace evidence itself

- Review metadata records who reviewed the framework and when.
- It does not replace evidence, authority, or runtime verification.
- It can be used to support auditability and traceability of review activity.
- The example values above are illustrative only and must not be used as actual approval evidence without a real review record and evidence reference.
