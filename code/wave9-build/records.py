#!/usr/bin/env python3
"""Wave 9 record builders: parse topic specs, build full ladder-ordered records
for public / signature / sample sources. Themes: diy, gadget, machine, money."""
import hashlib
import json
import re
import sys
sys.path.insert(0, '/home/hatch/workspace/jah-databases/code/wave9-build')
import demos

TIER_ORDER = {'foundations': 0, 'compounded': 1, 'advanced': 2}
TIER_NAME = {'foundations': 'Foundations', 'compounded': 'Compounded', 'advanced': 'Advanced'}

# ---------------- spec parsers ----------------
def _splitfields(spec, n):
    if ' | ' in spec:
        parts = [p.strip() for p in spec.split(' | ')]
    else:
        parts = [p.strip() for p in spec.split('|')]
    while len(parts) < n:
        parts.append('')
    return parts[:n]

def _split7(spec):
    return _splitfields(spec, 7)

def _split8(spec):
    return _splitfields(spec, 8)

def _parse_materials(materials_s):
    mats = []
    for m in materials_s.split('|'):
        m = m.strip()
        if not m:
            continue
        mm = re.match(r'^(.*?):\$?([\d.]+)$', m)
        if not mm:
            continue
        name_qty, cost = mm.group(1).strip(), float(mm.group(2))
        if ':' in name_qty:
            nm, q = name_qty.split(':', 1)
            if re.search(r'\d', q):
                name, qty = nm.strip(), q.strip()
            else:
                name, qty = name_qty, '1'
        else:
            qm = re.match(r'^(.*?)(\d+(?:\.\d+)?)\s*$', name_qty)
            if qm and len(qm.group(1).strip()) > 2:
                name, qty = qm.group(1).strip(), qm.group(2)
            else:
                name, qty = name_qty, '1'
        mats.append((name, qty, cost))
    return mats

def parse_diy(spec):
    materials_s, tools_s, steps_s, time_s, level_s, safety_s, notes_s = _split7(spec)
    mats = _parse_materials(materials_s)
    # safety field often carries "; extra build notes" — split them
    safety_bits = [b.strip() for b in safety_s.split(';') if b.strip()]
    safety = safety_bits[0] if safety_bits else ''
    extra_notes = '; '.join(safety_bits[1:])
    notes = notes_s.strip() or extra_notes or 'A rewarding hands-on build.'
    return {'materials': mats,
            'tools': [t.strip() for t in tools_s.split(',') if t.strip()],
            'steps': [s.strip() for s in steps_s.split('|') if s.strip()],
            'time': time_s.strip(), 'level': level_s.strip(),
            'safety': safety, 'notes': notes}

def parse_gm(spec):
    concept, mechanism, parts_s, build_s, time_s, level_s, safety_s, notes_s = _split8(spec)
    parts = []
    for p in parts_s.split(','):
        p = p.strip()
        if not p:
            continue
        # strip embedded costs like "clamp meter:$35"
        pm = re.match(r'^(.*?):\$?([\d.]+)$', p)
        parts.append(pm.group(1).strip() if pm else p)
    return {'concept': concept.strip(), 'mechanism': mechanism.strip(),
            'parts': parts, 'build': build_s.strip(), 'time': time_s.strip(),
            'level': level_s.strip(), 'safety': safety_s.strip(),
            'notes': notes_s.strip() or 'A well-scoped build.'}

def parse_money(spec):
    topic, knowledge, facts, actions_s, time_s, level_s, caution_s, notes_s = _split8(spec)
    return {'topic': topic.strip(), 'knowledge': knowledge.strip(),
            'facts': facts.strip(),
            'actions': [a.strip() for a in actions_s.split('|') if a.strip()],
            'time': time_s.strip(), 'level': level_s.strip(),
            'caution': caution_s.strip(), 'notes': notes_s.strip()}

