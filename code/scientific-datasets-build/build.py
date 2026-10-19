#!/usr/bin/env python3
"""Build the Scientific Datasets pair for JAH Databases (gap-audit part 2).

Verified 2026-10-17: manifest search found NO database covering scientific
datasets as raw observations (original measurements, experimental conditions,
formats, processing histories). Nearest neighbors: 'scientific-computing'
(computation methods, not datasets), 'scientific-instruments-public'
(instruments), 'scientific-method' (method), 'metrology-measurement-databases'
(a 10-record catalog OF databases, not measurement data). Whole-system title
sweep: dataset terms hit only incidental study-corpus items. ZERO full-record
coverage of the dataset discipline itself.

Two NEW databases, 34 ladder-ordered records each:
  scientific-datasets            - The Scientific Datasets Database (public-harvest)
  scientific-datasets-signature  - The Scientific Datasets Signature Database (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_scientific_datasets import ENTRIES

RK = "scientific dataset record"
CIT_PUB = ("Scientific datasets (standard references: Wilkinson et al. 'The FAIR Guiding "
           "Principles for scientific data management and stewardship' Scientific Data 2016; "
           "Bevington & Robinson 'Data Reduction and Error Analysis for the Physical Sciences' "
           "3rd ed. 2003; NIST/SEMATECH e-Handbook of Statistical Methods; JCGM 100:2008 "
           "(GUM) 'Evaluation of measurement data - Guide to the expression of uncertainty in "
           "measurement'; Unidata NetCDF; The HDF Group HDF5; DataCite Metadata Schema; "
           "Peng 'Reproducible Research in Computational Science' Science 2011; ISO 8601 "
           "date/time; W3C PROV data provenance model).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of dataset science."

STANDARDS = ["Documented dataset practice per the cited references",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="scientific-datasets", name_base="Scientific Datasets",
    tagline=("Raw scientific observations: original measurements, experimental conditions, "
             "storage formats, and full processing histories - what a dataset is, how honest "
             "measurements are recorded, and how data stays trustworthy from instrument to "
             "archive, taught progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-SCID-", prefix_sig="JAH-SCIDS-",
    ai_base="JAH Dataset Archivist",
    role_pub=("scientific dataset archivist - raw observations, measurements, experimental "
              "conditions, formats, metadata, processing histories; teaching progressively "
              "along the ladder from foundations through compounded to advanced; answers from "
              "many angles - definition, example, procedure, math, standards - using only the "
              "system's own archive data"),
    role_sig=("scientific dataset archivist - Signature editions: his original Signature "
              "treatment of dataset science, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search calibration, uncertainty, NetCDF, FAIR, provenance, sampling...",
    chat_ph="Ask about scientific datasets...",
    archive_topic="scientific-dataset records",
    gen_kind="scientific-dataset",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked dataset science: what a dataset is, "
              "measurement basics, experimental conditions, sampling, formats (CSV, NetCDF, "
              "HDF5), metadata, lab notebooks, calibration records, uncertainty, time series, "
              "replication, cleaning, controlled experiments, field data, sensor networks, "
              "surveys, imaging, spectra, sequence reads, climate records, catalogs, event "
              "data, pipelines, versioning, provenance, FAIR, design of experiments, missing "
              "data, fusion, propagation, reproducibility, archiving, simulated data, and "
              "publication - organized in the Signature system. Every record carries the full "
              "entry: description, how it works, key points, requirements, standards, "
              "citations, and a working demonstration program. Records are ordered by the "
              "teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of dataset science: the "
              "full ladder from what a dataset is through measurement, formats, pipelines, "
              "and provenance to FAIR publication, reframed as Signature science. Clearly "
              "labeled Signature-made, never presented as authentic public record. Every "
              "record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


@_reg("ds_mean")
def d_mean(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math, statistics
def main():
    # ten repeat readings of a 10.00 cm standard (cm)
    readings = [10.02, 9.98, 10.01, 10.03, 9.99, 10.00, 10.02, 9.97, 10.01, 10.00]
    n = len(readings)
    mean = statistics.mean(readings)
    sd = statistics.stdev(readings)          # sample standard deviation
    se = sd / math.sqrt(n)                   # standard error of the mean
    print("n=%d mean=%.4f cm sd=%.4f cm se=%.4f cm" % (n, mean, sd, se))
    print("reported: %.3f +/- %.3f cm (mean +/- standard error)" % (mean, se))
    assert abs(mean - 10.003) < 1e-9, mean
    assert abs(sd - 0.01897) < 1e-4, sd
    assert se < sd, "standard error must be smaller than sd"
    print("OK: %s summarized repeat measurements honestly" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_calfit")
def d_calfit(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # calibration: known masses (g) vs sensor reading (mV)
    xs = [0.0, 50.0, 100.0, 150.0, 200.0]
    ys = [2.1, 51.8, 102.3, 151.9, 202.4]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    a = my - b * mx
    ss_tot = sum((y - my) ** 2 for y in ys)
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    r2 = 1.0 - ss_res / ss_tot
    print("fit: reading = %.4f + %.4f * mass; R^2 = %.6f" % (a, b, r2))
    pred = a + b * 125.0
    print("125 g unknown -> predicted reading %.1f mV" % pred)
    assert abs(b - 1.0012) < 1e-3, b
    assert r2 > 0.9999, r2
    print("OK: %s fitted a real calibration line" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_errprop")
def d_errprop(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # density = mass / volume, independent uncertainties combined in quadrature
    m, um = 50.00, 0.05      # g
    v, uv = 20.0, 0.2        # cm^3
    rho = m / v
    u_rho = rho * math.sqrt((um / m) ** 2 + (uv / v) ** 2)
    print("density = %.3f g/cm^3 +/- %.4f g/cm^3" % (rho, u_rho))
    assert abs(rho - 2.5) < 1e-9
    assert abs(u_rho - 0.02512) < 1e-4, u_rho
    print("OK: %s propagated uncertainty in quadrature" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_sample")
def d_sample(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # standard error shrinks as 1/sqrt(n): how many readings for se <= 0.01?
    sd = 0.10
    target = 0.01
    n_needed = math.ceil((sd / target) ** 2)
    print("sd=%.2f target se=%.2f -> need n >= %d readings" % (sd, target, n_needed))
    for n in (10, 100, 400):
        print("  n=%3d -> se=%.4f" % (n, sd / math.sqrt(n)))
    assert n_needed == 100
    print("OK: %s sized the sample from the 1/sqrt(n) law" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_checksum")
def d_checksum(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import hashlib
def main():
    # a checksum manifest: filename -> sha256, then a fixity re-check
    payloads = {
        "run_001.csv": "t,reading\\n0,1.02\\n1,1.05\\n",
        "run_002.csv": "t,reading\\n0,0.98\\n1,1.01\\n",
        "notes.txt": "calibrated 2026-10-01 against JAH mass set\\n",
    }
    manifest = {fn: hashlib.sha256(data.encode()).hexdigest() for fn, data in payloads.items()}
    print("manifest (%d files):" % len(manifest))
    for fn, hx in sorted(manifest.items()):
        print("  %s  %s..." % (hx[:16], fn))
    # fixity re-check: recompute and compare
    bad = [fn for fn, data in payloads.items()
           if hashlib.sha256(data.encode()).hexdigest() != manifest[fn]]
    assert not bad, bad
    # tamper one file -> manifest catches it
    tampered = payloads["run_001.csv"] + "x"
    assert hashlib.sha256(tampered.encode()).hexdigest() != manifest["run_001.csv"]
    print("fixity check: all %d files verified; tamper detected" % len(manifest))
    print("OK: %s built and verified a checksum manifest" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_csv")
def d_csv(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import csv, io, statistics
def main():
    text = ("sample_id,temperature_C,pressure_kPa\\n"
            "A1,21.5,101.3\\nA2,22.1,101.1\\nA3,21.8,101.4\\nA4,22.4,101.2\\n")
    rows = list(csv.DictReader(io.StringIO(text)))
    temps = [float(r["temperature_C"]) for r in rows]
    press = [float(r["pressure_kPa"]) for r in rows]
    print("rows=%d temp mean=%.2f C (sd %.3f) pressure mean=%.2f kPa" % (
        len(rows), statistics.mean(temps), statistics.stdev(temps), statistics.mean(press)))
    assert len(rows) == 4
    assert abs(statistics.mean(temps) - 21.95) < 1e-9
    print("OK: %s parsed a real CSV and summarized columns" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_outlier")
def d_outlier(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import statistics
def main():
    # Tukey IQR fences: flag points outside [Q1-1.5 IQR, Q3+1.5 IQR] for review
    data = [10.1, 10.3, 9.9, 10.2, 10.0, 10.4, 9.8, 10.2, 15.7, 10.1]
    qs = statistics.quantiles(data, n=4)
    q1, q3 = qs[0], qs[2]
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    flagged = [x for x in data if x < lo or x > hi]
    print("Q1=%.2f Q3=%.2f IQR=%.2f fences=[%.2f, %.2f]" % (q1, q3, iqr, lo, hi))
    print("flagged for review (NOT silently deleted): %s" % flagged)
    assert flagged == [15.7], flagged
    print("OK: %s flagged outliers with Tukey fences" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_units")
def d_units(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # unit conversions a dataset pipeline performs (factors exact by definition)
    conv = [
        ("in->mm", 2.54, 1.0),
        ("lb->kg", 0.45359237, 1.0),
        ("psi->kPa", 6.894757, 1.0),
        ("degF->degC", None, 68.0),  # special: (F-32)*5/9
    ]
    results = {}
    results["in->mm"] = 12.0 * 25.4
    results["lb->kg"] = 150.0 * 0.45359237
    results["psi->kPa"] = 14.7 * 6.894757
    results["degF->degC"] = (68.0 - 32.0) * 5.0 / 9.0
    for k, v in results.items():
        print("  %s = %.4f" % (k, v))
    assert abs(results["in->mm"] - 304.8) < 1e-9
    assert abs(results["lb->kg"] - 68.0389) < 1e-3
    assert abs(results["psi->kPa"] - 101.353) < 1e-2
    assert abs(results["degF->degC"] - 20.0) < 1e-9
    print("OK: %s converted units with exact defined factors" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_timeseries")
def d_timeseries(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import datetime, statistics
def main():
    # hourly temperature readings -> daily means (a real resampling step)
    base = datetime.datetime(2026, 10, 1, 0, 0)
    hours = [(base + datetime.timedelta(hours=h),
              15.0 + 5.0 * __import__("math").sin(2 * 3.14159 * h / 24.0)) for h in range(48)]
    days = {}
    for ts, val in hours:
        days.setdefault(ts.date(), []).append(val)
    for day in sorted(days):
        vals = days[day]
        print("  %s: n=%d mean=%.2f C min=%.2f max=%.2f" % (
            day, len(vals), statistics.mean(vals), min(vals), max(vals)))
    assert len(days) == 2 and all(len(v) == 24 for v in days.values())
    assert abs(statistics.mean(days[sorted(days)[0]]) - 15.0) < 0.05
    print("OK: %s resampled an hourly series to daily means" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_version")
def d_version(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import hashlib, json
def main():
    # dataset versioning: immutable snapshot id = hash of sorted manifest
    files = {"run_001.csv": "abc123", "run_002.csv": "def456", "meta.json": "7890ab"}
    canon = json.dumps(files, sort_keys=True, separators=(",", ":"))
    snap = hashlib.sha256(canon.encode()).hexdigest()[:12]
    version = "v2.3.0+%s" % snap
    doi = "10.5281/jah.scid.%s" % snap
    print("snapshot: %s  doi: %s" % (version, doi))
    assert version.startswith("v2.3.0+") and len(snap) == 12
    # same files -> same snapshot (immutable, reproducible)
    assert hashlib.sha256(canon.encode()).hexdigest()[:12] == snap
    print("OK: %s minted an immutable dataset version" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_uncert")
def d_uncert(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math, statistics
def main():
    # GUM-style: Type A (repeatability) + Type B (calibration certificate) combined
    readings = [10.02, 9.98, 10.01, 10.03, 9.99, 10.00, 10.02, 9.97, 10.01, 10.00]
    u_a = statistics.stdev(readings) / math.sqrt(len(readings))   # Type A
    u_b = 0.010 / math.sqrt(3)                                     # Type B: +/-0.010 rectangular
    u_c = math.sqrt(u_a ** 2 + u_b ** 2)                           # combined standard
    U = 2.0 * u_c                                                  # expanded, k=2 (~95%)
    print("uA=%.4f uB=%.4f uc=%.4f U(k=2)=%.4f" % (u_a, u_b, u_c, U))
    assert abs(u_c - 0.00827) < 1e-4, u_c
    print("OK: %s combined Type A and Type B uncertainty (GUM)" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("ds_fair")
def d_fair(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # FAIR checklist: 15 guiding principles scored present/missing
    principles = ["F1 identifier", "F2 rich metadata", "F3 identifier in metadata",
                  "F4 indexed registry", "A1 retrievable protocol", "A1.1 open protocol",
                  "A1.2 auth where needed", "A2 metadata persists", "I1 formal language",
                  "I2 FAIR vocabularies", "I3 qualified references", "R1 plural attributes",
                  "R1.1 clear license", "R1.2 detailed provenance", "R1.3 community standards"]
    present = {"F1 identifier", "F2 rich metadata", "A1 retrievable protocol",
               "A1.1 open protocol", "R1.1 clear license", "R1.2 detailed provenance"}
    score = sum(1 for p in principles if p in present)
    print("FAIR: %d/%d principles satisfied" % (score, len(principles)))
    missing = [p for p in principles if p not in present]
    print("missing: %s" % "; ".join(missing[:5]) + (" ..." if len(missing) > 5 else ""))
    assert score == 6 and len(principles) == 15
    print("OK: %s scored a dataset against the FAIR principles" % ''' + __import__('json').dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
