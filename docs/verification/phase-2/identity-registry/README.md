# MeeChain Phase 2 — Identity Registry Design Baseline

Status: DRAFT v0.1  
Not ratified.

Purpose

This document defines the design baseline for an identity registry framework for MeeChain governance review. It is not a deployment specification and is not a production registry design.

Identity registry requirements

- unique identifier for each identity
- active/inactive status
- role mapping
- public key binding
- authority scope
- policy version attached to role assignment
- revocation status and evidence
- auditability of identity history

Minimum data model

```json
{
  "identity_id": "string",
  "identity_type": "human|organization|service|validator",
  "status": "active|inactive|suspended|revoked",
  "public_key": "string",
  "role_assignments": [],
  "authority_scope": [],
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "revocation_status": "none|pending|revoked",
  "policy_version": "string"
}
```

Design rules

- Private keys must not be stored in a registry unless explicitly required for a specific controlled system and approved by policy.
- Registry records must preserve historical versions for audit.
- Role assignments must be time-bounded when appropriate.
- Authority scope must be checked at decision time.
- A registry entry is not proof of authority by itself.

Registry status boundary

This design baseline does not authorize:

- production identity registry deployment
- live key issuance
- validator registration
- Mainnet identity creation

