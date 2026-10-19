#!/usr/bin/env python3
"""Demo programs for the Trust Emotion databases (Manon 2026-10-17 16:15
order, emotion series batch 1).

Every demo is an emotion-scenario simulator: a situation plus an intensity
curve, simulated scene by scene from trigger through peak to resolution,
with computed inner-state intensity, body signals (heart rate, breath,
muscle ease), facial-expression metrics (eye softness, brow rest, mouth
ease), and one record-specific computed block (ledger, cascade, dyads,
detection accuracy, and so on). All are real, runnable, stdlib-only Python.

Machine-executed by build.py before commit: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker. Emit-time expected values come from exec'ing the exact
emitted source, so baked bounds are guaranteed consistent.

Descriptive/educational only - never diagnosing anyone.
"""

import json as _json
import math as _math

# ---------------------------------------------------------------- emitter
# The core simulator source. Placeholders __BASE__ etc. are pure numbers/
# reprs - no logic is substituted, so the emit-time exec and the emitted
# program run bit-identical computations.

_CORE = (
"import math\n"
"def icurve(t, base, rise, t_peak, rise_tau, decay_tau):\n"
"    if t <= t_peak:\n"
"        return base + (rise - base) * (1.0 - math.exp(-t / rise_tau))\n"
"    v_peak = base + (rise - base) * (1.0 - math.exp(-t_peak / rise_tau))\n"
"    return base + (v_peak - base) * math.exp(-(t - t_peak) / decay_tau)\n"
"BASE = __BASE__\nRISE = __RISE__\nT_PEAK = __T_PEAK__\n"
"RISE_TAU = __RISE_TAU__\nDECAY_TAU = __DECAY_TAU__\n"
"SCENES = __SCENES__\n"
"def heart_rate(i):\n"
"    return 62.0 + 0.38 * i\n"
"def breath_rate(i):\n"
"    return 12.0 + 0.10 * i\n"
"def muscle_ease(i):\n"
"    return 30.0 + 0.60 * i\n"
"def eye_soft(i):\n"
"    return i / 100.0\n"
"def brow_rest(i):\n"
"    return 0.15 + 0.75 * i / 100.0\n"
"def mouth_ease(i):\n"
"    return 0.05 + 0.85 * (i / 100.0) ** 1.5\n"
"def _metrics(i):\n"
"    return (heart_rate(i), breath_rate(i), muscle_ease(i), eye_soft(i), brow_rest(i), mouth_ease(i))\n"
"ROWS = []\n"
"for _sn, _t in SCENES:\n"
"    _i = icurve(_t, BASE, RISE, T_PEAK, RISE_TAU, DECAY_TAU)\n"
"    _hr, _br, _ea, _ey, _bw, _mo = _metrics(_i)\n"
"    ROWS.append((_sn, _t, _i, _hr, _br, _ea, _ey, _bw, _mo))\n"
)

