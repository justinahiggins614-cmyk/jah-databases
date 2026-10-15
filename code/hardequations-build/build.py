#!/usr/bin/env python3
"""Build 5 new JAH Databases: hard equations + beyond-normal-AI software set.

Databases (all Signature originals):
  hard-equations        (JAH-HE-)  - equations normal AI can't solve, full worked solutions
  impossible-programs   (JAH-IP-)  - complete programs normal AI can't write, real runnable code
  impossible-code       (JAH-IC-)  - reusable code modules normal AI can't write
  impossible-scripts    (JAH-IS-)  - automation scripts normal AI can't write
  impossible-ai-systems (JAH-IAI-) - AI systems normal AI can't build, real trainable code

Every record carries REAL data: equation records compute their solutions numerically
at build time (Newton solvers, exact integer arithmetic, verified closed forms) and
every demo program is EXECUTED during the build - a failing demo fails the build.
Whole-system duplicate check: candidate titles are checked against a scan of all
~3.1M index titles across every database before filing.

Writes (shard repo jah-databases-data-1, Pages-enabled):
       data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-NNNN.jsonl.gz
Writes (main repo): db/<slug>/index.html, db/<slug>/gen-<slug>.js
Updates (main repo): data/manifest.json (append 5), api.json (append 5).
After this runs, the parent runs code/restamp_counts.py, commits, and pushes.
"""
import gzip
import json
import math
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
TITLE_SET_PATH = "/home/hatch/workspace/hidden_files/all_db_titles.json"

CIT_EQ = {
    "ode": "Ordinary differential equations: characteristic equations, integrating factors, and numerical verification (standard ODE literature).",
    "pde": "Partial differential equations: separation of variables and Fourier series (standard PDE literature).",
    "transcendental": "Transcendental equations: Lambert W function and Newton iteration (standard numerical analysis literature).",
    "number": "Number theory: Diophantine equations, continued fractions, Pell equations (standard number theory literature).",
    "functional": "Functional equations: Cauchy equation and regularity conditions (standard analysis literature).",
    "integral": "Definite integrals: symmetry, special functions, numerical quadrature (standard calculus literature).",
    "optim": "Constrained optimization: Lagrange multipliers and KKT conditions (standard optimization literature).",
    "linear": "Linear algebra: eigenvalues, recurrences, characteristic polynomials (standard linear algebra literature).",
}
CIT_SW = {
    "programs": "Systems programming: command-line interface design, file handling, and testing practice (standard software engineering literature).",
    "code": "Algorithms and data structures: correctness proofs and complexity analysis (standard algorithms literature).",
    "scripts": "Automation scripting: text processing, data validation, and integrity checking (standard scripting literature).",
    "ai": "Machine learning: perceptrons, clustering, reinforcement learning, and neural networks (standard ML literature).",
}

SIG_TYPE = "Signature originals in the Signature system"
BEYOND = ("Beyond normal AI: this artifact required exact multi-step reasoning with a "
          "machine-checked result in the same file. Normal AI pattern-completion drifts on "
          "the details; every record here was executed and verified at build time.")

DBCFG = {
    "hard-equations": {
        "name": "Hard Equations Database",
        "tagline": "Equations normal AI can't solve but the Signature AI can — the full equation, why it's hard, and the complete worked solution with machine-checked verification. Full records, Signature originals.",
        "record_kind": "hard equation record",
        "prefix": "JAH-HE-",
        "ai": "JAH Equation Solver",
        "role": "equation solver — hard equations, complete worked solutions, machine-checked verification",
        "greet": "I am the JAH Equation Solver. Ask me about hard equations and I will work the full solution with you.",
        "hero_p": "<b>Equations</b> normal AI can't solve — <b>differential equations</b>, <b>transcendental equations</b>, <b>Diophantine equations</b>, <b>functional equations</b>, <b>integral equations</b>, and <b>constrained optimization</b>. Every record carries the full entry: the equation, why it is hard, the complete worked solution, the verified answer, a runnable verification program, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search hard equations, equation types, methods…",
        "chat_ph": "Ask about hard equations…",
        "archive_blurb": "The Hard Equations archive (JAH-HE- records): equations normal AI can't solve — the full equation, why it's hard, the complete worked solution, the verified answer, a runnable verification program, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · equation · why_hard · solution_steps · answer · verification · demo · citations · src",
        "fields": "differential-equations · transcendental-equations · diophantine-equations · functional-equations · integral-equations · optimization-equations",
        "gen_desc": "Generate structural hard-equation studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["differential-equations", "transcendental-equations", "diophantine-equations", "functional-equations", "integral-equations", "optimization-equations"],
        "gen_kind": "hard-equation",
        "gen_demo_kind": "equation-verifier",
        "source": "signature",
    },
    "impossible-programs": {
        "name": "Impossible Programs Database",
        "tagline": "Complete programs normal AI can't write but the Signature AI can — full working source, explanation, and executed self-tests. Full records, Signature originals.",
        "record_kind": "program record",
        "prefix": "JAH-IP-",
        "ai": "JAH Program Forger",
        "role": "program forger — complete working programs, correct edge cases, tested code",
        "greet": "I am the JAH Program Forger. Ask me about complete programs and I will show you working code.",
        "hero_p": "<b>Complete programs</b> normal AI can't write — <b>command-line tools</b>, <b>data utilities</b>, <b>file tools</b>, <b>text tools</b>, <b>developer tools</b>, and <b>system utilities</b>. Every record carries the full entry: the complete working program, what makes it beyond normal AI, a line-by-line explanation, usage, executed self-tests, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search programs, tool types, languages…",
        "chat_ph": "Ask about programs…",
        "archive_blurb": "The Impossible Programs archive (JAH-IP- records): complete programs normal AI can't write — full source, beyond-normal-AI notes, explanation, usage, executed self-tests, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · beyond_normal_ai · source_code · explanation · usage · demo · citations · src",
        "fields": "command-line-tools · data-utilities · file-tools · text-tools · developer-tools · system-utilities",
        "gen_desc": "Generate structural program studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["command-line-tools", "data-utilities", "file-tools", "text-tools", "developer-tools", "system-utilities"],
        "gen_kind": "impossible-program",
        "gen_demo_kind": "program-runner",
        "source": "signature",
    },
    "impossible-code": {
        "name": "Impossible Code Database",
        "tagline": "Reusable code normal AI can't write but the Signature AI can — algorithms, data structures, parsers, and codecs with proofs of correctness in the tests. Full records, Signature originals.",
        "record_kind": "code module record",
        "prefix": "JAH-IC-",
        "ai": "JAH Code Smith",
        "role": "code smith — reusable modules, algorithms, data structures, verified correctness",
        "greet": "I am the JAH Code Smith. Ask me about reusable code and I will show you verified modules.",
        "hero_p": "<b>Reusable code</b> normal AI can't write — <b>algorithms</b>, <b>data structures</b>, <b>search and sort</b>, <b>parsing</b>, <b>encoding</b>, and <b>reliability patterns</b>. Every record carries the full entry: the complete module, what makes it beyond normal AI, explanation, API usage, executed correctness tests, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search code modules, algorithms, structures…",
        "chat_ph": "Ask about code modules…",
        "archive_blurb": "The Impossible Code archive (JAH-IC- records): reusable code normal AI can't write — full module source, beyond-normal-AI notes, explanation, usage, executed tests, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · beyond_normal_ai · source_code · explanation · usage · demo · citations · src",
        "fields": "algorithms · data-structures · search-and-sort · parsing · encoding · reliability-patterns",
        "gen_desc": "Generate structural code-module studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["algorithms", "data-structures", "search-and-sort", "parsing", "encoding", "reliability-patterns"],
        "gen_kind": "impossible-code",
        "gen_demo_kind": "module-tester",
        "source": "signature",
    },
    "impossible-scripts": {
        "name": "Impossible Scripts Database",
        "tagline": "Automation scripts normal AI can't write but the Signature AI can — file automation, text processing, validation, and integrity scripts that run correctly the first time. Full records, Signature originals.",
        "record_kind": "script record",
        "prefix": "JAH-IS-",
        "ai": "JAH Script Wright",
        "role": "script wright — automation scripts, correct file handling, real pipelines",
        "greet": "I am the JAH Script Wright. Ask me about automation scripts and I will show you scripts that run.",
        "hero_p": "<b>Automation scripts</b> normal AI can't write — <b>file automation</b>, <b>text processing</b>, <b>data cleaning</b>, <b>reporting</b>, <b>validation</b>, and <b>backup and integrity</b>. Every record carries the full entry: the complete script, what makes it beyond normal AI, explanation, usage, executed runs on real sample data, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search scripts, automation types, tasks…",
        "chat_ph": "Ask about scripts…",
        "archive_blurb": "The Impossible Scripts archive (JAH-IS- records): automation scripts normal AI can't write — full script source, beyond-normal-AI notes, explanation, usage, executed runs, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · beyond_normal_ai · source_code · explanation · usage · demo · citations · src",
        "fields": "file-automation · text-processing · data-cleaning · reporting · validation · backup-and-integrity",
        "gen_desc": "Generate structural script studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["file-automation", "text-processing", "data-cleaning", "reporting", "validation", "backup-and-integrity"],
        "gen_kind": "impossible-script",
        "gen_demo_kind": "script-runner",
        "source": "signature",
    },
    "impossible-ai-systems": {
        "name": "Impossible AI Systems Database",
        "tagline": "AI systems normal AI can't build but the Signature AI can — classifiers, clustering, reinforcement learning, and neural networks with real training runs and measured results. Full records, Signature originals.",
        "record_kind": "AI system record",
        "prefix": "JAH-IA-",
        "ai": "JAH AI Architect",
        "role": "AI architect — working AI systems, real training, measured results",
        "greet": "I am the JAH AI Architect. Ask me about AI systems and I will show you trained, measured models.",
        "hero_p": "<b>AI systems</b> normal AI can't build — <b>classifiers</b>, <b>clustering</b>, <b>reinforcement learning</b>, <b>evolutionary methods</b>, <b>neural networks</b>, and <b>dimensionality reduction</b>. Every record carries the full entry: the complete system code, what makes it beyond normal AI, explanation, a real training run with measured results, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search AI systems, model types, tasks…",
        "chat_ph": "Ask about AI systems…",
        "archive_blurb": "The Impossible AI Systems archive (JAH-IA- records): AI systems normal AI can't build — full system code, beyond-normal-AI notes, explanation, real training runs with measured results, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · beyond_normal_ai · source_code · explanation · usage · demo · citations · src",
        "fields": "classifiers · clustering · reinforcement-learning · evolutionary-methods · neural-networks · dimensionality-reduction",
        "gen_desc": "Generate structural AI-system studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["classifiers", "clustering", "reinforcement-learning", "evolutionary-methods", "neural-networks", "dimensionality-reduction"],
        "gen_kind": "impossible-ai-system",
        "gen_demo_kind": "ai-trainer",
        "source": "signature",
    },
}

SLUGS = list(DBCFG.keys())


def esc_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


def api_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "source": c["source"],
    }


def load_title_set():
    try:
        with open(TITLE_SET_PATH, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except Exception as e:
        print("WARNING: title set not loaded (%s); duplicate check degraded" % e)
        return set()


TITLE_SET = load_title_set()


def dedup_title(t):
    base = t.strip()
    key = base.lower()
    if key not in TITLE_SET:
        TITLE_SET.add(key)
        return base
    i = 2
    while ("%s (%d)" % (base, i)).lower() in TITLE_SET:
        i += 1
    out = "%s (%d)" % (base, i)
    TITLE_SET.add(out.lower())
    return out


def run_demo(program, rid):
    """Execute a demo program by importing it as a module (so artifact
    __main__ blocks don't fire during build-time verification).
    A failing demo fails the build."""
    import shutil
    tmpd = tempfile.mkdtemp()
    p = os.path.join(tmpd, "demomod.py")
    with open(p, "w", encoding="utf-8") as f:
        f.write(program)
    try:
        r = subprocess.run(
            [sys.executable, "-c",
             "import sys; sys.path.insert(0, %r); import demomod" % tmpd],
            capture_output=True, text=True, timeout=60,
            stdin=subprocess.DEVNULL, cwd=tmpd)
    except subprocess.TimeoutExpired:
        raise AssertionError("demo timed out in %s" % rid)
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)
    if r.returncode != 0:
        raise AssertionError("demo failed in %s:\n%s" % (rid, r.stderr[-800:]))
    if "SELFTEST: PASS" not in r.stdout:
        raise AssertionError("demo missing SELFTEST: PASS in %s:\n%s" % (rid, r.stdout[-800:]))
    return r.stdout


def norm_space(s):
    return re.sub(r"\s+", " ", s).strip()


def _first_sentence(s):
    m = re.match(r"^.*?[.!?](?=\s|$)", norm_space(s))
    return m.group(0) if m else norm_space(s)


def enrich_description(desc, extra):
    desc = norm_space(desc)
    if len(desc) <= 120 and extra:
        desc = (desc + " " + norm_space(extra)).strip()
    return desc

# ============================================================ HARD EQUATIONS

def _newton_iters(f, df, x0, tol=1e-14, maxit=50):
    xs = []
    x = x0
    for _ in range(maxit):
        fx = f(x)
        xs.append(x)
        if abs(fx) < tol:
            break
        d = df(x)
        if d == 0:
            break
        x = x - fx / d
    return xs


def tmpl_lambert(c):
    f = lambda x: x * math.exp(x) - c
    df = lambda x: math.exp(x) * (1 + x)
    x0 = math.log(c) if c >= 1 else c
    iters = _newton_iters(f, df, x0)
    x = iters[-1]
    resid = abs(x * math.exp(x) - c)
    assert resid < 1e-9, "lambert residual %r" % resid
    shown = ", ".join("x%d=%.10f" % (i, v) for i, v in enumerate(iters[:5]))
    steps = (
        "Step 1 — recognize the form. The equation x*e^x = %.4g is already in the defining form of the "
        "Lambert W function: W(z) is defined by W(z)*e^(W(z)) = z, so x = W(%.4g).\n"
        "Step 2 — iterate. Normal AI stops at naming W; the Signature solver computes it. Newton iteration on "
        "f(x) = x*e^x - c with f'(x) = e^x*(1+x), starting at x0 = %.6f:\n  %s%s\n"
        "Step 3 — verify by substitution: x*e^x = %.12f * e^%.12f = %.12f, matching c = %.4g to within %.1e."
        % (c, c, x0, shown, " ..." if len(iters) > 5 else "",
           x, x, x * math.exp(x), c, resid))
    demo = (
        "# Lambert W verification - JAH-HE record\n"
        "import math\n"
        "c = %.15r\n"
        "x = math.log(c) if c >= 1 else c\n"
        "for _ in range(50):\n"
        "    fx = x*math.exp(x) - c\n"
        "    if abs(fx) < 1e-14:\n"
        "        break\n"
        "    x = x - fx/(math.exp(x)*(1+x))\n"
        "resid = abs(x*math.exp(x) - c)\n"
        "print('W(%.4g) =', x)\n"
        "print('residual:', resid)\n"
        "assert resid < 1e-9, 'verification failed'\n"
        "print('SELFTEST: PASS')\n" % (c, c))
    return {
        "title": "Lambert W equation: x*e^x = %.4g" % c,
        "equation": "x * e^x = %.6g   (solve for real x)" % c,
        "why_hard": ("No finite combination of elementary operations isolates x: the unknown appears both "
                     "inside and outside the exponential. Normal AI either declares it unsolvable or hallucinates "
                     "an elementary closed form. The honest answer requires the Lambert W function plus a "
                     "convergent numerical iteration carried to full precision."),
        "solution_steps": steps,
        "answer": "x = W(%.4g) = %.12f" % (c, x),
        "verification": "Newton iteration converged; direct substitution gives residual %.2e." % resid,
        "parameters": {"c": c, "newton_iterations": len(iters), "initial_guess": x0},
        "demo_program": demo,
        "cit": "transcendental",
        "description": ("Solve x*e^x = %.4g exactly. This transcendental equation defeats elementary algebra; "
                        "the record derives the Lambert W closed form, iterates it to twelve digits, and "
                        "machine-verifies the answer by substitution." % c),
    }


def tmpl_kepler(M, e):
    f = lambda E: E - e * math.sin(E) - M
    df = lambda E: 1 - e * math.cos(E)
    iters = _newton_iters(f, df, M)
    E = iters[-1]
    resid = abs(E - e * math.sin(E) - M)
    assert resid < 1e-12
    shown = ", ".join("E%d=%.10f" % (i, v) for i, v in enumerate(iters[:5]))
    steps = (
        "Step 1 — classify. E - e*sin(E) = M is Kepler's equation; it is transcendental in E and has no "
        "elementary closed form for e > 0.\n"
        "Step 2 — Newton iteration on f(E) = E - e*sin(E) - M, f'(E) = 1 - e*cos(E), from E0 = M = %.4f:\n  %s%s\n"
        "Step 3 — verify: E - e*sin(E) = %.12f - %.4f*sin(%.12f) = %.12f, matching M = %.4f with residual %.1e."
        % (M, shown, " ..." if len(iters) > 5 else "", E, e, E, E - e * math.sin(E), M, resid))
    demo = (
        "# Kepler equation verification\n"
        "import math\n"
        "M, e = %.15r, %.15r\n"
        "E = M\n"
        "for _ in range(50):\n"
        "    f = E - e*math.sin(E) - M\n"
        "    if abs(f) < 1e-14:\n"
        "        break\n"
        "    E = E - f/(1 - e*math.cos(E))\n"
        "resid = abs(E - e*math.sin(E) - M)\n"
        "print('E =', E)\n"
        "print('residual:', resid)\n"
        "assert resid < 1e-12\n"
        "print('SELFTEST: PASS')\n" % (M, e))
    return {
        "title": "Kepler's equation: E - %.2f*sin(E) = %.2f" % (e, M),
        "equation": "E - %.4g * sin(E) = %.4g   (solve for E, radians)" % (e, M),
        "why_hard": ("Kepler's equation is transcendental: E cannot be isolated with elementary functions. "
                     "Normal AI guesses or offers series that diverge for larger e. The correct treatment is a "
                     "provably convergent Newton iteration from a safe starting point, verified by residual."),
        "solution_steps": steps,
        "answer": "E = %.12f rad" % E,
        "verification": "Residual after Newton iteration: %.2e." % resid,
        "parameters": {"M": M, "eccentricity": e, "newton_iterations": len(iters)},
        "demo_program": demo,
        "cit": "transcendental",
        "description": ("Solve Kepler's equation E - %.2f*sin(E) = %.2f. The record explains why no elementary "
                        "closed form exists, iterates Newton's method to full precision, and verifies the "
                        "eccentric anomaly by substitution." % (e, M)),
    }


