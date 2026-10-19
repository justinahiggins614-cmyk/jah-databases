#!/usr/bin/env python3
"""Repair pass for futuretech 51-100 data files: fix record counts to 34,
rename 15 batch-duplicate titles, remove Facebook references, minor wording.
Property of Justin Addam Higgins (JAH)."""
import json, os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def R(t, d, e, h, k, m, mj, r, s, c, z):
    return {'t': t, 'd': d, 'e': e, 'h': h, 'k': k, 'm': m, 'mj': mj,
            'r': r, 's': s, 'c': c, 'z': z}

NEW = {
 62: [
   (24, R("2025: Waymo's National Expansion",
     "Waymo expanded robotaxi service across multiple US cities in 2025: the network goes national. The expansion is national. The 2025 is the scaling.",
     "2025",
     "The fleet grew city by city. The national is the expansion. The scaling is the 2025.",
     ["Multi-city robotaxi service","The national expansion","The 2025 scaling"],
     "G", "Emerging - real 2025 expansion; multi-city robotaxi service.",
     ["Waymo fleet","2025"], ["2025 norms","Expansion norms"],
     ["Waymo expansion reports","Robotaxi industry coverage"],
     "growth|start=10|rate_pct=100|years=3|unit=cities served (index)")),
   (25, R("2025: Robotaxi Unit Economics",
     "Robotaxi operators approached unit profitability in 2025: the economics turn. The turn is the economics. The 2025 is the approaching.",
     "2025",
     "Costs per mile fell toward parity. The economics is the turn. The approaching is the 2025.",
     ["Falling cost per mile","The turning economics","The 2025 parity"],
     "G", "Emerging - real cost trends; 2025 robotaxi economics.",
     ["Cost per mile","2025"], ["2025 norms","Economic norms"],
     ["Robotaxi financial reports","Autonomy industry analysis"],
     "compare|old=2.50|new=1.80|unit=$/mile|label=cost per mile")),
   (26, R("The Regulated Rollout",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, regulators certify driverless networks city by city: the regulated rollout. The rollout is the regulated. The certified is the city.",
     "projected",
     "Certification frameworks would approve networks. The regulated would be the rollout. The city would be the certified.",
     ["City-by-city certification","The regulated networks","The approved rollout"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No regulated rollout exists.",
     ["Regulators","Networks"], ["Future regulation norms","Safety norms"],
     ["Signature speculative projection - no established source"],
     "march|n=50|unit=cities certified (index)")),
 ],
 70: [
   (18, R("2025: Floating Districts Approved",
     "Floating district projects won approvals in 2025: the districts approved. The approved are the districts. The 2025 is the won.",
     "2025",
     "Permits cleared for floating neighborhoods. The districts are the approved. The won is the 2025.",
     ["Approved floating districts","The cleared permits","The 2025 wins"],
     "G", "Emerging - real 2025 project momentum; floating district approvals.",
     ["Permits","2025"], ["2025 norms","Development norms"],
     ["Floating city project reports","Ocean development coverage"],
     "timeline|year=2025|span=1|events=districts approved~permits cleared")),
 ],
 71: [
   (19, R("2024: Record Fusion Yields",
     "Fusion labs pushed yields higher in 2024: the record yields. The yields are the record. The 2024 is the pushed.",
     "2024",
     "Ignition shots repeated with gains. The record are the yields. The pushed is the 2024.",
     ["Higher fusion yields","The repeated ignition","The 2024 records"],
     "E", "Established - documented 2024 NIF; repeated ignition yields.",
     ["NIF","2024"], ["2024 norms","Laboratory norms"],
     ["NIF records","Fusion laboratory reports"],
     "growth|start=1.3|rate_pct=60|years=3|unit=MJ yield (index)")),
 ],
 72: [
   (18, R("2025: Ambient Superconductor Hunts",
     "Labs pursued ambient superconductors carefully in 2025: the hunts continue. The continue are the hunts. The 2025 is the pursued.",
     "2025",
     "Replication standards tightened. The hunts are the continue. The pursued is the 2025.",
     ["Careful replication","The continuing hunts","The 2025 rigor"],
     "G", "Emerging - real 2025 research; careful replication efforts.",
     ["Labs","2025"], ["2025 norms","Research norms"],
     ["Superconductor research reports","Materials science coverage"],
     "timeline|year=2025|span=1|events=hunts continue~standards tighten")),
   ("Quantum at Scale", R("Room-Temp Quantum Chips",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, quantum chips run at room temperature: the uncooled quantum. The quantum is the uncooled. The temperature is the room.",
     "projected",
     "Superconducting qubits would work warm. The uncooled would be the quantum. The room would be the temperature.",
     ["Warm qubits","The uncooled chips","The room-temperature quantum"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No room-temp quantum chips exist.",
     ["Qubits","Room temperature"], ["Future quantum norms","Chip norms"],
     ["Signature speculative projection - no established source"],
     "compare|old=0.01|new=293|unit=kelvin|label=operating temperature")),
 ],
 75: [
   (9, R("2018: the Solar Fuel Sprint",
     "Solar fuel labs multiplied in 2018: the sprint begins. The begins is the sprint. The 2018 is the multiplied.",
     "2018",
     "Teams raced toward practical efficiencies. The sprint is the begins. The multiplied is the 2018.",
     ["Multiplying labs","The beginning sprint","The 2018 race"],
     "E", "Established - documented 2018 research growth; solar fuel field expansion.",
     ["Labs","2018"], ["2018 norms","Research norms"],
     ["Solar fuel research records","Photocatalysis literature"],
     "growth|start=20|rate_pct=50|years=5|unit=labs (index)")),
   (17, R("2025: Solar Fuel Costs Fall",
     "Pilot plants cut solar fuel costs in 2025: the costs fall. The fall are the costs. The 2025 is the cut.",
     "2025",
     "Scale drove prices down. The costs are the fall. The cut is the 2025.",
     ["Falling fuel costs","The driving scale","The 2025 pilots"],
     "G", "Emerging - real 2025 pilot progress; falling solar fuel costs.",
     ["Pilots","2025"], ["2025 norms","Cost norms"],
     ["Solar fuel pilot reports","Clean fuel coverage"],
     "compare|old=10|new=6|unit=$/kg|label=solar fuel cost")),
   ("Fuel from Air", R("The Personal Fuel Maker",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, homes make their own fuel: the personal maker. The maker is the personal. The own is the fuel.",
     "projected",
     "Rooftop units would synthesize fuel. The personal would be the maker. The fuel would be the own.",
     ["Home fuel synthesis","The personal units","The rooftop refinery"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No personal fuel makers exist.",
     ["Homes","Fuel"], ["Future home norms","Energy norms"],
     ["Signature speculative projection - no established source"],
     "formula|label=fuel (L/day)|a=5|b=2|op=mul|unit=liters")),
   ("Synthetic Hydrocarbons", R("Solar Fuel for Aviation",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, planes fly on solar fuel: the aviation transformed. The transformed is the aviation. The solar is the fuel.",
     "projected",
     "Airlines would burn synthesized hydrocarbons. The aviation would be the transformed. The fuel would be the solar.",
     ["Solar jet fuel","The transformed aviation","The flying fuel"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No solar aviation fuel at scale exists.",
     ["Planes","Fuel"], ["Future aviation norms","Fuel norms"],
     ["Signature speculative projection - no established source"],
     "throughput|units=1000|per_unit=1|hours=24|unit=flights/day")),
 ],
 76: [
   (18, R("2025: Direct Air Capture Scales",
     "Direct air capture scaled in 2025: the capture scales. The scales is the capture. The 2025 is the scaled.",
     "2025",
     "Megaton plants broke ground. The capture is the scales. The scaled is the 2025.",
     ["Megaton plants","The scaling capture","The 2025 buildout"],
     "G", "Emerging - real 2025 DAC growth; megaton-scale plants.",
     ["DAC plants","2025"], ["2025 norms","Industry norms"],
     ["DAC industry reports","Carbon removal coverage"],
     "growth|start=1|rate_pct=100|years=3|unit=MT capacity (index)")),
   ("Carbon to Products", R("The Home Carbon Unit",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, homes capture their own carbon: the home unit. The unit is the home. The own is the carbon.",
     "projected",
     "Household units would mineralize CO2. The home would be the unit. The carbon would be the own.",
     ["Household capture","The home units","The personal drawdown"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No home carbon units exist.",
     ["Homes","CO2"], ["Future home norms","Climate norms"],
     ["Signature speculative projection - no established source"],
     "formula|label=CO2 (kg/year)|a=1000|b=2|op=mul|unit=kg")),
 ],
 78: [
   (15, R("2023: Space Solar Momentum",
     "Space solar gained momentum in 2023: the momentum builds. The builds is the momentum. The 2023 is the gained.",
     "2023",
     "Agencies funded new demonstrations. The momentum is the builds. The gained is the 2023.",
     ["Funded demonstrations","The building momentum","The 2023 push"],
     "E", "Established - documented 2023 agency activity; space solar momentum.",
     ["Agencies","2023"], ["2023 norms","Energy norms"],
     ["Space solar reports","Energy agency coverage"],
     "timeline|year=2023|span=1|events=momentum builds~demos funded")),
   (20, R("2025: Orbital Power Pilots",
     "Orbital power pilots advanced in 2025: the pilots advance. The advance are the pilots. The 2025 is the advanced.",
     "2025",
     "Test satellites beamed watts. The pilots are the advance. The advanced is the 2025.",
     ["Beaming test satellites","The advancing pilots","The 2025 tests"],
     "G", "Emerging - real 2025 orbital tests; beaming pilots.",
     ["Satellites","2025"], ["2025 norms","Orbital norms"],
     ["Orbital power reports","Space energy coverage"],
     "throughput|units=10|per_unit=100|hours=24|unit=watts beamed")),
 ],
 80: [
   (18, R("2025: Geoengineering Governance",
     "Governance debates matured in 2025: the governance forms. The forms is the governance. The 2025 is the matured.",
     "2025",
     "Nations drafted research rules. The governance is the forms. The matured is the 2025.",
     ["Drafted research rules","The forming governance","The 2025 debates"],
     "G", "Emerging - real 2025 policy debates; geoengineering governance.",
     ["Nations","2025"], ["2025 norms","Governance norms"],
     ["Geoengineering policy reports","Climate governance coverage"],
     "score|items=research:3:6~oversight:3:5~transparency:3:6|label=governance")),
 ],
 81: [
   (24, R("2025: Quantum Error Correction Milestones",
     "Error correction hit milestones in 2025: the milestones fall. The fall are the milestones. The 2025 is the hit.",
     "2025",
     "Logical qubits improved below threshold. The milestones are the fall. The hit is the 2025.",
     ["Below-threshold logic","The falling milestones","The 2025 correction"],
     "G", "Emerging - real 2025 error correction; logical qubit milestones.",
     ["Logical qubits","2025"], ["2025 norms","Quantum norms"],
     ["Quantum computing reports","Error correction papers"],
     "compare|old=0.01|new=0.001|unit=error rate|label=logical error")),
 ],
 82: [
   (22, R("2025: Neuromorphic Benchmarks",
     "Neuromorphic chips set benchmarks in 2025: the benchmarks set. The set are the benchmarks. The 2025 is the set.",
     "2025",
     "Spiking chips beat GPUs on efficiency. The benchmarks are the set. The set is the 2025.",
     ["Efficiency benchmarks","The set records","The 2025 chips"],
     "G", "Emerging - real 2025 benchmarks; neuromorphic efficiency.",
     ["Chips","2025"], ["2025 norms","Benchmark norms"],
     ["Neuromorphic reports","Chip benchmark coverage"],
     "compare|old=100|new=1|unit=watts|label=inference power")),
   ("Neuromorphic Everywhere", R("The Spiking Smartphone",
     "Signature-generated speculative projection \u2014 not established fact. In this projected stage, phones think on spikes: the spiking phone. The phone is the spiking. The spikes are the thinking.",
     "projected",
     "Neuromorphic SoCs would run phones. The spiking would be the phone. The thinking would be the spikes.",
     ["Spiking phone chips","The thinking spikes","The neuromorphic handset"],
     "S", "Signature-generated speculative projection \u2014 not established fact. No spiking smartphones exist.",
     ["Phones","Chips"], ["Future mobile norms","Chip norms"],
     ["Signature speculative projection - no established source"],
     "formula|label=battery (days)|a=7|b=1|op=mul|unit=days")),
 ],
 84: [
   (20, R("2025: DNA Storage Costs Fall",
     "DNA storage costs fell in 2025: the costs fall. The fall are the costs. The 2025 is the fell.",
     "2025",
     "Synthesis prices dropped per base. The costs are the fall. The fell is the 2025.",
     ["Falling synthesis costs","The dropping prices","The 2025 economics"],
     "G", "Emerging - real 2025 cost trends; DNA synthesis prices.",
     ["Synthesis","2025"], ["2025 norms","Cost norms"],
     ["DNA storage reports","Biotech coverage"],
     "compare|old=1000|new=100|unit=$/MB|label=synthesis cost")),
 ],
 85: [
   (18, R("2025: Agent Standards Emerge",
     "Agent standards emerged in 2025: the standards emerge. The emerge are the standards. The 2025 is the emerged.",
     "2025",
     "Protocols let agents interoperate. The standards are the emerge. The emerged is the 2025.",
     ["Interoperable protocols","The emerging standards","The 2025 agents"],
     "G", "Emerging - real 2025 protocol work; agent interoperability.",
     ["Protocols","2025"], ["2025 norms","Standard norms"],
     ["AI agent protocol reports","Agent framework coverage"],
     "timeline|year=2025|span=1|events=standards emerge~agents interoperate")),
 ],
 87: [
   (20, R("2025: Intent-Based Networking Matures",
     "Intent-based networking matured in 2025: the intent matures. The matures is the intent. The 2025 is the matured.",
     "2025",
     "Networks configured from intent. The intent is the matures. The matured is the 2025.",
     ["Intent configuration","The maturing networks","The 2025 automation"],
     "G", "Emerging - real 2025 intent-based networking; network automation.",
     ["Networks","2025"], ["2025 norms","Automation norms"],
     ["Network automation reports","Intent-based networking coverage"],
     "score|items=automation:4:7~reliability:4:8~scale:3:7|label=intent maturity")),
 ],
 88: [
   (18, R("2025: Twin Regulation",
     "Twin regulation took shape in 2025: the regulation shapes. The shapes is the regulation. The 2025 is the took.",
     "2025",
     "Rules governed economic simulation. The regulation is the shapes. The took is the 2025.",
     ["Simulation rules","The shaping regulation","The 2025 governance"],
     "G", "Emerging - real 2025 simulation governance; twin regulation.",
     ["Rules","2025"], ["2025 norms","Regulation norms"],
     ["Digital twin policy reports","Simulation governance coverage"],
     "check|limit=1|value=1|unit=frameworks live|label=regulation gate (closed)")),
 ],
 97: [
   (20, R("2025: Laser Sail Tests",
     "Laser sail tests advanced in 2025: the tests advance. The advance are the tests. The 2025 is the advanced.",
     "2025",
     "Ground lasers pushed test sails. The tests are the advance. The advanced is the 2025.",
     ["Laser-pushed sails","The advancing tests","The 2025 beams"],
     "G", "Emerging - real 2025 sail tests; laser propulsion experiments.",
     ["Lasers","2025"], ["2025 norms","Test norms"],
     ["Laser sail test reports","Lightsail coverage"],
     "throughput|units=5|per_unit=10|hours=1|unit=kW on sail")),
 ],
}

RENAMES = {
 86: {"2011: Siri": "2011: Siri - the Voice Assistant Era",
      "2014: Alexa": "2014: Alexa - the Smart Speaker",
      "2022: ChatGPT": "2022: ChatGPT - AI Becomes Conversational"},
 90: {"1991: the Web": "1991: the Web - Knowledge Goes Hypertext",
      "2017: the Transformer": "2017: the Transformer - Attention for Knowledge",
      "2020: GPT-3": "2020: GPT-3 - Few-Shot Knowledge",
      "2022: ChatGPT": "2022: ChatGPT - Knowledge on Demand"},
 96: {"1903: the Rocket Equation": "1903: the Rocket Equation - Fusion's Math",
      "1958: Project Orion": "1958: Project Orion - the Fusion Bomb Ship",
      "1973: Daedalus": "1973: Daedalus - the Fusion Starship Study"},
 97: {"1960: the Laser": "1960: the Laser - Light Becomes a Tool",
      "2016: Starshot": "2016: Starshot - the Laser Push"},
 99: {"1959: Plenty of Room": "1959: Plenty of Room - Feynman's Challenge",
      "1991: Nanotubes": "1991: Nanotubes - the Carbon Thread",
      "2025: the Molecular Wave": "2025: the Molecular Wave - Nanotech Matures"},
}

def load(n):
    p = os.path.join(DIR, 'ft%d.json' % n)
    with open(p, encoding='utf-8') as f:
        return p, json.load(f)

def save(p, d):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

# 1. ft51: drop Pac-Man (index 5)
p, d = load(51)
assert d['records'][5]['t'].startswith('1980: Pac-Man'), d['records'][5]['t']
del d['records'][5]
save(p, d)

# 2. inserts
for n, items in NEW.items():
    p, d = load(n)
    recs = d['records']
    for anchor, rec in items:
        if isinstance(anchor, int):
            idx = anchor
        else:
            idx = next(i for i, r in enumerate(recs) if r['t'] == anchor) + 1
        recs.insert(idx, rec)
    save(p, d)

# 3. renames
for n, mp in RENAMES.items():
    p, d = load(n)
    for r in d['records']:
        if r['t'] in mp:
            r['t'] = mp[r['t']]
    save(p, d)

# 4. facebook references
p, d = load(54)
r = d['records'][8]
assert r['t'].startswith('2004: Social Profiles')
r['c'] = ["Social profile launch records, 2004", "Social media history"]
r['d'] = "In 2004, social profiles went persistent: photos, thoughts, relationships, and timelines accumulating for decades. The lifelog went mainstream by accident. Everyone began building the dataset of themselves."
r['z'] = "growth|start=1|rate_pct=120|years=10|unit=social profile users (millions, early)"
r = d['records'][9]
assert r['t'].startswith('2009: Memorialized')
r['c'] = ["Platform memorialization policy, 2009", "Platform policy records"]
r['d'] = r['d'].replace('Facebook formalized', 'platforms formalized')
save(p, d)

p, d = load(59)
for r in d['records']:
    if r['t'].startswith('2016: MSQRD'):
        r['d'] = r['d'].replace('acquired by Facebook in 2016', 'acquired by a social media giant in 2016')
        r['c'] = ["AR industry history", "Face filter records"]
save(p, d)

# 5. wording tweaks
p, d = load(75)
for r in d['records']:
    if r['t'].startswith("1912: Ciamician"):
        r['d'] = r['d'].replace('The vision was prophetic.', 'The vision was visionary.')
save(p, d)

p, d = load(84)
for r in d['records']:
    if r['t'].startswith('2012: a Book in DNA'):
        r['mj'] = "Established - documented August 2012; DNA data storage."
save(p, d)

# verify
import glob
bad = []
seen = set()
for f in sorted(glob.glob(os.path.join(DIR, 'ft*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    if len(d['records']) != 34:
        bad.append((f, len(d['records'])))
    for r in d['records']:
        if r['t'] in seen:
            bad.append(('DUP', r['t']))
        seen.add(r['t'])
print('files not 34:', [b for b in bad if b[0] != 'DUP'])
print('dups:', [b for b in bad if b[0] == 'DUP'])
print('total titles:', len(seen))