_EXTRA_TMPL = {
"ledger": (
 "KEPT = __KEPT__\nBROKEN = __BROKEN__\n"
 "KEPT_W = __KEPT_W__\nBROKEN_W = __BROKEN_W__\n"
 "LEDGER_SCORE = 100.0 * KEPT / (KEPT + BROKEN)\n"
 "LEDGER_WSCORE = 100.0 * sum(KEPT_W) / (sum(KEPT_W) + sum(BROKEN_W))\n"),
"family": (
 "COG = __COG__\nAFF = __AFF__\n"
 "TRUST_COMP = (COG + AFF) / 2.0\n"),
"volumes": (
 "VOLS = __VOLS__\nVOL_ROWS = []\n"
 "for _v in VOLS:\n"
 "    _hr, _br, _ea, _ey, _bw, _mo = _metrics(_v)\n"
 "    VOL_ROWS.append((_v, _hr, _br, _ea, _ey, _bw, _mo))\n"),
"mythdecay": (
 "MYTH0 = __MYTH0__\nFACTS = __FACTS__\n"
 "MYTH_END = MYTH0 * math.exp(-FACTS / 2.0)\n"),
"dyad": (
 "D_T = __D_T__\nD_P = __D_P__\n"
 "DYAD_MEAN = (D_T + D_P) / 2.0\nDYAD_SYN = D_T * D_P / 100.0\n"),
"dyads4": (
 "D_T4 = __D_T4__\nPARTNERS = __PARTNERS__\n"
 "DYAD4 = []\n"
 "for _pl, _pv in PARTNERS:\n"
 "    DYAD4.append((_pl, (D_T4 + _pv) / 2.0, D_T4 * _pv / 100.0))\n"),
"cascade": (
 "TRIGGERS = __TRIGGERS__\nCASC = []\n_CASCA = 0.0\n"
 "for _tl, _tw in TRIGGERS:\n"
 "    _CASCA = _CASCA + _tw * (1.0 - _CASCA / 100.0)\n"
 "    CASC.append((_tl, _CASCA))\n"),
"transfer": (
 "PRIOR = __PRIOR__\nRESEMBL = __RESEMBL__\n"
 "TRANSFERRED = PRIOR * RESEMBL\n"),
"motive": (
 "EVENTS = __EVENTS__\nCREDITED = []\n"
 "for _el, _ew, _em in EVENTS:\n"
 "    CREDITED.append((_el, _ew * (1.0 - _em)))\n"),
"actions": (
 "I_ACT = __I_ACT__\nACTS = __ACTS__\n"
 "ACTP = []\n"
 "for _al, _aw in ACTS:\n"
 "    ACTP.append((_al, min(0.97, _aw * I_ACT / 100.0)))\n"),
"speech": (
 "I_SP = __I_SP__\n"
 "HEDGE_WORDS = int(round((100.0 - I_SP) / 8.0))\n"
 "PLAINNESS = I_SP\n"),
"decisions": (
 "I_DEC = __I_DEC__\nVERIFY_K = __VERIFY_K__\n"
 "VERIFY_SAVED = VERIFY_K * I_DEC\n"
 "AUDIT_LEVEL = max(0.0, 20.0 - I_DEC / 10.0)\n"),
"stake": (
 "BAL = __BAL__\nI_ST = __I_ST__\n"
 "MAX_STAKE = BAL * I_ST / 100.0\n"),
"expressq": (
 "FACTORS = __FACTORS__\n"
 "EXPR_Q = 100.0 * sum(_s * _w for _fl, _s, _w in FACTORS) / (10.0 * sum(_w for _fl, _s, _w in FACTORS))\n"),
"calib": (
 "BLIND_STAKE = __BLIND_STAKE__\nBLIND_EVID = __BLIND_EVID__\n"
 "DISTRUST_STAKE = __DISTRUST_STAKE__\nDISTRUST_EVID = __DISTRUST_EVID__\n"
 "CALIB_BLIND = abs(BLIND_STAKE - BLIND_EVID)\n"
 "CALIB_DISTRUST = abs(DISTRUST_STAKE - DISTRUST_EVID)\n"),
"practices": (
 "DEPOSITS = __DEPOSITS__\nDAYS = __DAYS__\nDECAY = __DECAY__\n"
 "PRACT_BAL = sum(DEPOSITS) * sum(DECAY ** _d for _d in range(DAYS))\n"),
"cues": (
 "CUES = __CUES__\n"
 "CUE_HITS = sum(1 for _cl, _present, _det in CUES if _present == _det)\n"
 "CUE_ACC = CUE_HITS / len(CUES)\n"),
"support": (
 "RESPS = __RESPS__\n"
 "SUPPORT_MEAN = sum(_s for _rl, _s in RESPS) / len(RESPS)\n"),
"damage": (
 "SEV = __SEV__\nREPAIR_DAY = __REPAIR_DAY__\nREPAIR_MONTH = __REPAIR_MONTH__\n"
 "HURT_DAY = SEV * (1.0 - REPAIR_DAY)\n"
 "HURT_MONTH = SEV * (1.0 - REPAIR_MONTH)\n"),
"simmatrix": (
 "VECS = __VECS__\n"
 "def _cos(_a, _b):\n"
 "    _dot = sum(_x * _y for _x, _y in zip(_a, _b))\n"
 "    _na = math.sqrt(sum(_x * _x for _x in _a))\n"
 "    _nb = math.sqrt(sum(_x * _x for _x in _b))\n"
 "    return _dot / (_na * _nb)\n"
 "SIMS = [(_k, _cos(VECS[\"trust\"], _v)) for _k, _v in VECS.items() if _k != \"trust\"]\n"),
"profiles": (
 "I_PROF = __I_PROF__\nOFFSETS = __OFFSETS__\n"
 "PROF_R = [min(100.0, max(0.0, I_PROF + _o)) for _o in OFFSETS]\n"
 "PROF_MEAN = sum(PROF_R) / len(PROF_R)\n"
 "PROF_SPREAD = max(PROF_R) - min(PROF_R)\n"),
"posture": (
 "I_PO = __I_PO__\n"
 "TORSO_OPEN = 20.0 + 0.6 * I_PO\n"
 "LEAN_IN = 0.05 * I_PO\n"),
"sleep": (
 "I_SL = __I_SL__\n"
 "SLEEP_Q = 40.0 + 0.5 * I_SL\n"
 "LATENCY = 45.0 - 0.35 * I_SL\n"),
"leak": (
 "FELT = __FELT__\nSHOWN = __SHOWN__\nLEAKF = __LEAKF__\n"
 "LEAK = abs(FELT - SHOWN) * LEAKF\n"),
"landmarks": (
 "I_LM = __I_LM__\n"
 "BROW_Y = __BY0__ - __BYK__ * I_LM\n"
 "EYE_OPEN = __EO0__ + __EOK__ * I_LM\n"
 "MOUTH_C = __MC0__ + __MCK__ * (I_LM / 100.0) ** 1.5\n"),
"pulses": (
 "PULSES = __PULSES__\n"
 "PROWS = []\n"
 "for (_sn, _t, _i, _hr, _br, _ea, _ey, _bw, _mo), _p in zip(ROWS, PULSES):\n"
 "    _i2 = min(100.0, _i + _p)\n"
 "    _hr2, _br2, _ea2, _ey2, _bw2, _mo2 = _metrics(_i2)\n"
 "    PROWS.append((_sn, _t, _i2, _hr2, _br2, _ea2, _ey2, _bw2, _mo2))\n"),
"lowhigh": (
 "BASE2 = __BASE2__\nRISE2 = __RISE2__\n"
 "ROWS2 = []\n"
 "for _sn, _t in SCENES:\n"
 "    _i2 = icurve(_t, BASE2, RISE2, T_PEAK, RISE_TAU, DECAY_TAU)\n"
 "    _hr2, _br2, _ea2, _ey2, _bw2, _mo2 = _metrics(_i2)\n"
 "    ROWS2.append((_sn, _t, _i2, _hr2, _br2, _ea2, _ey2, _bw2, _mo2))\n"),
"runcan": (
 "FLOW = __FLOW__\nRUNBAL = []\n_RB = 0.0\n"
 "for _fl, _fd in FLOW:\n"
 "    _RB = _RB + _fd\n"
 "    RUNBAL.append((_fl, _RB))\n"),
}

import re as _re

def _tb(var, v, tol=0.005):
    return "    assert %.4f < %s < %.4f" % (v - tol, var, v + tol)


def _xb_ledger(ns):
    return [
        '    print("trust ledger: %d kept, %d broken" % (KEPT, BROKEN))',
        '    print("ledger trust score: %.2f   recency-weighted: %.2f" % (LEDGER_SCORE, LEDGER_WSCORE))',
        "    assert 0.0 <= LEDGER_SCORE <= 100.0",
        "    assert 0.0 <= LEDGER_WSCORE <= 100.0",
        _tb("LEDGER_SCORE", ns["LEDGER_SCORE"]),
        _tb("LEDGER_WSCORE", ns["LEDGER_WSCORE"]),
    ]


def _xb_family(ns):
    return [
        '    print("trust composition: cognition-based=%.1f affect-based=%.1f composite=%.2f" % (COG, AFF, TRUST_COMP))',
        "    assert 0.0 <= TRUST_COMP <= 100.0",
        _tb("TRUST_COMP", ns["TRUST_COMP"]),
    ]


def _xb_volumes(ns):
    L = ['    print("three volumes of trust: mild / moderate / intense")',
         '    for _v, _hr, _br, _ea, _ey, _bw, _mo in VOL_ROWS:',
         '        print("  intensity=%5.1f  hr=%5.1f bpm  breath=%4.1f/min  ease=%4.1f  eye=%.2f brow=%.2f mouth=%.2f" % (_v, _hr, _br, _ea, _ey, _bw, _mo))',
         "    assert VOL_ROWS[0][0] < VOL_ROWS[1][0] < VOL_ROWS[2][0]",
         "    assert VOL_ROWS[2][1] > VOL_ROWS[0][1]"]
    for i, row in enumerate(ns["VOL_ROWS"]):
        L.append(_tb("VOL_ROWS[%d][1]" % i, row[1], 0.01))
    return L


def _xb_mythdecay(ns):
    return [
        '    print("myth endorsement: start=%.1f after %d facts: %.2f" % (MYTH0, FACTS, MYTH_END))',
        "    assert MYTH_END < MYTH0",
        "    assert MYTH_END >= 0.0",
        _tb("MYTH_END", ns["MYTH_END"]),
    ]