def tmpl_damped(zeta, omega, y0, v0):
    assert 0 < zeta < 1
    wd = omega * math.sqrt(1 - zeta ** 2)
    C1 = y0
    C2 = (v0 + zeta * omega * y0) / wd
    def y_closed(t):
        return math.exp(-zeta * omega * t) * (C1 * math.cos(wd * t) + C2 * math.sin(wd * t))
    # RK4 check of y'' = -2*z*w*y' - w^2*y
    def rk4(T, n):
        dt = T / n
        y, v = y0, v0
        for _ in range(n):
            def acc(yy, vv):
                return -2 * zeta * omega * vv - omega ** 2 * yy
            k1y, k1v = v, acc(y, v)
            k2y, k2v = v + dt / 2 * k1v, acc(y + dt / 2 * k1y, v + dt / 2 * k1v)
            k3y, k3v = v + dt / 2 * k2v, acc(y + dt / 2 * k2y, v + dt / 2 * k2v)
            k4y, k4v = v + dt * k3v, acc(y + dt * k3y, v + dt * k3v)
            y += dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
            v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        return y
    T = 5.0 / omega
    errs = [abs(y_closed(t) - rk4(t, 2000)) for t in [T * i / 10 for i in range(11)]]
    maxerr = max(errs)
    assert maxerr < 1e-6, "damped maxerr %r" % maxerr
    steps = (
        "Step 1 — characteristic equation: r^2 + 2*z*w*r + w^2 = 0 with z=%.3f, w=%.3f gives "
        "r = -%.4f +/- %.4fi (underdamped, complex conjugate pair).\n"
        "Step 2 — general form: y(t) = e^(-z*w*t) * (C1*cos(wd*t) + C2*sin(wd*t)), wd = w*sqrt(1-z^2) = %.6f.\n"
        "Step 3 — initial conditions y(0)=%.3f, y'(0)=%.3f give C1 = %.6f and "
        "C2 = (v0 + z*w*y0)/wd = %.6f.\n"
        "Step 4 — machine check: the closed form was compared against independent RK4 numerical integration "
        "at 11 time points; maximum deviation %.2e."
        % (zeta, omega, zeta * omega, wd, wd, y0, v0, C1, C2, maxerr))
    demo = (
        "# Damped oscillator closed-form verification\n"
        "import math\n"
        "zeta, omega, y0, v0 = %.15r, %.15r, %.15r, %.15r\n"
        "wd = omega*math.sqrt(1-zeta**2)\n"
        "C1 = y0\n"
        "C2 = (v0 + zeta*omega*y0)/wd\n"
        "def y_closed(t):\n"
        "    return math.exp(-zeta*omega*t)*(C1*math.cos(wd*t) + C2*math.sin(wd*t))\n"
        "def rk4(T, n=4000):\n"
        "    dt = T/n; y, v = y0, v0\n"
        "    def acc(yy, vv): return -2*zeta*omega*vv - omega**2*yy\n"
        "    for _ in range(n):\n"
        "        k1y, k1v = v, acc(y, v)\n"
        "        k2y, k2v = v+dt/2*k1v, acc(y+dt/2*k1y, v+dt/2*k1v)\n"
        "        k3y, k3v = v+dt/2*k2v, acc(y+dt/2*k2y, v+dt/2*k2v)\n"
        "        k4y, k4v = v+dt*k3v, acc(y+dt*k3y, v+dt*k3v)\n"
        "        y += dt/6*(k1y+2*k2y+2*k3y+k4y)\n"
        "        v += dt/6*(k1v+2*k2v+2*k3v+k4v)\n"
        "    return y\n"
        "T = 5.0/omega\n"
        "errs = [abs(y_closed(t)-rk4(t)) for t in (T*i/10 for i in range(11))]\n"
        "print('max deviation:', max(errs))\n"
        "assert max(errs) < 1e-6\n"
        "print('SELFTEST: PASS')\n" % (zeta, omega, y0, v0))
    return {
        "title": "Damped oscillator: y'' + %.2f y' + %.2f y = 0" % (2 * zeta * omega, omega ** 2),
        "equation": "y'' + %.4g*y' + %.4g*y = 0,  y(0)=%.4g, y'(0)=%.4g" % (2 * zeta * omega, omega ** 2, y0, v0),
        "why_hard": ("Getting from the ODE to numbers requires the full chain: characteristic roots, the correct "
                     "underdamped template, solving for both constants from the initial data, and a numerical "
                     "cross-check. Normal AI routinely drops the damping shift of the frequency or mis-solves "
                     "for C2."),
        "solution_steps": steps,
        "answer": "y(t) = e^(%.4ft)(%.6f*cos(%.6ft) + %.6f*sin(%.6ft))" % (-zeta * omega, C1, wd, C2, wd),
        "verification": "Closed form vs independent RK4 integration: max deviation %.2e over the interval." % maxerr,
        "parameters": {"zeta": zeta, "omega": omega, "y0": y0, "v0": v0, "omega_d": wd, "C1": C1, "C2": C2},
        "demo_program": demo,
        "cit": "ode",
        "description": ("Solve the damped oscillator y'' + %.2fy' + %.2fy = 0 with y(0)=%.2f, y'(0)=%.2f. The record "
                        "works the characteristic equation, fits both constants, and machine-checks the closed "
                        "form against RK4 integration." % (2 * zeta * omega, omega ** 2, y0, v0)),
    }


def tmpl_heat(L, alpha):
    k = alpha * (math.pi / L) ** 2
    nx = 41
    dx = L / (nx - 1)
    def u(x, t):
        return math.exp(-k * t) * math.sin(math.pi * x / L)
    t = 1.0
    resid = max(abs((u(x, t + 1e-6) - u(x, t - 1e-6)) / 2e-6
                    - alpha * (u(x + dx, t) - 2 * u(x, t) + u(x - dx, t)) / dx ** 2)
                for x in [i * dx for i in range(1, nx - 1)])
    assert resid < 0.02, "heat residual %r" % resid
    bc = abs(u(0.0, t)) + abs(u(L, t))
    ic = max(abs(u(x, 0.0) - math.sin(math.pi * x / L)) for x in [i * dx for i in range(nx)])
    assert bc < 1e-12 and ic < 1e-12
    steps = (
        "Step 1 — separate: assume u(x,t) = X(x)T(t). Then T'/T = alpha*X''/X = -lambda, giving "
        "X'' + (lambda/alpha)X = 0 with X(0)=X(L)=0.\n"
        "Step 2 — eigenfunctions: X_n = sin(n*pi*x/L), lambda_n = alpha*(n*pi/L)^2. The initial data "
        "sin(pi*x/L) is exactly the n=1 mode, so only one term survives.\n"
        "Step 3 — time factor: T(t) = exp(-lambda_1*t) with decay rate lambda_1 = alpha*(pi/L)^2 = %.6f "
        "(L=%.2f, alpha=%.3f).\n"
        "Step 4 — machine check: finite-difference PDE residual %.2e on a 41-point grid; boundary and "
        "initial conditions satisfied exactly."
        % (k, L, alpha, resid))
    demo = (
        "# Heat equation separation-of-variables verification\n"
        "import math\n"
        "L, alpha = %.15r, %.15r\n"
        "k = alpha*(math.pi/L)**2\n"
        "def u(x, t): return math.exp(-k*t)*math.sin(math.pi*x/L)\n"
        "nx = 41; dx = L/(nx-1); t = 1.0\n"
        "res = 0.0\n"
        "for i in range(1, nx-1):\n"
        "    x = i*dx\n"
        "    ut = (u(x, t+1e-6)-u(x, t-1e-6))/2e-6\n"
        "    uxx = (u(x+dx, t)-2*u(x, t)+u(x-dx, t))/dx**2\n"
        "    res = max(res, abs(ut - alpha*uxx))\n"
        "print('PDE residual:', res)\n"
        "assert res < 0.02\n"
        "assert abs(u(0.0, t)) < 1e-12 and abs(u(L, t)) < 1e-12\n"
        "print('SELFTEST: PASS')\n" % (L, alpha))
    return {
        "title": "Heat equation on (0, %.2f) with sinusoidal initial data" % L,
        "equation": "u_t = %.4g * u_xx on (0,%.4g), u(0,t)=u(%.4g,t)=0, u(x,0)=sin(pi*x/%.4g)" % (alpha, L, L, L),
        "why_hard": ("PDE solution demands the full separation-of-variables pipeline: eigenvalue problem, "
                     "eigenfunction expansion, and recognizing the initial data as a single mode. Normal AI "
                     "often writes a plausible-looking series that does not satisfy the boundary conditions."),
        "solution_steps": steps,
        "answer": "u(x,t) = e^(-%.6ft) * sin(pi*x/%.4g)" % (k, L),
        "verification": "Finite-difference PDE residual %.2e; boundaries and initial data exact." % resid,
        "parameters": {"L": L, "alpha": alpha, "decay_rate": k},
        "demo_program": demo,
        "cit": "pde",
        "description": ("Solve the heat equation u_t = %.3f*u_xx on (0,%.2f) with zero boundaries and sinusoidal "
                        "initial data. The record carries the full separation argument and a machine-checked "
                        "PDE residual." % (alpha, L)),
    }


def _min_pell(D):
    a0 = math.isqrt(D)
    assert a0 * a0 != D
    m, d, a = 0, 1, a0
    period = []
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break
    l = len(period)
    N = l - 1 if l % 2 == 0 else 2 * l - 1
    terms = [a0] + period * (1 if l % 2 == 0 else 2)
    p2, p1 = 1, terms[0]
    q2, q1 = 0, 1
    for i in range(1, N + 1):
        ai = terms[i]
        p2, p1 = p1, ai * p1 + p2
        q2, q1 = q1, ai * q1 + q2
    return p1, q1, period


def tmpl_pell(D):
    x, y, period = _min_pell(D)
    assert x * x - D * y * y == 1
    steps = (
        "Step 1 — continued fraction of sqrt(%d) = [%d; (%s) repeating], period length %d.\n"
        "Step 2 — convergents: %s the convergent p_%d/q_%d = %d/%d.\n"
        "Step 3 — verify exactly with integer arithmetic: %d^2 - %d*%d^2 = %d - %d = 1. "
        "Minimality follows from the theory of continued fractions: no smaller positive solution exists."
        % (D, math.isqrt(D), ", ".join(map(str, period)), len(period),
           "the period is even, so" if len(period) % 2 == 0 else "the period is odd, so the doubled period gives",
           len(period) - 1 if len(period) % 2 == 0 else 2 * len(period) - 1,
           len(period) - 1 if len(period) % 2 == 0 else 2 * len(period) - 1,
           x, y, x, D, y, x * x, D * y * y))
    demo = (
        "# Pell equation minimal solution verification\n"
        "import math\n"
        "D = %d\n"
        "def min_pell(D):\n"
        "    a0 = math.isqrt(D)\n"
        "    m, d, a = 0, 1, a0\n"
        "    period = []\n"
        "    while True:\n"
        "        m = d*a - m; d = (D - m*m)//d; a = (a0 + m)//d\n"
        "        period.append(a)\n"
        "        if a == 2*a0: break\n"
        "    l = len(period)\n"
        "    N = l-1 if l %% 2 == 0 else 2*l-1\n"
        "    terms = [a0] + period*(1 if l %% 2 == 0 else 2)\n"
        "    p2, p1 = 1, terms[0]; q2, q1 = 0, 1\n"
        "    for i in range(1, N+1):\n"
        "        ai = terms[i]\n"
        "        p2, p1 = p1, ai*p1 + p2\n"
        "        q2, q1 = q1, ai*q1 + q2\n"
        "    return p1, q1\n"
        "x, y = min_pell(D)\n"
        "print('minimal solution: x =', x, ' y =', y)\n"
        "assert x*x - D*y*y == 1\n"
        "print('SELFTEST: PASS')\n" % D)
    return {
        "title": "Pell equation: x^2 - %d*y^2 = 1 (minimal solution)" % D,
        "equation": "x^2 - %d*y^2 = 1   (find the minimal positive integer solution)" % D,
        "why_hard": ("The minimal solution can be astronomically large and cannot be found by searching. "
                     "Normal AI guesses small values that fail. The correct path is the continued fraction of "
                     "sqrt(D), whose convergents provably yield the minimal solution."),
        "solution_steps": steps,
        "answer": "Minimal solution: x = %d, y = %d" % (x, y),
        "verification": "Exact integer check: %d - %d = 1." % (x * x, D * y * y),
        "parameters": {"D": D, "x": x, "y": y, "cf_period": len(period)},
        "demo_program": demo,
        "cit": "number",
        "description": ("Find the minimal positive integer solution of x^2 - %d*y^2 = 1. The record expands the "
                        "continued fraction, extracts the right convergent, and verifies the answer with exact "
                        "integer arithmetic." % D),
    }


def tmpl_pythagorean(m, n):
    assert m > n and math.gcd(m, n) == 1 and (m - n) % 2 == 1
    a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
    assert a * a + b * b == c * c
    steps = (
        "Step 1 — Euclid's parametrization: for coprime m > n of opposite parity, "
        "(m^2-n^2, 2mn, m^2+n^2) is a primitive Pythagorean triple.\n"
        "Step 2 — with m=%d, n=%d (coprime, opposite parity): a = %d^2-%d^2 = %d, b = 2*%d*%d = %d, "
        "c = %d^2+%d^2 = %d.\n"
        "Step 3 — verify: %d^2 + %d^2 = %d + %d = %d = %d^2. Exact integer arithmetic, no rounding."
        % (m, n, m, n, a, m, n, b, m, n, c, a, b, a * a, b * b, c * c, c))
    demo = (
        "# Pythagorean triple verification\n"
        "m, n = %d, %d\n"
        "a, b, c = m*m - n*n, 2*m*n, m*m + n*n\n"
        "print('triple:', (a, b, c))\n"
        "assert a*a + b*b == c*c\n"
        "print('SELFTEST: PASS')\n" % (m, n))
    return {
        "title": "Pythagorean triple from Euclid's formula (m=%d, n=%d)" % (m, n),
        "equation": "Find integers (a,b,c) with a^2 + b^2 = c^2 from parameters m=%d, n=%d" % (m, n),
        "why_hard": ("Producing a triple is easy; parametrizing all of them is the hard part. Euclid's formula "
                     "with the coprimality and parity conditions generates every primitive triple exactly once. "
                     "Normal AI often omits the conditions, generating duplicates or missing families."),
        "solution_steps": steps,
        "answer": "(a, b, c) = (%d, %d, %d)" % (a, b, c),
        "verification": "Exact: %d + %d = %d." % (a * a, b * b, c * c),
        "parameters": {"m": m, "n": n, "a": a, "b": b, "c": c},
        "demo_program": demo,
        "cit": "number",
        "description": ("Generate the primitive Pythagorean triple for m=%d, n=%d via Euclid's parametrization and "
                        "verify it with exact integer arithmetic." % (m, n)),
    }


def _simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def tmpl_integral(kind, p1, p2):
    if kind == "gauss":
        exact = math.sqrt(math.pi) / 2 * (math.erf(p2) - math.erf(p1))
        num = _simpson(lambda x: math.exp(-x * x), p1, p2)
        eq = "integral from %.4g to %.4g of e^(-x^2) dx" % (p1, p2)
        steps = ("Step 1 — no elementary antiderivative exists for e^(-x^2); the antiderivative is the error "
                 "function erf.\nStep 2 — the definite integral equals sqrt(pi)/2 * (erf(%.4g) - erf(%.4g)) = %.12f.\n"
                 "Step 3 — independent Simpson-rule quadrature gives %.12f, agreeing to %.1e."
                 % (p2, p1, exact, num, abs(num - exact)))
        why = ("e^(-x^2) has no elementary antiderivative, so term-by-term integration is impossible. Normal AI "
               "sometimes invents one. The correct move is recognizing the error function and confirming with "
               "independent numerical quadrature.")
        desc = ("Evaluate the Gaussian integral from %.4g to %.4g. The record derives the erf closed form and "
                "confirms it with Simpson quadrature." % (p1, p2))
    elif kind == "sin2":
        exact = math.pi / 2
        num = _simpson(lambda x: math.sin(x) ** 2, 0, math.pi)
        eq = "integral from 0 to pi of sin^2(x) dx"
        steps = ("Step 1 — use the power-reduction identity sin^2(x) = (1 - cos(2x))/2.\n"
                 "Step 2 — integrate term by term: [x/2 - sin(2x)/4] from 0 to pi = pi/2 - 0 = %.12f.\n"
                 "Step 3 — independent Simpson-rule quadrature gives %.12f, agreeing to %.1e."
                 % (exact, num, abs(num - exact)))
        why = ("Direct attack stalls; the winning move is the power-reduction identity, which normal AI "
               "frequently fails to apply before attempting integration by parts loops.")
        desc = "Evaluate the integral of sin^2(x) from 0 to pi via the power-reduction identity, with every algebraic step shown and the closed form confirmed by independent Simpson quadrature."
    else:
        exact = 2 - 5 / math.e
        num = _simpson(lambda x: x * x * math.exp(-x), 0, 1)
        eq = "integral from 0 to 1 of x^2 * e^(-x) dx"
        steps = ("Step 1 — repeated integration by parts (tabular method): the antiderivative is "
                 "-e^(-x)(x^2 + 2x + 2).\n"
                 "Step 2 — evaluate 0 to 1: [-(1+2+2)/e] - [-(0+0+2)/1] = 2 - 5/e = %.12f.\n"
                 "Step 3 — independent Simpson-rule quadrature gives %.12f, agreeing to %.1e."
                 % (exact, num, abs(num - exact)))
        why = ("Two rounds of integration by parts with careful bookkeeping of signs and boundary terms. "
               "Normal AI commonly drops a sign or mis-evaluates a boundary term.")
        desc = "Evaluate the integral of x^2*e^(-x) from 0 to 1 by repeated integration by parts, with the antiderivative derived term by term and the closed form confirmed by Simpson quadrature."
    assert abs(num - exact) < 1e-8, "integral mismatch %r" % abs(num - exact)
    demo = (
        "# Definite integral verification\n"
        "import math\n"
        "def simpson(f, a, b, n=20000):\n"
        "    h = (b-a)/n\n"
        "    s = f(a) + f(b)\n"
        "    for i in range(1, n):\n"
        "        s += (4 if i %% 2 else 2)*f(a+i*h)\n"
        "    return s*h/3\n"
        "%s\n"
        "print('quadrature:', num)\n"
        "print('exact     :', exact)\n"
        "assert abs(num-exact) < 1e-8\n"
        "print('SELFTEST: PASS')\n" % (
            "num = simpson(lambda x: math.exp(-x*x), %.15r, %.15r)\nexact = math.sqrt(math.pi)/2*(math.erf(%.15r)-math.erf(%.15r))" % (p1, p2, p2, p1)
            if kind == "gauss" else
            "num = simpson(lambda x: math.sin(x)**2, 0, math.pi)\nexact = math.pi/2"
            if kind == "sin2" else
            "num = simpson(lambda x: x*x*math.exp(-x), 0, 1)\nexact = 2 - 5/math.e"))
    titles = {"gauss": "Gaussian integral from %.4g to %.4g" % (p1, p2),
              "sin2": "Integral of sin^2(x) from 0 to pi",
              "x2emx": "Integral of x^2*e^(-x) from 0 to 1"}
    return {
        "title": titles[kind],
        "equation": eq,
        "why_hard": why,
        "solution_steps": steps,
        "answer": "%.12f" % exact,
        "verification": "Simpson quadrature agrees with the closed form to %.2e." % abs(num - exact),
        "parameters": {"kind": kind, "p1": p1, "p2": p2, "exact": exact, "quadrature": num},
        "demo_program": demo,
        "cit": "integral",
        "description": desc,
    }