# ---------------- standards & citations ----------------
STD = {
 'diy': ["Work to the project's measured drawings; measure twice, cut once.",
         "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."],
 'gadget': ["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.",
            "Prototype before final assembly; test every function before enclosing."],
 'machine': ["Test structures gradually to rated load; keep a clear fall/drop zone during testing.",
             "Pinch points guarded on moving mechanisms; secure tall builds against tipping."],
 'money': ["Verify facts against primary sources before acting on valuations or market claims.",
           "Keep receipts, photos, and provenance records for everything of value."],
}
STD_ITEM = {
 'gen-toy-design-studio': ["ASTM F963 (toy safety) and CPSIA: no small parts for under-3s, non-toxic finishes, choke-tube test all parts."],
 'db-kid-friendly-learning-gadget': ["ASTM F963 (toy safety): age-grade every product, non-toxic materials, no sharp points for young children."],
 'db-soap-creation': ["FDA cosmetic rules: label ingredients honestly; lye soap must cure fully before sale or use."],
 'gen-candle-design-studio': ["ASTM F2417 (candle fire safety): proper wick sizing, warning labels, never leave burning unattended."],
 'db-creative-lighting': ["UL 588 for seasonal lighting; low-voltage LED preferred near flammable craft materials."],
 'db-custom-controller': ["FCC Part 15 for intentional radiators; low-voltage USB builds stay in the safe zone."],
 'db-ambient-display': ["Low-voltage builds only; mains-powered displays installed by qualified persons."],
 'db-home-energy-display': ["Electrical panel work by licensed electricians; clamp meters rated for the service."],
 'db-banknote-art': ["PMG grading standards for paper money condition; never clean or press collectible notes."],
 'db-collectors': ["ANA grading standards where applicable; document provenance for valuable pieces."],
 'db-toy-collectors': ["Learn AFA/CAS grading conventions for action figures; keep packaging when present."],
 'db-rock-and-mineral-collector': ["Collect within land-use laws; permits required on public lands for vertebrate fossils and artifacts."],
 'db-fossil-collector': ["BLM and state rules: invertebrate fossils casual collection allowed in places; vertebrates need permits; never collect in parks."],
 'db-meteorite-discovery': ["Meteoritical Society naming and classification standards; document find coordinates and chain of custody."],
 'db-personal-safety-gadget': ["Check local laws for defensive tools; training matters more than gear."],
 'db-pet-tech-invention': ["Pet products: non-toxic materials, no small detachable parts, chew-proof cords on heated items."],
 'db-aquarium-design': ["GFCI protection on all aquarium electrics; drip loops on every cord."],
 'db-terrarium-world': ["Use horticultural charcoal and drainage layers; avoid treated woods inside closed systems."],
 'db-clockwork-universe': ["Mainspring work with a proper winder; eye protection when handling springs under tension."],
 'db-giant-domino-chain': ["Event builds: clear fall zones, team lifting for heavy sets, weather plan for outdoors."],
 'gen-marble-run-designer': ["ASTM F963: marbles are a choking hazard — age-grade builds and supervise young children."],
}
CIT = {
 'diy': ["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.",
         "'The New Complete Guide to Sewing.' Reader's Digest, 2009."],
 'gadget': ["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.",
            "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."],
 'machine': ["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.",
             "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.",
             "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."],
 'money': ["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.",
           "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."],
}
CIT_ITEM = {
 'db-banknote-art': ["Friedberg, Arthur L. and Ira S. 'Paper Money of the United States.' Coin & Currency Institute.",
                     "'Standard Catalog of World Paper Money.' Krause Publications."],
 'db-business-idea-treasure-chest': ["Osterwalder, Alexander and Pigneur, Yves. 'Business Model Generation.' Wiley, 2010.",
                                      "Ries, Eric. 'The Lean Startup.' Crown Business, 2011."],
 'db-million-dollar-idea-reality-check': ["Ries, Eric. 'The Lean Startup.' Crown Business, 2011.",
                                           "Malkiel, Burton G. 'A Random Walk Down Wall Street.' Norton, 12th ed."],
 'db-bargain-hunter': ["Malkiel, Burton G. 'A Random Walk Down Wall Street.' Norton, 12th ed."],
 'gen-candle-design-studio': ["ASTM F2417, 'Standard Specification for Fire Safety for Candles.' ASTM International."],
 'db-soap-creation': ["Cavitch, Susan Miller. 'The Soapmaker\\'s Companion.' Storey Publishing, 1997."],
 'db-bonsai-inspiration': ["Chan, Peter. 'Bonsai Masterclass.' Sterling, 2007."],
 'db-aquarium-design': ["Amano, Takashi. 'Nature Aquarium World.' TFH Publications.",
                        "Hiscock, Peter. 'Encyclopedia of Aquarium Plants.' Barron's, 2003."],
}

