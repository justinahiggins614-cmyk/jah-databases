#!/usr/bin/env python3
"""Demo programs for the Unsolved Public Health databases (Manon's 16:15 orders,
Unsolved Problems Solved series).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only Python that
walks through the Signature solution approach with adjustable assumptions, prints real
computed values, runs a confirm/refute panel, asserts tight bounds (never float
exact-equality), and ends with the OK marker. All 68 are machine-executed by build.py.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_uspu_vaccine_hesitancy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: hesitancy as a trust-ledger problem (measles herd threshold).
    # ADJUSTABLE ASSUMPTIONS: measles R0 and the community coverage rate.
    r0 = 12.0
    thr = 1.0 - 1.0 / r0          # herd-immunity threshold
    cov_low, cov_high = 0.90, 0.95
    eff_low = r0 * (1.0 - cov_low)
    eff_high = r0 * (1.0 - cov_high)
    print("step 1 - the bar: measles herd threshold = %.4f (need ~%.1f%% coverage)" % (thr, thr * 100))
    print("step 2 - a hesitant pocket at 90%% coverage: effective R = %.2f -> outbreak grows" % eff_low)
    print("step 3 - the same pocket at 95%% coverage: effective R = %.2f -> outbreak dies" % eff_high)
    print("step 4 - ledger read: coverage follows the trust balance, not the fact sheet")
    assert 0.916 < thr < 0.918, thr
    assert eff_low > 1.0, eff_low
    assert eff_high < 1.0, eff_high
    print("CONFIRM panel: community trust metrics predict uptake better than education or income.")
    print("REFUTE panel: a high-trust community with high hesitancy, or a fact-only campaign converting at scale.")
    print("OK: %s walked the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_obesity_drivers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: dated-shock decomposition of the obesity curve (slow integrator).
    # ADJUSTABLE ASSUMPTIONS: daily energy surplus after the environment shock.
    surplus_kcal_day = 50.0
    kcal_per_kg = 7700.0
    gain_per_year = surplus_kcal_day * 365.0 / kcal_per_kg
    decade_gain = gain_per_year * 10.0
    print("step 1 - the shock: environment flips, appetite regulation overwhelmed")
    print("step 2 - the integrator: %.0f kcal/day surplus -> %.2f kg/year" % (surplus_kcal_day, gain_per_year))
    print("step 3 - compounding: one decade of the shock = %.1f kg per person" % decade_gain)
    print("step 4 - decomposition: stack each dated shock (ultra-processing, portions, sweeteners) against the curve")
    assert 2.36 < gain_per_year < 2.38, gain_per_year
    assert 23.6 < decade_gain < 23.8, decade_gain
    print("CONFIRM panel: dated shocks predict each country's inflection with the integrator lag.")
    print("REFUTE panel: shock arrival without curve bending, or a single biological driver explaining more.")
    print("OK: %s walked the integrator" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_seasonal_flu_burden(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the annual flu toll and what a conserved-target vaccine changes.
    # ADJUSTABLE ASSUMPTIONS: attack rate, infection fatality ratio, coverage x effectiveness.
    pop, attack, ifr = 8.0e9, 0.10, 0.0008
    deaths = pop * attack * ifr
    cov, ve = 0.45, 0.50
    averted = deaths * cov * ve
    print("step 1 - the toll: %.0f infections x IFR %.4f = %.0f deaths/year" % (pop * attack, ifr, deaths))
    print("step 2 - today: %.0f%% coverage x %.0f%% effectiveness averts %.0f deaths" % (cov * 100, ve * 100, averted))
    print("step 3 - the red team: drift defeats the head-targeted guess most seasons")
    print("step 4 - conserved aim: stalk-directed immunity would hold across drifted seasons")
    assert 630000 < deaths < 650000, deaths
    assert 140000 < averted < 150000, averted
    print("CONFIRM panel: a stalk-based vaccine protecting across drifted seasons in field trials.")
    print("REFUTE panel: conserved targets unreachable at protective titers, or escape without fitness cost.")
    print("OK: %s walked the red team" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_tobacco_persistence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the demand-side plateau and the supply-side endgame (sinking lid).
    # ADJUSTABLE ASSUMPTIONS: current deaths and the demand-side annual decline rate.
    d0, decline, years = 8.0e6, 0.02, 35.0
    d_future = d0 * math.exp(-decline * years)
    plateau_share = 0.12   # demand measures asymptote near 10-15% prevalence
    print("step 1 - today: %.1f million tobacco deaths/year" % (d0 / 1e6))
    print("step 2 - demand-side only: %.1f million still dying in %d years" % (d_future / 1e6, int(years)))
    print("step 3 - the plateau: full MPOWER stalls near %.0f%% prevalence - the addicted core" % (plateau_share * 100))
    print("step 4 - endgame: sinking lid on licenses + generational sales ban + funded offramp")
    assert 3.9e6 < d_future < 4.1e6, d_future
    assert d_future > d0 * 0.45, d_future
    print("CONFIRM panel: generational bans collapse initiation without large illicit replacement.")
    print("REFUTE panel: illicit supply fully replacing legal supply under phaseout.")
    print("OK: %s walked the endgame" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_food_deserts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: swamp vs desert - price beats geography (logistic choice model).
    # ADJUSTABLE ASSUMPTIONS: distance sensitivity and the subsidy boost to the choice score.
    def p_healthy(dist_mi, subsidy_boost=0.0):
        score = 2.0 - 1.2 * dist_mi + subsidy_boost
        return 1.0 / (1.0 + math.exp(-score))
    p_near = p_healthy(0.5)
    p_far = p_healthy(2.5)
    p_far_sub = p_healthy(2.5, subsidy_boost=0.8)
    print("step 1 - near a store (0.5 mi): P(healthy choice) = %.3f" % p_near)
    print("step 2 - food desert (2.5 mi): P(healthy choice) = %.3f" % p_far)
    print("step 3 - desert + price flip (subsidy): P(healthy choice) = %.3f" % p_far_sub)
    print("step 4 - lesson: the store alone barely moves choice; the price ratio does")
    assert 0.80 < p_near < 0.81, p_near
    assert 0.26 < p_far < 0.28, p_far
    assert 0.44 < p_far_sub < 0.46, p_far_sub
    assert p_far_sub > p_far + 0.15, (p_far, p_far_sub)
    print("CONFIRM panel: price-ratio flips move population diets where store placement did not.")
    print("REFUTE panel: large price flips with zero diet change - purely cultural constraints.")
    print("OK: %s walked the swamp" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_lead_exposure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the lead ledger - IQ points and earnings lost per microgram.
    # ADJUSTABLE ASSUMPTIONS: blood lead level and IQ points lost per ug/dL.
    level_ug_dl = 5.0
    iq_per_unit = 0.5
    iq_lost = iq_per_unit * level_ug_dl
    lifetime_earnings = 1.2e6
    earnings_lost = lifetime_earnings * 0.02 * iq_lost
    print("step 1 - exposure: %.1f ug/dL blood lead x %.1f IQ points per unit" % (level_ug_dl, iq_per_unit))
    print("step 2 - brain cost: %.1f IQ points lost per child" % iq_lost)
    print("step 3 - money cost: $%.0f lifetime earnings lost per child" % earnings_lost)
    print("step 4 - the bond: borrow against the recovered earnings, remediate every source")
    assert 2.49 < iq_lost < 2.51, iq_lost
    assert 59000 < earnings_lost < 61000, earnings_lost
    print("CONFIRM panel: bond-funded cities show blood lead falling on the remediation schedule.")
    print("REFUTE panel: enumerated sources unfindable at scale, or remediation not moving blood lead.")
    print("OK: %s walked the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_clean_water_gaps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: maintenance-first water - price the service, not the hole.
    # ADJUSTABLE ASSUMPTIONS: borehole cost, people served, contract years, DALYs per person-year.
    cost, people, years = 10000.0, 500.0, 20.0
    cost_per_person_year = cost / (people * years)
    daly_per_person_year = 0.05
    total_daly = people * years * daly_per_person_year
    cost_per_daly = cost / total_daly
    print("step 1 - the asset: $%.0f borehole serves %.0f people for %.0f years" % (cost, people, years))
    print("step 2 - service price: $%.2f per person-year of safe water" % cost_per_person_year)
    print("step 3 - health return: %.0f DALYs averted at $%.0f per DALY" % (total_daly, cost_per_daly))
    print("step 4 - the contract: 20-year service deal, payment tied to flow, sensors verify uptime")
    assert 0.99 < cost_per_person_year < 1.01, cost_per_person_year
    assert 19.0 < cost_per_daly < 21.0, cost_per_daly
    print("CONFIRM panel: contract water points sustain multi-year uptime above charity baselines.")
    print("REFUTE panel: contracts decaying like charity projects - failure deeper than funding form.")
    print("OK: %s walked the pump" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_loneliness_epidemic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: loneliness as infrastructure - the social grid and its mortality price.
    # ADJUSTABLE ASSUMPTIONS: hazard ratio of loneliness and baseline 10-year mortality.
    hr, base_mort = 1.5, 0.08
    lonely_mort = base_mort * hr
    excess = lonely_mort - base_mort
    pop = 100000.0
    excess_deaths = pop * excess
    print("step 1 - the risk: loneliness HR = %.1f on 10-year mortality" % hr)
    print("step 2 - the price: %.1f%% -> %.1f%% mortality, +%.1f%% excess" % (base_mort * 100, lonely_mort * 100, excess * 100))
    print("step 3 - the city: %.0f excess deaths per 100k lonely residents per decade" % excess_deaths)
    print("step 4 - the rebuild: third places, shared rituals, contact-rich streets - measured like blood pressure")
    assert 0.119 < lonely_mort < 0.121, lonely_mort
    assert 3990 < excess_deaths < 4010, excess_deaths
    print("CONFIRM panel: contact-rebuilt neighborhoods show loneliness and disease declines tracking investment.")
    print("REFUTE panel: contact-rich environments with unchanged loneliness - driver is internal.")
    print("OK: %s walked the grid" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_mental_health_access(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the treatment cascade - standard care vs the task-shifted grid.
    # ADJUSTABLE ASSUMPTIONS: seek, receive, and recover rates under each model.
    need = 1000.0
    std = need * 0.40 * 0.50 * 0.60
    grid = need * 0.70 * 0.85 * 0.70
    print("step 1 - standard: 1000 in need -> %.0f seek -> %.0f receive -> %.0f recover (%.1f%%)" % (need * 0.40, need * 0.40 * 0.50, std, std / need * 100))
    print("step 2 - grid: lay counselors + remote supervision -> %.0f recover (%.1f%%)" % (grid, grid / need * 100))
    print("step 3 - the gap closed: %.1fx more recoveries with the same need" % (grid / std))
    print("step 4 - the constraint that matters: supervision ratio, not specialist headcount")
    assert 0.11 < std / need < 0.13, std
    assert 0.40 < grid / need < 0.44, grid
    assert grid > std * 3.0, (std, grid)
    print("CONFIRM panel: grid districts match specialist recovery rates at a fraction of the cost.")
    print("REFUTE panel: quality collapse at scale without in-person specialists.")
    print("OK: %s walked the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_maternal_disparities(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the thousand-fold gap in lifetime risk (three-delays chain).
    # ADJUSTABLE ASSUMPTIONS: maternal mortality ratios and total fertility rates.
    mmr_high, tfr_high = 500.0 / 1e5, 5.0
    risk_high = 1.0 - (1.0 - mmr_high) ** tfr_high
    mmr_low, tfr_low = 10.0 / 1e5, 1.7
    risk_low = 1.0 - (1.0 - mmr_low) ** tfr_low
    print("step 1 - high-mortality setting: MMR %.0f/100k x TFR %.1f -> lifetime risk %.4f (1 in %.0f)" % (mmr_high * 1e5, tfr_high, risk_high, 1.0 / risk_high))
    print("step 2 - low-mortality setting: MMR %.0f/100k x TFR %.1f -> lifetime risk %.6f (1 in %.0f)" % (mmr_low * 1e5, tfr_low, risk_low, 1.0 / risk_low))
    print("step 3 - the ratio: %.0fx more risk for the same physiological event" % (risk_high / risk_low))
    print("step 4 - the chain: register every pregnancy, guarantee transport, audit every death")
    assert 0.024 < risk_high < 0.026, risk_high
    assert 0.00016 < risk_low < 0.00018, risk_low
    assert risk_high / risk_low > 100.0, risk_high / risk_low
    print("CONFIRM panel: closed-loop districts drive mortality toward the achievable floor.")
    print("REFUTE panel: chains closing on paper while deaths persist - clinical quality beyond reach.")
    print("OK: %s walked the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_chronic_care_gap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the prevention bond - who pays, who saves, over what horizon.
    # ADJUSTABLE ASSUMPTIONS: program cost and the return multiple on averted costs.
    invest, ret_multiple, horizon = 1.0e6, 5.6, 10.0
    gross_averted = invest * ret_multiple
    net = gross_averted - invest
    per_year = net / horizon
    print("step 1 - the tilt: systems pay for rescue, starve prevention")
    print("step 2 - the bond: $%.1fM prevention program, %.1fx return in averted costs" % (invest / 1e6, ret_multiple))
    print("step 3 - the harvest: $%.1fM net over %d years ($%.0f/year back to the pool)" % (net / 1e6, int(horizon), per_year))
    print("step 4 - the fix: cross-budget pools so the saver funds the spender")
    assert 4.5e6 < net < 4.7e6, net
    assert 450000 < per_year < 470000, per_year
    print("CONFIRM panel: funded pools show measured averted costs exceeding program costs over 5-10 years.")
    print("REFUTE panel: honest measurement showing no net savings or health gain.")
    print("OK: %s walked the bond" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_air_pollution_burden(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: pricing the invisible - exposure-response to attributable fraction.
    # ADJUSTABLE ASSUMPTIONS: PM2.5 level and relative risk per 10 ug/m3.
    pm, guideline, rr10 = 35.0, 5.0, 1.08
    excess_units = (pm - guideline) / 10.0
    rr = rr10 ** excess_units
    af = (rr - 1.0) / rr
    print("step 1 - exposure: %.0f ug/m3 vs guideline %.0f -> %.0f excess units" % (pm, guideline, excess_units))
    print("step 2 - risk: relative risk = %.3f" % rr)
    print("step 3 - burden: attributable fraction = %.1f%% of exposed deaths" % (af * 100))
    print("step 4 - the price: put the per-ton mortality cost inside every permit decision")
    assert 1.25 < rr < 1.27, rr
    assert 0.20 < af < 0.22, af
    print("CONFIRM panel: health-priced permits cut pollution and mortality faster than controls.")
    print("REFUTE panel: priced damage failing to move emissions under real energy politics.")
    print("OK: %s walked the price" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_pandemic_prediction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: contact-risk forecasting - the spillover weather service.
    # ADJUSTABLE ASSUMPTIONS: emerging-disease rate per year and pandemic-capable fraction.
    eids_per_year, p_pandemic = 5.2, 0.02
    per_decade = eids_per_year * 10.0
    expected = per_decade * p_pandemic
    print("step 1 - the drumbeat: ~%.1f novel emerging diseases per year" % eids_per_year)
    print("step 2 - per decade: %.0f emergence events" % per_decade)
    print("step 3 - the forecast: %.2f expected pandemic-capable events per decade" % expected)
    print("step 4 - the service: watch the interfaces (markets, farms, forest fronts), not just the viruses")
    assert 1.03 < expected < 1.05, expected
    assert per_decade > 50.0, per_decade
    print("CONFIRM panel: interface alerts precede real spillovers, beating chance and hotspot baselines.")
    print("REFUTE panel: spillovers arriving without interface warning signs, or alert fatigue killing credibility.")
    print("OK: %s walked the forecast" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_spillover_prevention(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the IPBES bargain - prevention cost vs pandemic cost.
    # ADJUSTABLE ASSUMPTIONS: annual source-prevention cost and single-pandemic damage.
    prev_cost, pandemic_cost = 20.0e9, 10.0e12
    ratio = pandemic_cost / prev_cost
    break_even_p = prev_cost / pandemic_cost
    print("step 1 - the bargain: $%.0fB/year of source prevention" % (prev_cost / 1e9))
    print("step 2 - the stakes: $%.0fT for one pandemic" % (pandemic_cost / 1e12))
    print("step 3 - the ratio: prevention is %.0fx cheaper than a single catastrophe" % ratio)
    print("step 4 - break-even: prevention pays even if it stops a pandemic with P = %.4f%%" % (break_even_p * 100))
    assert 499.0 < ratio < 501.0, ratio
    assert break_even_p < 0.003, break_even_p
    print("CONFIRM panel: bonded interfaces show contact-risk declines without displacement.")
    print("REFUTE panel: spillover too rare and stochastic to price, or full displacement to unbonded frontiers.")
    print("OK: %s walked the bargain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_health_equity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the gradient as compounded interest - life-years by postcode.
    # ADJUSTABLE ASSUMPTIONS: the income-longevity gap and the exposed population.
    gap_years, pop = 14.6, 100000.0
    life_years_lost = gap_years * pop
    per_1000 = life_years_lost / 100.0
    print("step 1 - the gradient: %.1f years of life between top and bottom income percentiles" % gap_years)
    print("step 2 - the city: %.2f million life-years missing per 100k poor residents" % (life_years_lost / 1e6))
    print("step 3 - per thousand: %.0f life-years per 1000 people - a whole town's lifetimes" % per_1000)
    print("step 4 - the accounting: score every major policy for its gradient effect before adoption")
    assert 1.45e6 < life_years_lost < 1.47e6, life_years_lost
    assert 14590 < per_1000 < 14610, per_1000
    print("CONFIRM panel: scored policies shift toward gradient-narrowing choices vs unscored controls.")
    print("REFUTE panel: scoring changing nothing, or gradients immovable under full cross-government effort.")
    print("OK: %s walked the gradient" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_cold_chain(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: last-mile reliability engineering - excursion math per leg.
    # ADJUSTABLE ASSUMPTIONS: excursion probability per leg, legs to the last mile.
    vials, legs = 1000.0, 3
    p_old, p_new = 0.30, 0.05
    surv_old = (1.0 - p_old) ** legs
    surv_new = (1.0 - p_new) ** legs
    wasted_old = vials * (1.0 - surv_old)
    wasted_new = vials * (1.0 - surv_new)
    print("step 1 - old chain: %.0f%% excursion/leg over %d legs -> %.1f%% survive" % (p_old * 100, legs, surv_old * 100))
    print("step 2 - wasted: %.0f of %.0f vials dead on arrival" % (wasted_old, vials))
    print("step 3 - redesigned: passive carriers + indicators -> %.1f%% survive, %.0f wasted" % (surv_new * 100, wasted_new))
    print("step 4 - the rule: the worker must know the dose is alive before giving it")
    assert 655 < wasted_old < 659, wasted_old
    assert 140 < wasted_new < 146, wasted_new
    assert wasted_new < wasted_old * 0.25, (wasted_old, wasted_new)
    print("CONFIRM panel: pilot districts show collapsed wastage and rising verified-potency coverage.")
    print("REFUTE panel: thermostability unattainable for key vaccines, or the stack unaffordable at scale.")
    print("OK: %s walked the last mile" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_aging_care_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the dependency arithmetic - who cares for whom in 2050.
    # ADJUSTABLE ASSUMPTIONS: elderly and working-age populations, share needing daily help.
    elderly, working = 1.6e9, 4.9e9
    dep_ratio = elderly / working
    need_help = elderly * 0.10
    workers_needed = need_help / 4.0
    print("step 1 - 2050: %.1fB over 65 supported by %.1fB working-age -> dependency ratio %.2f" % (elderly / 1e9, working / 1e9, dep_ratio))
    print("step 2 - daily-help need: %.0f million elders" % (need_help / 1e6))
    print("step 3 - formal workforce at 1:4 ratio: %.0f million care workers" % (workers_needed / 1e6))
    print("step 4 - the grid: age-friendly environments + supported family caregivers + community teams + prefunded insurance")
    assert 0.32 < dep_ratio < 0.34, dep_ratio
    assert 39.0e6 < workers_needed < 41.0e6, workers_needed
    print("CONFIRM panel: grid districts deliver more independent-function years per elder at sustainable cost.")
    print("REFUTE panel: caregiver support failing to prevent burnout at scale, or prefunding politically impossible.")
    print("OK: %s walked the wave" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_opioid_crisis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the hydra market - wave growth and the iron law of prohibition.
    # ADJUSTABLE ASSUMPTIONS: overdose deaths 2010 and 2022 (US wave endpoints).
    d2010, d2022, years = 21000.0, 110000.0, 12.0
    factor = d2022 / d2010
    annual = factor ** (1.0 / years)
    print("step 1 - the waves: %.0fk deaths (2010) -> %.0fk (2022), %.2fx in %d years" % (d2010 / 1e3, d2022 / 1e3, factor, int(years)))
    print("step 2 - the growth: %.1f%% annual growth through pills, heroin, fentanyl" % ((annual - 1.0) * 100))
    print("step 3 - the iron law: each crackdown selected for potency - the market's answer to enforcement")
    print("step 4 - the flip: survival-first stack - naloxone saturation, treatment on demand, safe supply pilots")
    assert 1.14 < annual < 1.16, annual
    assert 5.2 < factor < 5.3, factor
    print("CONFIRM panel: survival-stack jurisdictions show sustained overdose declines vs supply-focused neighbors.")
    print("REFUTE panel: full survival stacks failing to bend the curve, or safe supply expanding initiation.")
    print("OK: %s walked the waves" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_diabetes_reversal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the DiRECT exit - remission arithmetic and the number needed to treat.
    # ADJUSTABLE ASSUMPTIONS: remission rates for structured program vs standard care.
    rem_int, rem_ctl = 0.46, 0.04
    nnt = 1.0 / (rem_int - rem_ctl)
    per_1000 = 1000.0 * (rem_int - rem_ctl)
    print("step 1 - DiRECT: %.0f%% remission (program) vs %.0f%% (standard care) at one year" % (rem_int * 100, rem_ctl * 100))
    print("step 2 - NNT: treat %.2f patients to produce one extra remission" % nnt)
    print("step 3 - scale: %.0f extra remissions per 1000 new diagnoses on the pathway" % per_1000)
    print("step 4 - the door: remission-default pathway at every diagnosis, clinics accountable for remission rates")
    assert 2.37 < nnt < 2.39, nnt
    assert 419 < per_1000 < 421, per_1000
    print("CONFIRM panel: pathway districts show population remission far above standard care, sustained at five years.")
    print("REFUTE panel: remission unmaintainable outside trials - weight regain erasing the exit at scale.")
    print("OK: %s walked the exit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_hypertension_control(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the cheapest win in chronic disease - control-rate arithmetic.
    # ADJUSTABLE ASSUMPTIONS: global hypertensives, current control, grid control target.
    total, ctl_now, ctl_grid = 1.28e9, 0.20, 0.70
    uncontrolled = total * (1.0 - ctl_now)
    newly_controlled = total * (ctl_grid - ctl_now)
    print("step 1 - the burden: %.2fB adults hypertensive, %.0f%% controlled" % (total / 1e9, ctl_now * 100))
    print("step 2 - the miss: %.2fB uncontrolled on pennies-a-day drugs" % (uncontrolled / 1e9))
    print("step 3 - the grid: protocol-driven care to %.0f%% -> %.2fB newly controlled" % (ctl_grid * 100, newly_controlled / 1e9))
    print("step 4 - the logistics: screening where people are, 90-day refills, registries that chase the lost")
    assert 1.02e9 < uncontrolled < 1.03e9, uncontrolled
    assert 6.39e8 < newly_controlled < 6.41e8, newly_controlled
    print("CONFIRM panel: grid districts reach 70% control at low cost, sustained for years.")
    print("REFUTE panel: adherence unfixable even with free drugs at the doorstep.")
    print("OK: %s walked the grid" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_amr(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the commons draining - resistance growth vs the dry pipeline.
    # ADJUSTABLE ASSUMPTIONS: 2019 attributable deaths and the 2050 warning level.
    d2019, d2050, years = 1.27e6, 10.0e6, 31.0
    annual = (d2050 / d2019) ** (1.0 / years)
    double_years = math.log(2.0) / math.log(annual)
    print("step 1 - the toll: %.2fM deaths directly attributable to AMR (2019)" % (d2019 / 1e6))
    print("step 2 - the warning: %.0fM/year by 2050 implies %.1f%% annual growth" % (d2050 / 1e6, (annual - 1.0) * 100))
    print("step 3 - the clock: deaths doubling every %.1f years on this path" % double_years)
    print("step 4 - the reserve: delinked pull incentives + stewardship with teeth + diagnostics + alternatives")
    assert 1.06 < annual < 1.08, annual
    assert 10.0 < double_years < 11.0, double_years
    print("CONFIRM panel: delinked incentives revive the pipeline; stewardship bends resistance curves.")
    print("REFUTE panel: evolution outpacing even a revived pipeline, or agricultural use untouchable everywhere.")
    print("OK: %s walked the commons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_misinformation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the adversarial information market - virality arithmetic.
    # ADJUSTABLE ASSUMPTIONS: per-generation spread of a falsehood vs a correction.
    r_mis, r_cor, gens = 2.5, 0.8, 5
    reach_mis = r_mis ** gens
    reach_cor = r_cor ** gens
    print("step 1 - the lie: R=%.1f over %d generations -> reach %.1f" % (r_mis, gens, reach_mis))
    print("step 2 - the correction: R=%.1f over %d generations -> reach %.2f" % (r_cor, gens, reach_cor))
    print("step 3 - the asymmetry: misinformation out-reaches correction %.0fx" % (reach_mis / reach_cor))
    print("step 4 - the defense: prebunk at scale, trusted messengers, friction on viral falsehoods")
    assert 97.0 < reach_mis < 99.0, reach_mis
    assert 0.32 < reach_cor < 0.34, reach_cor
    assert reach_mis / reach_cor > 200.0, reach_mis / reach_cor
    print("CONFIRM panel: stacked jurisdictions show misinformation belief declining vs controls in outbreaks.")
    print("REFUTE panel: prebunking failing outside labs, or virality friction technically impossible.")
    print("OK: %s walked the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_workforce_shortage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the draining pool - training vs attrition arithmetic to 2030.
    # ADJUSTABLE ASSUMPTIONS: annual training output and annual attrition (burnout, exits, migration).
    shortfall = 10.0e6
    train, attr, years = 1.0e6, 1.5e6, 5.0
    net_per_year = train - attr
    gap_2030 = shortfall - net_per_year * years
    print("step 1 - the gap: %.0fM worker shortfall projected" % (shortfall / 1e6))
    print("step 2 - the flows: +%.1fM trained, -%.1fM lost per year = net %+.1fM/year" % (train / 1e6, attr / 1e6, net_per_year / 1e6))
    print("step 3 - 2030: the gap grows to %.1fM on current flows" % (gap_2030 / 1e6))
    print("step 4 - the compact: paid community workforces, retention, recruitment bonds, task-shifting")
    assert 12.4e6 < gap_2030 < 12.6e6, gap_2030
    assert net_per_year < 0, net_per_year
    print("CONFIRM panel: compact regions raise workforce density toward need with improving retention.")
    print("REFUTE panel: paid community models unaffordable at national scale everywhere tried.")
    print("OK: %s walked the pool" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_tb_malaria_endgame(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: endgame economics - the decline rate the last mile demands.
    # ADJUSTABLE ASSUMPTIONS: halving time required to reach near-zero incidence.
    halve_years = 5.0
    annual_decline = 1.0 - 0.5 ** (1.0 / halve_years)
    cases, years = 1000.0, 15.0
    remaining = cases * (1.0 - annual_decline) ** years
    print("step 1 - the demand: halve incidence every %.0f years to reach the endgame" % halve_years)
    print("step 2 - the rate: %.1f%% annual decline, every year, for decades" % (annual_decline * 100))
    print("step 3 - the last mile: 1000 cases -> %.0f after %d years at that rate" % (remaining, int(years)))
    print("step 4 - the hunt: active case-finding, resistance surveillance, last-mile funds that grow as cases shrink")
    assert 0.12 < annual_decline < 0.14, annual_decline
    assert 120 < remaining < 130, remaining
    print("CONFIRM panel: compact regions drive incidence to near zero and hold it against importation.")
    print("REFUTE panel: resistance outpacing every regimen, or last-mile costs unfundable everywhere.")
    print("OK: %s walked the last mile" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_one_health(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: governing the interface - detection-delay arithmetic.
    # ADJUSTABLE ASSUMPTIONS: detection delay under siloed vs joint surveillance, doubling time.
    delay_silo, delay_joint, doubling = 30.0, 12.0, 7.0
    mult_silo = 2.0 ** (delay_silo / doubling)
    mult_joint = 2.0 ** (delay_joint / doubling)
    print("step 1 - siloed: %d-day detection delay at %d-day doubling -> %.1fx cases by detection" % (int(delay_silo), int(doubling), mult_silo))
    print("step 2 - joint: %d-day detection delay -> %.1fx cases by detection" % (int(delay_joint), mult_joint))
    print("step 3 - the dividend: joint surveillance catches the event %.1fx smaller" % (mult_silo / mult_joint))
    print("step 4 - the institution: pooled interface budgets, shared data, joint response teams")
    assert 19.0 < mult_silo < 20.0, mult_silo
    assert 3.2 < mult_joint < 3.4, mult_joint
    assert mult_silo / mult_joint > 5.0, mult_silo / mult_joint
    print("CONFIRM panel: compact countries detect and contain interface events faster and cheaper.")
    print("REFUTE panel: ministries refusing to pool budgets or share data under compact agreements.")
    print("OK: %s walked the interface" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_uhc_financing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the pooled purchaser - risk-pool arithmetic for a nation.
    # ADJUSTABLE ASSUMPTIONS: population, per-capita contribution, admin share, cost per person.
    pop, per_capita = 100.0e6, 50.0
    pool = pop * per_capita
    admin = 0.10
    care_fund = pool * (1.0 - admin)
    cost_per_person = 45.0
    covered = care_fund / cost_per_person
    print("step 1 - the pool: %.0fM people x $%.0f = $%.1fB national pool" % (pop / 1e6, per_capita, pool / 1e9))
    print("step 2 - after %.0f%% admin: $%.1fB for care" % (admin * 100, care_fund / 1e9))
    print("step 3 - at $%.0f/person: %.0fM covered (need: %.0fM)" % (cost_per_person, covered / 1e6, pop / 1e6))
    print("step 4 - the design: general revenue + earmarked health taxes, one strategic purchaser, published protection")
    assert 4.99e9 < pool < 5.01e9, pool
    assert covered >= pop, (covered, pop)
    print("CONFIRM panel: adopting countries drive catastrophic spending toward zero on domestic revenue.")
    print("REFUTE panel: tax bases too narrow to fund the package anywhere attempted.")
    print("OK: %s walked the pool" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_postviral_syndromes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the observatory - scale arithmetic for mechanism-first research.
    # ADJUSTABLE ASSUMPTIONS: cumulative infections and the persistent-symptom rate.
    infections, rate = 6.5e9, 0.06
    cases = infections * rate
    subtypes = 4.0
    per_subtype = cases / subtypes
    print("step 1 - the scale: %.1fB infections x %.0f%% persistent = %.0fM people" % (infections / 1e9, rate * 100, cases / 1e6))
    print("step 2 - the stratification: %.0f mechanistic subtypes -> %.0fM per subtype to study" % (subtypes, per_subtype / 1e6))
    print("step 3 - the design: deep phenotyping vs recovered controls, platform trials per subtype")
    print("step 4 - the honesty: normal standard tests mean the tests are wrong, not the patients")
    assert 3.8e8 < cases < 4.0e8, cases
    assert 9.5e7 < per_subtype < 10.0e7, per_subtype
    print("CONFIRM panel: stable subtypes with distinct biomarkers; targeted treatments beating one-size-fits-all.")
    print("REFUTE panel: no stable subtypes at any phenotyping depth - irreducible heterogeneity.")
    print("OK: %s walked the observatory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_climate_adaptation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: stress-testing - heat mortality with and without early warning.
    # ADJUSTABLE ASSUMPTIONS: baseline heat-death rate, warming multiplier, warning effectiveness.
    base_rate = 100.0
    warming_mult = 2.0
    warn_cut = 0.30
    unadapted = base_rate * warming_mult
    adapted = unadapted * (1.0 - warn_cut)
    saved_per_100k = unadapted - adapted
    print("step 1 - baseline: %.0f heat deaths per 100k elderly per hot season" % base_rate)
    print("step 2 - unadapted at +2C: %.0f per 100k" % unadapted)
    print("step 3 - with heat early-warning (%.0f%% cut): %.0f per 100k" % (warn_cut * 100, adapted))
    print("step 4 - saved: %.0f lives per 100k elderly per season - the adaptation dividend" % saved_per_100k)
    assert 139.0 < adapted < 141.0, adapted
    assert 59.0 < saved_per_100k < 61.0, saved_per_100k
    print("CONFIRM panel: standardized districts show lower climate-attributable mortality than controls.")
    print("REFUTE panel: extremes exceeding engineered tolerances everywhere - the physical adaptation limit.")
    print("OK: %s walked the stress test" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_health_data_interop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the nervous system - duplicate-test arithmetic under fragmentation.
    # ADJUSTABLE ASSUMPTIONS: patients, duplicate-test rates fragmented vs interoperable, test cost.
    patients = 1.0e6
    dup_frag, dup_int, test_cost = 0.08, 0.01, 200.0
    savings = patients * (dup_frag - dup_int) * test_cost
    missed_allergy = patients * 0.002 * (dup_frag - dup_int) / (dup_frag - dup_int)
    print("step 1 - fragmented: %.0f%% duplicate tests; interoperable: %.0f%%" % (dup_frag * 100, dup_int * 100))
    print("step 2 - the waste: $%.1fM/year in duplicated tests per million patients" % (savings / 1e6))
    print("step 3 - the harm beyond money: missed allergies, broken continuity, blind surveillance")
    print("step 4 - the fix: patient-mediated APIs, blocking penalized, scorecards published")
    assert 1.39e7 < savings < 1.41e7, savings
    assert savings > 1.0e7, savings
    print("CONFIRM panel: scored jurisdictions raise exchange rates and care continuity.")
    print("REFUTE panel: blocking technically unavoidable, or breaches destroying consent for sharing.")
    print("OK: %s walked the exchange" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_syndromic_surveillance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the early-warning dividend - exponential arithmetic of lead time.
    # ADJUSTABLE ASSUMPTIONS: cases at detection, doubling time, days of early warning.
    cases, doubling, lead = 10000.0, 7.0, 14.0
    reduction = 2.0 ** (lead / doubling)
    late_cases = cases * reduction
    averted = late_cases - cases
    print("step 1 - late detection: %.0f cases become %.0f after %d more days" % (cases, late_cases, int(lead)))
    print("step 2 - early warning: act %d days sooner at %.0f cases" % (int(lead), cases))
    print("step 3 - the dividend: %.0f cases averted - a %.0fx smaller outbreak" % (averted, reduction))
    print("step 4 - the pipeline: verified signals, published accuracy, pre-funded playbooks per alert level")
    assert 29900 < averted < 30100, averted
    assert 3.9 < reduction < 4.1, reduction
    print("CONFIRM panel: the pipeline detects real events days to weeks ahead with tolerable false alarms.")
    print("REFUTE panel: signals inseparable from noise at usable false-alarm rates.")
    print("OK: %s walked the signal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_behavior_change_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: structure-first - COM-B arithmetic for campaign vs environment.
    # ADJUSTABLE ASSUMPTIONS: capability, opportunity, motivation levels (multiplicative model).
    C, O, M = 0.8, 0.3, 0.9
    base = C * O * M
    campaign = C * O * 1.0      # persuasion maxes motivation; opportunity still binds
    structural = C * 0.8 * M    # environment fix lifts opportunity
    print("step 1 - baseline: C=%.1f x O=%.1f x M=%.1f -> behavior %.3f" % (C, O, M, base))
    print("step 2 - campaign (motivation to max): behavior %.3f (+%.1f%%)" % (campaign, (campaign - base) / base * 100))
    print("step 3 - structural (opportunity fixed): behavior %.3f (+%.1f%%)" % (structural, (structural - base) / base * 100))
    print("step 4 - the doctrine: fund the binding constraint first; campaign only to announce the new default")
    assert 0.215 < base < 0.218, base
    assert 0.239 < campaign < 0.241, campaign
    assert 0.575 < structural < 0.578, structural
    assert (structural - base) > (campaign - base) * 10.0, (campaign, structural)
    print("CONFIRM panel: structure-first programs change behavior where persuasion-only programs do not.")
    print("REFUTE panel: structural changes failing to move behavior - constraints cultural beyond policy.")
    print("OK: %s walked the doctrine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_dementia_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the dementia compact - prevalence arithmetic and the preventable fraction.
    # ADJUSTABLE ASSUMPTIONS: current prevalence, 2050 multiplier, preventable share.
    now, mult, preventable = 55.0e6, 3.0, 0.40
    future = now * mult
    preventable_cases = future * preventable
    caregivers = future * 0.8   # most care falls on families
    print("step 1 - today: %.0fM people live with dementia" % (now / 1e6))
    print("step 2 - 2050: %.0fM on current trends" % (future / 1e6))
    print("step 3 - preventable: %.0f%% of future cases = %.0fM (midlife risk-factor programs)" % (preventable * 100, preventable_cases / 1e6))
    print("step 4 - the care: %.0fM needing human care - the compact funds the care economy before the wave" % (caregivers / 1e6))
    assert 164.0e6 < future < 166.0e6, future
    assert 65.0e6 < preventable_cases < 67.0e6, preventable_cases
    print("CONFIRM panel: compact regions bend incidence down and sustain care quality vs controls.")
    print("REFUTE panel: the preventable fraction unreachable at population scale.")
    print("OK: %s walked the compact" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_ncd_transition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the driver-level offensive - best-buy arithmetic on tobacco tax.
    # ADJUSTABLE ASSUMPTIONS: tobacco deaths, tax-driven prevalence cut, pass-through to mortality.
    tobacco_deaths = 8.0e6
    tax_cut = 0.10
    averted = tobacco_deaths * tax_cut
    share_ncd = 0.74
    print("step 1 - the wave: NCDs cause %.0f%% of all deaths on earth" % (share_ncd * 100))
    print("step 2 - one best buy: tobacco tax cutting smoking %.0f%%" % (tax_cut * 100))
    print("step 3 - the yield: %.0f deaths averted per year from this single lever" % averted)
    print("step 4 - the offensive: the full best-buy package legislated together, drivers not diseases")
    assert 790000 < averted < 810000, averted
    assert averted > 0.5e6, averted
    print("CONFIRM panel: offensive jurisdictions bend premature NCD mortality faster than siloed controls.")
    print("REFUTE panel: best buys failing where fully implemented - drivers unmodifiable by policy.")
    print("OK: %s walked the offensive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_uspu_population_health_theory(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the production function - what a predictive theory must beat.
    # ADJUSTABLE ASSUMPTIONS: variance explained by the unified theory vs naive baselines.
    r2_naive, r2_single, r2_theory = 0.40, 0.52, 0.65
    gain_vs_naive = r2_theory - r2_naive
    gain_vs_single = r2_theory - r2_single
    print("step 1 - naive baseline (trend extrapolation): R^2 = %.2f" % r2_naive)
    print("step 2 - single-determinant model: R^2 = %.2f" % r2_single)
    print("step 3 - the theory (interactions + feedbacks): R^2 = %.2f" % r2_theory)
    print("step 4 - the bar: +%.2f over naive, +%.2f over single - pre-registered, out-of-sample, or it does not count" % (gain_vs_naive, gain_vs_single))
    assert 0.24 < gain_vs_naive < 0.26, gain_vs_naive
    assert 0.12 < gain_vs_single < 0.14, gain_vs_single
    print("CONFIRM panel: pre-registered predictions beat baselines across diverse populations.")
    print("REFUTE panel: no model beating naive out-of-sample - irreducible complexity.")
    print("OK: %s walked the function" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "vaccine-hesitancy": demo_uspu_vaccine_hesitancy,
 "obesity-drivers": demo_uspu_obesity_drivers,
 "seasonal-flu-burden": demo_uspu_seasonal_flu_burden,
 "tobacco-persistence": demo_uspu_tobacco_persistence,
 "food-deserts": demo_uspu_food_deserts,
 "lead-exposure": demo_uspu_lead_exposure,
 "clean-water-gaps": demo_uspu_clean_water_gaps,
 "loneliness-epidemic": demo_uspu_loneliness_epidemic,
 "mental-health-access": demo_uspu_mental_health_access,
 "maternal-disparities": demo_uspu_maternal_disparities,
 "chronic-care-gap": demo_uspu_chronic_care_gap,
 "air-pollution-burden": demo_uspu_air_pollution_burden,
 "pandemic-prediction": demo_uspu_pandemic_prediction,
 "spillover-prevention": demo_uspu_spillover_prevention,
 "health-equity": demo_uspu_health_equity,
 "cold-chain": demo_uspu_cold_chain,
 "aging-care-models": demo_uspu_aging_care_models,
 "opioid-crisis": demo_uspu_opioid_crisis,
 "diabetes-reversal": demo_uspu_diabetes_reversal,
 "hypertension-control": demo_uspu_hypertension_control,
 "amr": demo_uspu_amr,
 "misinformation": demo_uspu_misinformation,
 "workforce-shortage": demo_uspu_workforce_shortage,
 "tb-malaria-endgame": demo_uspu_tb_malaria_endgame,
 "one-health": demo_uspu_one_health,
 "uhc-financing": demo_uspu_uhc_financing,
 "postviral-syndromes": demo_uspu_postviral_syndromes,
 "climate-adaptation": demo_uspu_climate_adaptation,
 "health-data-interop": demo_uspu_health_data_interop,
 "syndromic-surveillance": demo_uspu_syndromic_surveillance,
 "behavior-change-scale": demo_uspu_behavior_change_scale,
 "dementia-scale": demo_uspu_dementia_scale,
 "ncd-transition": demo_uspu_ncd_transition,
 "population-health-theory": demo_uspu_population_health_theory,
}
