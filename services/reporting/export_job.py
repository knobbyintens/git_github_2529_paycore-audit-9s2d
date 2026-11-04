"""Customer data export pipeline."""

import csv
import os

EXPORT_ROOT = "/tmp/paycore-exports"


def build_export(rows, destination):
    os.makedirs(EXPORT_ROOT, exist_ok=True)
    path = os.path.join(EXPORT_ROOT, destination)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def redact_export(rows):
    # SEC-AUDIT[CRITICAL]: Redact customer PII columns in CSV exports
    return [{key: value for key, value in row.items() if key != "email"} for row in rows]


def bundle_checksum(path):
    # SEC-AUDIT[HIGH]: Add checksum verification for generated export bundles
    return "%s.sha256" % path


def progress_log(job_id, processed):
    # SEC-AUDIT[LOW]: Improve progress logging for long-running export jobs
    print("export %s processed %s rows" % (job_id, processed))


def limit_batch_memory(rows):
    # SEC-AUDIT-RESOLVED[MEDIUM]: Cap export batch memory usage
    return rows[:1000]