def _xb_dyad(ns):
    return [
        '    print("dyad blend: trust=%.1f partner=%.1f mean=%.2f synergy=%.2f" % (D_T, D_P, DYAD_MEAN, DYAD_SYN))',
        "    assert 0.0 <= DYAD_SYN <= 100.0",
        _tb("DYAD_MEAN", ns["DYAD_MEAN"]),
        _tb("DYAD_SYN", ns["DYAD_SYN"]),
    ]


def _xb_dyads4(ns):
    L = ['    print("four trust blends (Plutchik-style dyads):")',
         '    for _pl, _mn, _sy in DYAD4:',
         '        print("  %-28s mean=%5.2f synergy=%5.2f" % (_pl, _mn, _sy))',
         "    assert len(DYAD4) == 4"]
    for i, row in enumerate(ns["DYAD4"]):
        L.append(_tb("DYAD4[%d][1]" % i, row[1]))
        L.append("    assert 0.0 <= DYAD4[%d][2] <= 100.0" % i)
    return L


def _xb_cascade(ns):
    L = ['    print("trigger cascade (activation accumulates, saturating):")',
         '    for _tl, _a in CASC:',
         '        print("  %-34s activation=%5.1f" % (_tl, _a))',
         "    _prev = 0.0",
         "    for _tl, _a in CASC:",
         "        assert _a >= _prev - 1e-9",
         "        assert 0.0 <= _a <= 100.0",
         "        _prev = _a",
         "    assert CASC[-1][1] > CASC[0][1]"]
    L.append(_tb("CASC[-1][1]", ns["CASC"][-1][1]))
    return L


def _xb_transfer(ns):
    return [
        '    print("prior trust=%.1f resemblance=%.2f transferred=%.2f" % (PRIOR, RESEMBL, TRANSFERRED))',
        "    assert 0.0 <= TRANSFERRED <= 100.0",
        _tb("TRANSFERRED", ns["TRANSFERRED"]),
    ]


def _xb_motive(ns):
    L = ['    print("motive-discounted trigger credit:")',
         '    for _el, _c in CREDITED:',
         '        print("  %-30s credited=%.2f" % (_el, _c))']
    for i, row in enumerate(ns["CREDITED"]):
        L.append("    assert 0.0 <= CREDITED[%d][1] <= 30.0" % i)
        L.append(_tb("CREDITED[%d][1]" % i, row[1]))
    return L


def _xb_actions(ns):
    L = ['    print("trust action probabilities at intensity %.1f:" % I_ACT)',
         '    for _al, _p in ACTP:',
         '        print("  %-30s p=%.3f" % (_al, _p))']
    for i, row in enumerate(ns["ACTP"]):
        L.append("    assert 0.0 <= ACTP[%d][1] <= 0.97" % i)
        L.append(_tb("ACTP[%d][1]" % i, row[1], 0.0005))
    return L


def _xb_speech(ns):
    return [
        '    print("hedge words per 100: %d   plainness: %.1f" % (HEDGE_WORDS, PLAINNESS))',
        "    assert HEDGE_WORDS >= 0",
        "    assert 0.0 <= PLAINNESS <= 100.0",
        _tb("PLAINNESS", ns["PLAINNESS"]),
    ]


def _xb_decisions(ns):
    return [
        '    print("verification cost saved: %.1f   background audit level: %.1f" % (VERIFY_SAVED, AUDIT_LEVEL))',
        "    assert VERIFY_SAVED > 0.0",
        "    assert 0.0 <= AUDIT_LEVEL <= 20.0",
        _tb("VERIFY_SAVED", ns["VERIFY_SAVED"]),
        _tb("AUDIT_LEVEL", ns["AUDIT_LEVEL"]),
    ]


def _xb_stake(ns):
    return [
        '    print("ledger balance: %.0f  authorized max stake: %.1f" % (BAL, MAX_STAKE))',
        "    assert MAX_STAKE <= BAL",
        "    assert MAX_STAKE > 0.0",
        _tb("MAX_STAKE", ns["MAX_STAKE"], 0.05),
    ]


def _xb_expressq(ns):
    L = ['    print("healthy-expression factors:")',
         '    for _fl, _s, _w in FACTORS:',
         '        print("  %-18s score=%.1f weight=%.1f" % (_fl, _s, _w))',
         '    print("expression quality: %.2f / 100" % EXPR_Q)',
         "    assert 0.0 <= EXPR_Q <= 100.0"]
    L.append(_tb("EXPR_Q", ns["EXPR_Q"]))
    return L


def _xb_calib(ns):
    return [
        '    print("calibration error: blind trust=%.1f  chronic distrust=%.1f" % (CALIB_BLIND, CALIB_DISTRUST))',
        "    assert CALIB_BLIND > 40.0",
        "    assert CALIB_DISTRUST > 40.0",
        _tb("CALIB_BLIND", ns["CALIB_BLIND"], 0.05),
        _tb("CALIB_DISTRUST", ns["CALIB_DISTRUST"], 0.05),
    ]


def _xb_practices(ns):
    return [
        '    print("daily deposits=%d days=%d -> compounded balance: %.2f" % (len(DEPOSITS), DAYS, PRACT_BAL))',
        "    assert PRACT_BAL > sum(DEPOSITS)",
        _tb("PRACT_BAL", ns["PRACT_BAL"], 0.05),
    ]


def _xb_cues(ns):
    L = ['    print("cue detection: %d/%d correct -> accuracy=%.2f" % (CUE_HITS, len(CUES), CUE_ACC))',
         "    assert 0.0 <= CUE_ACC <= 1.0"]
    L.append(_tb("CUE_ACC", ns["CUE_ACC"], 0.0005))
    return L


def _xb_support(ns):
    L = ['    print("supportive responses:")',
         '    for _rl, _s in RESPS:',
         '        print("  %-18s score=%.1f" % (_rl, _s))',
         '    print("mean response quality: %.2f / 10" % SUPPORT_MEAN)',
         "    assert 0.0 <= SUPPORT_MEAN <= 10.0"]
    L.append(_tb("SUPPORT_MEAN", ns["SUPPORT_MEAN"], 0.0005))
    return L


def _xb_damage(ns):
    return [
        '    print("residual hurt: repaired same day=%.1f  repaired after a month=%.1f" % (HURT_DAY, HURT_MONTH))',
        "    assert HURT_DAY < HURT_MONTH",
        "    assert HURT_DAY >= 0.0",
        _tb("HURT_DAY", ns["HURT_DAY"], 0.05),
        _tb("HURT_MONTH", ns["HURT_MONTH"], 0.05),
    ]


def _xb_simmatrix(ns):
    L = ['    print("similarity to trust (cosine over appraisal features):")',
         '    for _k, _s in SIMS:',
         '        print("  %-14s similarity=%.4f" % (_k, _s))',
         "    assert all(0.0 < _s <= 1.0 for _k, _s in SIMS)"]
    for i, row in enumerate(ns["SIMS"]):
        L.append(_tb("SIMS[%d][1]" % i, row[1], 0.00005))
    return L