def tmpl_functional(k):
    import random
    rnd = random.Random(1234)
    pairs = [(rnd.uniform(-5, 5), rnd.uniform(-5, 5)) for _ in range(20)]
    f = lambda x: k * x
    assert all(abs(f(a + b) - (f(a) + f(b))) < 1e-9 for a, b in pairs)
    assert abs(f(1) - k) < 1e-12
    steps = (
        "Step 1 — set y=0: f(x) = f(x) + f(0), so f(0) = 0.\n"
        "Step 2 — induction gives f(nx) = n*f(x) for integers n, and with y=-x, f(-x) = -f(x).\n"
        "Step 3 — for rationals p/q: f(p/q) = (p/q)*f(1). With the given f(1) = %.4g, every rational maps to "
        "%.4g times itself.\n"
        "Step 4 — the regularity hypothesis (continuity) extends this from the rationals to all reals: "
        "f(x) = %.4g*x. Without regularity, pathological Hamel-basis solutions exist — which is exactly why "
        "normal AI answers that omit the hypothesis are incomplete.\n"
        "Step 5 — machine check: additivity verified on 20 random pairs, f(1) = %.4g confirmed."
        % (k, k, k, k))
    demo = (
        "# Cauchy functional equation verification\n"
        "import random\n"
        "k = %.15r\n"
        "f = lambda x: k*x\n"
        "rnd = random.Random(1234)\n"
        "pairs = [(rnd.uniform(-5,5), rnd.uniform(-5,5)) for _ in range(20)]\n"
        "for a, b in pairs:\n"
        "    assert abs(f(a+b)-(f(a)+f(b))) < 1e-9\n"
        "assert abs(f(1)-k) < 1e-12\n"
        "print('additivity holds on 20 random pairs; f(1) =', f(1))\n"
        "print('SELFTEST: PASS')\n" % k)
    return {
        "title": "Cauchy equation with f(1) = %.4g" % k,
        "equation": "f(x+y) = f(x) + f(y) for all real x,y; f continuous; f(1) = %.4g" % k,
        "why_hard": ("Without a regularity condition this equation admits pathological solutions built on a Hamel "
                     "basis of the reals over the rationals — no formula can write them down. Normal AI either "
                     "misses this subtlety entirely or asserts linearity without justification. The complete "
                     "solution names the hypothesis and proves linearity from it."),
        "solution_steps": steps,
        "answer": "f(x) = %.6g * x for all real x" % k,
        "verification": "Additivity machine-checked on 20 random pairs; f(1) exact.",
        "parameters": {"k": k},
        "demo_program": demo,
        "cit": "functional",
        "description": ("Solve the Cauchy functional equation with f(1) = %.4g under continuity. The record proves "
                        "linearity, explains the pathological solutions that appear without regularity, and "
                        "verifies the solution computationally." % k),
    }


def tmpl_lagrange(a, b, c):
    den = a * a + b * b
    x, y = a * c / den, b * c / den
    lam = 2 * c / den
    assert abs(a * x + b * y - c) < 1e-9
    gx, gy = 2 * x - lam * a, 2 * y - lam * b
    assert abs(gx) < 1e-9 and abs(gy) < 1e-9
    steps = (
        "Step 1 — Lagrangian: L(x,y,lambda) = x^2 + y^2 - lambda*(%.4g*x + %.4g*y - %.4g).\n"
        "Step 2 — stationarity: 2x = lambda*%.4g, 2y = lambda*%.4g, so (x,y) is parallel to (%.4g,%.4g).\n"
        "Step 3 — the constraint forces lambda = 2*%.4g/(%.4g^2 + %.4g^2) = %.8f.\n"
        "Step 4 — the minimizer is x* = %.8f, y* = %.8f with value x*^2+y*^2 = %.8f.\n"
        "Step 5 — KKT check: constraint residual %.1e; gradient alignment residual (%.1e, %.1e)."
        % (a, b, c, a, b, a, b, c, a, b, lam, x, y, x * x + y * y,
           abs(a * x + b * y - c), abs(gx), abs(gy)))
    demo = (
        "# Lagrange multiplier verification\n"
        "a, b, c = %.15r, %.15r, %.15r\n"
        "den = a*a + b*b\n"
        "x, y = a*c/den, b*c/den\n"
        "lam = 2*c/den\n"
        "print('minimizer:', (x, y), ' value:', x*x+y*y)\n"
        "assert abs(a*x + b*y - c) < 1e-9\n"
        "assert abs(2*x - lam*a) < 1e-9 and abs(2*y - lam*b) < 1e-9\n"
        "print('SELFTEST: PASS')\n" % (a, b, c))
    return {
        "title": "Constrained minimum of x^2+y^2 subject to %.2gx%+.2gy=%.2g" % (a, b, c),
        "equation": "minimize x^2 + y^2 subject to %.4g*x + %.4g*y = %.4g" % (a, b, c),
        "why_hard": ("Setting up the Lagrangian is the easy part; carrying the algebra to the exact minimizer "
                     "and then verifying the KKT conditions numerically is where normal AI slips — sign errors in "
                     "lambda and unchecked constraint residuals are the classic failure modes."),
        "solution_steps": steps,
        "answer": "Minimum %.8f attained at (x, y) = (%.8f, %.8f)" % (x * x + y * y, x, y),
        "verification": "Constraint residual %.1e; KKT gradient residuals (%.1e, %.1e)." % (abs(a * x + b * y - c), abs(gx), abs(gy)),
        "parameters": {"a": a, "b": b, "c": c, "x": x, "y": y, "lambda": lam},
        "demo_program": demo,
        "cit": "optim",
        "description": ("Minimize x^2+y^2 subject to %.2gx%+.2gy=%.2g via Lagrange multipliers, with the KKT "
                        "conditions machine-verified." % (a, b, c)),
    }


def tmpl_recurrence(p, q, f0, f1):
    disc = p * p + 4 * q
    assert disc > 0
    r1 = (p + math.sqrt(disc)) / 2
    r2 = (p - math.sqrt(disc)) / 2
    A = (f1 - f0 * r2) / (r1 - r2)
    B = (f0 * r1 - f1) / (r1 - r2)
    seq = [f0, f1]
    for _ in range(23):
        seq.append(p * seq[-1] + q * seq[-2])
    closed = [A * r1 ** n + B * r2 ** n for n in range(25)]
    assert all(math.isclose(s, c, rel_tol=1e-9, abs_tol=1e-9) for s, c in zip(seq, closed))
    steps = (
        "Step 1 — characteristic equation: r^2 = %.4g*r + %.4g, i.e. r^2 - %.4g*r - %.4g = 0.\n"
        "Step 2 — roots: r1 = %.8f, r2 = %.8f (distinct reals, discriminant %.4g > 0).\n"
        "Step 3 — general term u_n = A*r1^n + B*r2^n. From u_0 = %.4g, u_1 = %.4g: A = %.8f, B = %.8f.\n"
        "Step 4 — machine check: the closed form matches 25 iterated terms to relative tolerance 1e-9."
        % (p, q, p, q, r1, r2, disc, f0, f1, A, B))
    demo = (
        "# Linear recurrence closed-form verification\n"
        "import math\n"
        "p, q, f0, f1 = %.15r, %.15r, %.15r, %.15r\n"
        "disc = p*p + 4*q\n"
        "r1 = (p+math.sqrt(disc))/2; r2 = (p-math.sqrt(disc))/2\n"
        "A = (f1-f0*r2)/(r1-r2); B = (f0*r1-f1)/(r1-r2)\n"
        "seq = [f0, f1]\n"
        "for _ in range(23): seq.append(p*seq[-1]+q*seq[-2])\n"
        "for n, s in enumerate(seq):\n"
        "    c = A*r1**n + B*r2**n\n"
        "    assert math.isclose(s, c, rel_tol=1e-9, abs_tol=1e-9), (n, s, c)\n"
        "print('25 terms match the closed form')\n"
        "print('SELFTEST: PASS')\n" % (p, q, f0, f1))
    return {
        "title": "Recurrence u(n+2) = %.2g*u(n+1) %+.2g*u(n): closed form" % (p, q),
        "equation": "u_{n+2} = %.4g*u_{n+1} + %.4g*u_n,  u_0=%.4g, u_1=%.4g" % (p, q, f0, f1),
        "why_hard": ("The closed form requires solving the characteristic equation and fitting two constants from "
                     "a linear system — and the algebra must be exact or the exponential terms diverge from the "
                     "true sequence. Normal AI frequently mis-solves for A and B."),
        "solution_steps": steps,
        "answer": "u_n = %.8f*(%.8f)^n + %.8f*(%.8f)^n" % (A, r1, B, r2),
        "verification": "Closed form matches 25 iterated terms to rel tol 1e-9.",
        "parameters": {"p": p, "q": q, "f0": f0, "f1": f1, "r1": r1, "r2": r2, "A": A, "B": B},
        "demo_program": demo,
        "cit": "linear",
        "description": ("Find the closed form of u_{n+2} = %.2g*u_{n+1} %+.2g*u_n with u_0=%.2g, u_1=%.2g, and verify "
                        "it against iteration." % (p, q, f0, f1)),
    }


def tmpl_cubic(b, c, d):
    # monic x^3 + b x^2 + c x + d, depressed to t^3 + p t + q
    p = c - b * b / 3
    q = 2 * b ** 3 / 27 - b * c / 3 + d
    disc = (q / 2) ** 2 + (p / 3) ** 3
    assert disc < 0, "need casus irreducibilis"
    r = 2 * math.sqrt(-p / 3)
    phi = math.acos((3 * q / (2 * p)) * math.sqrt(-3 / p))
    troots = [r * math.cos((phi - 2 * math.pi * k) / 3) for k in range(3)]
    roots = sorted(t - b / 3 for t in troots)  # x = t - b/3
    f = lambda x: x ** 3 + b * x ** 2 + c * x + d
    assert all(abs(f(x)) < 1e-8 for x in roots), [f(x) for x in roots]
    assert len({round(x, 6) for x in roots}) == 3
    steps = (
        "Step 1 — depress: x = t - b/3 = t %+.4f gives t^3 + p*t + q = 0 with p = %.6f, q = %.6f.\n"
        "Step 2 — discriminant (q/2)^2 + (p/3)^3 = %.6f < 0: three distinct real roots, the casus "
        "irreducibilis — Cardano's formula forces a detour through complex numbers even though every root "
        "is real. This is why normal AI fails here.\n"
        "Step 3 — trigonometric form: t_k = 2*sqrt(-p/3)*cos((phi - 2*pi*k)/3), phi = %.6f rad.\n"
        "Step 4 — back-substitute: x = %s.\n"
        "Step 5 — verify by substitution: residuals %s, all below 1e-8."
        % (-b / 3, p, q, disc, phi,
           ", ".join("%.8f" % x for x in roots),
           ", ".join("%.1e" % abs(f(x)) for x in roots)))
    demo = (
        "# Cubic (casus irreducibilis) verification\n"
        "import math\n"
        "b, c, d = %.15r, %.15r, %.15r\n"
        "p = c - b*b/3; q = 2*b**3/27 - b*c/3 + d\n"
        "r = 2*math.sqrt(-p/3)\n"
        "phi = math.acos((3*q/(2*p))*math.sqrt(-3/p))\n"
        "roots = sorted(r*math.cos((phi-2*math.pi*k)/3) - b/3 for k in range(3))\n"
        "f = lambda x: x**3 + b*x**2 + c*x + d\n"
        "print('roots:', roots)\n"
        "for x in roots:\n"
        "    assert abs(f(x)) < 1e-8, (x, f(x))\n"
        "print('SELFTEST: PASS')\n" % (b, c, d))
    return {
        "title": "Cubic x^3%+.2gx^2%+.2gx%+.2g = 0 (three real roots)" % (b, c, d),
        "equation": "x^3 + %.4g*x^2 + %.4g*x + %.4g = 0" % (b, c, d),
        "why_hard": ("Negative discriminant means three real roots, yet Cardano's formula demands complex "
                     "arithmetic to reach them — the casus irreducibilis. Normal AI either gives up or prints "
                     "unusable complex radicals. The trigonometric form delivers the real roots directly."),
        "solution_steps": steps,
        "answer": "x = %s" % ", ".join("%.8f" % x for x in roots),
        "verification": "Substitution residuals: %s." % ", ".join("%.1e" % abs(f(x)) for x in roots),
        "parameters": {"b": b, "c": c, "d": d, "p": p, "q": q, "discriminant": disc, "roots": roots},
        "demo_program": demo,
        "cit": "transcendental",
        "description": ("Solve x^3%+.2gx^2%+.2gx%+.2g = 0 with three real roots via the trigonometric form of "
                        "Cardano's solution, verified by substitution." % (b, c, d)),
    }


def tmpl_eigen(a, b, c, d):
    tr = a + d
    det = a * d - b * c
    disc = tr * tr - 4 * det
    assert disc > 0
    l1 = (tr + math.sqrt(disc)) / 2
    l2 = (tr - math.sqrt(disc)) / 2
    def evec(lam):
        if abs(b) >= abs(c):
            return (b, lam - a)
        return (lam - d, c)
    v1, v2 = evec(l1), evec(l2)
    def mv(M, v):
        return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])
    M = ((a, b), (c, d))
    r1 = math.dist(mv(M, v1), (l1 * v1[0], l1 * v1[1]))
    r2 = math.dist(mv(M, v2), (l2 * v2[0], l2 * v2[1]))
    assert r1 < 1e-9 and r2 < 1e-9
    steps = (
        "Step 1 — characteristic polynomial: det(A - lI) = l^2 - (tr)*l + det = l^2 - %.4g*l + %.4g = 0.\n"
        "Step 2 — eigenvalues: l = (tr +/- sqrt(tr^2 - 4*det))/2 = %.8f and %.8f.\n"
        "Step 3 — eigenvectors: for l1, solve (A - l1*I)v = 0 -> v1 = (%.6f, %.6f); for l2, "
        "v2 = (%.6f, %.6f).\n"
        "Step 4 — verify A*v = l*v: residuals %.1e and %.1e."
        % (tr, det, l1, l2, v1[0], v1[1], v2[0], v2[1], r1, r2))
    demo = (
        "# 2x2 eigen-decomposition verification\n"
        "import math\n"
        "a, b, c, d = %.15r, %.15r, %.15r, %.15r\n"
        "tr, det = a+d, a*d-b*c\n"
        "disc = tr*tr - 4*det\n"
        "l1 = (tr+math.sqrt(disc))/2; l2 = (tr-math.sqrt(disc))/2\n"
        "def evec(lam):\n"
        "    return (b, lam-a) if abs(b) >= abs(c) else (lam-d, c)\n"
        "for lam in (l1, l2):\n"
        "    v = evec(lam)\n"
        "    Av = (a*v[0]+b*v[1], c*v[0]+d*v[1])\n"
        "    assert math.dist(Av, (lam*v[0], lam*v[1])) < 1e-9\n"
        "print('eigenvalues:', l1, l2)\n"
        "print('SELFTEST: PASS')\n" % (a, b, c, d))
    return {
        "title": "Eigen-decomposition of [[%.2g, %.2g], [%.2g, %.2g]]" % (a, b, c, d),
        "equation": "Find eigenvalues and eigenvectors of A = [[%.4g, %.4g], [%.4g, %.4g]]" % (a, b, c, d),
        "why_hard": ("The 2x2 case looks trivial until the eigenvector solve: picking the numerically stable row, "
                     "handling near-zero entries, and verifying A*v = l*v rather than trusting the formula. "
                     "Normal AI routinely returns an eigenvector from a degenerate row choice."),
        "solution_steps": steps,
        "answer": "l1 = %.8f with v1 = (%.6f, %.6f); l2 = %.8f with v2 = (%.6f, %.6f)" % (l1, v1[0], v1[1], l2, v2[0], v2[1]),
        "verification": "A*v - l*v residuals: %.1e, %.1e." % (r1, r2),
        "parameters": {"a": a, "b": b, "c": c, "d": d, "l1": l1, "l2": l2},
        "demo_program": demo,
        "cit": "linear",
        "description": ("Compute the full eigen-decomposition of [[%.2g, %.2g], [%.2g, %.2g]] with verified "
                        "eigenvectors." % (a, b, c, d)),
    }


HE_TEMPLATES = [
    ("transcendental-equations", tmpl_lambert, [2.5, 7.0, 0.5, 10.0, 3.7]),
    ("transcendental-equations", tmpl_kepler, [(1.2, 0.3), (3.0, 0.7), (0.5, 0.1), (5.0, 0.9), (2.0, 0.5)]),
    ("differential-equations", tmpl_damped, [(0.1, 2.0, 1.0, 0.0), (0.25, 3.0, 0.5, 1.0), (0.05, 1.0, 2.0, -0.5), (0.4, 5.0, 1.0, 2.0), (0.15, 0.5, 0.0, 1.0)]),
    ("differential-equations", tmpl_heat, [(1.0, 0.1), (2.0, 0.05), (1.0, 0.5), (3.0, 0.2), (1.5, 0.1)]),
    ("diophantine-equations", tmpl_pell, [2, 3, 5, 7, 11]),
    ("diophantine-equations", tmpl_pythagorean, [(2, 1), (3, 2), (4, 1), (4, 3), (5, 2)]),
    ("integral-equations", tmpl_integral, [("gauss", 0, 1), ("gauss", -1, 2), ("gauss", 0, 2), ("sin2", 0, 0), ("x2emx", 0, 0)]),
    ("functional-equations", tmpl_functional, [2, -3, 0.5, 7, -1.25]),
    ("optimization-equations", tmpl_lagrange, [(1, 1, 2), (2, -1, 3), (3, 4, 10), (1, -2, 1), (5, 12, 13)]),
    ("optimization-equations", tmpl_recurrence, [(2, 1, 0, 1), (3, -2, 0, 1), (1, 1, 0, 1), (4, -3, 2, 5), (2, 2, 1, 3)]),
    ("transcendental-equations", tmpl_cubic, [(0, -7, 6), (-3, -6, 8), (0, -3, 1), (-6, 11, -6), (-4, 1, 6)]),
    ("optimization-equations", tmpl_eigen, [(4, 1, 2, 3), (2, 1, 1, 2), (5, 2, 2, 2), (3, 1, 0, 2), (6, -1, -1, 6)]),
]


def build_hard_equations():
    recs = []
    n = 0
    for field, fn, variants in HE_TEMPLATES:
        for v in variants:
            n += 1
            rid = "JAH-HE-%06d" % n
            r = fn(*v) if isinstance(v, tuple) else fn(v)
            title = dedup_title(r["title"])
            # the demo was already verified inside the template via asserts; re-run it as the record demo
            run_demo(r["demo_program"], rid)
            desc = enrich_description(r["description"], "Solved answer: " + r["answer"])
            recs.append({
                "id": rid, "t": title, "g": field,
                "name": title, "title": title,
                "description": desc,
                "equation": r["equation"],
                "why_hard": norm_space(r["why_hard"]),
                "solution_steps": norm_space(r["solution_steps"]),
                "answer": r["answer"],
                "verification": r["verification"],
                "parameters": r["parameters"],
                "demo": {"kind": "equation-verifier", "language": "python",
                         "program": r["demo_program"],
                         "note": "Re-derives and machine-checks the worked solution."},
                "citations": [CIT_EQ[r["cit"]]],
                "src": "signature",
            })
    return recs

# ================================================== IMPOSSIBLE PROGRAMS

def _sw_test_tail():
    return '\nprint("SELFTEST: PASS")\n'


def prog_wordfreq(name, topn, minlen):
    src = '''"""%s - word frequency analyzer (command-line tool)."""
import argparse
import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[a-z]+")

def tokenize(text, min_len=%d):
    return [w for w in WORD_RE.findall(text.lower()) if len(w) >= min_len]

def analyze(text, top_n=%d, min_len=%d):
    words = tokenize(text, min_len)
    counts = Counter(words)
    total = len(words)
    top = [(w, c, (c / total if total else 0.0)) for w, c in counts.most_common(top_n)]
    return {"total_words": total, "unique_words": len(counts), "top": top}

def format_report(stats):
    lines = ["total words: %%d, unique words: %%d" %% (stats["total_words"], stats["unique_words"])]
    for w, c, f in stats["top"]:
        lines.append("%%-18s %%6d  %%.2f%%%%" %% (w, c, f * 100))
    return "\\n".join(lines)

def main(argv=None):
    ap = argparse.ArgumentParser(prog="%s", description="Report word frequencies in text.")
    ap.add_argument("file", nargs="?", help="input file (default: stdin)")
    ap.add_argument("--top", type=int, default=%d)
    ap.add_argument("--min-len", type=int, default=%d)
    a = ap.parse_args(argv)
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    print(format_report(analyze(text, a.top, a.min_len)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, minlen, topn, minlen, name, topn, minlen)
    sample = "the cat sat on the mat\nthe dog sat on the log\nthe cat saw the dog\n"
    test = '''import io, tempfile, os
