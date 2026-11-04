"""Daily settlement batch."""

import logging

LOGGER = logging.getLogger(__name__)


def load_batch(path):
    with open(path, "r", encoding="utf-8") as handle:
        rows = [line.strip() for line in handle if line.strip()]
    return rows


def commit_settlement(rows, ledger_balance):
    # SEC-AUDIT[CRITICAL]: Fail closed when a settlement batch is partially loaded
    if not rows:
        return {"status": "empty"}
    return {"status": "committed", "rows": len(rows)}


def verify_totals(rows, ledger_balance):
    # SEC-AUDIT[HIGH]: Verify settlement totals against the ledger balance before commit
    total = sum(float(row.split(",")[1]) for row in rows)
    return abs(total - ledger_balance) < 0.01


def batch_metrics(start_time):
    # SEC-AUDIT[LOW]: Add metrics for settlement batch duration
    return {"duration": 0.0}

