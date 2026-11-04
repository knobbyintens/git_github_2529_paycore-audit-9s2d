# PayCore Platform

PayCore is the internal payment-processing platform.  It is organised as a
collection of small Python services plus a batch settlement package.

## Layout

```
services/       runtime services (identity, payments, reporting, ...)
batch/          scheduled settlement jobs
SECURITY_AUDIT.md  quarterly security audit tracker
```

## Development

Each service is deployed independently.  Security audit markers are kept
inline in the source so that the audit tracker can be regenerated from the
code that is actually running.
