#!/usr/bin/env python3
"""Demo programs for the Unsolved Biology databases (Manon's 16:15 orders, batch 1).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only Python that
walks through the Signature solution approach with adjustable assumptions, prints real
computed values, runs a confirm/refute panel, asserts tight bounds (never float
exact-equality), and ends with the OK marker. All 68 are machine-executed by build.py.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_usb_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: sleep as the brain's nightly audit (ledger reconciliation).
    # ADJUSTABLE ASSUMPTIONS: rise/decay time constants of sleep pressure S.
    tau_rise, tau_fall = 18.2, 4.2   # hours; try 12.0/3.0 for a faster ledger
    wake_h, sleep_h = 16.0, 8.0
    s = 0.15                          # pressure at yesterday's wake
    s_bed = 1.0 - (1.0 - s) * math.exp(-wake_h / tau_rise)
    s_morn = s_bed * math.exp(-sleep_h / tau_fall)
    print("step 1 - ledger posts debits all day: pressure at bedtime S = %.4f" % s_bed)
    print("step 2 - audit settles the books overnight: pressure at wake S = %.4f" % s_morn)
    print("step 3 - cognition tracks the ledger: high S predicts errors, low S predicts clarity")
    assert 0.64 < s_bed < 0.66, s_bed
    assert 0.09 < s_morn < 0.11, s_morn
    print("CONFIRM panel: find a ledger variable (synaptic weight, metabolite) rising in wake,")
    print("  falling in sleep, predicting performance better than hours slept.")
    print("REFUTE panel: full cognition with zero sleep and no compensating mechanism.")
    print("OK: %s walked the audit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_dream(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: dreams as the overnight test suite (adversarial edge-case sampling).
    # ADJUSTABLE ASSUMPTIONS: cycle length and per-cycle REM minutes.
    night_min = 8.0 * 60.0
    cycle_min = 90.0
    rem_bouts = [10.0, 20.0, 25.0, 30.0, 35.0]  # REM grows across the night
    n_cycles = night_min / cycle_min
    total_rem = sum(rem_bouts)
    rem_pct = total_rem / night_min * 100.0
    print("step 1 - audit closes the books: %d sleep cycles of %.0f min" % (len(rem_bouts), cycle_min))
    print("step 2 - test suite runs: REM minutes per night = %.0f (%.2f %%)" % (total_rem, rem_pct))
    print("step 3 - edge cases dominate: threat/social scenarios are the historically lethal failures")
    assert total_rem == 120.0
    assert 24.9 < rem_pct < 25.1, rem_pct
    assert 5.3 < n_cycles < 5.4, n_cycles
    print("CONFIRM panel: dream content tracks the dreamer's recent prediction errors, not random replay.")
    print("REFUTE panel: dreams are pure replay with no novel recombination, or dream loss costs nothing.")
    print("OK: %s ran the test suite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_memory(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: memory as multi-signed contracts (systems re-signing across substrates).
    # ADJUSTABLE ASSUMPTIONS: initial strength S and the review schedule.
    import math
    reviews = [1.0, 3.0, 7.0, 15.0]   # days; each success doubles strength (re-signing)
    S, last = 1.0, 0.0
    for r in reviews:
        recall = math.exp(-(r - last) / S)   # strength at review time
        assert recall > 0.30, "contract lapsed before re-signing"
        S *= 2.0                              # countersignature: hippocampus -> cortex
        last = r
    final_day = 30.0
    r_trained = math.exp(-(final_day - last) / S)
    r_naive = math.exp(-final_day / 1.0)      # no re-signing: single fragile signature
    print("step 1 - hippocampus signs first: strength S = 1.0, fragile")
    print("step 2 - sleep countersigns on schedule %s: S doubles each time -> S = %.0f" % (reviews, S))
    print("step 3 - day-30 recall with re-signing: %.4f; without: %.2e" % (r_trained, r_naive))
    assert 0.39 < r_trained < 0.40, r_trained
    assert r_naive < 1e-6, r_naive
    print("CONFIRM panel: one memory's substrate migrating across systems on a re-signing schedule.")
    print("REFUTE panel: years-long memory with zero systems-level substrate change.")
    print("OK: %s renewed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_pain(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: chronic pain as a stuck gain-control loop (missing stand-down order).
    # ADJUSTABLE ASSUMPTIONS: gain rise during injury, reset rate after healing.
    gain, pain_threshold, touch = 1.0, 0.7, 0.5
    gain += 0.08 * 10.0          # injury: 10 days of deliberate gain increase
    print("step 1 - injury raises the alarm gain: gain = %.2f" % gain)
    perceived_stuck = touch * gain          # reset signal never arrived
    gain_reset = gain - 0.05 * 20.0         # healthy stand-down: 20 days of reset
    perceived_reset = touch * max(gain_reset, 1.0)
    print("step 2 - stuck loop: gentle touch %.1f x gain %.2f = %.2f %s threshold %.1f -> PAIN" %
          (touch, gain, perceived_stuck, ">", pain_threshold))
    print("step 3 - reset loop: gain back to %.2f -> perception %.2f, below threshold" %
          (max(gain_reset, 1.0), perceived_reset))
    assert 0.89 < perceived_stuck < 0.91, perceived_stuck
    assert perceived_stuck > pain_threshold > perceived_reset
    print("CONFIRM panel: a gain variable predicting who transitions from acute to chronic pain.")
    print("REFUTE panel: chronic pain with provably normal gain at every level of the neuraxis.")
    print("OK: %s found the missing stand-down" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_aging(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: aging as a repair-budget deficit (Gompertz mortality ledger).
    # ADJUSTABLE ASSUMPTIONS: baseline hazard a and aging rate b.
    a, b = 0.0002, 0.08664          # b = ln(2)/8: hazard doubles every ~8 years
    mu = lambda t: a * math.exp(b * t)
    ratio = mu(80.0) / mu(30.0)     # 50 years of compounding arrears
    doubling = math.log(2.0) / b
    print("step 1 - daily damage posts to 12 ledgers; repair budget covers it while young")
    print("step 2 - hazard at 30: %.5f/yr; at 80: %.4f/yr; ratio = %.2f" % (mu(30.0), mu(80.0), ratio))
    print("step 3 - mortality doubling time: %.3f years" % doubling)
    assert 75.0 < ratio < 77.0, ratio
    assert 7.99 < doubling < 8.01, doubling
    print("CONFIRM panel: one unrepaired-damage metric predicting mortality better than age,")
    print("  moving coherently with every lifespan-extending intervention.")
    print("REFUTE panel: a hallmark progressing independently of all others and of repair budget.")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_lifespan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: lifespan as a maintenance contract priced by predation.
    # ADJUSTABLE ASSUMPTIONS: allometric exponent and the mouse calibration point.
    exp = 0.25
    c = 2.0 / (0.025 ** exp)          # calibrate: 25 g mouse lives ~2 years
    mouse = c * (0.025 ** exp)
    whale = c * (100000.0 ** exp)     # 100-ton bowhead: what the curve alone predicts
    print("step 1 - contract length follows mass^%.2f: mouse %.2f yr" % (exp, mouse))
    print("step 2 - curve predicts whale %.1f yr; real bowheads exceed 200 yr" % whale)
    print("step 3 - the surplus is insurance: duplicated repair genes, extra p53 - the premium")
    assert 1.99 < mouse < 2.01, mouse
    assert 89.0 < whale < 90.0, whale
    assert whale < 200.0, "curve alone cannot price the whale's contract"
    print("CONFIRM panel: repair investment tracking extrinsic mortality better than body mass alone.")
    print("REFUTE panel: a high-predation species with lavish repair redundancy.")
    print("OK: %s priced the contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_regeneration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: regeneration as a race between sealing (scar) and rebuilding (blastema).
    # ADJUSTABLE ASSUMPTIONS: target cell count, starting cells, doubling time, scar deadline.
    target, start, dbl_h = 1e8, 1e4, 24.0
    doublings = math.log2(target / start)
    days_needed = doublings * dbl_h / 24.0
    scar_deadline_days = 2.0          # mammalian fibroblasts seal the wound fast
    cells_by_deadline = start * 2.0 ** (scar_deadline_days * 24.0 / dbl_h)
    print("step 1 - rebuilding contract needs %.2f doublings = %.2f days" % (doublings, days_needed))
    print("step 2 - scarring contract seals in %.0f days with only %.0e cells built" %
          (scar_deadline_days, cells_by_deadline))
    print("step 3 - salamander wins the slow race; mammal takes the fast seal (infection deadline)")
    assert 13.2 < doublings < 13.4, doublings
    assert 13.2 < days_needed < 13.4, days_needed
    assert cells_by_deadline < target / 1000.0
    print("CONFIRM panel: sequential mammalian protocol (delay scar, retune macrophages, pattern)")
    print("  yielding jointed regrowth instead of scar.")
    print("REFUTE panel: mammalian limb regrowth with full aggressive scarring left intact.")
    print("OK: %s timed the race" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_immunity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: immunity as calibrated coincidence detection (no single trusted signal).
    # ADJUSTABLE ASSUMPTIONS: per-sensor false-alarm/detection rates, sensors, votes needed.
    n, k = 5, 3                       # 5 sensors, need >= 3 agreeing alarms
    p_fp, p_det = 0.05, 0.80
    def binom(n_, k_, p_):
        return math.comb(n_, k_) * (p_ ** k_) * ((1.0 - p_) ** (n_ - k_))
    fp = sum(binom(n, j, p_fp) for j in range(k, n + 1))
    det = sum(binom(n, j, p_det) for j in range(k, n + 1))
    print("step 1 - one signal, one guard: false-alarm rate %.3f (shoots citizens)" % p_fp)
    print("step 2 - coincidence of %d sensors needing %d votes: false alarms %.5f" % (n, k, fp))
    print("step 3 - true detection stays high: %.4f - the border holds" % det)
    assert 0.94 < det < 0.945, det
    assert 0.0011 < fp < 0.0012, fp
    assert fp < p_fp / 40.0
    print("CONFIRM panel: per-tissue thresholds drifting before autoimmune onset.")
    print("REFUTE panel: a single signal proven to decide attack vs tolerance alone.")
    print("OK: %s calibrated the border" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_cellfate(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: cell fate as a toggle-switch attractor with chromatin padlocks.
    # ADJUSTABLE ASSUMPTIONS: feedback strength a; noise would tilt the switch.
    a = 3.0
    x, y = 0.1, 0.5                   # noisy signal tilts the switch off the ridge
    for _ in range(500):              # let the circuit settle (developmental time)
        x = a / (1.0 + y * y)
        y = a / (1.0 + x * x)
    # symmetric fixed point (the undecided ridge): solve s^3 + s - a = 0 by bisection
    # (plain iteration diverges here: the ridge fixed point is repelling)
    lo, hi = 1.0, 1.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if mid ** 3 + mid - a > 0.0:
            hi = mid
        else:
            lo = mid
    s = 0.5 * (lo + hi)
    print("step 1 - toggle circuit settles: X = %.4f (ON), Y = %.4f (OFF)" % (x, y))
    print("step 2 - undecided ridge at %.4f: unstable, the ball rolls off" % s)
    print("step 3 - chromatin padlocks the loser shut: Yamanaka must pick the locks in reverse")
    assert x > 2.5 and y < 0.45, (x, y)
    assert 1.20 < s < 1.23, s
    assert abs(x - a / (1.0 + y * y)) < 1e-9
    print("CONFIRM panel: reprogramming difficulty predicted from chromatin-lock inventory.")
    print("REFUTE panel: fate held with zero chromatin change.")
    print("OK: %s flipped the switch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_embryo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: embryos build by error-corrected consensus (French flag + averaging).
    # ADJUSTABLE ASSUMPTIONS: gradient length scale, thresholds, neighborhood size.
    lam, C0 = 100.0, 1.0               # microns
    T1, T2 = 0.60, 0.25                # blue/white/red thresholds
    x1 = -lam * math.log(T1 / C0)
    x2 = -lam * math.log(T2 / C0)
    sigma_single, N = 20.0, 25.0       # single-cell readout noise, neighbors consulted
    sigma_hood = sigma_single / math.sqrt(N)
    print("step 1 - one witness guesses: boundary at %.2f um, noise +/- %.0f um" % (x1, sigma_single))
    print("step 2 - %d neighbors compare notes: noise falls to +/- %.2f um" % (N, sigma_hood))
    print("step 3 - three flags: blue|x<%.2f|white|x<%.2f|red" % (x1, x2))
    assert 51.0 < x1 < 51.2, x1
    assert 138.5 < x2 < 138.8, x2
    assert 3.9 < sigma_hood < 4.1, sigma_hood
    print("CONFIRM panel: final pattern exactly as accurate as averaging math predicts.")
    print("REFUTE panel: embryonic precision with provably no cell-cell averaging.")
    print("OK: %s read the flag" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_microbiome(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the microbiome as a treaty ecosystem (terms, not just taxa).
    # ADJUSTABLE ASSUMPTIONS: competition coefficients; healthy treaty vs broken treaty.
    def equilibrium(c):
        # Lotka-Volterra coexistence: 1 - x - c*y = 0, 1 - y - c*x = 0
        return 1.0 / (1.0 + c), 1.0 / (1.0 + c)
    x_h, y_h = equilibrium(0.5)        # healthy treaty: moderate competition
    print("step 1 - healthy treaty terms (competition 0.5): species settle at %.4f, %.4f" % (x_h, y_h))
    # treaty breaks: antibiotics raise competition/stress -> new worse equilibrium
    x_b, y_b = equilibrium(1.5)        # still positive? 1/2.5 = 0.4: coexistence but degraded
    print("step 2 - broken treaty (stress 1.5): degraded equilibrium %.4f, %.4f" % (x_b, y_b))
    print("step 3 - fecal transplant re-signs the original treaty wholesale")
    assert 0.66 < x_h < 0.67 and 0.66 < y_h < 0.67, (x_h, y_h)
    assert x_b < x_h, "broken treaty must be the worse equilibrium"
    print("CONFIRM panel: specific treaty terms breaking before disease onset, longitudinally.")
    print("REFUTE panel: disease with fully healthy treaty terms by every measure.")
    print("OK: %s kept the treaty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_pregnancy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: pregnancy as a locally negotiated, hormonally expiring treaty.
    # ADJUSTABLE ASSUMPTIONS: attack strength, Treg/Teff ratios per jurisdiction.
    attack = 1.0
    r_tissue, r_decidua = 0.3, 2.5     # regulatory-to-effector ratios
    margin_tissue = r_tissue - 1.0      # negative: attack proceeds (infections cleared)
    margin_decidua = r_decidua - 1.0    # positive: treaty holds
    print("step 1 - ordinary tissue: regulation ratio %.1f, margin %+.1f -> defense active" %
          (r_tissue, margin_tissue))
    print("step 2 - placenta jurisdiction: ratio %.1f, margin %+.1f -> truce holds" %
          (r_decidua, margin_decidua))
    print("step 3 - labor hormones dissolve the jurisdiction on schedule; tolerance expires")
    assert margin_tissue < 0.0 < margin_decidua
    assert 1.4 < margin_decidua < 1.6, margin_decidua
    print("CONFIRM panel: first-trimester treaty metrics predicting preeclampsia.")
    print("REFUTE panel: rejection-free pregnancy with no local regulatory specialization.")
    print("OK: %s honored the nine-month treaty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_cancer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: cancer as defection from the multicellular contract (multistage).
    # ADJUSTABLE ASSUMPTIONS: number of required enforcement failures (hits).
    hits = 6
    k = 0.01 / (60.0 ** hits)          # calibrate: 1% incidence by age 60
    i60 = k * 60.0 ** hits
    i40 = k * 40.0 ** hits
    ratio = i60 / i40                  # == (60/40)^6: the price of compounding defections
    print("step 1 - one defection is suppressed: enforcement holds at every layer")
    print("step 2 - %d layered failures compound: incidence 40yr %.2e, 60yr %.2e" % (hits, i40, i60))
    print("step 3 - age ratio %.2f: cancer is enforcement failing on schedule" % ratio)
    assert 11.3 < ratio < 11.5, ratio
    assert 0.0099 < i60 < 0.0101, i60
    print("CONFIRM panel: enforcement-strengthening cutting incidence without touching mutation rates.")
    print("REFUTE panel: cancers arising with provably intact enforcement at every layer.")
    print("OK: %s policed the contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_rejuvenation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: rejuvenation as timed epigenetic re-authentication (dosing problem).
    # ADJUSTABLE ASSUMPTIONS: re-filing efficiency and oncogenic price per dose.
    eff, onc = 12.0, 0.8               # years restored per full dose; oncogenic exponent
    dose = 0.5
    years_back = dose * eff
    risk_mult = math.exp(dose * onc)   # cancer risk multiplier
    print("step 1 - pulse the Yamanaka factors at dose %.1f: %.1f years re-filed" % (dose, years_back))
    print("step 2 - oncogenic price: risk x %.3f (must stay < 1.5)" % risk_mult)
    print("step 3 - the window: re-file enough to matter, stop before pluripotency")
    assert 5.9 < years_back < 6.1, years_back
    assert 1.48 < risk_mult < 1.50, risk_mult
    full = math.exp(1.0 * onc)
    assert full > 2.2, "full dose must be oncogenic: the window is real"
    print("CONFIRM panel: multi-tissue restoration with zero increased lifetime tumors.")
    print("REFUTE panel: rejuvenation always carrying proportional cancer risk at any dose.")
    print("OK: %s timed the re-signing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_consciousness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: consciousness as the brain's self-authentication (integration proxy).
    # ADJUSTABLE ASSUMPTIONS: none structural - compare integrated vs feedforward wiring.
    # proxy: I = H(parts) - H(whole): information the whole generates above its parts
    h_part = 1.0                       # each binary node: 1 bit
    h_whole_integrated = 1.0           # Y = X: the pair carries 1 bit jointly
    h_whole_feedforward = 2.0          # independent: the pair carries 2 bits, no unity
    phi_proxy_integrated = 2.0 * h_part - h_whole_integrated
    phi_proxy_feedforward = 2.0 * h_part - h_whole_feedforward
    print("step 1 - integrated pair: parts 2 bits, whole 1 bit -> unity %.2f bit" % phi_proxy_integrated)
    print("step 2 - feedforward pair: parts 2 bits, whole 2 bits -> unity %.2f bit" % phi_proxy_feedforward)
    print("step 3 - the self-model needs unity: broadcast without integration is a press release")
    assert 0.99 < phi_proxy_integrated < 1.01, phi_proxy_integrated
    assert -0.01 < phi_proxy_feedforward < 0.01, phi_proxy_feedforward
    print("CONFIRM panel: disrupting self-modeling circuitry alone abolishing reportable experience.")
    print("REFUTE panel: full reportable consciousness with no self-modeling circuitry active.")
    print("note: the hard problem - why unity feels like anything - is NOT claimed solved.")
    print("OK: %s authenticated the witness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_neuralcode(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the neural code as a multiplexed protocol stack (LIF reader model).
    # ADJUSTABLE ASSUMPTIONS: membrane time constant, threshold, input currents.
    tau, vth, vreset = 0.020, 1.0, 0.0   # 20 ms reader
    def rate(I):
        ri = I  # R = 1
        if ri <= vth:
            return 0.0
        return 1.0 / (tau * math.log(ri / (ri - vth)))
    f_sub = rate(1.0)     # at threshold: silence
    f_mid = rate(1.5)     # moderate drive
    f_high = rate(2.0)    # strong drive
    print("step 1 - timing layer: fast readers catch spike coincidences the rate misses")
    print("step 2 - rate layer: I=1.5 -> %.2f Hz; I=2.0 -> %.2f Hz" % (f_mid, f_high))
    print("step 3 - population layer: the manifold is the vote made visible")
    assert f_sub == 0.0
    assert 45.4 < f_mid < 45.6, f_mid
    assert 72.0 < f_high < 72.2, f_high
    print("CONFIRM panel: one spike train, different effects when a reader's time constant changes.")
    print("REFUTE panel: a behavior using one coding layer across all deadline changes.")
    print("OK: %s read the multiplex" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_folding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: folding as hierarchical collapse with annealing rescue.
    # ADJUSTABLE ASSUMPTIONS: attempt rate, folding barrier, trap depth (kcal/mol).
    k0, RT = 1e6, 0.6
    barrier_fold, barrier_trap = 8.0, 12.0
    t_fold = 1.0 / (k0 * math.exp(-barrier_fold / RT))
    t_escape = 1.0 / (k0 * math.exp(-barrier_trap / RT))
    print("step 1 - local structures form first (microseconds): the cheap decisions")
    print("step 2 - global docking: folding time %.4f s down the funnel" % t_fold)
    print("step 3 - wrong valley: escape takes %.1f s; chaperones shake the puzzle (anneal)" % t_escape)
    assert 0.60 < t_fold < 0.64, t_fold
    assert 480.0 < t_escape < 490.0, t_escape
    assert t_escape > t_fold * 700.0, "traps must be deep to cause disease"
    print("CONFIRM panel: time-resolved folding showing local-before-global hierarchy.")
    print("REFUTE panel: global-before-local folding as the general rule.")
    print("OK: %s slid down the funnel" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "sleep": demo_usb_sleep,
 "dream": demo_usb_dream,
 "memory": demo_usb_memory,
 "pain": demo_usb_pain,
 "aging": demo_usb_aging,
 "lifespan": demo_usb_lifespan,
 "regeneration": demo_usb_regeneration,
 "immunity": demo_usb_immunity,
 "cellfate": demo_usb_cellfate,
 "embryo": demo_usb_embryo,
 "microbiome": demo_usb_microbiome,
 "pregnancy": demo_usb_pregnancy,
 "cancer": demo_usb_cancer,
 "rejuvenation": demo_usb_rejuvenation,
 "consciousness": demo_usb_consciousness,
 "neuralcode": demo_usb_neuralcode,
 "folding": demo_usb_folding,
}


def demo_usb_darkgenome(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the dark genome sorted by conservation x perturbation (not noise).
    # ADJUSTABLE ASSUMPTIONS: genome size, coding fraction, transcribed fraction.
    genome = 3.2e9
    coding = genome * 0.015
    transcribed = genome * 0.80
    ratio = transcribed / coding
    print("step 1 - protein code: %.3e bases (%.1f %%)" % (coding, coding / genome * 100.0))
    print("step 2 - biochemically active: %.3e bases - activity is not function" % transcribed)
    print("step 3 - activity exceeds code by %.1fx: sort by conservation x perturbation" % ratio)
    assert 4.79e7 < coding < 4.81e7, coding
    assert 53.3 < ratio < 53.4, ratio
    print("CONFIRM panel: full conservation-plus-perturbation census of a mammalian genome.")
    print("REFUTE panel: large conserved regions with zero perturbation effect as the rule.")
    print("OK: %s read the fine print" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_heritability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: heritability as holographic - stored in network wiring, not variant lists.
    # ADJUSTABLE ASSUMPTIONS: twin correlations; GWAS-explained slice.
    r_mz, r_dz = 0.85, 0.45
    h2 = 2.0 * (r_mz - r_dz)
    gwas = 0.25
    missing = h2 - gwas
    n_periph, each = 10000, 0.000055   # omnigenic periphery: dim pixels
    periphery = n_periph * each
    print("step 1 - twin studies: h2 = 2*(%.2f - %.2f) = %.2f" % (r_mz, r_dz, h2))
    print("step 2 - GWAS bright pixels explain %.2f; missing %.2f" % (gwas, missing))
    print("step 3 - %d dim pixels x %.6f = %.4f: the picture is in the arrangement" %
          (n_periph, each, periphery))
    assert 0.79 < h2 < 0.81, h2
    assert 0.54 < missing < 0.56, missing
    assert abs(periphery - missing) < 0.01
    print("CONFIRM panel: network-propagated models beating additive GWAS sums.")
    print("REFUTE panel: a complex trait fully explained by a short variant list.")
    print("OK: %s developed the hologram" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_epigenetics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the two-eraser protocol - most annotations struck before signing over.
    # ADJUSTABLE ASSUMPTIONS: erasure efficiency per wave.
    eff = 0.95
    m0 = 1.0
    after_w1 = m0 * (1.0 - eff)        # embryonic erasure
    after_w2 = after_w1 * (1.0 - eff)  # germline erasure
    print("step 1 - embryonic erasure strikes %.0f%%: %.4f of marks survive" % (eff * 100, after_w1))
    print("step 2 - germline erasure strikes again: %.5f survive both" % after_w2)
    print("step 3 - survivors are the protected class (imprints), not leakage")
    assert 0.049 < after_w1 < 0.051, after_w1
    assert 0.0024 < after_w2 < 0.0026, after_w2
    print("CONFIRM panel: complete catalog of erasure-escapee loci with mechanisms.")
    print("REFUTE panel: widespread mark survival through both erasure waves.")
    print("OK: %s honored the eraser clause" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_sex(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: sex as a moving-target defense priced by the twofold cost.
    # ADJUSTABLE ASSUMPTIONS: generations, parasite adaptation pressure.
    gens = 10
    ratio_clean = (2.0 ** gens) / (1.0 ** gens)   # asexual vs sexual, no parasites
    # Red Queen: adapted parasites cut asexual growth to 0.2x per generation
    asex_par = 0.2 ** gens
    sex_par = 1.0 ** gens                          # reshuffled locks stay ahead
    print("step 1 - no parasites: asexual outbreeds sexual %.0f to 1 in %d generations" % (ratio_clean, gens))
    print("step 2 - parasites adapted: asexual lineage fitness %.2e (collapse)" % asex_par)
    print("step 3 - reshuffled locks: sexual line holds at %.1f - the premium pays" % sex_par)
    assert 1023.0 < ratio_clean < 1025.0, ratio_clean
    assert asex_par < 1e-6
    assert sex_par > asex_par
    print("CONFIRM panel: asexuality transitions exactly where parasite pressure drops below cost.")
    print("REFUTE panel: sex dominating in proven parasite-free environments over deep time.")
    print("OK: %s outran the Red Queen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_multicellularity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the single-cell bottleneck as the cheater-proof covenant.
    # ADJUSTABLE ASSUMPTIONS: benefit b, cost c, relatedness r per life cycle.
    b, c = 10.0, 3.0
    r_clonal, r_chimeric = 1.0, 0.25
    margin_clonal = r_clonal * b - c
    margin_chimeric = r_chimeric * b - c
    print("step 1 - Hamilton's rule: cooperate if r*b > c (benefit %.0f, cost %.0f)" % (b, c))
    print("step 2 - clonal bottleneck r=%.2f: margin %+.1f -> covenant holds" % (r_clonal, margin_clonal))
    print("step 3 - chimeric aggregation r=%.2f: margin %+.1f -> cheaters win" % (r_chimeric, margin_chimeric))
    assert margin_clonal > 6.9 and margin_clonal < 7.1, margin_clonal
    assert margin_chimeric < -0.4 and margin_chimeric > -0.6, margin_chimeric
    print("CONFIRM panel: strict-bottleneck lineages showing less internal conflict.")
    print("REFUTE panel: stable complex multicellularity with no bottleneck and rampant chimerism.")
    print("OK: %s signed the original covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_cambrian(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the Cambrian three-key lock (toolkit x oxygen x predators).
    # ADJUSTABLE ASSUMPTIONS: oxygen threshold curve steepness, rate constant.
    k = 10.0
    def o2_factor(o2):
        return 1.0 / (1.0 + math.exp(-(o2 - 0.5) / 0.05))
    before = k * 1.0 * o2_factor(0.3) * 0.0      # toolkit ready, low oxygen, no predators
    mid = k * 1.0 * o2_factor(0.7) * 0.0         # oxygen up, still no detonator
    after = k * 1.0 * o2_factor(0.7) * 1.0       # third key turns: arms race ignites
    print("step 1 - toolkit ready, oxygen low, no predators: diversification %.3f" % before)
    print("step 2 - oxygen crosses threshold, no predators: %.3f (big slow animals, no explosion)" % mid)
    print("step 3 - predators arrive: diversification %.2f - the blink" % after)
    assert before == 0.0
    assert mid == 0.0
    assert 9.8 < after < 9.9, after
    print("CONFIRM panel: strict key sequence (toolkit, oxygen, predators, explosion) across basins.")
    print("REFUTE panel: explosion-scale radiation in a proven low-oxygen setting.")
    print("OK: %s turned all three keys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_ecosystems(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: May's stability criterion - architecture, not diversity, holds the web.
    # ADJUSTABLE ASSUMPTIONS: species n, connectance C, interaction spread sigma.
    def may(n, C, sigma):
        return sigma * math.sqrt(n * C)   # stable iff < 1
    modest = may(50, 0.2, 0.3)
    complex_random = may(200, 0.3, 0.4)
    complex_arch = may(200, 0.3, 0.1)     # weak-link architecture: same web, damped links
    print("step 1 - modest random web: sigma*sqrt(nC) = %.4f %s 1 (stable)" %
          (modest, "<" if modest < 1 else ">"))
    print("step 2 - complex random web: %.4f > 1 (May's collapse)" % complex_random)
    print("step 3 - same web, weak-link architecture: %.4f < 1 (the forest stands)" % complex_arch)
    assert 0.94 < modest < 0.96, modest
    assert 3.09 < complex_random < 3.11, complex_random
    assert 0.77 < complex_arch < 0.78, complex_arch
    print("CONFIRM panel: architectural metrics beating diversity counts at predicting collapses.")
    print("REFUTE panel: collapses with provably intact architecture.")
    print("OK: %s held the web" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_origin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the fidelity-length ratchet escaping Eigen's paradox.
    # ADJUSTABLE ASSUMPTIONS: replication superiority s, per-base fidelities.
    s = 10.0
    def lmax(q):
        return math.log(s) / (1.0 - q)   # error threshold: longest viable genome
    l_sloppy = lmax(0.95)                # early ribozymes: sloppy copying
    l_better = lmax(0.99)                # after the ratchet turns once
    print("step 1 - sloppy replicase (q=0.95): genomes up to %.2f bases viable" % l_sloppy)
    print("step 2 - longer genome encodes better replicase (q=0.99): up to %.2f bases" % l_better)
    print("step 3 - the ratchet: length and fidelity bootstrap each other - no leap needed")
    assert 46.0 < l_sloppy < 46.1, l_sloppy
    assert 230.2 < l_better < 230.4, l_better
    assert l_better > l_sloppy * 4.9
    print("CONFIRM panel: lab overlap-cradle sustaining RNA copying with heritable improvement.")
    print("REFUTE panel: proof no plausible environment overlap can sustain the ratchet.")
    print("OK: %s signed the first covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_lifeelsewhere(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the two-rate model - common microbes, filtered technosignatures.
    # ADJUSTABLE ASSUMPTIONS: optimistic vs pessimistic Drake factors.
    opt = [3.0, 1.0, 0.5, 1.0, 0.1, 0.1, 10000.0]   # simple life easy
    pes = [3.0, 0.5, 0.2, 0.01, 0.001, 0.01, 1000.0]
    def drake(f):
        n = 1.0
        for v in f:
            n *= v
        return n
    n_opt, n_pes = drake(opt), drake(pes)
    print("step 1 - simple life common: N = %.0f candidate cradles" % n_opt)
    print("step 2 - full chain pessimistic: N = %.2e" % n_pes)
    print("step 3 - split the question: microbes hum, technosignatures face the filter")
    assert 149.0 < n_opt < 151.0, n_opt
    assert n_pes < 1e-4, n_pes
    print("CONFIRM panel: a second independent biosphere (origin easy) + continued silence (filter real).")
    print("REFUTE panel: a sterile solar system despite genuinely habitable worlds.")
    print("OK: %s counted to one and stopped" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_ants(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the colony as a liquid computer (quorum thresholds).
    # ADJUSTABLE ASSUMPTIONS: quorum threshold, scout count, recruitment rate.
    Q, scouts, r = 10.0, 5.0, 1.5      # quorum ants, scouting ants, recruits per scout per min
    t_quorum = Q / (r * scouts)
    print("step 1 - scouts sample nests; encounters are the colony's census")
    print("step 2 - pheromone trails store the decision; evaporation is forgetting")
    print("step 3 - quorum %d reached in %.3f min: commit, no ballot box" % (Q, t_quorum))
    assert 1.33 < t_quorum < 1.34, t_quorum
    t_high = 20.0 / (r * scouts)       # higher threshold: slower, more accurate
    assert t_high > t_quorum * 1.9, "threshold tunes the speed-accuracy trade-off"
    print("CONFIRM panel: colony decisions predicted from encounter-rate dynamics alone.")
    print("REFUTE panel: decisions requiring individual ants to hold global state.")
    print("OK: %s joined the quorum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_plants(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the flytrap's leaky integrator - short-term memory without neurons.
    # ADJUSTABLE ASSUMPTIONS: leak time constant, trigger threshold.
    tau, thresh = 30.0, 1.2
    v_two_fast = 1.0 + math.exp(-20.0 / tau)    # two touches, 20 s apart
    v_two_slow = 1.0 + math.exp(-60.0 / tau)    # two touches, 60 s apart
    v_one = 1.0
    print("step 1 - one touch: charge %.2f %s threshold %.1f (a raindrop is ignored)" %
          (v_one, "<", thresh))
    print("step 2 - two touches 20 s apart: charge %.4f -> SNAP" % v_two_fast)
    print("step 3 - two touches 60 s apart: charge %.4f -> ignored (memory leaked away)" % v_two_slow)
    assert 1.51 < v_two_fast < 1.52, v_two_fast
    assert 1.13 < v_two_slow < 1.14, v_two_slow
    assert v_two_fast > thresh > v_two_slow > v_one
    print("CONFIRM panel: plant decisions predicted from distributed signal integration.")
    print("REFUTE panel: plant decisions requiring a centralized integrator.")
    print("OK: %s counted to two" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_virulence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: virulence priced by the transmission route (trade-off optimum).
    # ADJUSTABLE ASSUMPTIONS: transmission coefficient, background mortality, recovery rate.
    c, mu, gamma = 2.0, 0.1, 0.5
    def R0(v):
        return c * math.sqrt(v) / (mu + v + gamma)
    v_star = 0.6                        # analytic optimum: dR0/dv = 0 at v = mu + gamma
    r_star = R0(v_star)
    r_low = R0(0.1)
    print("step 1 - transmission buys spread at the price of host damage: R0(v) = 2*sqrt(v)/(0.6+v)")
    print("step 2 - optimum virulence v* = %.2f, R0 = %.4f" % (v_star, r_star))
    print("step 3 - too mild (v=0.1): R0 = %.4f - the meek do not transmit" % r_low)
    assert 0.59 < v_star < 0.61, v_star
    assert 1.29 < r_star < 1.30, r_star
    assert r_star > r_low * 1.4
    print("CONFIRM panel: virulence optima shifting with experimental transmission-route changes.")
    print("REFUTE panel: optima indifferent to transmission route across many pathogens.")
    print("OK: %s priced the trade-off" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_chirality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: symmetry broken by amplified whisper (nodal flow + bistable cascade).
    # ADJUSTABLE ASSUMPTIONS: flow velocity, node width, morphogen diffusivity.
    v, L, D = 10.0, 50.0, 100.0        # um/s, um, um^2/s
    Pe = v * L / D                     # Peclet: advection vs diffusion
    print("step 1 - cilia whisper: leftward flow v = %.0f um/s across the node" % v)
    print("step 2 - Peclet number %.2f %s 1: the whisper beats diffusion" % (Pe, ">"))
    print("step 3 - bistable Nodal cascade amplifies the whisper into decree: left, or mirror")
    assert 4.9 < Pe < 5.1, Pe
    assert Pe > 1.0, "advection must dominate for the bias to reach the sensors"
    print("CONFIRM panel: flow-sensor identification with gain tuning outcome reliability.")
    print("REFUTE panel: normal patterning with provably no flow or ciliary input.")
    print("OK: %s broke the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_viruses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: viruses as the biosphere's gene couriers (travel light, borrow all).
    # ADJUSTABLE ASSUMPTIONS: global virion estimate, burst size per virocell.
    total_virions = 1e31
    burst = 100.0                      # virions per virocell (infected cell factory)
    virocells = total_virions / burst
    dark_frac = 0.80                   # viral dark matter: genes matching nothing known
    print("step 1 - the courier fleet: %.2e virions on Earth" % total_virions)
    print("step 2 - the living form is the virocell: %.2e factories at burst %.0f" % (virocells, burst))
    print("step 3 - dark matter %.0f%%: the courier's toolkit, selected to be unrecognizable" %
          (dark_frac * 100.0))
    assert 0.99e29 < virocells < 1.01e29, virocells
    assert 0.79 < dark_frac < 0.81, dark_frac
    print("CONFIRM panel: functional screens assigning host-manipulation roles to dark matter.")
    print("REFUTE panel: dark matter proving mostly non-functional baggage.")
    print("OK: %s read the courier's manifest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_cellatlas(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the atlas as an attractor landscape (valleys, not stamps).
    # ADJUSTABLE ASSUMPTIONS: rare-cell frequency, survey depths.
    f_rare = 1e-6
    def detect(n):
        return 1.0 - (1.0 - f_rare) ** n
    p1, p2 = detect(1e6), detect(5e6)
    print("step 1 - broad survey (1M cells): rare valley found with probability %.4f" % p1)
    print("step 2 - deep survey (5M cells): probability %.4f - valleys, then slopes" % p2)
    print("step 3 - completeness = finite valleys mapped + slopes interpolated")
    assert 0.63 < p1 < 0.64, p1
    assert 0.993 < p2 < 0.994, p2
    print("CONFIRM panel: atlas convergence - new surveys adding only slopes and rare valleys.")
    print("REFUTE panel: unbounded new major valleys with every deeper survey.")
    print("OK: %s mapped the terrain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_luca(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: LUCA as a covenant community (gene-trading collective, frozen code).
    # ADJUSTABLE ASSUMPTIONS: inter-domain divergence, clock rate and its uncertainty.
    D, r = 0.84, 1e-10                 # substitutions/site, per site per year
    t = D / (2.0 * r)
    t_low = D / (2.0 * 1.2e-10)
    t_high = D / (2.0 * 0.8e-10)
    print("step 1 - molecular clock: %.1f billion years to the common ancestor" % (t / 1e9))
    print("step 2 - rate uncertainty: %.1f to %.1f billion years" % (t_low / 1e9, t_high / 1e9))
    print("step 3 - the code froze fast; bodies (private membranes) came later, independently")
    assert 4.19e9 < t < 4.21e9, t
    assert 3.49e9 < t_low < 3.51e9, t_low
    assert 5.24e9 < t_high < 5.26e9, t_high
    print("CONFIRM panel: membrane-lipid genes proving non-universal (independent cellularity).")
    print("REFUTE panel: a LUCA with a complete private membrane toolkit, no trading signal.")
    print("OK: %s met the ancestor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usb_theory(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the adjacent possible - laws of the reachable, not the actual.
    # ADJUSTABLE ASSUMPTIONS: branching factor, innovation steps, convergent attractors.
    b, n = 3, 5
    total = (b ** (n + 1) - 1) // (b - 1)   # reachable forms after n innovation steps
    attractors = 12                          # eyes, wings, eusociality...: the terrain's funnels
    print("step 1 - branching %d over %d steps: %d reachable forms (the adjacent possible)" % (b, n, total))
    print("step 2 - %d convergent attractors: contingency walks, law governs the terrain" % attractors)
    print("step 3 - a complete theory predicts the reachable, not the actual")
    assert 363 < total < 365, total
    assert attractors < total / 20.0, "attractors must be rare funnels, not the whole space"
    print("CONFIRM panel: adjacent-possible framework predicting convergent vs frozen outcomes.")
    print("REFUTE panel: convergence proving illusory under rigorous analysis.")
    print("OK: %s charted the possible" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS["darkgenome"] = demo_usb_darkgenome
DEMOS["heritability"] = demo_usb_heritability
DEMOS["epigenetics"] = demo_usb_epigenetics
DEMOS["sex"] = demo_usb_sex
DEMOS["multicellularity"] = demo_usb_multicellularity
DEMOS["cambrian"] = demo_usb_cambrian
DEMOS["ecosystems"] = demo_usb_ecosystems
DEMOS["origin"] = demo_usb_origin
DEMOS["lifeelsewhere"] = demo_usb_lifeelsewhere
DEMOS["ants"] = demo_usb_ants
DEMOS["plants"] = demo_usb_plants
DEMOS["virulence"] = demo_usb_virulence
DEMOS["chirality"] = demo_usb_chirality
DEMOS["viruses"] = demo_usb_viruses
DEMOS["cellatlas"] = demo_usb_cellatlas
DEMOS["luca"] = demo_usb_luca
DEMOS["theory"] = demo_usb_theory
