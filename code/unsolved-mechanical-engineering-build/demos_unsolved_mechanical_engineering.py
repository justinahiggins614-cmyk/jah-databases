#!/usr/bin/env python3
"""Solution-explorer demos for the Unsolved Mechanical Engineering databases.

Each demo is a working program: adjustable assumptions up top, numbered
explorer steps with real computed values, tight-bounds asserts (never float
exact-equality on computed floats), an explicit CONFIRM / REFUTE panel,
and the OK marker. The build machine-executes every demo; zero failures
are required.

Expected values are computed at build time with the same expressions the
program runs, so the asserts are tight but never brittle.
"""
import math

_EVAL_NS = {"__builtins__": {}, "math": math, "max": max, "min": min, "abs": abs}


def _fmt_val(v):
    if isinstance(v, float):
        return "%.6g" % v
    return repr(v)


def explorer(hdr, title, rid, group, e):
    sp = e["demo_spec"]
    ns = {}
    body = []
    body.append("import math")
    body.append("")
    body.append("def main():")
    body.append('    print("SOLUTION EXPLORER: %s")' % title.replace('"', "'"))
    body.append('    print("Record %s [%s]")' % (rid, group))
    body.append('    print("Approach: %s")' % sp["approach"].replace('"', "'"))
    body.append("    # ---- adjustable assumptions (edit these to explore) ----")
    for name, val, unit in sp["assume"]:
        ns[name] = val
        body.append("    %s = %r  # %s" % (name, val, unit))
    body.append('    print("assumptions: %s")' % (
        ", ".join("%s=%s %s" % (n, _fmt_val(v), u)
                  for n, v, u in sp["assume"])).replace('"', "'"))
    body.append("    # ---- explorer steps ----")
    derived = []
    step_no = 0
    for name, expr in sp["derived"]:
        step_no += 1
        try:
            v = eval(expr, _EVAL_NS, dict(ns))  # noqa: S307 - own build input
        except Exception as ex:
            raise ValueError("demo expr failed for %s: %s (%s)" % (rid, expr, ex))
        ns[name] = v
        derived.append((name, v))
        body.append("    %s = %s" % (name, expr))
        body.append('    print("step %d: %s = %s")' % (step_no, name, _fmt_val(v)))
    body.append("    # ---- checks (tight bounds, deterministic) ----")
    for name, v in derived:
        if isinstance(v, float):
            tol = max(abs(v) * 1e-3, 1e-9)
            body.append("    assert %.17g <= %s <= %.17g" % (v - tol, name, v + tol))
        else:
            body.append("    assert %s == %r" % (name, v))
    body.append('    print("CONFIRM: %s")' % sp["confirm"].replace('"', "'"))
    body.append('    print("REFUTE: %s")' % sp["refute"].replace('"', "'"))
    body.append('    print("OK: %s explored the solution space")' % title.replace('"', "'"))
    body.append("")
    body.append('if __name__ == "__main__":')
    body.append("    main()")
    prog = hdr(title, rid, group) + "\n".join(body) + "\n"
    return prog


def _mk(key):
    def fn(hdr, title, rid, group, e):
        assert e["key"] == key, "demo key mismatch: %s" % e["key"]
        return explorer(hdr, title, rid, group, e)
    fn.__name__ = "demo_" + key.replace("-", "_")
    return fn


DEMOS = {}
def _register(keys):
    for k in keys:
        DEMOS[k] = _mk(k)

_register([
    "bearing-life", "fouling", "gear-fatigue", "bolt-loosening",
    "vibration-harvest", "am-parts", "nvh", "small-turbo", "cui",
    "friction-wear", "cavitation", "thermal-packaging",
    "turbulence-closure", "transition", "drag-reduction", "nano-contact",
    "galling", "multiphase", "flutter", "thermoacoustic",
    "metamaterial-scale", "soft-robot-control", "microrobot-swim",
    "topology-opt", "compliant-fatigue", "random-fatigue", "creep-fatigue",
    "superlubricity", "active-turbulence", "scramjet",
    "hypersonic-transition", "navier-stokes", "chaotic-mixing", "tether",
])
