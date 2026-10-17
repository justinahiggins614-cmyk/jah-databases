#!/usr/bin/env python3
"""JAH Database Lock-In Governance enforcement.

Reads data/governance.json (machine-readable policy, never rendered).
No regulator AI exists yet — this module is what it will obey when built.

Generators/builders MUST call assert_mutation_allowed() before any
delete or overwrite of an existing record. Additive writes (new records,
new fields on new records, reorganization) are always allowed.

Removal/overwrite is allowed ONLY when the record is proven wrong AND
he (or his direct AI order) confirms it. Both conditions required.
"""
import json
import os
import time

REPO = os.path.expanduser("~/workspace/jah-databases")
POLICY_PATH = os.path.join(REPO, "data", "governance.json")
LOG_PATH = os.path.join(REPO, "data", "governance-log.jsonl")


class GovernanceError(RuntimeError):
    pass


def _policy():
    try:
        with open(POLICY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise GovernanceError(
            "data/governance.json missing — destructive ops refused until "
            "the lock-in policy file exists (STEP ZERO).")


def assert_mutation_allowed(op, record_id, proof=None, confirmed_by=None):
    """op: 'delete' or 'overwrite'. Raises GovernanceError unless allowed.

    proof: evidence the record is wrong (citation, measurement, diff).
    confirmed_by: 'manon' or 'direct-ai-order:<ref>'.
    """
    _policy()  # ensure policy file exists
    if op not in ("delete", "overwrite"):
        raise GovernanceError("unknown destructive op %r" % (op,))
    if not proof:
        raise GovernanceError(
            "refused %s of %s: no proof the record is wrong" % (op, record_id))
    if confirmed_by not in ("manon",) and not (
            isinstance(confirmed_by, str)
            and confirmed_by.startswith("direct-ai-order:")):
        raise GovernanceError(
            "refused %s of %s: requires his confirmation "
            "(confirmed_by='manon' or 'direct-ai-order:<ref>')" % (op, record_id))
    entry = {"ts": int(time.time()), "op": op, "record_id": record_id,
             "proof": proof, "confirmed_by": confirmed_by}
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return True


def is_additive_only_ok():
    """Additive operations (new records, reorganization) are always allowed."""
    _policy()
    return True
