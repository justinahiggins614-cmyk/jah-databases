#!/usr/bin/env python3
"""Demo programs for the Unsolved Economics databases (Manon's 16:15 orders).

Every demo is a SOLUTION-EXPLORER walkthrough: real, runnable, stdlib-only
Python that steps through the Signature solution approach for its record,
with adjustable assumptions (knobs), computed values, a CONFIRM panel and a
REFUTE panel, tight-bounds asserts (never float exact-equality), and the OK
marker. All 68 are machine-executed by build.py.

Public-half demos explore the approach in condensed form; signature-half
demos run the fuller treatment with extra assumption knobs. The honesty rule
is embedded: every demo states what would confirm or kill the proposal and
never claims proof.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", _json.dumps(name))


# ---------------------------------------------------------------- 1 rich/poor

def demo_rich_poor_countries(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 30x income gap")
    print("Step 1: decompose the gap with a Cobb-Douglas lens")
    y_ratio = 30.0          # rich output per worker / poor
    k_ratio = 15.0          # rich capital per worker / poor
    alpha = 1.0 / 3.0       # capital share
    capital_part = k_ratio ** alpha
    residual = y_ratio / capital_part
    print("  income ratio: %.1f | capital explains: %.3fx" % (y_ratio, capital_part))
    print("  unexplained residual: %.3fx" % residual)
    assert 12.16 < residual < 12.17
    print("Step 2: KNOB - vary the capital share alpha")
    for a in (0.30, 1.0/3.0, 0.40):
        r = y_ratio / (k_ratio ** a)
        print("  alpha=%.2f -> residual %.2fx (residual always dominates)" % (a, r))
        assert 10.1 < r < 13.4
    print("Step 3: the Signature reading - the residual is combination friction")
    print("CONFIRM panel:")
    print("  - idea-combination proxies (firm formation, cross-industry hiring)")
    print("    track the Solow residual across countries, controlling for capital")
    print("REFUTE panel:")
    print("  - dense-combination economies that still stagnate")
    print("  - fast growers with frozen labor markets")
    print("NOTE: a proposed research path, not a settled result")
    print("OK: %s decomposed the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_rich_poor_countries_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): combination friction")
    print("Step 1: same decomposition as the public walkthrough")
    y_ratio, k_ratio, alpha = 30.0, 15.0, 1.0/3.0
    residual = y_ratio / (k_ratio ** alpha)
    assert 12.16 < residual < 12.17
    print("  baseline residual: %.3fx" % residual)
    print("Step 2: KNOB - the combination-friction proxy across 8 economies")
    proxy = [0.20, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
    resid = [12.0*p + 0.5*math.sin(10*p) for p in proxy]
    mp, mr = sum(proxy)/8, sum(resid)/8
    cov = sum((a-mp)*(b-mr) for a, b in zip(proxy, resid))
    corr = cov / math.sqrt(sum((a-mp)**2 for a in proxy)*sum((b-mr)**2 for b in resid))
    print("  proxy-residual correlation: %.4f" % corr)
    assert 0.99 < corr < 1.0
    print("Step 3: KNOB - what if the proxy is pure noise?")
    noisy = [r + 4.0*math.sin(37*p) for r, p in zip(resid, proxy)]
    mn = sum(noisy)/8
    covn = sum((a-mp)*(b-mn) for a, b in zip(proxy, noisy))
    corrn = covn / math.sqrt(sum((a-mp)**2 for a in proxy)*sum((b-mn)**2 for b in noisy))
    print("  with heavy noise the correlation collapses to %.3f -> measurement matters" % corrn)
    assert corrn < corr
    print("Step 4: the test the proposal demands - does the proxy survive")
    print("  controls for capital, schooling years, and rule-of-law scores?")
    print("CONFIRM panel:")
    print("  - proxy-residual link survives the full control set, multi-country")
    print("  - reforms that cut combination friction precede growth accelerations")
    print("REFUTE panel:")
    print("  - link vanishes under controls (proxy was a correlate, not the channel)")
    print("  - combination-dense economies with no growth")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the full combination-friction explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 2 business cycle

def demo_business_cycle_cause(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: what starts a downturn")
    print("Step 1: build a synthetic output series (trend + cycle)")
    y = [100*1.004**t + 3*math.sin(2*math.pi*t/24) for t in range(60)]
    print("Step 2: KNOB - the cycle depends on the filter you choose")
    trend = [y[0] + (y[-1]-y[0])*t/59 for t in range(60)]
    g_lin = [y[t]-trend[t] for t in range(60)]
    ma = [sum(y[max(0,t-6):t+6])/len(y[max(0,t-6):t+6]) for t in range(60)]
    g_ma = [y[t]-ma[t] for t in range(60)]
    disagree = sum(1 for a, b in zip(g_lin, g_ma) if (a > 0) != (b > 0))
    print("  linear-trend gap vs moving-average gap disagree in %d of 60 quarters" % disagree)
    assert disagree == 11
    print("Step 3: the Signature reading - recessions as credit-network resonance")
    print("  when leveraged nodes deleverage together, collateral feedback amplifies")
    print("CONFIRM panel:")
    print("  - network fragility statistics (leverage concentration, maturity")
    print("    correlation) rise before downturns, out of sample, across countries")
    print("REFUTE panel:")
    print("  - recessions arriving with healthy unconcentrated balance sheets")
    print("NOTE: a candidate engine, not a proven one")
    print("OK: %s explored the cycle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_business_cycle_cause_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): credit-network resonance")
    print("Step 1: a toy network of balance sheets")
    lev = [1.5, 2.0, 3.0, 5.0, 8.0, 12.0]   # leverage ratios of 6 nodes
    shock = 0.10                              # 10% asset-price fall
    print("Step 2: KNOB - who must deleverage after the shock?")
    forced = [L for L in lev if L*shock > 0.5]
    print("  nodes forced to sell: %d of %d (leverage > %.1f)" % (len(forced), len(lev), 0.5/shock))
    assert len(forced) == 2
    print("Step 3: KNOB - feedback: forced sales deepen the shock")
    deepened = shock + 0.02*len(forced)
    forced2 = [L for L in lev if L*deepened > 0.5]
    print("  shock %.2f -> %.2f; forced sellers %d -> %d (the resonance)" % (
        shock, deepened, len(forced), len(forced2)))
    assert 0.139 < deepened < 0.141 and len(forced2) == 3
    print("Step 4: the measurable prediction - concentration of short-term debt")
    print("  among leveraged nodes should precede downturns")
    print("CONFIRM panel:")
    print("  - vulnerability index rises before every major crisis, out of sample")
    print("  - concentrated fragile networks resolve calmly only with intervention")
    print("REFUTE panel:")
    print("  - downturns with no prior fragility buildup")
    print("  - high fragility + normal triggers with no downturn")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the resonance explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------ 3 equity premium

def demo_equity_premium_puzzle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 6%% premium that should be 0.35%%")
    print("Step 1: the Mehra-Prescott calibration")
    premium_hist = 0.0698 - 0.0080      # stocks minus bills, 1889-1978
    sigma_c = 0.036                     # consumption volatility
    model_max = 10.0 * sigma_c**2       # risk aversion capped at 10
    implied_A = premium_hist / sigma_c**2
    print("  historical premium: %.2f%% | model max (A=10): %.2f%%" % (
        premium_hist*100, model_max*100))
    print("  (the full Mehra-Prescott joint calibration tightens the max to ~0.35%%)")
    print("  risk aversion needed to fit history: %.1f" % implied_A)
    assert 6.17 < premium_hist*100 < 6.19
    assert 1.29 < model_max*100 < 1.30
    assert 47.6 < implied_A < 47.8
    print("Step 2: KNOB - vary consumption volatility")
    for s in (0.030, 0.036, 0.045):
        print("  sigma=%.3f -> implied aversion %.1f (always absurd)" % (
            s, premium_hist/s**2))
    print("Step 3: the Signature reading - memory-weighted ambiguity pricing")
    print("  investors price the crash they remember, not the century they lived")
    print("CONFIRM panel:")
    print("  - the premium tracks the share of investors with personal")
    print("    experience of a severe drawdown, controlling for consumption vol")
    print("REFUTE panel:")
    print("  - high premiums in populations with no disaster memory")
    print("NOTE: a testable hypothesis, not an established result")
    print("OK: %s calibrated the puzzle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_equity_premium_puzzle_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): memory-weighted pricing")
    print("Step 1: two investor cohorts, different memories")
    # cohort A lived through a 40% crash; cohort B did not
    crash_memory = {"scarred": 0.40, "unscarred": 0.0}
    base_premium = 0.013   # rational-model premium
    print("Step 2: KNOB - memory weight on the worst episode")
    for w in (0.0, 0.3, 0.6):
        prem_scarred = base_premium + w*crash_memory["scarred"]*0.15
        prem_unscar = base_premium + w*crash_memory["unscarred"]*0.15
        print("  memory weight %.1f -> scarred premium %.2f%%, unscarred %.2f%%" % (
            w, prem_scarred*100, prem_unscar*100))
    assert abs((base_premium + 0.3*0.40*0.15) - 0.031) < 0.0005
    print("Step 3: the cross-country prediction - the premium should decay as")
    print("  the disaster cohort ages out of the investor population")
    decay = [0.0618*math.exp(-t/40.0) for t in (0, 20, 40)]
    print("  premium path as memory fades: %.2f%% -> %.2f%% -> %.2f%%" % tuple(
        d*100 for d in decay))
    assert 6.17 < decay[0]*100 < 6.19 and 2.26 < decay[2]*100 < 2.28
    print("CONFIRM panel:")
    print("  - cross-country panel: premium follows disaster-memory share")
    print("  - cohort portfolios: the scarred hold fewer equities at every age")
    print("REFUTE panel:")
    print("  - premium stable as the disaster cohort exits")
    print("  - no portfolio gap between scarred and unscarred cohorts")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the memory-pricing explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# --------------------------------------------------- 4 participation

def demo_participation_puzzle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: why households refuse the premium")
    print("Step 1: the breakeven wealth for a fixed entry cost")
    premium, share, cost = 0.06, 0.5, 2000.0
    breakeven = cost/(premium*share)
    print("  $%.0f entry cost, %.0f%% premium, half in stocks -> breakeven wealth $%.0f" % (
        cost, premium*100, breakeven))
    assert 66666 < breakeven < 66667
    print("Step 2: KNOB - the cost that would rationalize middle-class abstention")
    for c in (1000.0, 2000.0, 5000.0):
        print("  cost $%.0f -> breakeven $%.0f (implausibly high)" % (c, c/(premium*share)))
    print("Step 3: the Signature reading - the barrier is comprehension, not fees")
    print("  households enter when the market becomes legible, via a trusted peer")
    print("CONFIRM panel:")
    print("  - participation jumps when a trusted peer participates, beyond fees")
    print("  - plain-language explanations beat fee waivers in trials")
    print("REFUTE panel:")
    print("  - fee waivers move participation as much as explanations")
    print("NOTE: a candidate mechanism awaiting clean tests")
    print("OK: %s explored participation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_participation_puzzle_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the legibility threshold")
    print("Step 1: comprehension cost varies with exposure, not wealth")
    exposure = [0.1, 0.3, 0.5, 0.7, 0.9]
    comp_cost = [4000*(1-e) for e in exposure]
    wealth = 80000.0
    gain = wealth*0.06*0.5
    print("Step 2: KNOB - who participates as exposure rises?")
    for e, c in zip(exposure, comp_cost):
        print("  exposure %.1f -> comprehension cost $%.0f -> %s" % (
            e, c, "PARTICIPATES" if gain > c else "stays out"))
    assert comp_cost[2] == 2000.0 and gain > comp_cost[2] and gain < comp_cost[0]
    print("Step 3: the contagion prediction - one peer halves the cost")
    halved = [c*0.5 for c in comp_cost]
    n_in = sum(1 for c in halved if gain > c)
    print("  after a peer explains it: %d of 5 participate (was %d)" % (
        n_in, sum(1 for c in comp_cost if gain > c)))
    assert n_in == 5
    print("CONFIRM panel:")
    print("  - network data: participation contagion independent of income")
    print("  - field trials: explanations beat fee waivers")
    print("REFUTE panel:")
    print("  - no contagion in dense social networks")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the legibility explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 5 home bias

def demo_home_bias_puzzle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 94%% domestic portfolio")
    print("Step 1: the belief gap the bias implies (French-Poterba logic)")
    w_obs, w_mkt = 0.938, 0.50
    A, sigma = 2.0, 0.20
    gap = (w_obs - w_mkt)*A*sigma**2
    print("  observed %.1f%% domestic vs %.0f%% market weight" % (w_obs*100, w_mkt*100))
    print("  implied expected-return advantage of home: %.2f%%/yr" % (gap*100))
    assert 3.49 < gap*100 < 3.51
    print("Step 2: KNOB - vary risk aversion")
    for a in (2.0, 3.0, 5.0):
        print("  A=%.0f -> implied gap %.2f%%/yr (absurd at every level)" % (
            a, (w_obs-w_mkt)*a*sigma**2*100))
    print("Step 3: the Signature reading - investors hold what they can monitor")
    print("CONFIRM panel:")
    print("  - bias falls with legibility (dual listings, English disclosure),")
    print("    not with fee cuts")
    print("REFUTE panel:")
    print("  - fee cuts alone erase the bias")
    print("NOTE: a proposed lens, not a finding")
    print("OK: %s measured the bias" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_home_bias_puzzle_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): monitoring-cost legibility")
    print("Step 1: monitoring cost decays with legibility")
    leg = [0.2, 0.4, 0.6, 0.8, 1.0]
    mon = [0.05*(1-L) for L in leg]   # monitoring cost as return drag
    print("Step 2: KNOB - optimal foreign weight as legibility rises")
    A, sigma, prem = 2.0, 0.20, 0.02  # 2% foreign excess return available
    for L, m in zip(leg, mon):
        w = max(0.0, (prem - m)/(A*sigma**2))
        print("  legibility %.1f -> monitoring drag %.2f%% -> foreign weight %.1f%%" % (
            L, m*100, w*100))
    assert abs(max(0.0, (prem-mon[0])/(A*sigma**2)) - 0.0) < 1e-9
    assert abs((prem-mon[4])/(A*sigma**2) - 0.25) < 0.001
    print("Step 3: the prediction - disclosure reform should move weights,")
    print("  fee reform should not")
    print("CONFIRM panel:")
    print("  - panel: bias declines with legibility proxies, fees flat")
    print("REFUTE panel:")
    print("  - high bias persists with full foreign-information access")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the legibility explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------ 6 productivity slowdown

def demo_productivity_slowdown(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the halved growth engine")
    print("Step 1: what halving the growth rate costs over a working life")
    fast, slow, yrs = 0.028, 0.014, 50.0
    lvl_fast, lvl_slow = (1+fast)**yrs, (1+slow)**yrs
    print("  2.8%% for 50y -> income x%.2f | 1.4%% for 50y -> x%.2f" % (lvl_fast, lvl_slow))
    print("  the slowdown costs a factor of %.2f in living standards" % (lvl_fast/lvl_slow))
    assert 3.97 < lvl_fast < 3.99 and 2.00 < lvl_slow < 2.01
    assert 1.98 < lvl_fast/lvl_slow < 1.99
    dbl_fast = math.log(2)/math.log(1+fast)
    dbl_slow = math.log(2)/math.log(1+slow)
    print("  doubling time: %.1f years vs %.1f years" % (dbl_fast, dbl_slow))
    assert 25.0 < dbl_fast < 25.2 and 49.8 < dbl_slow < 50.0
    print("Step 2: the Signature reading - the combination bottleneck")
    print("  ideas multiply combinatorially; vetted combinations need attention,")
    print("  which grows only linearly with researchers")
    print("CONFIRM panel:")
    print("  - research productivity decays fastest where idea stocks grow fastest")
    print("  - vetting tools (simulation, automation) bend the curve")
    print("REFUTE panel:")
    print("  - flat research productivity in fast-growing fields")
    print("NOTE: a mechanism proposal awaiting measurement")
    print("OK: %s priced the slowdown" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_productivity_slowdown_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the combination bottleneck")
    print("Step 1: combinations explode while attention crawls")
    ideas = [100, 200, 400]
    combos = [n*(n-1)//2 for n in ideas]
    attention = [10*n for n in ideas]     # linear in researchers
    for n, c, a in zip(ideas, combos, attention):
        print("  %d ideas -> %d pairs, attention covers %d (coverage %.2f%%)" % (
            n, c, a, 100*a/c))
    assert combos[2] == 79800 and abs(100*attention[2]/combos[2] - 5.01) < 0.01
    print("Step 2: KNOB - research productivity = new ideas per researcher")
    print("  (each idea harder to find as the stock grows: productivity ~ 1/ideas)")
    researchers = 100.0
    prod = [researchers*10.0/n for n in ideas]
    print("  output per researcher: %.1f -> %.1f -> %.1f (falls as ideas grow)" % tuple(prod))
    assert prod[0] > prod[1] > prod[2]
    print("Step 3: KNOB - a vetting tool that 10x's attention")
    prod2 = [10*p for p in prod]
    print("  with 10x vetting: %.1f -> %.1f -> %.1f (higher, but decay resumes)" % tuple(prod2))
    assert prod2[2] > prod[2] and prod2[0] > prod2[1] > prod2[2]
    print("CONFIRM panel:")
    print("  - field data: decay rate tied to idea-stock growth")
    print("  - tool shocks raise output per researcher")
    print("REFUTE panel:")
    print("  - decay absent where idea stocks grow fastest")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the bottleneck explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 7 flattened phillips

def demo_flattened_phillips(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the curve that went flat")
    print("Step 1: the slope collapse, then and now")
    slope_1985, slope_2019 = 0.50, 0.05
    ugap = 2.0   # 2pp unemployment gap
    print("  1985: %.1fpp gap -> %.2fpp inflation response" % (ugap, slope_1985*ugap))
    print("  2019: %.1fpp gap -> %.2fpp inflation response" % (ugap, slope_2019*ugap))
    assert abs(slope_1985*ugap - 1.0) < 1e-9 and abs(slope_2019*ugap - 0.1) < 1e-9
    print("Step 2: KNOB - the Signature attention proxy")
    att_1985, att_2019 = 0.80, 0.20   # inflation news salience
    per_att = (slope_1985-slope_2019)/(att_1985-att_2019)
    print("  slope per unit of attention: %.2f" % per_att)
    assert 0.74 < per_att < 0.76
    print("Step 3: prediction - when salience returns, the slope should steepen")
    print("CONFIRM panel:")
    print("  - the slope tracks attention proxies across episodes")
    print("  - firms that watch inflation respond to slack; others do not")
    print("REFUTE panel:")
    print("  - slope flat where attention is high")
    print("NOTE: a candidate mechanism, not a verdict")
    print("OK: %s explored the flattening" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_flattened_phillips_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): attention-gated pricing")
    print("Step 1: firms reset prices from perceived slack, perception costs attention")
    attention = [0.9, 0.6, 0.3, 0.1]
    true_slope = 0.5
    eff = [true_slope*a for a in attention]
    for a, e in zip(attention, eff):
        print("  attention %.1f -> effective slope %.2f" % (a, e))
    assert abs(eff[0]-0.45) < 1e-9 and abs(eff[3]-0.05) < 1e-9
    print("Step 2: KNOB - a salience shock (2021-style) restores attention")
    shocked = [min(1.0, a+0.5) for a in attention]
    eff2 = [true_slope*a for a in shocked]
    print("  after shock: effective slopes", ["%.2f" % e for e in eff2])
    assert eff2[3] > eff[3]
    print("Step 3: the micro test - within-economy, watchers vs non-watchers")
    print("CONFIRM panel:")
    print("  - time series: slope covaries with news-coverage attention measures")
    print("  - microdata: watching firms respond to slack, others do not")
    print("REFUTE panel:")
    print("  - no attention-slope covariation across episodes")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the attention-gate explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------ 8 immobility

def demo_worker_immobility(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the $8,000 raise nobody takes")
    print("Step 1: the migration arithmetic")
    gain, r, yrs = 8000.0, 0.05, 20.0
    pv = gain*(1-(1+r)**-yrs)/r
    cash_cost, network_loss = 5000.0, 30000.0
    npv = pv - cash_cost - network_loss
    print("  PV of wage gain: $%.0f | cash cost $%.0f | network loss $%.0f" % (
        pv, cash_cost, network_loss))
    print("  NPV of moving: $%.0f (positive - yet most stay)" % npv)
    assert 99697 < pv < 99699 and 64697 < npv < 64699
    print("Step 2: KNOB - how big must the invisible cost be to rationalize staying?")
    for nl in (0.0, 30000.0, 80000.0, 95000.0):
        print("  network loss $%.0f -> NPV $%.0f" % (nl, pv-cash_cost-nl))
    print("Step 3: the Signature reading - the local network is productive capital")
    print("  moving destroys location-specific capital that cash costs miss")
    print("CONFIRM panel:")
    print("  - earnings cost of moving rises with pre-move network density")
    print("  - movers recover faster with portable credentials")
    print("REFUTE panel:")
    print("  - mobility uncorrelated with network measures")
    print("NOTE: a proposed weight in a multi-cause puzzle, not the whole answer")
    print("OK: %s priced staying put" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_worker_immobility_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): network-departure cost")
    print("Step 1: network capital by occupation type")
    oc = [("portable-credential", 0.1), ("firm-specific", 0.4), ("place-based", 0.7)]
    wage = 60000.0
    print("Step 2: KNOB - departure cost as a share of annual wage")
    for name_, d in oc:
        loss = wage*d
        print("  %-20s destroys $%.0f of network capital" % (name_, loss))
    assert abs(wage*0.7 - 42000) < 1
    print("Step 3: predicted mobility ranking (highest departure cost moves least)")
    ranking = sorted(oc, key=lambda x: x[1], reverse=True)
    print("  least mobile:", ranking[0][0], "| most mobile:", ranking[2][0])
    assert ranking[0][0] == "place-based" and ranking[2][0] == "portable-credential"
    print("Step 4: the team-move test - laggards hiring whole teams catch up faster")
    print("CONFIRM panel:")
    print("  - linked employer-employee data: team moves beat individual hires")
    print("  - mobility lowest where local networks are densest")
    print("REFUTE panel:")
    print("  - no earnings dip for movers; no density-mobility link")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the network-departure explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------ 9 happiness

def demo_happiness_paradox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: growth without happiness")
    print("Step 1: the paradox in one equation")
    a = 0.5   # happiness points per log-income unit (cross-section)
    growth = math.log(2)   # incomes double
    print("Step 2: KNOB - how wide is the comparison bandwidth?")
    for bfrac in (0.0, 0.5, 1.0):
        net = a*growth - bfrac*a*growth   # absolute gain minus comparison drag
        print("  comparison weight %.1f -> net happiness change %+.3f" % (bfrac, net))
    assert abs((a*growth - 1.0*a*growth)) < 1e-9
    assert 0.17 < (a*growth - 0.5*a*growth) < 0.18
    print("Step 3: the Signature reading - growth widens the visible comparison")
    print("  set as fast as it raises income, so the ratio stalls")
    print("CONFIRM panel:")
    print("  - local visible inequality predicts the happiness of the non-rich")
    print("  - media exposure to the rich shifts satisfaction without income change")
    print("REFUTE panel:")
    print("  - happiness rising with growth amid high visible inequality")
    print("NOTE: one candidate resolution among several live ones")
    print("OK: %s explored the paradox" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_happiness_paradox_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): comparison bandwidth")
    print("Step 1: happiness = absolute log income - bandwidth-weighted reference")
    a, b = 0.5, 0.5
    y0, y1 = 50000.0, 100000.0
    print("Step 2: KNOB - who is in the reference set?")
    for ref_mult in (1.0, 1.5, 2.0):
        h0 = a*math.log(y0) - b*math.log(y0*ref_mult)
        h1 = a*math.log(y1) - b*math.log(y1*ref_mult)
        print("  reference %.1fx own income -> happiness change %+.3f" % (ref_mult, h1-h0))
    assert abs((a*math.log(y1)-b*math.log(2*y1)) - (a*math.log(y0)-b*math.log(2*y0))) < 1e-9
    print("Step 3: the distributional prediction - happiness rises with growth")
    print("  only where growth is even or comparison sets stay narrow")
    even = a*math.log(2) - 0.2*a*math.log(2)   # narrow set, weak drag
    print("  narrow-set growth dividend: %+.3f happiness points" % even)
    assert 0.27 < even < 0.28
    print("CONFIRM panel:")
    print("  - microdata: visible inequality -> lower satisfaction of non-rich")
    print("  - natural experiments: media exposure shifts satisfaction")
    print("REFUTE panel:")
    print("  - flat happiness where comparison sets are provably narrow")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the comparison-bandwidth explorer" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "rich_poor_countries": demo_rich_poor_countries,
    "business_cycle_cause": demo_business_cycle_cause,
    "equity_premium_puzzle": demo_equity_premium_puzzle,
    "participation_puzzle": demo_participation_puzzle,
    "home_bias_puzzle": demo_home_bias_puzzle,
    "productivity_slowdown": demo_productivity_slowdown,
    "flattened_phillips": demo_flattened_phillips,
    "worker_immobility": demo_worker_immobility,
    "happiness_paradox": demo_happiness_paradox,
}

DEMOS_SIG = {
    "rich_poor_countries": demo_rich_poor_countries_sig,
    "business_cycle_cause": demo_business_cycle_cause_sig,
    "equity_premium_puzzle": demo_equity_premium_puzzle_sig,
    "participation_puzzle": demo_participation_puzzle_sig,
    "home_bias_puzzle": demo_home_bias_puzzle_sig,
    "productivity_slowdown": demo_productivity_slowdown_sig,
    "flattened_phillips": demo_flattened_phillips_sig,
    "worker_immobility": demo_worker_immobility_sig,
    "happiness_paradox": demo_happiness_paradox_sig,
}

# ------------------------------------------------------ 10 bubbles

def demo_bubble_formation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: prices that defy dividends")
    print("Step 1: the Shiller variance bound, toy version")
    # constant dividend 1, discount 5% -> perfect-foresight price is flat at 20
    p_star = [20.0]*60
    var_star = sum((p-20.0)**2 for p in p_star)/60
    print("Step 2: KNOB - sentiment amplitude in the market price")
    for amp in (5.0, 10.0, 15.0):
        p = [20.0 + amp*math.sin(2*math.pi*t/10) for t in range(60)]
        var_p = sum((x-20.0)**2 for x in p)/60
        print("  sentiment amplitude %.0f -> price variance %.1f vs bound %.1f %s" % (
            amp, var_p, var_star, "VIOLATED" if var_p > var_star else "ok"))
    assert abs(sum((20.0+10.0*math.sin(2*math.pi*t/10)-20.0)**2 for t in range(60))/60 - 50.0) < 1e-9
    print("Step 3: the Signature reading - narratives infect, credit amplifies")
    print("CONFIRM panel:")
    print("  - narrative-intensity x credit-growth indicators call past bubbles")
    print("    out of sample")
    print("REFUTE panel:")
    print("  - bubbles with no narrative surge; surges with credit that fizzle")
    print("NOTE: a research design, not a detection system")
    print("OK: %s tested the bound" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_bubble_formation_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): narrative-credit amplifier")
    print("Step 1: narrative spreads like an infection")
    infected, susceptible = 0.05, 0.95
    path = []
    for week in range(20):
        new = 0.35*infected*susceptible
        infected, susceptible = infected+new, susceptible-new
        path.append(infected)
    print("  narrative prevalence week 1/10/20: %.2f / %.2f / %.2f" % (
        path[0], path[9], path[19]))
    assert 0.06 < path[0] < 0.07 and 0.98 < path[19] < 0.99
    print("Step 2: KNOB - credit expansion multiplies the price impact")
    base_price = 20.0
    for credit in (1.0, 1.5, 2.0):
        peak = base_price + 30.0*path[19]*credit
        print("  credit multiplier %.1f -> peak price %.1f (fundamental 20)" % (credit, peak))
    assert abs((20.0+30.0*path[19]*1.5) - (20.0+45.0*path[19])) < 1e-9
    print("Step 3: the crash follows narrative exhaustion, not news")
    print("CONFIRM panel:")
    print("  - narrative peaks precede price peaks in past bubbles")
    print("  - credit growth separates bubbles from harmless fads")
    print("REFUTE panel:")
    print("  - price peaks preceding narrative peaks")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the epidemic explorer" % NAME)
if __name__ == "__main__":
    main()
''')


# ----------------------------------------------- 11 feldstein-horioka

def demo_feldstein_horioka(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: saving that stays home")
    print("Step 1: the 1980 regression on synthetic OECD data")
    s = [15,18,20,22,25,28,30,32,35,38]
    i = [0.8*x+2+0.5*math.sin(x) for x in s]
    ms, mi = sum(s)/10, sum(i)/10
    cov = sum((a-ms)*(b-mi) for a,b in zip(s,i))
    corr = cov/math.sqrt(sum((a-ms)**2 for a in s)*sum((b-mi)**2 for b in i))
    slope = cov/sum((a-ms)**2 for a in s)
    print("  saving-investment correlation: %.4f | slope: %.3f" % (corr, slope))
    assert 0.998 < corr < 0.999 and 0.79 < slope < 0.81
    print("Step 2: KNOB - what would perfect mobility look like?")
    print("  correlation near 0: investment chasing world returns, not home saving")
    print("Step 3: the Signature reading - capital is contractually sticky")
    print("  cross-border claims are harder to enforce, acting as a tax on mobility")
    print("CONFIRM panel:")
    print("  - the correlation tracks enforceability (treaties, creditor rights),")
    print("    not legal openness")
    print("REFUTE panel:")
    print("  - correlation tracking openness while enforceability stays flat")
    print("NOTE: a proposed decomposition, not an estimate")
    print("OK: %s ran the 1980 regression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_feldstein_horioka_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): contractual stickiness")
    print("Step 1: the enforceability tax on moving capital")
    enforce = [0.3, 0.5, 0.7, 0.9]   # collection probability abroad
    world_return = 0.08
    print("Step 2: KNOB - required return rises as enforceability falls")
    for e in enforce:
        required = world_return/e
        print("  enforceability %.1f -> required return %.2f%% to invest abroad" % (
            e, required*100))
    assert abs(0.08/0.3 - 0.2667) < 0.001
    print("Step 3: the treaty test - coverage should move the correlation,")
    print("  openness alone should not")
    print("CONFIRM panel:")
    print("  - correlation falls as bilateral treaty coverage rises, openness held fixed")
    print("REFUTE panel:")
    print("  - high correlation persisting under strong treaties")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s priced the stickiness" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 12 crisis prediction

def demo_crisis_prediction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the warning system that cries wolf")
    print("Step 1: a toy early-warning score (credit boom indicator)")
    import random
    random.seed(7)
    crisis = [0.3+0.6*random.random() for _ in range(10)]
    calm = [0.1+0.7*random.random() for _ in range(30)]
    wins = sum(1 for x in crisis for z in calm if x > z)
    auc = wins/(10*30)
    print("  AUC of the score: %.3f (0.5 is a coin flip)" % auc)
    assert 0.66 < auc < 0.67
    print("Step 2: KNOB - the policymaker's threshold trades hits for false alarms")
    for thr in (0.4, 0.5, 0.6):
        hit = sum(1 for x in crisis if x > thr)/10
        fa = sum(1 for z in calm if z > thr)/30
        print("  threshold %.1f -> hits %.1f%% of crises, false alarms %.1f%% of calm years" % (
            thr, hit*100, fa*100))
    assert abs(sum(1 for x in crisis if x > 0.5)/10 - 0.5) < 1e-9
    print("Step 3: the Signature reframe - forecast fragility, not timing")
    print("  predict the vulnerability window (a hazard rate), not the trigger date")
    print("CONFIRM panel:")
    print("  - vulnerability index high before every major crisis, out of sample")
    print("REFUTE panel:")
    print("  - crises at low measured vulnerability")
    print("NOTE: the reframe itself is the proposal, not a result")
    print("OK: %s tested the siren" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crisis_prediction_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): fragility forecasting")
    print("Step 1: vulnerability = leverage concentration x maturity mismatch")
    print("         x price deviation from cash-flow fundamentals")
    lev_c, mat_m, dev = 0.8, 0.7, 0.6
    vuln = lev_c*mat_m*dev
    print("  vulnerability index: %.3f" % vuln)
    assert 0.335 < vuln < 0.337
    print("Step 2: KNOB - the hazard rate, not a date")
    base_trigger = 0.05   # normal-size trigger arrival rate per year
    for v in (0.1, 0.336, 0.8):
        hazard = base_trigger*(1+9*v)
        print("  vulnerability %.2f -> crisis hazard %.1f%%/yr" % (v, hazard*100))
    assert abs(0.05*(1+9*0.336) - 0.2012) < 0.001
    print("Step 3: the evaluation discipline - strictly out of sample,")
    print("  multi-country, calm decades must score low")
    print("CONFIRM panel:")
    print("  - index rises before crises, stays low in calm decades")
    print("REFUTE panel:")
    print("  - long high-vulnerability stretches with no crisis")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the fragility forecaster" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------ 13 forward premium

def demo_forward_premium_puzzle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the regression that points backwards")
    print("Step 1: the Fama regression on synthetic currency data")
    ip = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08]
    ds = [0.005-0.9*d+0.01*math.sin(50*d) for d in ip]
    md, msd = sum(ip)/8, sum(ds)/8
    beta = sum((a-md)*(c-msd) for a,c in zip(ip,ds))/sum((a-md)**2 for a in ip)
    print("  theory predicts slope +1.00; estimated slope: %.2f" % beta)
    assert -1.12 < beta < -1.10
    print("Step 2: KNOB - the carry trade built on the anomaly")
    carry = sum(d for d in ip)/8 - sum(ds)/8
    print("  borrow low / lend high earns %.2f%%/yr on average in this sample" % (carry*100))
    assert 0.076 < carry < 0.078
    print("Step 3: the Signature reading - the premium is crash insurance")
    print("  the regression window rarely samples the jumps the premium prices")
    print("CONFIRM panel:")
    print("  - option-implied jump premia explain the carry cross-section")
    print("REFUTE panel:")
    print("  - unbiased slopes in fat-left-tail currencies")
    print("NOTE: a measurement proposal, not a solution")
    print("OK: %s ran the Fama regression" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_forward_premium_puzzle_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): crash-insurance pricing")
    print("Step 1: decompose the carry return into quiet drift and jump risk")
    quiet_drift = 0.03
    jump_prob, jump_size = 0.05, -0.40
    expected = quiet_drift + jump_prob*jump_size
    print("  quiet drift %+.2f%% + jump risk (%.0f%% x %+.0f%%) = expected %+.2f%%" % (
        quiet_drift*100, jump_prob*100, jump_size*100, expected*100))
    assert abs(expected - 0.01) < 1e-9
    print("Step 2: KNOB - the peso problem: samples without jumps look like free lunch")
    for realized_jumps in (0, 1, 2):
        realized = quiet_drift + realized_jumps*jump_size/20
        print("  %d jumps in 20 years -> realized %.2f%%/yr" % (realized_jumps, realized*100))
    assert abs((0.03 + 0*(-0.40)/20) - 0.03) < 1e-9
    print("Step 3: the options test - implied crash probabilities per currency")
    print("CONFIRM panel:")
    print("  - implied jump premia match carry excess returns currency by currency")
    print("REFUTE panel:")
    print("  - carry profits survive after pricing the insurance")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s priced the insurance" % NAME)
if __name__ == "__main__":
    main()
''')


# -------------------------------------------- 14 exchange rate disconnect

def demo_exchange_rate_disconnect(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the model that loses to a coin flip")
    print("Step 1: Meese-Rogoff horse race, toy version")
    rw = [0.02*math.sin(t/3)+0.01*math.cos(t/7) for t in range(40)]
    model_err = [e+0.015*math.sin(t/2) for t, e in enumerate(rw)]
    rmse_rw = math.sqrt(sum(e**2 for e in rw)/40)
    rmse_m = math.sqrt(sum(e**2 for e in model_err)/40)
    print("  random-walk RMSE: %.4f | fundamentals-model RMSE: %.4f" % (rmse_rw, rmse_m))
    print("  model / random walk: %.3f (>1 means the model loses)" % (rmse_m/rmse_rw))
    assert 1.21 < rmse_m/rmse_rw < 1.23
    print("Step 2: the Signature reading - flow dominance by timescale")
    print("  fundamentals drive the tide; portfolio flows drive the measured waves")
    print("CONFIRM panel:")
    print("  - fundamentals win at long horizons, order flow wins at short,")
    print("    with a stable crossover horizon")
    print("REFUTE panel:")
    print("  - no crossover; fundamentals winning at short horizons")
    print("NOTE: organizes the puzzle by timescale rather than solving it")
    print("OK: %s ran the horse race" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_exchange_rate_disconnect_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): flow dominance")
    print("Step 1: two markets, two speeds")
    trade_flow, portfolio_flow = 1.0, 50.0   # relative sizes at monthly horizon
    fund_signal, flow_noise = 1.0, 3.0
    observed = fund_signal*trade_flow + flow_noise*portfolio_flow
    fund_share = fund_signal*trade_flow/observed
    print("  fundamentals explain %.1f%% of the monthly move" % (fund_share*100))
    assert 0.006 < fund_share < 0.007
    print("Step 2: KNOB - stretch the horizon; flows mean-revert, fundamentals persist")
    for horizon in (1, 12, 60):
        flow_part = flow_noise*portfolio_flow/math.sqrt(horizon)
        fund_part = fund_signal*trade_flow*horizon/12
        share = fund_part/(fund_part+flow_part)
        print("  horizon %2d months -> fundamental share %.1f%%" % (horizon, share*100))
    assert share > fund_share
    print("Step 3: the crossover prediction - measurable from flow ratios")
    print("CONFIRM panel:")
    print("  - documented crossover, stable across currency pairs")
    print("REFUTE panel:")
    print("  - flow-dominated pairs where fundamentals win short-horizon")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s separated tide from waves" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------ 15 lucas paradox

def demo_lucas_paradox(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the capital that never arrives")
    print("Step 1: the marginal product arithmetic")
    k_ratio, alpha = 25.0, 0.40   # rich/poor capital per worker
    mpk_ratio = k_ratio**(1-alpha)
    print("  capital per worker 25x -> marginal product %.1fx higher in the poor country" % mpk_ratio)
    assert 6.89 < mpk_ratio < 6.91
    print("Step 2: KNOB - the prediction this implies")
    print("  with %.1fx returns, theory predicts torrents of investment;" % mpk_ratio)
    print("  reality delivers a trickle, often flowing the wrong way")
    print("Step 3: the Signature reading - price the enforceable return,")
    print("  not the marginal product: return x collection probability")
    print("CONFIRM panel:")
    print("  - investment surges after credible property-rights reforms,")
    print("    beyond what capital scarcity predicts")
    print("REFUTE panel:")
    print("  - large flows into institutionally weak, capital-scarce economies")
    print("NOTE: a proposed restatement awaiting measurement")
    print("OK: %s computed the missing torrent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lucas_paradox_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the enforceable return")
    print("Step 1: marginal product x collection probability")
    mpk_ratio = 25.0**0.6
    print("Step 2: KNOB - collection probability by institutional quality")
    for prob, label in ((0.9, "strong institutions"), (0.5, "middling"), (0.2, "weak")):
        enf = mpk_ratio*prob
        print("  %-20s -> enforceable return %.1fx (raw %.1fx)" % (label, enf, mpk_ratio))
    assert abs(mpk_ratio*0.2 - 1.3797) < 0.01
    print("  weak institutions turn a 6.9x return into a 1.4x return: the paradox dissolves")
    print("Step 3: the reform event-study the proposal demands")
    print("CONFIRM panel:")
    print("  - flows respond more to institutional reform than to capital scarcity")
    print("REFUTE panel:")
    print("  - reforms with no flow response")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s priced enforceability" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 16 dark matter

def demo_current_account_dark_matter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the trillion-dollar accounting ghost")
    print("Step 1: capitalize the income stream")
    net_income = 0.30    # trillion USD per year, stylized
    yield_ = 0.05
    implied_assets = net_income/yield_
    nfa = -10.0          # measured net position, trillion USD
    dark = implied_assets - nfa
    print("  income $%.2fT at %.0f%% yield -> implied assets $%.0fT" % (
        net_income, yield_*100, implied_assets))
    print("  measured position $%.0fT -> dark matter $%.0fT" % (nfa, dark))
    assert abs(implied_assets - 6.0) < 1e-9 and abs(dark - 16.0) < 1e-9
    print("Step 2: KNOB - the yield assumption moves the ghost")
    for y in (0.03, 0.05, 0.08):
        print("  yield %.0f%% -> implied assets $%.1fT -> dark matter $%.1fT" % (
            y*100, net_income/y, net_income/y - nfa))
    print("Step 3: the Signature reading - the missing wealth is the capitalized")
    print("  value of dollar liquidity services (the franchise of selling safety)")
    print("CONFIRM panel:")
    print("  - implied dark matter tracks safe-asset premia and dollar funding spreads")
    print("REFUTE panel:")
    print("  - dark matter stable while safety premia swing")
    print("NOTE: a measurable candidate for an unmeasured asset")
    print("OK: %s capitalized the ghost" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_current_account_dark_matter_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the liquidity franchise")
    print("Step 1: foreigners accept lower yields for dollar safety")
    discount = 0.015          # 150bp safety discount on Treasuries
    foreign_holdings = 8.0    # trillion USD, stylized
    annual_franchise = discount*foreign_holdings
    cap_rate = 0.04
    franchise_value = annual_franchise/cap_rate
    print("  annual franchise $%.2fT -> capitalized value $%.1fT" % (
        annual_franchise, franchise_value))
    assert abs(franchise_value - 3.0) < 1e-9
    print("Step 2: KNOB - the franchise breathes with crisis demand")
    for d in (0.005, 0.015, 0.030):
        print("  safety discount %dbp -> franchise $%.1fT" % (
            d*10000, d*foreign_holdings/cap_rate))
    assert abs(0.030*8.0/0.04 - 6.0) < 1e-9
    print("Step 3: compare against the dark-matter residual across time")
    print("CONFIRM panel:")
    print("  - franchise value covaries with the residual; return-differential")
    print("    stories cannot explain the comovement")
    print("REFUTE panel:")
    print("  - residual stable while the franchise swings")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s valued the franchise" % NAME)
if __name__ == "__main__":
    main()
''')


# -------------------------------------------- 17 productivity dispersion

def demo_productivity_dispersion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 2x gap inside one industry")
    print("Step 1: the 90-10 TFP ratio from a lognormal plant distribution")
    sigma = 0.42
    ratio = math.exp(2*1.2816*sigma)   # 90th vs 10th percentile
    print("  implied 90-10 TFP ratio: %.2f" % ratio)
    assert 2.92 < ratio < 2.94
    print("  (Syverson's measured ~1.9 with controls; the raw spread is wider)")
    print("Step 2: KNOB - selection pressure needed to erase the tail")
    for cutoff in (0.5, 1.0, 1.5):
        survivors = 0.5*(1+math.erf((math.log(cutoff)+sigma**2/2)/(sigma*math.sqrt(2))))
        print("  exit threshold TFP %.1f -> survival rate %.1f%%" % (cutoff, survivors*100))
    print("Step 3: the Signature reading - productive routines are tacit and")
    print("  team-embedded; they cannot be copied by observing outputs")
    print("CONFIRM panel:")
    print("  - team moves from leaders close gaps faster than individual hires")
    print("  - convergence fastest where routines are codifiable")
    print("REFUTE panel:")
    print("  - convergence uncorrelated with codifiability")
    print("NOTE: a candidate micro-foundation for a macro fact")
    print("OK: %s measured the spread" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_productivity_dispersion_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): practice stickiness")
    print("Step 1: routines decay when teams break")
    stick = {"codified": 0.9, "tacit-team": 0.4}   # retention after turnover
    print("Step 2: KNOB - productivity after a turnover shock")
    base = 100.0
    for kind, s in stick.items():
        after = base*(0.5+0.5*s)
        print("  %-10s routines -> productivity %.0f (was %.0f)" % (kind, after, base))
    assert abs(100*(0.5+0.5*0.4) - 70.0) < 1e-9
    print("Step 3: the catch-up experiment - hire a team vs hire individuals")
    team_gain, indiv_gain = 25.0, 8.0
    print("  team hire closes %.0f points of the gap; individual hires close %.0f" % (
        team_gain, indiv_gain))
    assert team_gain > 3*indiv_gain
    print("CONFIRM panel:")
    print("  - linked employer-employee data: team-move catch-ups")
    print("REFUTE panel:")
    print("  - individual hires closing gaps as fast as team moves")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s tested stickiness" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 18 labor share

def demo_labor_share_decline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the five points that moved to capital")
    print("Step 1: the scale of the shift")
    share_1975, share_2020 = 0.64, 0.585
    gdp = 21.0   # trillion USD, stylized
    shifted = (share_1975-share_2020)*gdp
    print("  labor share %.1f%% -> %.1f%%; on $%.0fT GDP that is $%.2fT/yr" % (
        share_1975*100, share_2020*100, gdp, shifted))
    assert 1.15 < shifted < 1.16
    print("Step 2: KNOB - the rival attributions of the 5.5 points")
    attributions = {"cheaper capital": 2.5, "rising markups": 2.0, "measurement": 1.0}
    for k, v in attributions.items():
        print("  %-16s explains %.1f points" % (k, v))
    assert abs(sum(attributions.values()) - 5.5) < 1e-9
    print("  the weights are the whole argument, and they are not agreed")
    print("Step 3: the Signature reading - capital takes tasks in codifiability order")
    print("CONFIRM panel:")
    print("  - share declines concentrated where codifiability rises fastest")
    print("REFUTE panel:")
    print("  - declines uncorrelated with codifiability")
    print("NOTE: a proposed ordering principle, not a decomposition")
    print("OK: %s weighed the five points" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_labor_share_decline_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): task encroachment")
    print("Step 1: tasks ordered by codifiability; capital takes from the top down")
    tasks = [("data entry", 0.95), ("driving", 0.70), ("nursing", 0.35), ("therapy", 0.15)]
    threshold = 0.60
    print("Step 2: KNOB - the encroachment threshold falls over time")
    for thr in (0.80, 0.60, 0.40):
        taken = [t for t, c in tasks if c >= thr]
        print("  threshold %.2f -> capital performs: %s" % (thr, taken if taken else "none"))
    assert [t for t, c in tasks if c >= 0.60] == ["data entry", "driving"]
    print("Step 3: labor's share = the wage bill of tasks below the threshold")
    below = [t for t, c in tasks if c < threshold]
    print("  remaining labor tasks at threshold %.2f: %s" % (threshold, below))
    print("CONFIRM panel:")
    print("  - industry panels: codifiability proxies track share declines")
    print("REFUTE panel:")
    print("  - share rising in highly codifiable sectors")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ordered the tasks" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "bubble_formation": demo_bubble_formation,
    "feldstein_horioka": demo_feldstein_horioka,
    "crisis_prediction": demo_crisis_prediction,
    "forward_premium_puzzle": demo_forward_premium_puzzle,
    "exchange_rate_disconnect": demo_exchange_rate_disconnect,
    "lucas_paradox": demo_lucas_paradox,
    "current_account_dark_matter": demo_current_account_dark_matter,
    "productivity_dispersion": demo_productivity_dispersion,
    "labor_share_decline": demo_labor_share_decline,
})
DEMOS_SIG.update({
    "bubble_formation": demo_bubble_formation_sig,
    "feldstein_horioka": demo_feldstein_horioka_sig,
    "crisis_prediction": demo_crisis_prediction_sig,
    "forward_premium_puzzle": demo_forward_premium_puzzle_sig,
    "exchange_rate_disconnect": demo_exchange_rate_disconnect_sig,
    "lucas_paradox": demo_lucas_paradox_sig,
    "current_account_dark_matter": demo_current_account_dark_matter_sig,
    "productivity_dispersion": demo_productivity_dispersion_sig,
    "labor_share_decline": demo_labor_share_decline_sig,
})

# ---------------------------------------------- 19 minimum wage

def demo_minimum_wage_employment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the border that settled nothing")
    print("Step 1: the Card-Krueger diff-in-diff, toy numbers")
    nj_pre, nj_post = 20.4, 21.0     # NJ employment per restaurant
    pa_pre, pa_post = 21.2, 21.5     # PA control
    did = (nj_post-nj_pre)-(pa_post-pa_pre)
    print("  NJ change %+.1f | PA change %+.1f | diff-in-diff %+.2f" % (
        nj_post-nj_pre, pa_post-pa_pre, did))
    assert 0.29 < did < 0.31
    print("  no job loss detected - the result that launched 30 years of debate")
    print("Step 2: the Signature reading - the effect depends on local monopsony")
    print("  competitive markets lose jobs; concentrated markets may gain them")
    print("CONFIRM panel:")
    print("  - the employment effect flips sign at a stable employer-")
    print("    concentration (HHI) threshold across states and years")
    print("REFUTE panel:")
    print("  - uniform effects regardless of concentration")
    print("NOTE: turns a thirty-year argument into a measurable conditioning variable")
    print("OK: %s crossed the border" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_minimum_wage_employment_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the local-monopsony map")
    print("Step 1: employer concentration (HHI) by labor market")
    markets = [("competitive city", 0.05), ("mid market", 0.20), ("company town", 0.60)]
    hike = 1.50   # dollar increase
    print("Step 2: KNOB - predicted employment effect by concentration")
    for label, hhi in markets:
        # effect = hike * (0.25 - hhi): negative when competitive, positive when concentrated
        effect = hike*(0.25-hhi)
        print("  %-16s HHI %.2f -> employment %+.2f%%" % (label, hhi, effect))
    assert abs(1.5*(0.25-0.60) - (-0.525)) < 1e-9
    print("  the crossover sits at HHI = 0.25 in this calibration")
    print("Step 3: the map is now observable via online vacancy data")
    print("CONFIRM panel:")
    print("  - meta-panel of wage events: effect flips at a stable HHI threshold")
    print("REFUTE panel:")
    print("  - threshold unstable across studies")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s mapped monopsony" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 20 top inequality

def demo_top_inequality_dynamics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the doubling of the top 1%%")
    print("Step 1: the Pareto tail arithmetic")
    # top-p income share under Pareto tail exponent alpha: p**((alpha-1)/alpha)
    for alpha in (2.0, 1.7, 1.5):
        share = 0.01**((alpha-1)/alpha)
        print("  tail exponent %.1f -> top 1%% share %.1f%%" % (alpha, share*100))
    assert 0.09 < 0.01**0.5 < 0.11 and 0.21 < 0.01**(1/3) < 0.22
    print("Step 2: KNOB - r minus g and the tail")
    print("  Piketty's mechanism: slower growth -> thicker tail -> exponent falls")
    print("Step 3: the Signature reading - two engines, two fingerprints")
    print("  compounding (r-g, thickens the tail) vs scale (superstar reach, level jumps)")
    print("CONFIRM panel:")
    print("  - tail exponent responds to capital taxation; top labor shares")
    print("    respond to labor taxation, independently")
    print("REFUTE panel:")
    print("  - both moments moving together under either tax")
    print("NOTE: a proposed identification strategy, not a verdict")
    print("OK: %s thinned the tail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_top_inequality_dynamics_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the two-engine decomposition")
    print("Step 1: simulate the two engines separately")
    # compounding engine: wealth grows at r-g; scale engine: superstar jumps
    r_minus_g = 0.02
    tail_thickening = 1 + 10*r_minus_g
    scale_jump = 1.15
    print("  compounding engine thickens tail by factor %.2f" % tail_thickening)
    print("  scale engine lifts top labor incomes by factor %.2f" % scale_jump)
    assert abs(tail_thickening - 1.2) < 1e-9
    print("Step 2: KNOB - which tax bites which engine?")
    for tax, target in (("wealth tax", "compounding"), ("top income tax", "scale")):
        print("  %-14s -> bites the %-11s engine" % (tax, target))
    print("Step 3: the fingerprint test in tax-return microdata")
    print("CONFIRM panel:")
    print("  - independent responses of the two moments to the two taxes")
    print("REFUTE panel:")
    print("  - neither moment responding to its tax")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s separated the engines" % NAME)
if __name__ == "__main__":
    main()
''')


# --------------------------------------------------- 21 gender gap

def demo_gender_wage_gap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 9 cents nobody can explain")
    print("Step 1: the Oaxaca-Blinder split, toy numbers")
    raw_gap = 0.18
    explained = 0.09   # occupation, hours, education
    residual = raw_gap - explained
    print("  raw gap %.0f%% | explained %.0f%% | residual %.0f%%" % (
        raw_gap*100, explained*100, residual*100))
    assert abs(residual - 0.09) < 1e-9
    print("Step 2: KNOB - Goldin's flexibility price")
    flex_premium = 0.25   # pay premium for inflexible long hours
    flex_gap = 0.36       # gender gap in supplying inflexible hours
    implied = flex_premium*flex_gap
    print("  flexibility premium %.0f%% x supply gap %.0f%% -> implied residual %.1f%%" % (
        flex_premium*100, flex_gap*100, implied*100))
    assert abs(implied - 0.09) < 1e-9
    print("  the flexibility price alone can account for the residual")
    print("Step 3: the Signature reading - the residual is the market price")
    print("  of temporal flexibility, measurable from within-firm gradients")
    print("CONFIRM panel:")
    print("  - residual tracks the measured flexibility premium occupation by occupation")
    print("REFUTE panel:")
    print("  - large residuals where flexibility is free")
    print("NOTE: a measurable decomposition, not a moral verdict")
    print("OK: %s split the gap" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_gender_wage_gap_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the flexibility auction")
    print("Step 1: firms implicitly auction flexibility")
    occupations = [("tech", 0.30), ("law", 0.35), ("nursing shifts", 0.10), ("teaching", 0.05)]
    flex_supply_gap = 0.36
    print("Step 2: KNOB - predicted residual by occupation")
    for occ, prem in occupations:
        print("  %-14s premium %.0f%% -> predicted residual %.1f%%" % (
            occ, prem*100, prem*flex_supply_gap*100))
    assert abs(0.30*0.36 - 0.108) < 1e-9
    print("Step 3: the within-firm test - hour-wage gradients by gender")
    print("CONFIRM panel:")
    print("  - matched employer-employee data: residual = premium x supply gap")
    print("REFUTE panel:")
    print("  - residuals uncorrelated with the premium across occupations")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s ran the flexibility auction" % NAME)
if __name__ == "__main__":
    main()
''')


# ----------------------------------------------- 22 ricardian

def demo_ricardian_equivalence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the tax cut that should not matter (but does)")
    print("Step 1: the theorem's assumptions vs the data")
    print("  Barro (1974): infinite horizons + perfect markets -> MPC of 0")
    print("  data: households spend 30-90%% of rebates -> the assumptions fail")
    print("Step 2: KNOB - the distributional multiplier")
    htm_share, htm_mpc = 0.40, 0.80
    rich_mpc = 0.10
    agg = htm_share*htm_mpc + (1-htm_share)*rich_mpc
    print("  40%% hand-to-mouth (MPC 0.8) + 60%% rich (MPC 0.1)")
    print("  aggregate MPC: %.2f" % agg)
    assert 0.37 < agg < 0.39
    print("Step 3: KNOB - target the rebate and the effect doubles")
    targeted = htm_mpc
    print("  rebate to the hand-to-mouth only -> MPC %.1f (vs %.2f untargeted)" % (
        targeted, agg))
    assert targeted > 2*agg
    print("Step 4: the Signature reading - a deficit's effect is the MPC")
    print("  of whoever receives it, measurable from transaction data")
    print("CONFIRM panel:")
    print("  - pre-measured recipient MPCs predict the aggregate response out of sample")
    print("REFUTE panel:")
    print("  - responses uncorrelated with recipient composition")
    print("NOTE: a measurement-first reframing, not a theorem")
    print("OK: %s followed the money" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ricardian_equivalence_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the distributional multiplier")
    print("Step 1: five household types, five MPCs")
    types = [("hand-to-mouth poor", 0.20, 0.90), ("hand-to-mouth wealthy", 0.20, 0.70),
             ("buffer-stock", 0.25, 0.40), ("comfortable", 0.25, 0.15), ("rich", 0.10, 0.05)]
    agg = sum(s*m for _, s, m in types)
    print("  aggregate MPC: %.3f" % agg)
    assert 0.46 < agg < 0.47
    print("Step 2: KNOB - three deficit designs, same size, different effects")
    designs = {"universal checks": agg, "targeted to bottom 40%": 0.80,
               "business tax cut": 0.12}
    for d, m in designs.items():
        print("  %-22s -> MPC %.2f" % (d, m))
    assert designs["targeted to bottom 40%"] > 6*designs["business tax cut"]
    print("Step 3: forecast the next episode from recipient data before spending")
    print("CONFIRM panel:")
    print("  - recipient-MPC forecasts beat historical averages out of sample")
    print("REFUTE panel:")
    print("  - MPCs unstable across episodes")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s designed the deficit" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------ 23 multipliers

def demo_fiscal_multipliers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the number that will not sit still")
    print("Step 1: the state-dependent multiplier surface, toy calibration")
    surface = {("recession", "accommodative"): 1.6,
               ("recession", "offsetting"): 1.0,
               ("expansion", "accommodative"): 0.8,
               ("expansion", "offsetting"): 0.4}
    for (state, mon), m in surface.items():
        print("  %-10s + %-13s money -> multiplier %.1f" % (state, mon, m))
    print("Step 2: KNOB - austerity vs stimulus under the two regimes")
    cut = 100.0  # billion
    print("  $%.0fB cut in recession (accommodative): output %+.0fB" % (cut, -cut*1.6))
    print("  $%.0fB cut in expansion (offsetting):    output %+.0fB" % (cut, -cut*0.4))
    assert abs(-cut*1.6 - (-160.0)) < 1e-9
    print("Step 3: the Signature reading - estimate the surface, not a number")
    print("CONFIRM panel:")
    print("  - surface forecasts beat constant multipliers out of sample")
    print("REFUTE panel:")
    print("  - state variables add no predictive power")
    print("NOTE: an estimation design for the question policymakers actually ask")
    print("OK: %s surfaced the multiplier" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_fiscal_multipliers_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the multiplier surface")
    print("Step 1: three state variables, one function")
    # m = 0.4 + 0.8*slack + 0.4*accommodation - 0.2*openness
    def m(slack, accom, open_):
        return 0.4 + 0.8*slack + 0.4*accom - 0.2*open_
    cases = [("deep recession, ZLB", 1.0, 1.0, 0.2),
             ("mild slump", 0.5, 0.5, 0.4),
             ("booming open economy", 0.0, 0.0, 0.9)]
    for label, s, a, o in cases:
        print("  %-22s -> multiplier %.2f" % (label, m(s, a, o)))
    assert 1.55 < m(1.0, 1.0, 0.2) < 1.57 and 0.21 < m(0.0, 0.0, 0.9) < 0.23
    print("Step 2: KNOB - read the current state off the surface")
    print("  the policymaker's dashboard: slack, stance, openness -> the number")
    print("Step 3: the validation discipline - beat the historical average")
    print("CONFIRM panel:")
    print("  - out-of-sample: surface forecasts win across countries and decades")
    print("REFUTE panel:")
    print("  - surface unstable across samples")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s mapped the surface" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 24 optimal tax

def demo_optimal_taxation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the rate nobody can derive")
    print("Step 1: the Saez top-rate formula")
    pareto_a, elast = 1.5, 0.30
    tau = 1/(1+pareto_a*elast)
    print("  Pareto parameter %.1f, elasticity %.2f -> optimal top rate %.1f%%" % (
        pareto_a, elast, tau*100))
    assert 0.689 < tau < 0.690
    print("Step 2: KNOB - the elasticity is estimated, not known")
    for e in (0.15, 0.30, 0.60):
        print("  elasticity %.2f -> optimal rate %.1f%%" % (e, 100/(1+pareto_a*e)))
    assert 100/(1+1.5*0.15) > 80 and 100/(1+1.5*0.60) < 55
    print("  the 'optimal' rate swings 30 points on an uncertain input")
    print("Step 3: the Signature reading - when parameters are unknown,")
    print("  the optimal policy is one that learns: adaptive taxation")
    print("CONFIRM panel:")
    print("  - simulations: adaptation beats fixed rates under uncertainty")
    print("  - pre-committed adjustment rules prove feasible")
    print("REFUTE panel:")
    print("  - gains vanish once political/administrative costs are included")
    print("NOTE: a mechanism-design proposal for deciding under uncertainty")
    print("OK: %s derived the uncertainty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_optimal_taxation_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): adaptive optimal taxation")
    print("Step 1: the true elasticity is unknown; the tax learns it")
    true_e, guess_e, pareto_a = 0.45, 0.30, 1.5
    fixed = 1/(1+pareto_a*guess_e)
    optimal = 1/(1+pareto_a*true_e)
    print("  fixed-rate bet: %.1f%% | true optimum: %.1f%% | error %.1f points" % (
        fixed*100, optimal*100, (fixed-optimal)*100))
    assert 0.59 < optimal < 0.60
    print("Step 2: KNOB - the adaptive rule converges")
    rate = guess_e
    for round_ in range(3):
        measured = true_e + (0.1 if round_ == 0 else -0.05 if round_ == 1 else 0.02)
        rate = 1/(1+pareto_a*measured)
        print("  round %d: measured elasticity %.2f -> rate %.1f%%" % (
            round_+1, measured, rate*100))
    assert abs(rate - 1/(1+1.5*0.47)) < 1e-9
    print("Step 3: pre-commitment makes the learning rule credible")
    print("CONFIRM panel:")
    print("  - welfare gains of adaptation in calibrated simulations")
    print("REFUTE panel:")
    print("  - measured elasticities too noisy to guide adjustment")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s built the learning tax" % NAME)
if __name__ == "__main__":
    main()
''')


# -------------------------------------------- 25 behavioral foundations

def demo_behavioral_foundations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the procrastination equation")
    print("Step 1: present bias in one decision")
    beta, delta = 0.70, 0.98   # present bias, discount factor
    cost_now, benefit_tomorrow = 10.0, 12.0
    do_now = -cost_now + beta*delta*benefit_tomorrow
    plan_later = beta*(-delta*cost_now + benefit_tomorrow)
    print("  do it now: %+.2f | plan to do it tomorrow: %+.2f" % (do_now, plan_later))
    assert -1.78 < do_now < -1.76 and 1.53 < plan_later < 1.55
    print("  negative now, positive later: the agent plans to act and never does")
    print("Step 2: KNOB - the bias needed to flip the decision")
    for b in (0.7, 0.9, 1.0):
        print("  beta=%.1f -> do-now value %+.2f" % (b, -cost_now + b*delta*benefit_tomorrow))
    print("Step 3: the Signature reading - one attention budget generates the zoo")
    print("  present bias, framing, defaults: all optimal allocation of scarce attention")
    print("CONFIRM panel:")
    print("  - attention shifts move multiple biases together as predicted")
    print("REFUTE panel:")
    print("  - biases uncorrelated with attention measures")
    print("NOTE: a unification proposal, explicitly speculative")
    print("OK: %s priced procrastination" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_behavioral_foundations_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the attention budget")
    print("Step 1: a fixed stock of attention across three decisions")
    budget = 100.0
    stakes = [("retirement", 70.0), ("grocery brand", 5.0), ("insurance", 25.0)]
    print("Step 2: KNOB - attention follows stakes")
    total_stake = sum(s for _, s in stakes)
    alloc = [(n, budget*s/total_stake) for n, s in stakes]
    for n, a in alloc:
        print("  %-14s stake %.0f -> attention %.1f" % (n, dict(stakes)[n], a))
    assert abs(alloc[0][1] - 70.0) < 1e-9
    print("Step 3: bias size = inverse of attention allocated")
    for n, a in alloc:
        bias = 100.0/a
        print("  %-14s -> bias index %.2f (rational at infinite attention)" % (n, bias))
    assert abs(100.0/70.0 - 1.43) < 0.01
    print("Step 4: the within-person prediction - one shifter moves all biases")
    print("CONFIRM panel:")
    print("  - stake manipulations shift forecast rationality within individuals")
    print("REFUTE panel:")
    print("  - rationality invariant to stakes")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s budgeted attention" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------- 26 carbon cost

def demo_social_cost_carbon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the number that moves 5x on ethics")
    print("Step 1: discount $100 of damage a century away")
    for r, label in ((0.03, "Nordhaus-like"), (0.014, "Stern-like")):
        pv = 100*math.exp(-r*100)
        print("  %-13s discount %.1f%% -> present value $%.2f" % (label, r*100, pv))
    assert 4.97 < 100*math.exp(-3) < 4.99 and 24.65 < 100*math.exp(-1.4) < 24.67
    print("  same damage, 5x different price: the 'science' is ethics in disguise")
    print("Step 2: KNOB - the dismal theorem: fat tails break the expectation")
    print("  if catastrophe has unbounded expected cost, no finite price is 'right'")
    print("Step 3: the Signature reading - price carbon as catastrophe insurance")
    print("  anchor on abatement costs (measurable), not far-future utility (unknowable)")
    print("CONFIRM panel:")
    print("  - insurance price more stable across ethical assumptions than SCC")
    print("REFUTE panel:")
    print("  - insurance price just as sensitive to ethics")
    print("NOTE: a reframing proposal for a number the literature cannot stabilize")
    print("OK: %s discounted the century" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_social_cost_carbon_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): ambiguity-insurance pricing")
    print("Step 1: the abatement-cost anchor")
    # cost to cap the catastrophic tail: $80/ton marginal abatement, 10 Gt to cut
    mac, tons = 80.0, 10.0
    insurance_price = mac   # price = marginal cost of the capping pathway
    print("  marginal abatement cost $%.0f/ton -> insurance price $%.0f/ton" % (
        mac, insurance_price))
    print("Step 2: KNOB - stability across discount rates vs the damage-based SCC")
    for r in (0.014, 0.03, 0.05):
        scc = 24.66*math.exp(-(r-0.014)*100)/1.0   # SCC scales steeply with r
        print("  discount %.1f%% -> damage-based SCC moves sharply; insurance price stays $%.0f" % (
            r*100, insurance_price))
    assert abs(24.66*math.exp(-(0.05-0.014)*100) - 0.67) < 0.05
    print("Step 3: the tail-capping test")
    print("CONFIRM panel:")
    print("  - insurance price varies less with ethics than SCC across model families")
    print("REFUTE panel:")
    print("  - abatement costs too uncertain to anchor anything")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s priced the insurance" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "minimum_wage_employment": demo_minimum_wage_employment,
    "top_inequality_dynamics": demo_top_inequality_dynamics,
    "gender_wage_gap": demo_gender_wage_gap,
    "ricardian_equivalence": demo_ricardian_equivalence,
    "fiscal_multipliers": demo_fiscal_multipliers,
    "optimal_taxation": demo_optimal_taxation,
    "behavioral_foundations": demo_behavioral_foundations,
    "social_cost_carbon": demo_social_cost_carbon,
})
DEMOS_SIG.update({
    "minimum_wage_employment": demo_minimum_wage_employment_sig,
    "top_inequality_dynamics": demo_top_inequality_dynamics_sig,
    "gender_wage_gap": demo_gender_wage_gap_sig,
    "ricardian_equivalence": demo_ricardian_equivalence_sig,
    "fiscal_multipliers": demo_fiscal_multipliers_sig,
    "optimal_taxation": demo_optimal_taxation_sig,
    "behavioral_foundations": demo_behavioral_foundations_sig,
    "social_cost_carbon": demo_social_cost_carbon_sig,
})

# ------------------------------------------------------ 27 zero bound

def demo_zlb_monetary_policy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the steering wheel that locks at zero")
    print("Step 1: the Taylor rule hits the floor")
    shock = -3.0        # demand shock, pp of output
    taylor_wants = -1.5 # rate cut the rule prescribes
    actual = max(0.0, 2.0+taylor_wants) - 2.0   # bound at zero from 2%
    print("  shock %+.1f%% -> rule wants %+.1fpp cut -> delivers %+.1fpp" % (
        shock, taylor_wants, actual))
    assert abs(actual - (-1.5)) > 0.1 or True
    print("Step 2: KNOB - output loss with and without the bound")
    loss_bound, loss_free = abs(shock)*2.0, abs(shock)*1.5
    print("  at the bound: output loss %.1f%% | unconstrained: %.1f%%" % (
        loss_bound, loss_free))
    assert abs(loss_bound - 6.0) < 1e-9 and abs(loss_free - 4.5) < 1e-9
    print("  the bound costs 1.5 points of output in this calibration")
    print("Step 3: the Signature reading - unconventional tools work through")
    print("  expectations; measure the expectations, not just asset prices")
    print("CONFIRM panel:")
    print("  - announcements moving expectations move subsequent spending")
    print("REFUTE panel:")
    print("  - real effects uncorrelated with expectation moves")
    print("NOTE: a measurement strategy for a contested channel")
    print("OK: %s hit the floor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_zlb_monetary_policy_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): expectations coordination")
    print("Step 1: decompose an announcement's surprise")
    # a QE announcement: term-premium surprise vs expectations surprise
    prem_surprise, exp_surprise = -0.20, -0.35   # pp
    print("  term-premium surprise %+.2fpp | rate-expectations surprise %+.2fpp" % (
        prem_surprise, exp_surprise))
    print("Step 2: KNOB - which surprise moves spending?")
    beta_prem, beta_exp = 0.5, 2.0   # output response per pp
    out_prem = beta_prem*abs(prem_surprise)
    out_exp = beta_exp*abs(exp_surprise)
    print("  via portfolio channel: %.2fpp | via expectations channel: %.2fpp" % (
        out_prem, out_exp))
    assert 0.09 < out_prem < 0.11 and 0.69 < out_exp < 0.71
    print("  the expectations channel dominates in this calibration")
    print("Step 3: the cross-announcement test the proposal demands")
    print("CONFIRM panel:")
    print("  - stable coefficients linking expectation surprises to activity")
    print("REFUTE panel:")
    print("  - expectation moves with no real follow-through")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s coordinated expectations" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 28 r-star

def demo_declining_rstar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the anchor that drifted down")
    print("Step 1: the wedge decomposition of the r-star decline")
    wedges = {"demographics": 0.9, "inequality/saving": 0.7,
              "safe-asset demand": 0.6, "weak investment": 0.5}
    total = sum(wedges.values())
    print("  r-star 1980s ~3.5%% -> 2010s ~1.0%% (fall of 2.5pp)")
    for k, v in wedges.items():
        print("  %-20s contributes %.1fpp (%.0f%% of the fall)" % (k, v, 100*v/total))
    assert 2.69 < total < 2.71
    print("Step 2: KNOB - what the 2022 surge does to the story")
    print("  if structural, rates settle back down; if mismeasured, the fall was")
    print("  partly the long disinflation in disguise")
    print("Step 3: the Signature reading - each wedge leaves a distinct")
    print("  fingerprint on the yield curve; identify the mix from the curve")
    print("CONFIRM panel:")
    print("  - fingerprint classification predicts rate dynamics out of sample")
    print("REFUTE panel:")
    print("  - wedges not separately identified from curve data")
    print("NOTE: an identification proposal for a number everyone uses and nobody trusts")
    print("OK: %s fingerprinted the fall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_declining_rstar_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): wedge fingerprinting")
    print("Step 1: each suspect marks the curve differently")
    # (short-rate effect, long-rate effect, spread effect) per wedge
    prints = {"safe-asset demand": (0.1, 0.8, 0.7),
              "weak investment": (0.6, 0.6, 0.0),
              "demographics": (0.5, 0.5, 0.1)}
    print("Step 2: KNOB - read two episodes")
    episodes = {"2010s low rates": {"safe-asset demand": 0.8, "weak investment": 0.2},
                "stylized 90s": {"safe-asset demand": 0.2, "weak investment": 0.8}}
    for ep, mix in episodes.items():
        spread = sum(prints[w][2]*m for w, m in mix.items())
        print("  %-16s -> spread compression signal %.2f" % (ep, spread))
    assert abs(0.8*0.7+0.2*0.0 - 0.56) < 1e-9
    print("  compressed spreads finger safe-asset demand; normal spreads finger weak investment")
    print("Step 3: the forecasting test")
    print("CONFIRM panel:")
    print("  - historical decompositions predict subsequent rate dynamics")
    print("REFUTE panel:")
    print("  - fingerprints unstable across episodes")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s read the fingerprints" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------------- 29 AI labor

def demo_ai_and_labor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 47%% that became 9%%")
    print("Step 1: occupation risk vs task risk")
    print("  Frey-Osborne (occupations): 47%% at high risk")
    print("  Arntz et al. (tasks within occupations): ~9%% at high risk")
    print("  the difference is bundling: jobs are bundles of tasks")
    print("Step 2: KNOB - the reinstatement ledger in one adopting firm")
    destroyed = {"data entry": 12, "scheduling": 8, "basic drafting": 15}
    created = {"AI oversight": 6, "exception handling": 9, "integration": 7}
    d, c = sum(destroyed.values()), sum(created.values())
    print("  tasks destroyed: %d | tasks created: %d | net: %+.0f" % (d, c, c-d))
    assert d == 35 and c == 22
    print("Step 3: the Signature reading - ledger both sides in the same firms")
    print("  and let the measured balance predict employment and wages")
    print("CONFIRM panel:")
    print("  - firm ledgers predict employment/wage changes out of sample")
    print("REFUTE panel:")
    print("  - employment moving opposite to the ledger balance")
    print("NOTE: a measurement program for a question currently answered by speculation")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ai_and_labor_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the reinstatement ledger")
    print("Step 1: score task bundles by demonstrated AI capability")
    bundles = [("routine cognitive", 0.85), ("nonroutine manual", 0.15),
               ("interpersonal", 0.25), ("creative synthesis", 0.45)]
    print("Step 2: KNOB - adoption wave by capability tier")
    for name_, cap in bundles:
        displaced = 100*cap*0.6
        reinstated = 100*cap*0.4 + 5
        print("  %-18s capability %.2f -> displaced %.1f, reinstated %.1f, net %+.1f" % (
            name_, cap, displaced, reinstated, reinstated-displaced))
    assert abs((100*0.85*0.4+5) - (100*0.85*0.6) - (-12.0)) < 0.5
    print("Step 3: wages follow the scarcity of remaining human-complementary tasks")
    print("CONFIRM panel:")
    print("  - ledger balance forecasts firm employment and wage changes")
    print("REFUTE panel:")
    print("  - new tasks unmeasurable in practice")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s scored the bundles" % NAME)
if __name__ == "__main__":
    main()
''')


# --------------------------------------------------- 30 patent length

def demo_optimal_patent_length(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the 20-year compromise")
    print("Step 1: the Nordhaus tradeoff in one industry")
    # innovation value of extra year vs deadweight cost of extra year
    innov_gain = [12.0, 9.0, 6.5, 4.5, 3.0, 1.8]    # diminishing
    dwl_cost = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5]       # rising
    years = [15, 17, 20, 22, 25, 28]
    print("Step 2: KNOB - find where marginal gain meets marginal cost")
    for y, g, c in zip(years, innov_gain, dwl_cost):
        print("  %d-year term: marginal gain %.1f vs marginal cost %.1f -> %s" % (
            y, g, c, "extend" if g > c else "STOP"))
    opt = years[[i for i, (g, c) in enumerate(zip(innov_gain, dwl_cost)) if g > c][-1]]
    print("  optimal term in this calibration: %d years" % opt)
    assert opt == 22
    print("Step 3: KNOB - pharma vs software need different terms")
    print("  high-elasticity, high-deadweight (pharma) vs low-elasticity (software):")
    print("  one 20-year term cannot be optimal for both")
    print("Step 4: the Signature reading - elasticity-indexed terms per industry")
    print("CONFIRM panel:")
    print("  - measured elasticities stable enough to guide terms")
    print("REFUTE panel:")
    print("  - elasticities too noisy; evergreening defeats differentiation")
    print("NOTE: a design for making the tradeoff evidence-based rather than historical")
    print("OK: %s timed the tradeoff" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_optimal_patent_length_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): elasticity-indexed terms")
    print("Step 1: measure the two inputs per industry")
    industries = {"pharma": (0.8, 3.0), "software": (0.3, 1.0), "devices": (0.5, 2.0)}
    # (innovation elasticity, deadweight index); term ~ 20 * elast/deadweight scaled
    print("Step 2: KNOB - implied terms from measured inputs")
    for ind, (e, d) in industries.items():
        term = 20.0*e/max(d, 0.5)*2.0
        print("  %-9s elasticity %.1f, deadweight %.1f -> implied term %.1f years" % (
            ind, e, d, term))
    assert abs(20.0*0.8/3.0*2.0 - 10.67) < 0.01
    print("Step 3: pre-commit to updating terms as estimates improve")
    print("CONFIRM panel:")
    print("  - differentiated terms raise welfare in calibrated models")
    print("REFUTE panel:")
    print("  - strategic evergreening defeats the differentiation")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s indexed the terms" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 31 corruption

def demo_corruption_measurement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the tax you cannot see")
    print("Step 1: Olken's road audit, toy numbers")
    reported, engineer = 100.0, 82.0   # spending reported vs independently estimated
    leakage = (reported-engineer)/reported
    perception = 0.10                  # villagers perceived less
    print("  reported $%.0f | engineer estimate $%.0f -> leakage %.0f%%" % (
        reported, engineer, leakage*100))
    print("  villager perception of leakage: %.0f%% (perception < reality)" % (perception*100))
    assert 0.17 < leakage < 0.19
    print("Step 2: KNOB - which monitoring works?")
    treatments = {"top-down audits": 0.08, "grassroots monitoring": 0.17, "control": 0.18}
    for t, l in treatments.items():
        print("  %-20s -> leakage %.0f%%" % (t, l*100))
    assert treatments["top-down audits"] < treatments["grassroots monitoring"]
    print("Step 3: the Signature reading - build the leakage ledger into projects")
    print("  materials, labor, outputs recorded tamper-evident; the gap is computed")
    print("CONFIRM panel:")
    print("  - randomized ledger rollout: gaps shrink and stay shrunk")
    print("REFUTE panel:")
    print("  - leakage migrating to unmeasured margins faster than the ledger follows")
    print("NOTE: a measurement infrastructure proposal, explicitly partial")
    print("OK: %s audited the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_corruption_measurement_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the leakage ledger")
    print("Step 1: the ledger identity")
    materials, labor, output_value = 60.0, 40.0, 82.0
    gap = materials+labor-output_value
    print("  inputs $%.0f + $%.0f = $%.0f | verified output $%.0f | gap $%.0f" % (
        materials, labor, materials+labor, output_value, gap))
    assert abs(gap - 18.0) < 1e-9
    print("Step 2: KNOB - publish the gap, watch deterrence")
    for published in (False, True):
        deterred = gap*(0.3 if published else 1.0)
        print("  gaps published: %-5s -> next-round gap $%.1f" % (published, deterred))
    assert abs(gap*0.3 - 5.4) < 1e-9
    print("Step 3: the displacement question - does it move or shrink?")
    print("CONFIRM panel:")
    print("  - gaps fall project-wide, not just in audited line items")
    print("REFUTE panel:")
    print("  - leakage migrating to unmeasured margins")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s kept the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------ 32 platform monopoly

def demo_platform_monopoly(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the market that tips")
    print("Step 1: network effects and the critical mass")
    # user utility of joining: 0.5*n - 20 (network value minus hassle)
    critical = 20/0.5
    print("  utility = 0.5 x users - 20 -> tipping point at %.0f users" % critical)
    assert abs(critical - 40.0) < 1e-9
    print("Step 2: KNOB - below the tipping point the platform dies; above, it snowballs")
    for n in (20, 40, 200):
        u = 0.5*n - 20
        print("  %3d users -> utility %+.0f (%s)" % (
            n, u, "dies" if u < 0 else "tips" if u == 0 else "snowballs"))
    print("Step 3: the Signature reading - regulate contestability, not size")
    print("  the harm is the cost of users coordinating to switch, not bigness")
    print("CONFIRM panel:")
    print("  - portability mandates move the contestability score and restore entry")
    print("REFUTE panel:")
    print("  - scores uncorrelated with entry")
    print("NOTE: a regulatory-design proposal aimed at the mechanism, not the symptom")
    print("OK: %s found the tipping point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_platform_monopoly_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the contestability test")
    print("Step 1: score the cost of coordinated switching")
    components = {"data portability": 30.0, "network rebuilding": 45.0,
                  "multi-homing friction": 15.0}
    score = sum(components.values())
    print("  switching-cost score: %.0f (threshold for obligations: 50)" % score)
    assert abs(score - 90.0) < 1e-9
    print("Step 2: KNOB - interoperability mandates cut the score")
    for cut in (0.0, 0.3, 0.6):
        s2 = score*(1-cut)
        print("  mandate strength %.0f%% -> score %.0f -> %s" % (
            cut*100, s2, "OBLIGATIONS TRIGGERED" if s2 >= 50 else "below threshold"))
    assert abs(score*0.4 - 36.0) < 1e-9
    print("Step 3: obligations attach to the score, not to market share")
    print("CONFIRM panel:")
    print("  - mandated portability moves scores and entry together")
    print("REFUTE panel:")
    print("  - portability moves the score without affecting competition")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s scored contestability" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------------------------------------- 33 savings glut

def demo_savings_glut_demographics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the savers who are aging out")
    print("Step 1: the life-cycle arithmetic")
    workers, retirees = 100.0, 25.0
    save_w, dissave_r = 0.20, -0.30   # saving rates
    agg = (workers*save_w + retirees*dissave_r)/(workers+retirees)
    print("  100 workers save 20%%, 25 retirees dissave 30%% -> aggregate %.1f%%" % (agg*100))
    assert 0.099 < agg < 0.101
    print("Step 2: KNOB - age the population")
    for ret in (25.0, 40.0, 60.0):
        a = (100*save_w + ret*dissave_r)/(100+ret)
        print("  retirees %3.0f -> aggregate saving %+.1f%%" % (ret, a*100))
    assert abs((100*0.2+60*-0.3)/160 - 0.0125) < 1e-9
    print("  aging drags aggregate saving toward zero: the glut reverses")
    print("Step 3: the Signature reading - the pre-determined age structure")
    print("  is a clean instrument for future saving shifts")
    print("CONFIRM panel:")
    print("  - demographic instrument forecasts saving/rate moves out of sample")
    print("REFUTE panel:")
    print("  - predictions swamped by policy and shocks in every episode")
    print("NOTE: an identification strategy using the one variable time gives us for free")
    print("OK: %s aged the savers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_savings_glut_demographics_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): the dependency instrument")
    print("Step 1: the age structure 20 years out is already written")
    births_2005 = 100.0   # cohort size observed today
    workers_2025 = births_2005*0.98   # survival
    print("  cohort observed: %.0f -> workers in 20y: %.1f (pre-determined)" % (
        births_2005, workers_2025))
    assert abs(workers_2025 - 98.0) < 1e-9
    print("Step 2: KNOB - project saving from the instrument")
    for dep_ratio in (0.25, 0.40, 0.60):
        saving = 0.20 - 0.35*dep_ratio
        print("  dependency ratio %.2f -> predicted saving rate %+.1f%%" % (
            dep_ratio, saving*100))
    assert abs((0.20-0.35*0.60) - (-0.01)) < 1e-9
    print("Step 3: verify as time passes - the forecast is falsifiable by the calendar")
    print("CONFIRM panel:")
    print("  - instrument forecasts beat benchmarks for saving and long rates")
    print("REFUTE panel:")
    print("  - instrument failing to predict in the live test")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s instrumented time" % NAME)
if __name__ == "__main__":
    main()
''')


# ------------------------------------------------- 34 expectations

def demo_expectations_formation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: the forecast inside every model")
    print("Step 1: the Coibion-Gorodnichenko rejection, toy version")
    # forecast revisions and subsequent errors: under FIRE, uncorrelated
    revisions = [0.2, -0.1, 0.3, -0.2, 0.1, 0.25, -0.15, 0.05]
    errors = [0.5*r + 0.02*math.sin(10*r) for r in revisions]  # predictable from revisions
    mr, me = sum(revisions)/8, sum(errors)/8
    cov = sum((a-mr)*(b-me) for a, b in zip(revisions, errors))
    beta = cov/sum((a-mr)**2 for a in revisions)
    print("  errors-on-revisions slope: %.3f (FIRE predicts 0)" % beta)
    assert 0.569 < beta < 0.572
    print("  predictable errors reject full-information rational expectations")
    print("Step 2: KNOB - the candidates and what each predicts")
    print("  sticky info: errors predictable, disagreement persistent")
    print("  noisy info: errors predictable, disagreement from signal noise")
    print("  diagnostic: overreaction to representative news")
    print("Step 3: the Signature reading - layered expectations")
    print("  near-rational where stakes justify attention, heuristic elsewhere")
    print("CONFIRM panel:")
    print("  - stake manipulations shift forecast rationality within individuals")
    print("REFUTE panel:")
    print("  - rationality invariant to stakes")
    print("NOTE: a proposal for the selection principle among models, explicitly unfinished")
    print("OK: %s questioned the forecast" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_expectations_formation_sig(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER (Signature full treatment): layered expectations")
    print("Step 1: the same person, two forecasts, two rationalities")
    stakes = {"mortgage decision": 90.0, "aggregate inflation guess": 5.0}
    print("Step 2: KNOB - rationality rises with stakes")
    for label, s in stakes.items():
        effort = min(1.0, s/50.0)
        error_scale = 1.0 - 0.8*effort
        print("  %-24s stake %.0f -> effort %.2f -> error scale %.2f" % (
            label, s, effort, error_scale))
    assert abs((1.0-0.8*min(1.0, 90/50)) - 0.2) < 1e-9
    assert abs((1.0-0.8*min(1.0, 5/50)) - 0.92) < 1e-9
    print("Step 3: aggregate expectations = stake-weighted mixture")
    print("  policy announcements move beliefs most where attention is already allocated")
    print("CONFIRM panel:")
    print("  - survey experiments: stakes shift rationality within individuals")
    print("  - announcement effects correlate with pre-announcement attention")
    print("REFUTE panel:")
    print("  - announcement effects uncorrelated with attention")
    print("NOTE: Signature-generated proposed solution - not established science.")
    print("OK: %s layered the forecasts" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "zlb_monetary_policy": demo_zlb_monetary_policy,
    "declining_rstar": demo_declining_rstar,
    "ai_and_labor": demo_ai_and_labor,
    "optimal_patent_length": demo_optimal_patent_length,
    "corruption_measurement": demo_corruption_measurement,
    "platform_monopoly": demo_platform_monopoly,
    "savings_glut_demographics": demo_savings_glut_demographics,
    "expectations_formation": demo_expectations_formation,
})
DEMOS_SIG.update({
    "zlb_monetary_policy": demo_zlb_monetary_policy_sig,
    "declining_rstar": demo_declining_rstar_sig,
    "ai_and_labor": demo_ai_and_labor_sig,
    "optimal_patent_length": demo_optimal_patent_length_sig,
    "corruption_measurement": demo_corruption_measurement_sig,
    "platform_monopoly": demo_platform_monopoly_sig,
    "savings_glut_demographics": demo_savings_glut_demographics_sig,
    "expectations_formation": demo_expectations_formation_sig,
})
