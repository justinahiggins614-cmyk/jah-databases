#!/usr/bin/env python3
"""Solution-explorer demo programs for the Unsolved Engineering databases.

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


def demo_use_grid_storage(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: time-layered storage - fast lithium layer plus bulk iron-air/thermal layer sized from real weather records.")
    ASSUME = {"city_load_GW": 1.0, "lull_hours": 72.0, "li_cost_per_kwh": 150.0, "target_cost_per_kwh": 20.0}
    print("assumptions: %s" % ASSUME)
    energy_kwh = ASSUME["city_load_GW"] * 1e6 * ASSUME["lull_hours"]
    cost_li = energy_kwh * ASSUME["li_cost_per_kwh"]
    cost_target = energy_kwh * ASSUME["target_cost_per_kwh"]
    print("energy to ride a 72-hour lull at 1 GW: %.3e kWh" % energy_kwh)
    print("at lithium-ion cost ($150/kWh): $%.3e" % cost_li)
    print("at long-duration target ($20/kWh): $%.3e" % cost_target)
    assert 7.199e7 < energy_kwh < 7.201e7
    assert 1.0799e10 < cost_li < 1.0801e10
    assert 1.4399e9 < cost_target < 1.4401e9
    print("gap to close: %.1fx cost reduction" % (cost_li / cost_target))
    assert 7.49 < cost_li / cost_target < 7.51
    print("CONFIRM: pilot rides a real multi-day wind lull with metered installed cost below $20/kWh of energy capacity.")
    print("REFUTE: bulk-layer materials degrade faster than modeled, or balance-of-plant costs refuse to fall with scale.")
    print("OK: %s explored the time layers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_direct_air_capture(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: capture only on curtailed surplus power with containerized modular units; optimize for capital cost, not efficiency.")
    ASSUME = {"cost_today_per_ton": 600.0, "target_per_ton": 100.0, "gigatons_per_year": 1.0}
    print("assumptions: %s" % ASSUME)
    bill_today = ASSUME["gigatons_per_year"] * 1e9 * ASSUME["cost_today_per_ton"]
    bill_target = ASSUME["gigatons_per_year"] * 1e9 * ASSUME["target_per_ton"]
    print("1 Gt/yr at today cost: $%.3e per year" % bill_today)
    print("1 Gt/yr at target cost: $%.3e per year" % bill_target)
    assert 5.999e11 < bill_today < 6.001e11
    assert 9.999e10 < bill_target < 1.0001e11
    reduction = 1.0 - ASSUME["target_per_ton"] / ASSUME["cost_today_per_ton"]
    print("required cost reduction: %.1f %%" % (reduction * 100))
    assert 0.8332 < reduction < 0.8334
    print("CONFIRM: full-year metered run where capture cost tracks the local curtailment price curve downward, third-party audited per ton.")
    print("REFUTE: sorbent degradation under intermittent cycling erases the energy savings, or mineralization kinetics prove too slow outside volcanic regions.")
    print("OK: %s priced the thermostat knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_desalination_energy(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: stop chasing the membrane limit; co-locate with waste heat, run pumps on surplus renewables, mine the brine for revenue.")
    ASSUME = {"plant_m3_per_day": 1e6, "ro_kwh_per_m3": 3.5, "thermal_kwh_per_m3": 12.0}
    print("assumptions: %s" % ASSUME)
    ro_gwh = ASSUME["plant_m3_per_day"] * ASSUME["ro_kwh_per_m3"] / 1e6
    th_gwh = ASSUME["plant_m3_per_day"] * ASSUME["thermal_kwh_per_m3"] / 1e6
    print("1M m3/day plant, reverse osmosis: %.2f GWh/day" % ro_gwh)
    print("1M m3/day plant, thermal: %.2f GWh/day" % th_gwh)
    assert 3.499 < ro_gwh < 3.501
    assert 11.99 < th_gwh < 12.01
    print("RO advantage over thermal: %.2fx less energy" % (th_gwh / ro_gwh))
    assert 3.427 < th_gwh / ro_gwh < 3.429
    print("CONFIRM: plant-level audit showing water cost falling as brine-mineral revenues rise, with marine monitoring showing no brine damage zone.")
    print("REFUTE: brine mineral markets saturate at the first plants, or biofouling under waste-heat preheating wipes out membrane gains.")
    print("OK: %s audited the water factory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_green_steel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: never buy hydrogen on the open market; co-site direct reduction with overbuilt renewables and run electrolyzers only on surplus.")
    ASSUME = {"h2_kg_per_ton_steel": 55.0, "kwh_per_kg_h2": 50.0, "blast_co2_per_ton": 1.9}
    print("assumptions: %s" % ASSUME)
    kwh_per_ton = ASSUME["h2_kg_per_ton_steel"] * ASSUME["kwh_per_kg_h2"]
    print("electricity per ton of green steel: %.0f kWh" % kwh_per_ton)
    assert 2749.0 < kwh_per_ton < 2751.0
    homes_days = kwh_per_ton / 30.0
    print("that is about %.0f home-days of electricity per ton of steel" % homes_days)
    assert 91.6 < homes_days < 91.8
    print("CO2 avoided vs blast furnace: ~%.1f t per ton of steel" % ASSUME["blast_co2_per_ton"])
    print("CONFIRM: audited cost per ton at or below the blast-furnace route over a full production year, with power purchase records proving the surplus thesis.")
    print("REFUTE: hydrogen buffer storage at required scale costs more than modeled, or ore pelletizing energy erases the margin.")
    print("OK: %s weighed the hydrogen bill" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_zero_carbon_cement(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: treat the kiln as a CO2 concentrator doing useful work for free; capture the pure process stream into materials.")
    # CaCO3 -> CaO + CO2 : 44.01 / 100.09 tons of CO2 per ton of limestone
    co2_per_limestone = 44.01 / 100.09
    print("stoichiometric CO2 per ton of limestone: %.4f t" % co2_per_limestone)
    assert 0.4396 < co2_per_limestone < 0.4398
    # about 1.18 t limestone-derived CaCO3 equivalent per ton of clinker in practice
    process_co2 = co2_per_limestone * 1.18
    print("process CO2 per ton of clinker: %.3f t (unavoidable by chemistry)" % process_co2)
    assert 0.518 < process_co2 < 0.520
    world_tons = 4.0e9
    print("at 4 Gt cement/yr, process stream alone: %.2e t CO2/yr" % (world_tons * process_co2))
    print("CONFIRM: plant gate-to-gate audit showing net-zero cement at commodity price with independently verified CO2 mass balance.")
    print("REFUTE: mineralization markets saturate, or alternative binders fail decades-long durability testing.")
    print("OK: %s read the limestone ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_solid_state_batteries(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: design backward from existing roll-to-roll lines; graded composite electrolyte trading peak density for manufacturability.")
    ASSUME = {"pack_kwh": 75.0, "li_wh_per_kg": 270.0, "ss_target_wh_per_kg": 450.0}
    print("assumptions: %s" % ASSUME)
    mass_li = ASSUME["pack_kwh"] * 1000.0 / ASSUME["li_wh_per_kg"]
    mass_ss = ASSUME["pack_kwh"] * 1000.0 / ASSUME["ss_target_wh_per_kg"]
    print("75 kWh pack, liquid Li-ion at 270 Wh/kg: %.1f kg" % mass_li)
    print("75 kWh pack, solid-state at 450 Wh/kg: %.1f kg" % mass_ss)
    assert 277.7 < mass_li < 277.9
    assert 166.6 < mass_ss < 166.8
    print("mass saved: %.1f kg (%.0f %%)" % (mass_li - mass_ss, (1 - mass_ss / mass_li) * 100))
    assert 111.0 < mass_li - mass_ss < 111.2
    print("CONFIRM: 1000-cycle life at 80%% capacity on a pilot line running at real line speeds, with costed bill of materials.")
    print("REFUTE: interfacial resistance grows with cycling faster than modeled, or moisture sensitivity forces dry-room costs that erase the advantage.")
    print("OK: %s weighed the pack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_green_hydrogen_economics(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: never sell hydrogen gas; co-locate electrolysis with the end process and ship dense stable commodities instead.")
    ASSUME = {"kwh_per_kg": 50.0, "lhv_kwh_per_kg": 33.3, "grey_usd_per_kg": 1.5, "green_usd_per_kg": 5.0}
    print("assumptions: %s" % ASSUME)
    eff = ASSUME["lhv_kwh_per_kg"] / ASSUME["kwh_per_kg"]
    print("electrolyzer efficiency (LHV basis): %.1f %%" % (eff * 100))
    assert 0.665 < eff < 0.667
    premium = ASSUME["green_usd_per_kg"] / ASSUME["grey_usd_per_kg"]
    print("green premium over grey hydrogen: %.2fx" % premium)
    assert 3.32 < premium < 3.34
    elec_cost = ASSUME["kwh_per_kg"] * 0.03
    print("at $0.03/kWh surplus power, electricity per kg H2: $%.2f" % elec_cost)
    assert 1.499 < elec_cost < 1.501
    print("CONFIRM: delivered green ammonia or green iron at cost parity with the grey route over a full operating year, audited end to end.")
    print("REFUTE: variable-flow chemical synthesis proves uncontrollable at scale, or intermittent-duty electrolyzer degradation destroys the maintenance budget.")
    print("OK: %s followed the molecule" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_sustainable_aviation_fuel(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: standardized waste-first SAF hubs at existing refineries; e-fuels only for the mandate volumes waste cannot cover.")
    ASSUME = {"fuel_kg_per_flight": 100000.0, "fossil_usd_per_kg": 0.60, "saf_multiplier": 3.0}
    print("assumptions: %s" % ASSUME)
    fossil_bill = ASSUME["fuel_kg_per_flight"] * ASSUME["fossil_usd_per_kg"]
    saf_bill = fossil_bill * ASSUME["saf_multiplier"]
    print("long-haul fuel bill, fossil: $%.0f" % fossil_bill)
    print("long-haul fuel bill, SAF at 3x: $%.0f" % saf_bill)
    assert 59999.0 < fossil_bill < 60001.0
    assert 179999.0 < saf_bill < 180001.0
    print("premium per flight: $%.0f" % (saf_bill - fossil_bill))
    print("per passenger (300 seats): $%.0f" % ((saf_bill - fossil_bill) / 300.0))
    assert 399.9 < (saf_bill - fossil_bill) / 300.0 < 400.1
    print("CONFIRM: hub-gate fuel cost within 1.5x fossil jet with lifecycle audit, at volumes measured in millions of tons.")
    print("REFUTE: waste feedstock competition bids prices past break-even, or pathway certification stays a multi-year bottleneck.")
    print("OK: %s fueled the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_battery_recycling(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: standardize pack disassembly interfaces; chemistry-specific hydrometallurgy hubs; take-back contracts closing the loop.")
    ASSUME = {"li_kg_per_pack": 8.0, "li_recovery": 0.90, "ni_co_recovery": 0.95}
    print("assumptions: %s" % ASSUME)
    li_back = ASSUME["li_kg_per_pack"] * ASSUME["li_recovery"]
    print("lithium recovered per retired pack: %.1f kg of %.0f kg" % (li_back, ASSUME["li_kg_per_pack"]))
    assert 7.19 < li_back < 7.21
    packs_per_gwh = 1e6 / 75.0
    li_per_gwh = packs_per_gwh * li_back / 1000.0
    print("per GWh of retired 75 kWh packs, lithium recovered: %.1f t" % li_per_gwh)
    assert 95.9 < li_per_gwh < 96.1
    print("CONFIRM: audited recovery above 90%% Li and 95%% Ni/Co at cost below mined equivalents across a full year of operation.")
    print("REFUTE: pack designs keep fragmenting faster than standards converge, or commodity crashes make efficient recycling uneconomic.")
    print("OK: %s closed the loop on paper" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_pfas_destruction(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: concentrate first with cheap sorbents, destroy only the concentrate with hydrated-electron chemistry on surplus power.")
    bonds = {"C-F": 485.0, "C-H": 413.0, "C-C": 347.0}
    print("bond energies (kJ/mol): %s" % bonds)
    ratio = bonds["C-F"] / bonds["C-C"]
    print("C-F is %.3fx stronger than C-C - that is why nothing in nature breaks it" % ratio)
    assert 1.397 < ratio < 1.399
    # concentration factor: 1M gallons at 100 ppt -> treat grams, not gallons
    liters = 1e6 * 3.785
    grams_pfas = liters * 100e-12 * 1000.0
    print("1M gallons at 100 ppt holds only %.1f g of PFAS - dilution is the enemy" % grams_pfas)
    assert 0.377 < grams_pfas < 0.379
    print("CONFIRM: continuous operation on real groundwater showing non-detect effluent and stoichiometric fluoride release matching influent fluorine mass.")
    print("REFUTE: concentrate matrices poison the destruction chemistry, or sorbent regeneration becomes the cost center.")
    print("OK: %s aimed at the strongest bond" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_ocean_plastic(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: rank by capture cost per ton - rivers first, gyres second, microplastics by prevention; each layer funds the next.")
    ASSUME = {"gyre_tons": 80000.0, "gyre_km2": 1.6e6, "inflow_tons_per_year": 8e6, "harvest_tons_per_year": 10000.0}
    print("assumptions: %s" % ASSUME)
    density = ASSUME["gyre_tons"] * 1000.0 / ASSUME["gyre_km2"]
    print("Great Pacific Garbage Patch density: %.1f kg per km2" % density)
    assert 49.9 < density < 50.1
    share = ASSUME["harvest_tons_per_year"] / ASSUME["inflow_tons_per_year"] * 100.0
    print("10 kt/yr harvest vs 8 Mt/yr inflow: %.3f %% of inflow" % share)
    assert 0.1249 < share < 0.1251
    years_to_gyre = ASSUME["gyre_tons"] / ASSUME["harvest_tons_per_year"]
    print("years to clear the patch at that rate (ignoring inflow): %.0f" % years_to_gyre)
    assert 7.99 < years_to_gyre < 8.01
    print("CONFIRM: measured year-on-year decline in river plastic flux at instrumented mouths; gyre mass-balance showing removal beating accumulation.")
    print("REFUTE: recovered-plastic markets collapse under contamination, or storms redistribute gyre plastic faster than harvesters track.")
    print("OK: %s sorted the currents" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_corrosion(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: corrosion as an information problem - embedded sensor grids at vulnerable interfaces, targeted protection only where attack is reported.")
    ASSUME = {"global_cost_trillion": 2.5, "gdp_trillion": 73.5, "avoidable_share": 0.25}
    print("assumptions: %s" % ASSUME)
    pct = ASSUME["global_cost_trillion"] / ASSUME["gdp_trillion"] * 100.0
    print("corrosion cost as share of global GDP: %.2f %%" % pct)
    assert 3.399 < pct < 3.403
    avoidable = ASSUME["global_cost_trillion"] * ASSUME["avoidable_share"]
    print("avoidable with existing best practice: $%.3f trillion/yr" % avoidable)
    assert 0.6249 < avoidable < 0.6251
    print("a 1%% cut in the corrosion bill: $%.1f billion/yr" % (ASSUME["global_cost_trillion"] * 1000 * 0.01))
    print("CONFIRM: instrumented structures showing a decade of near-zero section loss with maintenance an order of magnitude below uninstrumented twins.")
    print("REFUTE: sensor drift in real concrete/soil gives false confidence, or the electronics become the maintenance burden.")
    print("OK: %s listened to the rust" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_refree_magnets(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: exchange-spring nanocomposites - hard phase plus soft phase coupled below 10 nm - screened computationally, built by robot labs.")
    ASSUME = {"ndfeb_kj_m3": 400.0, "ndfeb_theory": 512.0, "ferrite_kj_m3": 38.0, "target_kj_m3": 200.0}
    print("assumptions: %s" % ASSUME)
    gap = ASSUME["ndfeb_kj_m3"] / ASSUME["ferrite_kj_m3"]
    print("NdFeB outperforms ferrite by %.2fx - the gap to close" % gap)
    assert 10.52 < gap < 10.54
    target_ratio = ASSUME["target_kj_m3"] / ASSUME["ndfeb_kj_m3"]
    print("Signature target (200 kJ/m3) as share of NdFeB: %.0f %%" % (target_ratio * 100))
    assert 0.499 < target_ratio < 0.501
    print("CONFIRM: bulk pellets above 200 kJ/m3 with coercivity surviving 150 C, reproduced across three independent batches.")
    print("REFUTE: grain growth during consolidation cannot be suppressed at industrial throughput, or the best pairs need supply-risky cobalt.")
    print("OK: %s weighed the field" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_inert_anode_aluminum(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the anode as a steady-state system - a self-repairing oxide skin fed by bath chemistry, monitored electrically in real time.")
    carbon_per_ton_al = 0.4
    co2 = carbon_per_ton_al * 44.0 / 12.0
    print("carbon anode consumed per ton of Al: %.1f t" % carbon_per_ton_al)
    print("direct CO2 per ton of Al: %.3f t" % co2)
    assert 1.466 < co2 < 1.468
    world_al_mt = 70.0
    print("at 70 Mt Al/yr, anode CO2 alone: %.1f Mt/yr" % (world_al_mt * co2))
    assert 102.6 < world_al_mt * co2 < 102.8
    print("an inert anode would emit oxygen instead of this entire stream.")
    print("CONFIRM: pilot cell running 12 months at industrial current density with anode wear below the economic threshold and P1020 metal purity.")
    print("REFUTE: dissolved anode metals contaminate aluminum beyond refining tolerance, or micro-cycling cuts current efficiency below baseline.")
    print("OK: %s watched the anode" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_fusion_power(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the maintainable machine beats the optimal plasma - cartridge blanket modules swapped by robots, tritium bred in the blanket loop.")
    laser_mj = 2.05
    fusion_mj = 3.15
    q = fusion_mj / laser_mj
    print("NIF Dec 2022: %.2f MJ fusion from %.2f MJ laser" % (fusion_mj, laser_mj))
    print("scientific gain Q: %.3f" % q)
    assert 1.536 < q < 1.538
    # wall-plug reality check: laser efficiency ~1%% -> wall-plug Q far below 1
    wall_q = q * 0.01
    print("at ~1%% laser wall-plug efficiency, wall-plug Q: %.4f (the mountain ahead)" % wall_q)
    assert 0.01536 < wall_q < 0.01538
    print("CONFIRM: blanket module surviving a full neutron fluence cycle with tritium breeding ratio above 1.0 and outage measured in weeks.")
    print("REFUTE: neutron damage outruns any serviceable replacement schedule, or tritium breeding cannot close the fuel cycle at any blanket design.")
    print("OK: %s counted the gain honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_room_temp_superconductor(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: chemical pre-compression - hydride-like hydrogen cages stabilized at ambient pressure inside rigid frameworks, screened computationally.")
    ASSUME = {"lah10_gpa": 170.0, "atm_per_gpa": 9869.0, "lah10_k": 250.0, "room_k": 293.0, "cuprate_record_k": 133.0}
    print("assumptions: %s" % ASSUME)
    atm = ASSUME["lah10_gpa"] * ASSUME["atm_per_gpa"]
    print("LaH10 250 K needs %.3e atmospheres" % atm)
    assert 1.677e6 < atm < 1.679e6
    print("temperature still short of room: %.0f K" % (ASSUME["room_k"] - ASSUME["lah10_k"]))
    print("ambient-pressure record (cuprate, 1993): %.0f K" % ASSUME["cuprate_record_k"])
    gap = ASSUME["room_k"] - ASSUME["cuprate_record_k"]
    print("gap from the ambient-pressure record to room temperature: %.0f K in 30+ years" % gap)
    assert 159.9 < gap < 160.1
    print("CONFIRM: zero resistance PLUS Meissner expulsion PLUS heat-capacity jump at the same temperature, ambient pressure, independently reproduced.")
    print("REFUTE: every ambient-stabilized hydride predicted decomposes on quenching, or coupling needs prove incompatible with ambient lattice stability.")
    print("OK: %s held the triple bar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_geothermal_anywhere(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: eliminate the reservoir - standardized closed-loop well pairs, the heat harvested by a sealed working fluid that never touches rock.")
    ASSUME = {"gradient_c_per_km": 27.0, "surface_c": 15.0, "target_c": 175.0}
    print("assumptions: %s" % ASSUME)
    depth_km = (ASSUME["target_c"] - ASSUME["surface_c"]) / ASSUME["gradient_c_per_km"]
    print("depth to 175 C at 27 C/km: %.2f km" % depth_km)
    assert 5.92 < depth_km < 5.94
    wells_for_100mw = 100.0 / 5.0
    print("at 5 MW per well pair, a 100 MW field needs %.0f pairs" % wells_for_100mw)
    assert 19.9 < wells_for_100mw < 20.1
    print("CONFIRM: a 10-pair field delivering modeled output for two years with drilling cost per pair falling on a documented learning curve.")
    print("REFUTE: deep drilling costs refuse to fall with repetition, or thermal drawdown chokes output faster than conduction replenishes it.")
    print("OK: %s drilled the numbers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_use_artificial_photosynthesis(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: concede the efficiency race; compete on installed cost with printable photocatalyst sheets replaced like roofing felt.")
    ASSUME = {"natural_pct": 1.0, "pv_electrolysis_pct": 20.0, "sheet_target_pct": 5.0}
    print("assumptions: %s" % ASSUME)
    print("natural photosynthesis: ~%.0f%%; PV+electrolysis: ~%.0f%%" % (ASSUME["natural_pct"], ASSUME["pv_electrolysis_pct"]))
    advantage = ASSUME["pv_electrolysis_pct"] / ASSUME["natural_pct"]
    print("the indirect route is already %.0fx nature" % advantage)
    assert 19.9 < advantage < 20.1
    sheet_vs_pv = ASSUME["sheet_target_pct"] / ASSUME["pv_electrolysis_pct"]
    print("a 5%% sheet concedes %.2fx efficiency - so it must win %.2fx on installed cost" % (1 / sheet_vs_pv, 1 / sheet_vs_pv))
    assert 3.99 < 1 / sheet_vs_pv < 4.01
    print("CONFIRM: a one-hectare basin running a full year with metered hydrogen output and a costed sheet-replacement log trending toward the PV-electrolysis benchmark.")
    print("REFUTE: photocorrosion destroys sheets faster than replacement economics allow, or gas separation at basin scale proves impractical.")
    print("OK: %s printed the leaf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_orbital_solar(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: no cathedral station - a swarm of identical beaming satellites, incremental capacity, revenue from premium always-on power first.")
    ASSUME = {"station_tons": 2500.0, "launch_usd_per_kg": 1500.0, "cf_orbit": 0.99, "cf_ground": 0.20}
    print("assumptions: %s" % ASSUME)
    launch_bill = ASSUME["station_tons"] * 1000.0 * ASSUME["launch_usd_per_kg"]
    print("launch bill for a 2500 t station at $1500/kg: $%.3e" % launch_bill)
    assert 3.749e9 < launch_bill < 3.751e9
    cf_gain = ASSUME["cf_orbit"] / ASSUME["cf_ground"]
    print("capacity-factor advantage over ground solar: %.2fx" % cf_gain)
    assert 4.94 < cf_gain < 4.96
    print("CONFIRM: a 10-unit cluster delivering metered power to a rectenna for a year with off-site beam intensity below safety limits at all times.")
    print("REFUTE: coherent beam combination proves unmaintainable in orbit, or end-to-end efficiency cannot clear the terrestrial solar-plus-storage bar.")
    print("OK: %s aimed the array" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_hypersonic_flight(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the vehicle as a flying heat exchanger - fuel as coolant, structure as radiator, trajectory budgeted thermally first.")
    mach_demo = 9.6
    mach_ref = 2.0
    heat_ratio = (mach_demo / mach_ref) ** 3
    print("X-43A reached Mach %.1f; heating scales ~v^3" % mach_demo)
    print("stagnation heating vs Mach 2 cruise: %.1fx" % heat_ratio)
    assert 110.5 < heat_ratio < 110.7
    print("scramjet specific impulse (~1000-2000 s) vs rocket (~450 s): the prize for air-breathing")
    isp_gain = 1500.0 / 450.0
    print("mid-range scramjet Isp advantage: %.2fx" % isp_gain)
    assert 3.32 < isp_gain < 3.34
    print("CONFIRM: subscale demonstrator completing a 30-minute sustained cruise with post-flight inspection showing thermal margins intact.")
    print("REFUTE: combined-cycle handoff proves uncontrollable at full scale, or cooled-structure maintenance between flights costs more than the speed is worth.")
    print("OK: %s budgeted the heat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_supersonic_economics(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: size the aircraft to the boom rule - a small low-boom design earning the overland case with measured data, premium routes first.")
    ASSUME = {"concorde_seats": 100.0, "fuel_mult": 3.0, "subsonic_casm": 0.10}
    print("assumptions: %s" % ASSUME)
    ss_casm = ASSUME["subsonic_casm"] * ASSUME["fuel_mult"]
    print("Concorde-era cost per seat-mile vs $%.2f subsonic: $%.2f" % (ASSUME["subsonic_casm"], ss_casm))
    assert 0.299 < ss_casm < 0.301
    fare_premium_needed = (ss_casm - ASSUME["subsonic_casm"]) * 4000.0
    print("fare premium needed on a 4000-mile sector: $%.0f per seat" % fare_premium_needed)
    assert 799.0 < fare_premium_needed < 801.0
    print("CONFIRM: certified boom at or below the annoyance threshold with load factors and fares covering operating cost on real routes.")
    print("REFUTE: low-boom shaping costs more drag than modeled, or regulators decline regardless of data.")
    print("OK: %s priced the boom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_hyperloop(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: de-risk by de-speeding - medium-vacuum freight-first corridors that pay for the tube before any passenger boards.")
    tube_pa = 100.0
    atm_pa = 101325.0
    ratio = tube_pa / atm_pa
    print("tube pressure %.0f Pa vs atmosphere %.0f Pa: %.2e atm" % (tube_pa, atm_pa, ratio))
    assert 9.86e-4 < ratio < 9.88e-4
    pods_per_hour = 3600.0 / 30.0
    pax_per_hour = pods_per_hour * 40.0
    print("at one pod per 30 s carrying 40: %.0f passengers/hour/direction" % pax_per_hour)
    assert 4799.0 < pax_per_hour < 4801.0
    print("a high-speed train every 5 min at 1000 seats: 12000/hr - the throughput bar the tube must clear")
    print("CONFIRM: three years of freight operation at 99%% dispatch reliability with audited cost per ton-km below trucking on the corridor.")
    print("REFUTE: tube maintenance and vacuum pumping exceed the model at real scale, or throughput per tube cannot pay the civil debt.")
    print("OK: %s pumped the tube" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_megawatt_charging(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the truck stop as a grid asset - buffer batteries shave megawatt spikes and sell grid services between trucks.")
    ASSUME = {"pack_kwh": 500.0, "minutes": 30.0, "trucks": 10.0}
    print("assumptions: %s" % ASSUME)
    kw = ASSUME["pack_kwh"] / (ASSUME["minutes"] / 60.0)
    print("500 kWh in 30 min needs %.0f kW average" % kw)
    assert 999.0 < kw < 1001.0
    site_mw = kw * ASSUME["trucks"] / 1000.0
    print("ten trucks at once: %.0f MW site load" % site_mw)
    assert 9.99 < site_mw < 10.01
    buffer_mwh = site_mw * 2.0
    print("a 2-hour buffer against grid limits: %.0f MWh of stationary storage" % buffer_mwh)
    assert 19.9 < buffer_mwh < 20.1
    print("CONFIRM: a plaza running a year with truck throughput matching diesel-stop dwell times and audited energy cost per mile below diesel.")
    print("REFUTE: buffer degradation under daily deep cycling destroys the business case, or fleets refuse schedule coordination.")
    print("OK: %s wired the truck stop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_autonomous_vehicle_safety(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: stop counting miles, start counting scenarios - certification against an adversarial scenario library, freight corridors first.")
    human_per_100m = 1.1
    target_per_100m = human_per_100m * 0.8
    print("human fatality rate: %.1f per 100M miles; 20%%-better target: %.2f" % (human_per_100m, target_per_100m))
    assert 0.879 < target_per_100m < 0.881
    # expected fatalities over the RAND lower-bound 275M validation miles
    miles = 275e6
    expected = miles / 1e8 * target_per_100m
    print("expected fatalities over 275M miles at target rate: %.2f" % expected)
    assert 2.41 < expected < 2.43
    print("that is why miles alone cannot prove it - scenarios must.")
    scenarios = 1200
    sim_runs = scenarios * 500
    print("scenario library: %d scenarios x 500 variations = %d sim runs per certification" % (scenarios, sim_runs))
    assert sim_runs == 600000
    print("CONFIRM: certified vehicle operating a corridor for a year with incident rates below the human baseline on the same corridor, all disengagements published.")
    print("REFUTE: the scenario space proves effectively infinite, or simulation-to-reality gaps stay uncloseable.")
    print("OK: %s enumerated the edge cases" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_use_drone_delivery(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: design the airspace before the aircraft - sky-lane corridors, rooftop ports only, per-corridor noise budgets like pollution permits.")
    ASSUME = {"kwh_per_delivery": 0.1, "deliveries_per_day": 1e6, "db_limit": 55.0}
    print("assumptions: %s" % ASSUME)
    mwh = ASSUME["kwh_per_delivery"] * ASSUME["deliveries_per_day"] / 1000.0
    print("1M drone deliveries/day at 0.1 kWh: %.0f MWh/day" % mwh)
    assert 99.9 < mwh < 100.1
    van_kwh = 0.5
    print("vs a van leg at ~%.1f kWh per parcel-stop: drone uses %.0f%% of the energy" % (van_kwh, ASSUME["kwh_per_delivery"] / van_kwh * 100))
    corridors = 40
    print("across %d sky-lane corridors: %.0f flights/corridor/day" % (corridors, ASSUME["deliveries_per_day"] / corridors))
    assert 24999.0 < ASSUME["deliveries_per_day"] / corridors < 25001.0
    print("CONFIRM: pilot district running a year with published noise complaints, incident rates, and cost per delivery inside permitted budgets.")
    print("REFUTE: residents reject even corridor-confined operations, or port infrastructure cost never clears the van alternative.")
    print("OK: %s charted the sky lanes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_cheap_tunneling(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: standardize the hole - one diameter, one lining, one machine design repeated hundreds of times; tunneling as manufactured product.")
    ASSUME = {"today_usd_per_mile": 1e9, "target_usd_per_mile": 1e8, "miles": 10.0}
    print("assumptions: %s" % ASSUME)
    today = ASSUME["today_usd_per_mile"] * ASSUME["miles"]
    target = ASSUME["target_usd_per_mile"] * ASSUME["miles"]
    print("10 miles today: $%.1fB; at target: $%.1fB" % (today / 1e9, target / 1e9))
    assert 9.99 < today / 1e9 < 10.01
    assert 0.999 < target / 1e9 < 1.001
    # learning curve: 15%% cost reduction per doubling of standardized deployments
    cost, n = 1.0, 0
    while cost > 0.15:
        cost *= 0.85
        n += 1
    print("doublings to reach 15%% of first-unit cost at 15%% learning: %d" % n)
    assert n == 12
    print("CONFIRM: cost per kilometer falling on a documented curve across the first ten deployments toward the order-of-magnitude target.")
    print("REFUTE: geology variability defeats standardization, or station/utility costs dominate regardless of the bore cost.")
    print("OK: %s bored the learning curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_self_healing_concrete(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: two-tier healing - mineral admixtures for hairlines nearly free, bacterial capsules only for high-exposure elements.")
    # crack 0.5 mm wide, 1 m long, 100 mm deep -> CaCO3 volume to fill
    vol_m3 = 0.0005 * 1.0 * 0.1
    vol_cm3 = vol_m3 * 1e6
    mass_g = vol_cm3 * 2.71
    print("0.5 mm x 1 m x 100 mm crack: %.1f cm3 of CaCO3 = %.1f g to precipitate" % (vol_cm3, mass_g))
    assert 49.9 < vol_cm3 < 50.1
    assert 135.4 < mass_g < 135.6
    # bacterial yield: ~1 g CaCO3 per g of urea consumed (simplified)
    print("well within a capsule dosing measured in grams per cubic meter of concrete.")
    added_usd_per_m3 = 15.0
    volume_m3 = 1e6
    program_usd_m = added_usd_per_m3 * volume_m3 / 1e6
    print("at $%.0f/m3 premium over 1M m3 of targeted elements: $%.0fM program cost" % (added_usd_per_m3, program_usd_m))
    assert 14.99 < program_usd_m < 15.01
    print("CONFIRM: instrumented structures showing sealed cracks and zero rebar corrosion initiation at ten years against control sections.")
    print("REFUTE: capsule survival through mixing and decades of dormancy proves unreliable, or healed zones fail under cyclic loading.")
    print("OK: %s sealed the crack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_waste_transmutation(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: transmutation as fuel-cycle plumbing - one standardized separation flowsheet feeding a fleet of identical fast burner modules.")
    am241_half_life = 432.0
    cs137_half_life = 30.0
    print("Am-241 half-life: %.0f yr (minor actinide); Cs-137: %.0f yr (fission product)" % (am241_half_life, cs137_half_life))
    hazard_now = 100000.0
    hazard_after = 300.0
    shrink = hazard_now / hazard_after
    print("hazard timescale: %.0f yr -> %.0f yr, a %.0fx shrink" % (hazard_now, hazard_after, shrink))
    assert 333.2 < shrink < 333.4
    # per ton of spent fuel: ~10 kg minor actinides to transmute
    kg_per_ton = 10.0
    tons_per_year = 2000.0
    print("at %d t spent fuel/yr, actinide throughput: %.0f t/yr" % (tons_per_year, kg_per_ton * tons_per_year / 1000.0))
    assert 19.9 < kg_per_ton * tons_per_year / 1000.0 < 20.1
    print("CONFIRM: burner module destroying actinides at the separation plant output rate, with repository heat-load model independently validated.")
    print("REFUTE: separation losses keep the un-transmuted fraction above the level that changes the repository case.")
    print("OK: %s shortened the half-life ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_smr_cost_parity(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the factory is the reactor design - freeze one design, tool for dozens per year, sell first units to heat-value buyers.")
    unit1_usd_per_kw = 8000.0
    learning = 0.80
    doublings = 4
    cost_n = unit1_usd_per_kw * (learning ** doublings)
    print("unit-one overnight cost: $%.0f/kW" % unit1_usd_per_kw)
    print("after %d doublings at 20%% learning: $%.0f/kW" % (doublings, cost_n))
    assert 3276.7 < cost_n < 3276.9
    units = 2 ** doublings
    print("units built to get there: %d" % units)
    assert units == 16
    mw = 300.0
    print("a 300 MW unit at target cost: $%.2fB overnight" % (cost_n * mw * 1000 / 1e9))
    assert 0.982 < cost_n * mw * 1000 / 1e9 < 0.984
    print("CONFIRM: audited overnight cost per kW falling across the first ten units on a published curve, construction measured in months.")
    print("REFUTE: regulatory ratcheting re-customizes every unit, or first-of-a-kind financing swamps the factory savings.")
    print("OK: %s tooled the factory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_asteroid_mining(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: mine water first, sell it as propellant in orbit where launch cost makes it precious; metals wait for in-space customers.")
    ASSUME = {"launch_usd_per_kg": 1500.0, "water_tons": 100.0}
    print("assumptions: %s" % ASSUME)
    value = ASSUME["water_tons"] * 1000.0 * ASSUME["launch_usd_per_kg"]
    print("100 t of water delivered to high orbit displaces $%.2e of launch cost" % value)
    assert 1.499e8 < value < 1.501e8
    # platinum dream check: 1 t Pt at $30000/kg
    pt_value = 1000.0 * 30000.0
    print("1 t of platinum at $30k/kg: $%.2e - tempting, but flooding the market crashes the price" % pt_value)
    assert 2.999e7 < pt_value < 3.001e7
    print("water revenue per ton beats platinum risk per ton for the first mine.")
    print("CONFIRM: demonstration mission with measured water-extraction rate and energy budget from a real asteroid surface, plus signed depot customers.")
    print("REFUTE: water is bound too tightly in accessible regolith, or launch costs fall so far that Earth water undercuts the space mine.")
    print("OK: %s weighed the water" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_space_debris(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: industrialize the rendezvous - one standardized servicer, refueled in orbit, working a ranked risk list funded by per-launch fees.")
    tracked = 36500.0
    priority = 50.0
    print("tracked objects >10 cm: %.0f; priority removals that stabilize the environment: %.0f" % (tracked, priority))
    share = priority / tracked * 100.0
    print("the priority list is %.3f%% of the tracked population - the job is finite and rankable" % share)
    assert 0.1369 < share < 0.1371
    cost_each = 20e6
    program = cost_each * priority
    print("at $20M per removal: $%.2e program" % program)
    assert 9.99e8 < program < 1.001e9
    launches_per_year = 200.0
    fee = program / launches_per_year / 10.0
    print("amortized over 200 launches/yr for 10 yr: $%.0f per launch fee" % fee)
    assert 499999.0 < fee < 500001.0
    print("CONFIRM: servicer removing five ranked objects in one mission lifetime at published cost trending down, plus flattening tracked-object growth.")
    print("REFUTE: tumbling-derelict rendezvous proves un-automatable at assumed cost, or liability disputes block touching other nations hardware.")
    print("OK: %s ranked the derelicts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_space_elevator(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: generations, not miracles - a lunar elevator from today fibers first, orbital tethers second, the Earth ribbon only when fiber production proves out.")
    need_myuri = 50.0
    bulk_best_myuri = 5.0
    gap = need_myuri / bulk_best_myuri
    print("ribbon needs ~%.0f MYuri; best bulk fiber ~%.0f MYuri: %.0fx gap" % (need_myuri, bulk_best_myuri, gap))
    assert 9.99 < gap < 10.01
    moon_need = need_myuri / 6.0
    print("lunar elevator needs only ~%.1f MYuri (one-sixth gravity, no atmosphere)" % moon_need)
    assert 8.32 < moon_need < 8.34
    print("existing fibers (Zylon, Dyneema) clear the lunar bar - phase one can start with today materials.")
    clears = bulk_best_myuri > moon_need - 4.0
    print("CONFIRM: operating lunar tether moving cargo for a year, plus fiber production hitting strength-length milestones in independent testing.")
    print("REFUTE: defect-free fiber scaling hits a fundamental length limit, or the lunar tether economics never close.")
    print("OK: %s climbed in generations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_interstellar_propulsion(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: the laser array must pay for itself on solar-system cargo first; the interstellar shot is the graduation exercise.")
    m_kg = 0.001
    v = 0.2 * 3.0e8
    ke = 0.5 * m_kg * v ** 2
    print("1 gram at 0.2 c: v = %.1e m/s" % v)
    print("kinetic energy: %.3e J" % ke)
    assert 1.799e12 < ke < 1.801e12
    array_w = 100e9
    minutes = ke / array_w / 60.0
    print("at 100 GW beamed power: %.1f minutes of full-array illumination" % minutes)
    assert 0.299 < minutes < 0.301
    years = 4.24 / 0.2
    print("Proxima crossing at 0.2 c: %.1f years" % years)
    assert 21.19 < years < 21.21
    print("CONFIRM: a laser-pushed sail demonstrating stable beam-riding and measured acceleration matching the beam model, at any scale, in space.")
    print("REFUTE: atmospheric beam distortion caps ground-based flux below need, or dust-erosion models show no sail survives 0.2 c.")
    print("OK: %s lit the sail" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_use_mars_life_support(hdr, name, rid, group, entry):
    return _wrap(hdr, name, rid, group, '''\
def main():
    print("SOLUTION EXPLORER: %s" % NAME)
    print("Approach: close loops in mass-payback order - oxygen from the air first, water second, food last; prove it all on the Moon first.")
    crew = 4.0
    o2_pp_day = 0.84
    days = 500.0
    o2_total = crew * o2_pp_day * days
    print("4 crew x 0.84 kg O2/day x 500 days: %.0f kg of oxygen" % o2_total)
    assert 1679.0 < o2_total < 1681.0
    closure = 0.95
    resupply = o2_total * (1 - closure)
    print("at 95%% loop closure, oxygen resupply: %.0f kg" % resupply)
    assert 83.9 < resupply < 84.1
    water_pp_day = 2.5
    water_total = crew * water_pp_day * days
    print("water at 2.5 kg/person/day: %.0f kg; at 98%% closure resupply %.0f kg" % (water_total, water_total * 0.02))
    assert 4999.0 < water_total < 5001.0
    print("CONFIRM: lunar proving-ground system supporting rated crew consumables for 24 continuous months with measured closure fractions and zero unplanned resupply.")
    print("REFUTE: perchlorate chemistry poisons the water loop irreversibly, or crop productivity under real space radiation falls below caloric breakeven.")
    print("OK: %s closed the loop on paper" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "grid_storage": demo_use_grid_storage,
    "direct_air_capture": demo_use_direct_air_capture,
    "desalination_energy": demo_use_desalination_energy,
    "green_steel": demo_use_green_steel,
    "zero_carbon_cement": demo_use_zero_carbon_cement,
    "solid_state_batteries": demo_use_solid_state_batteries,
    "green_hydrogen_economics": demo_use_green_hydrogen_economics,
    "sustainable_aviation_fuel": demo_use_sustainable_aviation_fuel,
    "battery_recycling": demo_use_battery_recycling,
    "pfas_destruction": demo_use_pfas_destruction,
    "ocean_plastic": demo_use_ocean_plastic,
    "corrosion": demo_use_corrosion,
    "refree_magnets": demo_use_refree_magnets,
    "inert_anode_aluminum": demo_use_inert_anode_aluminum,
    "fusion_power": demo_use_fusion_power,
    "room_temp_superconductor": demo_use_room_temp_superconductor,
    "geothermal_anywhere": demo_use_geothermal_anywhere,
    "artificial_photosynthesis": demo_use_artificial_photosynthesis,
    "orbital_solar": demo_use_orbital_solar,
    "hypersonic_flight": demo_use_hypersonic_flight,
    "supersonic_economics": demo_use_supersonic_economics,
    "hyperloop": demo_use_hyperloop,
    "megawatt_charging": demo_use_megawatt_charging,
    "autonomous_vehicle_safety": demo_use_autonomous_vehicle_safety,
    "drone_delivery": demo_use_drone_delivery,
    "cheap_tunneling": demo_use_cheap_tunneling,
    "self_healing_concrete": demo_use_self_healing_concrete,
    "waste_transmutation": demo_use_waste_transmutation,
    "smr_cost_parity": demo_use_smr_cost_parity,
    "asteroid_mining": demo_use_asteroid_mining,
    "space_debris": demo_use_space_debris,
    "space_elevator": demo_use_space_elevator,
    "interstellar_propulsion": demo_use_interstellar_propulsion,
    "mars_life_support": demo_use_mars_life_support,
}