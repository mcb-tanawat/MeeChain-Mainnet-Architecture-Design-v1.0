-- sample_queries.sql
-- Example DuckDB queries (pseudocode) to validate proposal/activation linkage

-- 1) Ensure every proposal has a unique proposal_id
SELECT proposal_id, COUNT(*) as cnt FROM artifacts WHERE type='proposal' GROUP BY proposal_id HAVING cnt > 1;

-- 2) Find proposals without activation
SELECT p.proposal_id FROM artifacts p WHERE p.type='proposal' AND NOT EXISTS (SELECT 1 FROM artifacts a WHERE a.type='activation' AND a.proposal_id = p.proposal_id);

-- 3) Ensure activation references a decision that matches the proposal
SELECT a.activation_id, a.proposal_id, d.decision_id FROM artifacts a JOIN artifacts d ON a.proposal_id = d.proposal_id WHERE a.type='activation' AND d.type='decision' AND d.outcome != 'Approved';
