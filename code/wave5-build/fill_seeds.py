#!/usr/bin/env python3
"""Insert the 27 missing seeds (each item needs 17) before its master seed."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

def S(key, t, g, fact, mech, evid, sig_a, sig_d, points):
    return ('  S("%s", "%s", "%s",\n    "%s",\n    "%s",\n    "%s",\n    "%s",\n    "%s",\n    [%s]),\n'
            % (key, t, g, fact, mech, evid, sig_a, sig_d,
               ", ".join('"%s"' % p for p in points)))

# (file, master_key, [seed blocks])
JOBS = []

# ---------- db-midnight-radio-mystery (+4) ----------
JOBS.append(("content_mystery_stories.py", "mrm-master", [
 S("mrm-deadline", "The Deadline Caller", "The Callers",
   "A fictional caller: every night at 02:47, a caller reads tomorrow's obituaries - and one night, a listener hears their own name.",
   "The deadline works as dread: the obituaries are public record, read early; the caller's list is always accurate - until the night it names the living. The keeper investigates: the caller reads from the newspaper's advance proofs.",
   "The twist: the proofs are real, the names are real, and the caller's 'mistake' was a typesetter's error - the living name belonged to a different town's edition. The dread was a misprint.",
   "The Signature reading: the proof is the prophecy. The deadline teaches that tomorrow's news is today's typesetting.",
   "Try the Signature method: check the edition. The prophecy was a printing error.",
   ["Fictional: nightly obituary readings", "One night names a living listener", "The advance proofs", "A typesetter's error", "Dread as misprint"]),
 S("mrm-weather", "The Weather That Wasn't", "The Signals",
   "A fictional signal: the station's weather reports describe weather that never happens - sunny forecasts on storm days, calm on gale nights.",
   "The weather works as misdirection: the forecasts are recorded a week in advance, from a almanac, not the sky. The keeper discovers the weather reader hasn't looked out a window in years.",
   "The twist: the almanac was the founder's, annotated with thirty years of patterns - and it's more accurate than the modern forecast half the time. The 'wrong' weather is the old weather, returning.",
   "The Signature reading: the almanac is the oracle. The weather teaches that old patterns outlive new models.",
   "Try the Signature method: read the annotations. The thirty-year pattern beats the satellite.",
   ["Fictional: forecasts that never happen", "Recorded from an almanac", "The founder's annotations", "Old patterns returning", "The oracle almanac"]),
 S("mrm-engineer2", "The Relief Engineer", "The Station",
   "A fictional staffer: the relief engineer who covers the keeper's nights off - and swears the equipment behaves differently when the keeper is away.",
   "The relief works as witness: the dials drift, the static shapes itself, the dead air lengthens - only on the keeper's nights off. The engineer logs it all, terrified and meticulous.",
   "The twist: the keeper, restless at home, calls in 'requests' under false names on those nights - the anomalies are the keeper's own restlessness, transmitted. The station misses its keeper.",
   "The Signature reading: the absence is the signal. The relief teaches that the keeper is part of the equipment.",
   "Try the Signature method: log the nights off. The anomalies are the missing keeper.",
   ["Fictional: the substitute engineer", "Equipment behaves differently", "Meticulous terrified logs", "The keeper calling in disguise", "Absence as signal"]),
 S("mrm-frequency", "The Frequency Auction", "The Signals",
   "A fictional threat: the station's frequency is auctioned - a corporation buys the band, and midnight radio faces its last broadcast.",
   "The auction works as the finale's engine: the town must prove the station's worth - the listeners, the letters, the lives changed. The keeper plans one last all-night show: the evidence.",
   "The twist: the corporation's representative grew up listening - the bid is withdrawn live on air, and the frequency is donated back. The auction was the test; the town passed.",
   "The Signature reading: the bid is the tribute. The auction teaches that worth, proven, is power.",
   "Try the Signature method: document the worth. The listeners' letters are the bid.",
   ["Fictional: the frequency auctioned", "The last broadcast threatened", "The town proves the worth", "The bidder was a listener", "Worth proven is power"]),
]))

# ---------- db-interactive-mystery-story (+3) ----------
JOBS.append(("content_mystery_stories.py", "ims-master", [
 S("ims-docks", "The Docks at Midnight", "City Cases",
   "A fictional interactive case: the docks at midnight - the smuggler's ledger, the bribed harbormaster, the reader's choice of whom to follow.",
   "The case works as a pursuit: the fog, the crates, the ships - the reader chooses the shadows or the lighthouse. Each path reveals a different smuggler; only one reveals the ledger.",
   "The solution: the harbormaster's log - the reader who checks the paperwork finds the truth. The docks reward the methodical.",
   "The Signature reading: the log is the lantern. The docks teach that paperwork beats pursuit.",
   "Try the Signature method: check the log. The harbormaster's book names the smuggler.",
   ["Fictional: midnight docks case", "The smuggler's ledger", "Choose: shadows or灯塔", "The paperwork reveals", "Method rewarded"]),
 S("ims-manor2", "The Manor's Second Floor", "Locked Rooms",
   "A fictional interactive case: the manor's second floor - the locked gallery, the missing portrait, the reader's choice of which door to open first.",
   "The case works as a floor plan: the gallery, the study, the dumbwaiter - the reader's route determines the clues. The portrait was removed from inside; the dust shows how.",
   "The solution: the dumbwaiter - the reader who thinks vertically finds the portrait hidden below. The manor rewards the spatial.",
   "The Signature reading: the vertical is the answer. The manor teaches that locked rooms have dumbwaiters.",
   "Try the Signature method: think vertically. The hidden portrait is one floor down.",
   ["Fictional: locked gallery case", "The missing portrait", "Choose your route", "The dumbwaiter solution", "Space rewarded"]),
 S("ims-village", "The Village Fete", "Country Cases",
   "A fictional interactive case: the village fete - the missing prize money, the committee's quarrels, the reader's choice of whom to question first.",
   "The case works as a social map: the vicar, the treasurer, the cake judge - each interview opens or closes paths. The money was never stolen; it was miscounted twice.",
   "The solution: the recount - the reader who audits the books finds the double error. The fete rewards the careful.",
   "The Signature reading: the audit is the answer. The fete teaches that most thefts are arithmetic.",
   "Try the Signature method: recount the money. The double error explains the missing prize.",
   ["Fictional: village fete case", "The missing prize money", "Question whom first", "Miscounted, not stolen", "Care rewarded"]),
]))

# ---------- db-civilization-simulator (+1) ----------
JOBS.append(("content_civ_build.py", "csm-resilience", [
 S("csm-trust", "The Trust Thermocline", "Institutions",
   "A simulation model: trust in a fictional society - the invisible infrastructure that makes everything else work. The model tracks trust as a stock: built slowly, spent quickly.",
   "The model works as a reservoir: fair institutions add trust, corruption drains it, and below a threshold the society's transaction costs explode. The demo runs the drain: watch cooperation collapse.",
   "The dynamics: the thermocline - trust falls gradually, then suddenly. The model teaches the sixteenth law: trust is the cheapest infrastructure and the hardest to rebuild.",
   "The Signature reading: the reservoir is the rule. Trust teaches that the invisible stock governs the visible flows.",
   "Try the Signature method: meter the fairness. The trusted society transacts cheaply.",
   ["Trust as a modeled stock", "Built slowly, spent quickly", "The thermocline collapse", "Transaction costs explode", "Cheapest infrastructure"],
   ),
]))

# ---------- db-mega-structure-concept (+1) ----------
JOBS.append(("content_civ_build.py", "msc-master", [
 S("msc-arcology2", "The Arcology Cluster", "Towers & Cities",
   "A complete fictional concept: the Arcology Cluster - seven kilometer-towers linked by skybridges, a city of 700,000. Structure: the towers share the loads through the bridges.",
   "The engineering works as mutual support: the bridges brace the towers, the towers anchor the bridges, the cluster resists wind as one. Energy: the shared grid; water: the shared loop.",
   "Construction: one tower first, then the bridges reach out, then the cluster grows. The concept is the arcology socialized - the towers as a team.",
   "The Signature reading: the bridge is the bracing. The Cluster teaches that towers are stronger together.",
   "Try the Signature method: link the towers. The bridged cluster stands as one.",
   ["Fictional: seven linked kilometer-towers", "700,000 residents", "Skybridges as structural bracing", "Shared energy and water", "Stronger together"]),
]))

# ---------- db-space-habitat-civilization (+1) ----------
JOBS.append(("content_civ_build.py", "shc-master", [
 S("shc-l5", "The L5 Shipyard Town", "Orbit",
   "A complete fictional habitat: the L5 Shipyard Town - 3,000 builders at the Earth-Sun L5 point, assembling the big ships. Life support: the spun habitats, the closed loops.",
   "The habitat works as a company town in deep space: the yards build the vessels, the town serves the builders, the location is the Lagrange stability. Governance: the builders' council.",
   "Culture: the welders' pride, the launch as festival, the Earth as the blue anchor. The Shipyard Town is where the future is assembled.",
   "The Signature reading: the yard is the town. L5 teaches that the stable point is the workplace.",
   "Try the Signature method: build at the Lagrange. The stable point is free station-keeping.",
   ["Fictional: 3,000 builders at L5", "Assembling the big ships", "Spun habitats; closed loops", "Builders' council", "Where the future is assembled"]),
]))

# ---------- db-future-farm (+1) ----------
JOBS.append(("content_civ_build.py", "ffa-master", [
 S("ffa-saltfarm", "The Saltwater Greenhouse", "Water Farms",
   "A complete fictional farm: the Saltwater Greenhouse - growing with seawater in the desert. Crops: the salt-tolerant - samphire, saltwort, hardy tomatoes. Water: the sea, desalinated by sun.",
   "The farm works as a seawater loop: the solar stills make fresh water, the brine grows the halophytes, the waste becomes the salt. The economics: the desert coast farmed.",
   "The Saltwater Greenhouse turns the coast's curse into crops. The concept is the farm that drinks the sea.",
   "The Signature reading: the brine is the crop. The Greenhouse teaches that saltwater is the underused irrigation.",
   "Try the Signature method: still the seawater. The solar-desalinated coast is the farm.",
   ["Fictional: seawater desert farming", "Halophytes and hardy crops", "Solar stills; brine crops", "The coast farmed", "Drinks the sea"],
   ),
]))

# ---------- db-lunar-economy (+2) ----------
JOBS.append(("content_civ_space.py", "le-master", [
 S("le-data", "Lunar Data Services", "Industries",
   "A grounded treatment: the Moon as a data haven - the cold, the stable, the secure. The product: the archival storage, the processing, the relay.",
   "The economics work as the cold storage: the permanently shadowed craters are naturally cryogenic - the servers cool free. The data is the weightless export.",
   "The projection: the digital industry - the Moon's cold as the asset. The crater is the data center.",
   "The Signature reading: the shadow is the server. Lunar data teaches that the cold is the computing.",
   "Try the Signature method: chill the servers. The shadowed crater is free cooling.",
   ["Data haven in the cold traps", "Free cryogenic cooling", "Archival storage as product", "The weightless export", "Cold as the asset"]),
 S("le-heritage", "Lunar Heritage Sites", "Trade",
   "A grounded treatment: the footprints as the heritage - the Apollo sites, the protected zones. The product: the preserved history, the visited past.",
   "The economics work as the pilgrimage: the visitors come, the sites are protected, the history is the attraction. The heritage is the shared treasure.",
   "The projection: the protected past - the sites preserved by agreement. The footprints are the monument.",
   "The Signature reading: the footprint is the heritage. Lunar sites teach that the first steps are sacred.",
   "Try the Signature method: zone the heritage. The protected site is the shared monument.",
   ["Apollo sites as heritage", "Protected by agreement", "The pilgrimage economy", "The shared treasure", "First steps sacred"]),
]))

# ---------- db-mars-economy (+3) ----------
JOBS.append(("content_civ_space.py", "me-master", [
 S("me-logistics", "Mars Logistics Corps", "Industries",
   "A grounded treatment: moving things on Mars - the rovers, the routes, the depots. The challenge: the dust, the distance, the delay.",
   "The economics work as the freight: the pressurized rovers haul, the depots cache, the routes connect. The logistics are the settlement's circulation.",
   "The projection: the maturing freight - the corps that keeps Mars moving. The route is the lifeline.",
   "The Signature reading: the depot is the distribution. Logistics teaches that the cached supply is the survival.",
   "Try the Signature method: cache the depots. The distributed supply survives the dust.",
   ["Pressurized rover freight", "Depots cache the supplies", "Routes connect settlements", "The circulation", "Cached supply is survival"]),
 S("me-art", "Mars Art and Media", "Independence",
   "A grounded treatment: the culture that pays - the films, the music, the Mars aesthetic. The product: the story of the new world, exported.",
   "The economics work as the attention: the documentaries, the novels, the fashions - the Mars brand. The culture funds the dream.",
   "The projection: the soft industry - the narrative as the export. The art is the independence, expressed.",
   "The Signature reading: the story is the export. Mars art teaches that the new world's narrative is its economy.",
   "Try the Signature method: film the canyon. The Mars aesthetic is the valuable brand.",
   ["Films, music, the aesthetic", "The Mars brand", "The attention economy", "Narrative as export", "Culture funds the dream"]),
 S("me-education", "Mars Education System", "Independence",
   "A grounded treatment: schooling the Martian-born - the curriculum, the teachers, the first generation. The challenge: the new world needs its own minds.",
   "The economics work as the investment: the schools built, the teachers trained, the children - the first natives - educated. The education is the future, enrolled.",
   "The projection: the native generation - the Martians, educated as Martians. The school is the civilization, reproducing.",
   "The Signature reading: the child is the colony. Mars education teaches that the first natives are the point.",
   "Try the Signature method: school the natives. The Martian-born generation is the civilization.",
   ["Schooling the Martian-born", "The first native generation", "The curriculum of the new world", "Education as the future", "The civilization, reproducing"]),
]))

# ---------- db-space-manufacturing-network (+1) ----------
JOBS.append(("content_civ_space.py", "smn-master", [
 S("smn-recycling", "The Debris Recycling", "The Chains",
   "A grounded treatment: mining the junk - the dead satellites, the spent stages, the orbital debris as feedstock. The problem: the crowded orbits.",
   "The industry works as the cleanup: the tugs collect, the processors shred, the foundries melt. The debris becomes the stock - the orbit cleaned and fed.",
   "The projection: the circular orbit - the junk as the mine. The recycling is the remediation, profitable.",
   "The Signature reading: the junk is the ore. Debris recycling teaches that the crowded orbit is the stockpile.",
   "Try the Signature method: tug the dead. The collected satellite is the feedstock.",
   ["Dead satellites as feedstock", "Tugs collect; foundries melt", "The orbit cleaned and fed", "Profitable remediation", "Junk as the ore"],
   ),
]))

# ---------- db-global-problem-solver (+1) ----------
JOBS.append(("content_civ_global.py", "gps-master", [
 S("gps-mental", "The Mental Health Gap", "Human Needs",
   "A grounded treatment: the untreated minds - the depression, the anxiety, the missing care. The data: the treatment gap - most receive nothing.",
   "The solutions, evaluated: the task-sharing (proven), the community workers (proven), the digital tools (promising), the destigmatization (necessary). The honest assessment: the care can scale.",
   "The projection: the closing gap is achievable. The barrier is the stigma and the staffing.",
   "The Signature reading: the worker is the therapy. Mental health teaches that the trained community heals.",
   "Try the Signature method: share the tasks. The community worker is the proven scale.",
   ["The global treatment gap", "Task-sharing proven", "Community workers proven", "The care can scale", "Stigma as the barrier"],
   ),
]))

# ---------- db-world-improvement-challenge (+2) ----------
JOBS.append(("content_civ_global.py", "wic-master", [
 S("wic-library", "The Library Challenge", "Your Street",
   "A structured challenge: the little free libraries - the books, the boxes, the sharing. The goal: a library on every block. The measure: the books circulating.",
   "The challenge works in 60 days: the boxes built, the books stocked, the stewards named. The win: the reading street.",
   "The prize: the shared shelf. The challenge is the smallest library - the block's books.",
   "The Signature reading: the box is the library. The challenge teaches that the shared book multiplies.",
   "Try the Signature method: build the box. The little library is the 60-day win.",
   ["A library on every block", "60 days; books circulating", "Boxes, books, stewards", "The reading street", "The shared shelf"]),
 S("wic-air", "The Clean Air Challenge", "Your City",
   "A structured challenge: the breathable city - the monitors, the actions, the blue days. The goal: the safe air. The measure: the particulate levels.",
   "The challenge works in three years: the monitoring network, the source cuts, the green buffers. The win: the city that breathes.",
   "The prize: the blue day. The challenge is the invisible made visible - the air, cleaned.",
   "The Signature reading: the monitor is the movement. The challenge teaches that the measured air improves.",
   "Try the Signature method: monitor the blocks. The mapped pollution is the targeted cut.",
   ["The breathable city", "Three years; particulate levels", "Monitors, source cuts, buffers", "The city that breathes", "The blue day"]),
]))

# ---------- db-planet-repair-concept (+1) ----------
JOBS.append(("content_civ_global.py", "prc-master", [
 S("prc-peat", "The Peatland Restoration", "Land Repair",
   "A complete concept: rewetting the peatlands - the drained bogs, the carbon vaults. The damage: the drained peat, the released carbon.",
   "The intervention works as rewetting: the drains blocked, the water returns, the sphagnum regrows. The concept is proven - the rewetted peat stores carbon.",
   "The recovery: the carbon locked, the birds returned, the bog breathing. The peatland is the climate's vault - restored.",
   "The Signature reading: the water is the lock. Peatlands teach that the wet bog is the carbon safe.",
   "Try the Signature method: block the drains. The rewetted peat is the carbon vault.",
   ["Rewetting drained peatlands", "The carbon vaults", "Proven: storing carbon", "The bog breathing", "Wet is the lock"],
   ),
]))

# ---------- db-biodiversity-recovery (+1) ----------
JOBS.append(("content_civ_global.py", "bdr-master", [
 S("bdr-insect", "The Insect Recovery", "Species Returns",
   "A documented comeback: the insects returning - the pollinators, the meadows restored. The decline: the windshield phenomenon, the silent fields.",
   "The intervention: the pesticide restraint, the wildflower strips, the dark skies. The return: the bees back, the meadows buzzing, the food webs rebuilding.",
   "The honest status: recovering where helped; the declines continue elsewhere. The insect teaches that the small is the foundational.",
   "The Signature reading: the strip is the recovery. Insects teach that the wildflower margin restores.",
   "Try the Signature method: plant the margins. The pollinator strip is the proven tool.",
   ["Pollinators returning where helped", "Wildflower strips", "Pesticide restraint", "The meadows buzzing", "Small is foundational"],
   ),
]))

# ---------- db-clean-water-for-everyone (+1) ----------
JOBS.append(("content_civ_global.py", "cwe-master", [
 S("cwe-atmospheric", "The Atmospheric Water", "The Sources",
   "A proven solution: water from air - the fog nets, the dew collectors, the atmospheric generators. The technology: the passive and the powered.",
   "The solution works as the sky's tap: the fog caught, the dew condensed, the humidity harvested. The proven record: the fog-net villages watered.",
   "The scale: the arid coasts, the mountain fogs - the niche, vital source. The atmospheric water is the sky's delivery.",
   "The Signature reading: the net is the well. Atmospheric water teaches that the fog is the reservoir.",
   "Try the Signature method: net the fog. The harvested air is the village's water.",
   ["Fog nets; dew collectors", "The passive harvest", "Fog-net villages watered", "The arid niche", "The sky's tap"],
   ),
]))

# ---------- db-global-learning-access (+1) ----------
JOBS.append(("content_civ_global.py", "gla-master", [
 S("gla-sign", "The Sign Language Library", "The Content",
   "A proven pathway: learning in sign - the video libraries, the deaf schools, the visual learning. The barrier: the unserved deaf children.",
   "The pathway works as the visual: the sign-language materials filmed, the deaf teachers trained, the schools opened. The proven record: the deaf children learning.",
   "The scale: the millions of deaf children out of school. The sign is the language - the library, visual.",
   "The Signature reading: the hand is the textbook. Sign teaches that the visual language educates.",
   "Try the Signature method: film the signs. The video library is the proven pathway.",
   ["Video sign-language libraries", "Deaf teachers trained", "The visual learning", "Millions unserved", "The hand educates"],
   ),
]))

# ---------- db-universal-accessibility (+1) ----------
JOBS.append(("content_civ_global.py", "uac-master", [
 S("uac-sensory", "The Sensory-Friendly Spaces", "The Built World",
   "A complete design: spaces for sensitive senses - the quiet rooms, the dimmed lights, the calm. The barrier: the overwhelming.",
   "The design works as the calm: the sensory maps, the quiet hours, the retreat spaces. The standard: the welcoming calm.",
   "The result: the space for everyone - the autistic, the anxious, the overwhelmed. The sensory-friendly space is the humane space.",
   "The Signature reading: the quiet hour is the welcome. The design teaches that the calm serves all.",
   "Try the Signature method: map the sensory. The quiet room is the inclusion.",
   ["Quiet rooms; dimmed lights", "Sensory maps; quiet hours", "The welcoming calm", "Serves every sensitivity", "The humane space"],
   ),
]))

# ---------- db-human-potential (+1) ----------
JOBS.append(("content_civ_global.py", "hp-master", [
 S("hp-grit", "The Grit Factor", "The Mind",
   "An evidence-grounded treatment: the perseverance - the grit, the long effort, the sustained. The finding: the grit predicts the achievement.",
   "The practices: the long goals, the sustained effort, the passion held. The evidence: the grit research.",
   "The flourishing: the persistent - the finishing, the achieving, the enduring. The grit is the long game.",
   "The Signature reading: the sustained is the success. Grit teaches that the long effort wins.",
   "Try the Signature method: hold the goal. The sustained passion is the proven predictor.",
   ["Grit predicts achievement", "Long goals; sustained effort", "The evidence", "The long game", "Persistence wins"],
   ),
]))

# ---------- db-civilization-milestones (+1) ----------
JOBS.append(("content_civ_global.py", "cm-master", [
 S("cm-print", "The Printing Press", "Crossed",
   "A historical milestone: the press - the movable type, the cheap book, the reading public. The crossing: the 1440s.",
   "The evidence: the presses, the books, the literacies rising. The consequence: the Reformation, the science, the public sphere - the ideas, unbound.",
   "The threshold: the cheap copy. Print made knowledge scalable - the milestone that multiplied minds.",
   "The Signature reading: the type is the torrent. Print teaches that the cheap copy changes everything.",
   "Try the Signature method: mark the press. The multiplied book is the modern mind.",
   ["Printing press, 1440s", "Movable type; cheap books", "Literacy rising", "Reformation, science", "The multiplied milestone"],
   ),
]))

# ---------- db-big-future-ideas-gallery (+1) ----------
JOBS.append(("content_civ_global.py", "bfi-gallery", [
 S("bfi-commons", "The Knowledge Commons", "The Visions",
   "A big idea: the shared mind - the open knowledge, the commons enriched, the everyone elevated. The promise: the wisdom, common.",
   "The problems: the funding, the quality, the sustaining. The path: the open projects now, the institutions supporting, the commons growing.",
   "The honest assessment: the underway - the commons already building. The knowledge is the heritage - the work is the sharing.",
   "The Signature reading: the shared is the multiplied. Commons teach that the open knowledge elevates all.",
   "Try the Signature method: contribute the knowledge. The enriched commons is the path's start.",
   ["The shared mind", "Open knowledge for all", "The underway commons", "Wisdom, common", "Sharing is the work"],
   ),
]))

for fname, master, seeds in JOBS:
    path = os.path.join(BASE, fname)
    src = open(path).read()
    anchor = '  S("%s",' % master
    assert anchor in src, "anchor %s missing in %s" % (master, fname)
    block = "".join(seeds)
    src = src.replace(anchor, block + anchor, 1)
    open(path, "w").write(src)
    print("inserted %d seeds into %s before %s" % (len(seeds), fname, master))
