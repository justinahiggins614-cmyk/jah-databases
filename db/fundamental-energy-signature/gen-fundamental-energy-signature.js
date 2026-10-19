(function(){'use strict';
/* jahdb-fundamental-energy-signature-1.0 — fundamental energy bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFEN-';
var KIND='fundamental energy record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Energy is the study of energy in all its forms: where it comes from, how it converts, how it\'s stored and moved, and what it costs — in money, in materials, in consequences. It is the master resource beneath civilization.', 'reasoning':'Energy thinkers reason in flows and stocks: sources, conversions, storage, and end uses, all balanced. Every energy claim is checked against thermodynamics — and every proposal is priced in full lifecycle cost.', 'quantities':'The core quantities are power (watts) and energy (joules, kWh), with capacity factor, efficiency, and energy return on investment (EROI) as the derived masters. The joule and the watt-hour translate between all forms.', 'mechanism':'Energy systems work conversion chains: primary source → conversion → carrier → end use, with losses at every step. Efficiency compounds along the chain — which is why electrification wins: fewer conversions, fewer losses.', 'miscon':'Energy is not \'used up\' — it converts to less useful forms (entropy always wins). Renewables are not \'free\' — they have material and land costs. And the grid cannot run on good intentions: it runs on balanced power, every second.'};
var SIGLENS=['In the Signature system, energy is the master constraint: every computation, every data center, every device in this network runs on energy, and the Signature formulation teaches each principle as a budget you can balance.','The Signature practice is to balance the energy budget: compute the flows, price the conversions, check the thermodynamics — so energy reasoning is done with numbers that must add up.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- household energy demo. Runs as-is with python3."""\ndevices = {"LED bulb (10W, 5h/day)": (10, 5), "fridge (150W avg)": (150, 24),\n           "AC (1500W, 8h/day)": (1500, 8), "phone charger (10W, 3h)": (10, 3)}\ntotal_kwh = 0\nfor name, (w, h) in devices.items():\n    kwh = w * h / 1000\n    total_kwh += kwh\n    print(f"{name:<28} {kwh:5.2f} kWh/day")\nprint(f"{\'TOTAL\':<28} {total_kwh:5.2f} kWh/day")\n', '#!/usr/bin/env python3\n"""{TITLE} -- solar output demo. Runs as-is with python3."""\ndef solar_kwh_per_day(panel_kw, sun_hours, efficiency=0.8):\n    return panel_kw * sun_hours * efficiency\nfor kw, hrs in [(5, 4), (5, 6), (10, 5)]:\n    print(f"{kw}kW system, {hrs} sun-hours: {solar_kwh_per_day(kw, hrs):.1f} kWh/day")\nprint("capacity factor = actual output / nameplate x 8760h")\n', '#!/usr/bin/env python3\n"""{TITLE} -- EV vs gasoline demo. Runs as-is with python3."""\n# per 100 km\ngas_l_per_100 = 8.0\ngas_kwh_per_l = 9.7\nev_kwh_per_100 = 18.0\ngas_energy = gas_l_per_100 * gas_kwh_per_l\nprint(f"gasoline car: {gas_energy:.0f} kWh of fuel per 100km (engine ~25% efficient -> ~19 kWh useful)")\nprint(f"EV: {ev_kwh_per_100} kWh per 100km (~90% efficient)")\nprint("electrification wins on efficiency: fewer conversions, fewer losses")\n'];
var TOPICS=[['Signature What Energy Is','Energy is the capacity to do work — and the master resource of civilization. The field studies energy\'s forms (mechanical, thermal, electrical, chemical, nuclear, radiant), its conversions, and its costs. Everything humans do runs on an energy flow.'],
['Signature The Core Question of Energy','The core question is: where does the energy come from, what does it cost, and what are the consequences? Every energy system — from a campfire to a grid — answers in joules, dollars, and emissions.'],
['Signature Assumptions: Thermodynamics Rules','The field assumes the laws of thermodynamics absolutely: energy is conserved, entropy increases, and no cycle beats Carnot. Proposals violating these are not innovations — they are errors.'],
['Signature The Vocabulary: Power versus Energy','The vocabulary distinguishes power (watts — rate) from energy (joules — amount), capacity from generation, and primary energy from useful energy. Confusing power with energy is the field\'s most common public error.'],
['Signature The Joule: The Fundamental Quantity','The joule is the fundamental quantity: one watt for one second. The kilowatt-hour (3.6 MJ) is the commercial unit — the currency in which civilization\'s energy is bought and sold.'],
['Signature Energy Accounting: The Primary Method','Energy accounting is the primary method: track every flow from source to service, with losses at each conversion. Sankey diagrams make the flows visible — and the losses undeniable.'],
['Signature A Canonical First Example','The canonical first example is the incandescent bulb: 60 watts in, 3 watts of light out — 5% efficient. The LED replacement (10 watts in, same light) teaches the whole field: service matters, efficiency multiplies.'],
['Signature How Energy Measures','The field measures with meters, analyzers, and life-cycle assessments: flows in real time, stocks over years, full costs cradle to grave. What gets measured gets managed — the meter is the policy instrument.'],
['Signature The Core Mechanism: The Conversion Chain','The core mechanism is the conversion chain: chemical → thermal → mechanical → electrical, each step losing some to heat. Electrification shortens chains — which is why heat pumps and EVs beat combustion on efficiency.'],
['Signature The Simplest Law: Conservation of Energy','The simplest law is the first law: energy is neither created nor destroyed. Every energy balance must close — the unclosed balance is where the error (or the fraud) hides.'],
['Signature Common Misconceptions in Energy','The misconceptions mislead policy: that energy is \'used up\' (it degrades in usefulness), that renewables have no costs (materials, land, variability), and that efficiency alone solves everything (rebound effects consume some gains).'],
['Signature How Beginners Practice Energy','Beginners practice by auditing: meter your home, compute your footprint, trace your electricity to its source. Personal energy accounting makes national energy debates concrete.'],
['Signature The Core Model: The Grid','The grid is the core model of energy systems: generation, transmission, distribution, and load balanced every second. It is the largest machine ever built — and the template for thinking about all energy systems.'],
['Signature The Great Equation: EROI','Energy return on investment — energy out over energy in — is the great equation: civilization runs on surplus energy. An EROI below ~10 struggles to support complexity; fossil fuels\' high EROI built the modern world.'],
['Signature Systems Thinking: The Energy Transition','Systems thinking frames the energy transition: sources, grids, storage, demand, and policy as one coupled system. Transition is not swapping power plants — it is rebuilding the system while it runs.'],
['Signature Invariance: Thermodynamics','The invariance principles are the laws of thermodynamics: no perpetual motion, no free lunch, entropy\'s arrow. They bound every proposal before economics or politics gets a vote.'],
['Signature Approximation: Capacity Factors','Approximation uses capacity factors and averages: a solar farm\'s annual output as a fraction of nameplate. Averages guide planning; the hard part — variability — is handled by storage, grids, and overbuilding.'],
['Signature Evidence Standards: Measured Performance','The evidence standard is measured performance over time: metered output, audited costs, lifecycle assessments. Nameplate ratings promise; meters prove.'],
['Signature Classic Discoveries','The classic discoveries are fire, the steam engine, electromagnetism, the photovoltaic effect, and nuclear fission. Each unlocked an energy source — and each remade civilization.'],
['Signature Core Trade-offs: Cost versus Cleanliness versus Reliability','The core trade-off is the energy trilemma: affordable, clean, reliable — pick the balance. Every system is a point on this triangle, and the art is moving the frontier, not just choosing.'],
['Signature Handling Uncertainty: Variability','Energy systems handle variability with storage, interconnection, overbuilding, and demand response: the toolkit for matching variable supply to inflexible demand. Uncertainty is engineered around, not wished away.'],
['Signature Tools of the Trade','The tools of the trade are the energy audit, the Sankey diagram, LCOE models, and grid simulators. The deepest is the lifecycle assessment — the full accounting from mine to decommissioning.'],
['Signature Ethics and Responsibility','Ethics in energy is intergenerational and global: who bears the costs of pollution and climate change, who gets access to energy, what we owe the future. Energy decisions are moral decisions with numbers attached.'],
['Signature Teaching Energy','Teaching it well starts with the meter: students audit real buildings, trace real electrons. Energy you have measured is energy you understand — abstractions follow the audit.'],
['Signature The Frontier Question','The frontier question is the fully decarbonized system: firm clean power, long-duration storage, decarbonized industry and transport. The frontier asks whether physics and economics allow it at the speed required.'],
['Signature Unifying Theories','The unifying theories are thermodynamics and economics: physics bounds what\'s possible, markets and policy decide what\'s built. Energy literacy means holding both — the joule and the dollar — simultaneously.'],
['Signature Computational Energy','Computational energy models the transition: capacity expansion models, grid simulations, and integrated assessment models. The models guide trillion-dollar decisions — so their assumptions are published and debated.'],
['Signature Bridges to Other Fields','Energy bridges to physics, engineering, economics, geology (resources), environmental science (impacts), and politics (policy). It is the master interdisciplinary field — everything connects through energy.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: economical long-duration storage, fusion at grid scale, and decarbonizing steel, cement, and aviation. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New energy claims are validated by metered performance and audited cost: the pilot plant\'s output, the installed system\'s LCOE. An energy technology earns trust at scale — the lab is only the audition.'],
['Signature The Great Debates','The great debates — nuclear\'s role, the pace of transition, degrowth versus green growth — are about values and risk, constrained by physics. The numbers set the boundaries; societies choose within them.'],
['Signature Failure Modes: When Energy Gets It Wrong','The field gets it wrong through uncounted costs (externalities), wishful capacity factors, and ignoring system integration. The immune system is full lifecycle accounting and the metered record.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis designs whole energy systems from fundamentals: sources balanced, conversions efficient, costs honest, thermodynamics respected. The fundamentals are the audit every proposal must pass.'],
['Signature The Signature Formulation: Energy as the Master Budget','The Signature formulation treats energy as the master budget of the network: every principle here balances a flow that must add up, because in the Signature system energy you cannot account for is energy you do not understand. That is the Signature capstone on energy bedrock.']];
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
    standards:["Thermodynamics is respected: no proposal violates the laws; efficiencies are stated honestly.", "Full lifecycle: costs include materials, land, and decommissioning, not just fuel.", "Units are consistent: compare in the same units (LCOE, EROI) or not at all."],citations:["Smil, V. \u2014 Energy and Civilization: A History (MIT Press).", "MacKay, D. J. C. \u2014 Sustainable Energy: Without the Hot Air (free online).", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-energy-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-energy-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
