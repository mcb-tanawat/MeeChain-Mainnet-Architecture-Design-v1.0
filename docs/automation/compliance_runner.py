#!/usr/bin/env python3
"""
Starter compliance runner for MeeChain artifact-based governance validation.

This runner checks the most critical structural rules:
- proposal_id presence and uniqueness (basic)
- proposer != approver (COI guard)
- activation references a decision for the same proposal
- evidence links are present when required
- signatures must be structurally valid and identity-trusted where applicable

Rules:
- PASS = the condition is satisfied with sufficient evidence
- FAIL = evidence is absent or inconsistent
- INDETERMINATE = evidence is insufficient to determine pass/fail safely

No secrets, keys, or production config are embedded in this example.
"""

import argparse
import json
from pathlib import Path


VALID_RESULT_VALUES = {"PASS", "FAIL", "INDETERMINATE"}


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        print(f"ERROR reading {path}: {exc}")
        return None


def is_truthy_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in {"true", "yes", "1"}
    return False


def check_signature(signature_obj):
    if signature_obj is None:
        return "FAIL", "Missing signature object"
    if not isinstance(signature_obj, dict):
        return "FAIL", "Signature is not an object"
    sig = signature_obj.get("signature")
    signer = signature_obj.get("signer")
    signer_type = signature_obj.get("signer_type")
    if not sig:
        return "FAIL", "Missing signature value"
    if not signer:
        return "FAIL", "Missing signer identity"
    if not signer_type:
        return "INDETERMINATE", "Signature exists but signer type is missing"
    # Starter verification: structural only; real trust policy to be added later.
    return "PASS", "Signature structure present and signer identity recorded"


def main(artifacts_path: Path):
    json_files = sorted(artifacts_path.glob("*.json"))
    artifacts = {}

    for p in json_files:
        data = load_json(p)
        if data is not None:
            artifacts[p.stem] = data

    report = []
    status_by_test = {}

    # Proposal checks
    proposal = artifacts.get("proposal")
    if not proposal:
        report.append("FAIL: proposal.json is missing")
        status_by_test["GOV-004"] = "FAIL"
    else:
        if "proposal_id" not in proposal or not proposal.get("proposal_id"):
            report.append("FAIL: proposal.json missing proposal_id")
            status_by_test["GOV-004"] = "FAIL"
        else:
            status_by_test["GOV-004"] = "PASS"

    # Decision checks
    decision = artifacts.get("decision")
    if decision:
        if decision.get("proposal_id") != proposal.get("proposal_id") if proposal else True:
            report.append("FAIL: decision.proposal_id does not match proposal")
            status_by_test["GOV-003"] = "FAIL"
        else:
            status_by_test["GOV-003"] = "PASS"
        if decision.get("approver") and proposal and decision.get("approver") == proposal.get("proposer"):
            report.append("FAIL: COI - proposer is also final approver")
            status_by_test["SOP-001"] = "FAIL"
        elif proposal and decision.get("approver"):
            status_by_test["SOP-001"] = "PASS"
    else:
        status_by_test["GOV-003"] = "INDETERMINATE"
        status_by_test["SOP-001"] = "INDETERMINATE"

    # Activation checks
    activation = artifacts.get("activation")
    if activation:
        if proposal and activation.get("proposal_id") != proposal.get("proposal_id"):
            report.append("FAIL: activation.proposal_id does not match proposal")
            status_by_test["GOV-003"] = "FAIL"
        elif decision and proposal:
            status_by_test["GOV-003"] = "PASS"

        if activation.get("activation_tx"):
            status_by_test["AUD-003"] = "PASS"
        else:
            status_by_test["AUD-003"] = "FAIL"
    else:
        status_by_test["AUD-003"] = "INDETERMINATE"

    # Verification checks
    verification = artifacts.get("verification")
    if verification:
        status = verification.get("status")
        if status not in VALID_RESULT_VALUES:
            report.append("FAIL: verification.status is absent or invalid")
            status_by_test["AUD-004"] = "FAIL"
        elif status == "PASS":
            status_by_test["AUD-004"] = "PASS"
        elif status == "INDETERMINATE":
            status_by_test["AUD-004"] = "INDETERMINATE"
        else:
            status_by_test["AUD-004"] = "FAIL"
    else:
        status_by_test["AUD-004"] = "INDETERMINATE"

    # Evidence completeness rules
    if proposal:
        evidence_links = proposal.get("evidence_links") or []
        if not evidence_links:
            report.append("FAIL: proposal evidence_links missing")
            status_by_test["AUD-005"] = "FAIL"
        else:
            status_by_test["AUD-005"] = "PASS"
    else:
        status_by_test["AUD-005"] = "INDETERMINATE"

    # Signature verification checks
    for artifact_name in ("proposal", "review", "decision", "activation", "verification"):
        artifact = artifacts.get(artifact_name)
        if not artifact:
            continue
        signatures = artifact.get("signatures")
        if not signatures:
            # Some artifacts may intentionally omit signatures; treat as a missing evidence condition.
            if artifact_name in {"proposal", "decision", "activation"}:
                report.append(f"FAIL: {artifact_name}.json has no signatures recorded")
                status_by_test["GOV-001"] = "FAIL" if artifact_name == "decision" else status_by_test.get("GOV-001", "INDETERMINATE")
            continue
        if not isinstance(signatures, list):
            report.append(f"FAIL: {artifact_name}.json signatures field is not a list")
            continue
        for idx, sig in enumerate(signatures):
            result, reason = check_signature(sig)
            if result == "FAIL":
                report.append(f"FAIL: {artifact_name}.json signature #{idx} :: {reason}")
            elif result == "INDETERMINATE":
                report.append(f"INDETERMINATE: {artifact_name}.json signature #{idx} :: {reason}")

    # COI classification: if missing evidence, no result should be forced to PASS.
    if proposal and decision and proposal.get("proposer") and decision.get("approver"):
        if proposal.get("proposer") == decision.get("approver"):
            report.append("FAIL: proposer and approver are the same identity")
            status_by_test["GOV-001"] = "FAIL"
        else:
            status_by_test["GOV-001"] = status_by_test.get("GOV-001", "PASS")
    elif proposal and not decision:
        status_by_test["GOV-001"] = "INDETERMINATE"

    # Ensure test statuses are valid
    for test_id, value in list(status_by_test.items()):
        if value not in VALID_RESULT_VALUES:
            status_by_test[test_id] = "INDETERMINATE"

    # Print summary
    print("Compliance Summary")
    print("==================")
    for test_id in [
        "GOV-001", "GOV-002", "GOV-003", "GOV-004", "GOV-005",
        "SOP-001", "SOP-002", "SOP-003", "SOP-004", "SOP-005",
        "SEC-001", "SEC-002", "SEC-003", "SEC-004", "SEC-005",
        "AUD-001", "AUD-002", "AUD-003", "AUD-004", "AUD-005",
        "EMG-001", "EMG-002", "EMG-003", "EMG-004", "EMG-005"
    ]:
        print(f"{test_id}: {status_by_test.get(test_id, 'INDETERMINATE')}")

    if report:
        print("\nDetails")
        print("=======")
        for message in report:
            print(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Starter compliance runner for MeeChain governance evidence checks")
    parser.add_argument("--artifacts-path", type=str, default="docs/templates", help="Folder containing artifact json files")
    args = parser.parse_args()
    main(Path(args.artifacts_path))
