#!/usr/bin/env python3
"""
Simple compliance runner to validate template artifacts.
Checks implemented:
- proposal has proposal_id
- proposer != approver (basic COI check) when approver present
- activation references an existing decision for the same proposal

This is a starter example — integrate into CI and extend checks to signature validation, on-chain lookups, and artifact storage checks.
"""
import argparse
import json
from pathlib import Path


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as e:
        print(f"ERROR reading {path}: {e}")
        return None


def main(artifacts_path: Path):
    artifacts = {}
    for p in artifacts_path.glob('*.json'):
        data = load_json(p)
        if not data:
            continue
        t = p.stem
        artifacts[t] = data

    report = []

    # Basic checks
    proposal = artifacts.get('proposal')
    decision = artifacts.get('decision')
    activation = artifacts.get('activation')

    if not proposal:
        report.append('MISSING: proposal.json')
    else:
        if 'proposal_id' not in proposal:
            report.append('FAIL: proposal missing proposal_id')

    if decision and proposal:
        if decision.get('proposal_id') != proposal.get('proposal_id'):
            report.append('FAIL: decision.proposal_id does not match proposal')
        if decision.get('approver') == proposal.get('proposer'):
            report.append('FAIL: COI - proposer is also approver')

    if activation and decision:
        if activation.get('proposal_id') != decision.get('proposal_id'):
            report.append('FAIL: activation.proposal_id does not match decision')

    if not report:
        print('OK: Basic compliance checks passed')
    else:
        print('\n'.join(report))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--artifacts-path', type=str, default='docs/templates', help='Path to artifact JSON files')
    args = parser.parse_args()
    main(Path(args.artifacts_path))
