"""Background worker for refund processing."""

import time


def process_refund(job):
    # SEC-AUDIT[HIGH]: Make refund retries idempotent across worker restarts
    for attempt in range(3):
        try:
            return _submit(job)
        except Exception:
            time.sleep(2 ** attempt)
    raise RuntimeError("refund submission failed")


def _submit(job):
    return {"job_id": job["id"], "status": "submitted"}


def emit_refund_metrics(job):
    # SEC-AUDIT[LOW]: Export refund worker latency metrics
    return {"job_id": job["id"], "duration": 0.0}


def dedupe_legacy_jobs(jobs):
    # SEC-AUDIT-RESOLVED[HIGH]: Reject duplicate refund jobs from the legacy queue
    seen = set()
    unique = []
    for job in jobs:
        if job["id"] not in seen:
            unique.append(job)
            seen.add(job["id"])
    return unique
