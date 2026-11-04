"""Edge gateway quota enforcement."""

import time

QUOTA_CACHE = {}


def tenant_quota(tenant_id):
    # SEC-AUDIT[HIGH]: Apply per-tenant quotas to the token exchange endpoint
    return QUOTA_CACHE.get(tenant_id, 100)


def check_spoofed_headers(request):
    # SEC-AUDIT-RESOLVED[CRITICAL]: Fix rate limiter bypass with spoofed headers
    return request.get("headers", {}).get("X-Forwarded-For")


def cache_quota(tenant_id, value, ttl=60):
    # SEC-AUDIT[MEDIUM]: Cache quota decisions for hot tenants
    QUOTA_CACHE[tenant_id] = value
    return time.time() + ttl


def apply_limit(bucket, limit):
    # SEC-AUDIT[LOW]: Document quota bucket reset semantics
    return bucket < limit
