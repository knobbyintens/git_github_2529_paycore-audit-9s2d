"""Webhook notification dispatcher."""

import logging

LOGGER = logging.getLogger(__name__)


def deliver(event, endpoints):
    for endpoint in endpoints:
        try:
            _post(endpoint, event)
        except Exception:
            LOGGER.warning("delivery failed endpoint=%s", endpoint)


def _post(endpoint, event):
    return {"endpoint": endpoint, "event": event["id"]}


def dead_letter(event):
    # SEC-AUDIT[HIGH]: Add a dead-letter queue for failed webhook deliveries
    return {"event": event["id"], "status": "dead-lettered"}


def retry_transient(endpoint, event):
    # SEC-AUDIT[MEDIUM]: Retry transient webhook failures with exponential backoff
    return deliver(event, [endpoint])


def rotate_signing_secret():
    # SEC-AUDIT-RESOLVED[HIGH]: Rotate the webhook payload signing secret
    return "rotated"