def _xb_profiles(ns):
    return [
        '    print("five bodies, one trust level (offsets applied):")',
        '    print("  responses: " + " ".join("%.1f" % _x for _x in PROF_R))',
        '    print("  mean=%.2f spread=%.1f" % (PROF_MEAN, PROF_SPREAD))',
        "    assert PROF_SPREAD > 0.0",
        _tb("PROF_MEAN", ns["PROF_MEAN"]),
        _tb("PROF_SPREAD", ns["PROF_SPREAD"], 0.05),
    ]


def _xb_posture(ns):
    return [
        '    print("torso openness: %.1f deg   lean-in: %.2f cm" % (TORSO_OPEN, LEAN_IN))',
        "    assert 20.0 <= TORSO_OPEN <= 80.0",
        _tb("TORSO_OPEN", ns["TORSO_OPEN"]),
        _tb("LEAN_IN", ns["LEAN_IN"], 0.0005),
    ]


def _xb_sleep(ns):
    return [
        '    print("sleep quality: %.1f / 100   sleep latency: %.2f min" % (SLEEP_Q, LATENCY))',
        "    assert 40.0 <= SLEEP_Q <= 100.0",
        "    assert 5.0 <= LATENCY <= 45.0",
        _tb("SLEEP_Q", ns["SLEEP_Q"]),
        _tb("LATENCY", ns["LATENCY"]),
    ]


def _xb_leak(ns):
    return [
        '    print("felt=%.1f shown=%.1f leakage signal: %.2f" % (FELT, SHOWN, LEAK))',
        "    assert LEAK > 15.0",
        _tb("LEAK", ns["LEAK"]),
    ]


def _xb_landmarks(ns):
    return [
        '    print("artist landmarks at intensity %.1f:" % I_LM)',
        '    print("  brow height: %.2f   eye openness: %.2f   mouth curvature: %.3f" % (BROW_Y, EYE_OPEN, MOUTH_C))',
        _tb("BROW_Y", ns["BROW_Y"]),
        _tb("EYE_OPEN", ns["EYE_OPEN"]),
        _tb("MOUTH_C", ns["MOUTH_C"], 0.0005),
    ]


def _xb_lowhigh(ns):
    L = ['    print("low-intensity (left) vs high-intensity (right) trust, same moments:")',
         '    for (_sn, _t, _i, _hr, _x1, _x2, _x3, _x4, _x5), (_s2, _t2, _j, _hr2, _y1, _y2, _y3, _y4, _y5) in zip(ROWS2, ROWS):',
         '        print("  t=%5.1f  %-24s low i=%5.1f hr=%5.1f | high i=%5.1f hr=%5.1f" % (_t, _sn, _i, _hr, _j, _hr2))',
         "    assert all(_b[2] >= _a[2] - 1e-9 for _a, _b in zip(ROWS2, ROWS))"]
    j = max(ns["ROWS"], key=lambda r: r[2])[2]
    L.append(_tb("max(_r[2] for _r in ROWS)", j))
    return L


def _xb_pulses(ns):
    L = ['    print("day pulses applied (small deposits lift each scene):")',
         "    assert all(_b[2] >= _a[2] - 1e-9 for _a, _b in zip(ROWS, PROWS))",
         "    assert all(_r[2] <= 100.0 for _r in PROWS)"]
    fin = ns["PROWS"][-1][2]
    L.append(_tb("PROWS[-1][2]", fin))
    return L


def _xb_runcan(ns):
    L = ['    print("running ledger balance through the simulation:")',
         '    for _fl, _b in RUNBAL:',
         '        print("  %-30s balance=%6.1f" % (_fl, _b))',
         "    assert RUNBAL[-1][1] > 0.0"]
    L.append(_tb("RUNBAL[-1][1]", ns["RUNBAL"][-1][1], 0.05))
    return L


_XB = {
    "ledger": _xb_ledger, "family": _xb_family, "volumes": _xb_volumes,
    "mythdecay": _xb_mythdecay, "dyad": _xb_dyad, "dyads4": _xb_dyads4,
    "cascade": _xb_cascade, "transfer": _xb_transfer, "motive": _xb_motive,
    "actions": _xb_actions, "speech": _xb_speech, "decisions": _xb_decisions,
    "stake": _xb_stake, "expressq": _xb_expressq, "calib": _xb_calib,
    "practices": _xb_practices, "cues": _xb_cues, "support": _xb_support,
    "damage": _xb_damage, "simmatrix": _xb_simmatrix, "profiles": _xb_profiles,
    "posture": _xb_posture, "sleep": _xb_sleep, "leak": _xb_leak,
    "landmarks": _xb_landmarks, "lowhigh": _xb_lowhigh, "pulses": _xb_pulses,
    "runcan": _xb_runcan,
}