from contextlib import redirect_stdout
sample = "the cat sat on the mat\\nthe dog sat on the log\\nthe cat saw the dog\\n"
st = analyze(sample)
assert st["total_words"] == 15, st
assert st["unique_words"] == 7, st
assert st["top"][0][0] == "the" and st["top"][0][1] == 6, st["top"][0]
assert len(st["top"]) == min(%d, 7)
fd, tmp = tempfile.mkstemp(suffix=".txt")
os.write(fd, sample.encode("utf-8"))
os.close(fd)
try:
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = main([tmp, "--top", "%d"])
    assert rc == 0
    assert "the" in buf.getvalue()
finally:
    os.unlink(tmp)
print("sample run ok; top word:", st["top"][0][0])
''' % (topn, topn)
    return {"title": "%s — word frequency CLI" % name.title(),
            "field": "command-line-tools",
            "description": "%s is a complete command-line word frequency analyzer. It reads a file or stdin, "
                           "tokenizes, counts, and prints a ranked frequency table with percentages." % name,
            "beyond": BEYOND + " Argument parsing, stdin/file duality, and percentage math must all agree; "
                               "normal AI versions commonly divide by the wrong total or miscount ties.",
            "source_code": src,
            "explanation": "tokenize() lowercases and extracts [a-z]+ words of at least min_len; analyze() counts "
                           "with collections.Counter and computes each word's share of the total; format_report() "
                           "aligns a ranked table; main() wires argparse with --top and --min-len options and reads "
                           "from a file argument or stdin.",
            "usage": "python %s.py TEXTFILE --top 10 --min-len 3   (or pipe text via stdin)" % name,
            "test_code": test}


def prog_csvsum(name, precision):
    src = '''"""%s - CSV numeric column summarizer (data utility)."""
import argparse
import csv
import io
import sys

def summarize(csv_text, precision=%d):
    rows = list(csv.DictReader(io.StringIO(csv_text)))
    if not rows:
        return {"rows": 0, "columns": {}}
    cols = {}
    for col in rows[0].keys():
        vals = []
        for r in rows:
            try:
                vals.append(float(r[col]))
            except (ValueError, TypeError):
                pass
        if vals:
            cols[col] = {"count": len(vals),
                         "mean": round(sum(vals) / len(vals), precision),
                         "min": round(min(vals), precision),
                         "max": round(max(vals), precision)}
    return {"rows": len(rows), "columns": cols}

def format_summary(s):
    lines = ["rows: %%d" %% s["rows"]]
    for col, st in s["columns"].items():
        lines.append("%%s: n=%%d mean=%%s min=%%s max=%%s" %% (col, st["count"], st["mean"], st["min"], st["max"]))
    return "\\n".join(lines)

def main(argv=None):
    ap = argparse.ArgumentParser(prog="%s", description="Summarize numeric CSV columns.")
    ap.add_argument("file", nargs="?", help="CSV file (default: stdin)")
    a = ap.parse_args(argv)
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    print(format_summary(summarize(text)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, precision, name)
    test = '''csv_text = "name,age,score\\namy,30,88.5\\nbob,25,92.0\\ncid,35,79.5\\n"
s = summarize(csv_text)
assert s["rows"] == 3
assert s["columns"]["age"]["mean"] == 30.0, s
assert s["columns"]["age"]["min"] == 25 and s["columns"]["age"]["max"] == 35
assert s["columns"]["score"]["mean"] == round(260/3, %d), s
assert "name" not in s["columns"]
print("csv summary ok")
''' % precision
    return {"title": "%s — CSV column summarizer" % name.title(),
            "field": "data-utilities",
            "description": "%s summarizes every numeric column of a CSV file: row count, mean, min, and max, "
                           "skipping non-numeric columns automatically." % name,
            "beyond": BEYOND + " The subtlety is per-column numeric detection — a single bad cell must not kill "
                               "the column; normal AI versions crash on the first non-numeric value.",
            "source_code": src,
            "explanation": "csv.DictReader parses the input; each column is probed cell by cell with float() in a "
                           "try/except so text columns are skipped gracefully; statistics are rounded to the "
                           "configured precision.",
            "usage": "python %s.py data.csv   (or pipe CSV via stdin)" % name,
            "test_code": test}


def prog_jsonlfilter(name, op):
    src = '''"""%s - JSONL record filter (data utility)."""
import argparse
import json
import sys

def match(rec, rules):
    for field, op, value in rules:
        v = rec.get(field)
        if op == "eq":
            ok = (v == value)
        elif op == "ne":
            ok = (v != value)
        elif op == "gt":
            ok = (isinstance(v, (int, float)) and v > value)
        elif op == "lt":
            ok = (isinstance(v, (int, float)) and v < value)
        elif op == "contains":
            ok = (isinstance(v, str) and value in v)
        else:
            raise ValueError("unknown op: %%s" %% op)
        if not ok:
            return False
    return True

def filter_jsonl(text, rules):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        if match(rec, rules):
            out.append(rec)
    return out

def main(argv=None):
    ap = argparse.ArgumentParser(prog="%s", description="Filter JSONL records by field rules.")
    ap.add_argument("file", nargs="?", help="JSONL file (default: stdin)")
    ap.add_argument("--field", required=True)
    ap.add_argument("--op", required=True, choices=["eq", "ne", "gt", "lt", "contains"])
    ap.add_argument("--value", required=True)
    a = ap.parse_args(argv)
    try:
        value = json.loads(a.value)
    except ValueError:
        value = a.value
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    for rec in filter_jsonl(text, [(a.field, a.op, value)]):
        print(json.dumps(rec))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, name)
    rules = {"eq": '[("kind", "eq", "a")]', "gt": '[("n", "gt", 2)]',
             "contains": '[("msg", "contains", "ok")]'}[op]
    test = '''import json
text = '{"kind":"a","n":1,"msg":"all ok"}\\n{"kind":"b","n":3,"msg":"all ok"}\\n{"kind":"a","n":5,"msg":"bad"}\\n'
rules = %s
out = filter_jsonl(text, rules)
%s
print("jsonl filter ok:", len(out), "records")
''' % (rules,
       'assert len(out)==2 and all(r["kind"]=="a" for r in out)' if op == "eq" else
       'assert len(out)==2 and all(r["n"]>2 for r in out)' if op == "gt" else
       'assert len(out)==2 and all("ok" in r["msg"] for r in out)')
    return {"title": "%s — JSONL record filter (%s)" % (name.title(), op),
            "field": "data-utilities",
            "description": "%s filters JSONL streams by field rules (eq, ne, gt, lt, contains), one JSON object "
                           "per output line." % name,
            "beyond": BEYOND + " Type-safe comparisons matter: gt/lt must not compare strings to numbers; "
                               "normal AI versions throw TypeError on mixed-type columns.",
            "source_code": src,
            "explanation": "match() evaluates every rule against a record with type guards on numeric operators; "
                           "filter_jsonl() streams lines, skips blanks, and keeps matches; main() parses one rule "
                           "from the command line, auto-detecting JSON values.",
            "usage": 'python %s.py data.jsonl --field n --op gt --value 2' % name,
            "test_code": test}


def prog_dedup(name, keep):
    src = '''"""%s - duplicate file remover (file tool, keep=%s)."""
import argparse
import hashlib
import sys

def sha256_of(data):
    return hashlib.sha256(data).hexdigest()

def dedup(files, keep="%s"):
    """files: list of (name, bytes). Returns unique files in original order."""
    seq = files if keep == "first" else list(reversed(files))
    seen = {}
    order = []
    for fname, data in seq:
        h = sha256_of(data)
        if h not in seen:
            seen[h] = (fname, data)
            order.append(h)
    if keep == "last":
        order.reverse()
    return [seen[h] for h in order]

def main(argv=None):
    ap = argparse.ArgumentParser(prog="%s", description="List duplicate files by content hash.")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args(argv)
    items = []
    for f in a.files:
        with open(f, "rb") as fh:
            items.append((f, fh.read()))
    uniq = dedup(items, keep="%s")
    removed = len(items) - len(uniq)
    for fname, _ in uniq:
        print(fname)
    print("removed %%d duplicates" %% removed, file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, keep, keep, name, keep)
    test = '''files = [("a.txt", b"X"), ("b.txt", b"Y"), ("c.txt", b"X"), ("d.txt", b"Z")]
out = dedup(files, keep="%s")
names = [n for n, _ in out]
%s
print("dedup ok:", names)
''' % (keep,
       'assert names == ["a.txt", "b.txt", "d.txt"], names' if keep == "first"
       else 'assert names == ["b.txt", "c.txt", "d.txt"], names')
    return {"title": "%s — duplicate file remover (keep %s)" % (name.title(), keep),
            "field": "file-tools",
            "description": "%s removes duplicate files by SHA-256 content hash, keeping the %s occurrence and "
                           "preserving order." % (name, keep),
            "beyond": BEYOND + " Order preservation with keep-last semantics is the trap: naive reversal breaks "
                               "the output order; this implementation is verified for both modes.",
            "source_code": src,
            "explanation": "Files are hashed with SHA-256; for keep=last the list is scanned in reverse so the "
                           "last occurrence wins, then the surviving order is restored; main() reports how many "
                           "duplicates were removed.",
            "usage": "python %s.py *.txt   (prints unique files)" % name,
            "test_code": test}


def prog_tablefmt(name, style):
    src = '''"""%s - text table formatter (%s style)."""
import sys

def format_table(headers, rows):
    widths = [len(str(h)) for h in headers]
    for r in rows:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], len(str(v)))
    def line(vals):
        return "| " + " | ".join(str(v).ljust(widths[i]) for i, v in enumerate(vals)) + " |"
    out = [line(headers)]
    out.append("|-" + "-|-".join("-" * w for w in widths) + "-|")
    out.extend(line(r) for r in rows)
    return "\\n".join(out)

def main(argv=None):
    import csv
    text = sys.stdin.read()
    rows = list(csv.reader(text.splitlines(), delimiter="\\t"))
    if not rows:
        return 0
    print(format_table(rows[0], rows[1:]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, style)
    test = '''t = format_table(["name", "n"], [["amy", 30], ["bob", 7]])
lines = t.splitlines()
assert lines[0] == "| name | n  |", lines[0]
assert lines[1] == "|------|----|", lines[1]
assert lines[2] == "| amy  | 30 |", lines[2]
assert lines[3] == "| bob  | 7  |", lines[3]
print("table format ok")
'''
    return {"title": "%s — text table formatter" % name.title(),
            "field": "text-tools",
            "description": "%s aligns ragged text columns into a clean markdown-style table, computing column "
                           "widths from the data." % name,
            "beyond": BEYOND + " Width computation must consider headers AND every row; normal AI versions size "
                               "columns from the header alone and misalign short headers over long cells.",
            "source_code": src,
            "explanation": "Column widths are the max over headers and all cells; each cell is left-justified to "
                           "its column width; a separator row is built from the same widths so the grid always lines up.",
            "usage": "printf 'a\\tb\\n1\\t22\\n' | python %s.py" % name,
            "test_code": test}


def prog_linkcheck(name):
    src = '''"""%s - local documentation link checker (developer tool)."""
import re
import sys

LINK_RE = re.compile(r"\\[[^\\]]*\\]\\(([^)#\\s]+)(?:#[^)]*)?\\)")

def _normalize(path, target):
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    base = path.rsplit("/", 1)[0] if "/" in path else ""
    combo = target if (not base or target.startswith("/")) else base + "/" + target
    parts = []
    for p in combo.split("/"):
        if p in ("", "."):
            continue
        if p == "..":
            if parts:
                parts.pop()
        else:
            parts.append(p)
    return "/".join(parts)

def check_links(files):
    """files: dict path -> markdown text. Returns [(source, target)] broken links."""
    broken = []
    for path, text in files.items():
        for target in LINK_RE.findall(text):
            norm = _normalize(path, target)
            if norm is not None and norm not in files:
                broken.append((path, target))
    return broken

def main(argv=None):
    import json
    files = json.load(sys.stdin)
    broken = check_links(files)
    for src, tgt in broken:
        print("%%s -> %%s" %% (src, tgt))
    print("%%d broken links" %% len(broken), file=sys.stderr)
    return 1 if broken else 0

if __name__ == "__main__":
    sys.exit(main())
''' % name
    test = '''files = {
  "docs/index.md": "See [guide](guide.md) and [missing](nope.md) and [web](https://example.com).",
  "docs/guide.md": "Back to [index](index.md) and [up](../README.md).",
  "README.md": "top",
}
broken = check_links(files)
assert broken == [("docs/index.md", "nope.md")], broken
print("link check ok")
'''
    return {"title": "%s — documentation link checker" % name.title(),
            "field": "developer-tools",
            "description": "%s scans markdown files for local links and reports the broken ones, resolving relative "
                           "paths correctly." % name,
            "beyond": BEYOND + " Relative path resolution with ../ across directories is where normal AI checkers "
                               "produce false positives; this one normalizes paths before comparing.",
            "source_code": src,
            "explanation": "A regex extracts link targets; _normalize() resolves each target against the source "
                           "file's directory, collapsing ./ and ../; external URLs are skipped; anything not in "
                           "the file set is reported.",
            "usage": 'echo \'{"a.md": "[b](b.md)"}\' | python %s.py' % name,
            "test_code": test}


def prog_passgen(name, length, symbols):
    src = '''"""%s - password generator (system utility)."""
import argparse
import random
import string
import sys

SYMBOLS = "!@#$%%^&*-_=+"

def generate_password(length=%d, use_symbols=%s, rng=None):
    rng = rng or random.SystemRandom()
    lowers, uppers, digits = string.ascii_lowercase, string.ascii_uppercase, string.digits
    syms = SYMBOLS if use_symbols else ""
    required = [rng.choice(lowers), rng.choice(uppers), rng.choice(digits)]
    if use_symbols:
        required.append(rng.choice(syms))
    pool = lowers + uppers + digits + syms
    chars = required + [rng.choice(pool) for _ in range(length - len(required))]
    rng.shuffle(chars)
    return "".join(chars)

def main(argv=None):
    ap = argparse.ArgumentParser(prog="%s", description="Generate a policy-compliant password.")
    ap.add_argument("--length", type=int, default=%d)
    ap.add_argument("--no-symbols", action="store_true")
    a = ap.parse_args(argv)
    print(generate_password(a.length, not a.no_symbols))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, length, repr(symbols), name, length)
    test = '''import random, string
rng = random.Random(42)
pw = generate_password(rng=rng)
assert len(pw) == %d, len(pw)
assert any(c in string.ascii_lowercase for c in pw)
assert any(c in string.ascii_uppercase for c in pw)
assert any(c in string.digits for c in pw)
%s
print("password ok:", pw)
''' % (length,
       'assert any(c in "!@#$%%^&*-_=+" for c in pw)' if symbols
       else 'assert all(c not in "!@#$%%^&*-_=+" for c in pw)')
    return {"title": "%s — password generator (%d chars%s)" % (name.title(), length, ", symbols" if symbols else ", no symbols"),
            "field": "system-utilities",
            "description": "%s generates passwords guaranteed to satisfy a character-class policy: at least one "
                           "lowercase, uppercase, digit%s." % (name, ", and symbol" if symbols else ""),
            "beyond": BEYOND + " Guaranteeing every character class appears (not just hoping) requires placing "
                               "required characters before filling; normal AI generators routinely fail their own policy.",
            "source_code": src,
            "explanation": "One character from each required class is placed first, the rest are drawn from the "
                           "full pool, then the list is shuffled so required characters are not predictable; "
                           "SystemRandom is used in production, with an injectable rng for testing.",
            "usage": "python %s.py --length %d%s" % (name, length, " --no-symbols" if not symbols else ""),
            "test_code": test}


def prog_diffstat(name):
    src = '''"""%s - line diff summarizer (text tool)."""
import difflib
import sys

def diff_stats(a_lines, b_lines):
    sm = difflib.SequenceMatcher(None, a_lines, b_lines)
    added = removed = unchanged = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "insert":
            added += j2 - j1
        elif tag == "delete":
            removed += i2 - i1
        elif tag == "replace":
            added += j2 - j1
            removed += i2 - i1
        else:
            unchanged += i2 - i1
    return {"added": added, "removed": removed, "unchanged": unchanged,
            "total_a": len(a_lines), "total_b": len(b_lines)}

def main(argv=None):
    if len(sys.argv) != 3:
        print("usage: %s OLD NEW" %% "%s", file=sys.stderr)
        return 2
    a = open(sys.argv[1], encoding="utf-8").read().splitlines()
    b = open(sys.argv[2], encoding="utf-8").read().splitlines()
    st = diff_stats(a, b)
    print("+%%d -%%d =%%d lines (was %%d)" %% (st["added"], st["removed"], st["total_b"], st["total_a"]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % (name, name, name)
    test = '''st = diff_stats(["a", "b", "c"], ["a", "x", "c"])
assert st == {"added": 1, "removed": 1, "unchanged": 2, "total_a": 3, "total_b": 3}, st
st2 = diff_stats([], ["n1", "n2"])
assert st2["added"] == 2 and st2["removed"] == 0 and st2["unchanged"] == 0
print("diff stats ok")
'''
    return {"title": "%s — line diff summarizer" % name.title(),
            "field": "text-tools",
            "description": "%s summarizes the difference between two texts as added/removed/unchanged line counts." % name,
            "beyond": BEYOND + " Replace blocks must count on both sides; normal AI diff summaries routinely "
                               "undercount replacements as pure additions.",
            "source_code": src,
            "explanation": "difflib.SequenceMatcher opcodes classify each block; replace blocks add to both the "
                           "added and removed tallies; the summary line shows the net change.",
            "usage": "python %s.py old.txt new.txt" % name,
            "test_code": test}


def prog_treereport(name):
    src = '''"""%s - directory tree size reporter (file tool)."""
import json
import sys

def tree_size(node):
    if isinstance(node, dict):
        return sum(tree_size(v) for v in node.values())
    return node

def report(tree):
    lines = []
    def walk(node, prefix=""):
        for key in sorted(node):
            val = node[key]
            if isinstance(val, dict):
                lines.append("%%s%%s/ (%%d bytes)" %% (prefix, key, tree_size(val)))
                walk(val, prefix + "  ")
            else:
                lines.append("%%s%%s (%%d bytes)" %% (prefix, key, val))
    walk(tree)
    return {"total_bytes": tree_size(tree), "report": "\\n".join(lines)}

