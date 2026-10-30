# Deferred Work Register

Status: DRAFT v0.1

Purpose

This register records all requirements that are deferred, not yet satisfied, or intentionally delayed. It exists to ensure that deferred items are not silently ignored.

Required register fields

- item_id: unique identifier for the deferred item
- title: short description of the deferred work
- description: rationale and context
- status: DEFERRED
- owner: responsible person or role
- target_milestone: planned milestone or review cycle
- acceptance_criteria: measurable completion standard
- review_authority: who has authority to decide completion
- last_reviewed: date of last review
- notes: current status and blockers

Example entry

```json
{
  "item_id": "DEFER-001",
  "title": "Trusted Identity Registry",
  "description": "Define a trusted identity registry for signer authorization under governance roles.",
  "status": "DEFERRED",
  "owner": "Governance / Identity Policy Team",
  "target_milestone": "Trust & Identity Policy Review",
  "acceptance_criteria": [
    "Registry model documented",
    "Role-to-identity mapping defined",
    "Signer authorization logic specified"
  ],
  "review_authority": "Governance Council / Review Board",
  "last_reviewed": "2026-10-30T00:00:00Z",
  "notes": "Deferred until framework definition and governance role model are reviewed."
}
```

Rules

- Every deferred item must have an owner and milestone
- Deferred items cannot remain pending indefinitely without a review record
- A deferred item must not be treated as PASS
- A deferred item must be reviewed again in the next governance review cycle
