#!/usr/bin/env python3
"""Shared build machinery for the JAH Databases Unsolved Problems batch 5
(15 field pairs x 34 records, Manon's 2026-10-17 16:15 orders, unsolved batch 5).

Each field lives in code/<slug>-build/ with:
  build.py          - thin driver: FIELD + ENTRIES import, calls shared.run_pair
  entries_<tag>.py  - FIELD dict + ENTRIES (34 dicts) + LABEL + SIG_TAIL

This module provides: the fixed label-gate assembly (round8 repair pattern),
record construction mirroring unsolved-statistics, shard writes, demo
execution, page + gen-js generation, node checks, and merger fragments.

LABEL GATE (non-negotiable): every record's how_it_works OPENS with the exact
string "Signature-generated proposed solution \u2014 not established science."
(em-dash U+2014, never hyphen). Assembly:
  signature half = LABEL + " " + sig_lens + " " + why + " " + solution_body
  public half    = LABEL + " " + why + " " + pointer
Gates assert startswith on ALL records (68/68 per pair) and zero hyphenated
leftovers.

CONCURRENCY: never touches data/manifest.json, api.json, hub index.html,
README.md, or docs/AI_ACCESS.md; never commits or pushes. Writes only:
  db/<slug>/ + db/<slug>-signature/ (index.html, gen-*.js)
  shard data dirs under ~/workspace/jah-databases-data-1/data/<slug>/
  merger fragment under ~/workspace/hidden_files/missing-builds/fragments/
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGDIR = "/home/hatch/workspace/hidden_files/missing-builds/fragments"
SWEEP = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"

LABEL = "Signature-generated proposed solution \u2014 not established science."
HYPHEN_LABEL = "Signature-generated proposed solution - not established science."

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

# ---------------------------------------------------------------- demo engines
# Each engine: (hdr_fn, name, rid, group, points, req, dp) -> program string.
# Programs are deterministic, print real computed values, assert invariants
# (never float exact-equality), print CONFIRM IF / REFUTE IF panels, end OK.

def _prog(hdr, name, rid, group, imports, body, approach, confirm, refute,
          notclaim, ok_expr):
    prog = hdr(name, rid, group) + imports + "\ndef main():\n"
    for line in body:
        prog += "    " + line + "\n"
    prog += "    print(%s)\n" % json.dumps("approach: " + approach)
    prog += "    print(%s)\n" % json.dumps("CONFIRM IF: " + confirm)
    prog += "    print(%s)\n" % json.dumps("REFUTE IF: " + refute)
    prog += "    print(%s)\n" % json.dumps("does NOT claim: " + notclaim)
    prog += "    print(%s + (%s))\n" % (json.dumps("OK: " + name + " "), ok_expr)
    prog += 'if __name__ == "__main__":\n    main()\n'
    return prog


def demo_data_science(hdr, name, rid, group, points, req, dp):
    p = dp["probs"]; q = dp["qpert"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "p = %s" % p, "q = %s" % q,
        "k = len(p)",
        "H = -sum(pi * math.log2(pi) for pi in p if pi > 0)",
        "KL = sum(pi * math.log2(pi / qi) for pi, qi in zip(p, q) if pi > 0)",
        "print('outcomes: %d, entropy H(p): %.4f bits' % (k, H))",
        "print('max entropy log2(k): %.4f bits' % math.log2(k))",
        "print('KL divergence D(p||q): %.4f bits' % KL)",
        "assert 0.0 < H <= math.log2(k) + 1e-9, 'entropy must sit in (0, log2 k]'",
        "assert KL >= -1e-9, 'KL divergence is never negative'",
        "assert abs(sum(p) - 1.0) < 1e-9 and abs(sum(q) - 1.0) < 1e-9",
    ], "attach a calibrated-uncertainty monitor to every prediction; report entropy and drift, not just the point estimate",
        "monitored models show better-calibrated uncertainty on held-out regimes than unmonitored ones",
        "uncertainty proves uncalibratable even with full distributional monitoring",
        "a formal theory of interpretability - the monitor is bookkeeping, not understanding",
        '"entropy %.4f bits, KL divergence %.4f bits" % (H, KL)')


def demo_operations_research(hdr, name, rid, group, points, req, dp):
    import itertools  # noqa: F401  (authoring-time only)
    coords = dp["coords"]
    return _prog(hdr, name, rid, group, "import math, itertools\n", [
        "C = %s" % coords,
        "n = len(C)",
        "D = [[math.hypot(C[i][0]-C[j][0], C[i][1]-C[j][1]) for j in range(n)] for i in range(n)]",
        "tours = []",
        "for perm in itertools.permutations(range(1, n)):",
        "    tour = (0,) + perm",
        "    L = sum(D[tour[i]][tour[(i+1) % n]] for i in range(n))",
        "    tours.append((L, tour))",
        "best, btour = min(tours, key=lambda t: t[0])",
        "print('nodes: %d, tours enumerated: %d' % (n, len(tours)))",
        "print('optimal tour length: %.4f, tour: %s' % (best, btour))",
        "assert best > 0, 'tour length must be positive'",
        "assert all(L >= best - 1e-9 for L, _ in tours), 'best must beat every tour'",
    ], "solve the small instance exactly, then bound the large one: exact optima on tractable cores, certified gaps elsewhere",
        "certified-gap methods close real routing gaps on benchmark instances",
        "exact methods stall below useful instance sizes and gaps never certify",
        "P equals NP or a polynomial TSP algorithm - the wall stands",
        '"enumerated %d tours and certified the optimum" % len(tours)')


def demo_industrial_engineering(hdr, name, rid, group, points, req, dp):
    lam, mu = dp["lam"], dp["mu"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "lam, mu = %r, %r" % (lam, mu),
        "rho = lam / mu",
        "Lq = rho ** 2 / (1.0 - rho)",
        "Wq = Lq / lam",
        "W = Wq + 1.0 / mu",
        "L = lam * W",
        "print('arrival rate: %.2f/hr, service rate: %.2f/hr' % (lam, mu))",
        "print('utilization rho: %.4f' % rho)",
        "print('mean queue length Lq: %.4f jobs, mean wait Wq: %.4f hr' % (Lq, Wq))",
        "assert 0.0 < rho < 1.0, 'queue must be stable'",
        "assert abs(L - (Lq + rho)) < 1e-9, 'Little law must close'",
        "assert Wq > 0 and Lq > 0",
    ], "instrument the real flow first: measure arrival and service rates, then let the queueing math size the buffers",
        "measured-rate models predict real queueing delays within tolerance on the floor",
        "real flows violate the Markov assumptions so badly the math misleads",
        "that human variability is fully modelable - the residual stays human",
        '"Little law closes at L=%.4f" % L')


def demo_nuclear_engineering(hdr, name, rid, group, points, req, dp):
    hl, n0 = dp["half_life"], dp["n0"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "half, n0 = %r, %r" % (hl, n0),
        "lam = math.log(2.0) / half",
        "N = lambda t: n0 * math.exp(-lam * t)",
        "A0 = lam * n0",
        "print('half-life: %.2f (illustrative units), decay constant: %.6f' % (half, lam))",
        "print('N(half-life): %.6e, expected: %.6e' % (N(half), n0 / 2.0))",
        "print('N(2 half-lives): %.6e, expected: %.6e' % (N(2*half), n0 / 4.0))",
        "print('initial activity: %.6e decays per unit time' % A0)",
        "assert abs(N(half) / (n0/2.0) - 1.0) < 1e-9, 'one half-life must halve the inventory'",
        "assert abs(N(2*half) / (n0/4.0) - 1.0) < 1e-9, 'two half-lives must quarter it'",
        "assert N(3*half) < N(2*half) < N(half) < n0, 'decay must be monotone'",
    ], "track every neutron-economy ledger line the way decay tracks atoms: continuous bookkeeping, no batch surprises",
        "ledger-grade tracking predicts real inventory and dose-relevant quantities within tolerance",
        "real plant data defeats the bookkeeping with unmodeled loss paths",
        "exact long-horizon prediction of material behavior - uncertainty bands stay attached",
        '"inventory halved exactly at one half-life"')


def demo_petroleum_engineering(hdr, name, rid, group, points, req, dp):
    k, A, dP, mu, L = dp["k"], dp["area"], dp["dp"], dp["mu"], dp["L"]
    return _prog(hdr, name, rid, group, "", [
        "k, A, dP, mu, L = %r, %r, %r, %r, %r" % (k, A, dP, mu, L),
        "q = k * A * dP / (mu * L)",
        "q2 = k * A * (2*dP) / (mu * L)",
        "print('Darcy flow rate q: %.4f (consistent units)' % q)",
        "print('flow at doubled pressure drop: %.4f' % q2)",
        "assert q > 0, 'flow must be positive down the pressure gradient'",
        "assert abs(q2 - 2*q) < 1e-9, 'Darcy flow must scale linearly with pressure drop'",
    ], "measure the pressure field densely, then let Darcy bookkeeping allocate every barrel to a gradient",
        "dense-pressure bookkeeping matches produced volumes within tolerance on real fields",
        "heterogeneity defeats the bookkeeping at every scale tried",
        "exact reservoir foresight - the subsurface keeps secrets",
        '"Darcy linearity verified at q=%.4f" % q')


def demo_environmental_engineering(hdr, name, rid, group, points, req, dp):
    cin, cout, kk, t = dp["cin"], dp["cout"], dp["k"], dp["t"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "cin, cout = %r, %r" % (cin, cout),
        "eta = (cin - cout) / cin",
        "k, t = %r, %r" % (kk, t),
        "C = lambda c0, tt: c0 * math.exp(-k * tt)",
        "print('influent: %.1f, effluent: %.1f (concentration units)' % (cin, cout))",
        "print('removal efficiency: %.4f' % eta)",
        "print('first-order decay check C(t)/C0 at t=%.1f: %.4f' % (t, C(1.0, t)))",
        "assert 0.0 <= eta <= 1.0, 'efficiency must be a fraction'",
        "assert C(1.0, t) < C(1.0, 0.0), 'decay must reduce concentration'",
        "assert C(1.0, 2*t) < C(1.0, t), 'decay must be monotone'",
    ], "close the mass balance first: every gram in, every gram accounted - removal claimed only what the balance proves",
        "closed mass balances reproduce real plant removal within measurement tolerance",
        "unmeasured loss paths make the balance a fiction",
        "zero-discharge certainty - the balance bounds, it does not bless",
        '"mass balance closed at eta=%.4f" % eta')


def demo_hydrology(hdr, name, rid, group, points, req, dp):
    n, w, d, s = dp["n"], dp["w"], dp["d"], dp["s"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "n, w, d, s = %r, %r, %r, %r" % (n, w, d, s),
        "A = w * d",
        "P = w + 2.0 * d",
        "R = A / P",
        "Q = (1.0 / n) * A * (R ** (2.0/3.0)) * math.sqrt(s)",
        "Q_rough = (1.0 / (2*n)) * A * (R ** (2.0/3.0)) * math.sqrt(s)",
        "print('area: %.2f m^2, wetted perimeter: %.2f m, hydraulic radius: %.4f m' % (A, P, R))",
        "print('Manning discharge Q: %.4f m^3/s' % Q)",
        "print('Q at doubled roughness: %.4f m^3/s' % Q_rough)",
        "assert Q > 0, 'discharge must be positive'",
        "assert Q_rough < Q, 'rougher channel must carry less'",
        "assert abs(Q_rough - Q/2.0) < 1e-9, 'Manning Q must scale as 1/n'",
    ], "let the channel geometry speak: measure cross-sections densely, route with honest roughness bands",
        "geometry-dense routing beats sparse-gauge routing on held-out floods",
        "roughness uncertainty swallows the geometry gains",
        "exact flood foresight - bands stay attached to every forecast",
        '"Manning discharge Q=%.4f m^3/s" % Q')


def demo_atmospheric_science(hdr, name, rid, group, points, req, dp):
    t0, gam, z = dp["t0"], dp["gamma"], dp["z"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "t0, gam, z = %r, %r, %r" % (t0, gam, z),
        "T = t0 - gam * z",
        "print('surface T: %.1f K, lapse rate: %.1f K/km' % (t0, gam))",
        "print('T at %.1f km: %.2f K' % (z, T))",
        "def es(tc):",
        "    return 6.112 * math.exp(17.67 * tc / (tc + 243.5))",
        "ratio = es(16.0) / es(15.0)",
        "print('Clausius-Clapeyron moisture ratio per +1C near 15C: %.4f' % ratio)",
        "assert T < t0, 'troposphere must cool with height'",
        "assert T > 0, 'temperature must stay physical'",
        "assert 1.05 < ratio < 1.10, 'moisture must rise about seven percent per degree'",
    ], "profile the column continuously: measured lapse structure first, modeled feedbacks second",
        "profile-constrained models beat climatology on held-out soundings",
        "sub-grid moist physics defeats the profile constraint",
        "exact cloud feedback - the constraint narrows, it does not close",
        '"T=%.2f K at %.1f km" % (T, z)')


def demo_cosmology(hdr, name, rid, group, points, req, dp):
    h0, d = dp["h0"], dp["d_mpc"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "h0, d = %r, %r" % (h0, d),
        "v = h0 * d",
        "d_pc = d * 1e6",
        "mu = 5.0 * math.log10(d_pc / 10.0)",
        "print('H0: %.1f km/s/Mpc, distance: %.1f Mpc' % (h0, d))",
        "print('recession velocity: %.1f km/s' % v)",
        "print('distance modulus: %.4f mag' % mu)",
        "assert v > 0, 'expansion must recede'",
        "assert abs(v / h0 - d) < 1e-9, 'Hubble law must invert cleanly'",
        "assert mu > 0, 'modulus must be positive at cosmological distance'",
    ], "anchor every rung: local anchors first, then the ladder - each rung audited against the one below",
        "audited ladders converge the local and early-universe measures",
        "systematics hide in every rung and the audit cannot find them",
        "a final H0 value - the audit reports tension honestly",
        '"distance modulus %.4f mag" % mu')


def demo_particle_physics(hdr, name, rid, group, points, req, dp):
    e1, e2, th = dp["e1"], dp["e2"], dp["theta_deg"]
    return _prog(hdr, name, rid, group, "import math\n", [
        "e1, e2, th = %r, %r, %r" % (e1, e2, th),
        "m = math.sqrt(max(0.0, 2.0 * e1 * e2 * (1.0 - math.cos(math.radians(th)))))",
        "print('photon energies: %.2f, %.2f GeV; opening angle: %.1f deg' % (e1, e2, th))",
        "print('two-body invariant mass: %.4f GeV (c=1 units)' % m)",
        "assert m >= 0, 'invariant mass must be non-negative'",
        "assert m <= e1 + e2 + 1e-9, 'invariant mass cannot exceed total energy'",
        "assert abs(m*m - 2.0*e1*e2*(1.0-math.cos(math.radians(th)))) < 1e-6",
    ], "reconstruct before theorizing: invariant-mass bookkeeping on every event, bumps only where the ledger says",
        "ledger-grade reconstruction reproduces known resonances at their masses",
        "backgrounds fake every bump the ledger finds",
        "a new particle discovery - the ledger reports, it does not proclaim",
        '"invariant mass m=%.4f GeV" % m')


def demo_biochemistry(hdr, name, rid, group, points, req, dp):
    vmax, km, ss = dp["vmax"], dp["km"], dp["s"]
    return _prog(hdr, name, rid, group, "", [
        "vmax, km = %r, %r" % (vmax, km),
        "S = %s" % ss,
        "v = [vmax * s / (km + s) for s in S]",
        "print('Vmax: %.1f, Km: %.2f (concentration units)' % (vmax, km))",
        "for s, vv in zip(S, v):",
        "    print('  [S]=%6.2f -> v=%7.3f' % (s, vv))",
        "assert all(b >= a for a, b in zip(v, v[1:])), 'rate must rise with substrate'",
        "assert all(vv < vmax for vv in v), 'rate must stay below Vmax'",
        "i = S.index(km)",
        "assert abs(v[i] - vmax/2.0) < 1e-9, 'v(Km) must equal Vmax/2'",
    ], "titrate the mechanism: full substrate curves first, mechanistic claims only where the curve forces them",
        "curve-forced mechanisms reproduce mutant kinetics within tolerance",
        "curves underdetermine mechanism at every turn",
        "the full catalytic mechanism - the curve constrains, it does not reveal",
        '"v(Km)=Vmax/2 confirmed exactly"')


def demo_bioinformatics(hdr, name, rid, group, points, req, dp):
    seed, L = dp["seed"], dp["length"]
    return _prog(hdr, name, rid, group, "import random\n", [
        "rng = random.Random(%r)" % seed,
        "seq = ''.join(rng.choice('ACGT') for _ in range(%r))" % L,
        "gc = sum(1 for b in seq if b in 'GC') / len(seq)",
        "print('sequence length: %d' % len(seq))",
        "print('GC content: %.4f' % gc)",
        "a, b, c = seq[:60], seq[20:80], seq[40:100]",
        "def ham(x, y):",
        "    return sum(1 for p, q in zip(x, y) if p != q)",
        "dab, dbc, dac = ham(a, b), ham(b, c), ham(a, c)",
        "print('Hamming distances: d(a,b)=%d d(b,c)=%d d(a,c)=%d' % (dab, dbc, dac))",
        "assert 0.0 <= gc <= 1.0, 'GC fraction must be a fraction'",
        "assert dac <= dab + dbc, 'Hamming distance must obey the triangle inequality'",
        "assert len(seq) == %r" % L,
    ], "count before clustering: composition statistics first, homology claims only where the counts license them",
        "count-first pipelines cut false homologs on benchmark families",
        "composition bias fools the counters too",
        "true homology - the counts screen, they do not certify",
        '"GC=%.4f with valid Hamming metric" % gc')


def demo_toxicology(hdr, name, rid, group, points, req, dp):
    emax, ec50, nn, cc = dp["emax"], dp["ec50"], dp["n"], dp["c"]
    return _prog(hdr, name, rid, group, "", [
        "emax, ec50, n = %r, %r, %r" % (emax, ec50, nn),
        "C = %s" % cc,
        "E = [emax * (c ** n) / (ec50 ** n + c ** n) if c > 0 else 0.0 for c in C]",
        "print('illustrative compound X - arbitrary units, NOT a real chemical or dose')",
        "print('Emax: %.1f, EC50: %.1f, Hill n: %.2f' % (emax, ec50, n))",
        "for c, e in zip(C, E):",
        "    print('  C=%6.2f -> response=%7.3f' % (c, e))",
        "assert E[0] == 0.0, 'zero exposure must give zero response'",
        "assert all(b >= a for a, b in zip(E, E[1:])), 'response must be monotone in dose'",
        "assert all(e < emax for e in E), 'response must stay below Emax'",
        "assert E[-1] > 0.9 * emax, 'high dose must approach the ceiling'",
    ], "model the curve, never the poison: fit response shapes on reference data, predict only within the tested range",
        "curve-shape models predict held-out responses within tolerance",
        "real biology breaks every fitted curve outside its range",
        "safe exposure limits from curves alone - the curve informs, it does not permit",
        '"monotone Hill curve reaching %.1f%% of Emax" % (100*E[-1]/emax)')


def demo_cryptography(hdr, name, rid, group, points, req, dp):
    p, g, a, b = dp["p"], dp["g"], dp["a"], dp["b"]
    return _prog(hdr, name, rid, group, "", [
        "p, g, a, b = %r, %r, %r, %r" % (p, g, a, b),
        "A = pow(g, a, p)",
        "B = pow(g, b, p)",
        "s1 = pow(B, a, p)",
        "s2 = pow(A, b, p)",
        "print('toy parameters ONLY - illustrative, not real key sizes')",
        "print('prime: %d, generator: %d' % (p, g))",
        "print('public values: A=%d B=%d' % (A, B))",
        "print('shared secrets: s1=%d s2=%d' % (s1, s2))",
        "assert s1 == s2, 'both sides must derive the same secret'",
        "assert 0 < s1 < p, 'secret must be a valid residue'",
        "assert pow(g, a + b, p) == (A * B) % p, 'exponent addition must hold mod p'",
    ], "prove the arithmetic before trusting the protocol: toy-parameter checks first, real sizes only after review",
        "arithmetic-checked protocols survive independent review",
        "implementation side channels void the arithmetic proof",
        "unbreakable encryption - the math holds, the deployment decides",
        '"both sides agreed on secret %d" % s1')


def demo_control_theory(hdr, name, rid, group, points, req, dp):
    z, wn = dp["zeta"], dp["wn"]
    return _prog(hdr, name, rid, group, "import math, cmath\n", [
        "zeta, wn = %r, %r" % (z, wn),
        "disc = zeta**2 - 1.0",
        "r1 = -zeta*wn + wn*cmath.sqrt(disc)",
        "r2 = -zeta*wn - wn*cmath.sqrt(disc)",
        "Mp = math.exp(-math.pi*zeta/math.sqrt(1-zeta**2)) if zeta < 1 else 0.0",
        "print('damping ratio: %.2f, natural frequency: %.2f rad/s' % (zeta, wn))",
        "print('poles: %.4f%+.4fi, %.4f%+.4fi' % (r1.real, r1.imag, r2.real, r2.imag))",
        "print('predicted overshoot: %.4f' % Mp)",
        "assert r1.real < 0 and r2.real < 0, 'positive damping must place poles left of the axis'",
        "assert (0.0 < Mp < 1.0) if zeta < 1.0 else Mp == 0.0, 'overshoot must match damping regime'",
        "assert abs(r1.real + zeta*wn) < 1e-9, 'real part must equal -zeta*wn'",
    ], "place the poles deliberately: stability margins computed first, performance claimed only inside the margins",
        "margin-first designs hold stability on the hardware",
        "unmodeled dynamics eat the margins",
        "guaranteed performance - the margins bound, they do not bless",
        '"stable poles placed, overshoot %.4f" % Mp')

DEMO_BUILDERS = {
    "data-science": demo_data_science,
    "operations-research": demo_operations_research,
    "industrial-engineering": demo_industrial_engineering,
    "nuclear-engineering": demo_nuclear_engineering,
    "petroleum-engineering": demo_petroleum_engineering,
    "environmental-engineering": demo_environmental_engineering,
    "hydrology": demo_hydrology,
    "atmospheric-science": demo_atmospheric_science,
    "cosmology": demo_cosmology,
    "particle-physics": demo_particle_physics,
    "biochemistry": demo_biochemistry,
    "bioinformatics": demo_bioinformatics,
    "toxicology": demo_toxicology,
    "cryptography": demo_cryptography,
    "control-theory": demo_control_theory,
}

# ---------------------------------------------------------------- config

def _cfg(slug, F, source):
    sig = source == "signature"
    name = F["sig_name"] if sig else F["name"]
    tagline = F["sig_tagline"] if sig else F["tagline"]
    ai = F["ai"] + (" (Signature)" if sig else "")
    role = F["role_sig"] if sig else F["role_pub"]
    pub_line = F["pub_line"]
    sig_line = F["sig_line"]
    return {
        "name": name, "tagline": tagline, "record_kind": "unsolved problem record",
        "prefix": F["sig_prefix"] if sig else F["prefix"], "ai": ai, "role": role,
        "hero_p": ("%s - %s Every record carries the full entry: problem, background, why it matters, "
                   "key points, requirements, standards, citations, and a working solution-explorer "
                   "demonstration program.%s" % (tagline, sig_line if sig else pub_line, F["ladder_text"])),
        "sig_type": ("Signature originals organized in the Signature system" if sig
                     else "Public records organized in the Signature system"),
        "search_ph": F["search_ph"], "chat_ph": F["chat_ph"],
        "archive_blurb": ("Seeded %s unsolved %s records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if sig else "public-record", F["disp"])),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": F["gen_desc"],
        "greet": F["greet_sig"] if sig else F["greet_pub"],
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-%s-study" % F["tag"],
        "gen_demo_kind": "unsolved-%s-demo" % F["tag"],
        "source": source,
    }


def build_records(slug, source, DBCFG, ENTRIES, F, demo_builder):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        why = e["why_it_matters"]
        if sig:
            assert e["sig_solution"].startswith(LABEL), \
                "sig solution must open with exact label: %s" % name
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["problem"] + " " + e["background"])
            sol_body = e["sig_solution"][len(LABEL):].lstrip()
            how = (LABEL + " " + e["sig_lens"] + " " + why + " " + sol_body)
            citations = list(e["citations"]) + [F["sig_tail"]]
        else:
            description = e["problem"] + " " + e["background"]
            how = LABEL + " " + why + " " + e["pointer"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e.get("standards") or F["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        program = demo_builder(base._hdr, name if not sig else title, rid, e["group"],
                               e["key_points"], "; ".join(e["requirements"]), e["demo"])
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-500:])
    return True


def run_pair(F, ENTRIES, tag):
    """Full pipeline for one field pair. FIELD dict F, 34 ENTRIES, tag for demos."""
    slug_pub = "unsolved-" + F["tag"]
    slug_sig = slug_pub + "-signature"
    DBCFG = {slug_pub: _cfg(slug_pub, F, "public"),
             slug_sig: _cfg(slug_sig, F, "signature")}
    base.DBCFG = DBCFG

    assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
    for e in ENTRIES:
        assert e["sig_solution"].startswith(LABEL), "entry sig_solution label: %s" % e["key"]
        assert "'" not in e["name"], "apostrophe in entry name %s" % e["key"]
        assert HYPHEN_LABEL not in e["sig_solution"], "hyphen label in %s" % e["key"]
    demo_builder = DEMO_BUILDERS[tag]

    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sspec = importlib.util.spec_from_file_location("sweep", SWEEP)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in (slug_pub, slug_sig):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source, DBCFG, ENTRIES, F, demo_builder)

    total = 0
    label_ok = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        assert [r["ladder_rank"] for r in recs] == list(range(1, 35)), \
            "ladder ranks must be 1-34 in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced")
            # LABEL GATE: record must OPEN with the exact em-dash label; zero hyphen leftovers.
            assert r["how_it_works"].startswith(LABEL), \
                "honesty label not at record open in %s" % r["id"]
            assert HYPHEN_LABEL not in r["how_it_works"], \
                "hyphenated label leftover in %s" % r["id"]
            label_ok += 1
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            assert "'" not in r["t"], "apostrophe in title %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-42s %d records" % (slug, n), flush=True)

    print("label gate: %d/%d how_it_works open with exact label; hyphenated leftovers: 0"
          % (label_ok, total), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=300)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
            assert "CONFIRM IF:" in p.stdout and "REFUTE IF:" in p.stdout, \
                "demo missing confirm/refute panel %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    builddir = os.path.join(REPO, "code", slug_pub + "-build")
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "public-synthetic-intelligence" not in page, "slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        scripts = re.findall(r'<script(?![^>]*type="application/ld\+json")[^>]*>(.*?)</script>',
                             page, flags=re.S)
        for i, body in enumerate(scripts):
            if body.strip():
                tmp = os.path.join(builddir, "_pagescript_%d.js" % i)
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(body)
                node_check(tmp)
                os.unlink(tmp)
        topics = {}
        for r in recs:
            topics.setdefault(r["ladder_tier"].capitalize(), []).append(
                "%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        node_check(gpath)
        for k in ("role", "ai", "greet", "search_ph", "chat_ph", "gen_desc"):
            assert "'" not in DBCFG[slug][k], "apostrophe in cfg %s for %s" % (k, slug)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    def frag_entry(slug):
        c = DBCFG[slug]
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        return {
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": idx, "record_count": 34,
            "status": "live", "full_records": 34, "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if not slug.endswith("-signature") else "signature",
        }
    os.makedirs(FRAGDIR, exist_ok=True)
    fragpath = os.path.join(FRAGDIR, slug_pub + ".json")
    with open(fragpath, "w", encoding="utf-8") as f:
        json.dump({"public": frag_entry(slug_pub), "signature": frag_entry(slug_sig)},
                  f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % fragpath)
    print("NOTE: manifest/api/hub/README/docs NOT touched - merger handles registration. No commit/push done.")
    return 0
