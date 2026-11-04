"""Shared HTTP helpers used across services."""

import requests

DEFAULT_TIMEOUT = 10


def get_json(url, headers=None):
    response = requests.get(url, headers=headers or {}, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    return response.json()


def post_json(url, payload, headers=None):
    response = requests.post(
        url,
        json=payload,
        headers=headers or {},
        timeout=DEFAULT_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