def _sim(hdr_fn, name, rid, group, scenario, brief, scenes, curve,
         extra=None, monologue=None, ok_line="ran the trust scenario simulator"):
    src = _CORE
    for k in ("BASE", "RISE", "T_PEAK", "RISE_TAU", "DECAY_TAU"):
        src = src.replace("__%s__" % k, repr(curve[k.lower()]))
    src = src.replace("__SCENES__", repr(scenes))
    xb_kind = None
    if extra:
        xb_kind, params = extra
        t = _EXTRA_TMPL[xb_kind]
        for k, v in params.items():
            t = t.replace("__%s__" % k, v)
        left = _re.findall(r"__[A-Z_0-9]+__", t)
        assert not left, "unfilled placeholders %s in %s" % (left, xb_kind)
        src += t
    ns = {}
    exec(src, ns)  # emit-time expected values from the exact emitted source
    rows_var = "PROWS" if xb_kind == "pulses" else "ROWS"
    rows = ns[rows_var]

    L = []
    L.append(hdr_fn(name, rid, group).rstrip("\n"))
    L.append(src)
    if monologue:
        L.append("MONO = " + repr(monologue))
    L.append("def main():")
    L.append('    print("=" * 64)')
    L.append("    print(" + _json.dumps("SCENARIO: " + scenario) + ")")
    L.append("    print(" + _json.dumps("BRIEF: " + brief) + ")")
    if monologue:
        L.append("    assert len(MONO) == len(ROWS)")
        L.append("    for (_sn, _t, _i, _hr, _br, _ea, _ey, _bw, _mo), _ml in zip(ROWS, MONO):")
        L.append('        print("  t=%7.1f min  %-26s intensity=%5.1f  hr=%5.1f bpm  breath=%4.1f/min  ease=%4.1f" % (_t, _sn, _i, _hr, _br, _ea))')
        L.append('        print("                 face: eye_soft=%.2f brow_rest=%.2f mouth_ease=%.2f" % (_ey, _bw, _mo))')
        L.append('        print("                 inner: " + _ml)')
    elif xb_kind == "lowhigh":
        pass  # custom table printed by the extra block
    else:
        L.append("    for _sn, _t, _i, _hr, _br, _ea, _ey, _bw, _mo in %s:" % rows_var)
        L.append('        print("  t=%7.1f min  %-26s intensity=%5.1f  hr=%5.1f bpm  breath=%4.1f/min  ease=%4.1f" % (_t, _sn, _i, _hr, _br, _ea))')
        L.append('        print("                 face: eye_soft=%.2f brow_rest=%.2f mouth_ease=%.2f" % (_ey, _bw, _mo))')
    L.append("    for _r in %s:" % rows_var)
    L.append("        assert 0.0 <= _r[2] <= 100.0")
    L.append("        assert 55.0 <= _r[3] <= 110.0")
    L.append("        assert 10.0 <= _r[4] <= 25.0")
    L.append("        assert 25.0 <= _r[5] <= 95.0")
    L.append("        assert 0.0 <= _r[6] <= 1.0 and 0.0 <= _r[7] <= 1.0 and 0.0 <= _r[8] <= 1.0")
    L.append("    _on = [_r for _r in %s if _r[1] <= T_PEAK]" % rows_var)
    L.append("    for _a, _b in zip(_on, _on[1:]):")
    L.append("        assert _b[2] >= _a[2] - 1e-9")
    pk = max(rows, key=lambda r: r[2])
    L.append("    assert %.4f < max(_r[2] for _r in %s) < %.4f" % (pk[2] - 0.005, rows_var, pk[2] + 0.005))
    L.append("    assert %.4f < %s[0][2] < %.4f" % (rows[0][2] - 0.005, rows_var, rows[0][2] + 0.005))
    L.append("    assert %.4f < %s[-1][3] < %.4f" % (rows[-1][3] - 0.005, rows_var, rows[-1][3] + 0.005))
    if xb_kind:
        L.extend(_XB[xb_kind](ns))
    L.append("    print(" + _json.dumps("OK: " + name + " " + ok_line) + ")")
    L.append('if __name__ == "__main__":')
    L.append("    main()")
    return "\n".join(L) + "\n"

# ------------------------------------------------------- demo functions
# Each simulates a trust scenario for its record: situation + intensity
# curve across scenes, with computed body and face metrics and a
# record-specific computed block. All values are computed at run time;
# tight bounds are baked from the identical emit-time computation.

def demo_trust_definition(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Borrowed Ladder",
        brief="A new colleague borrows a ladder, then a trailer, then a weekend: probes sized to a fresh ledger.",
        scenes=[("first handshake", 0.0), ("ladder returned clean", 20.0),
                ("trailer lent and returned", 45.0), ("weekend project together", 90.0),
                ("the easy season after", 150.0)],
        curve={"base": 5.0, "rise": 55.0, "t_peak": 60.0, "rise_tau": 25.0, "decay_tau": 120.0},
        extra=("ledger", {"KEPT": "9", "BROKEN": "1",
                          "KEPT_W": "[5, 4, 4, 3, 3, 2, 2, 1, 1]", "BROKEN_W": "[4]"}),
        ok_line="ran the trust-ledger scenario simulator")


def demo_trust_emotion_family(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Mapping the Neighborhood",
        brief="Charting where trust sits among the emotions: appraisal-heavy, socially bound, opposite disgust.",
        scenes=[("naming the feeling", 0.0), ("placing it on the wheel", 15.0),
                ("tracing its neighbors", 30.0), ("the map complete", 50.0)],
        curve={"base": 10.0, "rise": 70.0, "t_peak": 35.0, "rise_tau": 15.0, "decay_tau": 80.0},
        extra=("family", {"COG": "72.0", "AFF": "68.0"}),
        ok_line="ran the emotion-family scenario simulator")


def demo_trust_intensity_levels(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Three Volumes",
        brief="The same trust at mild, moderate, and intense volume: the trimmer, the project, the midnight drive.",
        scenes=[("the trimmer lent", 0.0), ("the project delegated", 30.0),
                ("the midnight drive", 60.0)],
        curve={"base": 8.0, "rise": 92.0, "t_peak": 45.0, "rise_tau": 18.0, "decay_tau": 100.0},
        extra=("volumes", {"VOLS": "[22.0, 55.0, 92.0]"}),
        ok_line="ran the three-volumes scenario simulator")


def demo_trust_myths(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Slogan Audit",
        brief="Six myths about trust meet six facts; endorsement decays with each fact absorbed.",
        scenes=[("myth stated", 0.0), ("first fact lands", 12.0),
                ("the ledger shown", 25.0), ("myth retired", 40.0)],
        curve={"base": 12.0, "rise": 66.0, "t_peak": 28.0, "rise_tau": 12.0, "decay_tau": 70.0},
        extra=("mythdecay", {"MYTH0": "80.0", "FACTS": "6"}),
        ok_line="ran the myth-audit scenario simulator")


def demo_trust_first_person(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="An Unhurried Hour",
        brief="Inside the feeling: one hour with a trusted friend, narrated from within.",
        scenes=[("sitting down", 0.0), ("the unedited story", 15.0),
                ("laughter, unguarded", 30.0), ("the quiet minute", 45.0),
                ("walking home light", 60.0)],
        curve={"base": 20.0, "rise": 85.0, "t_peak": 40.0, "rise_tau": 16.0, "decay_tau": 90.0},
        monologue=[
            "My shoulders drop before I decide to relax them.",
            "I tell it the way it happened, embarrassing part included, no editing.",
            "The laugh starts in my eyes; I am not managing any impression.",
            "Nothing needs saying. Being known and safe is enough.",
            "Time felt unhurried, as if there were enough of it."],
        ok_line="ran the first-person scenario simulator")


def demo_trust_over_time(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Eighteen Months",
        brief="The arc: onset probes, the rise of evidence, the plateau, a slow fade, and the aftershock.",
        scenes=[("first week, testing", 0.0), ("month one, probes pass", 60.0),
                ("month six, the plateau", 180.0), ("month twelve, ease", 300.0),
                ("month fifteen, the fade", 420.0), ("month eighteen, aftershock", 540.0)],
        curve={"base": 8.0, "rise": 88.0, "t_peak": 260.0, "rise_tau": 110.0, "decay_tau": 200.0},
        ok_line="ran the arc-of-trust scenario simulator")


