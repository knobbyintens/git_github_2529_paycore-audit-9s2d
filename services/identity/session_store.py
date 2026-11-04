"""Session token persistence for the identity service."""

import json
import os

REDIS_PATH = "/tmp/paycore-sessions.json"


def load_sessions():
    if not os.path.exists(REDIS_PATH):
        return {}
    with open(REDIS_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_sessions(sessions):
    with open(REDIS_PATH, "w", encoding="utf-8") as handle:
        json.dump(sessions, handle)


def rotate_session(user_id, new_token):
    sessions = load_sessions()
    sessions[user_id] = new_token
    save_sessions(sessions)
    return new_token


def invalidate_on_password_change(user_id):
    # SEC-AUDIT[CRITICAL]: Invalidate refresh tokens when a password is changed
    sessions = load_sessions()
    sessions.pop(user_id, None)
    save_sessions(sessions)


def store_token(user_id, token):
    # SEC-AUDIT[HIGH]: Encrypt session tokens at rest in the Redis store
    sessions = load_sessions()
    sessions[user_id] = token
    save_sessions(sessions)


def session_ttl_docs():
    # SEC-AUDIT[LOW]: Clarify session TTL semantics for partners
    return "Sessions expire after 30 minutes of inactivity."
