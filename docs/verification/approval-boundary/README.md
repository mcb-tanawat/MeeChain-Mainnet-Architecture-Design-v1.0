# Approval Boundary

Status: DRAFT v0.1

Purpose

This document defines the legal and operational boundary between document approval, governance ratification, and production authorization. It is intended to prevent the incorrect assumption that a Draft approval means a system is ready for production use.

Approval states

- APPROVE AS DRAFT
  - The document is suitable as a design baseline for review and iteration
  - It does not authorize production operations

- RATIFIED
  - The document or framework has passed the relevant governance process and is formally accepted as a governance standard
  - It still requires operational implementation and evidence readiness before enforcement

- PRODUCTION AUTHORIZED
  - The system or operation has passed the required governance and operational controls and is authorized for live use
  - This requires additional evidence, testing, and authority beyond document approval alone

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

