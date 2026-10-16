# Compliance automation

This folder contains a simple runner and example queries to demonstrate how to convert the Compliance Matrix tests into automated checks.

Files:
- compliance_runner.py — simple Python script to validate artifact linkages and basic rules
- sample_queries.sql — example DuckDB/SQL queries to run against an artifacts registry table

How to run

- Python runner: python3 docs/automation/compliance_runner.py --artifacts-path ./docs/templates
- DuckDB queries: load a table of artifact records and run sample_queries.sql