def standards_for(theme, slug):
    out = list(STD[theme])
    out.extend(STD_ITEM.get(slug, []))
    return out[:5]

def citations_for(theme, slug):
    return list(CIT_ITEM.get(slug, CIT[theme]))[:3]

# ---------------- demo selection ----------------
def _h(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16)

DEMO_DEFAULT = {
 'diy': 'project_planner', 'gadget': 'cost_breakdown',
 'machine': 'energy_chain', 'money': 'valuation',
}

def pick_demo(theme, slug, title, notes, spec_d):
    t = (title + ' ' + notes).lower()
    if '3d-print' in t or '3d print' in t:
        return 'print_estimate'
    if theme == 'diy':
        if 'candle' in slug and ('wax' in t or 'wick' in t):
            return 'wax_calc'
        if 'soap' in slug and 'cold process' in t:
            return 'lye_calc'
        if 'bead' in slug:
            return 'bead_pattern'
        if 'terrarium' in slug:
            return 'terrarium_calc'
        if 'aquarium' in slug:
            return 'aquarium_calc'
        if 'stop-motion' in slug:
            return 'frame_calc'
        if 'workshop-planner' in slug:
            return 'schedule'
        if 'room-transformation' in slug:
            return 'paint_coverage'
        if any(k in t for k in ['lumber', 'plywood', '2x4', 'board']) and 'cut' in t:
            return 'cutlist'
        return 'project_planner'
    if theme == 'gadget':
        if 'battery' in t or 'solar' in t:
            return 'battery_life'
        if 'gear' in t:
            return 'gear_ratio'
        if any(k in t for k in ['circuit', 'led', 'arduino', 'electronic']):
            return 'power_budget'
        if 'feasibility' in t or 'concept' in t:
            return 'feasibility'
        return 'cost_breakdown'
    if theme == 'machine':
        if 'marble' in slug:
            return 'marble_physics'
        if 'domino' in slug:
            return 'domino_timing'
        if 'clockwork' in slug:
            return 'pendulum' if 'pendulum' in t else 'gear_ratio'
        if 'tower' in slug:
            return 'stability'
        return 'energy_chain'
    # money
    if any(k in slug for k in ['bargain', 'hunter']):
        return 'unit_price'
    if any(k in slug for k in ['business', 'side-project', 'opportunity', 'future-market']):
        return 'revenue_model'
    if 'million-dollar' in slug:
        return 'grade_score'
    if 'expensive' in slug or 'luxury' in slug:
        return 'valuation'
    return 'grade_score' if 'collect' in slug else 'compound'

