/* JAH Emergency Preparedness Database generator — jahdb-emergency-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full emergency protocol. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable public-safety knowledge) or Signature-generated
   (homegrown drills/plans), labeled in `origin`. Never fabricates real-world facts. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'emergency';
var PREFIX = 'JAH-EMG-';
var VERSION = 'jahdb-emergency-1.0';
var RECORD_KIND = 'emergency protocol';
var CATS = ['fire-safety', 'medical-first-aid', 'natural-disaster', 'preparedness', 'safety-protocol'];

/* ================= REAL (sourced) data: [title, key_points, procedure] ================= */
var REAL_FIRE = [
['Stop, drop, and roll', 'If clothing catches fire: stop moving, drop to the ground, cover the face, and roll to smother flames', 'Stop: freeze where you are \u2014 running feeds the flames with oxygen. Drop: fall to the ground and cover your face with your hands. Roll: roll back and forth until the flames are fully out, then cool any burns with water and seek medical help.'],
['Using a fire extinguisher: PASS', 'Pull the pin; Aim at the base of the fire; Squeeze the handle; Sweep side to side', 'Pull: break the tamper seal and pull the pin. Aim: point the nozzle at the base of the flames, not the smoke. Squeeze: depress the handle to discharge. Sweep: move side to side across the base until the fire is out, and watch for re-ignition.'],
['Classes of fire', 'Class A: ordinary combustibles; B: flammable liquids; C: energized electrical; D: combustible metals; K: cooking oils', 'Identify the fuel: wood, paper, and cloth are Class A; gasoline and grease are Class B; live electrical equipment is Class C. Match the agent: water suits Class A only \u2014 never use water on grease or electrical fires. Call for help: if the fire exceeds a wastebasket in size, evacuate and call emergency services.'],
['Home fire escape planning', 'Two exits from every room; a family meeting point outside; practice twice a year', 'Draw the plan: map two ways out of every room, including windows. Set the meeting point: a fixed spot like a tree or mailbox. Practice: run the drill twice a year, at night as well as day. Teach children: show them how to check doors for heat and stay low under smoke.'],
['Smoke alarms', 'Alarms on every level, inside and outside bedrooms; test monthly', 'Install: place alarms on every level and in each bedroom area. Test monthly: press the test button. Replace: swap batteries yearly and the whole unit every ten years. Never disable: a chirping alarm needs a battery, not removal.'],
['Grease fire response', 'Never use water on a grease fire; smother it or use a Class K/B extinguisher', 'Turn off the heat if you can do so safely. Smother: slide a metal lid over the pan to starve the flames. Use baking soda for small flare-ups \u2014 never flour. Evacuate and call emergency services if it spreads beyond the pan.'],
['Escaping through smoke', 'Smoke rises; stay low, cover mouth and nose, check doors for heat', 'Get low: crawl where the air is clearer. Check doors: feel with the back of your hand \u2014 do not open a hot door. Cover airways: use a cloth over nose and mouth. Move to the exit: follow your escape plan to the meeting point.'],
['Closing doors against fire', 'A closed door slows fire and smoke dramatically; \u201cclose before you doze\u201d', 'Sleep with bedroom doors closed: it buys critical escape time. Close as you go: shut doors behind you while evacuating. Never lock yourself in: keep keys accessible and windows operable.'],
['Kitchen fire prevention', 'Never leave cooking unattended; keep flammables from burners; clean grease buildup', 'Stay in the kitchen while frying or broiling. Keep towels, paper, and curtains away from heat. Clean the stove and oven of grease regularly. Keep a lid and extinguisher within reach.'],
['Campfire and outdoor fire safety', 'Clear a wide perimeter, keep fires small, never leave unattended, drown and stir ashes cold', 'Clear the area: ten feet of bare ground around the fire. Keep it small and contained within a ring. Never leave it: even briefly. Extinguish fully: drown, stir, and feel \u2014 ashes must be cold to the touch.']
];
var REAL_MEDICAL = [
['Hands-only CPR basics', 'Call emergency services first; push hard and fast in the center of the chest', 'Call: phone emergency services and put it on speaker. Position: place the heel of your hand on the center of the chest. Compress: push hard and fast, about 2 inches deep at 100\u2013120 per minute. Continue: do not stop until help arrives or an AED is ready. Get certified: take a hands-on CPR course for full training.'],
['Using an AED', 'Turn it on and follow the voice prompts; it decides whether a shock is needed', 'Power on: open the AED and follow the voice prompts. Attach pads: place them on bare skin as diagrammed. Clear: make sure no one touches the patient during analysis. Shock if advised: press the button, then resume CPR immediately.'],
['Choking: abdominal thrusts', 'For a choking adult: stand behind, fist above the navel, quick upward thrusts', 'Ask: confirm they cannot cough, speak, or breathe. Position: stand behind and wrap your arms around the waist. Thrust: make a fist above the navel and pull sharply inward and upward. Repeat until the object clears or they become unresponsive \u2014 then call emergency services and begin CPR.'],
['Severe bleeding control', 'Direct pressure first; add dressings without removing soaked ones; tourniquet as a last resort', 'Press: apply firm direct pressure with cloth or dressing. Add: layer more dressings over soaked ones \u2014 never remove them. Elevate: raise the injury above the heart if possible. Tourniquet: for life-threatening limb bleeding, apply above the wound and note the time; get emergency help immediately.'],
['Burn first aid', 'Cool with running water; cover loosely; never pop blisters or apply ice', 'Cool: run cool (not cold) water over the burn for at least ten minutes. Cover: loosely with a clean, non-stick bandage. Don\u2019t: never pop blisters, apply ice, butter, or ointments on serious burns. Seek care: for large, deep, or face/hand burns, get medical help.'],
['Stroke: FAST', 'Face drooping; Arm weakness; Speech difficulty; Time to call emergency services', 'Face: ask them to smile \u2014 does one side droop? Arms: ask them to raise both \u2014 does one drift down? Speech: ask them to repeat a phrase \u2014 is it slurred? Time: if any sign appears, call emergency services immediately and note when symptoms started.'],
['Heart attack warning signs', 'Chest discomfort, upper-body pain, shortness of breath, cold sweat, nausea', 'Recognize: pressure or squeezing in the chest lasting minutes, pain in arms, back, neck, or jaw. Act: call emergency services immediately \u2014 do not drive yourself. Rest: sit or lie down and stay calm. Chew aspirin only if advised by emergency dispatch or your doctor.'],
['Anaphylaxis response', 'Severe allergic reaction: use an epinephrine auto-injector as prescribed, then call emergency services', 'Inject: use the prescribed auto-injector into the outer thigh through clothing if needed. Call: phone emergency services even if symptoms improve. Position: lie down with legs raised unless breathing is difficult. Second dose: a second injector may be used after 5\u201315 minutes if symptoms persist.'],
['Seizure first aid', 'Protect from injury; time it; never restrain or put anything in the mouth', 'Ease: guide them to the floor and cushion the head. Clear: move hard or sharp objects away. Time: note how long it lasts \u2014 call emergency services if over five minutes. After: roll into the recovery position once convulsions stop and stay until fully alert.'],
['Fracture and sprain care', 'Immobilize the injury; apply cold; seek medical evaluation', 'Stop: do not try to straighten a deformed limb. Immobilize: splint in the position found with padding. Cold: apply a cold pack wrapped in cloth for swelling. Elevate and get care: keep it raised and seek medical evaluation promptly.'],
['Nosebleed care', 'Lean forward, pinch the soft part of the nose, hold for 15 minutes', 'Lean forward: do not tilt the head back. Pinch: squeeze the soft lower nose shut. Hold: maintain pressure for a full 15 minutes without checking. Seek care: if bleeding persists beyond 20\u201330 minutes or follows a head injury.'],
['Heat exhaustion vs heatstroke', 'Heat exhaustion: heavy sweating, weakness; heatstroke: hot dry skin, confusion \u2014 call emergency services', 'Cool down: move to shade, loosen clothing, sip water. For exhaustion: rest and cool gradually. For heatstroke: call emergency services immediately \u2014 cool aggressively with water and ice packs to neck, armpits, and groin. Never leave someone with heatstroke alone.'],
['Hypothermia response', 'Shivering, confusion, drowsiness in the cold: warm gradually and call for help', 'Shelter: get the person out of wind and wet clothing. Warm gradually: blankets, warm drinks if alert \u2014 no alcohol. Handle gently: rough handling can trigger cardiac issues. Call: seek medical help for moderate or severe cases.'],
['Drowning response: reach or throw, don\u2019t go', 'Never swim out unless trained; extend a pole or throw a flotation device', 'Reach: extend a pole, branch, or towel from safety. Throw: toss a life ring or buoyant object. Don\u2019t go: untrained rescuers often become second victims. Call: phone emergency services and begin CPR if the person is unresponsive and not breathing.'],
['Poisoning response', 'Call poison control; do not induce vomiting unless directed', 'Identify: note what was taken and how much. Call: contact poison control or emergency services immediately. Follow: do exactly as directed \u2014 do not induce vomiting unless told to. Bring: take the container to the hospital if advised.']
];
var REAL_DISASTER = [
['Earthquake: Drop, Cover, Hold On', 'Drop to hands and knees; cover head and neck under sturdy furniture; hold on until shaking stops', 'Drop: get low before the shaking knocks you down. Cover: shelter under a sturdy table, covering head and neck. Hold on: stay put until shaking fully stops. After: check for injuries, expect aftershocks, and avoid elevators.'],
['Tsunami safety', 'After strong coastal shaking, move immediately to high ground \u2014 do not wait for warnings', 'Move: go to high ground or inland at once if shaking was strong or the sea recedes oddly. Don\u2019t wait: official warnings may not come in time. Stay: remain on high ground until authorities declare it safe \u2014 waves arrive in series.'],
['Tornado safety', 'Lowest floor, interior room, away from windows; mobile homes must be abandoned for shelter', 'Go low: descend to the lowest floor. Go in: choose an interior room or closet with no windows. Cover: protect head and neck with arms, blankets, or a mattress. Mobile homes: leave immediately for a sturdy shelter \u2014 vehicles and mobile homes are death traps in tornadoes.'],
['Hurricane preparedness', 'Know your evacuation zone; prepare supplies; secure the home before the storm', 'Know: learn your evacuation zone and routes in advance. Supply: gather water, food, medications, and documents for at least three days. Secure: board windows, bring in outdoor items, fill the tub. Leave: evacuate when ordered \u2014 never ride out a major hurricane on the coast.'],
['Flood safety: Turn Around, Don\u2019t Drown', 'Six inches of moving water can knock you down; twelve inches can float a car', 'Avoid: never walk or drive through floodwater. Turn around: find another route rather than crossing. Abandon: leave a stalled vehicle for higher ground immediately. After: avoid floodwater \u2014 it hides hazards and contamination.'],
['Lightning safety', 'When thunder roars, go indoors; avoid open fields, tall trees, and water', 'Shelter: get inside a substantial building or hard-topped vehicle. Avoid: open fields, isolated trees, and water. Wait: stay inside 30 minutes after the last thunder. If caught outside: crouch low, minimize contact with the ground.'],
['Wildfire evacuation', 'Leave early when ordered; close up the house; take the go-bag', 'Prepare: keep a go-bag and know two routes out. Leave early: do not wait for mandatory orders if fire is near. Secure: close windows and doors but leave them unlocked for firefighters. Don\u2019t return: wait for official all-clear.'],
['Blizzard survival', 'Stay with the vehicle if stranded; conserve fuel; stay visible', 'Stay: remain with the vehicle \u2014 it is your shelter. Signal: turn on hazards and hang a bright cloth on the antenna. Conserve: run the engine briefly for heat, cracking a window. Stay hydrated and move: keep blood circulating.'],
['Volcanic ash safety', 'Stay indoors; protect lungs and eyes; avoid driving in ash', 'Shelter: stay inside with windows closed. Protect: wear masks and goggles if you must go out. Avoid driving: ash clogs engines and blinds drivers. Clear: remove ash from roofs before it accumulates dangerously.'],
['Landslide warning signs', 'Unusual sounds, tilting trees, new cracks, and sudden water changes precede slides', 'Watch: heed rumbling sounds, cracking, and tilting poles or trees. Leave: evacuate immediately if you suspect a slide. Report: alert authorities about new cracks or water changes. Stay away: keep clear of the slide area afterward.']
];
var REAL_PREP = [
['Emergency kit: the basics', 'Water (1 gallon per person per day, 3 days), food, flashlight, batteries, first aid, whistle', 'Water: store one gallon per person per day for at least three days. Food: three days of non-perishable food plus a manual can opener. Tools: flashlight, extra batteries, whistle, and a basic first-aid kit. Rotate: check and refresh supplies every six months.'],
['Family emergency communication plan', 'An out-of-area contact everyone calls; a meeting place; practiced by all', 'Choose: pick an out-of-area contact every family member calls. Meet: set a neighborhood and an out-of-neighborhood meeting place. Practice: rehearse the plan, including texting when calls fail. Cards: give every member a wallet card with the numbers.'],
['Important documents kit', 'Copies of IDs, insurance, medical records, and account numbers in a waterproof container', 'Copy: duplicate IDs, policies, prescriptions, and deeds. Seal: store in a waterproof, fire-resistant container. Backup: keep encrypted digital copies offsite. Update: refresh after moves, births, and policy changes.'],
['Pet emergency preparedness', 'Pets need their own go-bag: food, water, carrier, medications, and records', 'Pack: three days of pet food and water plus bowls. Contain: a sturdy carrier or leash for each animal. Medicate: prescriptions and vaccination records. Plan: know pet-friendly shelters \u2014 most emergency shelters have limits.'],
['Car emergency kit', 'Jumper cables, spare tire, flashlight, blanket, water, and basic tools', 'Equip: jumper cables, tire gear, flashlight, and a blanket. Stock: water and snacks for delays. Tools: a basic kit plus a phone charger. Seasonal: add ice scraper or sunshade as needed.'],
['Go-bag (72-hour bag)', 'A packed bag ready to grab: documents, cash, clothes, food, water, light', 'Pack: copies of documents, cash, a change of clothes, and sturdy shoes. Sustain: three days of food and water plus a filter. Light and power: flashlight, batteries, and a charged power bank. Keep ready: store by the door and refresh twice a year.'],
['Sheltering in place', 'Stay inside with supplies when evacuation is more dangerous than remaining', 'Seal: close and lock windows and doors. Supply: gather food, water, and medications for the duration. Inform: monitor official channels for instructions. Conserve: ration power and phone battery.'],
['NOAA weather radio', 'A battery-backed weather radio gives official alerts when networks fail', 'Buy: choose a SAME-capable weather radio. Program: set your county code for local alerts. Power: keep batteries fresh and test weekly. Listen: act on watches (prepare) and warnings (act now).'],
['Power outage preparedness', 'Flashlights over candles; keep fridge closed; never run generators indoors', 'Light: use flashlights, not candles, to avoid fire. Food: keep fridge and freezer closed \u2014 food stays safe about four hours. Generator: run only outdoors, far from windows. Medical: plan for powered medical devices in advance.'],
['Water storage for emergencies', 'Store tap water in food-grade containers; rotate every six months', 'Container: use food-grade jugs, cleaned and sanitized. Fill: tap water from a treated supply needs no additives. Seal and date: label each container. Rotate: replace every six months.']
];
var REAL_SAFETY = [
['Gas leak response', 'Leave immediately; don\u2019t flip switches; call from outside', 'Leave: get everyone out at once \u2014 do not stop for belongings. Don\u2019t spark: do not flip switches, light matches, or use phones inside. Call: phone the gas company or emergency services from outside. Wait: do not re-enter until professionals declare it safe.'],
['Carbon monoxide safety', 'CO is odorless; alarms on every level; symptoms mimic flu', 'Alarm: install CO alarms on every level and near bedrooms. Symptom check: headache, dizziness, and nausea affecting multiple people means get out. Leave: evacuate to fresh air and call emergency services. Service: have fuel-burning appliances inspected yearly.'],
['Workplace fire drill', 'Know two exits, the alarm sound, and the assembly point; drills build muscle memory', 'Learn: identify two exits and the assembly point on day one. Listen: know what the alarm sounds like. Move: walk \u2014 don\u2019t run \u2014 to the assembly point and report. Improve: debrief every drill and fix the gaps.'],
['Active threat: Run, Hide, Fight', 'Run if you can; hide silently if you cannot; fight only as a last resort', 'Run: escape the area, leaving belongings, and call emergency services when safe. Hide: lock and barricade doors, silence phones, stay quiet. Fight: as a last resort, act with others to disrupt the attacker. Tell: give responders your location and descriptions.'],
['Home security basics', 'Lock doors and windows; light exteriors; know your neighbors', 'Lock: deadbolts on doors, locks on every window. Light: motion lighting deters intruders. Know: introduce yourself to neighbors and share vacation watches. Plan: rehearse what each family member does if someone breaks in.'],
['Water safety for families', 'Supervise children constantly near water; learn to swim; fence pools', 'Watch: designate a water watcher \u2014 no phones. Swim: enroll children in lessons early. Fence: four-sided pool fencing with self-closing gates. Gear: life jackets for weak swimmers and all boaters.'],
['Food safety temperatures', 'Poultry 165\u00b0F; ground meats 160\u00b0F; steaks and chops 145\u00b0F with rest; keep cold foods cold', 'Measure: use a food thermometer \u2014 color is not reliable. Hit the numbers: 165\u00b0F poultry, 160\u00b0F ground meat, 145\u00b0F whole cuts with a 3-minute rest. Chill fast: refrigerate leftovers within two hours. Separate: keep raw and ready-to-eat foods apart.'],
['Ladder safety', 'Three points of contact; 4-to-1 angle; never stand on the top rung', 'Angle: set the base one foot out for every four feet up. Contact: keep three points of contact while climbing. Top: never stand on the top two rungs. Spot: have someone foot the ladder on uneven ground.'],
['Chainsaw safety basics', 'Protective gear, firm stance, and respect for kickback', 'Gear: helmet, eye and ear protection, chaps, and boots. Stance: firm footing, saw close to the body. Kickback: never cut with the tip\u2019s upper quadrant. Maintain: a sharp, well-tensioned chain is safer.'],
['Generator safety', 'Never run a generator indoors or in a garage; keep it 20+ feet from the house', 'Outside only: exhaust kills \u2014 place generators far from windows and doors. Dry: operate on a dry surface under a canopy. Cool: let it cool before refueling. Connect: use heavy-duty outdoor cords or a transfer switch \u2014 never backfeed outlets.']
];

