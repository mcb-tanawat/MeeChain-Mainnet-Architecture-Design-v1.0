# Pull Request Body

In a nutshell
- This Draft PR expands the Compliance Matrix into an artifact-ready, testable format and adds starter automation to validate the evidence chain Proposal → Review → Decision → Activation → Verification.
- Changes are committed to branch compliance/matrix-detailed-v0.1 and are intentionally not merged to main — this PR is for review of scope, tests, and policy gaps before wider adoption.

What this PR contains
- docs/Compliance-Matrix-v0.1.md — expanded table covering GOV-001..005, SOP-001..005, SEC-001..005, AUD-001..005, EMG-001..005 with the following columns:
  - Test ID, Requirement, Evidence required, Owner/responsible role, Run frequency, Automation level, Initial status, Pass criteria
- docs/templates/ — example artifacts (proposal.json, review.json, decision.json, activation.json, verification.json):
  - Includes PASS, FAIL, and INDETERMINATE examples (no secrets/keys included).
- docs/automation/compliance_runner.py — starter runner that:
  - Validates artifact linkage (proposal↔decision↔activation)
  - Runs basic COI checks (reports INDETERMINATE when evidence insufficient)
  - Validates presence/format of signatures and reportable signature verification result (PASS / FAIL / INDETERMINATE)
  - Emits structured results (PASS / FAIL / INDETERMINATE) per Test ID
- docs/automation/sample_queries.sql — sample DuckDB/SQL queries for automated checks
- docs/README-summary.md — summary & recommended roadmap updates
- Minor updates to Governance-Charter-v0.1.md, Validator-Charter-v0.1.md, Emergency-Powers-Framework-v0.1.md to include “Required Charter changes” markers for:
  - Council override / rollback
  - Key separation (per-role keying / deployment key separation)
  - Deployment / activation separation

Key guarantees & constraints enforced in this work
- PASS means: the test passed the evidence / scope defined for that Test ID only — it is not a security certification for the network.
- Signature checks verify signature presence and run a basic verification step against a trust policy; absence of verifiable signer results in FAIL or INDETERMINATE (per test definition).
- COI checks return INDETERMINATE when evidence is insufficient; the runner will not make a “no COI” conclusion without sufficient evidence.
- No private keys / tokens / secrets / genesis / consensus / validator configs / public RPC changes are included in this work.
- This PR is a Draft to allow policy review before merging.

Testing / How reviewers can run checks
1. Clone the repo and checkout the branch:
   - git fetch origin
   - git checkout compliance/matrix-detailed-v0.1
2. Run the example compliance runner (Python 3.8+):
   - python3 docs/automation/compliance_runner.py --artifacts-path ./docs/templates
   - Expected runner behavior:
     - Prints structured output per Test ID, one of PASS / FAIL / INDETERMINATE
     - Exits cleanly; for this Draft we do not auto-fail CI on INDETERMINATE — the PR is for review
3. Run DuckDB queries (optional):
   - Load artifacts table into DuckDB and run docs/automation/sample_queries.sql to see SQL examples for automated checks
4. Inspect example artifacts:
   - docs/templates contains both passing and failing JSON artifacts; confirm that changing evidence_links or signatures changes the runner outcome as expected

Acceptance criteria (what must be true before merging)
- All Test IDs are present in docs/Compliance-Matrix-v0.1.md with clear Evidence required and Pass criteria
- compliance_runner.py implements:
  - proposal ↔ decision ↔ activation linkage checks
  - basic COI rules (proposer ≠ final approver; returns INDETERMINATE when missing evidence)
  - signature verification step consistent with a documented trust policy (runner reports result and does not assume a signer is valid without verification)
- Runner reports PASS only when evidence is sufficient and verifiable
- No secret material, no genesis/consensus/validator config changes, no public RPC enabled
- PR remains Draft and does not assign reviewers yet

Risks & open policy questions to resolve before merge
- Trust policy for signature verification: which identity/trust registry shall the runner trust? (on-chain DID registry, off-chain signer registry, or manual mapping)
- Exact quorum & threshold values for Governance Charter — the Compliance Matrix tests must be parameterized to use those once decided
- Council override / emergency veto: define explicit policy (who, when, how long, review process). The PR flags these as Required Charter changes but does not change policy yet.
- Deployment signing model: define per-role key custody and key separation specification (documented in Validator Charter / deployment playbooks)

Suggested reviewer actions
1. Review Compliance Matrix table rows and Evidence required columns — confirm coverage and make additions where tests are missing.
2. Review compliance_runner.py semantics for PASS / FAIL / INDETERMINATE and confirm the trust policy approach for signature verification.
3. Confirm the “Required Charter changes” markers (Council override / key separation / deployment separation) and start the policy work to resolve them.
4. Try the runner with the provided sample artifacts and validate that results match expectations (PASS examples → PASS, FAIL examples → FAIL, incomplete evidence → INDETERMINATE).
5. Once policy items are resolved, agree an owner to parameterize the tests (quorum/thresholds/trust registry) and iterate.

Suggested labels (for maintainers)
- docs
- wip
- governance
- compliance

Notes / checklist
- [ ] This PR is Draft and must not be merged until policy gaps are resolved
- [ ] All Test IDs present and have Evidence required and Pass criteria
- [ ] Runner returns PASS only when evidence is sufficient and signatures verified
- [ ] No secrets or configs included
- [ ] Required Charter changes have been acknowledged (Council override, key separation, deployment separation)
- [ ] Trust policy for signature verification has been selected or a path to select it is recorded
