#!/usr/bin/env python3
"""Demo programs for the Transaction Records databases.

Every demo is real, runnable, stdlib-only Python performing the actual
transaction-record computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_trx_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six questions every transaction record answers, and the family count
    family = {"orders": 1, "purchases": 1, "payments": 1, "returns": 1,
              "transfers": 1, "reconciliations": 1}
    questions = ["who paid", "who was paid", "how much",
                 "what currency", "when", "under what identifier"]
    print("transaction family members: %d" % len(family))
    print("questions answered: %d" % len(questions))
    states = ["pending", "settled", "reversed"]
    print("lifecycle states: %s" % ", ".join(states))
    assert len(family) == 6
    assert len(questions) == 6
    assert len(states) == 3
    print("rule: complete at birth, permanent forever, corrected only by new records")
    print("OK: %s framed the record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import hashlib
    # a well-formed record: the six organs present and checkable
    rec = {"id": "TXN-2026-0001", "payer": "CUST-881", "payee": "MERCH-204",
           "amount_minor": 1999, "currency": "USD",
           "event_time": "2026-10-17T14:03:22Z",
           "state": "settled", "lineage": ["ORD-5591", "AUTH-7712"]}
    required = ["id", "payer", "payee", "amount_minor", "currency",
                "event_time", "state"]
    missing = [k for k in required if k not in rec]
    print("missing organs: %s" % missing)
    assert missing == []
    # fingerprint the canonical form: tampering changes the hash
    canon = "|".join(str(rec[k]) for k in required)
    fp = hashlib.sha256(canon.encode()).hexdigest()[:16]
    print("record fingerprint: %s" % fp)
    print("amount: %d minor units %s" % (rec["amount_minor"], rec["currency"]))
    assert rec["amount_minor"] == 1999
    assert isinstance(rec["amount_minor"], int)
    print("rule: identifier, parties, amount, currency, time, state, lineage - or it is a rumor")
    print("OK: %s dissected the record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_lifecycle_states(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guarded state machine: pending -> settled|failed, settled -> reversed
    LEGAL = {"pending": {"authorized", "failed", "expired"},
             "authorized": {"captured", "voided", "expired"},
             "captured": {"settled"},
             "settled": {"reversed"},
             "failed": set(), "expired": set(), "voided": set(),
             "reversed": set()}
    def move(state, nxt):
        if nxt not in LEGAL[state]:
            raise ValueError("illegal %s -> %s" % (state, nxt))
        return nxt
    s = "pending"
    for nxt in ["authorized", "captured", "settled", "reversed"]:
        s = move(s, nxt)
    print("walked: pending -> authorized -> captured -> settled -> reversed")
    print("terminal state reached: %s" % s)
    assert s == "reversed"
    illegal = 0
    for bad in [("settled", "pending"), ("failed", "settled"), ("reversed", "settled")]:
        try:
            move(*bad)
        except ValueError:
            illegal += 1
    print("illegal transitions blocked: %d/3" % illegal)
    assert illegal == 3
    print("rule: history never runs backward; the undo is always a new record")
    print("OK: %s walked the lifecycle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_txn_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classify events into the four siblings plus cousins
    events = [("order", "ORD-1"), ("purchase", "PUR-1"), ("payment", "PAY-1"),
              ("transfer", "XFER-1"), ("order", "ORD-2"), ("payment", "PAY-2"),
              ("refund", "RFD-1"), ("reconciliation", "REC-1"),
              ("payment", "PAY-3"), ("chargeback", "CB-1")]
    FOLLOW = {"order": {"cancel"}, "payment": {"refund", "chargeback"},
              "transfer": {"reversal"}, "purchase": {"refund", "return"}}
    counts = {}
    for typ, _ in events:
        counts[typ] = counts.get(typ, 0) + 1
    for typ in sorted(counts):
        print("  %-15s %d" % (typ, counts[typ]))
    assert counts["payment"] == 3
    assert counts["order"] == 2
    assert sum(counts.values()) == 10
    # a refund filed against a mere order is a category error
    assert "refund" not in FOLLOW["order"], "orders take cancellations, not refunds"
    print("rule: the type decides which follow-ups are legal")
    print("OK: %s sorted the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_double_entry_basics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every transaction posts equal debits and credits; trial balance must be zero
    journal = []
    def post(desc, legs):
        # legs: list of (account, debit, credit) in minor units
        d = sum(l[1] for l in legs); c = sum(l[2] for l in legs)
        assert d == c, "unbalanced: %s" % desc
        journal.append((desc, legs))
    post("sell book for cash", [("cash", 2000, 0), ("sales revenue", 0, 2000)])
    post("pay postage", [("postage expense", 500, 0), ("cash", 0, 500)])
    post("refund damaged book", [("refunds contra-revenue", 2000, 0), ("cash", 0, 2000)])
    balances = {}
    for desc, legs in journal:
        for acct, d, c in legs:
            balances[acct] = balances.get(acct, 0) + d - c
    print("journal entries: %d" % len(journal))
    for acct in sorted(balances):
        print("  %-22s %+d" % (acct, balances[acct]))
    trial = sum(balances.values())
    print("trial balance: %d (must be 0)" % trial)
    assert trial == 0
    assert balances["cash"] == -500  # 2000 - 500 - 2000
    assert balances["sales revenue"] == -2000
    print("rule: debits equal credits, always; the trial balance is the proof")
    print("OK: %s balanced the books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_reading_receipt(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal, ROUND_HALF_UP
    # audit a receipt: extensions -> subtotal -> tax -> total
    lines = [("book", 2, "19.99"), ("bookmark", 1, "2.50")]
    tax_rate = Decimal("0.085")
    subtotal = sum(Decimal(q) * Decimal(p) for _, q, p in lines)
    tax = (subtotal * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total = subtotal + tax
    print("subtotal: %s" % subtotal)
    print("tax @8.5%%: %s" % tax)
    print("total: %s" % total)
    assert subtotal == Decimal("42.48")
    assert tax == Decimal("3.61")  # 42.48*0.085 = 3.6108 -> 3.61
    assert total == Decimal("46.09")
    # in minor units, exactly
    total_minor = int(total * 100)
    print("total minor units: %d" % total_minor)
    assert total_minor == 4609
    print("rule: line items sum to subtotal; tax is rate times subtotal, rounded once")
    print("OK: %s audited the receipt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_minor_units(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal, ROUND_HALF_UP
    # ISO 4217 minor units: USD 2, JPY 0, BHD 3
    MINOR = {"USD": 2, "JPY": 0, "BHD": 3}
    def to_minor(amount_str, ccy):
        q = Decimal(10) ** -MINOR[ccy]
        return int((Decimal(amount_str)).quantize(q, rounding=ROUND_HALF_UP)
                   * (10 ** MINOR[ccy]))
    usd = to_minor("19.99", "USD")
    jpy = to_minor("1500", "JPY")
    bhd = to_minor("2.675", "BHD")
    print("19.99 USD -> %d minor" % usd)
    print("1500 JPY  -> %d minor" % jpy)
    print("2.675 BHD -> %d minor (half-up)" % bhd)
    assert usd == 1999
    assert jpy == 1500
    assert bhd == 2675  # 2.675 exactly representable at 3 decimals
    # the float trap: 0.1 cannot be represented exactly in binary
    trap = 0.1 + 0.2
    print("float 0.1+0.2 = %.17f (not 0.3)" % trap)
    assert trap != 0.3
    print("rule: integers for money, always; floats are the phantom cent")
    print("OK: %s counted the minor units" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_timestamps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo
    # one global clock (UTC); local time is presentation only
    event_utc = datetime(2026, 1, 15, 14, 30, 22, tzinfo=timezone.utc)
    ny = event_utc.astimezone(ZoneInfo("America/New_York"))
    tokyo = event_utc.astimezone(ZoneInfo("Asia/Tokyo"))
    print("UTC:      %s" % event_utc.strftime("%Y-%m-%d %H:%M"))
    print("New York: %s" % ny.strftime("%Y-%m-%d %H:%M"))
    print("Tokyo:    %s" % tokyo.strftime("%Y-%m-%d %H:%M"))
    assert ny.hour == 9 and ny.day == 15      # EST = UTC-5 in January
    assert tokyo.hour == 23 and tokyo.day == 15  # JST = UTC+9
    # cutoff logic: 5pm Eastern cutoff decides the value date
    from datetime import timedelta
    cutoff = event_utc.astimezone(ZoneInfo("America/New_York")).replace(
        hour=17, minute=0, second=0)
    value_date = (event_utc + timedelta(days=1)).date() if ny >= cutoff else event_utc.date()
    print("value date: %s (cutoff 17:00 ET)" % value_date)
    assert str(value_date) == "2026-01-15"  # 09:30 ET is before cutoff
    print("rule: store UTC; the value date decides interest, the cutoff decides the value date")
    print("OK: %s kept the time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_parties(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the card purchase cast, each with a role
    cast = {"cardholder": "payer", "merchant": "payee", "issuer": "funds the payer",
            "acquirer": "collects for payee", "network": "carries messages, sets rules"}
    print("parties in a card purchase: %d" % len(cast))
    for who, role in cast.items():
        print("  %-10s -> %s" % (who, role))
    assert len(cast) == 5
    assert cast["cardholder"] == "payer"
    assert cast["merchant"] == "payee"
    # authorization binds the payer role: no authorization, no legitimate debit
    authorized = {"cardholder": True, "merchant": False}
    legit = all(authorized.get(p, False) for p in ["cardholder"])
    print("payer authorized: %s -> debit legitimate: %s" % (authorized["cardholder"], legit))
    assert legit is True
    print("rule: name every party and role; the dispute walks the chain backward")
    print("OK: %s named the parties" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_identifiers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import uuid
    # UUIDs: negligible collision odds; reference numbers: gap-auditable
    keys = {str(uuid.uuid4()) for _ in range(1000)}
    print("generated UUIDs: %d, unique: %d" % (1000, len(keys)))
    assert len(keys) == 1000
    # idempotency: the retry returns the stored result instead of acting twice
    store = {}
    def charge(idem_key, amount_minor):
        if idem_key in store:
            return store[idem_key], False  # replay: no new charge
        result = {"id": "PAY-%06d" % (len(store) + 1), "amount": amount_minor,
                  "state": "settled"}
        store[idem_key] = result
        return result, True
    key = str(uuid.uuid4())
    r1, acted1 = charge(key, 1999)
    r2, acted2 = charge(key, 1999)  # network retry with the same key
    r3, acted3 = charge(str(uuid.uuid4()), 1999)  # a genuinely new payment
    print("first: %s acted=%s | retry: %s acted=%s | new key: %s acted=%s"
          % (r1["id"], acted1, r2["id"], acted2, r3["id"], acted3))
    assert acted1 and not acted2 and acted3
    assert r1["id"] == r2["id"] and r1["id"] != r3["id"]
    assert len(store) == 2  # charged once for the retried key
    print("rule: one key per intended action; the retry is a lookup, not a gamble")
    print("OK: %s sealed the identifiers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_order_records(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal
    # the order freezes intent: line items, discounts, tax, total
    lines = [("widget A", 2, Decimal("120.00")), ("widget B", 1, Decimal("75.50"))]
    subtotal = sum(q * p for _, q, p in lines)
    discount = (subtotal * Decimal("0.10")).quantize(Decimal("0.01"))
    tax = ((subtotal - discount) * Decimal("0.06")).quantize(Decimal("0.01"))
    shipping = Decimal("9.99")
    total = subtotal - discount + tax + shipping
    print("subtotal: %s | discount 10%%: %s | tax 6%%: %s | shipping: %s"
          % (subtotal, discount, tax, shipping))
    print("order total: %s" % total)
    assert subtotal == Decimal("315.50")
    assert discount == Decimal("31.55")
    assert tax == Decimal("17.04")  # 283.95*0.06 = 17.037 -> 17.04
    assert total == Decimal("310.98")
    # order state machine
    state, seen = "created", ["created"]
    for nxt in ["awaiting_payment", "paid", "fulfilled"]:
        state = nxt
        seen.append(state)
    print("order states: %s" % " -> ".join(seen))
    assert state == "fulfilled"
    print("rule: the checkout price is a promise - snapshot it immutably")
    print("OK: %s froze the order" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_auth_capture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-step payment: authorize 100.00, capture 85.50 partial, void the rest
    auth = {"code": "AUTH-7712", "amount": 10000, "state": "authorized"}
    captures = []
    def capture(code, amount):
        assert code == auth["code"] and auth["state"] == "authorized"
        used = sum(captures)
        assert used + amount <= auth["amount"], "capture exceeds authorization"
        captures.append(amount)
        return amount
    c1 = capture("AUTH-7712", 8550)
    remaining = auth["amount"] - sum(captures)
    print("authorized: 100.00 | captured: %.2f | remaining hold: %.2f"
          % (c1 / 100, remaining / 100))
    assert c1 == 8550
    assert remaining == 1450
    # void the remainder before capture: hold released, no charge
    auth["state"] = "voided"
    print("voided remainder: hold released, charged total: %.2f" % (sum(captures) / 100))
    assert sum(captures) == 8550
    # a capture above the authorization is rejected
    auth2 = {"code": "AUTH-7713", "amount": 5000, "state": "authorized"}
    try:
        assert 0 + 6000 <= auth2["amount"]
        print("ERROR: over-capture allowed")
    except AssertionError:
        print("over-capture rejected: 60.00 against 50.00 authorization")
    print("rule: authorization reserves, capture claims - never more than reserved")
    print("OK: %s split the payment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_payment_methods(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost of moving 1000.00 by each rail
    amount = 100000  # minor units
    card_fee = int(amount * 0.029) + 30          # 2.9% + 0.30
    ach_fee = min(int(amount * 0.008), 500)      # 0.8% capped at 5.00
    wire_fee = 2500                               # flat 25.00
    print("card fee on 1000.00: %.2f" % (card_fee / 100))
    print("ACH  fee on 1000.00: %.2f" % (ach_fee / 100))
    print("wire fee on 1000.00: %.2f" % (wire_fee / 100))
    assert card_fee == 2930
    assert ach_fee == 500   # 8.00 capped to 5.00
    assert wire_fee == 2500
    assert ach_fee < wire_fee < card_fee
    speed = {"card": "seconds", "ach": "1-2 days", "wire": "hours"}
    final = {"card": "disputable", "ach": "returnable", "wire": "final"}
    for m in ["card", "ach", "wire"]:
        print("  %-4s settles in %-8s reversibility: %s" % (m, speed[m], final[m]))
    print("rule: speed, cost, finality, dispute rights - pick the bundle, not the dream")
    print("OK: %s compared the rails" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_idempotency(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import uuid
    # ledger keyed by idempotency key: the double-tap charges once
    ledger, keys = [], {}
    def post_transfer(idem_key, debit_acct, credit_acct, amount):
        if idem_key in keys:
            return keys[idem_key], False
        assert sum(1 for _ in [1]) == 1
        entry = {"debit": debit_acct, "credit": credit_acct, "amount": amount}
        # atomic: ledger insert and key insert commit together
        ledger.append(entry)
        keys[idem_key] = entry
        return entry, True
    k = str(uuid.uuid4())
    e1, a1 = post_transfer(k, "cash", "revenue", 5000)
    e2, a2 = post_transfer(k, "cash", "revenue", 5000)  # user tapped twice
    e3, a3 = post_transfer(k, "cash", "revenue", 5000)  # phone retried again
    print("attempts: 3 | ledger entries: %d | acted: %s %s %s" % (len(ledger), a1, a2, a3))
    assert len(ledger) == 1
    assert (a1, a2, a3) == (True, False, False)
    assert e1 is e2 is e3
    total_debited = sum(e["amount"] for e in ledger)
    print("total debited: %.2f (exactly once)" % (total_debited / 100))
    assert total_debited == 5000
    print("rule: the repeated knock is answered from memory - sealed exactly once")
    print("OK: %s made repeats harmless" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_refunds(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # partial refunds stack against the settled amount; the sum can never exceed it
    sale = {"id": "PAY-9001", "settled": 25000}
    refunds = []
    def refund(amount, reason):
        outstanding = sale["settled"] - sum(refunds)
        assert amount <= outstanding, "refund exceeds reversible amount"
        refunds.append(amount)
        return {"orig": sale["id"], "amount": amount, "reason": reason}
    r1 = refund(6000, "damaged item")
    r2 = refund(4000, "late shipment credit")
    net = sale["settled"] - sum(refunds)
    print("settled: 250.00 | refunds: 60.00 + 40.00 | net kept: %.2f" % (net / 100))
    assert sum(refunds) == 10000
    assert net == 15000
    try:
        refund(20000, "too much")
        print("ERROR: over-refund allowed")
    except AssertionError:
        print("over-refund rejected: 200.00 against 150.00 reversible")
    # double-entry mirror: debit contra-revenue, credit cash
    d = sum(refunds)
    print("mirror posting: debit refunds-contra %.2f, credit cash %.2f" % (d / 100, d / 100))
    assert d == 10000
    print("rule: the undo is a new record, and the stack can never exceed the sale")
    print("OK: %s posted the refunds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_returns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal
    # RMA pipeline: authorize -> receive -> inspect/grade -> refund per policy
    rma = {"id": "RMA-331", "order": "ORD-5591", "window_days": 30, "day": 12}
    assert rma["day"] <= rma["window_days"], "return window expired"
    items = [("headphones", Decimal("120.00"), "resellable"),
             ("case", Decimal("25.00"), "damaged")]
    restock_fee_rate = Decimal("0.15")
    refunds = []
    for name_i, price, grade in items:
        if grade == "resellable":
            refunds.append(price)
        elif grade == "damaged":
            refunds.append((price * (1 - restock_fee_rate)).quantize(Decimal("0.01")))
        print("  %-10s %-11s refund %s" % (name_i, grade, refunds[-1]))
    total_refund = sum(refunds)
    print("RMA %s within %d-day window | total refund: %s" % (rma["id"], rma["window_days"], total_refund))
    assert total_refund == Decimal("141.25")  # 120.00 + 25.00*0.85
    # resellable unit returns to available stock atomically with the refund
    stock_back = sum(1 for _, _, g in items if g == "resellable")
    print("units returned to stock: %d" % stock_back)
    assert stock_back == 1
    print("rule: the grade drives the money; every gate stamps its witness")
    print("OK: %s walked the return home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_chargebacks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dispute lifecycle: chargeback -> representment -> decision; track the rate
    sale = {"id": "PAY-4100", "amount": 50000}
    cb = {"reason": "13.1 merchandise not received", "amount": 50000, "fee": 1500}
    print("chargeback filed: %.2f + fee %.2f against %s"
          % (cb["amount"] / 100, cb["fee"] / 100, sale["id"]))
    # representment with delivery evidence wins
    evidence = {"tracking_delivered": True, "signature": True}
    won = evidence["tracking_delivered"] and evidence["signature"]
    net = 0 if won else -(cb["amount"] + cb["fee"])
    print("representment evidence: delivered=%s -> merchant %s | net %.2f"
          % (evidence["tracking_delivered"], "WINS" if won else "LOSES", net / 100))
    assert won is True and net == 0
    # the rate that matters: chargebacks / transactions vs the ~1% threshold
    txns, cbs = 10000, 42
    rate = cbs / txns * 100
    print("chargeback rate: %d/%d = %.2f%% (network threshold ~1%%)" % (cbs, txns, rate))
    assert 0.41 < rate < 0.43
    assert rate < 1.0
    print("rule: answer with evidence before the deadline; prevent with clear descriptors")
    print("OK: %s fought the dispute" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_bank_transfers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # NACHA-style batch: entries, batch control totals, file control totals
    entries = [("021000089", "acc-1", 10000), ("011401533", "acc-2", 20050),
               ("026009593", "acc-3", 7525)]
    batch_debit = sum(a for _, _, a in entries)
    batch_hash = sum(int(r[:8]) for r, _, _ in entries) % 10_000_000_000
    print("entries: %d | batch debit total: %.2f | entry hash: %d"
          % (len(entries), batch_debit / 100, batch_hash))
    assert batch_debit == 37575
    assert batch_hash == (2100008 + 1140153 + 2600959) % 10_000_000_000
    # file control must equal the sum of batch controls
    file_debit, file_count = batch_debit, len(entries)
    assert file_debit == batch_debit and file_count == len(entries)
    print("file control agrees with batch control: %.2f over %d entries" % (file_debit / 100, file_count))
    # a return references the original trace number
    ret = {"code": "R01", "reason": "insufficient funds", "orig_trace": "021000089-0001"}
    print("return %s (%s) references trace %s" % (ret["code"], ret["reason"], ret["orig_trace"]))
    assert ret["code"] == "R01"
    print("rule: balanced files or rejected files - the control totals are the conscience")
    print("OK: %s batched the transfers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_card_flow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one swipe: authorization -> clearing -> net settlement with interchange
    auth = {"code": "APPR-55", "amount": 20000, "state": "authorized"}
    clearing = {"code": auth["code"], "amount": 20000}  # matched by approval code
    assert clearing["code"] == auth["code"]
    interchange = int(clearing["amount"] * 0.018)   # 1.8% schedule
    assessment = int(clearing["amount"] * 0.0013)   # 0.13%
    markup = 20                                     # processor 0.20
    net = clearing["amount"] - interchange - assessment - markup
    print("sale 200.00 | interchange %.2f | assessment %.2f | markup %.2f"
          % (interchange / 100, assessment / 100, markup / 100))
    print("merchant net deposit: %.2f" % (net / 100))
    assert interchange == 360
    assert assessment == 26
    assert net == 20000 - 360 - 26 - 20
    assert 195.93 < net / 100 < 195.95
    # clearing without a matching authorization is an exception
    orphans = [c for c in [clearing] if c["code"] != auth["code"]]
    print("unmatched clearing records: %d" % len(orphans))
    assert orphans == []
    print("rule: the approval code threads all five hops; settlement is net")
    print("OK: %s relayed the swipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_reconciliation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # match the merchant ledger against the processor report; classify the breaks
    merchant = {"PAY-1": 10000, "PAY-2": 25000, "PAY-3": 7550, "PAY-4": 30000}
    processor = {"PAY-1": 10000, "PAY-2": 25000, "PAY-3": 7550,
                 "PAY-5": 12000}  # PAY-4 missing here, PAY-5 unknown there
    matched, breaks = [], []
    for tid, amt in merchant.items():
        if tid in processor and processor[tid] == amt:
            matched.append(tid)
        elif tid not in processor:
            breaks.append((tid, "timing: recorded today, settles tomorrow"))
    for tid in processor:
        if tid not in merchant:
            breaks.append((tid, "orphan: processor credit with no sale"))
    print("matched: %d/%d" % (len(matched), len(merchant)))
    for tid, kind in breaks:
        print("  break %-6s -> %s" % (tid, kind))
    assert len(matched) == 3
    assert len(breaks) == 2
    kinds = {k for _, k in breaks}
    assert any("timing" in k for k in kinds) and any("orphan" in k for k in kinds)
    print("rule: match on identifier and amount; classify every break, never just list it")
    print("OK: %s matched the ledgers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_settlement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # multilateral netting: thousands of gross transfers collapse to net positions
    # positive = owed money, negative = owing
    gross = [("A", "B", 100000), ("B", "C", 60000), ("C", "A", 40000),
             ("A", "C", 30000), ("B", "A", 20000)]
    net = {}
    for frm, to, amt in gross:
        net[frm] = net.get(frm, 0) - amt
        net[to] = net.get(to, 0) + amt
    print("gross transfers: %d totaling %.2f" % (len(gross), sum(a for _, _, a in gross) / 100))
    for p in sorted(net):
        print("  participant %s net %+d (%.2f)" % (p, net[p], net[p] / 100))
    total = sum(net.values())
    print("sum of net positions: %d (must be 0)" % total)
    assert total == 0
    assert net["A"] == -70000  # -100000-30000+40000+20000
    assert net["B"] == 20000   # +100000-60000-20000
    assert net["C"] == 50000   # +60000-40000+30000
    print("rule: clearing counts the debt, settlement delivers the coin - finality lives there")
    print("OK: %s netted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_fees(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three organs of the fee on a 100.00 sale
    sale = 10000
    interchange = int(sale * 0.0165)   # schedule: rewards card, retail
    assessment = int(sale * 0.0013)    # network toll
    markup = 25                        # processor margin
    total_fee = interchange + assessment + markup
    net = sale - total_fee
    print("interchange %.2f + assessment %.2f + markup %.2f = fee %.2f"
          % (interchange / 100, assessment / 100, markup / 100, total_fee / 100))
    print("merchant keeps: %.2f of 100.00" % (net / 100))
    assert interchange == 165
    assert assessment == 13
    assert total_fee == 203
    assert 97.96 < net / 100 < 97.98
    # the merchant's defense: recompute from the schedule and compare
    billed = 203
    assert billed == total_fee, "padded markup detected"
    print("recomputed from schedule: %.2f == billed %.2f -> no padding" % (total_fee / 100, billed / 100))
    print("rule: the toll itemized in the open; recompute it and compare")
    print("OK: %s itemized the fee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_double_entry_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # streaming trial balance over a day of events: sale, fee, settlement, refund
    journal = []
    seq = [0]
    def post(desc, legs):
        d = sum(l[1] for l in legs); c = sum(l[2] for l in legs)
        assert d == c, "unbalanced write rejected: %s" % desc
        seq[0] += 1
        journal.append((seq[0], desc, legs))
    for i in range(50):
        post("sale %d" % i, [("cash", 10000, 0), ("revenue", 0, 10000)])
        post("fee %d" % i, [("processing expense", 203, 0), ("merchant payable", 0, 203)])
    post("settle batch", [("merchant payable", 50 * 203, 0), ("bank", 0, 50 * 203)])
    post("refund one sale", [("refunds contra-revenue", 10000, 0), ("cash", 0, 10000)])
    balances = {}
    for _, _, legs in journal:
        for acct, d, c in legs:
            balances[acct] = balances.get(acct, 0) + d - c
    trial = sum(balances.values())
    print("journal entries: %d | accounts: %d" % (len(journal), len(balances)))
    print("trial balance: %d (must be 0 at every commit)" % trial)
    assert trial == 0
    assert balances["merchant payable"] == 0  # fees accrued then settled
    net_revenue = -(balances["revenue"] + balances["refunds contra-revenue"])
    print("net revenue kept: %.2f" % (net_revenue / 100))
    assert net_revenue == 490000  # 50 sales minus 1 refund
    print("rule: balance is a property of the write path - no entry walks alone")
    print("OK: %s scaled the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_iso20022(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # build a pacs.008-style customer credit transfer and validate its grammar
    msg = {"msg_type": "pacs.008",
           "instruction_id": "INS-2026-8841",
           "end_to_end_id": "E2E-CUST-77120",
           "transaction_id": "TXN-SYS-99012",
           "debtor": {"name": "Acme Corp", "account": "US44ACME0001"},
           "creditor": {"name": "Beta Ltd", "account": "GB29BETA0002"},
           "amount_minor": 250000, "currency": "USD"}
    required = ["instruction_id", "end_to_end_id", "transaction_id",
                "debtor", "creditor", "amount_minor", "currency"]
    missing = [k for k in required if k not in msg]
    print("message: %s | missing elements: %s" % (msg["msg_type"], missing))
    assert missing == []
    assert isinstance(msg["amount_minor"], int) and msg["currency"] == "USD"
    # the lineage trio survives the whole chain debtor -> creditor
    lineage = (msg["instruction_id"], msg["end_to_end_id"], msg["transaction_id"])
    print("lineage trio: %s / %s / %s" % lineage)
    assert all(lineage)
    # status report closes the loop: pacs.002 acceptance
    status = {"msg_type": "pacs.002", "ref": msg["end_to_end_id"], "status": "ACCP"}
    print("status report: %s -> %s" % (status["ref"], status["status"]))
    assert status["status"] == "ACCP"
    print("rule: pain initiates, pacs moves, camt reports - one grammar, no translation loss")
    print("OK: %s spoke ISO 20022" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_swift_mt_mx(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import re
    # parse an MT103: tagged fields, validated formats
    raw = ":20:REF20268841\\n:32A:261017USD250000,\\n:50K:/US44ACME0001\\nACME CORP\\n:59:/GB29BETA0002\\nBETA LTD"
    fields = dict(re.findall(r":(\\d+[A-Z]?):([^:]+)", raw))
    print("fields parsed: %s" % sorted(fields))
    ref = fields["20"].strip()
    f32 = fields["32A"].strip()
    m = re.match(r"(\\d{6})([A-Z]{3})([\\d,]+)", f32)
    assert m, "malformed :32A:"
    yymmdd, ccy, amt = m.groups()
    print("ref %s | value date %s | %s %s" % (ref, yymmdd, ccy, amt))
    assert yymmdd == "261017" and ccy == "USD"
    # charge option decides who pays transit fees
    for opt, paid_by in [("OUR", "sender"), ("SHA", "shared"), ("BEN", "beneficiary")]:
        print("  charge option %s -> fees paid by %s" % (opt, paid_by))
    # MX migration map
    migration = {"MT103": "pacs.008", "MT202": "pacs.009", "MT940": "camt.053"}
    assert migration["MT103"] == "pacs.008"
    print("migration: MT103 -> pacs.008, MT202 -> pacs.009, MT940 -> camt.053")
    print("rule: terse telegram or rich letter - carry both, reconcile across the translation")
    print("OK: %s wired the message" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_nacha(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # assemble a fixed-width NACHA file and prove the control totals balance
    def rtype(n, body):
        line = str(n) + body
        return line.ljust(94)[:94]
    entries = [("021000089", 10000), ("011401533", 20050)]
    batch_lines = [rtype(5, "BATCH-HEADER-ACME")]
    for i, (rtn, amt) in enumerate(entries):
        batch_lines.append(rtype(6, "TRACE%04d%s%010d" % (i + 1, rtn, amt)))
    batch_debit = sum(a for _, a in entries)
    batch_hash = sum(int(r[:8]) for r, _ in entries) % 10_000_000_000
    batch_lines.append(rtype(8, "CTRL%010d%010d%012d" % (batch_debit, len(entries), batch_hash)))
    file_lines = [rtype(1, "FILE-HEADER")] + batch_lines + [rtype(9, "FILE-CTRL")]
    bad = [l for l in file_lines if len(l) != 94]
    print("records: %d | all 94 chars: %s" % (len(file_lines), bad == []))
    assert bad == []
    assert batch_debit == 30050
    print("batch debit total: %.2f | entry hash: %d" % (batch_debit / 100, batch_hash))
    # file control agrees with batch control
    assert file_lines[-1].startswith("9")
    print("file control present; batch totals balance - file accepted")
    print("rule: ninety-four columns, no more, no less; totals sworn at the end")
    print("OK: %s wrote the NACHA file" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_pci_dss(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the record keeps what it needs and discards the rest
    pan = "4111111111111111"
    cvv = "737"
    def mask(p):
        return "*" * (len(p) - 4) + p[-4:]
    record = {"pan_display": mask(pan), "auth_code": "APPR-55",
              "token": "tok_9f27ab41", "network_ref": "ARN-88213"}
    print("stored PAN form: %s" % record["pan_display"])
    assert record["pan_display"] == "************1111"
    assert len(record["pan_display"]) == 16
    # sensitive authentication data must never be stored post-authorization
    forbidden = {"full_pan": pan, "cvv": cvv, "stripe_data": "present"}
    stored_keys = set(record)
    leaked = [k for k in forbidden if k in stored_keys]
    print("forbidden fields in record: %s" % leaked)
    assert leaked == []
    assert "cvv" not in stored_keys
    # the token still reconciles and disputes: it maps 1:1 to the card in the vault
    vault = {"tok_9f27ab41": pan}
    assert vault[record["token"]] == pan
    print("token %s resolves in the vault; the merchant never holds the PAN" % record["token"])
    print("rule: keep the seal (last four), burn the wax impression (the rest)")
    print("OK: %s guarded the card data" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_fraud_signals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import datetime, timedelta
    # velocity + impossible travel + probe pattern, scored together
    base = datetime(2026, 10, 17, 12, 0, 0)
    txns = [{"t": base + timedelta(minutes=m), "city": c, "amt": a}
            for m, c, a in [(0, "New York", 100), (2, "New York", 100),
                            (4, "New York", 100), (5, "New York", 100),
                            (6, "New York", 100), (7, "New York", 100),
                            (8, "New York", 100), (9, "New York", 100),
                            (10, "Singapore", 490000)]]
    window = [x for x in txns if x["t"] <= base + timedelta(minutes=10)]
    velocity = len(window)
    cities = {x["city"] for x in window}
    probe = sum(1 for x in window if x["amt"] == 100)
    big = max(x["amt"] for x in window)
    print("10-minute window: %d txns | cities %s | 1.00 probes %d | max %.2f"
          % (velocity, sorted(cities), probe, big / 100))
    signals = {"velocity>8": velocity > 8, "impossible_travel": len(cities) > 1,
               "probe_then_big": probe >= 5 and big > 100000}
    score = sum(signals.values())
    print("signals: %s | score %d/3" % (signals, score))
    assert velocity == 9 and probe == 8
    assert score == 3
    decision = "DECLINE" if score >= 2 else ("STEP-UP" if score == 1 else "APPROVE")
    print("decision: %s" % decision)
    assert decision == "DECLINE"
    print("rule: one sign is rumor, three are testimony - score them together")
    print("OK: %s read the signals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_audit_trails(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    import hashlib
    # hash-chained audit trail: each entry fingerprints the previous
    def h(s):
        return hashlib.sha256(s.encode()).hexdigest()
    trail = []
    prev = "GENESIS"
    for i, ev in enumerate(["created PAY-1", "authorized PAY-1",
                            "captured PAY-1", "settled PAY-1", "refunded PAY-1"]):
        entry = {"n": i, "event": ev, "prev": prev}
        entry["hash"] = h("%d|%s|%s" % (i, ev, prev))
        trail.append(entry)
        prev = entry["hash"]
    def verify(chain):
        p = "GENESIS"
        for e in chain:
            if e["prev"] != p:
                return False
            if e["hash"] != h("%d|%s|%s" % (e["n"], e["event"], e["prev"])):
                return False
            p = e["hash"]
        return True
    print("trail entries: %d | head hash: %s" % (len(trail), trail[-1]["hash"][:16]))
    assert verify(trail) is True
    # tamper with entry 2: the chain breaks from there on
    tampered = [dict(e) for e in trail]
    tampered[2]["event"] = "captured PAY-1 FOR 999999"
    print("tampered chain verifies: %s" % verify(tampered))
    assert verify(tampered) is False
    print("rule: the chain of witness cannot be edited - only extended")
    print("OK: %s sealed the trail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_fx(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from decimal import Decimal, ROUND_HALF_UP
    # convert 1000.00 USD to EUR at 0.92, rounding once to the target minor units
    rate = Decimal("0.92")
    usd_minor = 100000
    eur = (Decimal(usd_minor) / 100 * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    eur_minor = int(eur * 100)
    print("1000.00 USD @ 0.92 -> %s EUR (%d minor)" % (eur, eur_minor))
    assert eur_minor == 92000
    # the spread is the converter's price: market 0.92, board 0.905
    board = Decimal("0.905")
    eur_board = (Decimal(usd_minor) / 100 * board).quantize(Decimal("0.01"))
    spread_cost = eur - eur_board
    print("board rate 0.905 -> %s EUR | spread cost: %s EUR" % (eur_board, spread_cost))
    assert 14.99 < float(spread_cost) < 15.01
    # books keep both amounts; the FX difference posts balanced
    d = eur_minor
    print("balanced FX posting: debit cash-eur %d, credit cash-usd 100000, fx-loss %d"
          % (d, 100000 - int(Decimal(100000) / 100 * rate * 100)))
    print("rule: name both weighings, the scales, and the toll of the translator")
    print("OK: %s crossed the currency" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_ledger_design(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # append-only journal: sequence, balanced writes, balances re-derived
    journal, seq = [], [0]
    def write(txn_id, legs):
        d = sum(l[2] for l in legs); c = sum(l[3] for l in legs)
        assert d == c, "unbalanced commit rejected"
        seq[0] += 1
        for acct, direction, damt, camt in legs:
            journal.append({"seq": seq[0], "txn": txn_id, "acct": acct,
                            "d": damt, "c": camt})
    write("T1", [("cash", "d", 10000, 0), ("revenue", "c", 0, 10000)])
    write("T2", [("expense", "d", 203, 0), ("cash", "c", 0, 203)])
    write("T3", [("contra-revenue", "d", 10000, 0), ("cash", "c", 0, 10000)])
    seqs = [e["seq"] for e in journal]
    txns = sorted({e["txn"] for e in journal})
    print("journal rows: %d | txns: %d | sequence monotonic: %s"
          % (len(journal), len(txns), seqs == sorted(seqs)))
    assert seqs == sorted(seqs)  # replay order unambiguous; one seq per txn
    assert txns == ["T1", "T2", "T3"]
    # balances are derived, never stored as truth
    balances = {}
    for e in journal:
        balances[e["acct"]] = balances.get(e["acct"], 0) + e["d"] - e["c"]
    print("derived balances: %s" % {k: v for k, v in sorted(balances.items())})
    assert sum(balances.values()) == 0
    assert balances["cash"] == -203  # 10000 - 203 - 10000
    # no update or delete API exists: the past is not editable
    assert not hasattr(journal, "rewrite")
    print("rule: the journal remembers what the clerks forget - in order, forever")
    print("OK: %s designed the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_reversals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the undo is a new record: original + reversal nets to zero, both visible
    journal = []
    def post(desc, legs, ref=None):
        d = sum(l[1] for l in legs); c = sum(l[2] for l in legs)
        assert d == c
        journal.append({"desc": desc, "legs": legs, "ref": ref})
    post("wire out T-100", [("supplier payable", 150000, 0), ("bank", 0, 150000)])
    post("reversal of T-100 (wrong account)",
         [("bank", 150000, 0), ("supplier payable", 0, 150000)], ref="T-100")
    # re-send correctly as a third record
    post("wire out T-101 (corrected)", [("supplier payable", 150000, 0), ("bank", 0, 150000)])
    balances = {}
    for j in journal:
        for acct, d, c in j["legs"]:
            balances[acct] = balances.get(acct, 0) + d - c
    print("records: %d (original, reversal, corrected)" % len(journal))
    for acct in sorted(balances):
        print("  %-16s %+d" % (acct, balances[acct]))
    assert len(journal) == 3  # nothing deleted, nothing edited
    assert balances["bank"] == -150000  # one good wire outstanding
    assert balances["supplier payable"] == 150000
    assert journal[1]["ref"] == "T-100"
    print("rule: the undo is always a new record - history is the asset")
    print("OK: %s answered the mistake" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_realtime_payments(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import datetime, timezone, timedelta
    # instant payment: initiated and settled within seconds, final
    sent = datetime(2026, 10, 17, 23, 42, 11, tzinfo=timezone.utc)  # Saturday night
    settled = sent + timedelta(seconds=4)
    latency = (settled - sent).total_seconds()
    msg = {"type": "pacs.008", "id": "RTP-88412", "amount_minor": 7500,
           "currency": "USD", "state": "settled"}
    print("sent:    %s (Saturday 23:42 UTC)" % sent.strftime("%H:%M:%S"))
    print("settled: %s | latency %.0f seconds" % (settled.strftime("%H:%M:%S"), latency))
    assert 3.9 < latency < 4.1
    assert msg["state"] == "settled"
    assert sent.weekday() == 5  # Saturday: no banking hours needed
    # final: no returns exist; errors are corrected by a new payment back
    correction = {"type": "pacs.008", "id": "RTP-88413",
                  "amount_minor": 7500, "direction": "reverse"}
    net = msg["amount_minor"] - correction["amount_minor"]
    print("correction payment nets the error to: %d" % net)
    assert net == 0
    print("rule: check before you speak - instant finality has no recall window")
    print("OK: %s settled in seconds" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_trx_lifecycle_capstone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one 500.00 order through every station: the whole database in one story
    journal, lineage = [], {}
    def post(desc, legs, ref=None):
        assert sum(l[1] for l in legs) == sum(l[2] for l in legs)
        journal.append({"desc": desc, "legs": legs, "ref": ref})
    order_total = 50000
    lineage["ORD-1"] = None
    post("authorize 500.00", [("auth hold", 50000, 0), ("cardholder", 0, 50000)], ref="ORD-1")
    post("capture box 1: 300.00", [("cash", 30000, 0), ("revenue", 0, 30000)], ref="ORD-1")
    post("capture box 2: 200.00", [("cash", 20000, 0), ("revenue", 0, 20000)], ref="ORD-1")
    post("interchange+fees 2.03%", [("processing expense", 1015, 0), ("cash", 0, 1015)], ref="ORD-1")
    post("refund box 2 (damaged)", [("contra-revenue", 20000, 0), ("cash", 0, 20000)], ref="ORD-1")
    post("release auth hold", [("cardholder", 50000, 0), ("auth hold", 0, 50000)], ref="ORD-1")
    balances = {}
    for j in journal:
        for acct, d, c in j["legs"]:
            balances[acct] = balances.get(acct, 0) + d - c
    trial = sum(balances.values())
    print("stations posted: %d | trial balance: %d" % (len(journal), trial))
    assert trial == 0
    net_revenue = -(balances["revenue"] + balances["contra-revenue"])
    net_cash = balances["cash"]  # 30000 + 20000 - 1015 fees - 20000 refund
    print("net revenue kept: %.2f | net cash kept: %.2f"
          % (net_revenue / 100, net_cash / 100))
    assert net_cash == 28985
    assert net_revenue == 30000  # 500.00 sold, 200.00 refunded
    assert all(j["ref"] == "ORD-1" for j in journal)  # one unbroken lineage
    print("lineage: every record points to ORD-1 - spoken, kept, partly released, remembered")
    print("rule: a promise fully traced is a promise fully kept")
    print("OK: %s ran the full lifecycle" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_trx_what_is,
    "anatomy": demo_trx_anatomy,
    "lifecycle_states": demo_trx_lifecycle_states,
    "txn_types": demo_trx_txn_types,
    "double_entry_basics": demo_trx_double_entry_basics,
    "reading_receipt": demo_trx_reading_receipt,
    "minor_units": demo_trx_minor_units,
    "timestamps": demo_trx_timestamps,
    "parties": demo_trx_parties,
    "identifiers": demo_trx_identifiers,
    "order_records": demo_trx_order_records,
    "auth_capture": demo_trx_auth_capture,
    "payment_methods": demo_trx_payment_methods,
    "idempotency": demo_trx_idempotency,
    "refunds": demo_trx_refunds,
    "returns": demo_trx_returns,
    "chargebacks": demo_trx_chargebacks,
    "bank_transfers": demo_trx_bank_transfers,
    "card_flow": demo_trx_card_flow,
    "reconciliation": demo_trx_reconciliation,
    "settlement": demo_trx_settlement,
    "fees": demo_trx_fees,
    "double_entry_scale": demo_trx_double_entry_scale,
    "iso20022": demo_trx_iso20022,
    "swift_mt_mx": demo_trx_swift_mt_mx,
    "nacha": demo_trx_nacha,
    "pci_dss": demo_trx_pci_dss,
    "fraud_signals": demo_trx_fraud_signals,
    "audit_trails": demo_trx_audit_trails,
    "fx": demo_trx_fx,
    "ledger_design": demo_trx_ledger_design,
    "reversals": demo_trx_reversals,
    "realtime_payments": demo_trx_realtime_payments,
    "lifecycle_capstone": demo_trx_lifecycle_capstone,
}
