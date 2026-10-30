# Approval Boundary

Status: DRAFT v0.1

Purpose

This document defines the legal and operational boundary between document approval, governance ratification, and production authorization. It is intended to prevent the incorrect assumption that a draft approval means a system is ready for production use.

Approval states

- APPROVE AS DRAFT
  - the document is suitable as a design baseline for review and iteration
  - it does not authorize production operations

- RATIFIED
  - the document or framework has passed the relevant governance process and is formally accepted as a governance standard
  - it still requires operational implementation and evidence readiness before enforcement

- PRODUCTION AUTHORIZED
  - the system or operation has passed the required governance and operational controls and is authorized for live use
  - this requires additional evidence, testing, and authority beyond document approval alone

Rules

- Draft approval does not imply ratification.
- Ratification does not imply production authorization.
- Production authorization requires independent evidence and operational confirmation.
- The framework must explicitly state that Draft review does not authorize network operation, public RPC, Genesis change, or live activation.

Example

```text
Document review state: APPROVE AS DRAFT
Governance status: NOT RATIFIED
Production status: NOT AUTHORIZED
```

This document is a guardrail against over-interpretation of draft review outcomes.
