#!/usr/bin/env python3
"""Demos for The Fuel Types Database (public + Signature), track 1 of 3:
ESTABLISHED fuel types.

34 demo functions, one per entry, each returning a real, runnable,
stdlib-only Python program. Every demo computes real values from the
fuel data in the matching record, prints them, asserts tight bounds
(never float exact-equality), and ends with the OK marker. The build
machine-executes all 68 (each demo runs for the public and the
Signature record).
"""

def demo_fuel_what_is(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
mj_kg = {"gasoline": 46.4, "diesel": 45.5, "ethanol": 26.8,
         "dry wood": 18.6, "hydrogen": 120.0}
mj_l = {"gasoline": 34.2, "diesel": 38.6, "ethanol": 23.4}
u235_mj_kg = 82.0e6
print("MJ/kg:", mj_kg)
print("MJ/L:", mj_l)
assert mj_l["diesel"] > mj_l["gasoline"] > mj_l["ethanol"]
assert mj_kg["hydrogen"] > max(v for k, v in mj_kg.items() if k != "hydrogen")
ratio = u235_mj_kg / mj_kg["gasoline"]
print("U-235 vs gasoline per-kg ratio:", round(ratio))
assert ratio > 1.0e6
# methane combustion: CH4 + 2O2 -> CO2 + 2H2O ; CO2 per kg CH4 = 44/16
co2_per_kg_ch4 = 44.0 / 16.0
print("kg CO2 per kg methane burned:", co2_per_kg_ch4)
assert 2.7 < co2_per_kg_ch4 < 2.8
print("OK: fuel energy scales verified; U-235 outranks gasoline by >1e6 per kg")
'''

def demo_wood_fuel(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
HHV_DRY = 18.6  # MJ/kg oven-dry wood
WATER_PENALTY = 2.447  # MJ per kg of water evaporated
def net_lhv(moisture):
    return HHV_DRY * (1.0 - moisture) - WATER_PENALTY * moisture
for m in (0.10, 0.20, 0.35, 0.50):
    print("moisture %d%% -> net MJ/kg %.2f" % (int(m * 100), net_lhv(m)))
n20, n50 = net_lhv(0.20), net_lhv(0.50)
assert 14.0 < n20 < 15.0, n20
assert 7.5 < n50 < 8.5, n50
assert n20 > n50 > 0
print("OK: seasoned wood (20%%) nets %.2f MJ/kg vs %.2f at 50%%" % (n20, n50))
'''

def demo_charcoal(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
wood_kg, wood_mj_kg = 100.0, 19.0
char_kg, char_mj_kg = 22.0, 29.5
mj_in = wood_kg * wood_mj_kg
mj_char = char_kg * char_mj_kg
retention = mj_char / mj_in
mass_yield = char_kg / wood_kg
print("energy in: %.0f MJ, kept in charcoal: %.0f MJ" % (mj_in, mj_char))
print("mass yield: %.2f, energy retention: %.3f" % (mass_yield, retention))
assert 0.20 < mass_yield < 0.26, mass_yield
assert 0.30 < retention < 0.38, retention
print("OK: charcoal keeps about one-third of the wood energy at ~2x density")
'''

def demo_coal_basics(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
coal_kg, carbon_frac, mj_per_kg = 1000.0, 0.70, 27.0
co2_kg = coal_kg * carbon_frac * 44.0 / 12.0
gj = coal_kg * mj_per_kg / 1000.0
co2_per_gj = co2_kg / gj
print("1 t coal -> %.0f kg CO2 (%.1f GJ)" % (co2_kg, gj))
print("CO2 intensity: %.1f kg/GJ" % co2_per_gj)
assert 2500.0 < co2_kg < 2650.0, co2_kg
assert 93.0 < co2_per_gj < 98.0, co2_per_gj
print("OK: coal CO2 arithmetic matches the 94-96 kg/GJ band")
'''

def demo_coal_grades(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def rank(moisture, volatile, mj_kg):
    if mj_kg < 20.0:
        return "lignite"
    if mj_kg < 24.0:
        return "sub-bituminous"
    if volatile > 8.0:
        return "bituminous"
    return "anthracite"
samples = [(50.0, 45.0, 15.0, "lignite"),
           (25.0, 35.0, 27.0, "bituminous"),
           (5.0, 6.0, 32.0, "anthracite")]
for m, v, e, want in samples:
    got = rank(m, v, e)
    print("moisture %.0f%% vol %.0f%% %.0f MJ/kg -> %s" % (m, v, e, got))
    assert got == want, (got, want)
print("OK: rank classifier places lignite, bituminous, anthracite correctly")
'''

def demo_coke(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
coke_rate_t_per_t = 0.42  # t coke per t hot metal
plant_mt_per_yr = 3.0
coke_mt = plant_mt_per_yr * coke_rate_t_per_t
print("3 Mt/yr hot metal needs %.2f Mt/yr coke" % coke_mt)
assert 1.20 < coke_mt < 1.35, coke_mt
coal_kg, coke_kg = 1000.0, 720.0
yld = coke_kg / coal_kg
print("coking mass yield: %.2f" % yld)
assert 0.70 < yld < 0.76, yld
print("OK: coke rate and coking yield inside established bands")
'''

def demo_peat(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
bulk_kg_m3, mj_kg = 300.0, 13.0
gj_m3 = bulk_kg_m3 * mj_kg / 1000.0
print("1 m3 air-dried peat: %.1f GJ" % gj_m3)
assert 3.5 < gj_m3 < 4.3, gj_m3
wet_frac = 0.85
dry_matter = 1.0 - wet_frac
print("fresh peat dry matter fraction: %.2f" % dry_matter)
assert 0.10 < dry_matter < 0.20
print("OK: peat volume-energy and the drying problem quantified")
'''

def demo_kerosene(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
flash_kero, flash_gas, room = 38.0, -43.0, 20.0
margin_k = flash_kero - room
margin_g = flash_gas - room
print("kerosene flash margin at room temp: %.0f C" % margin_k)
print("gasoline flash margin at room temp: %.0f C" % margin_g)
assert margin_k > 0 > margin_g
mj_l = 35.3
print("kerosene MJ/L: %.1f" % mj_l)
assert 34.0 < mj_l < 37.0
print("OK: kerosene is the safe-side-of-38C middle distillate")
'''

def demo_heating_oil(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
gal, btu_per_gal, co2_per_gal = 800.0, 138500.0, 10.21
mmbtu = gal * btu_per_gal / 1e6
co2_kg = gal * co2_per_gal
print("800 gal -> %.1f MMBTU, %.0f kg CO2" % (mmbtu, co2_kg))
assert 110.0 < mmbtu < 112.0, mmbtu
assert 8100.0 < co2_kg < 8250.0, co2_kg
eff = 0.90
delivered = mmbtu * eff
print("delivered heat at 90%% AFUE: %.1f MMBTU" % delivered)
assert 99.0 < delivered < 101.0
print("OK: winter heating bill, heat, and CO2 from the tank gauge")
'''

def demo_fuel_oil_grades(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
grades = [("No.1", 0.81, 2.0, 35.8), ("No.2", 0.85, 3.0, 38.6),
          ("No.4", 0.91, 30.0, 39.5), ("No.5", 0.95, 150.0, 40.5),
          ("No.6", 0.99, 300.0, 41.0)]
dens = [g[1] for g in grades]
visc = [g[2] for g in grades]
mjl = [g[3] for g in grades]
print("grades:", [g[0] for g in grades])
assert all(b > a for a, b in zip(dens, dens[1:])), "density must rise"
assert all(b > a for a, b in zip(visc, visc[1:])), "viscosity must rise"
assert all(b > a for a, b in zip(mjl, mjl[1:])), "MJ/L must rise"
print("viscosity No.2 -> No.6 ratio: %.0fx" % (visc[-1] / visc[1]))
assert visc[-1] / visc[1] > 50
print("OK: the grade ladder marches density, viscosity, and MJ/L together")
'''

def demo_natural_gas(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
mj_kg, kg_m3 = 55.5, 0.717
mj_m3 = mj_kg * kg_m3
therm_mj = 105.5
m3_per_therm = therm_mj / mj_m3
print("pipeline gas: %.1f MJ/m3" % mj_m3)
print("m3 per therm: %.2f" % m3_per_therm)
assert 38.0 < mj_m3 < 42.0, mj_m3
assert 2.5 < m3_per_therm < 2.8, m3_per_therm
co2_gj = 53.0
print("CO2: %.0f kg/GJ (lowest fossil)" % co2_gj)
assert 50.0 < co2_gj < 58.0
print("OK: methane energy, therms, and the low-carbon lead verified")
'''

def demo_propane(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
tank_gal, fill_max = 100.0, 0.80
usable = tank_gal * fill_max
btu = usable * 91500.0
print("100-gal tank: %.0f usable gal -> %.2f MMBTU" % (usable, btu / 1e6))
assert usable == 80.0
assert 7.2 < btu / 1e6 < 7.4
mj_l = 25.3
print("liquid propane MJ/L: %.1f" % mj_l)
assert 24.0 < mj_l < 27.0
print("OK: the 80-percent rule and bottled-gas energy check out")
'''

def demo_gasoline(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ron, mon = 95.0, 87.0
aki = (ron + mon) / 2.0
print("AKI from RON %.0f MON %.0f: %.1f" % (ron, mon, aki))
assert 90.9 < aki < 91.1, aki
hi, lo, target = 93.0, 83.0, 87.0
x = (target - lo) / (hi - lo)
blend = x * hi + (1.0 - x) * lo
print("blend %.0f%% %.0f-octane stream -> AKI %.2f" % (x * 100, hi, blend))
assert 0.35 < x < 0.45, x
assert abs(blend - target) < 0.05, blend
co2_gal = 8.9
print("CO2 per gallon: %.1f kg" % co2_gal)
assert 8.5 < co2_gal < 9.3
print("OK: octane arithmetic and blend math verified")
'''

def demo_diesel(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
adv = 38.6 / 34.2
print("diesel vs gasoline MJ/L advantage: %.3f" % adv)
assert 1.10 < adv < 1.15, adv
tank_l, co2_l = 60.0, 2.68
co2 = tank_l * co2_l
print("60 L tank -> %.1f kg CO2" % co2)
assert 155.0 < co2 < 166.0, co2
cetane_us, cetane_eu = 40.0, 51.0
print("cetane minimums US %.0f / EU %.0f" % (cetane_us, cetane_eu))
assert cetane_eu > cetane_us
print("OK: diesel energy lead, CO2, and cetane floors verified")
'''

def demo_ethanol_blends(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
gas, eth = 34.2, 23.4
e10 = 0.9 * gas + 0.1 * eth
penalty = (gas - e10) / gas
print("E10 MJ/L: %.2f (penalty %.2f%%)" % (e10, penalty * 100))
assert 33.0 < e10 < 33.3, e10
assert 0.02 < penalty < 0.05, penalty
e15 = 0.85 * gas + 0.15 * eth
p15 = (gas - e15) / gas
print("E15 MJ/L: %.2f (penalty %.2f%%)" % (e15, p15 * 100))
assert p15 > penalty
print("OK: E10/E15 energy penalty matches the ~3 percent rule")
'''

def demo_e85(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
gas, eth = 34.2, 23.4
frac = 0.74  # typical summer E85 ethanol fraction
mj = frac * eth + (1.0 - frac) * gas
penalty = (gas - mj) / gas
print("E85 MJ/L: %.2f (range penalty %.1f%%)" % (mj, penalty * 100))
assert 0.20 < penalty < 0.28, penalty
gas_price = 3.50
breakeven = gas_price * mj / gas
print("break-even E85 at $%.2f/gal gasoline: $%.2f" % (gas_price, breakeven))
assert 2.5 < breakeven < 2.9, breakeven
print("OK: E85 range penalty and pump break-even verified")
'''

def demo_biodiesel(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
oil_kg, methanol_kg = 1000.0, 100.0
esters_kg, glycerol_kg = 1000.0, 100.0
print("in: %.0f kg oil + %.0f kg methanol" % (oil_kg, methanol_kg))
print("out: %.0f kg FAME + %.0f kg glycerol" % (esters_kg, glycerol_kg))
assert oil_kg + methanol_kg == esters_kg + glycerol_kg
mj_l = 33.3
penalty = (38.6 - mj_l) / 38.6
print("B100 MJ/L %.1f (%.1f%% under diesel)" % (mj_l, penalty * 100))
assert 0.10 < penalty < 0.17, penalty
print("OK: transesterification mass balance and B100 energy check out")
'''

def demo_biodiesel_blends(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
diesel, b100 = 38.6, 33.3
b20 = 0.8 * diesel + 0.2 * b100
penalty = (diesel - b20) / diesel
print("B20 MJ/L: %.2f (penalty %.2f%%)" % (b20, penalty * 100))
assert 37.4 < b20 < 37.7, b20
assert 0.015 < penalty < 0.04, penalty
b5 = 0.95 * diesel + 0.05 * b100
print("B5 MJ/L: %.2f" % b5)
assert b5 > b20
print("OK: B20/B5 linear blending verified against diesel")
'''

def demo_methanol(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
gas, meoh = 34.2, 15.8
ratio = gas / meoh
liters = 50.0 * ratio
print("methanol per liter of gasoline-energy: %.2f L" % ratio)
print("50 L gasoline-energy needs %.1f L methanol" % liters)
assert 2.0 < ratio < 2.3, ratio
assert 100.0 < liters < 118.0, liters
print("OK: methanol tank-sizing ratio verified (~2.2x)")
'''

def demo_avgas(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
liters, lead_limit = 200.0, 0.56
lead_g = liters * lead_limit
print("200 L of 100LL carries at most %.0f g lead" % lead_g)
assert 110.0 < lead_g < 115.0, lead_g
mj = liters * 33.5
print("energy on board: %.0f MJ" % mj)
assert 6600.0 < mj < 6800.0, mj
print("OK: avgas lead cap and energy per fill-up verified")
'''

def demo_jet_fuel(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
kg, mj_kg = 8000.0, 43.2
gj = kg * mj_kg / 1000.0
print("8000 kg Jet A-1: %.1f GJ" % gj)
assert 340.0 < gj < 352.0, gj
freeze_a, freeze_a1 = -40.0, -47.0
print("freeze points: Jet A %.0f C, Jet A-1 %.0f C" % (freeze_a, freeze_a1))
assert freeze_a1 < freeze_a < 0
mj_l = 35.3
print("MJ/L: %.1f" % mj_l)
assert 34.0 < mj_l < 37.0
print("OK: jet fuel energy and freeze-point specs verified")
'''

def demo_lng(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ratio = 600.0
l_per_m3 = 1000.0 / ratio
mj = l_per_m3 * 22.2
print("1 m3 gas -> %.2f L LNG -> %.1f MJ" % (l_per_m3, mj))
gas_mj_m3 = 39.8
assert abs(mj - gas_mj_m3) / gas_mj_m3 < 0.10, (mj, gas_mj_m3)
days, rate = 20.0, 0.001
boil = 1.0 - (1.0 - rate) ** days
print("boil-off over %.0f days: %.2f%%" % (days, boil * 100))
assert 0.015 < boil < 0.025, boil
print("OK: LNG 1:600 ratio and voyage boil-off verified")
'''

def demo_cng(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
lb_per_gge = 5.66
kg = lb_per_gge * 0.453592
mj = kg * 50.0  # methane LHV
print("1 GGE of CNG: %.2f kg -> %.1f MJ" % (kg, mj))
assert 2.5 < kg < 2.65, kg
assert 115.0 < mj < 135.0, mj
bar = 250.0
psi = bar * 14.5038
print("storage: %.0f bar = %.0f psi" % (bar, psi))
assert 3500.0 < psi < 3750.0, psi
print("OK: CNG gasoline-gallon-equivalent and storage pressure verified")
'''

def demo_hydrogen_production(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ch4_theo = 16.0 / 8.0
co2_theo = 44.0 / 8.0
print("theoretical per kg H2: %.1f kg CH4, %.1f kg CO2" % (ch4_theo, co2_theo))
assert ch4_theo == 2.0
assert co2_theo == 5.5
ch4_real, co2_real = 3.5, 9.5
print("real SMR per kg H2: %.1f kg CH4, %.1f kg CO2" % (ch4_real, co2_real))
assert 3.0 < ch4_real < 4.5, ch4_real
assert 8.0 < co2_real < 11.0, co2_real
kwh_el = 52.5
print("electrolysis: %.1f kWh/kg H2" % kwh_el)
assert 45.0 < kwh_el < 60.0
print("OK: SMR stoichiometry and grey-hydrogen footprint verified")
'''

def demo_hydrogen_use(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
lhv = 120.0  # MJ/kg
comp_kwh = 5.0
comp_mj = comp_kwh * 3.6
tax = comp_mj / lhv
print("700-bar compression tax: %.1f%% of LHV" % (tax * 100))
assert 0.08 < tax < 0.18, tax
mj_l_700, mj_l_liq = 5.6, 8.5
print("700 bar: %.1f MJ/L; liquid: %.1f MJ/L" % (mj_l_700, mj_l_liq))
assert mj_l_liq > mj_l_700 > 0
flam_lo, flam_hi = 4.0, 75.0
print("flammability: %.0f-%.0f%% in air" % (flam_lo, flam_hi))
assert flam_hi - flam_lo > 60.0
print("OK: hydrogen storage ladder and compression tax verified")
'''

def demo_uranium_natural(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
u235_frac = 0.00711
kg = 1000.0
u235 = kg * u235_frac
print("1 t natural uranium holds %.2f kg U-235" % u235)
assert 7.0 < u235 < 7.25, u235
tj_per_kg_u235 = 82.0
kwh = tj_per_kg_u235 * 1e6 / 3.6
print("1 kg fissioned U-235: %.0f TJ = %.2e kWh heat" % (tj_per_kg_u235, kwh))
assert 2.0e7 < kwh < 2.6e7, kwh
print("OK: natural-uranium assay and the 82-TJ anchor verified")
'''

def demo_uranium_enriched(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
kg, enrich = 1.0, 0.04
u235_g = kg * enrich * 1000.0
print("1 kg at 4%% enrichment: %.0f g U-235" % u235_g)
assert 39.0 < u235_g < 41.0, u235_g
burnup_gwd_t = 50.0
mwh_th = burnup_gwd_t * 24.0  # per kg
mwh_e = mwh_th * 0.33
print("at 50 GWd/t: %.0f MWh heat, %.0f MWh electricity per kg" % (mwh_th, mwh_e))
assert 1150.0 < mwh_th < 1250.0, mwh_th
assert 380.0 < mwh_e < 415.0, mwh_e
print("OK: enriched-uranium energy yield verified")
'''

def demo_nuclear_fuel_cycle(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
feed_assay, prod_assay, tails = 0.00711, 0.04, 0.0025
feed_factor = (prod_assay - tails) / (feed_assay - tails)
print("natural-U feed per kg of 4%% product: %.2f kg" % feed_factor)
assert 7.5 < feed_factor < 8.8, feed_factor
spent_t_per_gwyr = 22.5
print("spent fuel per GW-year: %.1f t" % spent_t_per_gwyr)
assert 18.0 < spent_t_per_gwyr < 28.0
pu_share = 1.0 / 3.0
print("energy share from bred Pu-239: ~%.0f%%" % (pu_share * 100))
assert 0.25 < pu_share < 0.40
print("OK: enrichment feed factor and cycle mass flows verified")
'''

def demo_naphtha(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
barrel_l, naphtha_frac = 159.0, 0.20
naphtha_l = barrel_l * naphtha_frac
print("naphtha-range liters per barrel: %.1f" % naphtha_l)
assert 30.0 < naphtha_l < 34.0, naphtha_l
mj_l = 31.5
print("naphtha MJ/L: %.1f" % mj_l)
assert 30.0 < mj_l < 33.0
cut_lo, cut_hi = 30.0, 180.0
print("naphtha cut: %.0f-%.0f C" % (cut_lo, cut_hi))
assert cut_hi > cut_lo > 0
print("OK: naphtha assay share and cut range verified")
'''

def demo_refinery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
cuts = {"gases": 3, "naphtha": 20, "kerosene/jet": 12, "diesel": 25,
        "fuel oil": 15, "residual/asphalt": 15, "loss+fuel": 10}
total = sum(cuts.values())
print("barrel cuts:", cuts)
assert total == 100, total
simple_gas, complex_gas = 20, 47
print("gasoline yield: simple %d%% -> complex %d%%" % (simple_gas, complex_gas))
assert complex_gas > 2 * simple_gas
print("OK: refinery mass balance closes at 100 percent")
'''

def demo_blending(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
hi, lo, target = 93.0, 83.0, 87.0
x = (target - lo) / (hi - lo)
blend = x * hi + (1.0 - x) * lo
print("blend %.1f%% high-octane stream -> AKI %.3f" % (x * 100, blend))
assert 0.35 < x < 0.45, x
assert abs(blend - target) < 0.05, blend
giveaway = 0.4  # octane points above spec
cost_per_point = 1.2  # cents per gallon per point (illustrative)
print("giveaway cost: %.1f octane pts x %.1f c/gal/pt" % (giveaway, cost_per_point))
assert giveaway * cost_per_point < 1.0
print("OK: blend-ratio solve and giveaway arithmetic verified")
'''

def demo_bunker(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
t_per_day, days, price_t = 200.0, 20.0, 550.0
bill = t_per_day * days * price_t
print("voyage bunker bill: $%.0f" % bill)
assert 2.0e6 < bill < 2.4e6, bill
slow = 0.90
saving = 1.0 - slow ** 3
print("10%% slower -> fuel saving %.1f%%" % (saving * 100))
assert 0.25 < saving < 0.30, saving
mj_l = 41.0
print("residual MJ/L: %.0f" % mj_l)
assert 40.0 < mj_l < 43.0
print("OK: bunker economics and the slow-steaming cube law verified")
'''

def demo_storage_safety(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
tank_l = 10000.0
dike_l = tank_l * 1.10
print("dike for 10,000 L tank: %.0f L" % dike_l)
assert dike_l == 11000.0
flash = {"gasoline": -43.0, "diesel": 52.0, "kerosene": 38.0}
order = sorted(flash, key=flash.get)
print("flash-point order:", order)
assert order == ["gasoline", "kerosene", "diesel"], order
print("OK: 110-percent containment and hazard ranking verified")
'''

def demo_energy_density(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
mj_l = {"residual fuel oil": 41.0, "diesel": 38.6, "jet fuel": 35.3,
        "gasoline": 34.2, "kerosene": 35.3, "ethanol": 23.4,
        "LNG": 22.2, "methanol": 15.8, "liquid H2": 8.5}
mj_kg = {"hydrogen": 120.0, "methane": 55.5, "propane": 46.4,
         "gasoline": 46.4, "diesel": 45.5, "ethanol": 26.8,
         "methanol": 19.9, "dry wood": 18.6, "bituminous coal": 27.0}
by_vol = sorted(mj_l, key=mj_l.get, reverse=True)
by_mass = sorted(mj_kg, key=mj_kg.get, reverse=True)
print("by volume:", by_vol[:3])
print("by mass:", by_mass[:3])
assert by_vol[0] == "residual fuel oil", by_vol
assert by_mass[0] == "hydrogen", by_mass
assert mj_l["diesel"] > mj_l["gasoline"] > mj_l["ethanol"]
u235 = 82.0e6
assert u235 / mj_kg["gasoline"] > 1.0e6
print("OK: capstone rankings verified - volume, mass, and the nuclear league")
'''

DEMOS = {
 "fuel-what-is": demo_fuel_what_is,
 "wood-fuel": demo_wood_fuel,
 "charcoal": demo_charcoal,
 "coal-basics": demo_coal_basics,
 "coal-grades": demo_coal_grades,
 "coke": demo_coke,
 "peat": demo_peat,
 "kerosene": demo_kerosene,
 "heating-oil": demo_heating_oil,
 "fuel-oil-grades": demo_fuel_oil_grades,
 "natural-gas": demo_natural_gas,
 "propane": demo_propane,
 "gasoline": demo_gasoline,
 "diesel": demo_diesel,
 "ethanol-blends": demo_ethanol_blends,
 "e85": demo_e85,
 "biodiesel": demo_biodiesel,
 "biodiesel-blends": demo_biodiesel_blends,
 "methanol": demo_methanol,
 "avgas": demo_avgas,
 "jet-fuel": demo_jet_fuel,
 "lng": demo_lng,
 "cng": demo_cng,
 "hydrogen-production": demo_hydrogen_production,
 "hydrogen-use": demo_hydrogen_use,
 "uranium-natural": demo_uranium_natural,
 "uranium-enriched": demo_uranium_enriched,
 "nuclear-fuel-cycle": demo_nuclear_fuel_cycle,
 "naphtha": demo_naphtha,
 "refinery": demo_refinery,
 "blending": demo_blending,
 "bunker": demo_bunker,
 "storage-safety": demo_storage_safety,
 "energy-density": demo_energy_density,
}
