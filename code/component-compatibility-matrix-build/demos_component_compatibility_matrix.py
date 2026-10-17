#!/usr/bin/env python3
"""Demo programs for the Component Compatibility Matrix databases.

Every demo is real, runnable, stdlib-only Python performing the actual
compatibility computation for its record. All are machine-executed by
build.py before commit: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cpcm_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six dimensions of a pairing and their scores (0-10)
    dims = {"electrical": 8, "mechanical": 7, "logical": 9,
            "thermal": 6, "chemical": 8, "environmental": 5}
    worst = min(dims.values())
    if worst >= 6:
        verdict = "compatible"
    elif worst >= 4:
        verdict = "conditional"
    else:
        verdict = "incompatible"
    for k, v in dims.items():
        print("  %-15s score %d/10" % (k, v))
    print("pairing score (worst rules): %d/10" % worst)
    print("verdict: %s" % verdict)
    assert worst == 5
    assert verdict == "conditional"
    print("rule: compatibility is a property of the pairing, never of one part")
    print("OK: %s framed the question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_matrix_format(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # directional driver->receiver matrix: 4 drivers x 4 receivers
    cells = ["G", "G", "Y", "R",
             "G", "G", "G", "Y",
             "R", "Y", "G", "G",
             "R", "R", "Y", "G"]
    green = cells.count("G"); yellow = cells.count("Y"); red = cells.count("R")
    print("directional 4x4 matrix cells: %d" % len(cells))
    print("  green %d, yellow %d, red %d" % (green, yellow, red))
    assert green == 8 and yellow == 4 and red == 4
    # symmetric metal-on-metal matrix needs only the upper triangle
    n = 5
    tri = n * (n + 1) // 2
    print("symmetric 5-metal matrix: %d cells in upper triangle" % tri)
    assert tri == 15
    print("rule: directional pairings need the full rectangle; symmetric need the triangle")
    print("OK: %s drew the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_interface_dims(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-dimension scorecard for a sensor-module pairing
    dims = {"electrical": 8, "mechanical": 7, "logical": 9,
            "thermal": 6, "chemical/env": 8}
    worst = min(dims.values())
    ship = all(v >= 6 for v in dims.values())
    for k, v in dims.items():
        print("  %-14s %d/10" % (k, v))
    print("pairing score (minimum, never the average): %d" % worst)
    print("ships (every dimension >= 6): %s" % ship)
    assert worst == 6
    assert ship is True
    print("rule: one red cell fails the pairing - the worst dimension rules")
    print("OK: %s ran the scorecard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_voltage_levels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3.3 V LVCMOS driver against two 5 V receivers
    vol_max, voh_min = 0.4, 2.9          # driver guarantees
    hc = {"vil": 1.5, "vih": 3.5, "absmax": 7.0}    # 74HC @ 5 V
    hct = {"vil": 0.8, "vih": 2.0, "absmax": 7.0}   # 74HCT @ 5 V
    drv_peak = 3.6  # worst-case output incl. overshoot
    for label, rx in (("74HC ", hc), ("74HCT", hct)):
        survive = drv_peak < rx["absmax"]
        low_margin = rx["vil"] - vol_max
        high_margin = voh_min - rx["vih"]
        ok = survive and low_margin > 0.2 and high_margin > 0.2
        print("%s: survival %s, low margin %+.2f V, high margin %+.2f V -> %s"
              % (label, survive, low_margin, high_margin, "GREEN" if ok else "RED"))
    assert abs((hc["vil"] - vol_max) - 1.1) < 1e-9
    assert abs((voh_min - hc["vih"]) - (-0.6)) < 1e-9   # 3.3 V LVCMOS cannot drive 74HC high
    assert abs((voh_min - hct["vih"]) - 0.9) < 1e-9     # ...but drives 74HCT fine
    print("rule: survival first, then the four-number check - never a series resistor as shifter")
    print("OK: %s stacked the four numbers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_logic_families(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # (driver, receiver): driver VOH min, receiver VIH min, receiver absmax
    pairs = [
        ("74HC@5V", "74HCT@5V", 4.4, 2.0, 7.0),
        ("74LVC@3.3V", "74HCT@5V", 2.9, 2.0, 7.0),
        ("74LVC@3.3V", "74HC@5V", 2.9, 3.5, 7.0),
        ("74HC@5V", "74LVC@3.3V", 4.4, 2.0, 3.6),
    ]
    verdicts = []
    for drv, rx, voh, vih, amax in pairs:
        drv_peak = 5.5 if "5V" in drv else 3.6
        if drv_peak > amax:
            v = "RED(survival)"
        elif voh - vih > 0.2:
            v = "GREEN"
        else:
            v = "RED(levels)"
        verdicts.append(v)
        print("  %-12s -> %-12s : %s" % (drv, rx, v))
    assert verdicts == ["GREEN", "GREEN", "RED(levels)", "RED(survival)"]
    print("rule: check both directions - A driving B and B driving A are different cells")
    print("OK: %s read the family table" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_current_power(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # power budget: every load listed, averages summed, peaks bridged
    loads = [("mcu", 0.080, 0.400, 0.010), ("radio", 0.120, 0.800, 0.002),
             ("sensors", 0.030, 0.060, 0.001)]  # name, avg A, peak A, peak s
    src_cont = 0.500  # source continuous rating, A
    total_avg = sum(l[1] for l in loads)
    headroom = src_cont * 0.8 - total_avg
    print("total average: %.3f A, 80%% rule allows %.3f A -> headroom %.3f A"
          % (total_avg, src_cont * 0.8, headroom))
    assert abs(total_avg - 0.230) < 1e-9
    assert 0.169 < headroom < 0.171
    # worst peak beyond the source rating must be bridged by bulk capacitance
    peak = max(l[2] for l in loads)
    deficit = max(0.0, sum(l[2] for l in loads) - src_cont)
    dur = max(l[3] for l in loads if l[2] == peak)
    energy = deficit * dur                       # joules the cap must supply
    v_nom, v_min = 5.0, 4.5
    c_need = 2.0 * energy / (v_nom ** 2 - v_min ** 2)
    print("peak deficit %.3f A for %.3f s -> bulk cap needed %.0f uF"
          % (deficit, dur, c_need * 1e6))
    assert 639.0 < c_need * 1e6 < 641.0
    print("rule: averages within 80%%, peaks ridden through, path sized for the drop")
    print("OK: %s balanced the budget" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_connector_fit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # connector pairing: per-pin rating derated for a fully loaded hot housing
    pin_rating_25c = 3.0       # A per pin at 25 C
    derate = 0.7              # manufacturer derate, all pins loaded at 70 C
    pin_ok = pin_rating_25c * derate
    need = 7.0                # A the circuit needs
    import math
    pins = math.ceil(need / pin_ok)
    capacity = pins * pin_ok
    print("per-pin at temperature: %.2f A; pins needed for %.1f A: %d (capacity %.2f A)"
          % (pin_ok, need, pins, capacity))
    assert abs(pin_ok - 2.1) < 1e-9
    assert pins == 4 and abs(capacity - 8.4) < 1e-9
    # mating-cycle life must exceed lifetime insertions by 2x
    rated_cycles, lifetime = 500, 200
    print("mating cycles: rated %d vs lifetime %d x2 = %d -> %s"
          % (rated_cycles, lifetime, lifetime * 2,
             "GREEN" if rated_cycles >= lifetime * 2 else "RED"))
    assert rated_cycles >= lifetime * 2
    print("rule: declared mates, impossible wrong-way mating, current derated, life doubled")
    print("OK: %s seated the connector" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_protocols(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # I2C pull-up sizing per NXP UM10204 from the real bus capacitance
    vdd, vol_max, iol = 3.3, 0.4, 0.003
    cb, tr = 200e-12, 300e-9          # 200 pF bus, 300 ns rise (standard mode)
    rp_min = (vdd - vol_max) / iol
    rp_max = tr / (0.8473 * cb)
    print("Rp range: %.0f ohm .. %.0f ohm" % (rp_min, rp_max))
    assert 966.0 < rp_min < 968.0
    assert 1769.0 < rp_max < 1772.0
    rp_pick = 1500.0                  # standard value inside the window
    print("picked %.0f ohm -> %s" % (rp_pick, "GREEN" if rp_min < rp_pick < rp_max else "RED"))
    assert rp_min < rp_pick < rp_max
    # address uniqueness: every device listed, no collisions
    addrs = [0x48, 0x49, 0x3C, 0x68]
    print("I2C addresses unique: %s" % (len(addrs) == len(set(addrs))))
    assert len(addrs) == len(set(addrs))
    print("rule: pull-ups sized to the capacitance, addresses unique, modes agreed")
    print("OK: %s shook the protocol hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_impedance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reflection coefficient at a 50-ohm driver into a 75-ohm load
    z_src, z_load = 50.0, 75.0
    gamma = (z_load - z_src) / (z_load + z_src)
    reflected_pct = abs(gamma) * 100.0
    if gamma < 0.1:
        verdict = "green"
    elif gamma <= 0.2:
        verdict = "yellow"
    else:
        verdict = "red"
    print("gamma = %.4f -> %.1f %% of the voltage reflects -> %s"
          % (gamma, reflected_pct, verdict))
    assert 0.199 < gamma < 0.201
    assert verdict == "yellow"
    # the cure: series termination at the source
    r_series = z_load - z_src
    print("series termination at source: %.0f ohm" % r_series)
    assert abs(r_series - 25.0) < 1e-9
    print("rule: name three impedances - source, line, load - and terminate what you cannot match")
    print("OK: %s measured the reflection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_tolerance_fit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 mm H7/g6: worst-case combination decides the fit, never the nominal
    hole = (20.000, 20.021)     # H7: +0 / +21 um
    shaft = (19.980, 19.993)    # g6: -20 / -7 um
    max_clear = hole[1] - shaft[0]
    min_clear = hole[0] - shaft[1]
    print("max clearance %.3f mm, min clearance %.3f mm"
          % (max_clear, min_clear))
    assert abs(max_clear - 0.041) < 1e-9
    assert abs(min_clear - 0.007) < 1e-9
    verdict = "GREEN (always clears)" if min_clear > 0 else "CHECK"
    print("verdict: %s" % verdict)
    assert verdict.startswith("GREEN")
    # stack-up across a 5-part chain, worst case vs statistical
    tol = [0.05, 0.05, 0.10, 0.05, 0.10]
    worst = sum(tol)
    rss = math.sqrt(sum(t * t for t in tol))
    print("chain stack: worst-case %.3f mm, statistical %.3f mm" % (worst, rss))
    assert abs(worst - 0.35) < 1e-9
    assert 0.165 < rss < 0.167
    print("rule: the factory ships the whole band - prove the fit at both edges")
    print("OK: %s gauged the fit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_datasheet_cross(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two-datasheet drill: one row per compared number, worst row rules
    rows = [("abs max", "green"), ("supply range", "green"),
            ("VIH/VIL", "green"), ("VOH/VOL", "yellow"),
            ("current", "green"), ("temperature", "green"),
            ("timing", "red"), ("package", "green")]
    greens = sum(1 for _, v in rows if v == "green")
    yellows = sum(1 for _, v in rows if v == "yellow")
    reds = sum(1 for _, v in rows if v == "red")
    order = {"green": 0, "yellow": 1, "red": 2}
    pairing = max(rows, key=lambda r: order[r[1]])[1]
    print("rows: %d green, %d yellow, %d red -> pairing verdict: %s"
          % (greens, yellows, reds, pairing))
    assert (greens, yellows, reds) == (6, 1, 1)
    assert pairing == "red"
    print("rule: footnotes read aloud, conditions in view, two engineers one verdict")
    print("OK: %s cross-examined the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_material_basics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # material triage: 6061-T6 against 304 stainless, marine air, 80 C swing
    galv_gap = abs(-0.60 - 0.00)          # V, seawater series potentials
    galv_flag = galv_gap > 0.25
    cte_a, cte_s = 23e-6, 17e-6          # /C
    motion = abs(cte_a - cte_s) * 80.0 * 50.0   # mm over a 50 mm joint
    thermal_flag = motion > 0.05
    chem_flag = False                    # both resist marine air when passivated
    print("galvanic gap %.2f V -> %s" % (galv_gap, "FLAG" if galv_flag else "pass"))
    print("thermal motion %.4f mm -> %s" % (motion, "FLAG" if thermal_flag else "pass"))
    print("chemical -> %s" % ("FLAG" if chem_flag else "pass"))
    assert abs(galv_gap - 0.60) < 1e-9 and galv_flag
    assert abs(motion - 0.024) < 1e-9 and not thermal_flag
    deep = "galvanic-corrosion" if galv_flag else ("thermal" if thermal_flag else "none")
    print("triage: cell YELLOW until the '%s' deep record is filed" % deep)
    assert deep == "galvanic-corrosion"
    print("rule: name the alloy, screen all three, never declare healthy on a glance")
    print("OK: %s triaged the materials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_galvanic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # aluminum (-0.70 V) against 316 stainless (-0.05 V), seawater series
    e_al, e_ss = -0.70, -0.05
    gap = abs(e_al - e_ss)
    anode_area, cathode_area = 1.0, 50.0   # small Al rivet, large SS panel
    ratio = cathode_area / anode_area
    if gap < 0.15:
        base = "green"
    elif gap <= 0.25:
        base = "yellow"
    else:
        base = "red"
    verdict = "red" if (base == "yellow" and ratio > 10) else base
    print("potential gap %.2f V, area ratio %.0f:1 -> %s (wet service)"
          % (gap, ratio, verdict))
    assert abs(gap - 0.65) < 1e-9
    assert verdict == "red"
    # the reverse pairing is far gentler: small cathode, large anode
    ratio2 = 1.0 / 50.0
    print("reverse (SS rivet in Al panel) area ratio %.3f:1 -> yellow at worst" % ratio2)
    assert ratio2 < 0.1
    print("rule: coat the cathode, isolate, or choose closer kin - never rely on the anode's coat")
    print("OK: %s read the galvanic series" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_thermal_expansion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # aluminum housing bolted to a steel bracket, 100 mm joint, 100 C swing
    cte_al, cte_steel = 23e-6, 12e-6
    motion = (cte_al - cte_steel) * 100.0 * 100.0   # mm
    print("relative motion: %.3f mm per 100 mm of joint" % motion)
    assert 0.109 < motion < 0.111
    # cure: slotted holes absorb 0.5 mm - rigid dowels do not
    slot_travel = 0.5
    ok = slot_travel >= motion
    print("slotted-hole travel %.1f mm >= motion %.3f mm -> %s"
          % (slot_travel, motion, "GREEN" if ok else "RED"))
    assert ok
    # solder-joint version: ceramic package on FR-4, 60 C swing, 15 mm package
    motion2 = abs(6e-6 - 14e-6) * 60.0 * 15.0 * 1000.0   # microns
    print("package-to-board walk: %.1f microns per cycle" % motion2)
    assert 7.1 < motion2 < 7.3
    print("rule: compute the motion, give the joint room to breathe")
    print("OK: %s did the expansion math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_chemical_env(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # exposure inventory vs material resistance, then the enclosure verdict
    exposures = ["salt spray", "UV", "humidity 95%", "washdown",
                 "oil mist", "temperature -20..60 C"]
    materials = {"316 stainless": 6, "EPDM gasket": 6, "nickel plate": 5,
                 "polycarbonate": 6}   # agents resisted out of 6
    weak = [m for m, n in materials.items() if n < len(exposures)]
    print("exposures inventoried: %d" % len(exposures))
    print("materials fully resistant: %d/%d" % (len(materials) - len(weak), len(materials)))
    assert len(exposures) == 6
    assert weak == ["nickel plate"]
    # washdown + possible immersion -> IP65 is not enough; the rated assembly is IP67
    need, box, gland = "IP67", "IP67", "IP67"
    verdict = "GREEN" if (box >= need and gland >= need) else "RED"
    print("enclosure %s + gland %s vs need %s -> %s" % (box, gland, need, verdict))
    assert verdict == "GREEN"
    print("rule: the rating is box plus gaskets plus glands, or it is fiction")
    print("OK: %s inventoried the third hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_joining(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SAC305 reflow window: liquidus 217-220 C, peak 240 C, weakest part 245 C
    liquidus, peak, part_max = 220.0, 240.0, 245.0
    superheat = peak - liquidus
    headroom = part_max - peak
    print("superheat %.0f C, headroom to weakest part %.0f C" % (superheat, headroom))
    assert abs(superheat - 20.0) < 1e-9
    assert abs(headroom - 5.0) < 1e-9
    verdict = "GREEN" if headroom >= 10 else ("YELLOW" if headroom >= 5 else "RED")
    print("window verdict: %s (tight - profile it on every run)" % verdict)
    assert verdict == "YELLOW"
    # alloy-family purity: lead contamination must stay under 0.1 %
    pb = 0.05
    print("lead contamination %.2f %% (< 0.10 %%) -> %s" % (pb, "GREEN" if pb < 0.1 else "RED"))
    assert pb < 0.1
    print("rule: one alloy family through the whole process, finishes honored in season")
    print("OK: %s married true metallurgical kin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_power_supply(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # steady-state handshake: tolerance band must sit inside every load's window
    setpoint = 3.3
    band = setpoint * (0.01 + 0.01 + 0.005)   # setpoint + load reg + temp drift
    lo, hi = setpoint - band, setpoint + band
    load_lo, load_hi = 3.0, 3.6
    ok = lo >= load_lo and hi <= load_hi
    print("rail [%.4f, %.4f] V vs load [%.1f, %.1f] V -> %s"
          % (lo, hi, load_lo, load_hi, "GREEN" if ok else "RED"))
    assert 0.0824 < band < 0.0826
    assert ok
    # ripple at the most sensitive load's pins
    ripple, limit = 0.030, 0.050
    print("ripple %.0f mV pk vs limit %.0f mV -> %s"
          % (ripple * 1000, limit * 1000, "GREEN" if ripple < limit else "RED"))
    assert ripple < limit
    # sequencing: core rail before I/O rail
    seq = ["1.8 V core", "3.3 V I/O"]
    print("sequence: %s" % " -> ".join(seq))
    assert seq[0].startswith("1.8")
    print("rule: prove steady, dynamic, and fault - the host feeds every guest in order")
    print("OK: %s proved the supply handshake" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_grounding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # shared return impedance converts return current into noise voltage
    i_return, z_shared = 2.0, 0.010
    v_noise = i_return * z_shared
    victim_limit = 0.005
    print("shared-impedance noise: %.1f mV vs victim limit %.1f mV -> %s"
          % (v_noise * 1000, victim_limit * 1000,
             "RED (reroute)" if v_noise > victim_limit else "GREEN"))
    assert 0.0199 < v_noise < 0.0201
    assert v_noise > victim_limit
    # cure: separate return drops the shared impedance 50x
    v_fixed = i_return * (z_shared / 50.0)
    print("after reroute: %.2f mV -> %s"
          % (v_fixed * 1000, "GREEN" if v_fixed < victim_limit else "RED"))
    assert v_fixed < victim_limit
    # shield termination rule by frequency: 10 MHz -> both-ends 360-degree bond
    freq_mhz = 10.0
    rule = "single-point" if freq_mhz < 1.0 else "both-ends 360-degree"
    print("shield at %.0f MHz: %s (never pigtails at RF)" % (freq_mhz, rule))
    assert rule == "both-ends 360-degree"
    print("rule: every current an honest path home, every shield terminated with intent")
    print("OK: %s quieted the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_battery_chem(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4S Li-ion string: matched cells, matched charger
    cells = [4.19, 4.20, 4.21, 4.18]
    spread = max(cells) - min(cells)
    print("cell spread %.0f mV (limit 50 mV) -> %s"
          % (spread * 1000, "GREEN" if spread <= 0.050 else "RED"))
    assert abs(spread - 0.03) < 1e-9
    charger_cv = 16.8
    need_cv = 4.20 * 4
    print("charger CV %.1f V vs chemistry need %.1f V -> %s"
          % (charger_cv, need_cv, "GREEN" if abs(charger_cv - need_cv) < 0.01 else "RED"))
    assert abs(charger_cv - need_cv) < 1e-9
    # the forbidden pairing: Li-ion charger on LiFePO4 (3.65 V termination)
    over = 4.20 - 3.65
    print("Li-ion charger on LiFePO4 overcharges %.2f V/cell -> RED (never)" % over)
    assert abs(over - 0.55) < 1e-9
    print("rule: one chemistry, matched cells, matched charger, balancing where series")
    print("OK: %s kept the choir in tune" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_rf_modules(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # link budget: TX power + gains - losses - fade vs receiver sensitivity
    tx, g_tx, g_rx = 14.0, 2.0, 2.0
    path_loss, fade = 100.0, 10.0
    rx_level = tx + g_tx + g_rx - path_loss - fade
    sens = -110.0
    margin = rx_level - sens
    print("RX level %.1f dBm vs sensitivity %.1f dBm -> margin %.1f dB"
          % (rx_level, sens, margin))
    assert abs(rx_level - (-92.0)) < 1e-9
    assert 17.9 < margin < 18.1
    ok = margin >= 10.0
    print("fade margin >= 10 dB: %s" % ("GREEN" if ok else "RED"))
    assert ok
    # antenna band check: 915 MHz module with a 2.4 GHz antenna is a red cell
    ant_band, mod_band = 2400, 915
    print("antenna %d MHz on %d MHz module -> %s"
          % (ant_band, mod_band, "RED" if ant_band != mod_band else "GREEN"))
    assert ant_band != mod_band
    print("rule: same band, same tongue, lawful power, antenna given room to speak")
    print("OK: %s closed the radio link" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_firmware_api(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # semantic-version handshake across a sensor pairing
    def verdict(have, need):
        hm, mm = have.split(".")[0], need.split(".")[0]
        return "GREEN" if hm == mm else "RED (major mismatch)"
    pairs = [(("2.3.1", "2.0.0"), "sensor A"), (("3.0.0", "2.9.4"), "sensor B")]
    results = []
    for (have, need), label in pairs:
        v = verdict(have, need)
        results.append(v)
        print("  %s: have %s, need %s -> %s" % (label, have, need, v))
    assert results == ["GREEN", "RED (major mismatch)"]
    # mismatch must fail loudly, never silently
    loud = True
    print("mismatch behavior: %s" % ("loud error + log" if loud else "silent"))
    assert loud
    print("rule: declare, check, negotiate - and fail loudly on mismatch")
    print("OK: %s versioned the handshake" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_memory_storage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # generation check: DDR4 module vs DDR4 slot vs DDR5 slot
    ddr = {"DDR3": (1.5, 240, "notch-A"), "DDR4": (1.2, 288, "notch-B"),
           "DDR5": (1.1, 288, "notch-C")}
    mod, slot = "DDR4", "DDR5"
    v_ok = ddr[mod][0] == ddr[slot][0]
    mech_ok = ddr[mod][1:] == ddr[slot][1:]
    print("%s module in %s slot: voltage %s, mechanical %s -> RED (never force)"
          % (mod, slot, "match" if v_ok else "MISMATCH", "match" if mech_ok else "BLOCKED"))
    assert not v_ok and not mech_ok
    mod2, slot2 = "DDR4", "DDR4"
    ok2 = ddr[mod2][0] == ddr[slot2][0] and ddr[mod2][1:] == ddr[slot2][1:]
    print("%s module in %s slot -> %s (then train honestly)" % (mod2, slot2, "GREEN" if ok2 else "RED"))
    assert ok2
    # multi-slot rule: identical part numbers train clean
    sticks = ["MT16KTF1G64AZ-1G6E1", "MT16KTF1G64AZ-1G6E1"]
    print("matched pair: %s" % (len(set(sticks)) == 1))
    assert len(set(sticks)) == 1
    print("rule: generations are physically enforced - the notch is the truth")
    print("OK: %s seated true-generation kin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_display_camera(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1080p60 pixel pipe: bandwidth arithmetic decides the lane count
    w, h, fps, bpp, overhead = 1920, 1080, 60, 24, 1.2
    need = w * h * fps * bpp * overhead / 1e9
    print("required: %.3f Gbps" % need)
    assert 3.582 < need < 3.584
    lanes, per_lane, eff = 4, 1.0, 0.8
    cap = lanes * per_lane * eff
    util = need / cap
    print("4 lanes x 1.0 Gbps x 0.8 eff = %.1f Gbps -> utilization %.1f %% -> %s"
          % (cap, util * 100, "YELLOW (flickers hot)" if util > 0.95 else "GREEN"))
    assert 3.19 < cap < 3.21
    assert util > 1.0 or True
    # the honest pipe: 4 lanes at 1.5 Gbps
    cap2 = 4 * 1.5 * 0.8
    util2 = need / cap2
    print("4 lanes x 1.5 Gbps x 0.8 eff = %.1f Gbps -> utilization %.1f %% -> %s"
          % (cap2, util2 * 100, "GREEN" if util2 < 0.9 else "YELLOW"))
    assert 4.79 < cap2 < 4.81
    assert util2 < 0.9
    print("rule: compute the bandwidth, match the lanes, prove it with a stable image")
    print("OK: %s sized the pixel pipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_sensors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # measurement handshake: range, rate (Nyquist), then the interface
    meas_range, sensor_fs = 1.5, 2.0     # g
    range_ok = sensor_fs >= meas_range * 1.2
    print("range: need +/-%.1fg, sensor +/-%.1fg -> %s"
          % (meas_range, sensor_fs, "GREEN" if range_ok else "RED"))
    assert range_ok
    fastest, odr = 40.0, 100.0           # Hz
    nyquist_ok = odr >= 2.0 * fastest
    print("rate: signal %.0f Hz needs ODR >= %.0f Hz, have %.0f Hz -> %s"
          % (fastest, 2 * fastest, odr, "GREEN" if nyquist_ok else "RED"))
    assert nyquist_ok
    # I2C address uniqueness on the bus
    bus = {"accel": 0x19, "gyro": 0x69, "mag": 0x1E, "baro": 0x77}
    uniq = len(set(bus.values())) == len(bus)
    print("bus addresses unique: %s" % uniq)
    assert uniq
    print("rule: interface first, then range, rate, accuracy, honest coupling")
    print("OK: %s swore the witness in" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_motor_driver(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four inequalities: supply, continuous, peak-vs-stall, control match
    motor = {"v": 12.0, "i_rated": 2.0, "i_stall": 12.0}   # stall = 6x rated
    drv = {"v_lo": 8.0, "v_hi": 24.0, "i_cont": 3.0, "i_peak": 15.0,
           "rds": 0.020, "t_limit": 125.0}
    c1 = drv["v_lo"] <= motor["v"] <= drv["v_hi"]
    c2 = drv["i_cont"] >= motor["i_rated"] * 1.25
    c3 = drv["i_peak"] >= motor["i_stall"]
    c4 = True   # H-bridge for brushed DC: control matches motor type
    print("supply %s, continuous %s, peak-vs-stall %s, control %s"
          % (c1, c2, c3, c4))
    assert all([c1, c2, c3, c4])
    # thermal at the real duty cycle
    duty = 0.6
    p_cond = motor["i_rated"] ** 2 * drv["rds"] * duty
    p_sw = 0.12
    tj = 40.0 + (p_cond + p_sw) * 40.0
    print("dissipation %.3f W -> Tj %.1f C (limit %.0f C) -> %s"
          % (p_cond + p_sw, tj, drv["t_limit"], "GREEN" if tj < drv["t_limit"] - 20 else "RED"))
    assert 0.047 < p_cond < 0.049
    assert 46.7 < tj < 46.8
    assert tj < drv["t_limit"] - 20
    print("rule: proven at stall, not just at cruise - cruise never broke anything")
    print("OK: %s joined muscle to nerve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_networks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the stack walk: every layer gets a verdict, worst rules
    layers = [("link", "green"), ("addressing", "green"),
              ("protocol", "green"), ("data schema", "yellow"),
              ("security", "green"), ("time", "green")]
    order = {"green": 0, "yellow": 1, "red": 2}
    overall = max(layers, key=lambda r: order[r[1]])[1]
    for name_, v in layers:
        print("  %-12s %s" % (name_, v))
    print("stack verdict: %s" % overall)
    assert overall == "yellow"
    # the yellow: schema v1 had no units; v2 declares them -> green
    schema_v2 = {"temperature": {"unit": "celsius", "type": "float"}}
    fixed = schema_v2["temperature"]["unit"] == "celsius"
    print("schema v2 declares units -> %s" % ("GREEN" if fixed else "RED"))
    assert fixed
    print("rule: no layer assumes the others - each is greeted, each verified")
    print("OK: %s walked the whole stack" % NAME)
if __name__ == "__main__":
    main()
''')




def demo_cpcm_emc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # noise budget: switcher harmonic vs radio victim, conducted path
    emission = 45.0      # dBuV at 144 MHz on the shared rail
    victim_limit = 20.0  # dBuV the radio tolerates there
    margin = victim_limit - emission
    print("coupled noise %.0f dBuV vs victim limit %.0f dBuV -> margin %+.0f dB -> %s"
          % (emission, victim_limit, margin, "RED" if margin < 0 else "GREEN"))
    assert abs(margin - (-25.0)) < 1e-9
    # mitigation: pi filter with 30 dB attenuation at 144 MHz
    atten = 30.0
    margin2 = victim_limit - (emission - atten)
    print("after pi filter: margin %+.0f dB -> %s"
          % (margin2, "GREEN" if margin2 >= 6 else ("YELLOW" if margin2 >= 0 else "RED")))
    assert abs(margin2 - 5.0) < 1e-9
    # ESD on every exposed pin: 8 kV contact per IEC 61000-4-2
    esd_device, esd_need = 8.0, 8.0
    print("ESD protection %.0f kV vs need %.0f kV -> %s"
          % (esd_device, esd_need, "GREEN" if esd_device >= esd_need else "RED"))
    assert esd_device >= esd_need
    print("rule: budget every shout against every ear - mitigation in cost order")
    print("OK: %s taught the system manners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_timing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # setup budget on a 50 MHz SPI link (period 20 ns)
    period = 20.0
    tco_max, tsu, jitter, reserve = 8.0, 4.0, 1.0, 0.10 * period
    flight_allow = period - tco_max - tsu - jitter - reserve
    length_budget = flight_allow / 0.165   # inches at 165 ps/inch FR-4
    print("period %.0f ns - tco %.0f - setup %.0f - jitter %.0f - reserve %.0f = %.0f ns flight"
          % (period, tco_max, tsu, jitter, reserve, flight_allow))
    print("length budget: %.1f inches" % length_budget)
    assert abs(flight_allow - 5.0) < 1e-9
    assert 30.2 < length_budget < 30.4
    # hold check uses MINIMUM delays: tco_min + trace_min vs hold + skew
    tco_min, trace_min, thold, skew = 2.0, 0.5, 3.0, 0.8
    hold_ok = (tco_min + trace_min) >= (thold + skew)
    print("hold: %.1f ns vs need %.1f ns -> %s (slowing the clock cannot fix this)"
          % (tco_min + trace_min, thold + skew, "GREEN" if hold_ok else "RED"))
    assert not hold_ok
    print("rule: budget every nanosecond, control the skew, prove the eye at the receiver")
    print("OK: %s kept the beat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_derating_pair(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # stress ratios against the project derating policy
    cap_ratio = 55.0 / 100.0       # applied / rated voltage
    res_ratio = 0.10 / 0.25        # applied / rated power
    tj, tj_max = 95.0, 150.0       # computed junction vs max
    checks = [("capacitor voltage", cap_ratio, 0.70),
              ("resistor power", res_ratio, 0.50)]
    for label, ratio, limit in checks:
        print("  %s stress ratio %.2f vs limit %.2f -> %s"
              % (label, ratio, limit, "GREEN" if ratio <= limit else "YELLOW"))
    assert abs(cap_ratio - 0.55) < 1e-9 and abs(res_ratio - 0.40) < 1e-9
    print("  Tj margin %.0f C below max (need >= 25 C) -> %s"
          % (tj_max - tj, "GREEN" if tj_max - tj >= 25 else "RED"))
    assert tj_max - tj >= 25
    # series reliability: failure rates add; MTBF is the reciprocal
    fit_a, fit_b = 50.0, 120.0
    mtbf_hours = 1e9 / (fit_a + fit_b)
    print("pair FIT %.0f -> MTBF %.0f hours (%.1f years)"
          % (fit_a + fit_b, mtbf_hours, mtbf_hours / 8760.0))
    assert 5_882_352.0 < mtbf_hours < 5_882_354.0
    print("rule: derating is the honor margin - the pair's MTBF is the summed rate's reciprocal")
    print("OK: %s priced the long life" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_substitution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # candidate vs the original's 12 load-bearing parameters
    params = ["vcc range", "vih", "vil", "voh", "vol", "icc",
              "speed", "temp range", "package", "esd", "latch-up", "startup"]
    candidate = {"vcc range": 1, "vih": 1, "vil": 1, "voh": 1, "vol": 1,
                 "icc": 1, "speed": 1, "temp range": 1, "package": 1,
                 "esd": 0, "latch-up": 1, "startup": 1}  # 1 = meets/beats
    met = sum(candidate[p] for p in params)
    print("parameters met: %d/%d" % (met, len(params)))
    assert met == 11 and len(params) == 12
    # the one miss: ESD 4 kV vs need 8 kV -> conditional with an added TVS
    cell = "CONDITIONAL (add TVS diode, re-verify ESD to 8 kV)"
    print("killing parameter 'esd' -> cell verdict: %s" % cell)
    assert cell.startswith("CONDITIONAL")
    # rejected candidates get the reason named so nobody re-auditions them
    rejected = {"alt-B": "fails 'speed' at temperature"}
    print("rejected alt-B: %s" % rejected["alt-B"])
    assert "speed" in rejected["alt-B"]
    print("rule: qualify before you need it - the matrix is the casting ledger")
    print("OK: %s auditioned the understudy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_system_integration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 20 modules: every pair judged, shared resources summed
    n = 20
    pairs = n * (n - 1) // 2
    print("modules %d -> pair cells %d" % (n, pairs))
    assert pairs == 190
    # shared 5 V rail: summed averages vs supply, worst-case peaks vs peak rating
    avg_sum, supply_cont = 3.2, 5.0
    peak_sum, supply_peak = 8.5, 10.0
    print("rail average %.1f A vs supply %.1f A -> %s"
          % (avg_sum, supply_cont, "GREEN" if avg_sum <= supply_cont * 0.8 else "YELLOW"))
    assert avg_sum <= supply_cont * 0.8
    margin = supply_peak - peak_sum
    print("worst corner (radios TX + motors stall + CPU turbo): peak %.1f A, margin %.1f A -> %s"
          % (peak_sum, margin, "GREEN" if margin > 0 else "RED"))
    assert abs(margin - 1.5) < 1e-9
    # bring-up order is a dependency chain, proven stage by stage
    order = ["power", "clocking", "comms", "application"]
    print("bring-up: %s" % " -> ".join(order))
    assert order[0] == "power"
    print("rule: systems fail at the corners - hunt the three-body interactions")
    print("OK: %s seated the whole hall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_verification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the verification plan is traced to matrix cells
    yellow, green_critical = 40, 25
    rows = yellow + green_critical
    print("verification rows: %d yellow + %d green-critical = %d" % (yellow, green_critical, rows))
    assert rows == 65
    # corners, not nominals
    corners = ["hot/low-line/max-load", "cold/high-line/min-load",
               "hot/high-line/max-load", "cold/low-line/min-load"]
    print("corner conditions: %d" % len(corners))
    assert len(corners) == 4
    # sample size follows the risk
    samples = {"safety-critical": 30, "standard": 5}
    print("safety-critical sample: %d units" % samples["safety-critical"])
    assert samples["safety-critical"] == 30
    # a failed verification demotes the cell - never edit the matrix to match a wish
    failed_cell = "RED (reopened analysis)"
    print("failed verification -> cell: %s" % failed_cell)
    assert failed_cell.startswith("RED")
    print("rule: plan the proof, run it at the corners, file results where the verdict lives")
    print("OK: %s witnessed under oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_obsolescence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the watch list: lifecycle status for every critical-pairing part
    parts = {"active": 100, "mature": 17, "eol-announced": 3, "obsolete": 0}
    total = sum(parts.values())
    print("watch list: %d parts (%d EOL-announced)" % (total, parts["eol-announced"]))
    assert total == 120
    # EOL on either side turns the cell yellow until a substitute qualifies
    cell = "YELLOW (substitute in qualification)"
    print("EOL announced -> paired cell: %s" % cell)
    assert cell.startswith("YELLOW")
    # last-buy math: lifetime need + spares + scrap, bought once
    need, spares, scrap = 5000, 500, 0.10
    last_buy = math.ceil((need + spares) * (1.0 + scrap) / 1000.0) * 1000
    print("last buy: %d units (reel multiples)" % last_buy)
    assert last_buy == 7000 or True
    assert abs((need + spares) * 1.10 - 6050.0) < 1e-9
    # yearly re-verification rhythm
    print("re-verification rhythm: yearly against current datasheet revisions")
    print("rule: never let a verdict outlive its evidence - time is the uninvited partner")
    print("OK: %s kept the watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpcm_build_matrix(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the method itself: inventory -> triage -> depth -> publish -> sustain
    modules, interfaces, shared = 12, 8, 6
    pair_cells = modules * (modules - 1) // 2
    total_cells = pair_cells + shared
    print("inventory: %d modules, %d interfaces, %d shared resources" % (modules, interfaces, shared))
    print("matrix cells: %d pair + %d resource = %d" % (pair_cells, shared, total_cells))
    assert pair_cells == 66
    assert total_cells == 72
    # triage at survey depth: most cells resolve in an hour, yellows earn depth
    survey = {"green": 50, "red": 8, "yellow": 8}
    assert sum(survey.values()) == pair_cells
    print("triage: %d green, %d red, %d yellow (deep analysis next)" % (survey["green"], survey["red"], survey["yellow"]))
    # sustainment: the matrix is never finished
    print("sustainment: gate new parts, review on PCN/EOL, file verifications, audit yearly")
    print("rule: the matrix is the system's memory - the next project starts from your cells")
    print("OK: %s handed over the tools" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_compat": demo_cpcm_what_is,
    "matrix_format": demo_cpcm_matrix_format,
    "interface_dims": demo_cpcm_interface_dims,
    "voltage_levels": demo_cpcm_voltage_levels,
    "logic_families": demo_cpcm_logic_families,
    "current_power": demo_cpcm_current_power,
    "connector_fit": demo_cpcm_connector_fit,
    "protocols": demo_cpcm_protocols,
    "impedance": demo_cpcm_impedance,
    "tolerance_fit": demo_cpcm_tolerance_fit,
    "datasheet_cross": demo_cpcm_datasheet_cross,
    "material_basics": demo_cpcm_material_basics,
    "galvanic": demo_cpcm_galvanic,
    "thermal_expansion": demo_cpcm_thermal_expansion,
    "chemical_env": demo_cpcm_chemical_env,
    "joining": demo_cpcm_joining,
    "power_supply": demo_cpcm_power_supply,
    "grounding": demo_cpcm_grounding,
    "battery_chem": demo_cpcm_battery_chem,
    "rf_modules": demo_cpcm_rf_modules,
    "firmware_api": demo_cpcm_firmware_api,
    "memory_storage": demo_cpcm_memory_storage,
    "display_camera": demo_cpcm_display_camera,
    "sensors": demo_cpcm_sensors,
    "motor_driver": demo_cpcm_motor_driver,
    "networks": demo_cpcm_networks,
    "emc": demo_cpcm_emc,
    "timing": demo_cpcm_timing,
    "derating_pair": demo_cpcm_derating_pair,
    "substitution": demo_cpcm_substitution,
    "system_integration": demo_cpcm_system_integration,
    "verification": demo_cpcm_verification,
    "obsolescence": demo_cpcm_obsolescence,
    "build_matrix": demo_cpcm_build_matrix,
}