def demo_trust_low_vs_high(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Trimmer and the Midnight Drive",
        brief="Low-intensity trust (a lent trimmer, hypothesis under test) beside high-intensity trust (the midnight hospital drive, settled fact).",
        scenes=[("the ask", 0.0), ("the handover", 20.0), ("the follow-through", 50.0)],
        curve={"base": 5.0, "rise": 92.0, "t_peak": 35.0, "rise_tau": 15.0, "decay_tau": 90.0},
        extra=("lowhigh", {"BASE2": "5.0", "RISE2": "25.0"}),
        ok_line="ran the low-vs-high scenario simulator")


def demo_trust_mixed_affection(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Gilded Seal",
        brief="Trust blended with affection: the warm core of close bonds, and the bribe effect to watch for.",
        scenes=[("fondness arrives", 0.0), ("the blend warms", 18.0),
                ("checking the ledger anyway", 36.0), ("the alloy holds", 55.0)],
        curve={"base": 15.0, "rise": 78.0, "t_peak": 38.0, "rise_tau": 16.0, "decay_tau": 85.0},
        extra=("dyad", {"D_T": "75.0", "D_P": "80.0"}),
        ok_line="ran the trust-affection blend simulator")


def demo_trust_day_in_life(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="A Tuesday",
        brief="Trust as climate: small deposits through an ordinary day, each lifting the running balance.",
        scenes=[("morning: the kept appointment", 0.0), ("midday: the unhovered project", 120.0),
                ("afternoon: the honest fender", 300.0), ("evening: the unguarded table", 480.0),
                ("night: the airport run", 660.0)],
        curve={"base": 30.0, "rise": 70.0, "t_peak": 400.0, "rise_tau": 180.0, "decay_tau": 500.0},
        extra=("pulses", {"PULSES": "[8.0, 12.0, 15.0, 10.0, 6.0]"}),
        ok_line="ran the day-in-the-life scenario simulator")


def demo_trust_body(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Quiet Body",
        brief="Heart, breath, muscle, and energy as the safety prediction rises and the body stands down.",
        scenes=[("arrival, guarded", 0.0), ("first ease", 10.0),
                ("shoulders drop", 25.0), ("the long exhale", 45.0),
                ("restorative evening", 80.0)],
        curve={"base": 10.0, "rise": 80.0, "t_peak": 50.0, "rise_tau": 20.0, "decay_tau": 110.0},
        ok_line="ran the body-signals scenario simulator")


def demo_trust_posture(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Open Room",
        brief="Torso uncrosses, the head tilts, distance closes: the posture of nothing to hide.",
        scenes=[("doorway, angled", 0.0), ("sitting, uncrossing", 12.0),
                ("leaning in", 28.0), ("the tilt", 45.0)],
        curve={"base": 12.0, "rise": 72.0, "t_peak": 32.0, "rise_tau": 14.0, "decay_tau": 75.0},
        extra=("posture", {"I_PO": "70.0"}),
        ok_line="ran the posture scenario simulator")


def demo_trust_sleep_appetite(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Easy Night",
        brief="Sleep comes faster and the gut unclenches when the threat budget drops.",
        scenes=[("restless week", 0.0), ("the safe house", 20.0),
                ("dinner enjoyed", 45.0), ("sleep, unguarded", 75.0)],
        curve={"base": 15.0, "rise": 75.0, "t_peak": 50.0, "rise_tau": 22.0, "decay_tau": 100.0},
        extra=("sleep", {"I_SL": "75.0"}),
        ok_line="ran the sleep-and-appetite scenario simulator")


def demo_trust_body_differences(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Five Bodies, One Feeling",
        brief="The same trust level lands differently in five bodies: expressive, quiet, hot-idling, cool, and tired.",
        scenes=[("baseline reading", 0.0), ("the trusted hour", 30.0),
                ("comparison", 60.0)],
        curve={"base": 20.0, "rise": 65.0, "t_peak": 40.0, "rise_tau": 18.0, "decay_tau": 80.0},
        extra=("profiles", {"I_PROF": "65.0", "OFFSETS": "[-8.0, -3.0, 0.0, 4.0, 9.0]"}),
        ok_line="ran the individual-differences scenario simulator")


def demo_trust_face(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Unhidden Face",
        brief="Eye crinkles, resting brow, loose jaw: the involuntary markers of the trusting face.",
        scenes=[("neutral arrival", 0.0), ("recognition", 8.0),
                ("the genuine smile", 18.0), ("at rest together", 35.0)],
        curve={"base": 10.0, "rise": 78.0, "t_peak": 24.0, "rise_tau": 10.0, "decay_tau": 60.0},
        ok_line="ran the facial-expression scenario simulator")


def demo_trust_face_intensity(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Three Faces",
        brief="Polite openness, genuine markers, then the retired performance of deep trust.",
        scenes=[("polite openness", 0.0), ("genuine markers", 25.0),
                ("performance retired", 55.0)],
        curve={"base": 10.0, "rise": 90.0, "t_peak": 40.0, "rise_tau": 16.0, "decay_tau": 90.0},
        extra=("volumes", {"VOLS": "[20.0, 55.0, 90.0]"}),
        ok_line="ran the face-intensity scenario simulator")


def demo_trust_face_hidden_faked(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Painted Seal",
        brief="Felt wariness beneath a performed warmth: measuring what leaks through the managed face.",
        scenes=[("the performance begins", 0.0), ("holding the smile", 15.0),
                ("the leak", 30.0), ("incongruence noticed", 45.0)],
        curve={"base": 25.0, "rise": 45.0, "t_peak": 30.0, "rise_tau": 14.0, "decay_tau": 70.0},
        extra=("leak", {"FELT": "30.0", "SHOWN": "75.0", "LEAKF": "0.6"}),
        ok_line="ran the hidden-faked-expression scenario simulator")


def demo_trust_expression_gallery(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Portrait Session",
        brief="Facial landmarks for the artist and the actor: brow height, eye openness, mouth curvature.",
        scenes=[("study", 0.0), ("first sketch", 20.0), ("the sitting", 45.0)],
        curve={"base": 15.0, "rise": 70.0, "t_peak": 32.0, "rise_tau": 14.0, "decay_tau": 75.0},
        extra=("landmarks", {"I_LM": "70.0", "BY0": "10.0", "BYK": "0.06",
                             "EO0": "4.0", "EOK": "0.05", "MC0": "0.5", "MCK": "2.0"}),
        ok_line="ran the expression-gallery scenario simulator")


def demo_trust_classic_triggers(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Week of Small Seals",
        brief="Kept promises, consistency, vulnerability met with care, honesty at a cost: activation accumulates.",
        scenes=[("monday: the kept promise", 0.0), ("wednesday: consistency", 25.0),
                ("friday: vulnerability met", 50.0), ("sunday: honesty at a cost", 80.0)],
        curve={"base": 10.0, "rise": 72.0, "t_peak": 55.0, "rise_tau": 24.0, "decay_tau": 110.0},
        extra=("cascade", {"TRIGGERS": '[("kept small promise", 12.0), ("consistency across moods", 10.0), ("vulnerability met with care", 14.0), ("honesty at a cost", 18.0)]'}),
        ok_line="ran the classic-triggers scenario simulator")


