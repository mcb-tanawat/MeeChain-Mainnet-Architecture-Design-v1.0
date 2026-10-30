MEECHAIN-VERIFICATION-RECORD-001

Initial Environment, Besu CLI & Genesis Staging Audit

Field| Value
Record ID| MEECHAIN-VERIFICATION-RECORD-001
Version| 0.3 — Pending Review
Status| "DRAFT — PENDING REVIEW"
Independent review| Not started
Approver| Not designated
Official archive| Not archived
Mainnet readiness| "NOT READY — MAINNET NOT APPROVED"

Working source: "Notion Record 001" (https://app.notion.com/p/33672e59addd4fae9607d5448be2bacc)

«This is a documentation copy of the working record. It is not an approval record and does not certify that raw evidence is attached or independently verified. This revision improves evidence traceability only; it does not represent new VM inspection or new technical testing.»

1. Purpose and scope

This record consolidates previously reported observations from the Debian Lab VM, Java 25 runtime, Besu 26.10.2 CLI checks, and existing Genesis/validator staging documents.

No new VM inspection, Genesis validation, setup-script execution, key generation, node startup, or network test is represented by this copy. Historical specifications for other VM instances must not be assumed to describe the current Lab VM.

2. Roles and independence

Role| Assignment| Status
Inspector| Not designated| Pending
Independent Reviewer| Not designated| Not started
Approver| Not designated| Not assigned

The roles are intentionally unnamed. The document author or proposer must not be treated as the independent reviewer or final approver by default. Any role overlap must be disclosed with limitations and compensating controls. The independent reviewer must not be the sole producer of the evidence being reviewed; any unavoidable overlap must be disclosed and handled through documented compensating controls approved by the designated authority.

3. Version history

Version| Description| Status
0.1| Initial draft| Superseded by 0.2
0.2| Separates finding and evidence status; adds role separation, version controls, and Evidence Register linkage| Superseded by 0.3
0.3| Adds explicit Finding-to-Evidence ID traceability and clarifies evidence separation for JVM workload, historical crashes, and JFR smoke testing| "DRAFT — PENDING REVIEW"
1.0| Reserved until independent review and formal approval are complete| Not issued

A version number is not evidence of approval.

4. Findings

Finding result status and evidence review status are separate. The result labels below describe only the stated test scope and do not imply that raw artifacts passed independent review.

Finding ID| Subject| Finding result| Evidence ID(s)| Evidence status / limitation
FND-ENV-001| Lab VM environment| "OBSERVED — CONFIGURATION REPORTED"| EV-001| Evidence pending. Limbo configuration was reported as 4096 MB RAM for "meechain-test.qcow2"; guest-visible memory must not be inferred from the emulator setting.
FND-JVM-001| JVM workload| "PASS — LIMITED JVM WORKLOAD TEST"| EV-002A| "PENDING EVIDENCE REVIEW". Reported 100,000,000 iterations produced checksum "13358191874298266279" for both JIT and interpreter; JIT 1,595 ms, interpreter 317,163 ms. This is not a general JVM stability certification.
FND-JFR-001| Historical JVM crashes| "INDETERMINATE — ROOT CAUSE UNKNOWN"| EV-002B| Historical crash logs were reported; original artifacts are not attached or independently reviewed. Root cause remains unknown. These historical crash records are distinct from the later JFR smoke-test recording.
FND-JFR-002| JFR smoke test| "PASS — LIMITED TEST"| EV-002C| "PENDING EVIDENCE REVIEW". JIT without JFR 1,590 ms; with JFR 1,162 ms; a short recording was created and its summary read. No performance conclusion should be drawn from one comparison; this does not close FND-JFR-001.
FND-BESU-001| Besu 26.10.2 CLI| "PASS — CLI SCOPE ONLY"| EV-003| "PENDING EVIDENCE REVIEW". Reported version/help commands exited successfully. This does not prove node startup, Genesis validity, validator readiness, QBFT consensus, or production readiness.
FND-GEN-001| Genesis staging file| "OBSERVED — EMPTY FILE REPORTED"| EV-004| Evidence pending. "genesis.json" was reported as 0 bytes; it is not a valid Genesis candidate and must not be overwritten as part of this record.
FND-APR-001| Genesis approval record| "OBSERVED — NO APPROVAL EVIDENCE"| EV-005| Evidence pending. The approval record was reported as 0 bytes; an empty file is not approval evidence.
FND-VAL-001| Validator configuration inventory| "OBSERVED — FILES REPORTED"| EV-006| Evidence pending. Four node configuration files were reported. Their presence does not prove valid configuration, validator identity, key custody, or deployment independence.
FND-DOC-001| Network specification discovery| "OBSERVED — SCOPE LIMITED"| EV-007| Evidence pending. A prior search did not find "NETWORK_SPEC_v0.1.md" in the specified staging path. This does not establish that it is absent elsewhere.
FND-VER-001| Client version target| "INDETERMINATE — VERSION TARGET NOT APPROVED"| EV-007| Genesis notes were reported to reference Besu 25.7.1 as pending, while CLI checks used 26.10.2. No approved target-version decision is established here.
FND-QBFT-001| QBFT runtime and consensus| "NOT TESTED"| None — not tested| No node startup, block production, validator participation, or QBFT consensus evidence is recorded. No QBFT test is authorized by this record.

5. Evidence linkage

"Evidence Register 001" (../evidence-register-001/README.md) tracks the artifacts required for these findings. The register is now version 0.2 and remains "DRAFT — INCOMPLETE". EV-002 is separated into EV-002A (JVM workload), EV-002B (historical JVM crashes), and EV-002C (JFR smoke test). An Evidence ID does not mean an artifact is attached, complete, or verified.

If an artifact is unavailable, retain the stated limitation; do not invent a substitute path, timestamp, checksum, or review result.

6. Review and approval gates

1. Evidence intake: identify source, environment, collector, timestamp, method, artifact, and custody location.
2. Integrity and completeness: verify artifact presence, size, SHA-256, redaction, and traceability.
3. Requirements reconciliation: identify the exact approved Network Specification, Genesis Policy, client-version decision, Genesis provenance, and validator requirements. Draft or unapproved sources must be labelled as such.
4. Independent review: an independent reviewer evaluates evidence and limitations and is not the sole producer of the evidence under review.
5. Decision and approval: an authorized approver records decision, scope, conditions, and date.
6. Controlled archive: freeze the approved record and register as a versioned snapshot and hash the exact archived artifacts.

Passing a documentation gate does not automatically pass a technical network validation gate.

7. Explicit non-authorization

This record does not authorize Genesis creation/modification, validator or node-key generation, setup-script execution, Besu node startup, QBFT testing, public RPC/P2P exposure, or Mainnet launch.

8. Current status

- Record 001: "DRAFT — PENDING REVIEW"
- Evidence Register 001: "DRAFT — INCOMPLETE"
- Independent review: Not started
- Approval: Not granted; approver not designated
- Official archive: Not archived
- Mainnet readiness: "NOT READY — MAINNET NOT APPROVED"
