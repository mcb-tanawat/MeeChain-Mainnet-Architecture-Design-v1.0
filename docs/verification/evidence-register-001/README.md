MEECHAIN-EVIDENCE-REGISTER-001

Evidence Register for Verification Record 001

Field| Value
Register ID| MEECHAIN-EVIDENCE-REGISTER-001
Version| 0.2
Status| "DRAFT — INCOMPLETE"
Applies to| MEECHAIN-VERIFICATION-RECORD-001
Independent review| Not started
Approval| Not granted

Working source: "Notion Evidence Register 001" (https://app.notion.com/p/431f29037f7d4cadad63df216c82f711)

«This register tracks evidence to be collected or linked. It is not raw evidence and does not certify that artifacts are attached, complete, or verified. This revision is documentation-only; it does not represent new VM inspection or new technical testing.»

1. Evidence status definitions

- REPORTED — NOT ATTACHED: A result has been reported, but the original artifact is not attached or linked.
- SOURCE DOCUMENT AVAILABLE — RAW EVIDENCE PENDING: A summary document is available, but the raw evidence it references still requires inspection.
- ATTACHED — PENDING REVIEW: An artifact is attached, but completeness, integrity, provenance, and traceability have not been independently reviewed.
- VERIFIED: An independent reviewer confirmed provenance, completeness, integrity, linkage, and hash.
- INDETERMINATE / NOT AVAILABLE: The source is missing, conflicting, or cannot be recovered. Do not infer a result in place of evidence.

Finding result status is separate. For example, "PASS — LIMITED JVM WORKLOAD TEST" may coexist with "PENDING EVIDENCE REVIEW".

2. Evidence inventory

Evidence ID| Related finding(s)| Required evidence| Current status| Missing information / limitation
EV-001| FND-ENV-001| Existing Limbo configuration showing 4096 MB assigned to "meechain-test.qcow2"; if already available, corresponding guest OS memory output| "REPORTED — NOT ATTACHED"| No artifact path, collection time, SHA-256, or guest-visible memory evidence is registered. New evidence collection must not be treated as authorization to re-inspect the VM.
EV-002A| FND-JVM-001| Original JIT and interpreter workload outputs; iteration count, elapsed time, full checksum; Java build and relevant runtime flags| "REPORTED — NOT ATTACHED"| Reported: 100,000,000 iterations; checksum "13358191874298266279" for both runs; JIT 1,595 ms; interpreter 317,163 ms. Raw output, run count, timestamps, Java flags, artifact path, and hash are not attached. This supports only the limited workload finding, not general JVM stability.
EV-002B| FND-JFR-001| Historical "hs_err_pid*.log" crash reports and associated crash-recording files, preserved as separate original artifacts where available| "REPORTED — NOT ATTACHED"| Historical JVM crashes were reported, including crashes involving JIT/JFR-related and other Java runtime frames. Original files, exact paths, timestamps, sizes, hashes, and a complete inventory are not attached. Root cause remains unknown; do not merge these historical crash artifacts with the later JFR smoke-test recording.
EV-002C| FND-JFR-002| JIT workload output without JFR and with JFR; generated JFR recording; JFR summary output; Java build and recording options| "REPORTED — NOT ATTACHED"| Reported: JIT without JFR 1,590 ms; with JFR 1,162 ms; a short recording was created and its summary read. Raw outputs, exact command lines, run count, timestamps, recording path, size, and hashes are not attached. One comparison does not establish a performance effect and does not resolve FND-JFR-001.
EV-003| FND-BESU-001| Actual Besu 26.10.2 commands tested, command lines, output, exit status, Java runtime, and collection time| "SOURCE DOCUMENT AVAILABLE — RAW EVIDENCE PENDING"| A Besu 26.10.2 compatibility/readiness assessment was reported as available, but its exact path/URI is not registered here. Raw CLI logs must be linked or explicitly recorded as unavailable. Do not rerun CLI commands automatically.
EV-004| FND-GEN-001| Existing Genesis staging inventory: exact path, 0-byte size, file metadata, SHA-256, and read-only observation record| "REPORTED — NOT ATTACHED"| Exact path and raw artifact are not attached. Do not edit or overwrite the file. An existing file is not an approved Genesis.
EV-005| FND-APR-001| Existing approval-record inventory: exact path, 0-byte size, file metadata, SHA-256, and read-only observation record| "REPORTED — NOT ATTACHED"| Exact path and raw artifact are not attached. An empty approval record is not evidence of approval.
EV-006| FND-VAL-001| Inventory of all four validator configuration files: path, filename, size, timestamp, and SHA-256; secrets excluded| "REPORTED — NOT ATTACHED"| Inventory and hashes are not attached. File presence does not prove validator identity or configuration validity. Never publish private keys, node keys, or secrets.
EV-007| FND-DOC-001, FND-VER-001| Search-scope record for governance documents; result for specified staging path; source/version metadata for Genesis Notes referencing Besu 25.7.1; applicable source documents and version decision| "PARTIAL — SOURCE DOCUMENTS AVAILABLE; SOURCE ARTIFACTS PENDING"| Network Specification and Genesis Policy have been referenced, but exact approved status and authoritative revision must be established from source records. Genesis Notes referencing 25.7.1 and a recorded target-client-version decision are not attached. The prior negative search applies only to its stated path scope.

3. Required metadata for each artifact

When an artifact is linked, record:

- Evidence ID and supported Finding ID(s);
- evidence type: raw output, configuration snapshot, source document, derived summary, or other;
- source system and owner, with environment identified as Lab or Mainnet;
- exact filename and path or URI;
- collection timestamp in ISO 8601 with timezone;
- collector and collection method;
- command/tool and version, where applicable;
- actual file size and SHA-256 of the collected artifact;
- controlled storage location and backup status;
- confidentiality classification, redaction status, and access permissions;
- reviewer, review result, role, and review timestamp;
- change history, without overwriting the original artifact.

Do not place private keys, node keys, credentials, or secrets in this register or in this public repository. Keep originals in an authorized restricted location and publish only a controlled redacted copy or reference.

4. Evidence handling and review gates

Gate A — Evidence intake without creating new data

- [ ] Use only existing artifacts or artifacts explicitly handed over by the system owner. This register does not authorize new VM inspection, setup-script execution, or creation of Genesis, keys, or configuration.
- [ ] If evidence is absent, retain "REPORTED — NOT ATTACHED" or "NOT AVAILABLE". Never guess a path, timestamp, checksum, or SHA-256.
- [ ] Scope every negative search result to the exact path and area actually searched.
- [ ] Identify each artifact as Lab or Mainnet. Do not mix environments, identities, keys, or configuration.

Gate B — Preservation and registration

- [ ] Preserve originals as read-only; use working copies and record the relationship between original and copy.
- [ ] Calculate SHA-256 only from an artifact that exists; record tool/method and time. Never invent hashes for missing files.
- [ ] Preserve metadata and raw output without rewriting prior results or merging results from different collection times.
- [ ] Identify confidential data and complete controlled redaction before placing any copy in a public/shared location.
- [ ] Add new evidence as a new register entry or revision with change history; do not silently replace prior evidence.

Gate C — Reconciliation with MeeChain requirements

- [ ] Confirm target Besu and Java versions from an approved decision before treating Genesis or configuration as validated. The reported difference between Besu 25.7.1 and 26.10.2 remains "INDETERMINATE" until a documented decision resolves it.
- [ ] For Genesis evidence, record provenance, source requirements, Besu version, path, SHA-256, and reviewer. An empty Genesis or approval-record file is not approval.
- [ ] Separate CLI evidence from node startup, validator identity, QBFT consensus, and recovery evidence. CLI help output cannot satisfy those validation gates.
- [ ] Record any Lab validator identity test as "TEST ONLY". Do not reuse Lab keys or identities in Mainnet by default.
- [ ] Establish the exact revision and approval status of Network Specification and Genesis Policy before treating them as binding requirements.

Gate D — Independent review and register closure

- [ ] Every conclusion links to a Finding ID and Evidence ID, or explicitly states that supporting evidence is unavailable.
- [ ] An independent reviewer checks source, path, timestamps, completeness, SHA-256, integrity, and limitations.
- [ ] Record conflicts and limitations; do not relabel contradictions as passed.
- [ ] Identify Inspector, Independent Reviewer, and Approver separately. Disclose role overlap and compensating controls if any. The reviewer must not be the sole producer of the evidence being reviewed; any unavoidable overlap must be disclosed and approved with documented compensating controls.
- [ ] Close the register only when each entry is "VERIFIED", "REJECTED / INDETERMINATE" with reasons, or "NOT AVAILABLE" with a bounded search scope. A complete list does not mean every artifact passed.
- [ ] Only after Record and Register complete independent review and formal approval should an exact snapshot be frozen, hashed, and archived under the controlled document lifecycle.

5. Version history

Version| Description| Status
0.1| Initial evidence tracking register for Record 001| Superseded by 0.2
0.2| Separates JVM workload, historical JVM crash, and JFR smoke-test evidence into distinct entries; clarifies the unregistered path for the reported Besu assessment and strengthens reviewer independence wording| "DRAFT — INCOMPLETE"

6. Current status

- EV-001 through EV-007: tracking entries only; raw artifacts remain unattached or unreviewed. EV-002 is split into EV-002A, EV-002B, and EV-002C as detailed above.
- Evidence Register 001: "DRAFT — INCOMPLETE"
- Verification Record 001: "DRAFT — PENDING REVIEW"
- Independent review: Not started
- Approval: Not granted
- Official archive: Not archived
- Technical re-inspection: Not performed and not authorized by this registed
