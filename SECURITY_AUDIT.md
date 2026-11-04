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

- [ ] [CRITICAL] **batch/daily_settlement.py:15** :: Fail closed when a settlement batch is partially loaded
- [ ] [CRITICAL] **services/identity/mfa_service.py:17** :: Invalidate backup codes after a single successful use
- [ ] [CRITICAL] **services/identity/session_store.py:29** :: Invalidate refresh tokens when a password is changed
- [ ] [CRITICAL] **services/identity/token_vault.py:16** :: Replace hardcoded fallback API key in the vault bootstrap path
- [ ] [CRITICAL] **services/payments/ledger.py:32** :: Reconcile refund entries with double-entry postings
- [ ] [CRITICAL] **services/reporting/export_job.py:20** :: Redact customer PII columns in CSV exports
- [ ] [CRITICAL] **services/reporting/redaction_rules.py:12** :: Prevent requester-controlled allowlists from bypassing redaction
- [ ] [HIGH] **batch/daily_settlement.py:22** :: Verify settlement totals against the ledger balance before commit
- [ ] [HIGH] **services/gateway/rate_limiter.py:9** :: Apply per-tenant quotas to the token exchange endpoint
- [ ] [HIGH] **services/identity/mfa_service.py:22** :: Rate limit repeated MFA verification attempts per user
- [ ] [HIGH] **services/identity/session_store.py:36** :: Encrypt session tokens at rest in the Redis store
- [ ] [HIGH] **services/identity/token_vault.py:32** :: Enforce per-service token expiry during credential exchange
- [ ] [HIGH] **services/identity/token_vault.py:55** :: Reject plaintext token storage in the session cache
- [ ] [HIGH] **services/notifications/dispatcher.py:21** :: Add a dead-letter queue for failed webhook deliveries
- [ ] [HIGH] **services/payments/ledger.py:48** :: Validate idempotency keys on every ledger append
- [ ] [HIGH] **services/payments/refund_worker.py:7** :: Make refund retries idempotent across worker restarts
- [ ] [HIGH] **services/reporting/export_job.py:25** :: Add checksum verification for generated export bundles
- [ ] [HIGH] **services/reporting/redaction_rules.py:7** :: Enforce masking on nested customer records in exports

## 📚 Revision History

| Date | Change |
| --- | --- |
| 2025-09-30 | Initial tracker created after the Q3 audit. |
| 2025-12-15 | Tracker migrated to the documentation repository. |
