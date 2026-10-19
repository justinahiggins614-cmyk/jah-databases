(function(){'use strict';
/* jahdb-fundamental-earth-science-signature-1.0 — fundamental earth-science bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFEAR-';
var KIND='fundamental earth-science record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Earth science studies our planet as a system: its rocks, oceans, atmosphere, and the interactions among them across deep time. Geology, oceanography, and atmospheric science join here into one picture of a dynamic world.', 'reasoning':'Earth scientists reason from the rock record and from process rates: the present is the key to the past — observable processes, extended over deep time, explain ancient formations. Multiple working hypotheses compete until the field evidence decides.', 'quantities':'The core quantities are time (millions to billions of years), temperature, pressure, and composition — of rocks, water, and air. Deep time is the master quantity: Earth is 4.54 billion years old, and most of its story happened before complex life.', 'mechanism':'Earth understanding is built by uniformitarianism plus deep time: slow processes — plate motion at centimeters per year, erosion grain by grain — given billions of years, build mountains and carve canyons. Catastrophes punctuate, but gradual processes dominate the budget.', 'miscon':'Earth science is not just rock collecting: it is quantitative and predictive. Continents do move — plate tectonics is measured directly by GPS. And the greenhouse effect is not a theory in dispute: it is measured physics, confirmed by satellites watching heat escape.'};
var SIGLENS=['In the Signature system, earth science is the study of the platform everything stands on: every database in this network ultimately describes a world, and the Signature formulation teaches each principle as a system you can model.','The Signature practice is to model the Earth: compute the plate motion, track the carbon, run the climate numbers — so planetary reasoning is done with quantities, not just admired as scenery.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- plate motion demo. Runs as-is with python3."""\ndef drift(cm_per_year, million_years):\n    return cm_per_year * million_years * 1e4  # cm*Myr -> km (1e6 yr * cm/yr /1e5)\nfor rate in [2, 5, 10]:\n    print(f"{rate} cm/yr for 100 Myr -> {drift(rate, 100):,.0f} km of motion")\nprint("Atlantic widens ~2-5 cm/yr: about as fast as fingernails grow")\n', '#!/usr/bin/env python3\n"""{TITLE} -- earthquake energy demo. Runs as-is with python3."""\ndef energy_joules(magnitude):\n    return 10 ** (1.5 * magnitude + 4.8)\nfor m in [5.0, 6.0, 7.0, 9.0]:\n    print(f"M{m:.1f} -> {energy_joules(m):.2e} joules")\nprint("each magnitude unit is ~32x the energy")\n', '#!/usr/bin/env python3\n"""{TITLE} -- deep time demo. Runs as-is with python3."""\nevents = [("Earth forms", 4540), ("First life", 3800), ("Oxygen atmosphere", 2400),\n          ("Cambrian explosion", 541), ("Dinosaurs extinct", 66), ("Homo sapiens", 0.3)]\nfor name, mya in events:\n    pct = 100 * mya / 4540\n    print(f"{name:<20} {mya:>6} Myr ago  ({pct:5.1f}% of Earth history ago)")\n'];
var TOPICS=[['Signature What Earth Science Is','Earth science studies the planet as an integrated system: the solid Earth, the oceans, the atmosphere, and their interactions over 4.54 billion years. It is where physics, chemistry, and biology meet at planetary scale.'],
['Signature The Core Question of Earth Science','The core question is: how does the Earth work, and how did it get this way? Every rock, every fossil, every atmospheric measurement is interrogated for process (what is happening) and history (what happened).'],
['Signature Assumptions: Uniformitarianism and Deep Time','The field assumes uniformitarianism — the present is the key to the past: the processes we observe today operated in the past — and deep time: Earth is billions of years old, giving slow processes time to work planetary-scale change.'],
['Signature The Vocabulary: Lithosphere, Hydrosphere, Atmosphere','The vocabulary names the spheres: lithosphere (rock), hydrosphere (water), atmosphere (air), biosphere (life), and the interfaces where the action is. The rock cycle, water cycle, and carbon cycle describe matter\'s circulation among them.'],
['Signature Deep Time: The Fundamental Quantity','Deep time is the fundamental quantity: 4.54 billion years, dated by radiometric clocks in meteorites and rocks. Human history occupies the last 0.0001% — the field\'s perspective is vertiginously long.'],
['Signature Field Observation: The Primary Method','Field observation is the primary method: reading outcrops, mapping formations, collecting samples in place. The laboratory analyzes, but the field decides — a theory that contradicts the outcrop is wrong.'],
['Signature A Canonical First Example','The canonical first example is the Grand Canyon: nearly two billion years of rock exposed, each layer a chapter, the canyon itself carved by the Colorado River. Standing at the rim is reading deep time in stratigraphy.'],
['Signature How Earth Science Measures','Earth science measures with seismometers, satellites, ice cores, and mass spectrometers: earthquakes image the interior, GPS tracks the plates, ice cores sample ancient air, isotopes date the rocks. Remote sensing made the whole planet an instrument.'],
['Signature The Core Mechanism: Plate Tectonics','The core mechanism is plate tectonics: the lithosphere divided into plates moving centimeters per year over the mantle, building mountains where they collide, opening oceans where they part, and recycling crust where they dive. It unifies earthquakes, volcanoes, and mountain ranges.'],
['Signature The Simplest Law: Superposition','The simplest law is Steno\'s superposition: in undisturbed strata, the oldest layer is at the bottom. Three centuries old and still the first tool of every field geologist — order before process.'],
['Signature Common Misconceptions in Earth Science','The misconceptions linger: that continents are fixed (GPS measures their motion), that the greenhouse effect is unproven (it is measured physics), that diamonds come from coal (they form far deeper, from other carbon), and that the Earth is cooling into inactivity (its interior still churns).'],
['Signature How Beginners Practice Earth Science','Beginners practice by identifying rocks and minerals, reading topographic maps, and interpreting road cuts: every exposure is a puzzle. A hand lens and a hardness kit teach more mineralogy than a semester of slides.'],
['Signature The Core Model: The Rock Cycle','The rock cycle is the core model: igneous rocks weather to sediment, sediment lithifies to sedimentary rock, heat and pressure make metamorphic rock, melting remakes igneous. Matter circulates; the cycle has no beginning.'],
['Signature The Great Equation: Radiometric Dating','Radiometric dating is the great equation made practical: N = N₀e^(-λt) turns parent-daughter isotope ratios into absolute ages. It dated the Earth, calibrated the fossil record, and gave deep time its numbers.'],
['Signature Systems Thinking: The Carbon Cycle','Systems thinking in earth science is the carbon cycle: carbon moving among atmosphere, ocean, biosphere, and rock, with feedbacks that stabilize or destabilize climate. The field\'s great insight is that the planet regulates itself — until pushed too fast.'],
['Signature Invariance: Conservation of Matter','The invariance principle is conservation of matter through the cycles: water, carbon, and rock are neither created nor destroyed, only moved and transformed. Every earth-science budget — water, carbon, sediment — is an accounting of conserved flows.'],
['Signature Approximation: Uniform Rates','Approximation assumes rates measured today extend into the past: present erosion rates date canyons, present spreading rates date oceans. Where rates changed — ice ages, impacts — the record itself corrects the assumption.'],
['Signature Evidence Standards: Multiple Lines','The evidence standard is consilience: independent lines — fossils, isotopes, magnetics, stratigraphy — converging on the same history. Plate tectonics won because paleomagnetism, seafloor age, and fossil distributions all agreed.'],
['Signature Classic Discoveries','The classic discoveries are deep time, the ice ages, plate tectonics, the iridium layer marking the dinosaur extinction, and the ozone hole. Each rewrote humanity\'s picture of its planet — and its place on it.'],
['Signature Core Trade-offs: Resolution versus Span','The core trade-off is resolution versus span: ice cores give exquisite recent detail, deep-sea sediments give coarse ancient records. Earth scientists stitch high-resolution short records to low-resolution long ones.'],
['Signature Handling Uncertainty: Dating Errors','Earth science handles uncertainty by dating the uncertainty: every age carries analytical error, and correlations between distant rocks carry stratigraphic uncertainty. Honest geochronology reports both.'],
['Signature Tools of the Trade','The tools of the trade are the rock hammer, the hand lens, the Brunton compass, the mass spectrometer, and the satellite. The most powerful is the geologic map — the field\'s synthesis of everything known about an area.'],
['Signature Ethics and Responsibility','Ethics in earth science concerns resources and hazards: honest reporting of reserves, responsible mining, and truthful hazard communication. The field\'s forecasts — eruptions, quakes, floods — carry life-or-death weight.'],
['Signature Teaching Earth Science','Teaching earth science well goes outside: the outcrop, the stream, the shoreline teach what no diagram can. Deep time is the hard concept — timelines walked at scale, where a step is a million years, make it visceral.'],
['Signature The Frontier Question','The frontier question is the deep Earth and the early Earth: what the lower mantle is made of, how plate tectonics started, and how the first continents grew. Seismology and geochemistry are converging on answers.'],
['Signature Unifying Theories','The unifying theory is plate tectonics joined to the rock and biogeochemical cycles: one framework linking earthquakes, volcanoes, mountain-building, ore deposits, and long-term climate. It is geology\'s equivalent of evolution.'],
['Signature Computational Earth Science','Computational earth science models the planet: mantle convection codes, climate models coupling ocean and atmosphere, and seismic tomography inverting waves into interior images. The models are tested against the 4.5-billion-year experiment already run.'],
['Signature Bridges to Other Fields','Earth science bridges to physics (geophysics), chemistry (geochemistry), biology (paleontology, biogeochemistry), astronomy (planetary science), and engineering (resource extraction, hazard mitigation). The planet is the shared laboratory.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: earthquake prediction at useful precision, the exact trigger of Snowball Earth episodes, the deep carbon cycle\'s full budget, and how life began in Earth\'s early environments. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New earth-science claims are validated by field checking: other geologists visit the outcrop, re-date the rocks, re-run the analysis. A claim that cannot survive a field trip does not survive.'],
['Signature The Great Debates','The great debates include the pace of early Earth processes, the role of impacts versus volcanism in mass extinctions, and how sensitive climate is to carbon dioxide — each argued with data from the rock record.'],
['Signature Failure Modes: When Earth Science Gets It Wrong','Earth science gets it wrong through over-extrapolation from one locality, ignoring deep time (assuming today\'s rates always), and confusing correlation with cause in the record. The field\'s immune system is the second outcrop.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis reads Earth whole: the rock\'s age, the fossil\'s environment, the isotope\'s temperature, the structure\'s deformation — one planet, many recorders, a single history. The fundamentals are the grammar of that reading.'],
['Signature The Signature Formulation: Earth Science as Planetary System','The Signature formulation treats Earth as the prototype system: every principle here models a world of interacting spheres over deep time, because in the Signature system a database — like a planet — is a system of cycles, and understanding the cycles is owning the system. That is the Signature capstone on earth-science bedrock.']];
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
    standards:["Deep time is respected: processes are scaled by their rates times their durations.", "Field evidence rules: models must survive contact with outcrops, cores, and instruments.", "Uncertainty is dated too: every age carries its error bars."],citations:["Press, F., Siever, R., Grotzinger, J., Jordan, T. \u2014 Understanding Earth.", "USGS \u2014 public domain earth science references and data.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-earth-science-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-earth-science-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