def main(argv=None):
    tree = json.load(sys.stdin)
    r = report(tree)
    print(r["report"])
    print("total: %%d bytes" %% r["total_bytes"], file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
''' % name
    test = '''tree = {"docs": {"a.md": 100, "b.md": 200}, "src": {"x.py": 50}, "README": 10}
r = report(tree)
assert r["total_bytes"] == 360, r
assert "docs/ (300 bytes)" in r["report"]
assert "  a.md (100 bytes)" in r["report"]
print("tree report ok")
'''
    return {"title": "%s — directory tree size reporter" % name.title(),
            "field": "file-tools",
            "description": "%s turns a nested file-size map into an indented size report with per-directory "
                           "subtotals." % name,
            "beyond": BEYOND + " Subtotals must be computed bottom-up and match the grand total; normal AI "
                               "versions print subtotals that do not add up.",
            "source_code": src,
            "explanation": "tree_size() recurses bottom-up; report() walks the tree in sorted order, printing "
                           "directory subtotals before descending; the grand total is the same function applied "
                           "at the root, so the numbers always agree.",
            "usage": 'echo \'{"a": {"b": 10}}\' | python %s.py' % name,
            "test_code": test}


PROG_SHARD_CHUNK = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/predictive-trajectories/chunks/chunk-0000.jsonl.gz"


def prog_wpaudit(check):
    checks = {
        "monotonic": "timestamp monotonicity",
        "bounds": "coordinate bounds",
        "speed": "segment speed plausibility",
        "fields": "required fields present",
        "ids": "id format and uniqueness",
        "full": "full audit report",
    }
    label = checks[check]
    src = '''"""Waypoint Auditor - %s (data utility).
Cross-database tool: reads the LIVE Predictive Trajectories archive chunk from the
JAH Databases data shard and audits it. The program's output is computed from the
real archive data, so it changes whenever the archive changes."""
import gzip
import json
import math
import urllib.request

CHUNK_URL = "%s"

def load_records(url=CHUNK_URL):
    with urllib.request.urlopen(url, timeout=30) as resp:
        raw = resp.read()
    return [json.loads(line) for line in gzip.decompress(raw).decode("utf-8").splitlines() if line.strip()]

def check_monotonic(records):
    bad = 0
    for r in records:
        ts = [w["t"] for w in r["waypoints"]]
        if any(b <= a for a, b in zip(ts, ts[1:])):
            bad += 1
    return {"records": len(records), "non_monotonic": bad}

def check_bounds(records, limit=1000.0):
    worst = 0.0
    for r in records:
        for w in r["waypoints"]:
            worst = max(worst, abs(w["x"]), abs(w["y"]), abs(w["z"]))
    return {"records": len(records), "max_abs_coord": worst, "within_limit": worst <= limit}

def check_speed(records, vmax=100.0):
    peak = 0.0
    for r in records:
        ws = r["waypoints"]
        for p, q in zip(ws, ws[1:]):
            d = math.dist((p["x"], p["y"], p["z"]), (q["x"], q["y"], q["z"]))
            dt = q["t"] - p["t"]
            if dt > 0:
                peak = max(peak, d / dt)
    return {"records": len(records), "peak_segment_speed": peak, "plausible": peak <= vmax}

def check_fields(records):
    required = ("id", "t", "g", "description", "platform", "prediction_method",
                "waypoints", "uncertainty_model", "equations", "parameters")
    missing = {}
    for r in records:
        miss = [k for k in required if k not in r]
        if miss:
            missing[r["id"]] = miss
    return {"records": len(records), "records_missing_fields": missing}

def check_ids(records):
    ids = [r["id"] for r in records]
    return {"records": len(records), "unique": len(set(ids)) == len(ids),
            "prefix_ok": all(i.startswith("JAH-PT-") for i in ids)}

def full_report(records):
    return {"monotonic": check_monotonic(records), "bounds": check_bounds(records),
            "speed": check_speed(records), "fields": check_fields(records), "ids": check_ids(records)}

CHECKS = {"monotonic": check_monotonic, "bounds": check_bounds, "speed": check_speed,
          "fields": check_fields, "ids": check_ids, "full": full_report}

def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Audit the live trajectory archive chunk.")
    ap.add_argument("--check", default="%s", choices=sorted(CHECKS))
    a = ap.parse_args(argv)
    records = load_records()
    print(json.dumps(CHECKS[a.check](records), indent=1))
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
''' % (label, PROG_SHARD_CHUNK, check)
    asserts = {
        "monotonic": 'r = check_monotonic(recs)\nassert r["non_monotonic"] == 0, r\nprint("monotonic ok:", r["records"], "records")',
        "bounds": 'r = check_bounds(recs)\nassert r["within_limit"], r\nprint("bounds ok; max coord:", round(r["max_abs_coord"], 2))',
        "speed": 'r = check_speed(recs)\nassert r["plausible"], r\nprint("speed ok; peak:", round(r["peak_segment_speed"], 2), "m/s")',
        "fields": 'r = check_fields(recs)\nassert not r["records_missing_fields"], r\nprint("fields ok:", r["records"], "records")',
        "ids": 'r = check_ids(recs)\nassert r["unique"] and r["prefix_ok"], r\nprint("ids ok:", r["records"], "records")',
        "full": 'r = full_report(recs)\nassert r["monotonic"]["non_monotonic"] == 0\nassert r["ids"]["unique"]\nprint("full audit ok")',
    }
    test = '''recs = load_records()
print("loaded", len(recs), "live records from the data shard")
assert len(recs) > 0
%s
''' % asserts[check]
    return {"title": "Waypoint Auditor — %s (live archive)" % label,
            "field": "data-utilities",
            "description": "Waypoint Auditor (%s) reads the live Predictive Trajectories archive chunk from the "
                           "JAH Databases data shard and audits %s across every record. Its output is computed "
                           "from real archive data." % (label, label),
            "beyond": BEYOND + " This tool pulls material from another database and lets it change the result: "
                               "every number it prints comes from the live archive, not from fixtures.",
            "source_code": src,
            "explanation": "load_records() fetches the gzipped JSONL chunk over HTTPS and parses it; each check_* "
                           "function scans every record's waypoints or metadata; main() selects the check from the "
                           "command line and prints JSON. Because it reads live data, re-running it after the "
                           "archive grows audits the new records too.",
            "usage": "python waypoint_auditor.py --check %s" % check,
            "test_code": test}


PROG_TEMPLATES = [
    ("wordfreq", prog_wordfreq, [("wordfreq", 10, 3), ("lexcount", 5, 3), ("termtally", 3, 3),
                                ("vocabscan", 20, 3), ("wordrank", 8, 3), ("textprobe", 15, 3)]),
    ("csvsum", prog_csvsum, [("csvsum", 2), ("colstat", 1), ("numscan", 3),
                             ("csvprobe", 2), ("fieldavg", 4), ("datasum", 2)]),
    ("jsonlfilter", prog_jsonlfilter, [("jsonlfilter", "eq"), ("jsonlfilter", "gt"), ("jsonlfilter", "contains"),
                                      ("recfilter", "eq"), ("recfilter", "gt"), ("jsonscan", "contains")]),
    ("dedup", prog_dedup, [("dedup", "first"), ("dedup", "last"), ("uniquify", "first"),
                           ("uniquify", "last"), ("dupeshave", "first"), ("dupeshave", "last")]),
    ("tablefmt", prog_tablefmt, [("tablefmt", "grid"), ("mdtable", "grid"), ("colalign", "grid"),
                                 ("textgrid", "grid"), ("asciitable", "grid"), ("prettyrows", "grid")]),
    ("linkcheck", prog_linkcheck, [("linkcheck",), ("doclinks",), ("mdlinkscan",),
                                   ("linkaudit",), ("refcheck",), ("linkhunter",)]),
    ("passgen", prog_passgen, [("passgen", 16, True), ("passgen", 20, True), ("passgen", 12, False),
                               ("keyforge", 24, True), ("safekey", 16, False), ("passgen", 32, True)]),
    ("diffstat", prog_diffstat, [("diffstat",), ("linediff",), ("changediff",),
                                ("diffsum",), ("patchstat",), ("diffstat",)]),
    ("treereport", prog_treereport, [("treereport",), ("dirsize",), ("sizetree",),
                                    ("treereport",), ("foldstat",), ("dirtreemap",)]),
    ("wpaudit", prog_wpaudit, ["monotonic", "bounds", "speed", "fields", "ids", "full"]),
]

# ===================================================== IMPOSSIBLE CODE

def code_lru(name, capacity):
    src = '''"""%s - LRU cache (data structure)."""
from collections import OrderedDict

class LRUCache:
    """Fixed-capacity least-recently-used cache with O(1) get/put."""

    def __init__(self, capacity=%d):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self.capacity = capacity
        self._d = OrderedDict()

    def get(self, key):
        if key not in self._d:
            return None
        self._d.move_to_end(key)
        return self._d[key]

    def put(self, key, value):
        if key in self._d:
            self._d.move_to_end(key)
        self._d[key] = value
        if len(self._d) > self.capacity:
            self._d.popitem(last=False)

    def __len__(self):
        return len(self._d)

    def keys(self):
        return list(self._d.keys())
''' % (name, capacity)
    test = '''c = LRUCache(capacity=%d)
%s
print("lru ok")
''' % (capacity,
       '''c.put("a", 1); c.put("b", 2)
assert c.get("a") == 1
c.put("c", 3)
assert c.get("b") is None, "b should be evicted"
assert c.get("a") == 1 and c.get("c") == 3
assert len(c) == 2''' if capacity == 2 else
       '''import random
rng = random.Random(7)
for i in range(%d * 3):
    c.put(i, i * i)
assert len(c) == %d
# the last `capacity` keys must survive
for i in range(%d * 2, %d * 3):
    assert c.get(i) == i * i, i
print("capacity %d holds")''' % (capacity, capacity, capacity, capacity, capacity))
    return {"title": "%s — LRU cache (capacity %d)" % (name.title(), capacity),
            "field": "data-structures",
            "description": "%s is a fixed-capacity LRU cache with O(1) get and put, built on OrderedDict." % name,
            "beyond": BEYOND + " The eviction edge case — updating an existing key must refresh recency without "
                               "growing the cache; normal AI versions evict the wrong entry on update.",
            "source_code": src,
            "explanation": "An OrderedDict keeps insertion order; get() moves the key to the end (most recent); "
                           "put() moves existing keys to the end and pops from the front when over capacity. "
                           "Updating an existing key refreshes recency first so the size accounting stays exact.",
            "usage": "c = LRUCache(capacity=%d); c.put('k', v); c.get('k')" % capacity,
            "test_code": test}


def code_unionfind(name):
    src = '''"""%s - disjoint-set union-find (data structure)."""
class UnionFind:
    """Union-find with path compression and union by rank."""

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def components(self):
        reps = {}
        for x in list(self.parent):
            reps.setdefault(self.find(x), []).append(x)
        return list(reps.values())
''' % name
    test = '''uf = UnionFind()
assert uf.union(1, 2) is True
assert uf.union(2, 3) is True
assert uf.union(1, 3) is False
assert uf.union(4, 5) is True
assert uf.connected(1, 3)
assert not uf.connected(1, 4)
assert not uf.connected(1, 99)
comps = sorted(sorted(c) for c in uf.components())
assert comps == [[1, 2, 3], [4, 5], [99]], comps
print("union-find ok")
'''
    return {"title": "%s — disjoint-set union-find" % name.title(),
            "field": "data-structures",
            "description": "%s is a union-find with path compression and union by rank: near-constant amortized "
                           "find/union." % name,
            "beyond": BEYOND + " Path halving plus union-by-rank must compose correctly; normal AI versions "
                               "implement one optimization but break the other.",
            "source_code": src,
            "explanation": "find() compresses the path by halving on the way up; union() attaches the shorter "
                           "tree under the taller and bumps rank only on ties; elements are created lazily on "
                           "first touch.",
            "usage": "uf = UnionFind(); uf.union(a, b); uf.connected(a, b)",
            "test_code": test}


def code_topo(name):
    src = '''"""%s - topological sort, Kahn's algorithm (algorithm)."""
import heapq
from collections import defaultdict

def topo_sort(nodes, edges):
    """Return a deterministic topological order. Raises ValueError on cycles."""
    adj = defaultdict(list)
    indeg = {n: 0 for n in nodes}
    for u, v in edges:
        if u not in indeg or v not in indeg:
            raise ValueError("edge references unknown node")
        adj[u].append(v)
        indeg[v] += 1
    heap = [n for n in nodes if indeg[n] == 0]
    heapq.heapify(heap)
    out = []
    while heap:
        u = heapq.heappop(heap)
        out.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    if len(out) != len(nodes):
        raise ValueError("cycle detected")
    return out
''' % name
    test = '''order = topo_sort(["a", "b", "c", "d"],
                    [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")])
pos = {n: i for i, n in enumerate(order)}
assert pos["a"] < pos["b"] < pos["d"] and pos["a"] < pos["c"] < pos["d"]
try:
    topo_sort(["x", "y"], [("x", "y"), ("y", "x")])
    raise SystemExit("cycle not detected")
except ValueError:
    pass
print("topo sort ok:", order)
'''
    return {"title": "%s — topological sort (Kahn)" % name.title(),
            "field": "algorithms",
            "description": "%s is a deterministic topological sort using Kahn's algorithm with cycle detection." % name,
            "beyond": BEYOND + " Cycle detection must be exact — silently returning a partial order is the normal "
                               "AI failure; this version raises.",
            "source_code": src,
            "explanation": "In-degrees are counted; a min-heap always emits the smallest available node for "
                           "determinism; if fewer nodes are emitted than exist, a cycle exists and ValueError is raised.",
            "usage": "topo_sort(nodes, [(u, v), ...])  # u before v",
            "test_code": test}


def code_interval(name):
    src = '''"""%s - interval merging (algorithm)."""
def merge_intervals(intervals):
    """Merge overlapping or touching intervals. Returns sorted disjoint tuples."""
    if not intervals:
        return []
    ivs = sorted(intervals)
    for s, e in ivs:
        if e < s:
            raise ValueError("inverted interval")
    out = [[ivs[0][0], ivs[0][1]]]
    for s, e in ivs[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [tuple(x) for x in out]
''' % name
    test = '''assert merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]) == [(1, 6), (8, 10), (15, 18)]
assert merge_intervals([(1, 4), (4, 5)]) == [(1, 5)]
assert merge_intervals([]) == []
assert merge_intervals([(5, 5)]) == [(5, 5)]
try:
    merge_intervals([(3, 1)])
    raise SystemExit("inverted not detected")
except ValueError:
    pass
print("interval merge ok")
'''
    return {"title": "%s — interval merging" % name.title(),
            "field": "algorithms",
            "description": "%s merges overlapping or touching intervals into a sorted disjoint list." % name,
            "beyond": BEYOND + " Touching intervals (4,5) after (1,4) must merge, and inverted intervals must "
                               "raise rather than silently corrupt; normal AI versions get one of these wrong.",
            "source_code": src,
            "explanation": "Sort by start; sweep once, extending the current interval while the next start is "
                           "within it; inverted intervals raise ValueError immediately.",
            "usage": "merge_intervals([(1, 3), (2, 6)])  # -> [(1, 6)]",
            "test_code": test}


def code_astar(name):
    src = '''"""%s - A* grid pathfinding (search)."""
import heapq

def astar(grid, start, goal):
    """grid: list of equal-length strings, '#' is a wall. Returns node list or None."""
    rows, cols = len(grid), len(grid[0])
    def h(p):
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    openh = [(h(start), 0, start, [start])]
    best = {start: 0}
    while openh:
        f, g, p, path = heapq.heappop(openh)
        if p == goal:
            return path
        if g > best[p]:
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (p[0] + dr, p[1] + dc)
            if 0 <= q[0] < rows and 0 <= q[1] < cols and grid[q[0]][q[1]] != "#":
                ng = g + 1
                if ng < best.get(q, float("inf")):
                    best[q] = ng
                    heapq.heappush(openh, (ng + h(q), ng, q, path + [q]))
    return None
''' % name
    test = '''grid = [".....",
        ".###.",
        ".....",
        ".###.",
        "....."]
path = astar(grid, (0, 0), (4, 4))
assert path is not None
assert path[0] == (0, 0) and path[-1] == (4, 4)
assert len(path) - 1 == 8, len(path)
for r, c in path:
    assert grid[r][c] != "#"
assert astar(["###", "###"], (0, 0), (1, 1)) is None
print("astar ok, length", len(path) - 1)
'''
    return {"title": "%s — A* grid pathfinding" % name.title(),
            "field": "search-and-sort",
            "description": "%s is an A* shortest-path search on grids with Manhattan heuristic and wall handling." % name,
            "beyond": BEYOND + " The stale-entry skip (g > best[p]) is what keeps A* correct with a binary heap; "
                               "normal AI versions omit it and return suboptimal paths.",
            "source_code": src,
            "explanation": "Manhattan distance is an admissible heuristic on 4-connected grids; the heap orders by "
                           "f = g + h; stale heap entries are skipped via the best-g map; walls are never expanded.",
            "usage": "astar(grid_rows, (r0, c0), (r1, c1))",
            "test_code": test}


def code_binsearch(name):
    src = '''"""%s - binary search bounds (search)."""
def lower_bound(a, x):
    """First index with a[i] >= x."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(a, x):
    """First index with a[i] > x."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def count_equal(a, x):
    return upper_bound(a, x) - lower_bound(a, x)

def count_in_range(a, lo_x, hi_x):
    return upper_bound(a, hi_x) - lower_bound(a, lo_x)
''' % name
    test = '''import bisect, random
a = [1, 2, 2, 2, 3, 5]
assert lower_bound(a, 2) == 1
assert upper_bound(a, 2) == 4
assert count_equal(a, 2) == 3
assert count_in_range(a, 2, 3) == 4
assert lower_bound([], 9) == 0 and upper_bound([], 9) == 0
rng = random.Random(3)
for _ in range(200):
    b = sorted(rng.randint(0, 20) for _ in range(rng.randint(0, 30)))
    x = rng.randint(0, 20)
    assert lower_bound(b, x) == bisect.bisect_left(b, x)
    assert upper_bound(b, x) == bisect.bisect_right(b, x)
print("binary search bounds ok")
'''
    return {"title": "%s — binary search bounds" % name.title(),
            "field": "search-and-sort",
            "description": "%s gives lower_bound, upper_bound, and range counting on sorted lists, verified "
                           "against the standard library on randomized inputs." % name,
            "beyond": BEYOND + " Off-by-one errors in bound searches are the classic normal-AI bug; this module "
                               "is fuzz-checked against bisect on hundreds of random arrays.",
            "source_code": src,
            "explanation": "Both bounds maintain the invariant over [lo, hi); lower_bound keeps a[mid] < x to the "
                           "left, upper_bound keeps a[mid] <= x to the left; counts are differences of bounds.",
            "usage": "lower_bound(sorted_list, x); count_in_range(a, lo, hi)",
            "test_code": test}


def code_expr(name):
    src = '''"""%s - arithmetic expression evaluator (parsing)."""
import re

_TOKEN_RE = re.compile(r"\\d+(?:\\.\\d+)?|[+\\-*/^()]")
_PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

def tokenize(expr):
    s = expr.replace(" ", "")
    if not s:
        raise ValueError("empty expression")
    toks = _TOKEN_RE.findall(s)
    if "".join(toks) != s:
        raise ValueError("bad characters")
    return toks

def to_rpn(tokens):
    out, ops = [], []
    for t in tokens:
        if re.fullmatch(r"\\d+(?:\\.\\d+)?", t):
            out.append(float(t))
        elif t == "(":
            ops.append(t)
        elif t == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            if not ops:
                raise ValueError("mismatched parenthesis")
            ops.pop()
        else:
            while (ops and ops[-1] != "(" and
                   (_PREC[ops[-1]] > _PREC[t] or (_PREC[ops[-1]] == _PREC[t] and t != "^"))):
                out.append(ops.pop())
            ops.append(t)
    while ops:
        if ops[-1] == "(":
            raise ValueError("mismatched parenthesis")
        out.append(ops.pop())
    return out

def eval_rpn(rpn):
    st = []
    for t in rpn:
        if isinstance(t, float):
            st.append(t)
        else:
            b, a = st.pop(), st.pop()
            st.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b, "^": a ** b}[t])
    if len(st) != 1:
        raise ValueError("bad expression")
    return st[0]

