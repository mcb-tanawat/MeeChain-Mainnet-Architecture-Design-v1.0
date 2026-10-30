MeeChain Verification Documentation

Status: Working drafts — not approved
Mainnet status: "NOT READY — MAINNET NOT APPROVED"

This directory contains version-controlled verification documentation. It does not contain raw VM evidence, node data, Genesis artifacts, validator keys, credentials, or production configuration.

Documents

Document| Version| Status| Purpose
"Verification Record 001" (./record-001/README.md)| 0.3| "DRAFT — PENDING REVIEW"| Initial environment, JVM/JFR, Besu CLI, and Genesis staging findings
"Evidence Register 001" (./evidence-register-001/README.md)| 0.2| "DRAFT — INCOMPLETE"| Tracks evidence required to support Record 001

Working sources

- "Record 001 — Notion" (https://app.notion.com/p/33672e59addd4fae9607d5448be2bacc)
- "Evidence Register 001 — Notion" (https://app.notion.com/p/431f29037f7d4cadad63df216c82f711)
- "MeeChain verification and reporting standard" (https://app.notion.com/p/8c4d8f8cfd3c45b6a14a85fd2dfed670)

Notion is the working review/governance workspace. This directory is a version-controlled documentation mirror. A Git commit is not independent review, approval, ratification, or authorization to operate Mainnet.

Evidence handling rules

1. Keep raw evidence in an access-controlled workspace. Never publish private keys, node keys, credentials, personal data, secrets, or unredacted sensitive logs in this public repository.
2. Publish only reviewed, appropriately redacted documentation and evidence references.
3. Never invent a path, timestamp, checksum, SHA-256, reviewer, approval, or evidence status.
4. Keep finding result status separate from evidence review status.
5. Preserve original artifacts. Add new evidence records rather than silently replacing prior evidence.
6. Identify each artifact as Lab or Mainnet. Never mix identities, keys, configuration, or data between environments.
7. CLI help output is not proof of node startup, validator readiness, QBFT consensus, recovery, or production readiness.
8. Evidence IDs are traceability references only; they do not prove that an artifact is attached, complete, or verified.

Change control

Version 1.0 is reserved until independent review and formal approval have actually been completed and recorded. Draft revisions may increment while review remains pending.

Explicit non-authorization

These documents do not authorize Genesis creation/modification, validator or node-key generation, setup-script execution, Besu node startup, QBFT testing, public RPC/P2P exposure, or Mainnet deployment.
