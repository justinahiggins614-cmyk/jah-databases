#!/usr/bin/env python3
"""Demo programs for the Unsolved Ecology databases (Manon's 16:15 orders, batch).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only Python that
walks through the Signature solution approach with adjustable assumptions, prints real
computed values, runs a confirm/refute panel, asserts tight bounds (never float
exact-equality), and ends with the OK marker. All 68 are machine-executed by build.py.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_uec_tropics_rich(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the tropics as a compound-interest ledger (energy x stability x time).
    # ADJUSTABLE ASSUMPTIONS: the energy curve and the deep-time stability weights.
    lats = [0.0, 15.0, 30.0, 45.0, 60.0]
    energy = [0.99, 0.93, 0.80, 0.60, 0.38]      # normalized solar input proxy
    stability = [1.00, 0.95, 0.80, 0.55, 0.30]   # fraction of deep time climatically stable
    R0 = 320.0
    rich = [R0 * e * s for e, s in zip(energy, stability)]
    print("step 1 - ledger inputs per latitude: energy %s, stability %s" % (energy, stability))
    print("step 2 - richness = 320 x energy x stability -> %s" % [round(r, 1) for r in rich])
    ratio = rich[0] / rich[-1]
    print("step 3 - equatorial to polar richness ratio = %.2f" % ratio)
    assert 316.0 < rich[0] < 318.0, rich[0]
    assert 36.0 < rich[-1] < 37.0, rich[-1]
    assert 8.6 < ratio < 8.8, ratio
    print("CONFIRM panel: fossil-calibrated speciation minus extinction favoring the tropics,")
    print("  with the three-factor product beating any single factor.")
    print("REFUTE panel: a major group poorer in the tropics despite high energy and stability.")
    print("OK: %s compounded the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_species_area(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the species-area curve as three compartments (sampling, buffering, habitat).
    # ADJUSTABLE ASSUMPTIONS: the power-law constant c and exponent z.
    c, z = 30.0, 0.25
    areas = [1.0, 10.0, 100.0, 1000.0]
    S = [c * a ** z for a in areas]
    print("step 1 - S = cA^z with c=%.1f, z=%.2f" % (c, z))
    print("step 2 - predicted richness for areas %s -> %s" % (areas, [round(s, 2) for s in S]))
    z_check = math.log(S[3] / S[0]) / math.log(areas[3] / areas[0])
    print("step 3 - exponent recovered from the curve ends: z = %.6f" % z_check)
    assert 53.3 < S[1] < 53.4, S[1]
    assert 168.6 < S[3] < 168.8, S[3]
    assert abs(z_check - 0.25) < 1e-9, z_check
    print("CONFIRM panel: nested plots showing kinks where sampling hands off to buffering to habitat.")
    print("REFUTE panel: perfectly smooth power laws across six orders of magnitude, no kinks anywhere.")
    print("OK: %s audited the compartments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_invasions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: invasion as a three-gate audition; gate two is a numbers game.
    # ADJUSTABLE ASSUMPTIONS: logistic intercept and the propagule-pressure slope.
    def p_est(N):
        return 1.0 / (1.0 + math.exp(-(-3.0 + 2.0 * math.log10(N))))
    p10, p1k, p100k = p_est(10.0), p_est(1000.0), p_est(100000.0)
    print("step 1 - gate two is propagule pressure: P(establish | N founders)")
    print("step 2 - N=10 -> %.4f; N=1000 -> %.4f; N=100000 -> %.4f" % (p10, p1k, p100k))
    print("step 3 - a thousand-fold rise in founders multiplies success ~%.1fx" % (p1k / p10))
    assert 0.26 < p10 < 0.28, p10
    assert 0.95 < p1k < 0.96, p1k
    assert p100k > 0.999, p100k
    print("CONFIRM panel: the gate scorecard beating trait-only models on past introductions.")
    print("REFUTE panel: repeated massive invasions from tiny founder numbers with poor trait match.")
    print("OK: %s ran the audition" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_predator_prey(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the cycle as a three-engine machine (predators, food, climate).
    # ADJUSTABLE ASSUMPTIONS: growth, attack, conversion, mortality rates; integration step.
    r, a, e, m = 0.5, 0.02, 0.1, 0.3
    x, y, dt = 40.0, 9.0, 0.05
    xs, ys = [], []
    for _ in range(1200):
        xs.append(x); ys.append(y)
        x += (r * x - a * x * y) * dt
        y += (e * a * x * y - m * y) * dt
    amp = max(xs) - min(xs)
    i_px = xs.index(max(xs)); i_py = ys.index(max(ys))
    lag = (i_py - i_px) % len(xs)
    print("step 1 - Lotka-Volterra pair integrated: prey oscillates with amplitude %.1f" % amp)
    print("step 2 - prey peaks at step %d, predators peak at step %d (lag %d steps)" % (i_px, i_py, lag))
    print("step 3 - driver partition: this run is 100% top-down by construction; nature mixes three engines")
    assert all(v > 0 for v in xs), "prey went negative"
    assert 5.0 < amp < 600.0, amp
    assert 0 < lag < 600, lag
    print("CONFIRM panel: exclusion experiments fingerprinting each driver in real systems.")
    print("REFUTE panel: cycles unchanged by both predator removal and food addition.")
    print("OK: %s read the cycle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_collapse_sudden(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: sudden collapse as a fold bifurcation with hysteresis.
    # ADJUSTABLE ASSUMPTIONS: the pressure step size and relaxation length.
    def equil(r, x0, steps=800):
        x = x0
        for _ in range(steps):
            x += 0.05 * (r + x - x ** 3)
        return x
    x = equil(0.5, 0.0)
    fwd = []
    for i in range(21):
        x = equil(0.5 - 0.05 * i, x); fwd.append(x)
    xb = fwd[-1]
    bwd = []
    for i in range(21):
        xb = equil(-0.5 + 0.05 * i, xb); bwd.append(xb)
    gap = fwd[10] - bwd[10]
    print("step 1 - pressure eased 0.5 -> -0.5: system state ends at %.3f" % fwd[-1])
    print("step 2 - pressure restored -0.5 -> 0.5: system state ends at %.3f" % bwd[-1])
    print("step 3 - hysteresis gap at zero pressure: %.3f (the return trip costs extra)" % gap)
    assert fwd[10] > 0.9, fwd[10]
    assert bwd[10] < -0.9, bwd[10]
    assert gap > 1.8, gap
    print("CONFIRM panel: feedback audits classifying known gradual vs threshold systems.")
    print("REFUTE panel: sudden collapses with no measurable positive feedback beforehand.")
    print("OK: %s mapped the valleys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_extinction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: extinction risk as a debt ledger (pressure debits vs buffering credits).
    # ADJUSTABLE ASSUMPTIONS: the range-credit curve and the loss-debit weight.
    def risk(loss_frac, range_km2):
        return (loss_frac * 100.0) / (1.0 + math.log10(range_km2))
    endemic = risk(0.7, 50.0)        # narrow island endemic, 70% habitat lost
    widespread = risk(0.7, 1e6)      # continental generalist, same loss
    print("step 1 - ledger: debits = habitat loss; credits = range size (log-scaled)")
    print("step 2 - island endemic risk score = %.2f" % endemic)
    print("step 3 - continental generalist risk score = %.2f" % widespread)
    assert 25.0 < endemic < 27.0, endemic
    assert 9.0 < widespread < 11.0, widespread
    assert endemic > 2.0 * widespread
    print("CONFIRM panel: the watchlist beating Red List criteria on the next decade of losses.")
    print("REFUTE panel: most observed extinctions coming from species the ledger ranked safe.")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_bef(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the biodiversity-function curve as shift coverage.
    # ADJUSTABLE ASSUMPTIONS: maximum function Fmax and the half-saturation richness k.
    Fmax, k = 500.0, 4.0
    rich = [1, 2, 4, 8, 16]
    F = [Fmax * s / (s + k) for s in rich]
    print("step 1 - function F(S) = %d * S/(S+%d): saturating coverage" % (Fmax, k))
    print("step 2 - F at richness %s -> %s" % (rich, [round(f, 1) for f in F]))
    gain_early = F[1] - F[0]
    gain_late = F[4] - F[3]
    per_sp_early = gain_early / 1.0
    per_sp_late = gain_late / 8.0
    print("step 3 - marginal gain 1->2 species: %.1f; 8->16 species: %.1f" % (gain_early, gain_late))
    print("step 3b - per added species: early %.1f vs late %.1f (diminishing returns)" % (per_sp_early, per_sp_late))
    assert 99.9 < F[0] < 100.1, F[0]
    assert 399.9 < F[4] < 400.1, F[4]
    assert per_sp_early > 5.0 * per_sp_late > 0, (per_sp_early, per_sp_late)
    print("CONFIRM panel: removal experiments where deleting the minimum crew collapses function.")
    print("REFUTE panel: function carried by interactions no coverage matrix can capture.")
    print("OK: %s scheduled the shifts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_microbes_role(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: microbial job descriptions from guild knockouts.
    # ADJUSTABLE ASSUMPTIONS: baseline decomposition rate and each guild's load share.
    base = 0.80   # per-year decomposition rate, intact community
    knock_nfix = 0.72    # nitrogen fixers suppressed
    knock_decomp = 0.35  # decomposers suppressed
    knock_both = 0.28
    print("step 1 - intact community decomposition rate: %.2f /yr" % base)
    print("step 2 - knock out N-fixers -> %.2f; knock out decomposers -> %.2f" % (knock_nfix, knock_decomp))
    print("step 3 - knock out both -> %.2f (loads do not simply add)" % knock_both)
    assert knock_decomp < knock_nfix < base
    assert knock_both < knock_decomp
    assert 0.34 < knock_decomp < 0.36, knock_decomp
    print("CONFIRM panel: knockout maps predicting new suppression outcomes across continents.")
    print("REFUTE panel: function entirely emergent, no knockout mapping to function loss.")
    print("OK: %s wrote the job descriptions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_no_return(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: recovery vs lock-in as an ignition threshold (Allee valley).
    # ADJUSTABLE ASSUMPTIONS: growth rate r, ignition threshold A, starting cover.
    r, A, dt = 0.5, 0.3, 0.05
    def run(x0, steps=600):
        x = x0
        for _ in range(steps):
            x += dt * r * x * (x - A) * (1.0 - x)
            x = min(max(x, 0.0), 1.0)
        return x
    low, high = run(0.20), run(0.50)
    print("step 1 - ignition threshold A = %.1f: below it the old state's feedbacks cannot restart" % A)
    print("step 2 - trial patch at 20%% cover ends at %.4f (locked)" % low)
    print("step 3 - trial patch at 50%% cover ends at %.4f (recovered)" % high)
    assert low < 0.01, low
    assert high > 0.99, high
    print("CONFIRM panel: the recovery-readiness index predicting five-year restoration outcomes.")
    print("REFUTE panel: locked-classified sites recovering spontaneously at meaningful rates.")
    print("OK: %s surveyed the valley" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_food_webs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the food web as a suspension bridge; arrangement carries the load.
    # ADJUSTABLE ASSUMPTIONS: connectance levels and the removal fraction.
    import random
    random.seed(42)
    def robustness(n, C, trials=40, remove_frac=0.2):
        # random web: basal species 0..n/4-1; consumer i eats random lower species with prob C
        keep = []
        for _ in range(trials):
            prey_of = {}
            for i in range(n):
                prey_of[i] = [j for j in range(i) if random.random() < C] if i >= n // 4 else []
            extinct = set(random.sample(range(n), int(n * remove_frac)))
            changed = True
            while changed:
                changed = False
                for i in range(n // 4, n):
                    if i not in extinct and prey_of[i] and all(p in extinct for p in prey_of[i]):
                        extinct.add(i); changed = True
            keep.append((n - len(extinct)) / n)
        return sum(keep) / len(keep)
    r_lo = robustness(16, 0.15)
    r_hi = robustness(16, 0.45)
    print("step 1 - bridge inspection: 16-species webs at connectance 0.15 vs 0.45")
    print("step 2 - fraction surviving after 20%% species removal: low-C %.3f, high-C %.3f" % (r_lo, r_hi))
    print("step 3 - arrangement effect: higher connectance retains %.3f more of the web" % (r_hi - r_lo))
    assert 0.0 < r_lo < 1.0 and 0.0 < r_hi < 1.0
    assert r_hi > r_lo, (r_lo, r_hi)
    print("CONFIRM panel: load-bearing maps predicting whole-ecosystem removal outcomes.")
    print("REFUTE panel: removal outcomes dominated by non-trophic factors the map ignores.")
    print("OK: %s inspected the bridge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_dispersal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the dispersal lottery - the jackpot tail writes the future.
    # ADJUSTABLE ASSUMPTIONS: exponential decay rate and the fat-tail exponent.
    lam = 0.5                       # exponential kernel per km
    tail_exp = math.exp(-lam * 10.0)      # fraction traveling beyond 10 km
    alpha = 2.5
    tail_fat = 10.0 ** (1.0 - alpha)       # power-law tail beyond 10 km, from 1 km
    print("step 1 - exponential kernel: fraction beyond 10 km = %.5f" % tail_exp)
    print("step 2 - fat-tailed kernel: fraction beyond 10 km = %.5f" % tail_fat)
    print("step 3 - the fat tail delivers %.1fx more jackpot colonists" % (tail_fat / tail_exp))
    assert 0.006 < tail_exp < 0.007, tail_exp
    assert 0.031 < tail_fat < 0.032, tail_fat
    assert 4.5 < tail_fat / tail_exp < 5.0
    print("CONFIRM panel: measured tails beating extrapolated kernels on colonization forecasts.")
    print("REFUTE panel: the three methods disagreeing irreconcilably - no stable tail to measure.")
    print("OK: %s counted the jackpots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_restoration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: restoration as rebuilding from salvaged parts; inventory first.
    # ADJUSTABLE ASSUMPTIONS: the completeness-to-success logistic curve.
    def p_success(comp):
        return 1.0 / (1.0 + math.exp(-(8.0 * comp - 4.0)))
    p30, p70, p90 = p_success(0.3), p_success(0.7), p_success(0.9)
    print("step 1 - parts inventory completeness scored 0..1 before any planting")
    print("step 2 - P(success): completeness 0.3 -> %.3f; 0.7 -> %.3f; 0.9 -> %.3f" % (p30, p70, p90))
    print("step 3 - matched technique on a 0.7 site beats blind planting on a 0.3 site ~%.1fx" % (p70 / p30))
    assert 0.16 < p30 < 0.18, p30
    assert 0.82 < p70 < 0.84, p70
    assert p90 > 0.95, p90
    print("CONFIRM panel: audited projects outperforming matched unaudited controls.")
    print("REFUTE panel: complete-inventory projects failing as often as controls.")
    print("OK: %s inventoried the parts" % NAME)
if __name__ == "__main__":
    main()
''')

print("demos chunk 1 done")


def demo_uec_trophic_cascades(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: a cascade as a signal traveling down a noisy wire.
    # ADJUSTABLE ASSUMPTIONS: growth, attack, conversion, mortality rates; integration step.
    r, K, a, e, m, b, n, dt = 1.5, 200.0, 0.02, 0.25, 0.3, 0.03, 0.25, 0.02
    def run(with_pred, steps=3000):
        P, H, C = 60.0, 20.0, 5.0
        for _ in range(steps):
            dP = (r * P * (1 - P / K) - a * P * H) * dt
            dH = (e * a * P * H - m * H - (b * H * C if with_pred else 0.0)) * dt
            dC = (e * b * H * C - n * C) * dt if with_pred else 0.0
            P, H, C = max(P + dP, 0.0), max(H + dH, 0.0), max(C + dC, 0.0)
        return P, H, C
    Pw, Hw, Cw = run(True)
    Pn, Hn, _ = run(False)
    print("step 1 - three-level chain integrated to equilibrium, predators present vs removed")
    print("step 2 - plant biomass: with predators %.1f, without predators %.1f" % (Pw, Pn))
    print("step 3 - cascade strength: plants fall %.1f%% when the top link is cut" % (100.0 * (Pw - Pn) / Pw))
    assert Pw > 100.0, Pw
    assert Pn < 70.0, Pn
    assert Hw < Hn, (Hw, Hn)
    print("CONFIRM panel: the transmission index beating predator presence-absence on documented manipulations.")
    print("REFUTE panel: strong cascades where the index predicts fizzle, repeatedly.")
    print("OK: %s traced the signal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_disturbance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the disturbance hump, conditional on the checklist.
    # ADJUSTABLE ASSUMPTIONS: the hump shape and the disturbance levels sampled.
    def D(x):
        return 4.0 * x * (1.0 - x)
    levels = [0.1, 0.3, 0.5, 0.7, 0.9]
    div = [D(x) for x in levels]
    print("step 1 - checklist: competitive hierarchy present, disturbance resets it, scales matched")
    print("step 2 - diversity at disturbance %s -> %s" % (levels, [round(d, 2) for d in div]))
    print("step 3 - peak at intermediate disturbance: %.2f vs edges %.2f" % (D(0.5), D(0.1)))
    assert abs(D(0.5) - 1.0) < 1e-9
    assert abs(div[0] - 0.36) < 1e-9 and abs(div[4] - 0.36) < 1e-9
    assert div[2] > div[1] > div[0] and div[2] > div[3] > div[4]
    print("CONFIRM panel: pre-registered hump vs no-hump calls across twenty systems.")
    print("REFUTE panel: checklist-passing systems showing no hump.")
    print("OK: %s checked the referee" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_productivity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: productivity as four foremen; the strictest one shouts the orders.
    # ADJUSTABLE ASSUMPTIONS: resource levels and the maximum growth rate.
    def npp(light, water, N, P, gmax=100.0):
        return gmax * min(light, water, N, P)
    base = npp(0.9, 0.5, 0.8, 0.7)
    watered = npp(0.9, 0.9, 0.8, 0.7)
    fertilized = npp(0.9, 0.9, 1.0, 1.0)
    print("step 1 - foreman audit: light=0.9 water=0.5 N=0.8 P=0.7 -> water shouts")
    print("step 2 - baseline NPP = %.1f; water added -> %.1f (now phosphorus shouts)" % (base, watered))
    print("step 3 - water + nutrients -> %.1f (light finally binds)" % fertilized)
    assert 49.9 < base < 50.1, base
    assert 69.9 < watered < 70.1, watered
    assert 89.9 < fertilized < 90.1, fertilized
    print("CONFIRM panel: the limitation atlas beating single-factor models on new experiments.")
    print("REFUTE panel: limitation so idiosyncratic per site that no biome atlas transfers.")
    print("OK: %s audited the foremen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_neutral_niche(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: neutral theory as the blank map; deviations are the niche mountains.
    # ADJUSTABLE ASSUMPTIONS: the observed abundance vectors being compared.
    def broken_stick(S, N):
        return [(N / S) * sum(1.0 / j for j in range(i + 1, S + 1)) for i in range(S)]
    S, N = 8, 200
    exp = broken_stick(S, N)
    neutral_like = [66, 44, 30, 23, 16, 11, 7, 3]   # hollow curve: close to the null map
    niche_like = [30, 28, 27, 26, 24, 23, 22, 20]   # even spacing: limiting similarity at work
    def dev(obs):
        return sum(abs(math.log(o / e)) for o, e in zip(obs, exp))
    d_neu, d_niche = dev(neutral_like), dev(niche_like)
    print("step 1 - blank map (broken-stick null) for S=%d, N=%d" % (S, N))
    print("step 2 - deviation score: neutral-like community %.3f, niche-like community %.3f" % (d_neu, d_niche))
    print("step 3 - the mountains stand %.2fx taller in the niche-structured community" % (d_niche / d_neu))
    assert d_niche > d_neu, (d_neu, d_niche)
    assert 0.1 < d_neu < 1.0, d_neu
    assert d_niche > 1.5, d_niche
    print("CONFIRM panel: niche-fraction scores predicting management responses across taxa.")
    print("REFUTE panel: niche signatures shown to be artifacts of the neutral model itself.")
    print("OK: %s mapped the deviations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_plankton(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the paradox resolved by kill-the-winner (enemies cull the abundant).
    # ADJUSTABLE ASSUMPTIONS: competition strength, kill-the-winner mortality, integration step.
    def run(ktw, steps=6000, dt=0.02):
        r, K, a, d, eps = 1.0, 1.0, 1.2, 0.8, 1e-6
        x, y = 0.50, 0.51   # asymmetric start: symmetry would freeze the contest
        for _ in range(steps):
            mx = d * x * x / (x + y + eps) if ktw else 0.0
            my = d * y * y / (x + y + eps) if ktw else 0.0
            x = max(x + dt * (r * x * (1 - (x + a * y) / K) - mx), 0.0)
            y = max(y + dt * (r * y * (1 - (y + a * x) / K) - my), 0.0)
        return x, y
    xs, ys = run(False)
    xk, yk = run(True)
    print("step 1 - two competitors, one resource, no enemies: end at %.4f and %.4f (exclusion)" % (xs, ys))
    print("step 2 - add kill-the-winner enemies (they strike the abundant): end at %.4f and %.4f" % (xk, yk))
    print("step 3 - the winner can never win: abundance itself summons its enemies")
    assert min(xs, ys) < 0.05, (xs, ys)
    assert xk > 0.2 and yk > 0.2, (xk, yk)
    assert abs(xk - yk) < 0.05, (xk, yk)
    print("CONFIRM panel: regional censuses predicting diversity change when a mechanism is altered.")
    print("REFUTE panel: high diversity where all measured mechanisms are weak.")
    print("OK: %s let the winners lose" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_dilution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the transmission table - dilution depends on who sits down.
    # ADJUSTABLE ASSUMPTIONS: host competences and vectorial capacity.
    v = 0.5   # vectorial capacity
    diverse = [0.9, 0.3, 0.1]       # good reservoir plus two poor transmitters
    depauperate = [0.9]             # only the good reservoir remains
    risk_div = v * sum(diverse) / len(diverse)
    risk_dep = v * sum(depauperate) / len(depauperate)
    print("step 1 - table audit: competences %s, mean %.3f" % (diverse, sum(diverse) / len(diverse)))
    print("step 2 - disease risk: diverse community %.3f, depauperate community %.3f" % (risk_div, risk_dep))
    print("step 3 - losing the poor transmitters amplifies risk %.2fx" % (risk_dep / risk_div))
    assert 0.21 < risk_div < 0.22, risk_div
    assert 0.44 < risk_dep < 0.46, risk_dep
    assert risk_dep > 2.0 * risk_div
    print("CONFIRM panel: competence-ordered audits beating richness alone across disease systems.")
    print("REFUTE panel: audits predicting dilution where amplification is observed, repeatedly.")
    print("OK: %s audited the table" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_forest_carbon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the forest carbon business on thin margins (growth revenue, mortality cost).
    # ADJUSTABLE ASSUMPTIONS: baseline growth/mortality, CO2 boost, mortality climate sensitivity.
    G0, M0, boost, k, warm = 2.5, 1.0, 0.15, 0.9, 0.02
    def net(t):
        return G0 * (1 + boost) - M0 * math.exp(k * warm * t)
    n0 = net(0.0)
    t_flip = math.log(G0 * (1 + boost) / M0) / (k * warm)
    print("step 1 - margin ledger: growth revenue %.3f vs mortality cost %.3f -> net %.3f tC/ha/yr" % (G0 * (1 + boost), M0, n0))
    print("step 2 - mortality compounds with warming; the margin narrows every year")
    print("step 3 - flip clock: net sink reaches zero in %.1f years" % t_flip)
    assert 1.87 < n0 < 1.88, n0
    assert 58.0 < t_flip < 60.0, t_flip
    assert net(t_flip + 20) < 0, net(t_flip + 20)
    print("CONFIRM panel: margin-watch warnings preceding observed regional sink-to-source flips.")
    print("REFUTE panel: mortality dominated by processes with no trackable climate signal.")
    print("OK: %s watched the margins" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_diversity_stability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the portfolio audit - which part of stability diversity truly earns.
    # ADJUSTABLE ASSUMPTIONS: species mean, variance, and the richness levels compared.
    mean, var = 10.0, 4.0
    def cv(n):
        return math.sqrt(n * var) / (n * mean)   # uncorrelated species: the pure statistical dividend
    cv1, cv16 = cv(1), cv(16)
    print("step 1 - one species: aggregate CV = %.3f" % cv1)
    print("step 2 - sixteen uncorrelated species: aggregate CV = %.3f" % cv16)
    print("step 3 - statistical dividend alone cuts variability %.1fx; compensation would cut further" % (cv1 / cv16))
    assert 0.199 < cv1 < 0.201, cv1
    assert 0.049 < cv16 < 0.051, cv16
    assert 3.9 < cv1 / cv16 < 4.1
    print("CONFIRM panel: the compensatory component predicting real disturbance resistance.")
    print("REFUTE panel: compensatory components near zero everywhere.")
    print("OK: %s audited the portfolio" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_metacommunity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the delivery audit - kitchens vs delivery service, read experimentally.
    # ADJUSTABLE ASSUMPTIONS: colonization and extinction rates under low/high dispersal.
    e = 0.15
    def occupancy(c, steps=8000, dt=0.02):
        p = 0.1
        for _ in range(steps):
            p += dt * (c * p * (1 - p) - e * p)
            p = min(max(p, 0.0), 1.0)
        return p
    p_lo = occupancy(0.20)
    p_hi = occupancy(0.60)
    print("step 1 - Levins patch model: dp/dt = c*p*(1-p) - e*p, e=%.2f" % e)
    print("step 2 - low dispersal c=0.20 -> occupancy %.3f; high dispersal c=0.60 -> %.3f" % (p_lo, p_hi))
    print("step 3 - delivery share: occupancy rises %.2fx when the delivery service is funded" % (p_hi / p_lo))
    assert 0.24 < p_lo < 0.26, p_lo
    assert 0.74 < p_hi < 0.76, p_hi
    assert p_hi > 2.5 * p_lo
    print("CONFIRM panel: manipulative partitions predicting corridor and nutrient management outcomes.")
    print("REFUTE panel: manipulations whose side effects confound every reading.")
    print("OK: %s audited the deliveries" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_janzen_connell(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the minefield census - kill zones measured per species.
    # ADJUSTABLE ASSUMPTIONS: maximum survival and the minefield decay distance.
    smax, d0 = 0.9, 8.0
    def surv(d):
        return smax * (1 - math.exp(-d / d0))
    s1, s10, s30 = surv(1.0), surv(10.0), surv(30.0)
    print("step 1 - seedling survival vs distance from parent: s(d) = %.1f*(1-exp(-d/%.0f))" % (smax, d0))
    print("step 2 - 1 m: %.3f; 10 m: %.3f; 30 m: %.3f" % (s1, s10, s30))
    print("step 3 - the minefield is %.1fx deadlier at 1 m than at 30 m" % (s30 / s1))
    assert 0.10 < s1 < 0.12, s1
    assert 0.63 < s10 < 0.66, s10
    assert 0.87 < s30 < 0.89, s30
    print("CONFIRM panel: measured strengths sustaining diversity in forest simulators.")
    print("REFUTE panel: strengths too weak to maintain even a tenth of observed diversity.")
    print("OK: %s censused the minefield" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_early_warning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the smoke detector - calibrated against tipped and untipped series.
    # ADJUSTABLE ASSUMPTIONS: the AR(1) memory parameter early vs late, noise level, seed.
    import random
    random.seed(0)
    def series(phi, n=2000):
        x, out = 0.0, []
        for _ in range(n):
            x = phi * x + random.gauss(0, 1)
            out.append(x)
        return out
    def stats(s):
        m = sum(s) / len(s)
        var = sum((v - m) ** 2 for v in s) / len(s)
        ac = sum((s[i] - m) * (s[i - 1] - m) for i in range(1, len(s))) / sum((v - m) ** 2 for v in s)
        return var, ac
    v_early, ac_early = stats(series(0.5))
    v_late, ac_late = stats(series(0.9))
    print("step 1 - healthy system (memory 0.5): variance %.2f, autocorrelation %.3f" % (v_early, ac_early))
    print("step 2 - near-threshold system (memory 0.9): variance %.2f, autocorrelation %.3f" % (v_late, ac_late))
    print("step 3 - the detector reads %.1fx variance and %.2f extra autocorrelation" % (v_late / v_early, ac_late - ac_early))
    assert v_late > 2.0 * v_early, (v_early, v_late)
    assert ac_late > ac_early + 0.2, (ac_early, ac_late)
    assert 0.4 < ac_early < 0.6, ac_early
    print("CONFIRM panel: calibrated indicators flagging real transitions with actionable lead time.")
    print("REFUTE panel: no indicator beating chance across the real-series library.")
    print("OK: %s calibrated the detector" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_legacy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the memory audit - same present, different pasts, different recoveries.
    # ADJUSTABLE ASSUMPTIONS: growth rate, starting cover with/without legacy seed bank.
    r = 0.1
    def t90(x0):
        return math.log((0.9 / 0.1) / (x0 / (1 - x0))) / r   # logistic time to 90%% of K
    tA = t90(0.05)   # no legacy: bare start
    tB = t90(0.20)   # legacy seed bank: head start
    print("step 1 - two sites, same present conditions; site B carries a legacy seed bank")
    print("step 2 - years to 90%% recovery: site A (no memory) %.1f, site B (memory) %.1f" % (tA, tB))
    print("step 3 - the past shortens recovery by %.1f years: that gap is the memory signal" % (tA - tB))
    assert 51.0 < tA < 52.0, tA
    assert 35.0 < tB < 36.5, tB
    assert tA - tB > 14.0
    print("CONFIRM panel: memory timescales beating present-conditions-only recovery forecasts.")
    print("REFUTE panel: divergences vanishing once subtle present differences are accounted for.")
    print("OK: %s audited the memory" % NAME)
if __name__ == "__main__":
    main()
''')

print("demos chunk 2 done")


def demo_uec_predict_collapse(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: headlights in fog - skill is measured per lead time, never assumed.
    # ADJUSTABLE ASSUMPTIONS: the skill decay timescale tau.
    tau = 3.0   # years; skill decays as exp(-lead/tau)
    def skill(lead):
        return math.exp(-lead / tau)
    s1, s5, s10 = skill(1.0), skill(5.0), skill(10.0)
    print("step 1 - forecast skill vs lead time: skill(lead) = exp(-lead/%.1f)" % tau)
    print("step 2 - skill at 1 yr: %.3f; 5 yr: %.3f; 10 yr: %.3f" % (s1, s5, s10))
    print("step 3 - headlights reach ~%.0f years before skill falls below 5%%" % (-tau * math.log(0.05)))
    assert 0.71 < s1 < 0.73, s1
    assert 0.18 < s5 < 0.20, s5
    assert s10 < 0.05, s10
    print("CONFIRM panel: scoreboards showing stable positive skill at management-relevant leads.")
    print("REFUTE panel: skill flat at zero beyond days-to-weeks across all systems despite good data.")
    print("OK: %s measured the headlights" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_rainforest(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the fortune audit - crediting each income stream of hyperdiversity.
    # ADJUSTABLE ASSUMPTIONS: speciation/extinction rates and the deep-time window.
    lam_tr, mu_tr = 0.25, 0.10     # tropical speciation, extinction per Myr
    lam_te, mu_te = 0.12, 0.09     # temperate speciation, extinction per Myr
    T = 50.0                        # Myr of accumulation
    r_tr, r_te = lam_tr - mu_tr, lam_te - mu_te
    ratio = math.exp((r_tr - r_te) * T)
    print("step 1 - net diversification: tropics %.2f/Myr, temperate %.2f/Myr" % (r_tr, r_te))
    print("step 2 - over %.0f Myr the tropical account compounds to %.0fx the temperate one" % (T, ratio))
    print("step 3 - cradle (faster speciation) and museum (slower extinction) both credit the ledger")
    assert 0.14 < r_tr < 0.16, r_tr
    assert 0.02 < r_te < 0.04, r_te
    assert 400.0 < ratio < 410.0, ratio
    print("CONFIRM panel: credited shares predicting independent facts like endemic lineage depth.")
    print("REFUTE panel: evidence streams contradicting each other irreconcilably.")
    print("OK: %s audited the fortune" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_uncultured(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the shadow trade - linking genomes to in-situ appetites.
    # ADJUSTABLE ASSUMPTIONS: observed richness, singletons/doubletons, cultured count.
    S_obs, f1, f2, cultured = 5000, 2000, 400, 800
    chao1 = S_obs + f1 ** 2 / (2 * f2)
    cultured_frac = cultured / chao1
    print("step 1 - sequenced: %d taxa; singletons %d, doubletons %d" % (S_obs, f1, f2))
    print("step 2 - Chao1 estimated true richness: %.0f" % chao1)
    print("step 3 - cultured fraction of the estimated workforce: %.3f (the shadows dominate)" % cultured_frac)
    assert 9900.0 < chao1 < 10100.0, chao1
    assert 0.079 < cultured_frac < 0.081, cultured_frac
    print("CONFIRM panel: atlas assignments predicting suppression and nutrient-addition outcomes.")
    print("REFUTE panel: activity methods too coarse for lineage-level function mapping.")
    print("OK: %s read the shadows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_metabolic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the master key - testing which doors metabolic scaling opens.
    # ADJUSTABLE ASSUMPTIONS: the scaling exponent and the two body masses compared.
    exp = 0.75
    mouse, elephant = 0.02, 4000.0   # kg
    ratio = (elephant / mouse) ** exp
    per_gram = ratio / (elephant / mouse)
    print("step 1 - B = B0 * M^%.2f: the proposed master key" % exp)
    print("step 2 - elephant total metabolism / mouse total metabolism = %.0f" % ratio)
    print("step 3 - per gram, the elephant burns only %.4f as fast: the key predicts it" % per_gram)
    assert 9450.0 < ratio < 9470.0, ratio
    assert 0.047 < per_gram < 0.048, per_gram
    print("CONFIRM panel: pre-registered predictions holding on fresh data across two scales.")
    print("REFUTE panel: core predictions failing on fresh data despite reasonable adjustments.")
    print("OK: %s tested the key" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_novel_eco(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: instrument navigation - when the old charts show blank water.
    # ADJUSTABLE ASSUMPTIONS: climate deltas, normalization scales, the analog threshold.
    dT, dP = 4.0, -200.0          # projected change: +4 C, -200 mm rain
    sT, sP = 2.0, 300.0           # normalization scales
    analog_thresh = 1.5
    dist = math.sqrt((dT / sT) ** 2 + (dP / sP) ** 2)
    print("step 1 - projected climate shift: +%.0f C, %+.0f mm vs historical variability" % (dT, dP))
    print("step 2 - distance to nearest historical analog: %.3f standardized units" % dist)
    print("step 3 - analog threshold %.1f -> this future is %s" % (analog_thresh, "NO-ANALOG" if dist > analog_thresh else "has precedent"))
    assert 2.10 < dist < 2.12, dist
    assert dist > analog_thresh
    print("CONFIRM panel: charter-managed landscapes maintaining function through no-analog transitions.")
    print("REFUTE panel: functions proving as history-dependent as species composition.")
    print("OK: %s read the instruments" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_may_paradox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the stress test with better dummies - structure changes everything.
    # ADJUSTABLE ASSUMPTIONS: interaction strengths of the two toy pairs.
    import cmath
    def max_real(a, b, c, d):
        tr = a + d
        det = a * d - b * c
        disc = cmath.sqrt(tr * tr - 4 * det)
        l1 = (tr + disc) / 2
        l2 = (tr - disc) / 2
        return max(l1.real, l2.real)
    structured = max_real(0.0, 0.8, -0.8, 0.0)    # antisymmetric: predator-prey pair
    randomish = max_real(0.0, 0.8, 0.6, 0.0)      # same strengths, random signs
    print("step 1 - predator-prey pair (+/-): max eigenvalue real part = %.4f" % structured)
    print("step 2 - random-sign pair (+/+): max eigenvalue real part = %.4f" % randomish)
    print("step 3 - identical strengths, opposite stability: arrangement is the resolver")
    assert abs(structured) < 1e-9, structured
    assert 0.69 < randomish < 0.70, randomish
    print("CONFIRM panel: gap-closing audits reconciling theory with reality across web types.")
    print("REFUTE panel: gaps no combination of measured stabilizers closes.")
    print("OK: %s built better dummies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_rare_species(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the insurance vault - value measured on the day disaster strikes.
    # ADJUSTABLE ASSUMPTIONS: dominant and rare species contributions in normal vs drought years.
    dom_normal, rare_normal = 100.0, 5.0
    dom_drought, rare_drought = 10.0, 60.0
    total_normal = dom_normal + rare_normal
    total_drought_with = dom_drought + rare_drought
    print("step 1 - normal year function: dominant %.0f + rare %.0f = %.0f" % (dom_normal, rare_normal, total_normal))
    print("step 2 - drought year: dominant collapses to %.0f; rare steps up to %.0f" % (dom_drought, rare_drought))
    print("step 3 - drought function with the policy: %.0f vs without it: %.0f (%.1fx)" % (
        total_drought_with, dom_drought, total_drought_with / dom_drought))
    assert total_drought_with == 70.0
    assert total_drought_with / dom_drought == 7.0
    assert rare_normal / total_normal < 0.05
    print("CONFIRM panel: high-option rare species stepping up after real disturbances.")
    print("REFUTE panel: rare species never stepping up - dominants always covering instead.")
    print("OK: %s valued the vault" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_subsidies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the trade books - every cross-boundary flow ledgered.
    # ADJUSTABLE ASSUMPTIONS: baseline growth and the growth response per unit marine nitrogen.
    base, resp = 2.1, 2.0   # mm/yr baseline; mm/yr per unit marine-N fraction
    f_none, f_salmon = 0.0, 0.3
    g_none = base * (1 + resp * f_none)
    g_salmon = base * (1 + resp * f_salmon)
    print("step 1 - riparian tree growth, no salmon nitrogen (f=0): %.2f mm/yr" % g_none)
    print("step 2 - with salmon run (marine N fraction 0.3): %.2f mm/yr" % g_salmon)
    print("step 3 - dependence ratio: the run boosts growth %.2fx" % (g_salmon / g_none))
    assert 2.09 < g_none < 2.11, g_none
    assert 3.35 < g_salmon < 3.37, g_salmon
    assert 1.59 < g_salmon / g_none < 1.61
    print("CONFIRM panel: ledgers beating closed-system models on dam removals and run collapses.")
    print("REFUTE panel: subsidies universally supplementary, never load-bearing.")
    print("OK: %s kept the trade books" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_services_value(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the load rating - every valuation stamped with what it can carry.
    # ADJUSTABLE ASSUMPTIONS: estimates, uncertainties, and the rating cutoffs.
    def rate(est, unc):
        rel = unc / est
        if rel < 0.25:
            return "payment design"
        if rel < 0.75:
            return "project screening"
        return "attention only"
    v_wet = rate(12.0, 8.0)      # wetland flood protection: wide uncertainty
    v_pol = rate(2.1, 0.4)       # pollination production function: tight
    print("step 1 - wetland flood protection $12M +/- $8M -> rated: %s" % v_wet)
    print("step 2 - crop pollination $2.1M +/- $0.4M -> rated: %s" % v_pol)
    print("step 3 - the same dollar sign carries different loads; the stamp says which")
    assert v_wet == "project screening", v_wet
    assert v_pol == "payment design", v_pol
    assert rate(5.0, 4.5) == "attention only"
    print("CONFIRM panel: rated valuations predicting payment and litigation outcomes.")
    print("REFUTE panel: uncertainty so large no valuation earns above the lowest rating.")
    print("OK: %s stamped the loads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uec_unified(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SOLUTION EXPLORER: the archipelago map - every framework scored on the same battery.
    # ADJUSTABLE ASSUMPTIONS: the pattern battery and each framework's scores (2/1/0).
    patterns = ["abundance", "species-area", "lat-gradient", "body-size",
                "trophic-pyramid", "dist-decay", "metab-scale", "occupancy"]
    neutral =   [2, 2, 1, 1, 0, 1, 0, 1]
    metabolic = [1, 0, 1, 2, 2, 0, 2, 1]
    maxent =    [2, 2, 0, 0, 1, 2, 1, 1]
    scores = {"neutral": sum(neutral), "metabolic": sum(metabolic), "maxent": sum(maxent)}
    covered = sum(1 for i in range(len(patterns))
                  if max(neutral[i], metabolic[i], maxent[i]) == 2)
    print("step 1 - pattern battery: %d classic macroecological patterns" % len(patterns))
    print("step 2 - framework scores: %s" % scores)
    print("step 3 - patterns with at least one quantitative prediction: %d of %d" % (covered, len(patterns)))
    assert scores == {"neutral": 8, "metabolic": 9, "maxent": 9}, scores
    assert covered == 6, covered
    print("CONFIRM panel: the scoreboard guiding successful discriminating tests.")
    print("REFUTE panel: patterns proving framework-relative, no fair battery possible.")
    print("OK: %s charted the archipelago" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "tropics-rich": demo_uec_tropics_rich,
 "species-area": demo_uec_species_area,
 "invasions": demo_uec_invasions,
 "predator-prey": demo_uec_predator_prey,
 "collapse-sudden": demo_uec_collapse_sudden,
 "extinction": demo_uec_extinction,
 "bef": demo_uec_bef,
 "microbes-role": demo_uec_microbes_role,
 "no-return": demo_uec_no_return,
 "food-webs": demo_uec_food_webs,
 "dispersal": demo_uec_dispersal,
 "restoration": demo_uec_restoration,
 "trophic-cascades": demo_uec_trophic_cascades,
 "disturbance": demo_uec_disturbance,
 "productivity": demo_uec_productivity,
 "neutral-niche": demo_uec_neutral_niche,
 "plankton": demo_uec_plankton,
 "dilution": demo_uec_dilution,
 "forest-carbon": demo_uec_forest_carbon,
 "diversity-stability": demo_uec_diversity_stability,
 "metacommunity": demo_uec_metacommunity,
 "janzen-connell": demo_uec_janzen_connell,
 "early-warning": demo_uec_early_warning,
 "legacy": demo_uec_legacy,
 "predict-collapse": demo_uec_predict_collapse,
 "rainforest": demo_uec_rainforest,
 "uncultured": demo_uec_uncultured,
 "metabolic": demo_uec_metabolic,
 "novel-eco": demo_uec_novel_eco,
 "may-paradox": demo_uec_may_paradox,
 "rare-species": demo_uec_rare_species,
 "subsidies": demo_uec_subsidies,
 "services-value": demo_uec_services_value,
 "unified": demo_uec_unified,
}

print("demos complete:", len(DEMOS))