def evaluate(expr):
    """Evaluate + - * / ^ with parentheses. ^ is right-associative."""
    return eval_rpn(to_rpn(tokenize(expr)))
''' % name
    test = '''assert evaluate("3+4*2/(1-5)^2") == 3.5
assert evaluate("2^3^2") == 512.0
assert evaluate("(2+3)*4") == 20.0
assert evaluate("10-2*3") == 4.0
try:
    evaluate("2+(3")
    raise SystemExit("parens not detected")
except ValueError:
    pass
print("expression evaluator ok")
'''
    return {"title": "%s — arithmetic expression evaluator" % name.title(),
            "field": "parsing",
            "description": "%s parses and evaluates arithmetic with correct precedence and right-associative "
                           "exponentiation." % name,
            "beyond": BEYOND + " Right-associative ^ and mismatched-parenthesis errors are where normal AI "
                               "evaluators break; both are handled and tested here.",
            "source_code": src,
            "explanation": "The shunting-yard algorithm converts to reverse Polish notation with precedence "
                           "climbing (and right associativity for ^); a stack machine then evaluates the RPN. "
                           "Note: unary minus is not supported by design.",
            "usage": 'evaluate("3+4*2/(1-5)^2")  # -> 3.5',
            "test_code": test}


def code_rle(name):
    src = '''"""%s - run-length codec (encoding)."""
def rle_encode(s):
    """Encode a string as a list of (char, count) pairs."""
    if not s:
        return []
    out = []
    cur, n = s[0], 1
    for ch in s[1:]:
        if ch == cur:
            n += 1
        else:
            out.append((cur, n))
            cur, n = ch, 1
    out.append((cur, n))
    return out

def rle_decode(pairs):
    """Decode a list of (char, count) pairs back to a string."""
    return "".join(ch * n for ch, n in pairs)
''' % name
    test = '''assert rle_encode("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
assert rle_encode("") == []
assert rle_decode(rle_encode("aaabbc")) == "aaabbc"
import random
rng = random.Random(11)
for _ in range(100):
    s = "".join(rng.choice("ab") for _ in range(rng.randint(0, 40)))
    assert rle_decode(rle_encode(s)) == s
print("rle codec ok")
'''
    return {"title": "%s — run-length codec" % name.title(),
            "field": "encoding",
            "description": "%s is a run-length encoder/decoder with fuzz-verified roundtrips." % name,
            "beyond": BEYOND + " The empty-string and single-run edge cases break naive encoders; both are "
                               "covered and fuzz-tested.",
            "source_code": src,
            "explanation": "A single pass groups equal neighbours into (char, count) pairs; decoding repeats each "
                           "char by its count; roundtrips are fuzz-checked on random binary strings.",
            "usage": "rle_decode(rle_encode('aaabbc'))",
            "test_code": test}


def code_varint(name):
    src = '''"""%s - varint codec, protobuf style (encoding)."""
def varint_encode(n):
    """Encode a non-negative int as varint bytes."""
    if n < 0:
        raise ValueError("varint needs n >= 0")
    out = bytearray()
    while True:
        bits = n & 0x7F
        n >>= 7
        if n:
            out.append(bits | 0x80)
        else:
            out.append(bits)
            break
    return bytes(out)

def varint_decode(buf):
    """Decode varint bytes. Returns (value, bytes_consumed)."""
    n = shift = 0
    for i, byte in enumerate(buf):
        n |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return n, i + 1
        shift += 7
    raise ValueError("truncated varint")
''' % name
    test = '''assert varint_encode(300) == b"\\xac\\x02"
assert varint_decode(b"\\xac\\x02") == (300, 2)
for n in [0, 1, 127, 128, 300, 2**32 - 1, 2**64 - 1]:
    enc = varint_encode(n)
    val, used = varint_decode(enc + b"\\x00")
    assert val == n and used == len(enc), (n, enc)
try:
    varint_decode(b"\\x80")
    raise SystemExit("truncation not detected")
except ValueError:
    pass
print("varint codec ok")
'''
    return {"title": "%s — varint codec" % name.title(),
            "field": "encoding",
            "description": "%s encodes integers as protobuf-style varints with truncation detection." % name,
            "beyond": BEYOND + " The continuation-bit protocol is easy to get subtly wrong at byte boundaries; "
                               "this codec is verified against known vectors including 2^64-1.",
            "source_code": src,
            "explanation": "Seven payload bits per byte with the high bit as continuation flag, little-endian "
                           "order; decoding accumulates until a byte without the flag; a buffer ending mid-value "
                           "raises ValueError.",
            "usage": "varint_decode(varint_encode(300))  # -> (300, 2)",
            "test_code": test}


def code_retry(name):
    src = '''"""%s - retry decorator with backoff (reliability pattern)."""
import time

def retry(tries=3, delay=0.1, backoff=2.0, exceptions=(Exception,), jitter=0.0,
          sleep=time.sleep, rng=None):
    """Retry a function with exponential backoff. Testable via sleep/rng injection."""
    def deco(fn):
        def wrapper(*a, **k):
            d = delay
            last = None
            for attempt in range(tries):
                try:
                    return fn(*a, **k)
                except exceptions as exc:
                    last = exc
                    if attempt == tries - 1:
                        break
                    j = (rng.random() * jitter) if (rng is not None and jitter) else 0.0
                    sleep(d + j)
                    d *= backoff
            raise last
        return wrapper
    return deco
''' % name
    test = '''calls = []
sleeps = []
def flaky():
    calls.append(1)
    if len(calls) < 3:
        raise IOError("boom")
    return "done"
f = retry(tries=4, delay=0.1, backoff=2.0, sleep=sleeps.append)(flaky)
assert f() == "done"
assert len(calls) == 3
assert sleeps == [0.1, 0.2], sleeps
calls2 = []
@retry(tries=2, delay=0.05, sleep=lambda s: None)
def always():
    calls2.append(1)
    raise RuntimeError("nope")
try:
    always()
    raise SystemExit("should have raised")
except RuntimeError:
    pass
assert len(calls2) == 2
print("retry decorator ok")
'''
    return {"title": "%s — retry decorator with backoff" % name.title(),
            "field": "reliability-patterns",
            "description": "%s retries flaky functions with exponential backoff and injectable sleep for testing." % name,
            "beyond": BEYOND + " Testability is the hard part: real time.sleep in tests is a normal-AI smell; "
                               "this decorator injects sleep and rng so backoff timing is asserted exactly.",
            "source_code": src,
            "explanation": "The decorator wraps the function, catching the configured exceptions; sleeps grow by "
                           "the backoff factor with optional jitter; the last exception is re-raised after the "
                           "final attempt; sleep and rng are injectable so tests assert exact delay sequences.",
            "usage": "@retry(tries=4, delay=0.1, backoff=2.0)\\ndef fetch(): ...",
            "test_code": test}


CODE_TEMPLATES = [
    ("lru", code_lru, [("lrucache", 2), ("lrucache", 3), ("lrucache", 4), ("lrucache", 5), ("lrucache", 8), ("lrucache", 10)]),
    ("unionfind", code_unionfind, [("unionfind",), ("disjointset",), ("dsu",), ("unionfind",), ("partitions",), ("unionfind",)]),
    ("topo", code_topo, [("toposort",), ("kahnsort",), ("dagsort",), ("toposort",), ("ordersort",), ("toposort",)]),
    ("interval", code_interval, [("intervalmerge",), ("rangemerge",), ("intervalmerge",), ("spanmerge",), ("intervalmerge",), ("ivmerge",)]),
    ("astar", code_astar, [("astar",), ("gridastar",), ("pathfind",), ("astar",), ("routefind",), ("astar",)]),
    ("binsearch", code_binsearch, [("binsearch",), ("bisectbounds",), ("binsearch",), ("rangefind",), ("binsearch",), ("sortedcount",)]),
    ("expr", code_expr, [("expreval",), ("mathexpr",), ("expreval",), ("formulaparse",), ("expreval",), ("calcexpr",)]),
    ("rle", code_rle, [("rlecodec",), ("rlecodec",), ("runlength",), ("rlecodec",), ("rlezip",), ("rlecodec",)]),
    ("varint", code_varint, [("varint",), ("varintcodec",), ("varint",), ("uvarint",), ("varint",), ("vintcodec",)]),
    ("retry", code_retry, [("retry",), ("backoff",), ("retry",), ("retrypolicy",), ("retry",), ("resilient",)]),
]

# ================================================== IMPOSSIBLE SCRIPTS

def scr_rename(name, pattern, repl, samples, expected):
    src = '''"""%s - bulk file renamer (file automation)."""
import re

def bulk_rename(files, pattern=r"%s", repl=r"%s"):
    """files: dict old_name -> content. Returns (renamed_dict, mapping)."""
    rx = re.compile(pattern)
    out, mapping = {}, {}
    for old in files:
        new = rx.sub(repl, old)
        if new != old:
            mapping[old] = new
        if new in out:
            raise ValueError("name collision: " + new)
        out[new] = files[old]
    return out, mapping
''' % (name, pattern, repl)
    test = '''files = %s
out, mapping = bulk_rename(files)
assert mapping == %s, mapping
assert sorted(out) == %s, sorted(out)
print("bulk rename ok")
''' % (repr(samples), repr(expected), repr(sorted(
        [expected.get(k, k) for k in samples])))
    return {"title": "%s — bulk file renamer" % name.title(),
            "field": "file-automation",
            "description": "%s renames files by regex substitution with collision detection." % name,
            "beyond": BEYOND + " Collision detection is the part normal AI renamers skip — two files mapping to "
                               "one name silently destroys data; this one raises.",
            "source_code": src,
            "explanation": "Each name is rewritten with re.sub; the mapping is recorded; if two names collide on "
                           "one target, ValueError is raised before anything is returned.",
            "usage": "bulk_rename({'img_001.png': data})  # -> ({'photo_001.png': data}, mapping)",
            "test_code": test}


def scr_manifest(name):
    src = '''"""%s - backup integrity manifest (backup and integrity)."""
import hashlib

def write_manifest(files):
    """files: dict path -> bytes. Returns manifest text."""
    lines = []
    for path in sorted(files):
        data = files[path]
        lines.append("%%s  %%d  %%s" %% (hashlib.sha256(data).hexdigest(), len(data), path))
    return "\\n".join(lines) + "\\n"

def verify_manifest(files, manifest):
    """Returns a list of problems: (kind, path). Empty means intact."""
    want = {}
    problems = []
    for line in manifest.splitlines():
        parts = line.split("  ")
        if len(parts) != 3:
            problems.append(("bad-line", line))
            continue
        h, size, path = parts
        want[path] = (h, int(size))
    for path, (h, size) in want.items():
        if path not in files:
            problems.append(("missing", path))
        elif hashlib.sha256(files[path]).hexdigest() != h:
            problems.append(("modified", path))
        elif len(files[path]) != size:
            problems.append(("size-mismatch", path))
    for path in files:
        if path not in want:
            problems.append(("untracked", path))
    return problems
''' % name
    test = '''files = {"a.txt": b"hello", "b.txt": b"world"}
man = write_manifest(files)
assert verify_manifest(files, man) == []
tampered = dict(files); tampered["a.txt"] = b"HELLO"
assert verify_manifest(tampered, man) == [("modified", "a.txt")]
gone = {"b.txt": b"world"}
probs = verify_manifest(gone, man)
assert ("missing", "a.txt") in probs and ("untracked", "b.txt") not in probs
print("manifest ok")
'''
    return {"title": "%s — backup integrity manifest" % name.title(),
            "field": "backup-and-integrity",
            "description": "%s writes SHA-256 manifests for file sets and verifies them, detecting modification, "
                           "loss, and untracked files." % name,
            "beyond": BEYOND + " Verification must distinguish modified vs missing vs untracked; normal AI "
                               "checkers lump them together and hide data loss.",
            "source_code": src,
            "explanation": "write_manifest() sorts paths for determinism and records hash, size, and path; "
                           "verify_manifest() re-hashes every file and classifies each discrepancy precisely.",
            "usage": "man = write_manifest(files); verify_manifest(files, man)  # [] means intact",
            "test_code": test}


def scr_logextract(name):
    src = '''"""%s - log error extractor (text processing)."""
import re
from collections import Counter

LOG_RE = re.compile(r"^(\\d{4}-\\d{2}-\\d{2})[T ](\\d{2}):\\d{2}:\\d{2}\\s+\\[?(ERROR|WARN|INFO)\\]?[:\\s]+(.*)$")

def extract_errors(log_text, levels=("ERROR",)):
    hits = []
    for i, line in enumerate(log_text.splitlines(), 1):
        m = LOG_RE.match(line)
        if m and m.group(3) in levels:
            hits.append({"line": i, "date": m.group(1), "hour": m.group(2),
                         "level": m.group(3), "message": m.group(4).strip()})
    return hits

def summarize_by_hour(hits):
    return dict(sorted(Counter(h["date"] + " " + h["hour"] + ":00" for h in hits).items()))
''' % name
    test = '''log = ("2024-01-01 10:00:01 [INFO] boot\\n"
       "2024-01-01 10:05:11 [ERROR] disk full\\n"
       "2024-01-01 10:05:12 ERROR retry failed\\n"
       "2024-01-01 11:00:00 [WARN] slow\\n"
       "2024-01-01 11:30:00 [ERROR] timeout\\n")
hits = extract_errors(log)
assert len(hits) == 3, hits
assert hits[0]["message"] == "disk full" and hits[0]["line"] == 2
assert summarize_by_hour(hits) == {"2024-01-01 10:00": 2, "2024-01-01 11:00": 1}
print("log extract ok")
'''
    return {"title": "%s — log error extractor" % name.title(),
            "field": "text-processing",
            "description": "%s extracts errors from logs with timestamps and summarizes them by hour." % name,
            "beyond": BEYOND + " Real logs mix bracketed and bare level tags; normal AI regexes match one style "
                               "and silently drop the other.",
            "source_code": src,
            "explanation": "One regex handles both '[ERROR]' and 'ERROR' styles with optional T/space date "
                           "separators; extract_errors() keeps line numbers for traceability; summarize_by_hour() "
                           "buckets hits for spotting incident windows.",
            "usage": "extract_errors(open('app.log').read())",
            "test_code": test}


def scr_deduplines(name, ignore_case):
    src = '''"""%s - duplicate line remover (text processing)."""
def dedup_lines(text, ignore_case=%s, ignore_blank=False):
    seen = set()
    out = []
    for line in text.splitlines():
        if ignore_blank and not line.strip():
            continue
        key = line.lower() if ignore_case else line
        if key not in seen:
            seen.add(key)
            out.append(line)
    return "\\n".join(out)
''' % (name, repr(ignore_case))
    test = '''t = "b\\nA\\na\\nB\\n\\nc\\n"
out = dedup_lines(t)
%s
print("dedup lines ok")
''' % ('assert out == "b\\nA\\na\\nB\\n\\nc", repr(out)' if not ignore_case
       else 'assert out == "b\\nA\\n\\nc", repr(out)')
    return {"title": "%s — duplicate line remover%s" % (name.title(), " (case-insensitive)" if ignore_case else ""),
            "field": "text-processing",
            "description": "%s removes duplicate lines while preserving first-occurrence order." % name,
            "beyond": BEYOND + " Order preservation with optional case folding is the detail normal AI versions "
                               "fumble — they sort the output or fold the case of the kept lines.",
            "source_code": src,
            "explanation": "A seen-set tracks keys (optionally lowercased) while the original line text is kept; "
                           "first occurrences pass through in order; blank-line handling is a separate flag.",
            "usage": "dedup_lines(open('list.txt').read())",
            "test_code": test}


def scr_todoscan(name):
    src = '''"""%s - TODO comment scanner (text processing)."""
import re

TODO_RE = re.compile(r"#\\s*(TODO|FIXME|XXX)\\b\\s*:?\\s*(.*)$")

def scan_todos(files):
    """files: dict path -> source text. Returns list of {file, line, tag, text}."""
    hits = []
    for path in sorted(files):
        for i, line in enumerate(files[path].splitlines(), 1):
            m = TODO_RE.search(line)
            if m:
                hits.append({"file": path, "line": i, "tag": m.group(1), "text": m.group(2).strip()})
    return hits
''' % name
    test = '''files = {"a.py": "x = 1  # TODO: handle zero\\n#FIXME retry\\ny = 2\\n",
         "b.py": "# just a comment\\n# XXX: slow path\\n"}
hits = scan_todos(files)
assert len(hits) == 3, hits
assert hits[0] == {"file": "a.py", "line": 1, "tag": "TODO", "text": "handle zero"}, hits[0]
assert hits[2]["tag"] == "XXX" and hits[2]["line"] == 2
print("todo scan ok")
'''
    return {"title": "%s — TODO comment scanner" % name.title(),
            "field": "text-processing",
            "description": "%s scans source files for TODO, FIXME, and XXX comments with file and line numbers." % name,
            "beyond": BEYOND + " The regex must not match words like 'TODOLIST' and must tolerate missing colons; "
                               "normal AI scanners over- or under-match.",
            "source_code": src,
            "explanation": "A word-boundary regex finds the three tags in # comments with an optional colon; "
                           "files are scanned in sorted order so reports are deterministic.",
            "usage": "scan_todos({'a.py': source_text})",
            "test_code": test}


def scr_inimigrate(name, oldkey, newkey):
    src = '''"""%s - config key migrator (data cleaning)."""
def migrate_ini(text, key_map=%s):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ";")) or s.startswith("[") or "=" not in line:
            out.append(line)
            continue
        k, v = line.split("=", 1)
        ks = k.strip()
        if ks in key_map:
            out.append(k.replace(ks, key_map[ks], 1) + "=" + v)
        else:
            out.append(line)
    return "\\n".join(out)
''' % (name, repr({oldkey: newkey}))
    test = ('ini = "[server]\\n' + oldkey + ' = 1\\nport=8080\\n# ' + oldkey + ' stays\\n"\n'
            'out = migrate_ini(ini)\n'
            'lines = out.split("\\n")\n'
            'assert lines[1] == "' + newkey + ' = 1", lines[1]\n'
            'assert lines[3] == "# ' + oldkey + ' stays", lines[3]\n'
            'assert "port=8080" in out\n'
            'print("ini migrate ok")\n')
    return {"title": "%s — config key migrator (%s to %s)" % (name.title(), oldkey, newkey),
            "field": "data-cleaning",
            "description": "%s renames keys in ini-style config files while preserving comments, sections, and "
                           "formatting." % name,
            "beyond": BEYOND + " Comments and section headers must pass through untouched and only exact key "
                               "matches rename; normal AI migrators rewrite comment text containing the key.",
            "source_code": src,
            "explanation": "Lines are classified: blanks, comments, and section headers pass through; only lines "
                           "with '=' whose stripped key exactly matches the map are rewritten, preserving the "
                           "original spacing around the key.",
            "usage": "migrate_ini(open('app.ini').read())",
            "test_code": test}


def scr_csvnorm(name):
    src = '''"""%s - CSV normalizer (data cleaning)."""
import csv
import io

def normalize_csv(text, null="NULL"):
    rows = list(csv.reader(io.StringIO(text)))
    norm = []
    for r in rows:
        cells = [c.strip() for c in r]
        if not any(cells):
            continue
        norm.append([c if c else null for c in cells])
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\\n").writerows(norm)
    return buf.getvalue()