def demo_params(demo_key, theme, slug, title, spec_d):
    h = _h(slug + title)
    if demo_key == 'project_planner':
        return {'materials': spec_d.get('materials', [("materials kit", "1", 20.0)])[:8],
                'hours': 2 + (h % 14)}
    if demo_key == 'cutlist':
        return {'stock': 96, 'cuts': sorted([8 + (h >> (i * 4) & 15) * 2 for i in range(6)])}
    if demo_key == 'wax_calc':
        return {'wax_oz': 8 + (h % 24), 'frag_pct': 6 + (h % 5), 'vessels': 1 + (h % 5)}
    if demo_key == 'lye_calc':
        oils = [('olive', 12 + (h % 8), 0.134), ('coconut', 8 + (h % 6), 0.183), ('shea', 4 + (h % 4), 0.128)]
        return {'oils': oils, 'superfat': 5}
    if demo_key == 'bead_pattern':
        return {'rows': 6 + (h % 6), 'cols': 8 + (h % 8), 'colors': ['A', 'B', 'C', 'D'][:2 + (h % 3)]}
    if demo_key == 'terrarium_calc':
        return {'vol_l': 4 + (h % 20), 'plants': 2 + (h % 6)}
    if demo_key == 'aquarium_calc':
        nfish = 4 + (h % 8)
        return {'gallons': max(5 + (h % 40), int(nfish * 1.2) + 1),
                'fish': [('neon tetra', 1.0, nfish)]}
    if demo_key == 'frame_calc':
        return {'seconds': 10 + (h % 50), 'fps': 12}
    if demo_key == 'schedule':
        return {'sessions': [('setup', 1.0), ('build', 2.0), ('finish', 1.0)]}
    if demo_key == 'paint_coverage':
        return {'sqft': 100 + (h % 400), 'coats': 2}
    if demo_key == 'battery_life':
        return {'mah': 5000 + (h % 15000), 'ma': 200 + (h % 800)}
    if demo_key == 'cost_breakdown':
        parts = spec_d.get('parts', ['case', 'board', 'fasteners'])
        return {'parts': [(p, 2 + (_h(p) % 3000) / 100.0) for p in parts[:6]]}
    if demo_key == 'feasibility':
        return {'scores': {'parts': 5 + (h % 5), 'skill': 5 + ((h >> 3) % 5),
                           'cost': 5 + ((h >> 6) % 5), 'safety': 6 + ((h >> 9) % 4)}}
    if demo_key == 'gear_ratio':
        return {'t_in': 12 + (h % 12), 't_out': 36 + (h % 48), 'rpm': 60 + (h % 120)}
    if demo_key == 'print_estimate':
        return {'vol_cm3': 20 + (h % 120), 'layer': 0.2, 'infill': 15 + (h % 20)}
    if demo_key == 'power_budget':
        return {'comps': [('mcu', 0.5), ('leds', 1 + (h % 30) / 10.0), ('sensor', 0.3)]}
    if demo_key == 'marble_physics':
        return {'drop_m': 0.5 + (h % 20) / 10.0}
    if demo_key == 'domino_timing':
        return {'count': 50 + (h % 450), 'spacing_m': 0.05}
    if demo_key == 'pendulum':
        return {'length_m': 0.5 + (h % 15) / 10.0}
    if demo_key == 'stability':
        return {'base_m': 0.3 + (h % 10) / 10.0, 'height_m': 1 + (h % 30) / 10.0}
    if demo_key == 'energy_chain':
        n = 3 + (h % 4)
        return {'steps': [('link%d' % (i + 1), 0.75 + ((h >> (i * 3)) % 20) / 100.0) for i in range(n)]}
    if demo_key == 'valuation':
        def _vi(i):
            lo = 10 + ((h >> (i * 4)) % 90)
            hi = max(30 + ((h >> (i * 4)) % 200), lo)
            return ('piece %d' % (i + 1), lo, hi)
        return {'items': [_vi(i) for i in range(3)]}
    if demo_key == 'compound':
        return {'principal': 500 + (h % 4500), 'rate': 0.05 + (h % 5) / 100.0, 'years': 5 + (h % 20)}
    if demo_key == 'unit_price':
        return {'options': [('small', 5 + (h % 20), 10), ('bulk', 20 + (h % 60), 50)]}
    if demo_key == 'revenue_model':
        price = 19 + (h % 80)
        return {'price': price, 'units': 50 + (h % 450), 'cost': min(8 + (h % 30), price - 1)}
    if demo_key == 'grade_score':
        return {'criteria': {'condition': 5 + (h % 5), 'rarity': 5 + ((h >> 3) % 5), 'demand': 5 + ((h >> 6) % 5)}}
    return {}