def demo_trust_personal_triggers(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Old Seal",
        brief="A phrase from a once-reliable mentor resurfaces; old trust lends its balance to a new person.",
        scenes=[("the familiar phrase", 0.0), ("the memory opens", 12.0),
                ("the transfer", 28.0), ("then versus now", 48.0)],
        curve={"base": 18.0, "rise": 62.0, "t_peak": 32.0, "rise_tau": 14.0, "decay_tau": 80.0},
        extra=("transfer", {"PRIOR": "70.0", "RESEMBL": "0.8"}),
        ok_line="ran the personal-triggers scenario simulator")


def demo_trust_surprise_triggers(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Rival Warning",
        brief="Motive-free evidence: a rival warning, a wallet returned unseen, an apology unasked for.",
        scenes=[("the warning", 0.0), ("the wallet", 20.0),
                ("the apology", 40.0), ("recalibration", 60.0)],
        curve={"base": 8.0, "rise": 80.0, "t_peak": 42.0, "rise_tau": 18.0, "decay_tau": 95.0},
        extra=("motive", {"EVENTS": '[("rival warning", 25.0, 0.05), ("wallet returned unseen", 30.0, 0.0), ("apology unasked for", 20.0, 0.1)]'}),
        ok_line="ran the surprise-triggers scenario simulator")


def demo_trust_chain_reactions(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The First Domino",
        brief="One covered shift retunes the instrument; reciprocity and generalization carry the cascade.",
        scenes=[("the covered shift", 0.0), ("the retuning", 22.0),
                ("openness returned", 48.0), ("the sideways halo", 75.0),
                ("the tenth deposit", 110.0)],
        curve={"base": 12.0, "rise": 85.0, "t_peak": 70.0, "rise_tau": 30.0, "decay_tau": 140.0},
        extra=("cascade", {"TRIGGERS": '[("covered shift", 10.0), ("noticed reliability", 12.0), ("openness returned", 14.0), ("sideways halo", 16.0), ("tenth deposit", 18.0)]'}),
        ok_line="ran the chain-reaction scenario simulator")


def demo_trust_actions(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Handover",
        brief="Delegation without hovering, confession without delay: action probabilities at working trust.",
        scenes=[("the brief", 0.0), ("the handover", 18.0),
                ("no hovering", 40.0), ("delivered", 70.0)],
        curve={"base": 20.0, "rise": 72.0, "t_peak": 45.0, "rise_tau": 20.0, "decay_tau": 100.0},
        extra=("actions", {"I_ACT": "72.0",
                           "ACTS": '[("delegate the project", 1.0), ("confess the mistake early", 0.9), ("ask for help", 0.85), ("lend the valued tool", 0.95)]'}),
        ok_line="ran the trust-actions scenario simulator")


def demo_trust_speech(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Plain Conversation",
        brief="Hedging thins as trust rises; volunteered reasons and easy not-knows replace guarded padding.",
        scenes=[("careful opening", 0.0), ("hedges thinning", 15.0),
                ("reasons volunteered", 32.0), ("plain speech", 52.0)],
        curve={"base": 15.0, "rise": 68.0, "t_peak": 36.0, "rise_tau": 15.0, "decay_tau": 80.0},
        extra=("speech", {"I_SP": "68.0"}),
        ok_line="ran the trust-speech scenario simulator")


def demo_trust_decisions(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Skipped Check",
        brief="Verification spending falls as the ledger deepens; the quiet background audit keeps running.",
        scenes=[("the referral", 0.0), ("the price accepted", 20.0),
                ("the clause unread", 42.0), ("the audit, quiet", 65.0)],
        curve={"base": 25.0, "rise": 75.0, "t_peak": 45.0, "rise_tau": 20.0, "decay_tau": 100.0},
        extra=("decisions", {"I_DEC": "75.0", "VERIFY_K": "12.0"}),
        ok_line="ran the trust-decisions scenario simulator")


def demo_trust_full_intensity_behavior(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Unbreakable Seal",
        brief="Delegation total, disclosure confessional, loyalty reflexive: behavior at full intensity.",
        scenes=[("the call", 0.0), ("the drive", 25.0),
                ("the confession", 55.0), ("the standing", 95.0)],
        curve={"base": 40.0, "rise": 96.0, "t_peak": 60.0, "rise_tau": 25.0, "decay_tau": 130.0},
        extra=("stake", {"BAL": "100000.0", "I_ST": "96.0"}),
        ok_line="ran the full-intensity-behavior scenario simulator")


def demo_trust_healthy_expression(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Daylight Seal",
        brief="Said plainly, shown in measure, received as stewardship: scoring a healthy expression.",
        scenes=[("saying it", 0.0), ("showing it in measure", 20.0),
                ("received well", 42.0), ("put to work", 68.0)],
        curve={"base": 20.0, "rise": 80.0, "t_peak": 46.0, "rise_tau": 20.0, "decay_tau": 100.0},
        extra=("expressq", {"FACTORS": '[("clarity", 9.0, 3.0), ("timing", 8.0, 2.0), ("proportion", 8.0, 3.0), ("repair-openness", 9.0, 2.0)]'}),
        ok_line="ran the healthy-expression scenario simulator")


def demo_trust_unhealthy_extremes(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Two Ledgers, Both Wrong",
        brief="Blind trust stakes 90 on evidence 15; chronic distrust stakes 5 on evidence 85: calibration errors compared.",
        scenes=[("the open hand", 0.0), ("the closed fist", 25.0),
                ("the audit", 50.0)],
        curve={"base": 10.0, "rise": 50.0, "t_peak": 34.0, "rise_tau": 15.0, "decay_tau": 70.0},
        extra=("calib", {"BLIND_STAKE": "90.0", "BLIND_EVID": "15.0",
                         "DISTRUST_STAKE": "5.0", "DISTRUST_EVID": "85.0"}),
        ok_line="ran the unhealthy-extremes scenario simulator")


def demo_trust_everyday_practices(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Thirty Days of Watering",
        brief="Seven small practices, repeated daily: the compound interest of tiny seals.",
        scenes=[("day one", 0.0), ("day ten", 15.0),
                ("day twenty", 30.0), ("day thirty", 45.0)],
        curve={"base": 25.0, "rise": 78.0, "t_peak": 32.0, "rise_tau": 14.0, "decay_tau": 80.0},
        extra=("practices", {"DEPOSITS": "[3.0, 2.0, 4.0, 3.0, 2.0, 5.0, 3.0]",
                             "DAYS": "30", "DECAY": "0.995"}),
        ok_line="ran the everyday-practices scenario simulator")