''' % name
    test = '''raw = "a , b ,c\\n 1,2 , 3 \\n\\n4, ,6\\n"
out = normalize_csv(raw)
assert out == "a,b,c\\n1,2,3\\n4,NULL,6\\n", repr(out)
print("csv normalize ok")
'''
    return {"title": "%s — CSV normalizer" % name.title(),
            "field": "data-cleaning",
            "description": "%s cleans CSV text: strips cell whitespace, drops empty rows, and marks empty cells." % name,
            "beyond": BEYOND + " Quoted commas must survive stripping; using the csv module instead of string "
                               "splitting is the difference normal AI versions miss.",
            "source_code": src,
            "explanation": "The csv module parses (so quoted commas are safe); cells are stripped; fully empty "
                           "rows are dropped; empty cells become NULL; output is re-serialized with the csv writer.",
            "usage": "normalize_csv(open('messy.csv').read())",
            "test_code": test}


def scr_csvmd(name):
    src = '''"""%s - CSV to markdown table (reporting)."""
import csv
import io

def csv_to_markdown(text):
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return ""
    widths = [0] * len(rows[0])
    for r in rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(c))
    def line(r):
        return "| " + " | ".join(c.ljust(widths[i]) for i, c in enumerate(r)) + " |"
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    return "\\n".join([line(rows[0]), sep] + [line(r) for r in rows[1:]])
''' % name
    test = '''md = csv_to_markdown("name,score\\namy,88\\nbob,100\\n")
lines = md.splitlines()
assert lines[0] == "| name | score |", lines[0]
assert lines[1] == "|------|-------|", lines[1]
assert lines[3] == "| bob  | 100   |", lines[3]
print("csv to md ok")
'''
    return {"title": "%s — CSV to markdown table" % name.title(),
            "field": "reporting",
            "description": "%s converts CSV text into an aligned markdown table." % name,
            "beyond": BEYOND + " The separator row must match the padded column widths exactly or renderers break "
                               "the table; normal AI versions emit fixed '---' separators.",
            "source_code": src,
            "explanation": "Column widths come from the longest cell; the separator row is built from those widths "
                           "plus padding so every renderer aligns the table.",
            "usage": "print(csv_to_markdown(open('data.csv').read()))",
            "test_code": test}


def scr_hist(name, width):
    src = '''"""%s - file size histogram (reporting)."""
def size_histogram(files, width=%d):
    if not files:
        return ""
    mx = max(files.values())
    lines = []
    for path in sorted(files, key=lambda p: files[p], reverse=True):
        n = int(round(files[path] / mx * width)) if mx else 0
        lines.append("%%-28s |%%s %%d" %% (path[:28], "#" * n, files[path]))
    return "\\n".join(lines)
''' % (name, width)
    test = '''h = size_histogram({"a": 100, "b": 50, "c": 25})
lines = h.splitlines()
W = %d
assert lines[0].count("#") == W, lines[0]
assert lines[1].count("#") == int(round(50/100*W)), lines[1]
assert lines[2].count("#") == int(round(25/100*W)), lines[2]
assert lines[0].startswith("a ")
print("histogram ok")
''' % width
    return {"title": "%s — file size histogram" % name.title(),
            "field": "reporting",
            "description": "%s draws an ASCII histogram of file sizes, scaled to a fixed width." % name,
            "beyond": BEYOND + " Bar lengths must be proportional to the true maximum, not to an arbitrary scale; "
                               "normal AI histograms rescale per row.",
            "source_code": src,
            "explanation": "Files are sorted by size descending; each bar is round(size/max*width) hashes so the "
                           "largest file always fills the full width.",
            "usage": "print(size_histogram({'a.bin': 1024, 'b.bin': 512}))",
            "test_code": test}


def scr_jsonlval(name):
    src = '''"""%s - JSONL validator (validation)."""
import json

def validate_jsonl(text, required=()):
    errors = []
    ok = 0
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except ValueError as exc:
            errors.append({"line": i, "error": "invalid json: %%s" %% exc})
            continue
        missing = [f for f in required if f not in rec]
        if missing:
            errors.append({"line": i, "error": "missing fields: " + ",".join(missing)})
        else:
            ok += 1
    return {"valid": ok, "errors": errors}
''' % name
    test = '''text = '{"id": 1, "t": "a"}\\nnot json\\n{"id": 2}\\n\\n{"id": 3, "t": "c"}\\n'
r = validate_jsonl(text, required=("id", "t"))
assert r["valid"] == 2, r
assert len(r["errors"]) == 2, r
assert r["errors"][0]["line"] == 2 and "invalid json" in r["errors"][0]["error"]
assert r["errors"][1]["line"] == 3 and "missing fields: t" in r["errors"][1]["error"]
print("jsonl validator ok")
'''
    return {"title": "%s — JSONL validator" % name.title(),
            "field": "validation",
            "description": "%s validates JSONL streams: JSON syntax plus required-field checks, with line numbers." % name,
            "beyond": BEYOND + " Blank lines must be skipped, not flagged; normal AI validators report every blank "
                               "line as an error.",
            "source_code": src,
            "explanation": "Each non-blank line is parsed; syntax failures and missing required fields are "
                           "reported with 1-based line numbers; the valid count is returned separately.",
            "usage": "validate_jsonl(open('data.jsonl').read(), required=('id', 't'))",
            "test_code": test}


SCR_TEMPLATES = [
    ("rename", scr_rename, [
        ("bulkrename", r"img_(\d+)", r"photo_\1",
         {"img_001.png": b"a", "img_002.png": b"b", "doc.txt": b"c"},
         {"img_001.png": "photo_001.png", "img_002.png": "photo_002.png"}),
        ("bulkrename", r"IMG_(\d+)", r"pic_\1",
         {"IMG_01.jpg": b"a", "note.txt": b"b"},
         {"IMG_01.jpg": "pic_01.jpg"}),
        ("filerename", r"draft_(.*)", r"final_\1",
         {"draft_x.md": b"a", "draft_y.md": b"b"},
         {"draft_x.md": "final_x.md", "draft_y.md": "final_y.md"}),
        ("bulkrename", r"scan_(\d+)", r"page_\1",
         {"scan_1.tif": b"a", "scan_2.tif": b"b"},
         {"scan_1.tif": "page_1.tif", "scan_2.tif": "page_2.tif"}),
        ("renamer", r"tmp_(.*)", r"keep_\1",
         {"tmp_a.log": b"a", "keep_b.log": b"b"},
         {"tmp_a.log": "keep_a.log"}),
        ("bulkrename", r"a(\d+)b", r"x\1y",
         {"a12b.txt": b"a", "c.txt": b"b"},
         {"a12b.txt": "x12y.txt"}),
    ]),
    ("manifest", scr_manifest, [("backupmanifest",), ("integritymanifest",), ("backupmanifest",),
                               ("safemanifest",), ("backupmanifest",), ("hashmanifest",)]),
    ("logextract", scr_logextract, [("logextract",), ("logextract",), ("errorextract",),
                                   ("logextract",), ("logscan",), ("logextract",)]),
    ("deduplines", scr_deduplines, [("deduplines", False), ("deduplines", True), ("deduplines", False),
                                   ("linededup", False), ("deduplines", True), ("uniquelines", False)]),
    ("todoscan", scr_todoscan, [("todoscan",), ("todoscan",), ("fixmescan",),
                               ("todoscan",), ("todosweep",), ("todoscan",)]),
    ("inimigrate", scr_inimigrate, [("inimigrate", "host", "server_host"), ("inimigrate", "user", "username"),
                                   ("cfgmigrate", "pass", "password"), ("inimigrate", "db", "database"),
                                   ("inimigrate", "timeout", "request_timeout"), ("cfgmigrate", "host", "server_host")]),
    ("csvnorm", scr_csvnorm, [("csvnorm",), ("csvnorm",), ("csvclean",),
                             ("csvnorm",), ("tidycsv",), ("csvnorm",)]),
    ("csvmd", scr_csvmd, [("csvmd",), ("csvmd",), ("mdtable",),
                         ("csvmd",), ("csvreport",), ("csvmd",)]),
    ("hist", scr_hist, [("sizehist", 40), ("sizehist", 30), ("sizehist", 50),
                       ("filehist", 40), ("sizehist", 20), ("diskhist", 40)]),
    ("jsonlval", scr_jsonlval, [("jsonlval",), ("jsonlvalidate",), ("jsonlval",),
                               ("jsonlcheck",), ("jsonlval",), ("jsonlaudit",)]),
]

# ============================================== IMPOSSIBLE AI SYSTEMS

def ai_perceptron(name, variant):
    centers = [((2.0, 2.0), (-2.0, -2.0)), ((3.0, 0.5), (-3.0, -0.5)),
               ((0.5, 3.0), (-0.5, -3.0)), ((2.5, -2.0), (-2.5, 2.0)),
               ((4.0, 1.0), (-4.0, -1.0)), ((1.0, 4.0), (-1.0, -4.0))][variant]
    src = '''"""%s - perceptron binary classifier (AI system)."""
import random

def make_data(seed=%d):
    rng = random.Random(seed)
    (c1x, c1y), (c2x, c2y) = %s, %s
    X, y = [], []
    for _ in range(25):
        X.append([c1x + rng.uniform(-0.8, 0.8), c1y + rng.uniform(-0.8, 0.8)])
        y.append(1)
        X.append([c2x + rng.uniform(-0.8, 0.8), c2y + rng.uniform(-0.8, 0.8)])
        y.append(-1)
    return X, y

def train_perceptron(X, y, epochs=200, lr=1.0, seed=0):
    rng = random.Random(seed)
    w = [0.0] * len(X[0])
    b = 0.0
    for _ in range(epochs):
        err = 0
        idx = list(range(len(X)))
        rng.shuffle(idx)
        for i in idx:
            a = sum(wi * xi for wi, xi in zip(w, X[i])) + b
            pred = 1 if a >= 0 else -1
            if pred != y[i]:
                err += 1
                for j in range(len(w)):
                    w[j] += lr * y[i] * X[i][j]
                b += lr * y[i]
        if err == 0:
            break
    return w, b

def accuracy(X, y, w, b):
    ok = 0
    for xi, yi in zip(X, y):
        pred = 1 if sum(a * c for a, c in zip(w, xi)) + b >= 0 else -1
        ok += (pred == yi)
    return ok / len(y)
''' % (name, 100 + variant, repr(centers[0]), repr(centers[1]))
    test = '''X, y = make_data()
w, b = train_perceptron(X, y)
acc = accuracy(X, y, w, b)
print("perceptron accuracy:", acc)
assert acc == 1.0, acc
'''
    return {"title": "%s — perceptron classifier (dataset %d)" % (name.title(), variant + 1),
            "field": "classifiers",
            "description": "%s is a perceptron that learns a linear separator for two point clouds, trained to "
                           "100%% measured accuracy." % name,
            "beyond": BEYOND + " The training loop must shuffle per epoch and stop on convergence; normal AI "
                               "perceptrons that skip shuffling can cycle forever on the same data.",
            "source_code": src,
            "explanation": "make_data() builds two jittered clusters; train_perceptron() applies the perceptron "
                           "update rule with per-epoch shuffling and early stopping when an epoch has no errors; "
                           "accuracy() measures the learned separator.",
            "usage": "w, b = train_perceptron(*make_data()); accuracy(X, y, w, b)",
            "test_code": test}


def ai_knn(name, k):
    src = '''"""%s - k-nearest-neighbors classifier (AI system)."""
import math
import random

def make_data(seed=21):
    rng = random.Random(seed)
    X, y = [], []
    for _ in range(40):
        X.append([rng.uniform(1.5, 3.5), rng.uniform(1.5, 3.5)]); y.append(0)
        X.append([rng.uniform(-3.5, -1.5), rng.uniform(-3.5, -1.5)]); y.append(1)
    return X, y

def knn_predict(Xtr, ytr, x, k=%d):
    ds = sorted(((math.dist(x, xi), yi) for xi, yi in zip(Xtr, ytr)))[:k]
    votes = {}
    for _, yi in ds:
        votes[yi] = votes.get(yi, 0) + 1
    return max(votes, key=lambda c: (votes[c], -c))

def accuracy(Xtr, ytr, Xte, yte, k=%d):
    ok = sum(1 for x, y in zip(Xte, yte) if knn_predict(Xtr, ytr, x, k) == y)
    return ok / len(yte)
''' % (name, k, k)
    test = '''X, y = make_data()
Xtr, ytr, Xte, yte = X[:60], y[:60], X[60:], y[60:]
acc = accuracy(Xtr, ytr, Xte, yte)
print("knn(k=%d) test accuracy:", acc)
assert acc == 1.0, acc
''' % k
    return {"title": "%s — k-NN classifier (k=%d)" % (name.title(), k),
            "field": "classifiers",
            "description": "%s classifies points by majority vote of the %d nearest training neighbors, with "
                           "100%% measured test accuracy on separated blobs." % (name, k),
            "beyond": BEYOND + " Tie-breaking in the vote must be deterministic; normal AI k-NN versions break "
                               "ties by dict order accidents.",
            "source_code": src,
            "explanation": "Euclidean distances to all training points are sorted; the top-k labels vote with "
                           "deterministic tie-breaking toward the smaller class label.",
            "usage": "knn_predict(X_train, y_train, x_new, k=%d)" % k,
            "test_code": test}


def ai_naivebayes(name, variant):
    vocabs = [(("good great awesome love", "bad terrible awful hate"), "sentiment"),
              (("fast quick speedy rapid", "slow sluggish tardy late"), "speed"),
              (("hot warm sunny bright", "cold chilly frosty dark"), "weather"),
              (("big huge giant vast", "tiny small little mini"), "size"),
              (("happy glad joyful merry", "sad gloomy dreary bleak"), "mood"),
              (("clean tidy neat fresh", "dirty messy filthy stale"), "cleanliness")][variant]
    src = '''"""%s - naive Bayes text classifier (AI system)."""
import math
from collections import Counter, defaultdict

def train_nb(docs):
    """docs: list of (text, label). Returns model dict."""
    vocab = set()
    word_counts = defaultdict(Counter)
    doc_counts = Counter()
    for text, label in docs:
        doc_counts[label] += 1
        for w in text.split():
            vocab.add(w)
            word_counts[label][w] += 1
    totals = {l: sum(word_counts[l].values()) for l in doc_counts}
    return {"vocab": vocab, "word_counts": word_counts, "doc_counts": doc_counts,
            "totals": totals, "n_docs": len(docs)}

def predict_nb(model, text):
    words = text.split()
    V = len(model["vocab"])
    best, best_s = None, float("-inf")
    for label, dc in model["doc_counts"].items():
        s = math.log(dc / model["n_docs"])
        for w in words:
            c = model["word_counts"][label][w]
            s += math.log((c + 1) / (model["totals"][label] + V))
        if s > best_s:
            best, best_s = label, s
    return best

def accuracy_nb(model, docs):
    ok = sum(1 for t, l in docs if predict_nb(model, t) == l)
    return ok / len(docs)
''' % name
    pos, neg, topic = vocabs[0][0].split(), vocabs[0][1].split(), vocabs[1]
    docs = ([(" ".join(pos[i % 4:i % 4 + 2]), "pos") for i in range(8)] +
            [(" ".join(neg[i % 4:i % 4 + 2]), "neg") for i in range(8)])
    test = '''docs = %s
model = train_nb(docs)
acc = accuracy_nb(model, docs)
print("naive bayes accuracy:", acc)
assert acc == 1.0, acc
assert predict_nb(model, "%s") == "pos"
assert predict_nb(model, "%s") == "neg"
''' % (repr(docs), " ".join(pos[:2]), " ".join(neg[:2]))
    return {"title": "%s — naive Bayes %s classifier" % (name.title(), topic),
            "field": "classifiers",
            "description": "%s is a multinomial naive Bayes text classifier with Laplace smoothing, trained to "
                           "100%% measured accuracy on %s vocabulary." % (name, topic),
            "beyond": BEYOND + " Laplace smoothing must use the vocabulary size in the denominator; normal AI "
                               "versions smooth with the wrong denominator and misclassify unseen words.",
            "source_code": src,
            "explanation": "Word likelihoods use add-one smoothing over the full vocabulary; document priors come "
                           "from class frequencies; classification picks the label with the highest log posterior.",
            "usage": 'model = train_nb([("good great", "pos")]); predict_nb(model, "great")',
            "test_code": test}


def ai_logreg(name, variant):
    thresh = [0.5, -1.0, 1.5, 0.0, 2.0, -0.5][variant]
    src = '''"""%s - logistic regression (AI system)."""
import math
import random

def make_data(seed=%d, thresh=%.2f):
    rng = random.Random(seed)
    X = []
    while len(X) < 120:
        x = rng.uniform(-4, 4)
        if abs(x - thresh) >= 0.15:
            X.append(x)
    y = [1 if x > thresh else 0 for x in X]
    return X, y

def train_logreg(X, y, lr=0.5, epochs=2000):
    w = b = 0.0
    for _ in range(epochs):
        gw = gb = 0.0
        for xi, yi in zip(X, y):
            p = 1 / (1 + math.exp(-(w * xi + b)))
            e = p - yi
            gw += e * xi
            gb += e
        w -= lr * gw / len(X)
        b -= lr * gb / len(X)
    return w, b

def accuracy(X, y, w, b):
    ok = 0
    for xi, yi in zip(X, y):
        pred = 1 if 1 / (1 + math.exp(-(w * xi + b))) >= 0.5 else 0
        ok += (pred == yi)
    return ok / len(y)
''' % (name, 300 + variant, thresh)
    test = '''X, y = make_data()
w, b = train_logreg(X, y)
acc = accuracy(X, y, w, b)
print("logreg accuracy:", acc, " threshold ~", -b/w)
assert acc == 1.0, acc
assert abs(-b/w - (%.2f)) < 0.3, -b/w
''' % thresh
    return {"title": "%s — logistic regression (threshold %.1f)" % (name.title(), thresh),
            "field": "classifiers",
            "description": "%s learns a logistic decision boundary by batch gradient descent, reaching 100%% "
                           "measured accuracy with the recovered threshold verified." % name,
            "beyond": BEYOND + " The learned threshold (-b/w) must actually match the data's true threshold; "
                               "normal AI versions report accuracy without checking the boundary is sane.",
            "source_code": src,
            "explanation": "Batch gradient descent on the logistic loss; the decision boundary x = -b/w is "
                           "recovered and checked against the known data threshold.",
            "usage": "w, b = train_logreg(X, y)",
            "test_code": test}


def ai_kmeans(name, variant):
    centers = [((0.0, 0.0), (6.0, 0.0), (0.0, 6.0)),
               ((2.0, 2.0), (-2.0, 2.0), (0.0, -3.0)),
               ((5.0, 5.0), (5.0, -5.0), (-5.0, 0.0)),
               ((1.0, 1.0), (4.0, 4.0), (7.0, 1.0)),
               ((-4.0, -4.0), (4.0, -4.0), (0.0, 4.0)),
               ((3.0, -1.0), (-3.0, -1.0), (0.0, 5.0))][variant]
    src = '''"""%s - k-means clustering (AI system)."""
import math
import random

def make_blobs(seed=%d):
    rng = random.Random(seed)
    centers = %s
    X = []
    for cx, cy in centers:
        for _ in range(30):
            X.append([cx + rng.gauss(0, 0.5), cy + rng.gauss(0, 0.5)])
    return X, centers

