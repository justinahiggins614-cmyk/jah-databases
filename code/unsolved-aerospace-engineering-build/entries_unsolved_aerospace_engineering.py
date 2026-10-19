#!/usr/bin/env python3
"""Entries for The Unsolved Aerospace Engineering Database (unsolved-aerospace-engineering)
and its Signature half (unsolved-aerospace-engineering-signature).

34 famous unsolved problems in aerospace engineering, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never engineering
advice, never a design recommendation.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "engineering advice.")

STD_COMMON = [
    "Problem statements verified against the published aerospace literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never engineering advice, never a design recommendation.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "turbulence",
 "name": "Turbulence: The Last Unsolved Problem of Classical Physics",
 "group": "Aerodynamics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Turbulence governs drag, lift, and mixing - yet no complete theory predicts it. Why is turbulence still unsolved?",
 "description": "Turbulence - chaotic fluid motion - determines aircraft drag, engine mixing, and atmospheric behavior. The Navier-Stokes equations describe it but can't be solved generally; the Clay Millennium Prize for Navier-Stokes regularity is unclaimed. Engineering relies on models (RANS, LES) that approximate without understanding.",
 "background": "Reynolds (1883) characterized the transition; Kolmogorov (1941) gave statistical laws; the Millennium Prize (2000) formalized the math problem. CFD models turbulence without solving it. As of 2026 the theory remains incomplete.",
 "why_it_matters": "Turbulence modeling limits aircraft efficiency: a real theory would transform aerodynamics.",
 "sig_pointer": "The Signature system's proposed approach treats turbulence as a closure problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that turbulence needs closure: the statistical rules connecting scales identified - completing the theory from data upward. "
  "Assumptions: (1) closure rules exist; (2) they are discoverable; (3) they are universal. "
  "Reasoning path: a closure model explains model successes and predicts true turbulence theory. "
  "Proposed mechanism: 'closure-completed' turbulence - data-discovered scale laws. "
  "What would confirm it: discovered laws predicting flows across regimes. "
  "What would kill it: evidence that turbulence has no universal laws. "
  "What this does not claim: it does not claim turbulence is solved, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads turbulence as missing scale laws, and asks what data would discover.",
 "how_it_works": "Researchers study turbulence through DNS simulations, Kolmogorov theory, and machine-learned closures.",
 "key_points": [
  "Navier-Stokes describes but doesn't solve turbulence.",
  "The Millennium Prize for regularity is unclaimed.",
  "Kolmogorov gave statistical laws, not a theory.",
  "Engineering models approximate without understanding.",
  "Drag and mixing depend on the unsolved.",
 ],
 "requirements": [
  "Discovered universal scale laws.",
  "Predictions across flow regimes.",
  "Theory replacing models.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Reynolds O. Transition experiments. 1883.",
  "Kolmogorov AN. Turbulence statistics. 1941.",
  "Clay Mathematics Institute. Navier-Stokes prize. 2000.",
  "Pope SB. Turbulent Flows. Cambridge; 2000.",
 ],
 "demo_data": {"a": ("aircraft drag from turbulence, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of aircraft drag is turbulence - modeled, never understood",
               "confirm": "discovered laws predict flows across regimes",
               "refute": "turbulence proves to have no universal laws"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "laminar-flow",
 "name": "Laminar Flow Control: The Drag Revolution That Wasn't",
 "group": "Aerodynamics",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Laminar flow could cut drag dramatically - but keeping wings laminar in service has defeated decades of effort. Why?",
 "description": "Laminar-flow control - maintaining smooth airflow over wings - promises 10-15% drag reduction; but insect strikes, surface imperfections, and atmospheric disturbances trip the boundary layer turbulent. Decades of research (X-21, 787 test programs) haven't delivered operational laminar flow.",
 "background": "Laminar-flow research dates to the 1940s-60s (X-21 suction wings); natural laminar flow airfoils helped gliders; commercial programs (787 tail tests) showed partial success. As of 2026 operational laminar flow remains elusive.",
 "why_it_matters": "Laminar flow would cut fuel burn ~10%: the largest single aerodynamic prize.",
 "sig_pointer": "The Signature system's proposed approach treats laminar flow as a robustness problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that laminar flow needs robustness: the disturbance-rejection (surface tolerance, insect mitigation, active control) that keeps flow laminar in service. "
  "Assumptions: (1) robustness is engineerable; (2) it is affordable; (3) it preserves the drag benefit. "
  "Reasoning path: a robustness model explains lab-service gaps and predicts operational laminar flow. "
  "Proposed mechanism: 'robustness-engineered' laminar flow - service-tolerant laminar wings. "
  "What would confirm it: laminar wings maintaining benefit in service. "
  "What would kill it: evidence that service disturbances defeat all control. "
  "What this does not claim: it does not claim laminar flow is operational, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads laminar flow as fragile perfection, and asks what robustness would sustain.",
 "how_it_works": "Researchers study laminar flow through boundary-layer research, suction-wing tests, and disturbance studies.",
 "key_points": [
  "Laminar flow promises 10-15% drag reduction.",
  "Insects and imperfections trip the boundary layer.",
  "X-21 and 787 programs showed partial success.",
  "Decades of research haven't delivered operations.",
  "Robustness, not physics, is the barrier.",
 ],
 "requirements": [
  "Service-robust laminar wings.",
  "Maintained drag benefit in operations.",
  "Affordable robustness solutions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "X-21 laminar-flow program. Various; 1960s.",
  "Schrauf G et al. Laminar flow research. Various; 2005-2015.",
  "Boeing 787 laminar-flow tests. Various; 2010s.",
  "Joslin RD. Laminar flow control reviews. 1998.",
 ],
 "demo_data": {"a": ("drag reduction from laminar flow, percent (approx)", 12.0),
               "b": ("percent scale", 100.0), "bounds": (0.07, 0.18),
               "step1": "a tenth of drag removable - if the wing survives insects and reality",
               "confirm": "laminar wings maintain benefit in service",
               "refute": "service disturbances prove to defeat all control"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "sonic-boom",
 "name": "Sonic Booms: The Barrier to Supersonic Flight",
 "group": "Aerodynamics",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Sonic booms banned overland supersonic flight - can shaped booms make supersonic travel acceptable?",
 "description": "Sonic booms - the N-wave from supersonic flight - led to the 1973 overland ban, killing commercial supersonic transport. Low-boom designs (shaped signatures) promise acceptable noise; NASA's X-59 (2020s) tests the concept. Whether shaped booms are publicly acceptable is unproven.",
 "background": "The overland ban (1973) followed Concorde's boom; low-boom theory (Seebass, 1960s-70s) proposed shaped signatures; the X-59 QueSST (2020s) is the flight test. As of 2026 the technology flies with acceptability pending.",
 "why_it_matters": "Acceptable supersonic flight would halve intercontinental travel times: the boom is the barrier.",
 "sig_pointer": "The Signature system's proposed approach validates low-boom acceptability, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that low-boom flight needs acceptability proof: shaped signatures tested on real communities - with measured response. "
  "Assumptions: (1) shaping works; (2) acceptability is measurable; (3) communities accept. "
  "Reasoning path: an acceptability model explains the ban's persistence and predicts supersonic return. "
  "Proposed mechanism: 'acceptability-proven' low-boom flight - community-tested supersonic. "
  "What would confirm it: community tests showing acceptable response. "
  "What would kill it: evidence that any boom is unacceptable. "
  "What this does not claim: it does not claim supersonic flight is acceptable, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads the boom as untested acceptability, and asks what communities would tolerate.",
 "how_it_works": "Researchers study sonic booms through X-59 flight tests, shaped-signature theory, and community-response studies.",
 "key_points": [
  "The 1973 overland ban killed commercial supersonic flight.",
  "Low-boom shaping promises acceptable signatures.",
  "NASA's X-59 tests the concept.",
  "Public acceptability is unproven.",
  "The boom is the regulatory barrier.",
 ],
 "requirements": [
  "Shaped-boom flight demonstration.",
  "Community acceptability proof.",
  "Regulatory change based on evidence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Seebass R et al. Low-boom theory. Various; 1969-1975.",
  "NASA X-59 QueSST program. 2018 onward.",
  "Plotkin KJ et al. Boom acceptability. Various; 2005-2015.",
  "FAA. Supersonic regulations. Various.",
 ],
 "demo_data": {"a": ("years of overland supersonic ban (approx)", 50.0),
               "b": ("years scale", 100.0), "bounds": (0.4, 0.62),
               "step1": "fifty years banned by noise - the barrier a shaped wave might lift",
               "confirm": "community tests show acceptable response",
               "refute": "any boom proves unacceptable"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "scramjet",
 "name": "Scramjets: Sustained Hypersonic Flight",
 "group": "Propulsion",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Scramjets promise hypersonic air-breathing flight - but sustained combustion in supersonic airflow remains fiendishly hard. What blocks it?",
 "description": "Scramjets - supersonic-combustion ramjets - could power hypersonic vehicles; but mixing fuel in millisecond-residence supersonic flow, managing heat, and sustaining combustion have defeated operational use. X-43 and X-51 flew briefly; no operational scramjet exists.",
 "background": "Scramjet research dates to the 1950s-60s; X-43 (2004) flew at Mach 9.6 briefly; X-51 (2010-2013) sustained minutes. As of 2026 scramjets are experimental with military programs active.",
 "why_it_matters": "Operational scramjets would enable hypersonic transport and access: the propulsion frontier.",
 "sig_pointer": "The Signature system's proposed approach treats scramjet combustion as a mixing problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that scramjet combustion is a mixing problem: the fuel-air mixing in millisecond flows engineered - with validated sustained combustion. "
  "Assumptions: (1) mixing is the barrier; (2) it is engineerable; (3) sustained flight follows. "
  "Reasoning path: a mixing model explains brief-flight history and predicts operational scramjets. "
  "Proposed mechanism: 'mixing-engineered' scramjets - sustained supersonic combustion. "
  "What would confirm it: sustained scramjet flight demonstrations. "
  "What would kill it: evidence that supersonic combustion is inherently unsustainable. "
  "What this does not claim: it does not claim operational scramjets exist, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads scramjets as unmixed combustion, and asks what engineering would sustain it.",
 "how_it_works": "Researchers study scramjets through X-43/X-51 follow-ups, mixing research, and hypersonic test programs.",
 "key_points": [
  "Scramjets promise hypersonic air-breathing flight.",
  "Supersonic combustion must complete in milliseconds.",
  "X-43 and X-51 flew briefly.",
  "No operational scramjet exists.",
  "Heat and mixing are the barriers.",
 ],
 "requirements": [
  "Sustained supersonic combustion.",
  "Operational flight demonstrations.",
  "Heat-management solutions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "X-43A program. Various; 2004.",
  "X-51A Waverider. Various; 2010-2013.",
  "Curran ET. Scramjet history. Various; 2001.",
  "Smart MK et al. Scramjet reviews. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("X-51 sustained flight, minutes (approx)", 3.5),
               "b": ("minutes for operational flight (approx)", 60.0), "bounds": (0.03, 0.1),
               "step1": "three minutes against an hour needed - the sustained-flight gap",
               "confirm": "sustained scramjet flight demonstrations",
               "refute": "supersonic combustion proves inherently unsustainable"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "reusable-launch",
 "name": "Fully Reusable Launch: The Cost Frontier",
 "group": "Space",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "SpaceX proved booster reuse - but fully reusable orbital launch (Starship's goal) is unproven. What blocks the cost revolution?",
 "description": "Reusable launch - recovering and reflying orbital vehicles - promises order-of-magnitude cost reduction; Falcon 9 proved partial reuse; Starship aims for full rapid reuse. But heat-shield refurbishment, engine life, and turnaround operations are unproven at scale.",
 "background": "The Shuttle was partially reusable at high cost; Falcon 9 (2015 onward) proved booster economics; Starship (2020s) targets full reuse. As of 2026 full rapid reuse is in testing.",
 "why_it_matters": "Full reuse would make space access routine: the economic foundation of the space age.",
 "sig_pointer": "The Signature system's proposed approach treats reuse as an operations problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that full reuse is an operations problem: the turnaround, refurbishment, and reliability engineering that makes reflying routine. "
  "Assumptions: (1) the physics is solved; (2) operations are the barrier; (3) they are engineerable. "
  "Reasoning path: an operations model explains partial-reuse history and predicts full-reuse economics. "
  "Proposed mechanism: 'operations-engineered' full reuse - aircraft-like turnaround. "
  "What would confirm it: rapid full-stack reflights at low cost. "
  "What would kill it: evidence that orbital reuse can't be economical. "
  "What this does not claim: it does not claim full reuse exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads reuse as unengineered operations, and asks what turnaround would make routine.",
 "how_it_works": "Researchers study reusable launch through Starship test programs, refurbishment research, and cost modeling.",
 "key_points": [
  "Falcon 9 proved partial-reuse economics.",
  "Starship targets full rapid reuse.",
  "Heat-shield and engine life are unproven.",
  "The Shuttle was reusable at high cost.",
  "Operations, not physics, may be the barrier.",
 ],
 "requirements": [
  "Rapid full-stack reflights.",
  "Refurbishment costs proving economics.",
  "Aircraft-like turnaround operations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "SpaceX. Falcon 9 reuse program. 2015 onward.",
  "SpaceX. Starship test program. 2020 onward.",
  "NASA. Shuttle cost analyses. Various.",
  "Jones H et al. Reuse economics. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("Falcon 9 cost reduction from reuse, fold (approx)", 2.0),
               "b": ("Starship targeted reduction, fold (approx)", 10.0), "bounds": (0.12, 0.3),
               "step1": "two-fold achieved of ten-fold targeted - the reuse revolution's remaining gap",
               "confirm": "rapid full-stack reflights at low cost",
               "refute": "orbital reuse proves uneconomical"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "electric-aviation",
 "name": "Electric Aviation: The Battery Barrier",
 "group": "Propulsion",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Electric aircraft work for short hops - but batteries are 50x less energy-dense than jet fuel. Can electric aviation scale?",
 "description": "Electric aviation - battery-powered flight - succeeds in trainers and eVTOL prototypes; but energy density (250 Wh/kg vs 12,000 Wh/kg for jet fuel) limits range to short hops. Whether batteries improve enough for regional flight is the open question.",
 "background": "Electric flight dates to early experiments; the 2010s-2020s brought eVTOL investment; battery density improves ~5% yearly. As of 2026 electric aviation is short-range with scaling uncertain.",
 "why_it_matters": "Scaled electric aviation would decarbonize flight: the battery barrier is aviation's climate bottleneck.",
 "sig_pointer": "The Signature system's proposed approach treats electric aviation as an energy-density race, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that electric aviation scales with energy density: the Wh/kg thresholds for each mission mapped - with battery roadmaps targeting them. "
  "Assumptions: (1) density keeps improving; (2) thresholds are reachable; (3) missions follow. "
  "Reasoning path: a density model explains current limits and predicts scaling. "
  "Proposed mechanism: 'density-targeted' electric aviation - missions matched to battery roadmaps. "
  "What would confirm it: batteries reaching regional-flight thresholds. "
  "What would kill it: evidence that density plateaus below thresholds. "
  "What this does not claim: it does not claim electric aviation scales, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads electric flight as energy-density-limited, and asks what thresholds would unlock missions.",
 "how_it_works": "Researchers study electric aviation through battery roadmaps, eVTOL test programs, and mission analyses.",
 "key_points": [
  "Batteries are ~50x less energy-dense than jet fuel.",
  "Electric flight works for short hops and trainers.",
  "eVTOL investment is massive.",
  "Density improves ~5% yearly.",
  "Regional flight needs unreached thresholds.",
 ],
 "requirements": [
  "Batteries reaching mission thresholds.",
  "Certified electric aircraft at scale.",
  "Density roadmaps proving the path.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hepperle M. Electric flight analyses. Various; 2012-2017.",
  "eVTOL industry reports. Various; 2018-2024.",
  "Bacchini A et al. Battery aviation reviews. Various; 2019-2023.",
  "Gnadt AR et al. Electric aircraft performance. Various; 2018-2019.",
 ],
 "demo_data": {"a": ("jet fuel energy density, Wh/kg (approx)", 12000.0),
               "b": ("battery energy density, Wh/kg (approx)", 250.0), "bounds": (35.0, 60.0),
               "step1": "forty-eight-fold energy gap - the physics electric aviation must close",
               "confirm": "batteries reach regional-flight thresholds",
               "refute": "density proves to plateau below thresholds"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "hypersonic-heat",
 "name": "Hypersonic Heating: Surviving Mach 5+",
 "group": "Aerodynamics",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Hypersonic flight melts structures - how do vehicles survive the heat of Mach 5+?",
 "description": "Hypersonic heating - shock-layer temperatures of thousands of degrees - destroys conventional materials; thermal protection (ablatives, actively cooled structures, ultra-high-temperature ceramics) is the enabling technology. But reusable, reliable hypersonic thermal protection is unproven.",
 "background": "Reentry heating was solved for capsules (ablatives, 1960s); the Shuttle's tiles were reusable but fragile; hypersonic cruise needs new solutions. UHTC research is active. As of 2026 reusable hypersonic TPS is developmental.",
 "why_it_matters": "Thermal protection enables hypersonic flight: the material barrier to Mach 5+.",
 "sig_pointer": "The Signature system's proposed approach treats hypersonic heating as a materials problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hypersonic survival needs reusable high-temperature materials: UHTCs and actively cooled structures validated for repeated flight. "
  "Assumptions: (1) materials exist; (2) they are reusable; (3) they are affordable. "
  "Reasoning path: a materials model explains the expendable-reusable gap and predicts sustained hypersonic flight. "
  "Proposed mechanism: 'reusable-TPS' hypersonics - validated repeated-flight thermal protection. "
  "What would confirm it: reusable hypersonic vehicles flying repeatedly. "
  "What would kill it: evidence that hypersonic heating defeats reusability. "
  "What this does not claim: it does not claim reusable hypersonics exist, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads hypersonic heat as a materials gap, and asks what reusable protection would enable.",
 "how_it_works": "Researchers study hypersonic heating through UHTC research, arc-jet testing, and TPS development.",
 "key_points": [
  "Hypersonic shock layers reach thousands of degrees.",
  "Ablatives work once; reusability is unproven.",
  "Shuttle tiles were reusable but fragile.",
  "UHTCs are the leading candidate.",
  "Thermal protection is the enabling technology.",
 ],
 "requirements": [
  "Reusable high-temperature materials.",
  "Repeated hypersonic flight demonstrations.",
  "Affordable TPS solutions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Anderson JD. Hypersonic heating. Various editions.",
  "Fahrenholtz WG et al. UHTC research. Various; 2007-2020.",
  "NASA. TPS development programs. Various.",
  "Glass DE et al. Hypersonic materials. Various; 2008-2016.",
 ],
 "demo_data": {"a": ("hypersonic leading-edge temperature, C (approx)", 2000.0),
               "b": ("titanium limit, C (approx)", 600.0), "bounds": (2.5, 4.5),
               "step1": "three times titanium's limit - the heat conventional airframes can't survive",
               "confirm": "reusable hypersonic vehicles fly repeatedly",
               "refute": "hypersonic heating proves to defeat reusability"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "autonomous-flight",
 "name": "Autonomous Flight: Certifying the Pilotless Airliner",
 "group": "Avionics",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Autopilots fly most of every flight - but certifying fully autonomous airliners is uncharted. What would certification require?",
 "description": "Autonomous flight - AI pilots for airliners - faces the certification problem: aviation certifies deterministic systems; learning systems resist certification. The safety case for pilotless airliners is undefined; public acceptance is untested.",
 "background": "Autopilots automated cruise decades ago; UAVs proved remote operation; urban air mobility needs autonomy. EASA/FAA are developing AI certification frameworks. As of 2026 autonomous airliners are conceptual.",
 "why_it_matters": "Certified autonomy would transform aviation economics and enable new missions: the regulatory frontier.",
 "sig_pointer": "The Signature system's proposed approach builds the autonomy safety case, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that autonomous flight needs a new safety case: the verification methods for learning systems developed - with safety proven beyond human pilots. "
  "Assumptions: (1) verification is achievable; (2) it convinces regulators; (3) the public accepts. "
  "Reasoning path: a safety-case model explains the certification block and predicts autonomous aviation. "
  "Proposed mechanism: 'safety-cased' autonomy - verified AI pilots. "
  "What would confirm it: certified autonomous flights with superior safety. "
  "What would kill it: evidence that learning systems can't be certified. "
  "What this does not claim: it does not claim autonomous airliners exist, offers no engineering advice, and does not constitute a certification recommendation."),
 "sig_lens": "The Signature lens reads autonomy as uncertifiable learning, and asks what verification would certify.",
 "how_it_works": "Researchers study autonomous flight through AI-certification research, UAV safety cases, and EASA/FAA frameworks.",
 "key_points": [
  "Autopilots fly most of every flight already.",
  "Learning systems resist traditional certification.",
  "The safety case for pilotless airliners is undefined.",
  "EASA/FAA are developing AI frameworks.",
  "Public acceptance is untested.",
 ],
 "requirements": [
  "Verification methods for learning systems.",
  "Regulatory safety cases accepted.",
  "Demonstrated superior safety.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "EASA. AI certification roadmap. 2020 onward.",
  "FAA. Autonomy research programs. Various.",
  "Belcastro CM et al. Flight autonomy reviews. Various; 2017-2022.",
  "NASA. Autonomy research. Various.",
 ],
 "demo_data": {"a": ("flight time on autopilot, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 0.98),
               "step1": "nine-tenths automated already - with the last tenth uncertifiable",
               "confirm": "certified autonomous flights with superior safety",
               "refute": "learning systems prove uncertifiable"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "space-debris",
 "name": "Space Debris: The Orbital Commons Crisis",
 "group": "Space",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Orbital debris threatens the space age - Kessler syndrome could close orbits. Can debris be managed or removed?",
 "description": "Space debris - 30,000+ tracked objects, millions untracked - grows with megaconstellations; collisions cascade (Kessler syndrome). Removal technologies (nets, harpoons, lasers, tugs) are experimental; the governance (who pays, who removes) is unresolved.",
 "background": "Kessler's 1978 prediction framed the problem; the Iridium-Cosmos collision (2009) proved it; megaconstellations accelerated growth. Active-removal demos are early. As of 2026 debris grows with removal unproven.",
 "why_it_matters": "Kessler syndrome could deny orbits for generations: debris management is space's tragedy of the commons.",
 "sig_pointer": "The Signature system's proposed approach makes debris removal economical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that debris removal needs economics: the incentives and technologies making removal pay - with governance assigning responsibility. "
  "Assumptions: (1) removal is technically feasible; (2) economics can work; (3) governance is achievable. "
  "Reasoning path: an economics model explains the inaction and predicts a managed orbital commons. "
  "Proposed mechanism: 'economical' debris removal - incentivized active cleanup. "
  "What would confirm it: operational debris-removal services. "
  "What would kill it: evidence that removal is uneconomical at scale. "
  "What this does not claim: it does not claim debris removal exists, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads debris as an unpaid commons, and asks what economics would clean it.",
 "how_it_works": "Researchers study debris through tracking catalogs, removal demos, and governance research.",
 "key_points": [
  "30,000+ tracked objects; millions untracked.",
  "Kessler syndrome could cascade.",
  "Megaconstellations accelerate growth.",
  "Removal technologies are experimental.",
  "Governance (who pays) is unresolved.",
 ],
 "requirements": [
  "Operational removal technologies.",
  "Economics making removal pay.",
  "Governance assigning responsibility.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kessler DJ et al. Collision frequency. 1978.",
  "Iridium-Cosmos collision. 2009.",
  "ESA. Space debris reports. Annual.",
  "Liou JC et al. Debris modeling. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("tracked debris objects (approx)", 30000.0),
               "b": ("objects scale (hundred-thousands)", 100000.0), "bounds": (0.2, 0.42),
               "step1": "thirty thousand tracked against millions untracked - the cataloged fraction",
               "confirm": "operational debris-removal services",
               "refute": "removal proves uneconomical at scale"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "nuclear-propulsion",
 "name": "Nuclear Thermal Propulsion for Mars",
 "group": "Space",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Chemical rockets make Mars trips slow - nuclear thermal propulsion could halve transit time. Why isn't it flying?",
 "description": "Nuclear thermal propulsion (NTP) - fission heating hydrogen - offers twice chemical efficiency; NERVA proved it in the 1960s-70s. But testing restrictions, political concerns, and program cancellations kept it grounded. NASA's DRACO program (2020s) revives it.",
 "background": "NERVA (1955-1973) demonstrated NTP; political and treaty concerns ended testing; DRACO (2021 onward) plans flight demos. As of 2026 NTP is proven technology awaiting flight.",
 "why_it_matters": "NTP would halve Mars transit: the propulsion for human deep space.",
 "sig_pointer": "The Signature system's proposed approach flies NTP demonstrators, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that NTP needs flight demonstration: the DRACO-class demos proving safe operation - unlocking Mars architectures. "
  "Assumptions: (1) demos succeed; (2) safety is demonstrable; (3) politics follows proof. "
  "Reasoning path: a demonstration model explains the 50-year gap and predicts NTP flight. "
  "Proposed mechanism: 'demonstrated' NTP - flown safe nuclear propulsion. "
  "What would confirm it: successful NTP flight demos. "
  "What would kill it: evidence that NTP can't be flown safely or politically. "
  "What this does not claim: it does not claim NTP flies, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads NTP as proven but unflown, and asks what demonstration would launch it.",
 "how_it_works": "Researchers study NTP through NERVA history, DRACO development, and Mars-architecture studies.",
 "key_points": [
  "NTP offers twice chemical efficiency.",
  "NERVA proved it in the 1960s-70s.",
  "Testing and politics kept it grounded.",
  "DRACO plans flight demonstrations.",
  "Fifty years proven, zero flown.",
 ],
 "requirements": [
  "Successful flight demonstrations.",
  "Demonstrated safe operation.",
  "Mars architectures using NTP.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NERVA program. Various; 1955-1973.",
  "NASA/DARPA DRACO program. 2021 onward.",
  "Angelo JA et al. NTP reviews. Various; 2000-2020.",
  "Houts MG et al. NTP development. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("years since NERVA proved NTP (approx)", 55.0),
               "b": ("years scale", 100.0), "bounds": (0.45, 0.68),
               "step1": "fifty-five years proven, zero flown - the propulsion that waits on politics",
               "confirm": "successful NTP flight demos",
               "refute": "NTP proves un-flyable safely or politically"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "supersonic-transport",
 "name": "Supersonic Transport's Return",
 "group": "Aviation",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Concorde retired in 2003 - can supersonic airliners return economically and acceptably?",
 "description": "Supersonic transport's return - Boom Supersonic and others - needs low-boom designs, efficient engines, and economics that work. Concorde failed economically; the new generation bets on technology and premium markets.",
 "background": "Concorde (1976-2003) proved technical feasibility and economic failure; Boom's Overture (2020s) targets Mach 1.7 with 65 passengers. As of 2026 no supersonic airliner flies commercially.",
 "why_it_matters": "Supersonic return would transform long-haul travel: the market test of low-boom technology.",
 "sig_pointer": "The Signature system's proposed approach proves supersonic economics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that supersonic return needs economic proof: the operating economics demonstrated - with low-boom acceptability. "
  "Assumptions: (1) technology suffices; (2) premium markets exist; (3) economics close. "
  "Reasoning path: an economics model explains Concorde's failure and predicts the return's conditions. "
  "Proposed mechanism: 'economically-proven' supersonic transport - viable operations. "
  "What would confirm it: profitable supersonic operations. "
  "What would kill it: evidence that supersonic economics never close. "
  "What this does not claim: it does not claim supersonic airliners fly, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads Concorde as economic failure, and asks what economics would succeed.",
 "how_it_works": "Researchers study supersonic transport through Boom's program, Concorde economics, and market analyses.",
 "key_points": [
  "Concorde proved feasibility, failed economically.",
  "Boom targets Mach 1.7 with new technology.",
  "Low-boom and efficiency are the bets.",
  "No supersonic airliner flies commercially.",
  "Premium markets are the assumed demand.",
 ],
 "requirements": [
  "Demonstrated profitable operations.",
  "Low-boom acceptability proof.",
  "Certified supersonic airliners.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Concorde operations history. Various; 1976-2003.",
  "Boom Supersonic. Overture program. 2016 onward.",
  "Rico F et al. Supersonic economics. Various; 2018-2023.",
  "NASA. Supersonic research. Various.",
 ],
 "demo_data": {"a": ("Concorde years of operation (approx)", 27.0),
               "b": ("years since retirement (approx)", 23.0), "bounds": (0.9, 1.5),
               "step1": "twenty-seven years flying, twenty-three grounded - the supersonic intermission",
               "confirm": "profitable supersonic operations",
               "refute": "supersonic economics prove never to close"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "aeroelasticity",
 "name": "Aeroelasticity: When Wings Bend",
 "group": "Structures",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Flexible wings flutter and diverge - how are ever-lighter, ever-flexibler wings kept stable?",
 "description": "Aeroelasticity - fluid-structure interaction - causes flutter (oscillation) and divergence (static instability); as wings get lighter and higher-aspect-ratio, the problems intensify. Active flutter suppression and morphing structures are the frontiers.",
 "background": "Flutter destroyed early aircraft; the theory matured mid-20th-century; active suppression (1970s-80s) showed promise; high-aspect-ratio wings (787, A350) pushed the envelope. As of 2026 passive design dominates with active control emerging.",
 "why_it_matters": "Lighter flexible wings save fuel: aeroelastic mastery enables the efficient airliner.",
 "sig_pointer": "The Signature system's proposed approach treats aeroelasticity as controllable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that aeroelasticity is actively controllable: the flutter and divergence suppressed by smart structures - enabling ultra-flexible wings. "
  "Assumptions: (1) control is achievable; (2) it is certifiable; (3) it enables lighter wings. "
  "Reasoning path: a control model explains the passive-design era and predicts active aeroelastic wings. "
  "Proposed mechanism: 'actively-controlled' aeroelasticity - smart suppression. "
  "What would confirm it: certified active-flutter-suppression wings. "
  "What would kill it: evidence that active control can't be certified. "
  "What this does not claim: it does not claim active wings fly, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads flexible wings as controllable, and asks what active suppression would enable.",
 "how_it_works": "Researchers study aeroelasticity through flutter testing, active-control research, and morphing-wing programs.",
 "key_points": [
  "Flutter and divergence threaten flexible wings.",
  "Lighter high-aspect-ratio wings intensify the problems.",
  "Passive design dominates current practice.",
  "Active suppression showed early promise.",
  "Certification is the barrier.",
 ],
 "requirements": [
  "Certified active flutter suppression.",
  "Ultra-flexible wings in service.",
  "Morphing structures proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bisplinghoff RL et al. Aeroelasticity classics. 1955.",
  "Noll TE et al. Active suppression. Various; 1980s-90s.",
  "Wright JR, Cooper JE. Modern aeroelasticity. 2015.",
  "Afzal F et al. Morphing wings. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("787 wingspan, meters (approx)", 60.0),
               "b": ("737 wingspan, meters (approx)", 36.0), "bounds": (1.4, 2.0),
               "step1": "wings growing longer and flexibler - the flutter frontier advancing",
               "confirm": "certified active-flutter-suppression wings",
               "refute": "active control proves uncertifiable"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "composite-fatigue",
 "name": "Composite Fatigue: The Unknown Lifespan",
 "group": "Structures",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Composite airframes don't fatigue like metal - but how they fail over decades is incompletely understood. What's their true lifespan?",
 "description": "Composite structures (787, A350 are majority composite) - lack metal's well-understood fatigue behavior: damage modes (delamination, matrix cracking) are complex, inspection is harder, and long-term aging data is limited. The fleet is young; the lifespan question is open.",
 "background": "Composites entered airframes progressively (1970s-2000s); the 787 (2011) was the composite leap; damage-tolerance philosophy adapted from metals. As of 2026 the oldest composite airliners are teenagers with lifespan unproven.",
 "why_it_matters": "Composite lifespan determines fleet economics and safety: the unknown at the heart of the modern airliner.",
 "sig_pointer": "The Signature system's proposed approach predicts composite lifespan from damage physics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that composite lifespan is predictable: the damage physics (delamination growth, matrix aging) modeled - with fleet data validating. "
  "Assumptions: (1) the physics is modelable; (2) models predict lifespan; (3) validation is feasible. "
  "Reasoning path: a physics model explains the uncertainty and predicts confident lifespans. "
  "Proposed mechanism: 'physics-predicted' composite lifespan - modeled aging. "
  "What would confirm it: models predicting fleet damage accurately. "
  "What would kill it: evidence that composite aging is unpredictable. "
  "What this does not claim: it does not claim any lifespan, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads composite aging as unmodeled physics, and asks what prediction would certify.",
 "how_it_works": "Researchers study composite fatigue through damage-mechanics research, fleet monitoring, and aging tests.",
 "key_points": [
  "Composites lack metal's understood fatigue behavior.",
  "Damage modes are complex and hard to inspect.",
  "The 787 was the composite leap (2011).",
  "Long-term aging data is limited.",
  "Lifespan is unproven.",
 ],
 "requirements": [
  "Validated damage-physics models.",
  "Fleet data confirming predictions.",
  "Confident lifespan certification.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Baker A et al. Composite airframe reviews. Various; 2004-2018.",
  "FAA. Composite damage tolerance. Various.",
  "Rouchon J et al. Composite aging. Various; 2010-2020.",
  "Soutis C et al. Composite fatigue. Various; 2005-2019.",
 ],
 "demo_data": {"a": ("787 composite content, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.4, 0.62),
               "step1": "half the airliner is composite - with lifespan physics still maturing",
               "confirm": "models predict fleet damage accurately",
               "refute": "composite aging proves unpredictable"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "boundary-layer",
 "name": "Boundary-Layer Transition Prediction",
 "group": "Aerodynamics",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Where laminar becomes turbulent - the transition point - can't be reliably predicted. Why is transition still unpredictable?",
 "description": "Boundary-layer transition - the switch from smooth to turbulent flow - determines drag and heating; but prediction relies on empirical correlations (e^n method) that fail in complex flows. The receptivity problem (how disturbances enter) is unsolved.",
 "background": "Transition research dates to Reynolds; the e^n method (1950s-60s) became standard; receptivity theory (Morkovin, Reshotko) framed the gap. DNS is revealing mechanisms. As of 2026 prediction remains semi-empirical.",
 "why_it_matters": "Transition prediction would enable designed laminar flow and accurate heating: the aerodynamic design bottleneck.",
 "sig_pointer": "The Signature system's proposed approach predicts transition from first principles, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that transition is predictable from receptivity: the disturbance-entry physics solved - with first-principles prediction. "
  "Assumptions: (1) receptivity is solvable; (2) it predicts transition; (3) it generalizes. "
  "Reasoning path: a receptivity model explains empirical limits and predicts design-grade transition. "
  "Proposed mechanism: 'receptivity-solved' transition prediction - first-principles. "
  "What would confirm it: first-principles predictions matching experiments. "
  "What would kill it: evidence that transition is inherently unpredictable. "
  "What this does not claim: it does not claim transition is predictable, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads transition as unsolved receptivity, and asks what physics would predict it.",
 "how_it_works": "Researchers study transition through DNS, receptivity experiments, and e^n-method improvements.",
 "key_points": [
  "Transition determines drag and heating.",
  "The e^n method is empirical and limited.",
  "Receptivity (disturbance entry) is unsolved.",
  "DNS is revealing mechanisms.",
  "Prediction remains semi-empirical.",
 ],
 "requirements": [
  "Solved receptivity physics.",
  "First-principles transition prediction.",
  "Design-grade accuracy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Morkovin MV. Receptivity. Various; 1969-1993.",
  "Reshotko E et al. Transition reviews. Various; 1976-2008.",
  "Schrauf G et al. e^n method. Various; 2005-2015.",
  "Zhong X et al. DNS transition. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("transition-prediction methods that are first-principles (approx)", 1.0),
               "b": ("transition-prediction methods used (approx)", 10.0), "bounds": (0.05, 0.18),
               "step1": "one in ten methods is first-principles - the prediction gap at drag's source",
               "confirm": "first-principles predictions match experiments",
               "refute": "transition proves inherently unpredictable"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "engine-efficiency",
 "name": "The Efficiency Limit of Jet Engines",
 "group": "Propulsion",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Jet engines approach thermodynamic limits - how much efficiency remains, and what comes after the turbofan?",
 "description": "Turbofan efficiency - propulsive plus thermal - has improved steadily; but Brayton-cycle limits, materials temperatures, and propulsive efficiency bound further gains. Open-rotor, hybrid-electric, and hydrogen concepts promise the next step; the ultimate limit is debated.",
 "background": "Turbofan efficiency doubled since the 1960s; geared turbofans (PW1000G) captured the latest gains; open-rotor (CFM RISE) targets the next. As of 2026 the turbofan is maturing with successors in development.",
 "why_it_matters": "Engine efficiency is aviation's climate lever: the remaining gains determine the industry's emissions path.",
 "sig_pointer": "The Signature system's proposed approach maps the post-turbofan future, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that post-turbofan propulsion needs architecture mapping: the efficiency potential of each successor quantified - guiding investment. "
  "Assumptions: (1) potentials are quantifiable; (2) they are comparable; (3) mapping guides the industry. "
  "Reasoning path: an architecture model explains the maturity and predicts the successor. "
  "Proposed mechanism: 'architecture-mapped' propulsion futures - quantified successor potentials. "
  "What would confirm it: mapped architectures delivering predicted gains. "
  "What would kill it: evidence that no successor beats the turbofan. "
  "What this does not claim: it does not claim any successor works, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads the turbofan as maturing, and asks what architecture succeeds it.",
 "how_it_works": "Researchers study engine efficiency through cycle analyses, open-rotor programs, and hybrid-electric research.",
 "key_points": [
  "Turbofan efficiency doubled since the 1960s.",
  "Thermodynamic and materials limits bound gains.",
  "Geared turbofans captured recent improvements.",
  "Open-rotor and hybrids are the candidates.",
  "The ultimate limit is debated.",
 ],
 "requirements": [
  "Quantified successor potentials.",
  "Demonstrated next-architecture gains.",
  "Industry transition guided by mapping.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cumpsty N. Jet Propulsion. Various editions.",
  "Epstein AH. Turbofan limits. Various; 2014-2019.",
  "CFM RISE open-rotor program. 2021 onward.",
  "NACA/NASA. Propulsion roadmaps. Various.",
 ],
 "demo_data": {"a": ("turbofan efficiency gain since 1960s, percent (approx)", 100.0),
               "b": ("remaining gain potential, percent (approx)", 25.0), "bounds": (3.0, 5.5),
               "step1": "doubled already, a quarter remaining - the maturing curve's tail",
               "confirm": "mapped architectures deliver predicted gains",
               "refute": "no successor proves to beat the turbofan"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "hydrogen-aviation",
 "name": "Hydrogen Aviation: The Fuel Switch",
 "group": "Propulsion",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Hydrogen could decarbonize flight - but its volume, infrastructure, and contrail effects are formidable. Can hydrogen aviation work?",
 "description": "Hydrogen aviation - burning or fuel-celling H2 - eliminates CO2; but liquid hydrogen's volume (4x kerosene), cryogenic handling, infrastructure absence, and uncertain contrail effects challenge it. Airbus targets 2035; the feasibility is debated.",
 "background": "Hydrogen flight was tested historically (Tu-155, 1988); Airbus ZEROe (2020) revived it; contrail research complicates the climate case. As of 2026 hydrogen aviation is in development with feasibility open.",
 "why_it_matters": "Hydrogen is aviation's main decarbonization bet: its feasibility determines the industry's climate future.",
 "sig_pointer": "The Signature system's proposed approach proves hydrogen aviation's system feasibility, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hydrogen aviation needs system proof: the aircraft, infrastructure, and climate benefit demonstrated together - not separately. "
  "Assumptions: (1) the system is the right unit; (2) it is demonstrable; (3) proof guides investment. "
  "Reasoning path: a systems model explains component optimism and predicts real feasibility. "
  "Proposed mechanism: 'system-proven' hydrogen aviation - integrated demonstration. "
  "What would confirm it: integrated demos showing viable operations. "
  "What would kill it: evidence that the system doesn't close. "
  "What this does not claim: it does not claim hydrogen aviation works, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads hydrogen as component promises, and asks what system proof would show.",
 "how_it_works": "Researchers study hydrogen aviation through ZEROe development, contrail research, and infrastructure studies.",
 "key_points": [
  "Hydrogen eliminates flight CO2.",
  "Liquid H2 needs 4x kerosene's volume.",
  "Infrastructure doesn't exist.",
  "Contrail effects are uncertain.",
  "Airbus targets 2035 entry.",
 ],
 "requirements": [
  "Integrated system demonstrations.",
  "Viable operations proven.",
  "Climate benefit including contrails.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Airbus ZEROe program. 2020 onward.",
  "Tu-155 hydrogen flights. 1988.",
  "Bock L et al. Hydrogen contrails. Various; 2020-2023.",
  "Nuttall WJ et al. Hydrogen aviation reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("hydrogen volume vs kerosene, fold (approx)", 4.0),
               "b": ("fold scale", 10.0), "bounds": (0.3, 0.52),
               "step1": "four times the tank volume - the packaging problem at hydrogen's heart",
               "confirm": "integrated demos show viable operations",
               "refute": "the system proves not to close"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "morphing-wings",
 "name": "Morphing Wings: The Shape-Shifting Airliner",
 "group": "Structures",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Birds morph wings continuously; airliners use discrete flaps. Can shape-shifting wings become practical?",
 "description": "Morphing wings - continuously adapting airfoil shape - promise optimal efficiency across flight regimes; but actuation weight, skin durability, and certification challenge practicality. NASA's ACTE (2014) flew compliant flaps; full morphing remains research.",
 "background": "Morphing concepts date decades; smart materials enabled new approaches; ACTE demonstrated compliant structures in flight. As of 2026 morphing is proven feasible with practicality pending.",
 "why_it_matters": "Morphing wings would optimize every flight phase: the efficiency of continuous adaptation.",
 "sig_pointer": "The Signature system's proposed approach makes morphing practical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that morphing needs practicality proof: the weight, durability, and certification demonstrated - with net benefit. "
  "Assumptions: (1) practicality is achievable; (2) net benefit is positive; (3) certification follows. "
  "Reasoning path: a practicality model explains research status and predicts operational morphing. "
  "Proposed mechanism: 'practicality-proven' morphing - certified net-benefit wings. "
  "What would confirm it: morphing wings in service with measured benefit. "
  "What would kill it: evidence that morphing never pays its weight. "
  "What this does not claim: it does not claim morphing wings fly commercially, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads morphing as feasible but impractical, and asks what proof would operationalize it.",
 "how_it_works": "Researchers study morphing through ACTE follow-ups, smart-materials research, and benefit analyses.",
 "key_points": [
  "Morphing promises optimal efficiency per flight phase.",
  "Actuation weight and skin durability challenge it.",
  "NASA ACTE flew compliant flaps (2014).",
  "Full morphing remains research.",
  "Net benefit is unproven.",
 ],
 "requirements": [
  "Certified morphing structures.",
  "Measured net benefit in service.",
  "Durable morphing skins.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NASA ACTE program. 2014.",
  "Barbarino S et al. Morphing reviews. Various; 2011-2019.",
  "Joo JJ et al. Morphing actuation. Various; 2015-2020.",
  "Kota S et al. Compliant structures. Various; 2010-2018.",
 ],
 "demo_data": {"a": ("morphing efficiency gain potential, percent (approx)", 8.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.12),
               "step1": "eight percent potential against unproven weight cost - the morphing ledger",
               "confirm": "morphing wings in service with measured benefit",
               "refute": "morphing proves never to pay its weight"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "wake-turbulence",
 "name": "Wake Turbulence: The Invisible Hazard",
 "group": "Operations",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Aircraft wakes endanger followers - separation standards waste capacity. Can wakes be predicted and mitigated?",
 "description": "Wake turbulence - wingtip vortices - forces separation minima that limit airport capacity; prediction (weather-dependent decay) and mitigation (vortex alleviation) are incomplete. RECAT reformed separations modestly; dynamic wake separation is the goal.",
 "background": "Wake accidents drove separation standards; RECAT (2010s) refined categories; lidar vortex tracking advanced. As of 2026 static separations dominate with dynamic concepts emerging.",
 "why_it_matters": "Wake separations limit the world's busiest airports: dynamic management would unlock capacity.",
 "sig_pointer": "The Signature system's proposed approach makes wake separation dynamic, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wake separation should be dynamic: real-time vortex prediction and weather-adaptive spacing - safely reducing minima. "
  "Assumptions: (1) prediction is accurate; (2) it is certifiable; (3) capacity gains are real. "
  "Reasoning path: a dynamic model explains static conservatism and predicts capacity unlock. "
  "Proposed mechanism: 'dynamically-managed' wake separation - adaptive spacing. "
  "What would confirm it: dynamic separations safely increasing throughput. "
  "What would kill it: evidence that wakes are unpredictable. "
  "What this does not claim: it does not claim dynamic separation is safe, offers no engineering advice, and does not constitute an operational recommendation."),
 "sig_lens": "The Signature lens reads separations as static conservatism, and asks what prediction would safely shrink.",
 "how_it_works": "Researchers study wakes through lidar tracking, RECAT analyses, and dynamic-separation trials.",
 "key_points": [
  "Wake vortices force capacity-limiting separations.",
  "RECAT refined categories modestly.",
  "Weather-dependent decay is predictable in principle.",
  "Dynamic separation is the goal.",
  "Static standards dominate practice.",
 ],
 "requirements": [
  "Accurate real-time wake prediction.",
  "Certified dynamic separations.",
  "Demonstrated throughput gains.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "RECAT program. Various; 2010s.",
  "Gerz T et al. Wake research. Various; 2002-2012.",
  "Holzapfel F et al. Wake prediction. Various; 2015-2020.",
  "FAA. Wake separation standards. Various.",
 ],
 "demo_data": {"a": ("capacity gain from dynamic separation, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.06, 0.16),
               "step1": "a tenth more capacity from smarter spacing - the invisible hazard's visible prize",
               "confirm": "dynamic separations safely increase throughput",
               "refute": "wakes prove unpredictable"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "icing",
 "name": "Aircraft Icing: The Unpredictable Threat",
 "group": "Operations",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Ice accretes on wings unpredictably - supercooled droplets defeat forecasting and protection. Can icing be predicted and prevented?",
 "description": "Aircraft icing - supercooled droplet accretion - causes performance loss and accidents; forecasting is imprecise; protection systems (bleed air, electrothermal) are heavy and incomplete. Supercooled large droplets (SLD) are the hardest threat.",
 "background": "Icing research dates to the 1940s; the ATR-72 Roselawn crash (1994) drove SLD regulation; protection systems improved incrementally. As of 2026 icing remains forecasted poorly and protected partially.",
 "why_it_matters": "Icing kills: better prediction and protection would remove a persistent accident cause.",
 "sig_pointer": "The Signature system's proposed approach predicts icing precisely, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that icing needs precise prediction: the microphysical forecasting and real-time detection enabling avoidance and targeted protection. "
  "Assumptions: (1) prediction is achievable; (2) detection works; (3) avoidance is practical. "
  "Reasoning path: a prediction model explains the accident persistence and predicts icing safety. "
  "Proposed mechanism: 'precisely-predicted' icing - forecasted and detected. "
  "What would confirm it: prediction systems preventing icing encounters. "
  "What would kill it: evidence that icing microphysics defeats forecasting. "
  "What this does not claim: it does not claim icing is predictable, offers no engineering advice, and does not constitute an operational recommendation."),
 "sig_lens": "The Signature lens reads icing as unforecast microphysics, and asks what prediction would prevent.",
 "how_it_works": "Researchers study icing through microphysics research, SLD regulation, and detection systems.",
 "key_points": [
  "Supercooled droplets accrete unpredictably.",
  "Forecasting is imprecise.",
  "Protection systems are heavy and partial.",
  "SLD is the hardest threat.",
  "Icing remains an accident cause.",
 ],
 "requirements": [
  "Precise microphysical forecasting.",
  "Real-time icing detection.",
  "Lightweight complete protection.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Roselawn ATR-72 accident. 1994.",
  "FAA. SLD regulations. Various; 2014 onward.",
  "Politovich MK et al. Icing forecasting. Various; 2003-2015.",
  "Lynch FT, Khodadoust A. Icing reviews. Various; 2001-2020.",
 ],
 "demo_data": {"a": ("icing-related accidents per decade (approx)", 30.0),
               "b": ("accidents scale (hundreds)", 100.0), "bounds": (0.2, 0.42),
               "step1": "thirty accidents a decade from a forecastable threat - the prediction gap's toll",
               "confirm": "prediction systems prevent icing encounters",
               "refute": "microphysics proves to defeat forecasting"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "contraails",
 "name": "Contrails: Aviation's Hidden Climate Impact",
 "group": "Environment",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Contrails may warm the climate more than aviation CO2 - but the science is uncertain and mitigation unproven. What's the real impact?",
 "description": "Contrail cirrus - ice clouds from exhaust - may cause more warming than aviation's CO2; but the magnitude is uncertain (estimates vary widely), and mitigation (altitude changes, cleaner fuel) is unproven at scale. The field debates whether contrails are aviation's main climate problem.",
 "background": "Contrail climate research grew in the 2000s-2010s (Burkhardt, Karcher); Lee (2021) assessed the effective radiative forcing. Avoidance trials are early. As of 2026 the impact is significant-but-uncertain.",
 "why_it_matters": "If contrails dominate aviation warming, mitigation transforms the industry's climate strategy.",
 "sig_pointer": "The Signature system's proposed approach quantifies and mitigates contrails, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that contrails need quantification then mitigation: the warming measured precisely - with avoidance proven operationally. "
  "Assumptions: (1) the impact is quantifiable; (2) avoidance works; (3) it is affordable. "
  "Reasoning path: a quantify-then-mitigate model explains the strategic uncertainty and predicts contrail policy. "
  "Proposed mechanism: 'quantified-mitigated' contrails - measured impact with proven avoidance. "
  "What would confirm it: precise warming attribution and operational avoidance. "
  "What would kill it: evidence that contrail impact is negligible or unavoidable. "
  "What this does not claim: it does not claim any warming number, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads contrails as uncertain warming, and asks what measurement would strategize.",
 "how_it_works": "Researchers study contrails through radiative-forcing research, avoidance trials, and fuel studies.",
 "key_points": [
  "Contrails may warm more than aviation CO2.",
  "The magnitude is highly uncertain.",
  "Mitigation (altitude, fuel) is unproven at scale.",
  "Lee (2021) assessed the forcing.",
  "The strategic question is open.",
 ],
 "requirements": [
  "Precise warming quantification.",
  "Proven operational avoidance.",
  "Climate strategy incorporating contrails.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Burkhardt U, Karcher B. Contrail cirrus. Various; 2009-2011.",
  "Lee DS et al. Aviation climate assessment. Atmospheric Environment. 2021;244:117834.",
  "Teoh R et al. Contrail avoidance. Various; 2020-2023.",
  "Grewe V et al. Mitigation reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("contrail warming vs aviation CO2, ratio (approx)", 1.5),
               "b": ("ratio scale", 10.0), "bounds": (0.1, 0.22),
               "step1": "one-and-a-half times the CO2 warming, possibly - the uncertain majority of aviation's climate impact",
               "confirm": "precise warming attribution and operational avoidance",
               "refute": "contrail impact proves negligible or unavoidable"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "urban-air-mobility",
 "name": "Urban Air Mobility: The Flying-Taxi Promise",
 "group": "Aviation",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "eVTOL air taxis promise urban flight - but certification, noise, economics, and air-traffic integration are all unsolved. Will UAM work?",
 "description": "Urban air mobility - electric VTOL air taxis - attracted billions; but the challenges compound: certifying novel aircraft, community noise acceptance, unit economics, vertiport infrastructure, and airspace integration. No UAM system operates commercially.",
 "background": "The eVTOL boom (2016-2021) brought investment; certification programs (Joby, Archer) advanced; but timelines slipped. As of 2026 commercial UAM is pending with skepticism growing.",
 "why_it_matters": "Working UAM would transform urban transport: the most hyped aviation promise of the decade.",
 "sig_pointer": "The Signature system's proposed approach proves UAM's system viability, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that UAM needs system proof: the aircraft, noise, economics, and airspace demonstrated together - in real cities. "
  "Assumptions: (1) the system is the right unit; (2) demos are feasible; (3) proof convinces markets. "
  "Reasoning path: a systems model explains component optimism and predicts real viability. "
  "Proposed mechanism: 'system-proven' UAM - integrated city demonstrations. "
  "What would confirm it: profitable quiet UAM operations. "
  "What would kill it: evidence that the system doesn't close. "
  "What this does not claim: it does not claim UAM works, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads UAM as component promises, and asks what integrated proof would show.",
 "how_it_works": "Researchers study UAM through certification programs, noise research, and economic modeling.",
 "key_points": [
  "Billions invested in eVTOL.",
  "Certification timelines slipped.",
  "Noise acceptance is unproven.",
  "Unit economics are uncertain.",
  "No commercial UAM operates.",
 ],
 "requirements": [
  "Certified eVTOL aircraft.",
  "Community noise acceptance.",
  "Profitable operations demonstrated.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Joby Aviation. Certification program. Various.",
  "Archer Aviation. Program updates. Various.",
  "NASA. UAM noise research. Various; 2020-2023.",
  "Cohen AP et al. UAM reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("eVTOL investment, billions (approx)", 10.0),
               "b": ("commercial UAM systems operating", 0.5), "bounds": (15.0, 25.0),
               "step1": "ten billion invested, zero systems operating - the hype-reality gap",
               "confirm": "profitable quiet UAM operations",
               "refute": "the system proves not to close"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "mars-entry",
 "name": "Mars Entry, Descent, and Landing",
 "group": "Space",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Landing heavy payloads on Mars - the thin atmosphere defeats parachutes, the thick enough for heating. How do humans land?",
 "description": "Mars EDL - landing large masses - is the critical Mars-mission technology: the atmosphere is too thin for parachute-only landing of heavy payloads, too thick to ignore. Supersonic retropropulsion (SpaceX) and inflatable heat shields (LOFTID, 2022) are candidates; human-scale landing is unproven.",
 "background": "Robotic landings succeeded to ~1 ton (MSL, 2012); human missions need 20+ tons. LOFTID (2022) proved inflatable aeroshells; Starship plans retropropulsion. As of 2026 human-scale Mars EDL is unproven.",
 "why_it_matters": "Mars EDL enables human Mars missions: the landing problem at exploration's frontier.",
 "sig_pointer": "The Signature system's proposed approach proves human-scale Mars EDL, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that Mars EDL needs scaled demonstration: the 20-ton landing proven - by the method that works. "
  "Assumptions: (1) a method exists; (2) it scales; (3) demos prove it. "
  "Reasoning path: a demonstration model explains the robotic-human gap and predicts Mars landing. "
  "Proposed mechanism: 'scale-proven' Mars EDL - demonstrated heavy landing. "
  "What would confirm it: 20-ton Mars landing demonstrations. "
  "What would kill it: evidence that no method scales. "
  "What this does not claim: it does not claim Mars landing is solved, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads Mars EDL as unscaled success, and asks what demonstration would prove heavy landing.",
 "how_it_works": "Researchers study Mars EDL through LOFTID follow-ups, retropropulsion research, and architecture studies.",
 "key_points": [
  "Robotic landings reached ~1 ton.",
  "Human missions need 20+ tons.",
  "LOFTID proved inflatable aeroshells (2022).",
  "Retropropulsion is SpaceX's approach.",
  "Human-scale EDL is unproven.",
 ],
 "requirements": [
  "20-ton landing demonstrations.",
  "Validated EDL architectures.",
  "Human-rated Mars landing systems.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "MSL EDL. Various; 2012.",
  "NASA LOFTID. 2022.",
  "Braun RD et al. Mars EDL reviews. Various; 2006-2020.",
  "SpaceX. Starship Mars architecture. Various.",
 ],
 "demo_data": {"a": ("human Mars landing mass needed, tons (approx)", 20.0),
               "b": ("largest Mars landing, tons (approx)", 1.0), "bounds": (15.0, 25.0),
               "step1": "twenty times the landed mass needed - the scaling gap at Mars",
               "confirm": "20-ton Mars landing demonstrations",
               "refute": "no method proves to scale"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "space-nuclear",
 "name": "Space Nuclear Power",
 "group": "Space",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Deep-space missions need nuclear power - but reactors in space face political, safety, and technical barriers. Can space nuclear scale?",
 "description": "Space nuclear power - fission reactors and advanced RTGs - enables outer-planet missions and lunar bases; but launch safety, political opposition, and cost limit it. Kilopower/KRUSTY (2018) proved small reactors; flight systems are pending.",
 "background": "RTGs powered Voyagers; fission was tested (SNAP-10A, 1965); Kilopower revived the field. As of 2026 space fission is proven on the ground, unflown.",
 "why_it_matters": "Space nuclear enables the outer solar system and permanent Moon/Mars presence: the power for deep space.",
 "sig_pointer": "The Signature system's proposed approach flies space reactors, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that space nuclear needs flight: the demonstrated reactors flown - proving safe operation. "
  "Assumptions: (1) ground demos suffice technically; (2) flight is politically achievable; (3) operations prove out. "
  "Reasoning path: a flight model explains the ground-flight gap and predicts space nuclear power. "
  "Proposed mechanism: 'flown' space nuclear - operational reactors in space. "
  "What would confirm it: reactor-powered deep-space missions. "
  "What would kill it: evidence that space reactors can't fly politically or safely. "
  "What this does not claim: it does not claim space reactors fly, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads space nuclear as ground-proven, and asks what flight would unlock.",
 "how_it_works": "Researchers study space nuclear through Kilopower follow-ups, safety analyses, and mission studies.",
 "key_points": [
  "RTGs powered outer-planet missions.",
  "Kilopower proved small fission (2018).",
  "Launch safety and politics are barriers.",
  "No fission reactor has flown since 1965.",
  "Deep space needs nuclear power.",
 ],
 "requirements": [
  "Flown fission reactors.",
  "Demonstrated launch safety.",
  "Operational deep-space nuclear power.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "SNAP-10A flight. 1965.",
  "Gibson MA et al. Kilopower/KRUSTY. Various; 2018-2020.",
  "Mason LS et al. Space reactor reviews. Various; 2020-2023.",
  "NASA. Fission surface power program. Various.",
 ],
 "demo_data": {"a": ("years since a fission reactor flew in space (approx)", 60.0),
               "b": ("years scale", 100.0), "bounds": (0.5, 0.72),
               "step1": "sixty years since SNAP-10A - the power source that never returned to orbit",
               "confirm": "reactor-powered deep-space missions",
               "refute": "space reactors prove un-flyable"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "in-space-manufacturing",
 "name": "In-Space Manufacturing",
 "group": "Space",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Building in space avoids launch constraints - but microgravity manufacturing is barely proven. What can be made off-Earth?",
 "description": "In-space manufacturing - 3D printing, fiber optics (ZBLAN), pharmaceuticals in microgravity - promises products impossible on Earth; but the ISS demos are small, economics are unproven, and the business case is early.",
 "background": "ISS manufacturing demos (2010s-2020s) showed feasibility; ZBLAN fiber drew commercial interest; Varda targets pharmaceuticals. As of 2026 in-space manufacturing is demonstrated with economics pending.",
 "why_it_matters": "Proven in-space manufacturing would create the orbital economy: the industrialization of space.",
 "sig_pointer": "The Signature system's proposed approach proves in-space manufacturing economics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that in-space manufacturing needs economic proof: the products whose space-made value exceeds the cost - demonstrated at scale. "
  "Assumptions: (1) such products exist; (2) scale is achievable; (3) economics close. "
  "Reasoning path: an economics model explains demo-status and predicts orbital industry. "
  "Proposed mechanism: 'economically-proven' in-space manufacturing - profitable orbital production. "
  "What would confirm it: profitable space-made products. "
  "What would kill it: evidence that no product justifies the cost. "
  "What this does not claim: it does not claim orbital industry exists, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads orbital manufacturing as unproven economics, and asks what products would justify it.",
 "how_it_works": "Researchers study in-space manufacturing through ISS demos, ZBLAN trials, and economic analyses.",
 "key_points": [
  "Microgravity enables unique products.",
  "ISS demos proved feasibility.",
  "ZBLAN fiber is the leading candidate.",
  "Economics are unproven.",
  "The business case is early.",
 ],
 "requirements": [
  "Profitable space-made products.",
  "Scaled orbital production.",
  "Economic proof of the industry.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "ISS manufacturing demonstrations. Various; 2014-2023.",
  "Varda Space Industries. Various; 2021 onward.",
  "ZBLAN fiber research. Various; 2015-2022.",
  "Skomorowski et al. Space manufacturing reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("in-space manufacturing revenue, millions of dollars (approx)", 10.0),
               "b": ("terrestrial manufacturing, millions of dollars (approx)", 15000000.0), "bounds": (0.0000004, 0.0000009),
               "step1": "ten million against fifteen trillion - the orbital economy's infancy",
               "confirm": "profitable space-made products",
               "refute": "no product proves to justify the cost"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "lunar-infrastructure",
 "name": "Lunar Infrastructure: Building on the Moon",
 "group": "Space",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Permanent lunar presence needs power, shelter, and resources - but lunar construction is unproven. How do we build on the Moon?",
 "description": "Lunar infrastructure - habitats, power systems, ISRU (in-situ resource utilization) - is required for Artemis' sustained presence; but regolith construction, dust mitigation, and lunar-night power are unsolved engineering.",
 "background": "Apollo proved visits; Artemis plans presence; ISRU research (oxygen from regolith) advanced; dust remains the unsolved nuisance. As of 2026 lunar infrastructure is in development.",
 "why_it_matters": "Lunar infrastructure enables the Moon as humanity's second home and Mars' staging point.",
 "sig_pointer": "The Signature system's proposed approach builds lunar infrastructure stepwise, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that lunar infrastructure builds stepwise: the power, shelter, and ISRU demonstrated incrementally - with dust solved. "
  "Assumptions: (1) stepwise demos work; (2) dust is solvable; (3) presence follows. "
  "Reasoning path: a stepwise model explains the development status and predicts lunar settlement. "
  "Proposed mechanism: 'stepwise-built' lunar infrastructure - demonstrated capabilities. "
  "What would confirm it: operational lunar infrastructure elements. "
  "What would kill it: evidence that lunar construction is infeasible. "
  "What this does not claim: it does not claim lunar bases exist, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads the Moon as unbuilt infrastructure, and asks what stepwise demos would establish.",
 "how_it_works": "Researchers study lunar infrastructure through ISRU research, dust-mitigation studies, and Artemis planning.",
 "key_points": [
  "Artemis plans sustained lunar presence.",
  "ISRU (oxygen from regolith) is advancing.",
  "Lunar dust is the unsolved nuisance.",
  "Lunar-night power is unsolved.",
  "Construction is unproven.",
 ],
 "requirements": [
  "Demonstrated ISRU at scale.",
  "Dust-mitigation solutions.",
  "Operational lunar infrastructure.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NASA Artemis program. Various; 2019 onward.",
  "Sanders GB et al. ISRU reviews. Various; 2010-2020.",
  "Gaier JR et al. Lunar dust. Various; 2005-2020.",
  "Crawford IA et al. Lunar infrastructure. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("lunar infrastructure elements operational (approx)", 2.0),
               "b": ("elements needed for presence (approx)", 20.0), "bounds": (0.05, 0.18),
               "step1": "two of twenty elements operational - the Moon's unbuilt foundation",
               "confirm": "operational lunar infrastructure elements",
               "refute": "lunar construction proves infeasible"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "asteroid-mining",
 "name": "Asteroid Mining: The Resource Frontier",
 "group": "Space",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Asteroids hold trillions in resources - but extraction economics are unproven. Can space mining work?",
 "description": "Asteroid mining - extracting water and metals from near-Earth asteroids - promises space resources; but prospecting, extraction in microgravity, and the economics (launch costs vs resource value) are unproven. Companies rose and fell (Planetary Resources).",
 "background": "The asteroid-mining boom (2010s) brought investment; technical and economic reality deflated it; water-for-propellant remains the plausible first product. As of 2026 asteroid mining is concept with demos pending.",
 "why_it_matters": "Working asteroid mining would supply space activity without Earth's gravity well: the resource base of the space age.",
 "sig_pointer": "The Signature system's proposed approach proves asteroid-mining economics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that asteroid mining needs economic proof: the water-first business case demonstrated - with extraction proven. "
  "Assumptions: (1) water is the first product; (2) extraction works; (3) economics close. "
  "Reasoning path: an economics model explains the boom-bust and predicts real mining. "
  "Proposed mechanism: 'economically-proven' asteroid mining - profitable extraction. "
  "What would confirm it: profitable asteroid-extracted water. "
  "What would kill it: evidence that extraction never pays. "
  "What this does not claim: it does not claim asteroid mining works, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads asteroid mining as unproven economics, and asks what water-first proof would show.",
 "how_it_works": "Researchers study asteroid mining through prospecting research, extraction demos, and economic modeling.",
 "key_points": [
  "Asteroids hold vast water and metal resources.",
  "The 2010s boom deflated on reality.",
  "Water-for-propellant is the plausible first product.",
  "Extraction in microgravity is unproven.",
  "Economics are the barrier.",
 ],
 "requirements": [
  "Demonstrated microgravity extraction.",
  "Profitable water production.",
  "Economic proof of the industry.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Planetary Resources / Deep Space Industries. Various; 2012-2019.",
  "Elvis M et al. Asteroid mining reviews. Various; 2014-2021.",
  "Sercel JC et al. Water mining concepts. Various; 2018-2022.",
  "Crawford IA et al. Space resources. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("asteroid-mining revenue to date, millions (approx)", 1.0),
               "b": ("investment in asteroid mining, millions (approx)", 100.0), "bounds": (0.005, 0.02),
               "step1": "a million earned on a hundred million invested - the frontier's ledger",
               "confirm": "profitable asteroid-extracted water",
               "refute": "extraction proves never to pay"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "interstellar",
 "name": "Interstellar Flight: The Ultimate Challenge",
 "group": "Space",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "The stars are light-years away - is interstellar flight possible, even in principle?",
 "description": "Interstellar flight - reaching other stars - needs propulsion far beyond chemical: fusion, antimatter, beamed sails (Breakthrough Starshot), or generation ships. The physics is speculative; the engineering is centuries-scale.",
 "background": "Daedalus (1970s) studied fusion starships; Starshot (2016) proposed laser-driven sails; physics allows but engineering doesn't. As of 2026 interstellar flight is speculative with active concepts.",
 "why_it_matters": "Interstellar flight is humanity's ultimate journey: the question of whether the stars are reachable.",
 "sig_pointer": "The Signature system's proposed approach treats interstellar flight as a physics-first problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that interstellar flight needs physics breakthroughs: the propulsion physics proven before engineering - with concepts matured stepwise. "
  "Assumptions: (1) physics allows it; (2) breakthroughs are achievable; (3) stepwise maturation works. "
  "Reasoning path: a physics-first model explains the speculative status and predicts eventual flight. "
  "Proposed mechanism: 'physics-proven' interstellar concepts - demonstrated propulsion physics. "
  "What would confirm it: breakthrough propulsion demonstrations. "
  "What would kill it: evidence that interstellar flight is physically impossible. "
  "What this does not claim: it does not claim interstellar flight is possible, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads the stars as physics-limited, and asks what breakthroughs would reach them.",
 "how_it_works": "Researchers study interstellar flight through Starshot research, fusion-propulsion studies, and physics analyses.",
 "key_points": [
  "Chemical propulsion can't reach the stars.",
  "Fusion, antimatter, and beamed sails are concepts.",
  "Breakthrough Starshot proposes laser sails.",
  "The engineering is centuries-scale.",
  "Physics allows; engineering doesn't.",
 ],
 "requirements": [
  "Breakthrough propulsion physics.",
  "Demonstrated interstellar-capable systems.",
  "Stepwise concept maturation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Project Daedalus. Various; 1973-1978.",
  "Breakthrough Starshot. 2016 onward.",
  "Long KF et al. Interstellar reviews. Various; 2012-2022.",
  "Crawford IA et al. Interstellar feasibility. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("nearest star distance, light-years (approx)", 4.2),
               "b": ("Voyager speed, light-years per year (approx)", 0.000005), "bounds": (600000.0, 1100000.0),
               "step1": "four light-years at Voyager's crawl - eight hundred thousand years of travel",
               "confirm": "breakthrough propulsion demonstrations",
               "refute": "interstellar flight proves physically impossible"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "aerospace-theory",
 "name": "A Unified Theory of Flight",
 "group": "Theory",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Aerodynamics, structures, propulsion, and control are separate disciplines - can flight be understood as one system?",
 "description": "Aerospace engineering is fragmented: aerodynamicists, structural engineers, and propulsion specialists optimize separately; multidisciplinary optimization is emerging but the unified theory - flight as one coupled system - doesn't exist.",
 "background": "MDO (multidisciplinary design optimization) grew in the 1990s-2000s; coupled simulations are advancing. As of 2026 the disciplines cooperate without unifying.",
 "why_it_matters": "Unified flight theory would optimize the whole vehicle: the systems science of aerospace.",
 "sig_pointer": "The Signature system's proposed approach unifies flight disciplines computationally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that flight disciplines unify computationally: the coupled aero-structural-propulsive-control models - with emergent optima. "
  "Assumptions: (1) coupling is modelable; (2) unified models optimize better; (3) they are tractable. "
  "Reasoning path: a computational model explains disciplinary fragmentation and predicts unified design. "
  "Proposed mechanism: 'computationally-unified' flight design - coupled optimization. "
  "What would confirm it: unified designs beating disciplinary ones. "
  "What would kill it: evidence that coupling defeats optimization. "
  "What this does not claim: it does not claim a unified theory exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads aerospace as fragmented disciplines, and asks what coupling would optimize.",
 "how_it_works": "Researchers study flight theory through MDO research, coupled simulations, and systems analyses.",
 "key_points": [
  "Aerospace disciplines optimize separately.",
  "MDO couples them computationally.",
  "No unified theory of flight exists.",
  "Coupled optima differ from disciplinary ones.",
  "Systems science is emerging.",
 ],
 "requirements": [
  "Tractable coupled models.",
  "Unified designs beating disciplinary ones.",
  "Disciplinary adoption of coupling.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sobieszczanski-Sobieski et al. MDO. Various; 1990s-2000s.",
  "Martins JRRA et al. MDO reviews. Various; 2013-2021.",
  "Nicolai LM et al. Systems design. Various editions.",
  "Raymer DP. Aircraft design systems. Various editions.",
 ],
 "demo_data": {"a": ("design disciplines optimized jointly (approx)", 3.0),
               "b": ("aerospace disciplines (approx)", 8.0), "bounds": (0.25, 0.5),
               "step1": "three of eight disciplines jointly optimized - the fragmented design of flight",
               "confirm": "unified designs beat disciplinary ones",
               "refute": "coupling proves to defeat optimization"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "supersonic-business",
 "name": "Supersonic Business Aviation",
 "group": "Aviation",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Supersonic business jets promise speed for the wealthy - but the market, noise, and economics are all uncertain. Is there a business case?",
 "description": "Supersonic business jets - smaller than airliners, premium-priced - are proposed by startups; but the development costs, sonic-boom restrictions, and market size are all questionable. No supersonic business jet has flown.",
 "background": "Aerion's AS2 (2014-2021) was the leading attempt; it collapsed on funding. Spike and others continue. As of 2026 the segment is conceptual.",
 "why_it_matters": "The business jet is supersonic's easiest market: its viability tests the whole supersonic return.",
 "sig_pointer": "The Signature system's proposed approach proves the supersonic business case, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that supersonic business aviation needs market proof: the demand, economics, and certification demonstrated - at business-jet scale. "
  "Assumptions: (1) the market exists; (2) economics close at small scale; (3) certification is achievable. "
  "Reasoning path: a market model explains Aerion's failure and predicts viable supersonic business flight. "
  "Proposed mechanism: 'market-proven' supersonic business jets - demonstrated demand and economics. "
  "What would confirm it: flying certified supersonic business jets. "
  "What would kill it: evidence that the market doesn't exist. "
  "What this does not claim: it does not claim supersonic business jets fly, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads supersonic business flight as unproven market, and asks what proof would launch it.",
 "how_it_works": "Researchers study supersonic business aviation through market analyses, Aerion lessons, and certification research.",
 "key_points": [
  "Aerion's AS2 collapsed on funding (2021).",
  "No supersonic business jet has flown.",
  "Development costs are enormous.",
  "Boom restrictions limit routes.",
  "Market size is uncertain.",
 ],
 "requirements": [
  "Demonstrated market demand.",
  "Certified supersonic business jets.",
  "Viable unit economics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Aerion Supersonic. AS2 program. 2014-2021.",
  "Spike Aerospace. Various; 2013 onward.",
  "Rico F et al. Supersonic market analyses. Various; 2018-2023.",
  "FAA. Supersonic business-jet studies. Various.",
 ],
 "demo_data": {"a": ("supersonic business jets flying", 0.5),
               "b": ("business jets flying, thousands (approx)", 20.0), "bounds": (0.015, 0.04),
               "step1": "zero supersonic of twenty thousand business jets - the speed the market hasn't bought",
               "confirm": "flying certified supersonic business jets",
               "refute": "the market proves not to exist"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "air-traffic",
 "name": "The Future Air-Traffic System",
 "group": "Operations",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Air traffic doubles every 15 years - can the control system scale, or does it need reinvention?",
 "description": "Air-traffic management - radar, voice, fixed routes - strains under growth; NextGen/SESAR modernize incrementally; but drones, UAM, and supersonic need a reinvented system. Trajectory-based operations and automation are the path; the transition is slow.",
 "background": "NextGen (2000s onward) and SESAR modernized incrementally; drone integration (UTM) is emerging; full trajectory-based operations are pending. As of 2026 the system scales with strain.",
 "why_it_matters": "The air-traffic system is aviation's nervous system: its reinvention enables all future flight.",
 "sig_pointer": "The Signature system's proposed approach reinvents air-traffic management, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that air traffic needs trajectory-based reinvention: the automated, trajectory-managed system - handling all airspace users. "
  "Assumptions: (1) the technology exists; (2) transition is manageable; (3) it scales. "
  "Reasoning path: a reinvention model explains incremental strain and predicts scalable ATM. "
  "Proposed mechanism: 'trajectory-reinvented' air traffic - automated management. "
  "What would confirm it: trajectory-based operations at scale. "
  "What would kill it: evidence that the legacy system can't transition. "
  "What this does not claim: it does not claim reinvented ATM exists, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads air traffic as strained legacy, and asks what reinvention would scale.",
 "how_it_works": "Researchers study ATM through NextGen/SESAR evaluations, UTM development, and trajectory research.",
 "key_points": [
  "Air traffic doubles every ~15 years.",
  "NextGen/SESAR modernize incrementally.",
  "Drones and UAM need new airspace.",
  "Trajectory-based operations are pending.",
  "The system scales with strain.",
 ],
 "requirements": [
  "Trajectory-based operations at scale.",
  "Integrated drone/UAM airspace.",
  "Automated management proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "FAA NextGen program. Various; 2000s onward.",
  "SESAR program. Various; 2000s onward.",
  "NASA UTM research. Various; 2015-2022.",
  "EUROCONTROL. ATM modernization. Various.",
 ],
 "demo_data": {"a": ("annual flights, millions (approx)", 40.0),
               "b": ("system capacity, millions (approx)", 50.0), "bounds": (0.65, 0.95),
               "step1": "forty million flights against fifty million capacity - the strain before the doubling",
               "confirm": "trajectory-based operations at scale",
               "refute": "the legacy system proves unable to transition"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "space-tourism-safety",
 "name": "Space Tourism Safety",
 "group": "Space",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Space tourism flies civilians - but the safety standards are informed consent, not certification. What should civilian spaceflight safety be?",
 "description": "Space tourism - suborbital and orbital civilian flights - operates under informed-consent regimes, not airliner certification. The safety record is short; the acceptable risk is undefined; a fatal accident could end the industry.",
 "background": "Virgin Galactic and Blue Origin fly suborbitally; SpaceX flies orbital tourists; the FAA's learning period limits regulation. As of 2026 civilian spaceflight is lightly regulated with safety unproven at scale.",
 "why_it_matters": "Space tourism's safety determines the industry's future: one disaster could ground it for a generation.",
 "sig_pointer": "The Signature system's proposed approach defines civilian spaceflight safety, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that space tourism needs defined safety standards: the certification-equivalent safety case - with acceptable risk explicit. "
  "Assumptions: (1) standards are definable; (2) they are achievable; (3) the industry accepts. "
  "Reasoning path: a standards model explains the regulatory gap and predicts safe space tourism. "
  "Proposed mechanism: 'standards-defined' space tourism - certified civilian safety. "
  "What would confirm it: certified operations with strong safety records. "
  "What would kill it: evidence that spaceflight can't be made safe enough. "
  "What this does not claim: it does not claim space tourism is safe, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads space tourism as unregulated risk, and asks what standards would make safe.",
 "how_it_works": "Researchers study space-tourism safety through flight records, risk analyses, and regulatory research.",
 "key_points": [
  "Civilian spaceflight uses informed consent, not certification.",
  "The safety record is short.",
  "Acceptable risk is undefined.",
  "A fatal accident could end the industry.",
  "Regulation is in a learning period.",
 ],
 "requirements": [
  "Defined safety standards.",
  "Certified civilian operations.",
  "Strong safety records at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "FAA. Human spaceflight regulations. Various.",
  "Virgin Galactic / Blue Origin flight programs. Various.",
  "SpaceX. Civilian missions. Various; 2021 onward.",
  "Pelton JN et al. Space tourism safety. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("civilians flown to space (approx)", 600.0),
               "b": ("airline passengers yearly, billions (approx)", 4.0), "bounds": (100.0, 200.0),
               "step1": "six hundred civilians against four billion airline passengers - the safety sample's infancy",
               "confirm": "certified operations with strong safety records",
               "refute": "spaceflight proves unable to be made safe enough"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "hypersonic-weapons-arms",
 "name": "Hypersonic Arms Dynamics",
 "group": "Policy",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Hypersonic weapons compress decision time - how does aerospace engineering account for strategic stability?",
 "description": "Hypersonic weapons - maneuverable Mach 5+ delivery - challenge missile defense and compress response time; the strategic-stability implications are debated; arms-control frameworks don't cover them. The engineering-policy interface is unresolved.",
 "background": "Hypersonic weapon programs accelerated in the 2010s-2020s (US, Russia, China); strategic-stability research is active. As of 2026 the weapons exist with the stability framework pending.",
 "why_it_matters": "Hypersonic arms dynamics could destabilize deterrence: the engineering with strategic consequences.",
 "sig_pointer": "The Signature system's proposed approach addresses hypersonic stability, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hypersonic stability needs engineering-informed policy: the technical realities (timelines, defenses) grounding arms frameworks. "
  "Assumptions: (1) technical facts are knowable; (2) they inform policy; (3) frameworks are achievable. "
  "Reasoning path: a technical model explains the policy gap and predicts stable frameworks. "
  "Proposed mechanism: 'technically-grounded' hypersonic policy - engineering-informed stability. "
  "What would confirm it: frameworks incorporating technical realities. "
  "What would kill it: evidence that hypersonics inherently destabilize. "
  "What this does not claim: it takes no position on weapons programs, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads hypersonics as policy-lagging technology, and asks what technical grounding would stabilize.",
 "how_it_works": "Researchers study hypersonic stability through technical analyses, arms-control research, and strategic studies.",
 "key_points": [
  "Hypersonic weapons compress decision time.",
  "Missile defense is challenged.",
  "Arms-control frameworks don't cover them.",
  "Programs are active in major powers.",
  "The stability framework is pending.",
 ],
 "requirements": [
  "Technically-grounded policy frameworks.",
  "Strategic-stability assessments.",
  "Engineering-informed arms control.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Acton JM et al. Hypersonic stability. Various; 2019-2023.",
  "Tracy CL et al. Technical analyses. Various; 2020-2023.",
  "Speier RH et al. Arms control reviews. Various; 2017-2022.",
  "RAND. Hypersonic studies. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("decision time with hypersonics, minutes (approx)", 10.0),
               "b": ("decision time with ICBMs, minutes (approx)", 30.0), "bounds": (0.25, 0.45),
               "step1": "ten minutes against thirty - the compressed timeline of hypersonic decision",
               "confirm": "frameworks incorporating technical realities",
               "refute": "hypersonics prove inherently destabilizing"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "sustainable-aviation",
 "name": "Sustainable Aviation's Path",
 "group": "Environment",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Aviation must decarbonize - but SAF, hydrogen, and electric each face limits. What's the real path to sustainable flight?",
 "description": "Sustainable aviation - net-zero flight - needs some combination of sustainable aviation fuel (SAF, limited feedstock), hydrogen (volume challenges), electric (range limits), and operational efficiency. No single path suffices; the mix is debated.",
 "background": "SAF mandates spread (EU, 2020s); hydrogen and electric develop; ICAO's CORSIA addresses emissions. As of 2026 the path is multi-track with no dominant solution.",
 "why_it_matters": "Aviation's climate future depends on the right mix: the industry's existential strategy.",
 "sig_pointer": "The Signature system's proposed approach optimizes aviation's decarbonization mix, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that aviation decarbonization needs mix optimization: the SAF-hydrogen-electric-efficiency combination that achieves net-zero - computed per mission. "
  "Assumptions: (1) the mix is optimizable; (2) it is computable; (3) it guides investment. "
  "Reasoning path: an optimization model explains the multi-track debate and predicts the winning mix. "
  "Proposed mechanism: 'mix-optimized' sustainable aviation - computed decarbonization. "
  "What would confirm it: optimized mixes achieving net-zero. "
  "What would kill it: evidence that no mix achieves net-zero. "
  "What this does not claim: it does not claim any path works, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads sustainability as unoptimized mix, and asks what computation would find.",
 "how_it_works": "Researchers study sustainable aviation through SAF lifecycle analyses, hydrogen assessments, and mix modeling.",
 "key_points": [
  "SAF faces feedstock limits.",
  "Hydrogen faces volume challenges.",
  "Electric faces range limits.",
  "No single path suffices.",
  "The mix is debated.",
 ],
 "requirements": [
  "Optimized decarbonization mixes.",
  "Net-zero demonstrated per mission.",
  "Investment guided by optimization.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "ICAO CORSIA. Various; 2016 onward.",
  "EU SAF mandates. Various; 2020s.",
  "Mukhopadhaya J et al. Aviation decarbonization. Various; 2022-2024.",
  "Graver B et al. ICCT aviation analyses. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("SAF share of jet fuel, percent (approx)", 0.5),
               "b": ("SAF needed for net-zero, percent (approx)", 65.0), "bounds": (0.004, 0.012),
               "step1": "half a percent against sixty-five needed - the sustainable fuel's scale gap",
               "confirm": "optimized mixes achieve net-zero",
               "refute": "no mix proves able to achieve net-zero"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "flight-future",
 "name": "The Future of Flight: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "What will flight look like in a century? The field extrapolates poorly - can aerospace's future be foreseen?",
 "description": "Aerospace futurology - predicting flight's century - is speculative: past predictions (flying cars by 2000) failed; the field needs structured foresight. Whether systematic futures work improves decisions is the meta-question.",
 "background": "Aerospace predictions have a poor record; scenario methods are used sporadically. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (infrastructure, research) need foresight: the discipline of aerospace futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined aerospace foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that aerospace futures need disciplined foresight: the scenario methods and technology roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains prediction failures and predicts better futures work. "
  "Proposed mechanism: 'disciplined' aerospace foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that aerospace futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads aerospace futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study aerospace futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "Aerospace predictions have a poor record.",
  "Flying cars were promised by 2000.",
  "Scenario methods are used sporadically.",
  "Long-horizon decisions need foresight.",
  "The discipline is undeveloped.",
 ],
 "requirements": [
  "Validated foresight methods.",
  "Track records for predictions.",
  "Decisions guided by foresight.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NASA. Technology roadmaps. Various.",
  "Bilstein RE. Aerospace prediction histories. Various.",
  "Stern N et al. Foresight methods. Various; 2018-2022.",
  "AIAA. Futures workshops. Various.",
 ],
 "demo_data": {"a": ("aerospace predictions with validated track records (approx)", 5.0),
               "b": ("aerospace predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "aerospace futures prove unforeseeable"},
},
]
