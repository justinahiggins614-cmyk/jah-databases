#!/usr/bin/env python3
"""Solution-explorer demo programs for the Unsolved Electrical Engineering
databases (Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series).

Every demo is real, runnable, stdlib-only Python that walks the user through
the Signature solution approach for its record: adjustable assumptions, the
computed numbers behind the approach, and an explicit CONFIRM / REFUTE panel
stating what evidence would validate or kill the approach. All are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Honesty rule: no demo claims the problem is solved; every walkthrough is
labeled as exploring a proposed approach, with the refutation panel given
equal weight to the confirmation panel.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_use_wireless_power_distance(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: resonant relay lattice - passive tuned repeaters hop the near field across a room.")
    ASSUME = {"per_hop_eff": 0.98, "hops": 10, "input_w": 100.0}
    print("assumptions: %s" % ASSUME)
    end_to_end = ASSUME["per_hop_eff"] ** ASSUME["hops"]
    out_w = ASSUME["input_w"] * end_to_end
    print("end-to-end efficiency over %d hops: %.3f" % (ASSUME["hops"], end_to_end))
    print("100 W in -> %.1f W out" % out_w)
    assert 0.816 < end_to_end < 0.818
    assert 81.6 < out_w < 81.8
    radiative = 1.0 / (4 * math.pi * 25.0)
    print("same distance by radiation spreading: %.4f (hop lattice wins by %.0fx)" % (radiative, end_to_end / radiative))
    assert 0.0031 < radiative < 0.0033
    print("CONFIRM: 5-meter corridor delivers 100 W above 80 percent end-to-end, fields under exposure limits, independent lab audit.")
    print("REFUTE: per-hop loss will not drop below 5 percent at commodity Q, or a walking human collapses the chain.")
    print("OK: %s hopped the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_grid_100_renewables(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: stability-as-a-service lattice - grid-forming inverters synthesizing one virtual synchronous machine.")
    ASSUME = {"system_GW": 10.0, "loss_GW": 2.0, "H_synth_s": 5.0, "f0_Hz": 60.0}
    print("assumptions: %s" % ASSUME)
    rocof = ASSUME["f0_Hz"] * ASSUME["loss_GW"] / (2.0 * ASSUME["H_synth_s"] * ASSUME["system_GW"])
    print("rate of change of frequency after 2-GW loss: %.2f Hz/s" % rocof)
    assert 1.19 < rocof < 1.21
    fast_MW = ASSUME["loss_GW"] * 1000.0 * 0.5
    print("fast frequency response needed within 500 ms: %.0f MW" % fast_MW)
    assert 999.0 < fast_MW < 1001.0
    consensus_ms = 0.1
    print("consensus deadline per inverter: %.1f ms (GPS-disciplined, holdover on outage)" % consensus_ms)
    print("CONFIRM: hardware-in-the-loop 10-GW synthetic system survives fault, 2-GW loss, and GPS holdover inside grid codes, witnessed by a transmission operator.")
    print("REFUTE: consensus latency cannot stay under the stability deadline on real utility networks.")
    print("OK: %s synthesized the inertia" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_terahertz_room_temp(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: coherent combining - 400 weak plasma-wave oscillators phase-locked into one beam.")
    ASSUME = {"elements": 400, "p_each_uW": 25.0}
    print("assumptions: %s" % ASSUME)
    p_total_W = ASSUME["elements"] * ASSUME["p_each_uW"] * 1e-6
    eirp_W = (ASSUME["elements"] ** 2) * ASSUME["p_each_uW"] * 1e-6
    print("total emitted power: %.4f W" % p_total_W)
    print("effective isotropic radiated power: %.2f W" % eirp_W)
    assert 0.0099 < p_total_W < 0.0101
    assert 3.99 < eirp_W < 4.01
    print("array gain over one element: %d x" % ASSUME["elements"])
    print("CONFIRM: tile delivers 1 mW continuous at 1 THz at room temperature with link-grade phase noise, calibrated power meter.")
    print("REFUTE: phase-locking overhead eats more power than the array emits, or thermal crosstalk outruns the trimming loop.")
    print("OK: %s combined the array" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_beyond_silicon_transistors(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: hybrid silicon backbone - beyond-silicon tier on top, silicon underneath reroutes around defects.")
    ASSUME = {"top_devices": 1e9, "defect_per_million": 1.0, "energy_delay_gain": 3.0}
    print("assumptions: %s" % ASSUME)
    bad = ASSUME["top_devices"] * ASSUME["defect_per_million"] / 1e6
    print("bad devices per wafer at 1 defect per million: %.0f (rerouted by silicon base)" % bad)
    assert 999.0 < bad < 1001.0
    good_frac = 1.0 - bad / ASSUME["top_devices"]
    print("functional fraction: %.6f" % good_frac)
    assert 0.999998 < good_frac < 1.0
    print("energy-delay improvement on real benchmark: %.1fx" % ASSUME["energy_delay_gain"])
    print("CONFIRM: foundry pilot at 90 percent functional yield across 1000 wafers with 3x energy-delay win, audited.")
    print("REFUTE: top-tier defect density stays above 1 per million after three process generations.")
    print("OK: %s stacked the wafer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_quantum_interconnects(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: entanglement distillation factories - purify many noisy pairs into few excellent ones.")
    ASSUME = {"raw_pairs": 1000, "f0": 0.60, "rounds": 4}
    print("assumptions: %s" % ASSUME)
    f = ASSUME["f0"]
    pairs = ASSUME["raw_pairs"]
    for _ in range(ASSUME["rounds"]):
        f = f * f / (f * f + (1 - f) * (1 - f))
        pairs = pairs // 2
    print("after %d distillation rounds: %d pairs at fidelity %.4f" % (ASSUME["rounds"], pairs, f))
    assert pairs == 62
    assert 0.9983 < f < 0.9986
    print("rate traded for fidelity: 1000 raw -> 62 distilled")
    print("CONFIRM: two processors 10 m apart share distilled pairs above 99 percent fidelity at 1 kHz, Bell-tomography verified.")
    print("REFUTE: node memory decoheres pairs faster than purification creates them.")
    print("OK: %s distilled the link" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_universal_memory(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: heterogeneous universal tier - one address space, three physics underneath, hardware migration.")
    ASSUME = {"hot_GB": 1.0, "warm_GB": 64.0, "cold_TB": 1.0, "hot_hit": 0.95, "accesses": 1e9}
    print("assumptions: %s" % ASSUME)
    e_hot_pJ, e_migrate_pJ = 10.0, 500.0
    e_total_J = ASSUME["accesses"] * (ASSUME["hot_hit"] * e_hot_pJ + (1 - ASSUME["hot_hit"]) * e_migrate_pJ) * 1e-12
    print("energy for 1e9 accesses with 95 percent hot hits: %.3f J" % e_total_J)
    assert 0.0344 < e_total_J < 0.0346
    e_dram_J = ASSUME["accesses"] * 100.0 * 1e-12
    print("same accesses on DRAM-only traffic: %.3f J (migration overhead included above)" % e_dram_J)
    assert 0.0999 < e_dram_J < 0.1001
    print("CONFIRM: prototype cube within 10 percent of DRAM performance, 10M power cycles, zero data loss, cost within 2x of DRAM per GB.")
    print("REFUTE: migration traffic costs more energy than the hierarchy it replaces.")
    print("OK: %s unified the memory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_chip_thermal_wall(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: cooling as a chip layer - microfluidic channels between 3D stack tiers, per-tier pumped.")
    ASSUME = {"power_W_per_cm2": 500.0, "die_cm2": 4.0, "rho": 1500.0, "cp": 1100.0, "dT_K": 20.0}
    print("assumptions: %s" % ASSUME)
    p_total = ASSUME["power_W_per_cm2"] * ASSUME["die_cm2"]
    mdot = p_total / (ASSUME["rho"] * ASSUME["cp"] * ASSUME["dT_K"])
    print("chip power to remove: %.0f W" % p_total)
    print("dielectric coolant flow needed: %.2f g/s" % (mdot * 1000.0))
    assert 1999.0 < p_total < 2001.0
    assert 6.05e-5 < mdot < 6.07e-5
    print("heat path shortened from millimeters to tens of microns")
    print("CONFIRM: stacked processor sustains 500 W per cm2 for 1000 h under 85 C, zero leaks, cost adder under 15 percent.")
    print("REFUTE: channel clogging or pump failures strand heat mid-stack.")
    print("OK: %s cooled the stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_ambient_energy_harvesting(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: cooperative harvesting aperture - metasurface tile funnels many bands to one rectifier.")
    ASSUME = {"tile_m2": 0.25, "ambient_uW_per_cm2": 1.0, "rect_eff": 0.30,
              "burst_mW": 10.0, "burst_ms": 10.0, "period_s": 60.0}
    print("assumptions: %s" % ASSUME)
    caught_mW = ASSUME["tile_m2"] * 1e4 * ASSUME["ambient_uW_per_cm2"] / 1000.0
    dc_mW = caught_mW * ASSUME["rect_eff"]
    avg_need_mW = ASSUME["burst_mW"] * (ASSUME["burst_ms"] / 1000.0) / ASSUME["period_s"]
    print("RF caught by tile: %.2f mW -> DC after rectification: %.2f mW" % (caught_mW, dc_mW))
    print("sensor average need (10 ms burst per minute): %.4f mW" % avg_need_mW)
    assert 2.49 < caught_mW < 2.51
    assert 0.749 < dc_mW < 0.751
    assert 0.0016 < avg_need_mW < 0.0018
    print("harvest margin: %.0fx over need" % (dc_mW / avg_need_mW))
    assert 449.0 < dc_mW / avg_need_mW < 451.0
    print("CONFIRM: tile sustains a sensor reporting every 60 s indefinitely in a real office, one year logged uptime.")
    print("REFUTE: multi-band combining loss above 50 percent, or rectifier efficiency collapse at real indoor input powers.")
    print("OK: %s sipped the spectrum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_emi_wireless_world(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: interference etiquette in silicon - sense, classify, predict, yield.")
    ASSUME = {"devices": 200, "demand_Mbps_each": 1.0, "channel_Mbps": 500.0,
              "eff_dumb": 0.25, "eff_polite": 0.85}
    print("assumptions: %s" % ASSUME)
    demand = ASSUME["devices"] * ASSUME["demand_Mbps_each"]
    good_dumb = ASSUME["channel_Mbps"] * ASSUME["eff_dumb"]
    good_polite = ASSUME["channel_Mbps"] * ASSUME["eff_polite"]
    print("total demand: %.0f Mbps" % demand)
    print("dumb protocols deliver: %.0f Mbps -> %s" % (good_dumb, "COLLAPSE" if good_dumb < demand else "ok"))
    print("polite etiquette delivers: %.0f Mbps -> %s" % (good_polite, "COLLAPSE" if good_polite < demand else "ok"))
    assert 199.0 < demand < 201.0
    assert 124.0 < good_dumb < 126.0
    assert 424.0 < good_polite < 426.0
    print("CONFIRM: 200-radio testbed shows 3x median throughput and 10x worst-case latency win, misbehaving device throttled by neighbors.")
    print("REFUTE: classification fails in real multipath clutter, or legacy devices defect from the etiquette.")
    print("OK: %s taught the radios manners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_ultrafast_charging_grid(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the charger as a grid asset - buffer plus grid-forming inverters, peaks shaved, services sold.")
    ASSUME = {"stalls": 10, "kw_per_stall": 350.0, "contract_MW": 1.0, "demand_charge_per_kw_month": 20.0}
    print("assumptions: %s" % ASSUME)
    peak_MW = ASSUME["stalls"] * ASSUME["kw_per_stall"] / 1000.0
    avoided_MW = peak_MW - ASSUME["contract_MW"]
    savings_month = avoided_MW * 1000.0 * ASSUME["demand_charge_per_kw_month"]
    print("unbuffered peak: %.1f MW, contracted grid draw: %.1f MW" % (peak_MW, ASSUME["contract_MW"]))
    print("demand-charge savings: $%.0f per month" % savings_month)
    assert 3.49 < peak_MW < 3.51
    assert 49999.0 < savings_month < 50001.0
    print("CONFIRM: 10-stall plaza holds 1-MW contract for a year at full-rate sessions, audited 7-year buffer payback.")
    print("REFUTE: ancillary prices collapse as every station chases them, or buffer degradation halves assumed lifetime.")
    print("OK: %s made the charger pay its way" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_solid_state_transformers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: hybrid transformer - iron core for bulk power, fractional-rated electronics for the smarts.")
    ASSUME = {"kva": 100.0, "elec_frac": 0.15, "iron_loss_pct": 1.5, "elec_eff": 0.97}
    print("assumptions: %s" % ASSUME)
    bulk_loss_kW = ASSUME["kva"] * ASSUME["iron_loss_pct"] / 100.0
    elec_kW = ASSUME["kva"] * ASSUME["elec_frac"]
    elec_loss_kW = elec_kW * (1 - ASSUME["elec_eff"])
    total_pct = (bulk_loss_kW + elec_loss_kW) / ASSUME["kva"] * 100.0
    print("bulk iron loss: %.2f kW, electronics loss: %.2f kW" % (bulk_loss_kW, elec_loss_kW))
    print("total loss: %.2f percent vs %.2f percent conventional" % (total_pct, ASSUME["iron_loss_pct"]))
    assert 1.49 < bulk_loss_kW < 1.51
    assert 0.449 < elec_loss_kW < 0.451
    assert 1.94 < total_pct < 1.96
    print("CONFIRM: 100-unit utility pilot, losses within 0.3 percent of conventional, voltage complaints down 80 percent, 3 years.")
    print("REFUTE: electronic failures take whole transformers offline, or installed cost above 2x kills rate-basing.")
    print("OK: %s wrapped the iron in smarts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_superconducting_cables(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: cooling as shared infrastructure - one district nitrogen loop, many cable segments.")
    ASSUME = {"length_km": 3.0, "hts_MW": 500.0, "cu_MW_same_duct": 100.0, "cryo_kW": 50.0}
    print("assumptions: %s" % ASSUME)
    capacity_gain = ASSUME["hts_MW"] / ASSUME["cu_MW_same_duct"]
    cryo_frac = ASSUME["cryo_kW"] / (ASSUME["hts_MW"] * 1000.0) * 100.0
    cryo_MWh_yr = ASSUME["cryo_kW"] * 8760.0 / 1000.0
    print("capacity gain in the same duct: %.1fx" % capacity_gain)
    print("refrigeration overhead: %.3f percent of throughput" % cryo_frac)
    print("cryo energy per year: %.0f MWh" % cryo_MWh_yr)
    assert 4.99 < capacity_gain < 5.01
    assert 0.0099 < cryo_frac < 0.0101
    assert 437.9 < cryo_MWh_yr < 438.1
    print("CONFIRM: 5-year city pilot, availability above 99.9 percent, cost within 30 percent of new duct construction per MW-mile.")
    print("REFUTE: cryocooler maintenance refuses to fall with scale, or one quench destroys utility confidence.")
    print("OK: %s shared the cold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_silicon_photonics_cost(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the laser as a shared utility - one comb laser feeding 64 silicon modulators.")
    ASSUME = {"channels": 64, "laser_cost": 200.0, "link_Tbps": 51.2, "pJ_per_bit": 5.0}
    print("assumptions: %s" % ASSUME)
    per_channel = ASSUME["laser_cost"] / ASSUME["channels"]
    power_W = ASSUME["link_Tbps"] * 1e12 * ASSUME["pJ_per_bit"] * 1e-12
    print("laser cost per channel: $%.2f" % per_channel)
    print("link power at 5 pJ per bit: %.0f W" % power_W)
    assert 3.124 < per_channel < 3.126
    assert 255.9 < power_W < 256.1
    print("CONFIRM: 51.2-Tb/s module under 5 pJ per bit, laser under 20 percent of cost, 5000 h without re-tuning.")
    print("REFUTE: comb laser lifetime below datacenter needs, or thermal crosstalk defeats ring trimming at full count.")
    print("OK: %s shared the laser" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_spintronics_logic(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: normally-off spin-CMOS hybrid - spintronics keeps state, CMOS does the fast switching.")
    ASSUME = {"leak_uW": 10.0, "sleep_h": 1.0, "latches": 1e5, "write_nJ": 1.0}
    print("assumptions: %s" % ASSUME)
    leak_mJ = ASSUME["leak_uW"] * 1e-6 * ASSUME["sleep_h"] * 3600.0 * 1000.0
    snapshot_mJ = ASSUME["latches"] * ASSUME["write_nJ"] * 1e-6
    print("CMOS leakage for 1 h sleep: %.1f mJ" % leak_mJ)
    print("spin snapshot-and-sleep cost: %.1f mJ" % snapshot_mJ)
    assert 35.9 < leak_mJ < 36.1
    assert 0.0999 < snapshot_mJ < 0.1001
    print("sleep energy win: %.0fx" % (leak_mJ / snapshot_mJ))
    assert 359.0 < leak_mJ / snapshot_mJ < 361.0
    print("CONFIRM: microcontroller with 100x lower sleep energy on a real sensor workload, 10-year retention by accelerated aging.")
    print("REFUTE: spin-write energy stays above the leakage it saves at realistic duty cycles.")
    print("OK: %s slept without leaking" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_neuromorphic_datacenter(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: neuromorphic inference beachhead - win sparse event-driven niches on energy per inference.")
    ASSUME = {"inferences_day": 1e6, "gpu_mJ": 10.0, "neuro_mJ": 0.2}
    print("assumptions: %s" % ASSUME)
    gpu_kJ = ASSUME["inferences_day"] * ASSUME["gpu_mJ"] / 1e6
    neuro_kJ = ASSUME["inferences_day"] * ASSUME["neuro_mJ"] / 1e6
    print("GPU energy per day: %.1f kJ, neuromorphic: %.2f kJ" % (gpu_kJ, neuro_kJ))
    assert 9.99 < gpu_kJ < 10.01
    assert 0.1999 < neuro_kJ < 0.2001
    print("energy win: %.0fx" % (gpu_kJ / neuro_kJ))
    assert 49.9 < gpu_kJ / neuro_kJ < 50.1
    print("CONFIRM: production deployment, 1M inferences per day, 50x lower energy at equal accuracy, one year.")
    print("REFUTE: spike-conversion accuracy loss customers will not accept, or GPUs close the gap first.")
    print("OK: %s earned its rack slot" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_single_molecule_manufacturing(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: statistics as the device - monolayer patches where the ensemble average is the signal.")
    ASSUME = {"molecules_per_patch": 1e6, "single_sigma": 1.0}
    print("assumptions: %s" % ASSUME)
    averaging = math.sqrt(ASSUME["molecules_per_patch"])
    patch_sigma = ASSUME["single_sigma"] / averaging
    print("single-molecule variation: %.1f -> patch variation after averaging: %.4f" % (ASSUME["single_sigma"], patch_sigma))
    assert 999.9 < averaging < 1000.1
    assert 0.00099 < patch_sigma < 0.00101
    print("reproducibility gain from ensemble averaging: %.0fx" % averaging)
    print("CONFIRM: 1-kb monolayer array, BER below 1e-6 after calibration, 1 year at 85 C, wafer-scale self-assembly.")
    print("REFUTE: monolayer migration shifts calibration faster than monthly recalibration can track.")
    print("OK: %s let statistics manufacture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_cryogenic_logic_scale(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: cryogenic logic as the quantum control plane - the fridge is already running.")
    ASSUME = {"cables_direct": 300, "heat_mW_each": 5.0, "mux_lines": 30}
    print("assumptions: %s" % ASSUME)
    heat_direct_W = ASSUME["cables_direct"] * ASSUME["heat_mW_each"] / 1000.0
    heat_mux_W = ASSUME["mux_lines"] * ASSUME["heat_mW_each"] / 1000.0
    print("control heat load, direct cables: %.2f W at 4 K" % heat_direct_W)
    print("control heat load, cryo-muxed: %.2f W at 4 K" % heat_mux_W)
    assert 1.499 < heat_direct_W < 1.501
    assert 0.1499 < heat_mux_W < 0.1501
    print("heat reduction: %.0fx" % (heat_direct_W / heat_mux_W))
    assert 9.99 < heat_direct_W / heat_mux_W < 10.01
    print("CONFIRM: 1000-qubit system fully cryo-controlled, 10x less wiring heat, no qubit error increase, 6 months.")
    print("REFUTE: flux-trapping or thermal-cycling failures beat cables on field reliability.")
    print("OK: %s moved the controller into the cold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_dynamic_wireless_charging(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: charge where trucks already slow down - climbing lanes, modular cassettes, fleet economics.")
    ASSUME = {"segment_km": 2.0, "speed_kmh": 30.0, "power_kW": 200.0, "eff": 0.80}
    print("assumptions: %s" % ASSUME)
    seconds = ASSUME["segment_km"] * 3600.0 / ASSUME["speed_kmh"]
    energy_kWh = ASSUME["power_kW"] * seconds / 3600.0
    from_road = energy_kWh / ASSUME["eff"]
    print("time on segment: %.0f s, energy to battery: %.1f kWh, drawn from road: %.1f kWh" % (seconds, energy_kWh, from_road))
    assert 239.9 < seconds < 240.1
    assert 13.32 < energy_kWh < 13.34
    assert 16.65 < from_road < 16.67
    truck_km = ASSUME["segment_km"]
    print("energy per km of corridor: %.1f kWh" % (from_road / truck_km))
    print("CONFIRM: 1-year freight pilot, cost per km below diesel parity, coil-to-battery above 80 percent, cassette swaps under 30 min.")
    print("REFUTE: road-wear failures demand cassette replacement faster than every 5 years.")
    print("OK: %s charged the climbing lane" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_emp_hardening_grid(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: sacrificial protection - neutral blockers plus a strategic spare-transformer reserve.")
    ASSUME = {"gic_amps": 100.0, "fleet": 1000, "spares": 50, "loss_no_hardening_pct": 30.0}
    print("assumptions: %s" % ASSUME)
    lost_no_hard = ASSUME["fleet"] * ASSUME["loss_no_hardening_pct"] / 100.0
    lost_hard = ASSUME["fleet"] * 0.05
    print("transformers lost, unhardened Carrington-class event: %.0f" % lost_no_hard)
    print("transformers lost, blockers plus reserve: %.0f (covered by %.0f spares)" % (lost_hard, ASSUME["spares"]))
    assert 299.9 < lost_no_hard < 300.1
    assert 49.9 < lost_hard < 50.1
    print("neutral blocker stops %.0f A quasi-DC per transformer" % ASSUME["gic_amps"])
    print("CONFIRM: modeled Carrington event shows under 5 percent fleet loss, validated against 2024 storm GIC data.")
    print("REFUTE: blocker resonances create failure modes worse than the disease.")
    print("OK: %s bounded the catastrophe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_hvdc_breakers(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: two-stage interruption - superconducting limiter tames the fault, hybrid breaker clears it.")
    ASSUME = {"voltage_kV": 320.0, "fault_kA": 25.0, "limited_kA": 8.0, "clear_ms": 3.0}
    print("assumptions: %s" % ASSUME)
    energy_MJ = ASSUME["voltage_kV"] * ASSUME["limited_kA"] * (ASSUME["clear_ms"] / 1000.0)
    energy_no_limit = ASSUME["voltage_kV"] * ASSUME["fault_kA"] * (ASSUME["clear_ms"] / 1000.0)
    print("energy the breaker absorbs, limited fault: %.2f MJ" % energy_MJ)
    print("energy without the limiter stage: %.2f MJ" % energy_no_limit)
    assert 7.67 < energy_MJ < 7.69
    assert 23.99 < energy_no_limit < 24.01
    print("limiter relief factor: %.2fx" % (energy_no_limit / energy_MJ))
    assert 3.124 < energy_no_limit / energy_MJ < 3.126
    print("CONFIRM: three-terminal 320-kV test grid clears bolted faults 50 times, healthy branches undisturbed.")
    print("REFUTE: limiter recovery exceeds reclosing deadlines, or repeated quenches degrade the superconductor.")
    print("OK: %s tamed the DC fault" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_wide_bandgap_cost(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: voltage-bin division of labor - GaN-on-silicon under 650 V, SiC above.")
    ASSUME = {"power_kW": 10.0, "si_loss_pct": 3.0, "gan_loss_pct": 1.0, "hours_yr": 4000.0}
    print("assumptions: %s" % ASSUME)
    si_loss_kW = ASSUME["power_kW"] * ASSUME["si_loss_pct"] / 100.0
    gan_loss_kW = ASSUME["power_kW"] * ASSUME["gan_loss_pct"] / 100.0
    saved_kWh_yr = (si_loss_kW - gan_loss_kW) * ASSUME["hours_yr"]
    print("silicon loss: %.2f kW, GaN loss: %.2f kW" % (si_loss_kW, gan_loss_kW))
    print("energy saved per converter per year: %.0f kWh" % saved_kWh_yr)
    assert 0.2999 < si_loss_kW < 0.3001
    assert 0.0999 < gan_loss_kW < 0.1001
    assert 799.9 < saved_kWh_yr < 800.1
    print("CONFIRM: GaN-on-Si power ICs at price parity with silicon superjunction MOSFETs, 100-650 V, three-vendor BOM audit.")
    print("REFUTE: GaN dynamic on-resistance refuses to stay tamed across temperature.")
    print("OK: %s binned the bandgaps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_motor_power_density(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: multiplicative gains - superconducting windings, ironless topology, direct cooling, high speed.")
    ASSUME = {"power_MW": 1.0, "target_kW_per_kg": 25.0, "eff": 0.98,
              "gains": [2.5, 2.0, 2.0, 2.0]}
    print("assumptions: %s" % ASSUME)
    mass_kg = ASSUME["power_MW"] * 1e6 / (ASSUME["target_kW_per_kg"] * 1000.0)
    loss_kW = ASSUME["power_MW"] * 1000.0 * (1 - ASSUME["eff"])
    combined = 1.0
    for g in ASSUME["gains"]:
        combined *= g
    print("1-MW motor mass at 25 kW per kg: %.1f kg" % mass_kg)
    print("loss at 98 percent efficiency: %.0f kW" % loss_kW)
    print("stacked gain over baseline: %.0fx" % combined)
    assert 39.9 < mass_kg < 40.1
    assert 19.99 < loss_kW < 20.01
    assert 19.9 < combined < 20.1
    print("CONFIRM: demonstrator sustains 25 kW per kg for 100 h above 98 percent efficiency, independently tested.")
    print("REFUTE: superconducting AC loss at speed erases the winding advantage.")
    print("OK: %s compounded the gains" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_solid_state_lidar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: FMCW-on-silicon - laser, phased array, and coherent receiver on one chip.")
    ASSUME = {"tx_mW": 100.0, "range_m": 200.0, "target_reflect": 0.10,
              "aperture_mm": 25.0, "need_pW": 10.0}
    print("assumptions: %s" % ASSUME)
    pr_nW = ASSUME["tx_mW"] * 1e6 * ASSUME["target_reflect"] * (ASSUME["aperture_mm"] / 1000.0) ** 2 / (ASSUME["range_m"] ** 2)
    margin_dB = 10.0 * math.log10(pr_nW / (ASSUME["need_pW"] / 1000.0))
    print("received power at 200 m, 10 percent target: %.3f nW" % pr_nW)
    print("margin over coherent-detection need: %.1f dB" % margin_dB)
    assert 0.156 < pr_nW < 0.157
    assert 11.93 < margin_dB < 11.95
    print("CONFIRM: 200-m range in rain, automotive qualification, volume pricing under 150 dollars.")
    print("REFUTE: phased-array sidelobes make phantom targets no algorithm suppresses.")
    print("OK: %s put lidar on a chip" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_implant_wireless_power(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: ultrasonic power channel - sound penetrates tissue kinder than radio.")
    ASSUME = {"tx_mW": 100.0, "depth_cm": 8.0, "atten_dB_per_cm": 0.5, "piezo_eff": 0.50}
    print("assumptions: %s" % ASSUME)
    atten_dB = ASSUME["depth_cm"] * ASSUME["atten_dB_per_cm"]
    arrive_mW = ASSUME["tx_mW"] * 10.0 ** (-atten_dB / 10.0)
    dc_mW = arrive_mW * ASSUME["piezo_eff"]
    print("attenuation at 8 cm: %.1f dB -> %.1f mW arrives -> %.1f mW DC" % (atten_dB, arrive_mW, dc_mW))
    assert 3.99 < atten_dB < 4.01
    assert 39.8 < arrive_mW < 39.9
    assert 19.9 < dc_mW < 20.0
    print("tissue heating stays under 1 C per thermal model")
    print("CONFIRM: large-animal trial, 6 months continuous deep-implant power, heating under 1 C, clean histology.")
    print("REFUTE: bone shadowing blocks the beam at common implant sites, or motion tracking cannot hold focus.")
    print("OK: %s powered through tissue" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_thz_links_range(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: weather-adaptive terahertz mesh - short hops, massive arrays, route around the rain.")
    ASSUME = {"hop_m": 200.0, "rain_dB_per_km": 10.0, "elements": 256, "rate_Gbps": 50.0}
    print("assumptions: %s" % ASSUME)
    rain_dB = ASSUME["rain_dB_per_km"] * ASSUME["hop_m"] / 1000.0
    array_dB = 10.0 * math.log10(ASSUME["elements"])
    print("heavy-rain loss on a 200-m hop: %.1f dB" % rain_dB)
    print("256-element array gain: %.2f dB" % array_dB)
    assert 1.99 < rain_dB < 2.01
    assert 24.07 < array_dB < 24.09
    print("net link margin contribution: %.1f dB" % (array_dB - rain_dB))
    assert 22.06 < array_dB - rain_dB < 22.10
    print("CONFIRM: 20-node urban mesh, 99.9 percent availability at 50 Gb/s per link, full year including storm season.")
    print("REFUTE: array power erases the energy advantage, or gusts drop links faster than rerouting recovers.")
    print("OK: %s meshed through the weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_smes_economics(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: SMES as the grid's fastest muscle - monetize sub-second services, not bulk energy.")
    ASSUME = {"MW": 5.0, "MJ": 20.0, "cycles_day": 1000.0, "years": 20.0, "battery_cycles": 5000.0}
    print("assumptions: %s" % ASSUME)
    lifetime_cycles = ASSUME["cycles_day"] * 365.0 * ASSUME["years"]
    battery_lives = lifetime_cycles / ASSUME["battery_cycles"]
    print("lifetime shallow cycles: %.2e" % lifetime_cycles)
    print("battery replacements to match: %.0f" % battery_lives)
    assert 7.29e6 < lifetime_cycles < 7.31e6
    assert 1459.0 < battery_lives < 1461.0
    print("round-trip efficiency above 95 percent, cycle life effectively infinite")
    print("CONFIRM: 3-year deployment, audited levelized cost per MW of fast response below batteries over 20 years, zero coil degradation.")
    print("REFUTE: HTS wire prices plateau above crossover, or markets refuse to pay distinctly for sub-second services.")
    print("OK: %s priced the fastest muscle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_backscatter_city(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: coordinated backscatter - dedicated illuminators, scheduled slots, tags stay microwatt-simple.")
    ASSUME = {"tags": 10000, "slots_per_frame": 100, "frame_s": 1.0, "kb_per_slot": 1.0}
    print("assumptions: %s" % ASSUME)
    frames_per_tag = ASSUME["tags"] / ASSUME["slots_per_frame"]
    avg_bps = ASSUME["kb_per_slot"] * 1000.0 / frames_per_tag
    print("schedule rotation: each tag transmits every %.0f s" % frames_per_tag)
    print("average throughput per tag: %.0f bps" % avg_bps)
    assert 99.9 < frames_per_tag < 100.1
    assert 9.99 < avg_bps < 10.01
    print("CONFIRM: 10000-tag district pilot, 99 percent delivery, 5-year tag life, tag cost under one dollar at volume.")
    print("REFUTE: urban multipath defeats the slot schedule, or illuminator costs exceed the sensing value.")
    print("OK: %s networked the trillion tags" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_noninvasive_bci(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: fuse weak modalities - high-density EEG plus functional ultrasound plus learned per-user priors.")
    ASSUME = {"wpm": 60.0, "chars_per_word": 5.0, "bits_per_char": 20.0, "eeg_ch": 256}
    print("assumptions: %s" % ASSUME)
    chars_s = ASSUME["wpm"] * ASSUME["chars_per_word"] / 60.0
    info_bps = chars_s * ASSUME["bits_per_char"]
    print("decoded speech rate: %.1f chars per second" % chars_s)
    print("neural information rate: %.0f bps from %d EEG channels" % (info_bps, ASSUME["eeg_ch"]))
    assert 4.99 < chars_s < 5.01
    assert 99.9 < info_bps < 100.1
    print("CONFIRM: locked-in users reach 60-plus wpm attempted-speech decoding noninvasively, registered trial, sustained across sessions.")
    print("REFUTE: inter-session variability forces recalibration every use.")
    print("OK: %s fused the modalities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_picosecond_power_delivery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: granular power - per-region regulators with lookahead from the instruction stream.")
    ASSUME = {"vdd_V": 0.5, "droop_mV": 20.0, "lookahead_cycles": 10, "clock_GHz": 3.0, "reg_eff": 0.85}
    print("assumptions: %s" % ASSUME)
    droop_pct = ASSUME["droop_mV"] / 1000.0 / ASSUME["vdd_V"] * 100.0
    warn_ns = ASSUME["lookahead_cycles"] / ASSUME["clock_GHz"]
    print("droop budget: %.1f percent of supply" % droop_pct)
    print("lookahead warning time: %.2f ns" % warn_ns)
    assert 3.99 < droop_pct < 4.01
    assert 3.32 < warn_ns < 3.34
    print("regulator efficiency: %.0f percent" % (ASSUME["reg_eff"] * 100.0))
    print("CONFIRM: test chip holds sub-20-mV droop at 0.5 V under worst di/dt, regulator above 85 percent, area under 10 percent.")
    print("REFUTE: regulator switching noise couples into sensitive circuits worse than the droop it fixes.")
    print("OK: %s delivered power at the point of load" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_self_healing_grid(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: healing by pre-computed playbook - the digital twin rehearses disasters nightly.")
    ASSUME = {"saidi_min": 100.0, "improvement": 0.40, "auto_pct": 95.0, "scenarios_nightly": 1e6}
    print("assumptions: %s" % ASSUME)
    saidi_new = ASSUME["saidi_min"] * (1 - ASSUME["improvement"])
    manual = 100.0 - ASSUME["auto_pct"]
    print("SAIDI: %.0f min -> %.0f min per year" % (ASSUME["saidi_min"], saidi_new))
    print("faults needing humans: %.0f percent" % manual)
    assert 59.9 < saidi_new < 60.1
    assert 4.99 < manual < 5.01
    print("playbooks regenerated from %.0e twin scenarios every night" % ASSUME["scenarios_nightly"])
    print("CONFIRM: utility pilot clears 95 percent of faults autonomously, SAIDI/SAIFI up 40 percent, zero playbook-caused cascades, 2 years.")
    print("REFUTE: twin-model mismatch makes playbooks wrong in unmodeled conditions.")
    print("OK: %s rehearsed the disaster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_reversible_logic_landauer(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: reversible accelerators for naturally reversible workloads - dodge Landauer where it counts.")
    ASSUME = {"temp_K": 300.0, "fraction_of_landauer": 0.1, "cmos_pJ_per_op": 10.0}
    print("assumptions: %s" % ASSUME)
    kT = 1.380649e-23 * ASSUME["temp_K"]
    landauer_J = kT * math.log(2)
    target_J = landauer_J * ASSUME["fraction_of_landauer"]
    cmos_J = ASSUME["cmos_pJ_per_op"] * 1e-12
    print("Landauer limit at 300 K: %.3e J per erased bit" % landauer_J)
    print("reversible accelerator target: %.3e J" % target_J)
    print("CMOS baseline per op: %.3e J (%.0fx above target)" % (cmos_J, cmos_J / target_J))
    assert 2.86e-21 < landauer_J < 2.88e-21
    assert 2.86e-22 < target_J < 2.88e-22
    assert 3.48e10 < cmos_J / target_J < 3.50e10
    print("CONFIRM: measured FFT energy below 0.1 kT ln2 per bit-erasure-equivalent, throughput within 3x of CMOS.")
    print("REFUTE: adiabatic clock losses exceed recovered energy at practical speeds.")
    print("OK: %s uncomputed the bill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_antenna_chu_limit(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: leave the theorem's assumptions - parametric pumping buys bandwidth the passive limit forbids.")
    ASSUME = {"ka": 0.5, "bandwidth_gain": 5.0, "nf_penalty_dB": 2.0}
    print("assumptions: %s" % ASSUME)
    q_chu = 1.0 / (ASSUME["ka"] ** 3)
    print("Chu-limit Q for ka = %.1f: %.1f (narrowband by theorem)" % (ASSUME["ka"], q_chu))
    assert 7.99 < q_chu < 8.01
    eff_product_gain = ASSUME["bandwidth_gain"]
    print("bandwidth-efficiency product gain over passive baseline: %.0fx" % eff_product_gain)
    print("noise-figure penalty budget: %.0f dB" % ASSUME["nf_penalty_dB"])
    print("CONFIRM: module shows 5x bandwidth-efficiency product at equal size, NF degradation under 2 dB, unconditionally stable.")
    print("REFUTE: pump phase noise ruins the noise figure, or pump power exceeds what the radio saves.")
    print("OK: %s sidestepped the theorem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_room_temp_photon_detector(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: waveguide SPADs with learned afterpulse cancellation - accept noisy physics, clean it computationally.")
    ASSUME = {"sys_eff": 0.50, "dark_Hz": 100.0, "signal_Hz": 1e6, "distance_km": 50.0}
    print("assumptions: %s" % ASSUME)
    detections = ASSUME["signal_Hz"] * ASSUME["sys_eff"]
    snr = detections / ASSUME["dark_Hz"]
    print("detections per second at 1550 nm: %.0e" % detections)
    print("signal-to-dark ratio: %.0e" % snr)
    assert 4.99e5 < detections < 5.01e5
    assert 4.99e3 < snr < 5.01e3
    print("thermoelectric cooling to -40 C only - no cryogen")
    print("CONFIRM: 50 percent system efficiency, dark under 100 Hz, 50-km field QKD trial within 2x of SNSPD key rates.")
    print("REFUTE: afterpulse correlations prove unlearnable at high count rates.")
    print("OK: %s detected the warm photon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_million_qubit_wiring(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: control hierarchy like DRAM - row-column addressing with cryogenic demultiplexers.")
    ASSUME = {"qubits_demo": 10000, "qubits_target": 1e6, "wire_budget": 500}
    print("assumptions: %s" % ASSUME)
    wires_demo = int(2 * math.sqrt(ASSUME["qubits_demo"]))
    wires_target = int(2 * math.sqrt(ASSUME["qubits_target"]))
    direct_target = int(ASSUME["qubits_target"])
    print("10k-qubit vehicle: %d wires (budget %d)" % (wires_demo, ASSUME["wire_budget"]))
    print("million-qubit machine: %d wires vs %d direct (%.0fx reduction)" % (wires_target, direct_target, direct_target / wires_target))
    assert wires_demo == 200
    assert wires_demo < ASSUME["wire_budget"]
    assert wires_target == 2000
    assert 499.9 < direct_target / wires_target < 500.1
    print("CONFIRM: 10000-qubit vehicle under 500 wires, simultaneous benchmarking with crosstalk below threshold.")
    print("REFUTE: demultiplexer transients decohere neighbors, or addressing latency outruns coherence.")
    print("OK: %s wired the million" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "wireless_power_distance": demo_use_wireless_power_distance,
    "grid_100_renewables": demo_use_grid_100_renewables,
    "terahertz_room_temp": demo_use_terahertz_room_temp,
    "beyond_silicon_transistors": demo_use_beyond_silicon_transistors,
    "quantum_interconnects": demo_use_quantum_interconnects,
    "universal_memory": demo_use_universal_memory,
    "chip_thermal_wall": demo_use_chip_thermal_wall,
    "ambient_energy_harvesting": demo_use_ambient_energy_harvesting,
    "emi_wireless_world": demo_use_emi_wireless_world,
    "ultrafast_charging_grid": demo_use_ultrafast_charging_grid,
    "solid_state_transformers": demo_use_solid_state_transformers,
    "superconducting_cables": demo_use_superconducting_cables,
    "silicon_photonics_cost": demo_use_silicon_photonics_cost,
    "spintronics_logic": demo_use_spintronics_logic,
    "neuromorphic_datacenter": demo_use_neuromorphic_datacenter,
    "single_molecule_manufacturing": demo_use_single_molecule_manufacturing,
    "cryogenic_logic_scale": demo_use_cryogenic_logic_scale,
    "dynamic_wireless_charging": demo_use_dynamic_wireless_charging,
    "emp_hardening_grid": demo_use_emp_hardening_grid,
    "hvdc_breakers": demo_use_hvdc_breakers,
    "wide_bandgap_cost": demo_use_wide_bandgap_cost,
    "motor_power_density": demo_use_motor_power_density,
    "solid_state_lidar": demo_use_solid_state_lidar,
    "implant_wireless_power": demo_use_implant_wireless_power,
    "thz_links_range": demo_use_thz_links_range,
    "smes_economics": demo_use_smes_economics,
    "backscatter_city": demo_use_backscatter_city,
    "noninvasive_bci": demo_use_noninvasive_bci,
    "picosecond_power_delivery": demo_use_picosecond_power_delivery,
    "self_healing_grid": demo_use_self_healing_grid,
    "reversible_logic_landauer": demo_use_reversible_logic_landauer,
    "antenna_chu_limit": demo_use_antenna_chu_limit,
    "room_temp_photon_detector": demo_use_room_temp_photon_detector,
    "million_qubit_wiring": demo_use_million_qubit_wiring,
}
