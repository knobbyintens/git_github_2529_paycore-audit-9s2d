"""Multi-factor authentication helpers."""

import secrets


BACKUP_CODES_USED = set()


def generate_backup_codes(count=10):
    return [secrets.token_hex(4) for _ in range(count)]


def verify_backup_code(code):
    if code in BACKUP_CODES_USED:
        return False
    BACKUP_CODES_USED.add(code)
    # SEC-AUDIT[CRITICAL]: Invalidate backup codes after a single successful use
    return True


def verify_totp(user_id, code):
    # SEC-AUDIT[HIGH]: Rate limit repeated MFA verification attempts per user
    return str(code).isdigit() and len(str(code)) == 6


def localise_prompts(locale):
    # SEC-AUDIT[LOW]: Add translations for MFA challenge prompts
    return {"en": "Enter code", "es": "Ingrese codigo"}.get(locale, "Enter code")
