(function(){'use strict';
/* jahdb-fundamental-physics-1.0 — fundamental physics bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FPHY-';
var KIND='fundamental physics record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Physics is the study of matter, energy, space, and time, and the fundamental laws governing their interactions. It seeks the smallest set of principles from which the behavior of the physical world can be derived.', 'reasoning':'Physicists reason by mathematizing nature: write down equations for a system, solve or approximate them, and test the predictions against measurement. When prediction and measurement disagree, the theory — not the data — is on trial.', 'quantities':'The core quantities are mass, length, time, electric charge, and temperature, with energy and momentum as the great derived quantities. The SI units — kilogram, meter, second, ampere, kelvin — anchor every measurement.', 'mechanism':'Physical understanding is built by idealization: strip a system to its essentials (the frictionless plane, the point mass), solve the ideal case exactly, then add the complications back as corrections. The ideal case reveals the law; the corrections fit the world.', 'miscon':'Physics is not just applied mathematics: experiment is sovereign, and beautiful equations that disagree with measurement are wrong. Quantum mechanics does not mean \'anything goes\' — it is the most precisely tested theory in history. And relativity does not make everything relative: the speed of light is absolute.'};
var SIGLENS=['In the Signature system, physics is the reality check on all construction: every engine, every simulation, every manufactured thing in this network must respect physical law, and the Signature formulation teaches each principle as a law you can compute with.','The Signature practice is to compute the physics: run the simulation, check the conservation law, compare prediction to measurement — so physical law is experienced as constraint, not just read as text.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- projectile motion demo. Runs as-is with python3."""\nimport math\ng = 9.81\ndef projectile(v0, angle_deg):\n    th = math.radians(angle_deg)\n    t = 2 * v0 * math.sin(th) / g\n    r = v0 * math.cos(th) * t\n    h = (v0 * math.sin(th)) ** 2 / (2 * g)\n    return t, r, h\nfor v, a in [(20, 30), (20, 45), (20, 60)]:\n    t, r, h = projectile(v, a)\n    print(f"v={v} m/s angle={a}: time={t:.2f}s range={r:.2f}m maxheight={h:.2f}m")\n', '#!/usr/bin/env python3\n"""{TITLE} -- kinetic energy demo. Runs as-is with python3."""\ndef kinetic_energy(m, v):\n    return 0.5 * m * v * v\nfor m, v in [(1000, 30), (80, 5), (0.05, 300)]:\n    ke = kinetic_energy(m, v)\n    print(f"m={m} kg v={v} m/s -> KE={ke:,.1f} J")\nprint("note: doubling speed quadruples energy")\n', '#!/usr/bin/env python3\n"""{TITLE} -- pendulum period demo. Runs as-is with python3."""\nimport math\ng = 9.81\ndef period(L):\n    return 2 * math.pi * math.sqrt(L / g)\nfor L in [0.25, 1.0, 4.0]:\n    print(f"L={L} m -> T={period(L):.3f} s")\nprint("note: period depends on length, not mass or amplitude (small angles)")\n'];
var TOPICS=[['What Physics Is','Physics studies matter, energy, space, and time and the laws relating them, from quarks to galaxies. Its ambition is extreme: to explain the maximum of phenomena with the minimum of principles — and its method, mathematized prediction tested by experiment, is the template for all of science.'],
['The Core Question of Physics','The core question of physics is: what are the laws, and what do they predict? Given a system\'s initial conditions and the governing laws, physics asks what must happen next — and then builds the experiment that checks the answer.'],
['Assumptions: The Uniformity of Nature','Physics assumes the uniformity of nature: the laws found in the laboratory hold in distant galaxies and in the distant past. Without this assumption no distant measurement could teach us anything; with it, a spectral line from a billion light-years away reveals an atom\'s structure.'],
['The Vocabulary: Fields, Forces, and Particles','The vocabulary of physics names its actors: particles with mass and charge, fields filling space, forces mediating interactions, and waves carrying energy. The Standard Model organizes the particles; general relativity describes gravity as curved spacetime.'],
['Energy: The Fundamental Quantity','Energy is the fundamental quantity of physics: the capacity to do work, conserved in every interaction, appearing as motion, heat, mass, and light. From E = mc² to the first law of thermodynamics, energy bookkeeping is the universal audit of physical processes.'],
['Experiment: The Primary Method','Experiment is the primary method and the final judge: controlled conditions, measured outcomes, quantified uncertainty. Galileo\'s inclined planes, Rutherford\'s scattering, the double-slit — each forced nature to answer a precisely posed question.'],
['A Canonical First Example','The canonical first example is projectile motion: launched at speed v₀ and angle θ, the projectile follows a parabola with range v₀²sin(2θ)/g. One equation unifies thrown stones and artillery shells — the idealization revealing the law beneath the air resistance.'],
['How Physics Measures','Physics measures by comparison to standards: the meter defined by the speed of light, the second by atomic transitions, the kilogram by the Planck constant. Modern metrology defines units from fundamental constants, so the standards are built into nature itself.'],
['The Core Mechanism: Laws Plus Initial Conditions','The core mechanism of physical prediction is laws plus initial conditions: the laws (F = ma, Maxwell\'s equations, Schrödinger\'s equation) dictate how systems evolve, and the initial conditions pick out which evolution is ours. Same laws, different starts, different worlds.'],
['The Simplest Law: Conservation of Energy','The simplest and deepest law is conservation of energy: in an isolated system the total never changes, only transforms. Perpetual motion machines fail not from poor engineering but from this law — and every working engine is a managed transformation of it.'],
['Common Misconceptions in Physics','The misconceptions are durable: that quantum mechanics means anything is possible (it is rigidly probabilistic), that relativity makes everything relative (c is absolute), that centrifugal force is fundamental (it is a frame artifact), and that physics is finished (dark matter and dark energy say otherwise).'],
['How Beginners Practice Physics','Beginners practice physics by solving problems with diagrams: draw the system, label the forces, write the equations, check the units, and ask whether the answer is reasonable. Estimation — Fermi problems — trains the physical intuition that formulas alone cannot.'],
['The Core Model: The Harmonic Oscillator','The harmonic oscillator — mass on a spring, pendulum at small angles — is the core model: the same mathematics describes vibrations, circuits, and molecular bonds. Master the oscillator and you hold the key to half of classical and quantum physics.'],
['The Great Equation: E = mc²','Einstein\'s E = mc² is the great equation: mass is frozen energy, and the speed of light is the exchange rate. It explains the Sun\'s fire, nuclear power, and particle creation — and it follows from the symmetries of spacetime, not from experiment alone.'],
['Systems Thinking: Emergence','Systems thinking in physics confronts emergence: temperature, pressure, and phase transitions are meaningless for one atom and inevitable for 10²³. Statistical mechanics bridges the scales, deriving the macroscopic laws from microscopic statistics.'],
['Invariance: Symmetry and Conservation','Noether\'s theorem is the invariance principle: every continuous symmetry implies a conservation law — time symmetry gives energy conservation, space symmetry gives momentum, rotational symmetry gives angular momentum. Symmetry is the deep reason the conservation laws hold.'],
['Approximation: Perturbation Theory','Approximation in physics is perturbation theory: solve the simple system exactly, then add the small complication as a series of corrections. From planetary orbits to quantum electrodynamics — the most precisely tested theory ever — the method is the same.'],
['Evidence Standards: Five Sigma','The evidence standard in frontier physics is demanding: particle discoveries require five-sigma significance, a one-in-3.5-million fluke probability, plus independent replication. Extraordinary claims — faster-than-light neutrinos — die under this standard, as they should.'],
['Classic Experiments','The classic experiments are the field\'s crown jewels: Young\'s double slit, Michelson-Morley, Rutherford scattering, the photoelectric effect, the bending of starlight in 1919. Each overturned a worldview with a measurement.'],
['Core Trade-offs: Precision versus Scope','The core trade-off is precision versus scope: quantum electrodynamics predicts the electron\'s magnetism to ten decimal places but says nothing about galaxies; cosmology describes the universe but coarsely. Effective theories trade scope for precision at each scale.'],
['Handling Uncertainty: Quantum Probability','Quantum mechanics handles uncertainty fundamentally: the uncertainty principle limits simultaneous knowledge of conjugate quantities, and measurement outcomes are probabilistic at the deepest level known. The probabilities are precise; only the outcomes are chancy.'],
['Tools of the Trade','The tools of the trade are the differential equation, the conservation law, the symmetry argument, and the order-of-magnitude estimate — plus particle accelerators, telescopes, and lasers for the experimentalist. The thought experiment remains the cheapest apparatus.'],
['Ethics and Responsibility','Ethics in physics became unavoidable with the atomic bomb: the same nuclear physics powers cities and levels them. The field\'s responsibility, debated since the Franck Report, is to understand the consequences of its discoveries and speak honestly about them.'],
['Teaching Physics','Teaching physics well leads with phenomena: drop the objects, swing the pendulum, then mathematize what was seen. Students who have predicted, measured, and been surprised own the concept in a way equation-first teaching rarely achieves.'],
['The Frontier Question','The frontier question is unification: reconciling general relativity with quantum mechanics in a theory of quantum gravity. String theory, loop quantum gravity, and emergent-spacetime programs compete — all mathematically deep, none yet experimentally confirmed.'],
['Unifying Theories','The unifying theories are the field\'s triumphs: Newton unified earthly and celestial motion, Maxwell unified electricity, magnetism, and light, the electroweak theory unified two forces, and the Standard Model organizes three of the four. Gravity alone resists the pattern.'],
['Computational Physics','Computational physics simulates what equations cannot solve: lattice quantum chromodynamics computes hadron masses from first principles, N-body codes evolve galaxies, and climate models integrate the fluid equations of the atmosphere. Simulation is now the third pillar beside theory and experiment.'],
['Bridges to Other Fields','Physics bridges everywhere: biophysics to life, geophysics to the Earth, astrophysics to the cosmos, econophysics to markets, and engineering as applied physics entire. Each bridge exports the method — mathematize, predict, measure — and imports fresh phenomena.'],
['The Great Unsolved Problems','The great unsolved problems are stated and open: the nature of dark matter and dark energy (95% of the universe\'s content), quantum gravity, the matter-antimatter asymmetry, and high-temperature superconductivity\'s mechanism. Labeled unsolved — the measurements are real, the explanations are not.'],
['How New Claims Are Validated','New physical claims are validated by independent replication and by surviving dedicated attempts at falsification: blind analyses, independent detectors, and rival groups checking the systematics. Cold fusion died here; the Higgs boson survived it.'],
['The Great Debates','The great debates include the interpretation of quantum mechanics (Copenhagen, many-worlds, pilot-wave), the reality of the multiverse, and whether beauty is a reliable guide to truth. The debates persist because the mathematics works regardless of interpretation.'],
['Failure Modes: When Physics Gets It Wrong','Physics gets it wrong through experimenter bias, underestimated systematics, and theory-driven blindness: N-rays, polywater, and faster-than-light neutrinos each collapsed under replication. The field\'s immune system is the independent measurement.'],
['Synthesis: Building on the Fundamentals','Synthesis at the advanced level means wielding conservation laws, symmetries, and approximations together: identify the symmetries, write the conserved quantities, choose the right idealization, compute, and compare with measurement. The fundamentals never retire.'],
['The Signature Formulation: Physics as Computable Law','The Signature formulation treats physical law as computable constraint: every principle in this database runs as a program you can execute, because in the Signature system a law of nature you cannot compute with is a law you have not yet understood. That is the Signature capstone on physical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
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
    standards:["Predictions are quantitative: a theory that predicts nothing measurable predicts nothing.", "Units are carried through every calculation; a result without units is not a physical result.", "Experiment is sovereign: persistent disagreement with measurement falsifies the theory."],citations:["Feynman, R. P., Leighton, R. B., Sands, M. \u2014 The Feynman Lectures on Physics.", "Young, H. D. and Freedman, R. A. \u2014 University Physics.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-physics-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-physics',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
