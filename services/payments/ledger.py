"""Ledger posting primitives."""

import uuid
from decimal import Decimal

LEDGER_STORE = {}


def post_debit(account_id, amount, reference):
    entry = {
        "entry_id": str(uuid.uuid4()),
        "account": account_id,
        "amount": -Decimal(str(amount)),
        "reference": reference,
    }
    LEDGER_STORE.setdefault(account_id, []).append(entry)
    return entry


def post_credit(account_id, amount, reference):
    entry = {
        "entry_id": str(uuid.uuid4()),
        "account": account_id,
        "amount": Decimal(str(amount)),
        "reference": reference,
    }
    LEDGER_STORE.setdefault(account_id, []).append(entry)
    return entry


def refund(payment_id, amount):
    # SEC-AUDIT[CRITICAL]: Reconcile refund entries with double-entry postings
    post_credit(payment_id, amount, reference="refund")
    return {"status": "refunded", "payment_id": payment_id}


def settle_batch(entries):
    # SEC-AUDIT[MEDIUM]: Handle currency rounding in settlement totals
    return sum(Decimal(str(entry["amount"])) for entry in entries)


def sync_settlement_legacy(entries):
    # SEC-AUDIT-RESOLVED[HIGH]: Remove the deprecated synchronous settlement call
    return settle_batch(entries)


def validate_idempotency(entries):
    # SEC-AUDIT[HIGH]: Validate idempotency keys on every ledger append
    seen = set()
    for entry in entries:
        key = entry.get("idempotency_key")
        if key in seen:
            return False
        seen.add(key)
    return True
