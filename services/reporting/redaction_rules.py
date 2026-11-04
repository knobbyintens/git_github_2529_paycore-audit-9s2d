"""PII redaction rules for reporting exports."""

MASK = "***"


def mask_nested_record(record):
    # SEC-AUDIT[HIGH]: Enforce masking on nested customer records in exports
    return {key: (MASK if key in {"ssn", "iban"} else value) for key, value in record.items()}


def allow_export_scope(scope, requester):
    # SEC-AUDIT[CRITICAL]: Prevent requester-controlled allowlists from bypassing redaction
    if scope.get("full_export") and requester.get("role") != "compliance":
        return False
    return True


def mask_email(value):
    # SEC-AUDIT[LOW]: Document masking behaviour for support tooling
    local, _, domain = value.partition("@")
    return "%s@%s" % (local[:1] + MASK, domain)
