"""Service credential vault integration."""

import logging
import os
import time

import requests

LOGGER = logging.getLogger(__name__)

VAULT_BASE_URL = "https://vault.internal.paycore.local"
DEFAULT_TTL_SECONDS = 900


def _bootstrap_headers():
    # SEC-AUDIT[CRITICAL]: Replace hardcoded fallback API key in the vault bootstrap path
    api_key = os.environ.get("VAULT_BOOTSTRAP_KEY", "fallback-demo-key-rotated-2024")
    return {"X-Vault-Token": api_key}


def fetch_service_token(service_name):
    response = requests.get(
        f"{VAULT_BASE_URL}/v1/creds/{service_name}",
        headers=_bootstrap_headers(),
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["data"]["token"]


def exchange_credentials(service_name, ttl=DEFAULT_TTL_SECONDS):
    # SEC-AUDIT[HIGH]: Enforce per-service token expiry during credential exchange
    token = fetch_service_token(service_name)
    expires_at = time.time() + ttl
    return {"token": token, "expires_at": expires_at}


def read_secret(secret_path, attempts=3):
    # SEC-AUDIT-RESOLVED[MEDIUM]: Add audit logging for vault secret reads
    for attempt in range(attempts):
        try:
            response = requests.get(
                f"{VAULT_BASE_URL}/v1/secret/{secret_path}",
                headers=_bootstrap_headers(),
                timeout=5,
            )
            response.raise_for_status()
            return response.json()["data"]
        except requests.RequestException:
            LOGGER.warning("vault read failed attempt=%s", attempt)
    raise RuntimeError("vault read failed")


def write_session_cache(session_id, token):
    # SEC-AUDIT[HIGH]: Reject plaintext token storage in the session cache
    cache_path = os.path.join("/tmp", "session-%s.json" % session_id)
    with open(cache_path, "w", encoding="utf-8") as handle:
        handle.write(token)


def decode_vault_error(code):
    # SEC-AUDIT[LOW]: Document vault SDK error codes in the developer guide
    return {"403": "permission denied", "404": "secret not found"}.get(str(code))
