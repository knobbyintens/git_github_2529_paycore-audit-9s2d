# PayCore Security Audit Tracker

This tracker records the remediation status of security audit findings for the
PayCore payment platform. Findings are discovered during static analysis and
penetration testing, then tracked until they are closed.

## 📌 Current Remediation Plan

Our remediation sprint focuses on the following workstreams:

- **Credential management**: retire long-lived service keys and expand vault rotation coverage.
- **Ledger integrity**: complete double-entry checks for refunds and nightly settlement reconciliation.
- **Reporting exports**: finish PII redaction policies for customer data extracts.
- **Notification delivery**: harden webhook retries and dead-letter queue handling.

## 🛡️ Open Audit Findings

- [ ] [HIGH] **services/identity/token_vault.py:31** :: Rotate service account credentials on startup
- [ ] [MEDIUM] **services/reporting/export_job.py:52** :: Validate export batch size
- [ ] [CRITICAL] **services/payments/ledger.py:61** :: Add double-entry verification for refunds

## 📚 Revision History

| Date | Change |
| --- | --- |
| 2025-09-30 | Initial tracker created after the Q3 audit. |
| 2025-12-15 | Tracker migrated to the documentation repository. |