/* ================= Signature-generation pools ================= */
var DRILL_TOPICS = [
['Office evacuation drill','safety-protocol','A quarterly drill that moves every occupant to the assembly point in under four minutes.','Announce: notify floor wardens a week ahead, but not the exact time. Execute: sound the alarm, wardens sweep their zones, everyone walks to the assembly point. Account: wardens report headcounts to the coordinator. Debrief: log the time, note bottlenecks, and fix them before next quarter.'],
['School lockdown drill','safety-protocol','A practiced, calm lockdown that secures every classroom in ninety seconds.','Prepare: teachers review the procedure with students age-appropriately. Execute: lock doors, cover windows, move students from sight lines, silence devices. Account: teachers report status by the silent check-in system. Debrief: counselors available; refine the plan from observations.'],
['Family fire drill night','fire-safety','A twice-yearly home drill every member \u2014 including kids \u2014 can run half-asleep.','Plan: walk the two exits from each bedroom together. Practice: sound the alarm and time the escape to the meeting point. Teach: show children to stay low and never hide. Repeat: drill once in daylight, once at night.'],
['Workplace severe-weather drill','natural-disaster','Everyone reaches the shelter area before the warning expires.','Map: post shelter routes from every workstation. Execute: on the drill tone, move to the interior shelter with head cover. Account: supervisors check in their teams. Review: time the movement and clear blocked routes.'],
['Community CERT-style drill','preparedness','Neighbors practice triage, light search, and radio check-ins together.','Organize: assign teams \u2014 medical, search, communications. Execute: run a scenario with mock victims across the block. Communicate: practice radio discipline and status boards. Improve: after-action review with the fire department liaison.'],
['Kitchen fire drill at home','fire-safety','Everyone knows the grease-fire response without panicking.','Teach: demonstrate the lid-smother technique on a cold pan. Practice: each adult rehearses PASS with a training extinguisher. Drill: call out \u201cfire!\u201d and time the response. Review: check the extinguisher gauge monthly.'],
['Flood evacuation drill','natural-disaster','The household can leave for high ground with go-bags in fifteen minutes.','Pack: go-bags staged by the door, documents sealed. Route: two routes to high ground mapped and driven. Execute: on the alert, load, lock, and leave \u2014 no detours. Regroup: check in with the out-of-area contact.'],
['Power-outage weekend drill','preparedness','The family lives comfortably off-grid for 48 hours to find the gaps.','Simulate: kill the main breaker Friday evening. Live it: cook, light, and entertain without grid power. Log: write down every missing item. Fix: buy the gaps Monday \u2014 that is the whole point.'],
['First-aid skills night','medical-first-aid','A monthly hour keeping bleeding control, CPR, and choking response fresh.','Review: one skill per month on rotation. Practice: mannequins for CPR, partners for choking technique. Quiz: scenario cards \u2014 \u201cwhat do you do first?\u201d Certify: renew formal certification before it lapses.'],
['Apartment building fire drill','fire-safety','High-rise residents know stairwells, not elevators, and the refuge floors.','Learn: post stairwell maps on every floor. Execute: alarm sounds, residents descend by stairs to assembly. Assist: buddies assigned for mobility-impaired neighbors. Debrief: building management logs times and issues.'],
['Earthquake drop drill','natural-disaster','Drop, Cover, Hold On becomes reflex through monthly sixty-second drills.','Signal: a tone or shout starts the drill anywhere. Execute: drop, cover under the nearest sturdy furniture, hold on. Count: hold a full sixty seconds. Review: identify rooms with no good cover and fix them.'],
['Tornado shelter drill','natural-disaster','Everyone reaches the windowless interior room in under two minutes.','Designate: the lowest, most interior room is the shelter. Stock: helmets, shoes, and a weather radio inside. Execute: drill the move on the warning tone. Harden: reinforce the shelter space over time.'],
['Wilderness first-aid scenario','medical-first-aid','Hiking groups practice splinting, bleeding control, and evacuation decisions.','Scenario: one member plays the injured hiker each outing. Treat: splint, bandage, and assess with real gear. Decide: practice the stay-or-evacuate call. Debrief: what gear was missing? Add it.'],
['Chemical spill response drill','safety-protocol','Lab and shop teams contain a mock spill without spreading it.','Alert: announce the spill and its safety data sheet. Contain: dam the spread with absorbents from upwind. Protect: full PPE before approaching. Report: log the drill and restock the spill kit.'],
['Active-threat tabletop exercise','safety-protocol','Leadership walks through Run, Hide, Fight decisions before a crisis.','Scenario: a facilitator presents an evolving threat. Decide: the team chooses actions at each branch. Record: capture every decision and its rationale. Improve: turn lessons into updated procedures within a week.']
];
var CHECKLISTS = [
['Hurricane supply checklist','preparedness','Water, food, medications, documents, and power for a week without services.'],
['Winter storm car kit checklist','preparedness','Blanket, shovel, sand, snacks, and a charged phone for roadside survival.'],
['Baby and toddler emergency checklist','preparedness','Formula, diapers, comfort items, and pediatric medications packed to grab.'],
['Senior emergency checklist','preparedness','Medications list, mobility aids, medical contacts, and a buddy system.'],
['Pet evacuation checklist','preparedness','Carrier, food, water, records, and a pet-friendly destination confirmed.'],
['Home fireproofing checklist','fire-safety','Alarms, extinguishers, escape ladders, and cleared perimeters room by room.'],
['Wildfire defensible-space checklist','fire-safety','Thirty feet of lean, clean, and green around the home.'],
['First-aid kit restock checklist','medical-first-aid','Every item checked, dated, and replaced on a six-month cycle.'],
['Storm shelter stocking checklist','natural-disaster','Seventy-two hours of comfort and safety in the shelter space.'],
['Workplace emergency contacts checklist','safety-protocol','Every number current, posted, and tested quarterly.']
];
var PLAN_SCENARIOS = ['a week-long ice storm','a major earthquake','a chemical plant incident nearby','a dam failure upstream','a pandemic lockdown','a cyberattack on utilities','a train derailment with hazmat','a stadium evacuation','a campus emergency','a hospital surge event','a refinery fire','a flash flood at night'];
var REAL = interleave([
  REAL_FIRE.map(function (e) { return { k: 'f', e: e }; }),
  REAL_MEDICAL.map(function (e) { return { k: 'm', e: e }; }),
  REAL_DISASTER.map(function (e) { return { k: 'd', e: e }; }),
  REAL_PREP.map(function (e) { return { k: 'p', e: e }; }),
  REAL_SAFETY.map(function (e) { return { k: 's', e: e }; })
]);
function realRecord(e, id, seed, cat) {
  var secs = [
    { heading: 'Key points', body: e[0] + '. ' + e[1] + '.' },
    { heading: 'Procedure', body: e[2] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: cat, record_kind: RECORD_KIND, origin: 'sourced', summary: e[1] + '.', details: { key_points: e[1].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: standard public-safety guidance; get certified hands-on training for medical procedures.', related: [], _seed: seed };
}
function sigDrill(r, id, seed, topic) {
  var t = topic || pick(DRILL_TOPICS, r);
  var secs = [{ heading: 'The drill', body: t[0] + ' (' + t[1] + '). ' + t[2] }, { heading: 'Running it', body: t[3] }];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature drill', category: t[1], record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: t[1], key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown drill template; adapt to local codes and professional guidance.', related: [], _seed: seed };
}
function sigChecklist(r, id, seed) {
  var c = pick(CHECKLISTS, r);
  var items = shuffle(['Water and food for 72 hours','Flashlight and batteries','First-aid supplies','Medications and prescriptions','Important documents (copies)','Cash in small bills','Phone charger and power bank','Change of clothes','Blanket or sleeping bag','Whistle and multi-tool','Local maps','Emergency contact card'], r).slice(0, ri(r, 6, 9));
  var secs = [
    { heading: 'The checklist', body: c[0] + ' (' + c[1] + '). ' + c[2] },
    { heading: 'Items', body: 'Work through every item, checking each off only when it is packed, dated, and reachable: ' + items.join('; ') + '.' },
    { heading: 'Maintenance', body: 'Review this checklist every six months: replace expired food, medications, and batteries, and update documents after any move or policy change.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: c[0] + ' \u2014 Signature checklist', category: c[1], record_kind: RECORD_KIND, origin: 'signature-generated', summary: c[2], details: { area: c[1], items: items }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown preparedness checklist.', related: [], _seed: seed };
}
function sigPlan(r, id, seed) {
  var sc = pick(PLAN_SCENARIOS, r);
  var cat = pick(CATS, r);
  var secs = [
    { heading: 'Scenario', body: 'A Signature tabletop plan for ' + sc + ', filed under ' + cat + '.' },
    { heading: 'Assumptions', body: 'Assume normal services degrade within hours, communications are intermittent, and official guidance arrives late. The plan must work with what the household or team already owns.' },
    { heading: 'Actions', body: 'First hour: account for every person, secure the immediate area, and establish the out-of-area check-in. First day: ration supplies, set watch rotations, and monitor official channels. First week: resupply, assist neighbors, and document needs for aid workers.' },
    { heading: 'Review', body: 'Rehearse this plan yearly as a tabletop exercise: present the scenario, make decisions under time pressure, and update the written plan with every lesson learned.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: 'Contingency plan: ' + sc, category: cat, record_kind: RECORD_KIND, origin: 'signature-generated', summary: 'A Signature tabletop contingency plan for ' + sc + '.', details: { scenario: sc, area: cat }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown planning exercise, not official guidance.', related: [], _seed: seed };
}
var CATMAP = { f: 'fire-safety', m: 'medical-first-aid', d: 'natural-disaster', p: 'preparedness', s: 'safety-protocol' };
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (!opts.category || CATMAP[re.k] === opts.category) return realRecord(re.e, id, seed, CATMAP[re.k]);
  }
  var cat = opts.category || pick(CATS, rnd);
  var k = (rnd() * 3) | 0;
  if (k === 0) { var pool = DRILL_TOPICS.filter(function (x) { return !opts.category || x[1] === cat; }); return sigDrill(rnd, id, seed, pick(pool.length ? pool : DRILL_TOPICS, rnd)); }
  if (k === 1) return sigChecklist(rnd, id, seed);
  return sigPlan(rnd, id, seed);
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-EMG-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  return { ok: errors.length === 0, errors: errors };
}
function driftCheck(rec, sample) {
  var errors = [];
  for (var i = 0; i < sample.length; i++) {
    if (sample[i] && sample[i].t === rec.title && sample[i].id !== rec.id) { errors.push('duplicate title in archive sample'); break; }
  }
  return { ok: errors.length === 0, errors: errors };
}
var GEN = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, slug: SLUG, prefix: PREFIX, categories: CATS, record_kind: RECORD_KIND, realCount: REAL.length };
if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, GEN);
if (typeof module !== 'undefined' && module.exports) module.exports = GEN;
})();