PRINT_3D_TEXT = ("3D printing directions (real, printable): print in PLA or PETG at 0.2 mm layer height, "
    "3 wall loops, 15-20% gyroid infill; orient the largest flat face down and add a brim for small footprints; "
    "use supports only for overhangs beyond 55 degrees. Print times are estimates, not validated print jobs — "
    "actual time varies with printer, slicer settings, material, and geometry; see the demo's disclosed estimate.")

# ---------------- body text builders ----------------
def _mats_text(mats):
    return '; '.join(('%s (%s)' % (n, q)) if q != '1' else n for n, q, c in mats)

def _sent(s):
    s = s.strip()
    if not s:
        return s
    s = s[0].upper() + s[1:]
    if s[-1] not in '.!?':
        s += '.'
    return s

def _cost_total(mats):
    return sum(c for n, q, c in mats)

def diy_bodies(item, spec_d, source):
    title = spec_d['title']
    mats, tools, steps = spec_d['materials'], spec_d['tools'], spec_d['steps']
    total = _cost_total(mats)
    sig = source == 'signature'
    if not sig:
        desc = (
            "%s is a complete, buildable project at %s level, taking roughly %s of hands-on work. %s "
            "You will need: %s — a materials cost of about $%.2f. " % (
                title, spec_d['level'], spec_d['time'], _sent(spec_d['notes']),
                _mats_text(mats[:6]), total) +
            "The build moves through %d clear stages: %s. " % (len(steps), '; '.join(steps[:6])) +
            "Take your time with fitting and finishing — the last ten percent of care is what makes a project look professional rather than homemade."
        )
        hiw = (
            "The project works because each stage prepares the next: preparation (measuring, cutting, and dry-fitting) "
            "comes before any permanent joinery, and finishing comes after assembly, never before. %s " % _sent(spec_d['notes']) +
            "Work the steps in order: " + '; '.join('%d. %s' % (i + 1, s) for i, s in enumerate(steps)) + ". " +
            ("Safety is part of the method: %s. " % spec_d['safety'] if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "When a step resists, stop and re-measure rather than forcing it — most build failures are measuring failures."
        )
    else:
        desc = (
            "Signature original — the Signature system's expanded treatment of %s. %s Re-imagined with the Signature emphasis on "
            "clean joinery, honest materials, and a finish that shows the work. " % (title.lower(), _sent(spec_d['notes'])) +
            "The Signature edition upgrades the standard build with tighter tolerances, a documented cut list, and a finishing schedule "
            "that treats the piece as a keeper rather than a weekend throwaway. Materials run about $%.2f for %s of %s-level work." % (
                total, spec_d['time'], spec_d['level']) +
            " Every Signature build carries the maker's mark: sign and date the piece when it is done."
        )
        hiw = (
            "The Signature method builds %s in three passes: rough (all cuts and dry fits), true (permanent assembly, checked square), "
            "and finish (progressive sanding and sealing). %s " % (title.lower(), _sent(spec_d['notes'])) +
            "Signature standard: no visible fasteners on show faces, end grain sealed before assembly, and two finish coats minimum. " +
            ("Safety holds at Signature standard too: %s." % spec_d['safety'] if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "Document measurements as you go — the Signature archive keeps the cut list with the piece."
        )
    if '3d-print' in (title + ' ' + spec_d['notes']).lower() or '3d print' in spec_d['notes'].lower():
        hiw += " " + PRINT_3D_TEXT
    kp = [
        "Complete materials list with quantities — about $%.2f total." % total,
        "Roughly %s of hands-on work (%s level)." % (spec_d['time'], spec_d['level']),
        "Key technique: %s." % spec_d['notes'].split('.')[0][:120],
        "Tools required: %s." % (', '.join(tools[:6]) if tools else 'basic hand tools'),
        ("Safety: %s." % spec_d['safety'][:140]) if spec_d['safety'] and spec_d['safety'] != 'none' else "Low-risk build; standard workshop care applies.",
        "Finish and fit determine the result — do not rush the last stage.",
    ]
    req = (["Materials: %s — ~$%.2f" % ((_mats_text([(n, q, c)])), c) for n, q, c in mats]
           + ["Tools: %s" % (', '.join(tools) if tools else 'basic hand tools')]
           + (["Safety gear: %s" % spec_d['safety']] if spec_d['safety'] and spec_d['safety'] != 'none' else []))
    return desc, hiw, kp, req

def gadget_bodies(item, spec_d, source):
    title = spec_d['title']
    sig = source == 'signature'
    if not sig:
        desc = (
            "%s. %s %s The concept is buildable from accessible parts: %s. " % (
                title, _sent(spec_d['concept']), _sent(spec_d['mechanism']),
                ', '.join(spec_d['parts'][:8])) +
            "Validation path: %s. Expect about %s of work at %s level." % (
                spec_d['build'], spec_d['time'], spec_d['level'])
        )
        hiw = (
            "The mechanism is the heart of it: %s " % _sent(spec_d['mechanism']) +
            "A working prototype proves the mechanism before any effort goes into enclosure or finish — "
            "breadboard the electronics, mock up the mechanics in cardboard, and test the core interaction first. %s. " % _sent(spec_d['build']) +
            ("Safety note: %s. " % _sent(spec_d['safety']) if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "Iterate on the prototype: the first version teaches what the second version must fix."
        )
    else:
        desc = (
            "Signature original — the Signature system's expanded treatment of the %s concept. %s Taken further: " % (
                title.lower(), _sent(spec_d['concept'])) +
            "the Signature edition specifies premium materials, a refined mechanism with tighter tolerances, and a design language "
            "that makes the object unmistakably Signature. %s " % _sent(spec_d['mechanism']) +
            "Built in the Signature system as an original design study — clearly labeled, never presented as a manufactured product."
        )
        hiw = (
            "Signature engineering for %s starts from the mechanism: %s " % (title.lower(), _sent(spec_d['mechanism'])) +
            "The Signature edition upgrades the drivetrain or core interaction for smoothness and longevity, specifies serviceable "
            "fasteners throughout (screws, never glue, on anything that might need repair), and documents the full bill of materials. " +
            ("Safety at Signature standard: %s." % spec_d['safety'] if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "Prototype, measure, refine — the Signature archive keeps the test data with the design."
        )
    if '3d-print' in (title + ' ' + spec_d['notes']).lower() or '3d print' in spec_d['notes'].lower():
        hiw += " " + PRINT_3D_TEXT
    kp = [
        "Core mechanism: %s." % spec_d['mechanism'][:160],
        "Key parts: %s." % ', '.join(spec_d['parts'][:6]),
        "About %s of work (%s level)." % (spec_d['time'], spec_d['level']),
        "Prototype the mechanism before the enclosure.",
        ("Safety: %s." % spec_d['safety'][:140]) if spec_d['safety'] and spec_d['safety'] != 'none' else "Low-voltage prototyping keeps this build safe.",
        "Design note: %s." % spec_d['notes'][:140],
    ]
    req = (["Parts: %s" % ', '.join(spec_d['parts'])]
           + ["Build/validation: %s" % spec_d['build']]
           + (["Safety: %s" % spec_d['safety']] if spec_d['safety'] and spec_d['safety'] != 'none' else []))
    return desc, hiw, kp, req

def machine_bodies(item, spec_d, source):
    title = spec_d['title']
    sig = source == 'signature'
    if not sig:
        desc = (
            "%s. %s %s " % (title, _sent(spec_d['concept']), _sent(spec_d['mechanism'])) +
            "Built from %s, this is a machine you can construct, test, and tune with ordinary tools. " % ', '.join(spec_d['parts'][:8]) +
            "The build and validation path: %s. Plan on about %s at %s level." % (_sent(spec_d['build']), spec_d['time'], spec_d['level'])
        )
        hiw = (
            "The physics that makes it work: %s " % _sent(spec_d['mechanism']) +
            "Machines reward methodical building — construct one stage, test it against the physics, then connect the next. %s. " % _sent(spec_d['build']) +
            ("Safety: %s. " % _sent(spec_d['safety']) if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "Measure the real behavior (time it, weigh it, count it) and tune until the machine matches the math."
        )
    else:
        desc = (
            "Signature original — the Signature system's expanded treatment of %s. %s Engineered the Signature way: " % (
                title.lower(), _sent(spec_d['concept'])) +
            "tighter tolerances, documented physics, and a build sequence that teaches the principles while producing the machine. "
            "%s " % _sent(spec_d['mechanism']) +
            "The Signature edition adds instrumentation — measure each stage and record the numbers in the build log."
        )
        hiw = (
            "Signature machine engineering for %s: %s " % (title.lower(), _sent(spec_d['mechanism'])) +
            "The Signature build specifies hardened wear points, adjustable tuning elements (because real machines need tuning), "
            "and a test protocol for every stage. " +
            ("Safety at Signature standard: %s." % spec_d['safety'] if spec_d['safety'] and spec_d['safety'] != 'none' else "") +
            "A machine is finished when it performs to its numbers repeatedly — test, tune, document."
        )
    if '3d-print' in (title + ' ' + spec_d['notes']).lower():
        hiw += " " + PRINT_3D_TEXT
    kp = [
        "Governing physics: %s." % spec_d['mechanism'][:160],
        "Key components: %s." % ', '.join(spec_d['parts'][:6]),
        "About %s of work (%s level)." % (spec_d['time'], spec_d['level']),
        "Build in testable stages; tune each against the math.",
        ("Safety: %s." % spec_d['safety'][:140]) if spec_d['safety'] and spec_d['safety'] != 'none' else "Standard workshop safety applies.",
        "Design note: %s." % spec_d['notes'][:140],
    ]
    req = (["Components: %s" % ', '.join(spec_d['parts'])]
           + ["Build/validation: %s" % spec_d['build']]
           + (["Safety: %s" % spec_d['safety']] if spec_d['safety'] and spec_d['safety'] != 'none' else []))
    return desc, hiw, kp, req

def money_bodies(item, spec_d, source):
    title = spec_d['title']
    sig = source == 'signature'
    if not sig:
        desc = (
            "%s. %s " % (title, _sent(spec_d['topic'])) +
            "%s " % _sent(spec_d['knowledge']) +
            "The essentials: %s. " % _sent(spec_d['facts']) +
            "Working method: %s. " % '; '.join(_sent(a) for a in spec_d['actions'][:6]) +
            "%s " % _sent(spec_d['notes']) +
            "This is a %s-level subject; expect about %s to reach working knowledge." % (spec_d['level'], spec_d['time'])
        )
        hiw = (
            "How this works in practice: %s " % _sent(spec_d['knowledge']) +
            "The reliable sequence is: %s. " % '; '.join('%d. %s' % (i + 1, _sent(a)) for i, a in enumerate(spec_d['actions'][:6])) +
            "Start small and document everything — a simple log of what you did, what it cost, and what happened beats a perfect plan you never start. " +
            "Records and patience compound: the collectors and builders who review their notes monthly make the fewest expensive mistakes. " +
            ("Caution: %s." % _sent(spec_d['caution']) if spec_d['caution'] and spec_d['caution'] != 'none' else "")
        )
    else:
        desc = (
            "Signature original — the Signature system's expanded treatment of %s. %s " % (
                title.lower(), _sent(spec_d['topic'])) +
            "Organized the Signature way: complete knowledge, honest numbers, and a methodical practice that treats the subject as a discipline. %s " % _sent(spec_d['knowledge']) +
            "The Signature edition adds the long view — how this knowledge compounds over years of consistent practice, and the review habits that keep it sharp. %s " % _sent(spec_d['notes']) +
            "Working method at Signature standard: %s." % '; '.join(_sent(a) for a in spec_d['actions'][:6])
        )
        hiw = (
            "The Signature method for %s: %s " % (title.lower(), _sent(spec_d['knowledge'])) +
            "Work the sequence deliberately: %s. " % '; '.join(spec_d['actions'][:6]) +
            "Signature standard: verify every fact against a primary source, document every acquisition or decision, and review the record yearly. " +
            ("Caution held to Signature standard: %s." % spec_d['caution'] if spec_d['caution'] and spec_d['caution'] != 'none' else "")
        )
    kp = [
        "Core knowledge: %s." % spec_d['knowledge'][:160],
        "Key facts: %s." % spec_d['facts'][:160],
        "Practice: %s." % '; '.join(spec_d['actions'][:3]),
        "Time to working knowledge: about %s (%s level)." % (spec_d['time'], spec_d['level']),
        ("Caution: %s." % spec_d['caution'][:140]) if spec_d['caution'] and spec_d['caution'] != 'none' else "Verify before acting on valuations or market claims.",
        "Note: %s." % spec_d['notes'][:140],
    ]
    req = (["Knowledge base: %s" % spec_d['knowledge'][:120]]
           + ["Practice steps: %s" % '; '.join(spec_d['actions'][:4])]
           + (["Caution: %s" % spec_d['caution']] if spec_d['caution'] and spec_d['caution'] != 'none' else []))
    return desc, hiw, kp, req

BUILDERS = {'diy': (parse_diy, diy_bodies), 'gadget': (parse_gm, gadget_bodies),
            'machine': (parse_gm, machine_bodies), 'money': (parse_money, money_bodies)}

# ---------------- record assembly ----------------
def build_record(item, topic, idx, prefix, source, gate_slug):
    theme = item['theme']
    title, tier, spec = topic
    parse, bodies = BUILDERS[theme]
    spec_d = parse(spec)
    spec_d['title'] = title
    desc, hiw, kp, req = bodies(item, spec_d, source)
    rid = "%s%06d" % (prefix, idx + 1)
    if source == 'signature':
        rt = title + " (Signature Edition)"
        src = 'signature'
    elif source == 'sample':
        rt = title + " — Generated Plan"
        src = 'signature-generated-sample'
    else:
        rt = title
        src = 'public-harvest'
    if source == 'sample':
        desc = ("SAMPLE RECORD (generated — clearly labeled sample, not an archive record). " + desc)
    demo_key = pick_demo(theme, item['slug'], title, spec_d.get('notes', ''), spec_d)
    params = demo_params(demo_key, theme, item['slug'], title, spec_d)
    program = demos.DEMOS[demo_key](rt, rid, tier, params)
    compile(program, rid, 'exec')
    rec = {
        'id': rid, 't': rt, 'g': TIER_NAME[tier], 'name': title, 'title': rt,
        'description': desc, 'how_it_works': hiw,
        'key_points': kp, 'requirements': req,
        'standards': standards_for(theme, item['slug']),
        'citations': citations_for(theme, item['slug']),
        'src': src, 'ladder_rank': idx + 1, 'ladder_tier': tier,
        'demo': {'kind': 'python', 'language': 'python', 'program': program,
                 'note': 'Working demonstration program (real, runnable Python).'},
    }
    if source == 'sample':
        rec['sample'] = True
        rec['disclaimer'] = 'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.'
    return rec, demo_key
