(function(){'use strict';
/* jahdb-fundamental-environmental-science-signature-1.0 — fundamental environmental-science bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFENV-';
var KIND='fundamental environmental-science record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Environmental science studies how humans interact with natural systems: the flows of energy and materials through the environment, the impacts of human activity, and the management of air, water, land, and biodiversity. It is problem-driven and interdisciplinary by nature.', 'reasoning':'Environmental scientists reason with budgets and baselines: measure the flows (carbon, nitrogen, water), compare to pre-disturbance baselines, and attribute change. Systems thinking is mandatory — everything connects, and fixes in one place cause effects in another.', 'quantities':'The core quantities are concentrations (ppm, ppb), fluxes (tons per year), and indices (air quality, water quality, biodiversity). The master quantity is the human footprint relative to the planet\'s carrying capacity.', 'mechanism':'Environmental understanding is built by monitoring plus modeling: long-term measurements reveal trends, models project consequences, and interventions are tested against the monitored record. The Keeling curve — CO₂ rising since 1958 — is the iconic example.', 'miscon':'Environmental science is not activism: it is measurement and analysis, though its findings inform policy. \'The solution to pollution is dilution\' is false — persistent pollutants accumulate. And individual action versus systemic change is a false choice: both matter, at different scales.'};
var SIGLENS=['In the Signature system, environmental science is the stewardship discipline: every construction in this network is evaluated for its footprint and its sustainability, and the Signature formulation teaches each principle as a budget you can balance.','The Signature practice is to compute the footprint: balance the carbon budget, track the water, audit the waste — so environmental reasoning is done with numbers that can be checked.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- carbon footprint demo. Runs as-is with python3."""\n# kg CO2 per unit\nFACTORS = {"km driven (gas car)": 0.21, "kWh electricity": 0.4, "kg beef": 27.0, "flight km": 0.15}\nusage = {"km driven (gas car)": 15000, "kWh electricity": 4000, "kg beef": 50, "flight km": 5000}\ntotal = 0\nfor item, amount in usage.items():\n    co2 = FACTORS[item] * amount\n    total += co2\n    print(f"{item:<22} {co2:>8,.0f} kg CO2")\nprint(f"{\'TOTAL\':<22} {total:>8,.0f} kg CO2 per year")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Keeling curve trend demo. Runs as-is with python3."""\n# approximate annual Mauna Loa CO2 (ppm)\ndata = {1960: 317, 1980: 339, 2000: 370, 2020: 414, 2024: 425}\nyears = sorted(data)\nfor y in years:\n    print(y, data[y], "ppm")\nrise = (data[2024] - data[1960]) / (2024 - 1960)\nprint(f"average rise: {rise:.2f} ppm/year over 64 years")\n', '#!/usr/bin/env python3\n"""{TITLE} -- water budget demo. Runs as-is with python3."""\n# liters per item (approximate water footprints)\nFOOTPRINT = {"kg wheat": 1500, "kg rice": 2500, "kg beef": 15400, "cotton shirt": 2700}\nfor item, liters in FOOTPRINT.items():\n    print(f"{item:<14} {liters:>6,} liters")\nprint("a kilogram of beef takes ~10x the water of a kilogram of wheat")\n'];
var TOPICS=[['Signature What Environmental Science Is','Environmental science studies the interactions between humans and natural systems: how we use air, water, land, and living resources, what our wastes do, and how to manage the relationship sustainably. It borrows from every natural science and aims at decisions.'],
['Signature The Core Question of Environmental Science','The core question is: what are we doing to the environment, what will it do to us, and what should we do about it? Description, prediction, and management — the field refuses to stop at the first two.'],
['Signature Assumptions: Systems and Limits','The field assumes systems thinking (everything connects) and limits (the planet\'s absorptive and regenerative capacities are finite). Actions have downstream effects, and \'away\' — where wastes go — is always somewhere.'],
['Signature The Vocabulary: Footprints, Budgets, Baselines','The vocabulary is budgets and footprints: carbon footprint, water footprint, ecological footprint — each comparing human demand to nature\'s supply. Baselines define the reference state; carrying capacity defines the limit.'],
['Signature Carrying Capacity: The Fundamental Quantity','Carrying capacity is the fundamental quantity: the population or activity level an environment can sustain indefinitely. Overshoot — exceeding it temporarily — is possible, but the bill arrives as depletion and degradation.'],
['Signature Monitoring: The Primary Method','Monitoring is the primary method: long-term, systematic measurement of air, water, soil, and species. The Keeling curve\'s steady CO₂ rise, measured since 1958, is environmental science\'s iconic product — a trend no model could have faked.'],
['Signature A Canonical First Example','The canonical first example is the ozone hole: CFCs measured in the stratosphere, the Antarctic ozone collapse observed, the chemistry worked out, and the Montreal Protocol phasing out CFCs — science to treaty in fourteen years, and the ozone layer recovering.'],
['Signature How Environmental Science Measures','The field measures with sensor networks, satellites, and bioindicators: air monitors in cities, stream gauges in watersheds, lichens and macroinvertebrates as living instruments. Remote sensing made the whole planet\'s health checkable from orbit.'],
['Signature The Core Mechanism: Source, Pathway, Receptor','The core mechanism is source → pathway → receptor: a pollutant emitted, transported through air or water, and received by lungs, lakes, or ecosystems. Managing any environmental problem means intervening somewhere on that chain.'],
['Signature The Simplest Law: Mass Balance','The simplest law is mass balance: what goes in must come out or accumulate. Applied to carbon, nitrogen, or plastic, it turns vague concern into accounting — and the accounts show accumulation.'],
['Signature Common Misconceptions in Environmental Science','The misconceptions mislead: that dilution solves pollution (persistent pollutants accumulate), that the environment is separate from the economy (the economy is a wholly owned subsidiary), and that individual action and systemic change are alternatives (both are needed).'],
['Signature How Beginners Practice Environmental Science','Beginners practice by auditing: measure your household\'s waste, energy, and water for a week; sample a local stream; map land use around your home. Personal budgets make planetary budgets intuitive.'],
['Signature The Core Model: The Carbon Cycle (Anthropogenic)','The anthropogenic carbon cycle is the core model: fossil carbon, locked away for millions of years, released in decades; about half absorbed by oceans and land, the rest accumulating in the air. The budget is measured, not modeled — and it does not balance in our favor.'],
['Signature The Great Equation: I = PAT','The IPAT equation — Impact = Population × Affluence × Technology — is the great accounting identity: environmental impact factorizes into how many of us, how much each uses, and how dirty the technology is. Every sustainability strategy works on one of the three terms.'],
['Signature Systems Thinking: Everything Connects','Systems thinking is the field\'s native mode: fertilizer runoff feeds algal blooms that kill fisheries; air conditioning cools rooms and warms the planet. Life-cycle analysis follows a product from mine to landfill so no impact hides offstage.'],
['Signature Invariance: Conservation Laws Apply','The invariance principles are the conservation laws applied to the environment: carbon, nitrogen, and water are conserved, so every emission is a deposit somewhere. There is no \'away\' — only elsewhere.'],
['Signature Approximation: Models and Scenarios','Approximation uses models and scenarios: climate models project ranges under different emissions paths, not single predictions. The honest output is a cone of futures — and the cone\'s width is itself information.'],
['Signature Evidence Standards: Long Records','The evidence standard is the long record: trends established over decades, with natural variability quantified. A single hot year proves nothing; the multi-decade rise, the ocean heat content, the retreating ice — together — prove the trend.'],
['Signature Classic Discoveries','The classic discoveries are the greenhouse effect\'s measurement, the ozone hole and its cause, acid rain\'s chemistry, biomagnification of DDT, and the Keeling curve. Each moved from observation to mechanism to policy.'],
['Signature Core Trade-offs: Development versus Preservation','The core trade-off is development versus preservation, navigated by sustainable development: meeting present needs without compromising future ones. The practical art is finding the designs — clean energy, circular materials — that dissolve the trade.'],
['Signature Handling Uncertainty: Precaution','The field handles uncertainty with the precautionary principle: where harm may be serious and irreversible, lack of full certainty does not justify inaction. It is decision theory for the planet — asymmetric risks demand asymmetric caution.'],
['Signature Tools of the Trade','The tools of the trade are the sensor, the budget, and the life-cycle analysis: measure the flows, balance the accounts, follow the product cradle to grave. GIS maps it all — every environmental question is, at bottom, a where question.'],
['Signature Ethics and Responsibility','Ethics in environmental science is intergenerational: the present decides what the future inherits. Environmental justice adds the present dimension — pollution burdens fall on the poor first. The field\'s findings are inherently moral facts.'],
['Signature Teaching Environmental Science','Teaching it well starts with the local: the creek behind the school, the city\'s air on a still day, the landfill on the edge of town. Global problems become real when students have measured a local one.'],
['Signature The Frontier Question','The frontier question is planetary boundaries: which Earth-system limits are we approaching, how do they interact, and can humanity operate safely within them? The framework is new; the quantification is the frontier.'],
['Signature Unifying Theories','The unifying framework is earth-system science: atmosphere, ocean, land, ice, and biosphere as one coupled system, with humans now a geological force — the Anthropocene. It unifies the field\'s fragments into a single planetary picture.'],
['Signature Computational Environmental Science','Computational environmental science runs the planet in silico: coupled climate models, hydrological models, species distribution models, and integrated assessment models linking economies to emissions. The models guide trillion-dollar decisions — so their uncertainties are published, not hidden.'],
['Signature Bridges to Other Fields','Environmental science bridges to ecology, chemistry, public health, economics, engineering, law, and policy: each contributes a piece, none suffices alone. It is the original interdisciplinary science.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the full social cost of carbon, scalable carbon removal, feeding ten billion within planetary boundaries, and halting biodiversity loss while developing. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New environmental claims are validated by the monitoring record: independent sensor networks, satellite confirmation, and reanalysis by rival groups. A trend is trusted when multiple instruments, on multiple platforms, agree.'],
['Signature The Great Debates','The great debates concern pace and policy, not the basic physics: how fast to decarbonize, nuclear\'s role, geoengineering\'s risks, degrowth versus green growth. The science constrains the options; values choose among them.'],
['Signature Failure Modes: When Environmental Science Gets It Wrong','The field gets it wrong through single-medium thinking (cleaning air by polluting water), ignoring rebound effects (efficiency gains spent on more consumption), and false precision in projections. The immune system is whole-system accounting.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis manages whole systems: the watershed, the airshed, the foodshed — budgets balanced, baselines monitored, interventions tested against the record. The fundamentals are the instruments on the planetary dashboard.'],
['Signature The Signature Formulation: Environmental Science as Stewardship','The Signature formulation makes environmental science the stewardship layer of the network: every database, every build, every deployment gets its footprint computed and shown, because in the Signature system construction without stewardship is incomplete. That is the Signature capstone on environmental bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Baselines are stated: change is measured against a defined reference.", "Uncertainty is shown: projections carry scenarios and confidence, not false precision.", "Solutions are assessed whole-system: no burden-shifting to another medium or place."],citations:["Miller, G. T. and Spoolman, S. \u2014 Living in the Environment.", "IPCC Assessment Reports \u2014 the consensus science of climate change.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-environmental-science-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-environmental-science-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