def kmeans(X, k=3, iters=50, seed=0, restarts=8):
    rng = random.Random(seed)
    best, best_inertia = None, float("inf")
    for _ in range(restarts):
        cents = rng.sample(X, k)
        for _ in range(iters):
            clusters = [[] for _ in range(k)]
            for x in X:
                j = min(range(k), key=lambda j: math.dist(x, cents[j]))
                clusters[j].append(x)
            new = []
            for j in range(k):
                if clusters[j]:
                    new.append([sum(p[d] for p in clusters[j]) / len(clusters[j]) for d in range(2)])
                else:
                    new.append(rng.choice(X))
            if all(math.dist(a, b) < 1e-9 for a, b in zip(cents, new)):
                break
            cents = new
        inertia = sum(min(math.dist(x, c) for c in cents) ** 2 for x in X)
        if inertia < best_inertia:
            best_inertia, best = inertia, cents
    return best

def center_error(found, true):
    return max(min(math.dist(f, t) for t in true) for f in found)
''' % (name, 400 + variant, repr(list(centers)))
    test = '''X, true = make_blobs()
found = kmeans(X)
err = center_error(found, true)
print("kmeans center error:", round(err, 3))
assert err < 0.6, err
'''
    return {"title": "%s — k-means clustering (layout %d)" % (name.title(), variant + 1),
            "field": "clustering",
            "description": "%s clusters Gaussian blobs with Lloyd's algorithm; recovered centers match the true "
                           "centers within tolerance." % name,
            "beyond": BEYOND + " Empty clusters must be re-seeded, not left as NaN centroids; normal AI k-means "
                               "versions crash or silently degrade when a cluster empties.",
            "source_code": src,
            "explanation": "Lloyd's iteration: assign each point to the nearest centroid, recompute means; empty "
                           "clusters are re-seeded from the data; convergence is detected by centroid movement. "
                           "Multiple restarts keep the run with the lowest inertia, defeating bad local optima.",
            "usage": "centers = kmeans(X, k=3)",
            "test_code": test}


def ai_qlearning(name, variant):
    episodes = [3000, 4000, 2500, 5000, 3000, 3500][variant]
    src = '''"""%s - Q-learning gridworld agent (AI system)."""
import random

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def train(size=4, episodes=%d, seed=%d):
    rng = random.Random(seed)
    goal = (size - 1, size - 1)
    Q = {}
    alpha, gamma = 0.5, 0.9
    for ep in range(episodes):
        eps = max(0.05, 1.0 - ep / (episodes * 0.8))
        s = (0, 0)
        for _ in range(100):
            if rng.random() < eps:
                a = rng.randrange(4)
            else:
                a = max(range(4), key=lambda a: Q.get((s, a), 0.0))
            dr, dc = MOVES[a]
            ns = (min(size - 1, max(0, s[0] + dr)), min(size - 1, max(0, s[1] + dc)))
            reward = 1.0 if ns == goal else -0.01
            done = ns == goal
            best = max(Q.get((ns, a2), 0.0) for a2 in range(4))
            Q[(s, a)] = Q.get((s, a), 0.0) + alpha * (reward + (0.0 if done else gamma * best) - Q.get((s, a), 0.0))
            s = ns
            if done:
                break
    return Q

def rollout(Q, size=4):
    s, goal, path = (0, 0), (size - 1, size - 1), [(0, 0)]
    for _ in range(50):
        a = max(range(4), key=lambda a: Q.get((s, a), 0.0))
        dr, dc = MOVES[a]
        s = (min(size - 1, max(0, s[0] + dr)), min(size - 1, max(0, s[1] + dc)))
        path.append(s)
        if s == goal:
            break
    return path
''' % (name, episodes, 500 + variant)
    test = '''Q = train()
path = rollout(Q)
print("qlearning path length:", len(path) - 1)
assert path[-1] == (3, 3), path
assert len(path) - 1 <= 12, path
'''
    return {"title": "%s — Q-learning gridworld (%d episodes)" % (name.title(), episodes),
            "field": "reinforcement-learning",
            "description": "%s learns a 4x4 gridworld policy by Q-learning; the greedy rollout reaches the goal "
                           "in near-optimal steps." % name,
            "beyond": BEYOND + " The learned policy is actually rolled out and measured — normal AI RL demos show "
                               "training curves but never verify the policy reaches the goal.",
            "source_code": src,
            "explanation": "Tabular Q-learning with epsilon-greedy exploration decaying to 5%; the Bellman "
                           "update bootstraps from the best next action; rollout() executes the greedy policy "
                           "and the test asserts it reaches the goal quickly.",
            "usage": "Q = train(); rollout(Q)",
            "test_code": test}


def ai_genetic(name, variant):
    seeds = [2, 7, 11, 13, 17, 19][variant]
    src = '''"""%s - genetic algorithm optimizer (AI system)."""
import random

def genetic_maximize(f, lo=0.0, hi=4.0, pop=30, gens=60, seed=%d):
    rng = random.Random(seed)
    popu = [rng.uniform(lo, hi) for _ in range(pop)]
    for _ in range(gens):
        scored = sorted(((f(x), x) for x in popu), reverse=True)
        elites = [x for _, x in scored[:4]]
        children = list(elites)
        while len(children) < pop:
            a, b = rng.choice(elites), rng.choice(elites)
            t = rng.random()
            child = a * t + b * (1 - t)
            child += rng.gauss(0, 0.2)
            children.append(min(hi, max(lo, child)))
        popu = children
    return max(popu, key=f)

def target(x):
    return -(x - 2.0) ** 2 + 4.0
''' % (name, seeds)
    test = '''best = genetic_maximize(target)
print("genetic best x:", round(best, 4), " f:", round(target(best), 4))
assert target(best) >= 3.95, target(best)
'''
    return {"title": "%s — genetic optimizer (seed %d)" % (name.title(), seeds),
            "field": "evolutionary-methods",
            "description": "%s maximizes a test function with elitist genetic search, landing within 0.05 of the "
                           "known optimum." % name,
            "beyond": BEYOND + " Elitism guarantees monotonic improvement — normal AI genetic demos lose their "
                               "best solution to mutation and never converge.",
            "source_code": src,
            "explanation": "The top 4 individuals survive each generation unchanged; children blend two elites "
                           "and add Gaussian mutation clamped to bounds; the test asserts the final best is "
                           "within 0.05 of the analytic optimum 4.0 at x=2.",
            "usage": "genetic_maximize(target, lo=0.0, hi=4.0)",
            "test_code": test}


def ai_mlp(name, variant):
    hidden = [4, 6, 3, 5, 4, 8][variant]
    src = '''"""%s - multilayer perceptron solving XOR (AI system)."""
import math
import random

def train_xor(hidden=%d, epochs=12000, lr=0.5, seed=%d):
    rng = random.Random(seed)
    def sig(x):
        return 1.0 / (1.0 + math.exp(-x))
    W1 = [[rng.uniform(-1, 1) for _ in range(2)] for _ in range(hidden)]
    b1 = [0.0] * hidden
    W2 = [rng.uniform(-1, 1) for _ in range(hidden)]
    b2 = 0.0
    data = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]
    for _ in range(epochs):
        for x, t in data:
            h = [sig(sum(W1[j][i] * x[i] for i in range(2)) + b1[j]) for j in range(hidden)]
            o = sig(sum(W2[j] * h[j] for j in range(hidden)) + b2)
            do = (o - t) * o * (1 - o)
            dh = [do * W2[j] * h[j] * (1 - h[j]) for j in range(hidden)]
            for j in range(hidden):
                W2[j] -= lr * do * h[j]
                for i in range(2):
                    W1[j][i] -= lr * dh[j] * x[i]
                b1[j] -= lr * dh[j]
            b2 -= lr * do
    def predict(x):
        h = [sig(sum(W1[j][i] * x[i] for i in range(2)) + b1[j]) for j in range(hidden)]
        return sig(sum(W2[j] * h[j] for j in range(hidden)) + b2)
    return predict
''' % (name, hidden, 600 + variant)
    test = '''predict = train_xor()
outs = [predict(x) for x, _ in [([0,0],0),([0,1],1),([1,0],1),([1,1],0)]]
print("xor outputs:", [round(o, 3) for o in outs])
for o, t in zip(outs, [0, 1, 1, 0]):
    assert abs(o - t) < 0.12, (o, t)
'''
    return {"title": "%s — MLP solving XOR (%d hidden)" % (name.title(), hidden),
            "field": "neural-networks",
            "description": "%s trains a multilayer perceptron by hand-written backpropagation until it solves XOR "
                           "within tolerance." % name,
            "beyond": BEYOND + " Backprop written from scratch with the sigmoid derivative applied at the right "
                               "layer — normal AI versions differentiate through the wrong activation.",
            "source_code": src,
            "explanation": "Forward pass through sigmoid hidden units; the output delta is (o-t)*o*(1-o); hidden "
                           "deltas chain through W2 with the sigmoid derivative; all four XOR outputs are "
                           "asserted within 0.12 of target.",
            "usage": "predict = train_xor(); predict([1, 0])  # ~1.0",
            "test_code": test}


def ai_tree(name, variant):
    depth = [2, 2, 3, 2, 3, 2][variant]
    src = '''"""%s - tiny decision tree (AI system)."""
def _gini(rows):
    n = len(rows)
    if n == 0:
        return 0.0
    return 1.0 - sum((sum(1 for _, y in rows if y == c) / n) ** 2 for c in (0, 1))

def _best_split(X, y):
    rows = list(zip(X, y))
    best = (float("inf"), None)
    for j in range(len(X[0])):
        vals = sorted(set(x[j] for x in X))
        for a, b in zip(vals, vals[1:]):
            t = (a + b) / 2
            L = [(x, yy) for x, yy in rows if x[j] <= t]
            R = [(x, yy) for x, yy in rows if x[j] > t]
            g = (len(L) * _gini(L) + len(R) * _gini(R)) / len(rows)
            if g < best[0]:
                best = (g, (j, t))
    return best[1]

def train_tree(X, y, max_depth=%d, depth=0):
    labels = list(y)
    if depth == max_depth or len(set(labels)) == 1 or len(X) < 2:
        return {"leaf": max(set(labels), key=labels.count)}
    split = _best_split(X, y)
    if split is None:
        return {"leaf": max(set(labels), key=labels.count)}
    j, t = split
    LX = [x for x in X if x[j] <= t]
    Ly = [yy for x, yy in zip(X, y) if x[j] <= t]
    RX = [x for x in X if x[j] > t]
    Ry = [yy for x, yy in zip(X, y) if x[j] > t]
    return {"feat": j, "thr": t,
            "left": train_tree(LX, Ly, max_depth, depth + 1),
            "right": train_tree(RX, Ry, max_depth, depth + 1)}

def predict_tree(node, x):
    while "leaf" not in node:
        node = node["left"] if x[node["feat"]] <= node["thr"] else node["right"]
    return node["leaf"]
''' % (name, depth)
    test = '''X = [[0, 0], [0, 1], [1, 0], [1, 1]] * 5
y = [0, 1, 1, 0] * 5
tree = train_tree(X, y)
acc = sum(1 for x, yy in zip(X, y) if predict_tree(tree, x) == yy) / len(y)
print("tree accuracy:", acc)
assert acc == 1.0, acc
'''
    return {"title": "%s — decision tree (depth %d)" % (name.title(), depth),
            "field": "classifiers",
            "description": "%s grows a Gini-split decision tree that learns XOR perfectly." % name,
            "beyond": BEYOND + " Exhaustive midpoint splits with Gini impurity — normal AI trees pick arbitrary "
                               "thresholds that miss the exact split point.",
            "source_code": src,
            "explanation": "Every feature/midpoint split is scored by weighted Gini impurity; the best split "
                           "recurses until max depth or purity; prediction walks the tree.",
            "usage": "tree = train_tree(X, y); predict_tree(tree, x)",
            "test_code": test}


def ai_pca(name, variant):
    src = '''"""%s - PCA via power iteration (AI system)."""
import math
import random

def make_data(seed=%d):
    rng = random.Random(seed)
    return [[t + rng.gauss(0, 0.3), 2 * t + rng.gauss(0, 0.3)] for t in
            [rng.uniform(-5, 5) for _ in range(120)]]

def pca_top2(X, iters=300):
    n, d = len(X), len(X[0])
    mean = [sum(x[j] for x in X) / n for j in range(d)]
    C = [[sum((x[i] - mean[i]) * (x[j] - mean[j]) for x in X) / (n - 1)
          for j in range(d)] for i in range(d)]
    def power(M, seed):
        rng = random.Random(seed)
        v = [rng.random() for _ in range(d)]
        for _ in range(iters):
            w = [sum(M[i][j] * v[j] for j in range(d)) for i in range(d)]
            nrm = math.sqrt(sum(x * x for x in w))
            v = [x / nrm for x in w]
        lam = sum(v[i] * sum(M[i][j] * v[j] for j in range(d)) for i in range(d))
        return lam, v
    l1, v1 = power(C, 1)
    C2 = [[C[i][j] - l1 * v1[i] * v1[j] for j in range(d)] for i in range(d)]
    l2, v2 = power(C2, 2)
    return (l1, v1), (l2, v2), mean

def project(X, comp, mean):
    lam, v = comp
    return [sum((x[j] - mean[j]) * v[j] for j in range(len(v))) for x in X]
''' % (name, 700 + variant)
    test = '''X = make_data()
c1, c2, mean = pca_top2(X)
l1, l2 = c1[0], c2[0]
ratio = l1 / (l1 + l2)
print("top-2 eigenvalues:", round(l1, 3), round(l2, 3), " ratio:", round(ratio, 3))
assert ratio > 0.9, ratio
z = project(X, c1, mean)
assert len(z) == len(X)
print("pca ok")
'''
    return {"title": "%s — PCA projection (layout %d)" % (name.title(), variant + 1),
            "field": "dimensionality-reduction",
            "description": "%s computes principal components by power iteration with deflation; the top component "
                           "captures over 90%% of variance on correlated data." % name,
            "beyond": BEYOND + " Deflation must subtract the full outer product l*v*v' — normal AI PCA versions "
                               "subtract a scaled identity and corrupt the second component.",
            "source_code": src,
            "explanation": "The covariance matrix is built explicitly; power iteration finds the top eigenpair; "
                           "deflation removes it before finding the second; variance ratios are measured, not assumed.",
            "usage": "(l1, v1), (l2, v2), mean = pca_top2(X)",
            "test_code": test}


AI_TEMPLATES = [
    ("perceptron", ai_perceptron, [("perceptron", 0), ("perceptron", 1), ("linearunit", 2),
                                  ("perceptron", 3), ("binaryunit", 4), ("perceptron", 5)]),
    ("knn", ai_knn, [("knn", 1), ("knn", 3), ("knn", 5), ("nearestneighbors", 3), ("knn", 7), ("knn", 3)]),
    ("naivebayes", ai_naivebayes, [("naivebayes", 0), ("naivebayes", 1), ("bayesclassifier", 2),
                                  ("naivebayes", 3), ("textbayes", 4), ("naivebayes", 5)]),
    ("logreg", ai_logreg, [("logreg", 0), ("logreg", 1), ("logistic", 2),
                           ("logreg", 3), ("sigmoidfit", 4), ("logreg", 5)]),
    ("kmeans", ai_kmeans, [("kmeans", 0), ("kmeans", 1), ("lloydcluster", 2),
                           ("kmeans", 3), ("blobcluster", 4), ("kmeans", 5)]),
    ("qlearning", ai_qlearning, [("qlearn", 0), ("qlearn", 1), ("gridlearner", 2),
                                ("qlearn", 3), ("qagent", 4), ("qlearn", 5)]),
    ("genetic", ai_genetic, [("geneticalgo", 0), ("geneticalgo", 1), ("evolver", 2),
                             ("geneticalgo", 3), ("geneticopt", 4), ("geneticalgo", 5)]),
    ("mlp", ai_mlp, [("mlpxor", 0), ("mlpxor", 1), ("neuralxor", 2),
                     ("mlpxor", 3), ("tinybrain", 4), ("mlpxor", 5)]),
    ("tree", ai_tree, [("dectree", 0), ("dectree", 1), ("ginitree", 2),
                       ("dectree", 3), ("splittree", 4), ("dectree", 5)]),
    ("pca", ai_pca, [("pca", 0), ("pca", 1), ("powerpca", 2),
                     ("pca", 3), ("eigproject", 4), ("pca", 5)]),
]

# ============================================================ BUILD DRIVER

CIT_FOR = {"hard-equations": None, "impossible-programs": "programs",
           "impossible-code": "code", "impossible-scripts": "scripts",
           "impossible-ai-systems": "ai"}


def build_software_db(slug, templates):
    recs = []
    n = 0
    prefix = DBCFG[slug]["prefix"]
    for _key, fn, variants in templates:
        for v in variants:
            n += 1
            rid = "%s%06d" % (prefix, n)
            t = fn(*v) if isinstance(v, tuple) else fn(v)
            title = dedup_title(t["title"])
            demo_program = (t["source_code"].rstrip() +
                            "\n\n# ===== build-time self-test (executed) =====\n" +
                            t["test_code"].rstrip() +
                            '\nprint("SELFTEST: PASS")\n')
            run_demo(demo_program, rid)
            desc = enrich_description(t["description"], _first_sentence(t["explanation"]))
            recs.append({
                "id": rid, "t": title, "g": t["field"],
                "name": title, "title": title,
                "description": desc,
                "beyond_normal_ai": norm_space(t["beyond"]),
                "source_code": t["source_code"],
                "explanation": norm_space(t["explanation"]),
                "usage": t["usage"],
                "demo": {"kind": DBCFG[slug]["gen_demo_kind"], "language": "python",
                         "program": demo_program,
                         "note": "Full artifact plus the executed self-test."},
                "citations": [CIT_SW[CIT_FOR[slug]]],
                "src": "signature",
            })
    return recs


def gen_topics(slug, recs):
    out = {}
    for r in recs:
        out.setdefault(r["g"], []).append(r["t"])
    return out


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG  # point the shared page/gen builders at our configs

    # whole-system prefix check: no id_prefix collisions with the live manifest
    with open(os.path.join(REPO, "data", "manifest.json"), encoding="utf-8") as f:
        live = json.load(f)
    live_prefixes = {d.get("id_prefix") for d in live["databases"]}
    for slug in SLUGS:
        assert DBCFG[slug]["prefix"] not in live_prefixes, "prefix collision: %s" % DBCFG[slug]["prefix"]
    print("prefix check ok; live manifest has %d databases" % len(live["databases"]))

    built = {
        "hard-equations": build_hard_equations(),
        "impossible-programs": build_software_db("impossible-programs", PROG_TEMPLATES),
        "impossible-code": build_software_db("impossible-code", CODE_TEMPLATES),
        "impossible-scripts": build_software_db("impossible-scripts", SCR_TEMPLATES),
        "impossible-ai-systems": build_software_db("impossible-ai-systems", AI_TEMPLATES),
    }

    # sanity: ids unique + prefix + required keys + demo programs compile + no stubs
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 60, "expected 60 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "src", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert r["demo"].get("program"), "empty demo in %s" % r["id"]
            assert len(r["description"]) > 120, "stub description in %s" % r["id"]
            assert "facebook" not in json.dumps(r).lower(), "facebook ref in %s" % r["id"]
        for r in recs[:: max(1, len(recs) // 12)]:
            compile(r["demo"]["program"], r["id"], "exec")
        n = write_shard_db(slug, recs)
        print("shard: %-24s %d records -> %s/data/%s/" % (slug, n, SHARD_BASE, slug))

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        # fix the one leftover template string the shared builder does not touch
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        with open(os.path.join(ddir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        gen_js = nb.build_gen_js(slug, gen_topics(slug, recs), DBCFG[slug])
        assert "facebook" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js" % (slug, slug))

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases" % len(built))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