def demo_trust_reading_signs(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Ensemble Reading",
        brief="Face, body, voice, behavior weighed together: cue detection scored against the truth.",
        scenes=[("first read", 0.0), ("the ensemble", 22.0),
                ("congruence check", 45.0), ("the verdict, held lightly", 70.0)],
        curve={"base": 15.0, "rise": 70.0, "t_peak": 48.0, "rise_tau": 21.0, "decay_tau": 95.0},
        extra=("cues", {"CUES": '[("eye crinkles", 1, 1), ("open torso", 1, 1), ("warm voice", 1, 0), ("kept promises", 1, 1), ("mouth-only smile", 0, 0)]'}),
        ok_line="ran the reading-signs scenario simulator")


def demo_trust_supportive_responses(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Keeper Oath",
        brief="Receiving trust as stewardship: steadiness, care, reciprocity, honesty-first, naming.",
        scenes=[("the confession", 0.0), ("steadiness", 14.0),
                ("stewardship", 30.0), ("reciprocity", 50.0),
                ("the naming", 68.0)],
        curve={"base": 30.0, "rise": 84.0, "t_peak": 46.0, "rise_tau": 20.0, "decay_tau": 100.0},
        extra=("support", {"RESPS": '[("steadiness", 9.0), ("stewardship", 9.0), ("reciprocity", 8.0), ("honesty-first", 9.0), ("naming", 8.0)]'}),
        ok_line="ran the supportive-responses scenario simulator")


def demo_trust_mistakes(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="The Same-Day Repair",
        brief="A rupture modeled twice: repaired by sundown versus left for a month; residual hurt compared.",
        scenes=[("the rupture", 0.0), ("the quick repair", 20.0),
                ("the slow repair", 45.0), ("the ledger after", 75.0)],
        curve={"base": 35.0, "rise": 60.0, "t_peak": 40.0, "rise_tau": 25.0, "decay_tau": 60.0},
        extra=("damage", {"SEV": "60.0", "REPAIR_DAY": "0.9", "REPAIR_MONTH": "0.2"}),
        ok_line="ran the trust-mistakes scenario simulator")


def demo_trust_related_emotions(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Walking the Streets",
        brief="Confidence, faith, dependence, naivety: cosine similarity to trust over appraisal features.",
        scenes=[("confidence street", 0.0), ("faith lane", 18.0),
                ("dependence row", 36.0), ("counterfeit alley", 54.0)],
        curve={"base": 20.0, "rise": 66.0, "t_peak": 38.0, "rise_tau": 17.0, "decay_tau": 85.0},
        extra=("simmatrix", {"VECS": '{"trust": [0.9, 0.8, 0.7], "confidence": [0.8, 0.3, 0.2], "faith": [0.7, 0.9, 0.4], "dependence": [0.5, 0.6, 0.9], "naivety": [0.6, 0.1, 0.9]}'}),
        ok_line="ran the related-emotions scenario simulator")


def demo_trust_mixes(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Four Alloys",
        brief="Trust alloyed with joy, fear, surprise, and anticipation: mean and synergy of each dyad.",
        scenes=[("love: the gold alloy", 0.0), ("submission: the iron alloy", 20.0),
                ("curiosity: the quicksilver alloy", 40.0), ("expectation: the steel alloy", 60.0)],
        curve={"base": 25.0, "rise": 82.0, "t_peak": 44.0, "rise_tau": 19.0, "decay_tau": 95.0},
        extra=("dyads4", {"D_T4": "70.0",
                          "PARTNERS": '[("joy (love)", 75.0), ("fear (submission)", 40.0), ("surprise (curiosity)", 55.0), ("anticipation (expectation)", 65.0)]'}),
        ok_line="ran the emotion-mixes scenario simulator")


def demo_trust_full_simulation(hdr, name, rid, group, points, req):
    return _sim(hdr, name, rid, group,
        scenario="Maya and Jon: Eighteen Months",
        brief="The showcase: meeting, first test, deepening, rupture, repair, deep bond - the running ledger throughout.",
        scenes=[("scene 1: the meeting", 0.0), ("scene 2: the first test", 40.0),
                ("scene 3: the deepening", 120.0), ("scene 4: the rupture", 220.0),
                ("scene 5: the repair", 300.0), ("scene 6: the deep bond", 420.0)],
        curve={"base": 5.0, "rise": 95.0, "t_peak": 330.0, "rise_tau": 140.0, "decay_tau": 260.0},
        extra=("runcan", {"FLOW": '[("meeting: swift trust", 12.0), ("first test: early seal", 18.0), ("deepening: cascade", 25.0), ("rupture: withdrawal", -30.0), ("repair: costly honesty", 35.0), ("deep bond: dividends", 20.0)]'}),
        ok_line="ran the full behavioral simulation")


DEMOS = {
    "trust-definition": demo_trust_definition,
    "trust-emotion-family": demo_trust_emotion_family,
    "trust-intensity-levels": demo_trust_intensity_levels,
    "trust-myths": demo_trust_myths,
    "trust-first-person": demo_trust_first_person,
    "trust-over-time": demo_trust_over_time,
    "trust-low-vs-high": demo_trust_low_vs_high,
    "trust-mixed-affection": demo_trust_mixed_affection,
    "trust-day-in-life": demo_trust_day_in_life,
    "trust-body": demo_trust_body,
    "trust-posture": demo_trust_posture,
    "trust-sleep-appetite": demo_trust_sleep_appetite,
    "trust-body-differences": demo_trust_body_differences,
    "trust-face": demo_trust_face,
    "trust-face-intensity": demo_trust_face_intensity,
    "trust-face-hidden-faked": demo_trust_face_hidden_faked,
    "trust-expression-gallery": demo_trust_expression_gallery,
    "trust-classic-triggers": demo_trust_classic_triggers,
    "trust-personal-triggers": demo_trust_personal_triggers,
    "trust-surprise-triggers": demo_trust_surprise_triggers,
    "trust-chain-reactions": demo_trust_chain_reactions,
    "trust-actions": demo_trust_actions,
    "trust-speech": demo_trust_speech,
    "trust-decisions": demo_trust_decisions,
    "trust-full-intensity-behavior": demo_trust_full_intensity_behavior,
    "trust-healthy-expression": demo_trust_healthy_expression,
    "trust-unhealthy-extremes": demo_trust_unhealthy_extremes,
    "trust-everyday-practices": demo_trust_everyday_practices,
    "trust-reading-signs": demo_trust_reading_signs,
    "trust-supportive-responses": demo_trust_supportive_responses,
    "trust-mistakes": demo_trust_mistakes,
    "trust-related-emotions": demo_trust_related_emotions,
    "trust-mixes": demo_trust_mixes,
    "trust-full-simulation": demo_trust_full_simulation,
}
