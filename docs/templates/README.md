# Templates README

This directory contains canonical artifacts and templates to capture the Proposal → Review → Decision → Activation → Verification evidence chain.

Place generated artifacts in a storage location (e.g., repo path, IPFS CID, or on-chain registry) and reference their location in each artifact's metadata.

Artifacts

- proposal.json — canonical fields that describe a Proposal
- review.json — review record produced by authorized Reviewer(s)
- decision.json — signed decision record (approval/reject)
- activation.json — activation record (tx, validators, signatures)
- verification.json — verification report and evidence

Usage

- Use these templates as-is for manual tests, or have tooling generate them when a Proposal flows through the process.
- The compliance runner (../automation/compliance_runner.py) consumes these artifacts to produce a compliance report.
