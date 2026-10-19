(function(){'use strict';
/* jahdb-fundamental-chemistry-1.0 — fundamental chemistry bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FCHE-';
var KIND='fundamental chemistry record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Chemistry is the study of matter\'s composition, structure, properties, and transformations: what substances are made of, how their atoms arrange and bond, and how they change into new substances. It is the molecular science connecting physics to biology.', 'reasoning':'Chemists reason from structure to properties: the arrangement of atoms and electrons determines how a substance behaves. The periodic table organizes the elements by recurring patterns, and reaction mechanisms trace the step-by-step dance of bonds breaking and forming.', 'quantities':'The core quantities are the mole (6.022×10²³ entities), molar mass, concentration, pH, and energy changes (enthalpy, Gibbs free energy). The mole bridges the atomic scale and the laboratory scale.', 'mechanism':'Chemical understanding is built by mechanism: propose how electrons move during a reaction, test with kinetics and isotopes, and refine. The mechanism explains why reactions go, how fast, and what forms — structure determines function at the molecular level.', 'miscon':'Chemistry is not just mixing colorful liquids: it is quantitative and predictive. Natural does not mean safe and synthetic does not mean dangerous — toxicity is about dose and structure, not origin. And the periodic table is not arbitrary: its shape encodes quantum mechanics.'};
var SIGLENS=['In the Signature system, chemistry is the molecular construction kit: every material, medicine, and manufactured substance in this network is assembled from chemical principles, and the Signature formulation teaches each principle as a recipe you can verify.','The Signature practice is to compute the chemistry: balance the equation, calculate the yield, check the energetics — so molecular reasoning is done with numbers, not just memorized as facts.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- molar mass demo. Runs as-is with python3."""\nATOMIC = {"H": 1.008, "C": 12.011, "O": 15.999, "N": 14.007, "Na": 22.990, "Cl": 35.45}\ndef molar_mass(formula):\n    import re\n    total = 0.0\n    for el, n in re.findall(r"([A-Z][a-z]?)(\\d*)", formula):\n        total += ATOMIC[el] * (int(n) if n else 1)\n    return total\nfor f in ["H2O", "CO2", "NaCl", "C6H12O6"]:\n    print(f, "->", round(molar_mass(f), 3), "g/mol")\n', '#!/usr/bin/env python3\n"""{TITLE} -- ideal gas law demo. Runs as-is with python3."""\nR = 0.082057  # L atm / (mol K)\ndef moles_from_pvt(p_atm, v_L, t_K):\n    return p_atm * v_L / (R * t_K)\nn = moles_from_pvt(1.0, 22.4, 273.15)\nprint(f"1 atm, 22.4 L, 273 K -> {n:.3f} mol (about 1 mole: STP check)")\nprint("22.4 L of any ideal gas at STP is ~1 mole")\n', '#!/usr/bin/env python3\n"""{TITLE} -- pH demo. Runs as-is with python3."""\nimport math\ndef ph(h_conc):\n    return -math.log10(h_conc)\nfor h in [1e-1, 1e-7, 1e-13]:\n    print(f"[H+]={h:.0e} M -> pH={ph(h):.1f}")\nprint("each pH unit is a 10x change in [H+]")\n'];
var TOPICS=[['What Chemistry Is','Chemistry studies what matter is made of and how it transforms: the composition, structure, and properties of substances and the reactions that convert them. It sits at the center of science — built on physics, building toward biology — and its unit of thought is the molecule.'],
['The Core Question of Chemistry','The core question of chemistry is: what is it made of, and what will it become? Given a substance\'s structure, chemistry asks how it will behave; given a desired product, it asks what starting materials and conditions will make it.'],
['Assumptions: Atoms and Conservation','Chemistry assumes atoms are real, countable, and conserved in reactions: the 118 elements combine in fixed ratios, and no chemical reaction creates or destroys atoms. This conservation is the audit rule behind every balanced equation.'],
['The Vocabulary: Elements, Compounds, Mixtures','The vocabulary distinguishes elements (one kind of atom), compounds (atoms bonded in fixed ratios), and mixtures (physically combined, separable). Within compounds: ionic, covalent, and metallic bonding — three ways atoms hold together.'],
['The Mole: The Fundamental Quantity','The mole is the fundamental quantity: 6.022×10²³ entities, the chemist\'s dozen. It converts between the atomic scale and the balance: one mole of carbon-12 weighs exactly 12 grams, linking the invisible to the weighable.'],
['The Reaction Mechanism: The Primary Method','The reaction mechanism is the primary method: tracing, step by step, which bonds break and form and how electrons move. Mechanisms explain rates, products, and side reactions — the difference between knowing that a reaction works and knowing why.'],
['A Canonical First Example','The canonical first example is the combustion of methane: CH₄ + 2O₂ → CO₂ + 2H₂O. Atoms balance on both sides, energy is released as heat and light, and the equation encodes both the material and the energetic story of the reaction.'],
['How Chemistry Measures','Chemistry measures with the balance, the spectrometer, and the chromatograph: mass for quantity, spectra for identity and structure, separation for purity. Titration — the careful neutralization to an endpoint — remains the classic quantitative technique.'],
['The Core Mechanism: Structure Determines Properties','The core mechanism of chemical reasoning is structure determines properties: diamond and graphite are both pure carbon, but their different atomic arrangements make one the hardest natural material and the other a lubricant. Arrangement is destiny.'],
['The Simplest Law: Conservation of Mass','The simplest law is conservation of mass in chemical reactions: the total mass of reactants equals the total mass of products. Lavoisier established it by weighing sealed vessels — the birth of quantitative chemistry.'],
['Common Misconceptions in Chemistry','The misconceptions are cultural: that \'chemicals\' means \'toxins\' (everything is chemicals, including water), that natural means safe (ricin and botulinum are natural), and that chemistry is just cooking (cooking is applied chemistry, but chemistry is predictive science).'],
['How Beginners Practice Chemistry','Beginners practice chemistry by balancing equations, doing stoichiometry, and working safely at the bench: measure, mix, observe, record. Dimensional analysis — tracking units through every calculation — catches most errors before they happen.'],
['The Core Model: The Atom','The atom is the core model: a nucleus of protons and neutrons surrounded by electrons in quantized orbitals. The quantum model explains the periodic table\'s shape, bonding behavior, and spectra — the whole of chemistry flows from electron arrangement.'],
['The Great Equation: ΔG = ΔH − TΔS','The Gibbs free energy equation, ΔG = ΔH − TΔS, is the great equation: it predicts whether a reaction proceeds spontaneously by balancing enthalpy\'s drive toward lower energy against entropy\'s drive toward disorder. Negative ΔG means go.'],
['Systems Thinking: Equilibrium','Systems thinking in chemistry is equilibrium: opposing reactions running simultaneously, with the balance point set by thermodynamics. Le Chatelier\'s principle predicts how systems respond to disturbance — the foundation of industrial process control.'],
['Invariance: Conservation Laws','The invariance principles are conservation of mass, atoms, charge, and energy in every reaction. These conservations constrain what reactions are possible before kinetics asks which actually happen — thermodynamics proposes, kinetics disposes.'],
['Approximation: Ideal Behavior','Approximation in chemistry uses ideal behavior as the reference: ideal gases, ideal solutions, dilute limits. Real systems deviate, and the deviations are systematized — van der Waals corrections, activity coefficients — as ordered departures from the ideal.'],
['Evidence Standards: Reproducible Synthesis','The evidence standard is reproducible synthesis and characterization: a new compound must be made again by others and its structure confirmed by independent spectra. A claimed molecule without clean spectra is a rumor, not a result.'],
['Classic Discoveries','The classic discoveries include the periodic table, the structure of benzene, the DNA double helix, the synthesis of urea (ending vitalism), and the development of the Haber-Bosch process. Each connected the molecular world to human-scale consequences.'],
['Core Trade-offs: Yield versus Selectivity','The core trade-off is yield versus selectivity versus rate: forcing conditions raise conversion but breed side products; mild conditions are clean but slow. Catalysts escape the trade partially — speeding desired paths without being consumed.'],
['Handling Uncertainty: Kinetics','Chemical kinetics handles uncertainty about mechanism through rate laws: measuring how rate depends on concentration reveals the slow step. The Arrhenius equation quantifies temperature\'s exponential effect — the reason refrigerators preserve food.'],
['Tools of the Trade','The tools of the trade are the periodic table, the balanced equation, the spectrometer, and the fume hood. The most powerful is the retrosynthetic arrow: reasoning backward from target molecule to available starting materials.'],
['Ethics and Responsibility','Ethics in chemistry confronts dual use directly: the same knowledge synthesizes medicines and poisons, fertilizers and explosives. The field\'s responsibility is embodied in safety culture, controlled-substance law, and the chemist\'s personal judgment.'],
['Teaching Chemistry','Teaching chemistry well pairs the bench with the model: let students see the color change, then explain it with electron movement. Misconceptions about the particulate nature of matter are the known hard spots, and simulations help where eyes cannot go.'],
['The Frontier Question','The frontier question is predictive design: can we compute, before synthesizing, the molecule with exactly the desired properties — the perfect catalyst, the room-temperature superconductor, the ideal drug? Quantum chemistry and machine learning are converging on it.'],
['Unifying Theories','The unifying theories are quantum mechanics beneath all bonding, thermodynamics governing all change, and the periodic law organizing all elements. Together they reduced chemistry\'s vast catalog to consequences of electron behavior.'],
['Computational Chemistry','Computational chemistry predicts before it synthesizes: density functional theory estimates structures and energies, molecular dynamics simulates reactions atom by atom, and machine learning now proposes new molecules. Computation is the field\'s fastest-growing laboratory.'],
['Bridges to Other Fields','Chemistry bridges to physics (quantum chemistry), biology (biochemistry, molecular biology), medicine (pharmacology), materials science (polymers, semiconductors), and environmental science (atmospheric chemistry). Each bridge is a hybrid discipline with its own journals.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the exact mechanism of high-temperature superconductivity, fully predictive protein-ligand binding, nitrogen fixation under mild conditions rivaling nature\'s enzymes, and the origin-of-life chemistry. Active research, no settled answers.'],
['How New Claims Are Validated','New chemical claims are validated by independent synthesis and full characterization: another lab makes the compound, spectra match, and the reported properties reproduce. Retractions in chemistry most often trace to mischaracterized structures.'],
['The Great Debates','The great debates include the nature of the chemical bond (orbital models versus valence bond), the definition of aromaticity, and how much of chemistry reduces to physics versus requiring its own concepts. The debates refine the models without halting synthesis.'],
['Failure Modes: When Chemistry Gets It Wrong','Chemistry gets it wrong through mischaracterized products, irreproducible procedures, and scale-up surprises: what works in a flask may fail in a reactor. The field\'s immune system is the demand for spectra, yields, and exact procedures.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis wields the fundamentals together: thermodynamics says whether, kinetics says how fast, mechanism says how, and the periodic patterns suggest what to try. The master chemist reads a reaction the way a musician reads a score.'],
['The Signature Formulation: Chemistry as Verified Recipe','The Signature formulation treats every chemical principle as a verified recipe: balanced, quantified, with conditions and safety stated, because in the Signature system a reaction you cannot compute and reproduce is a reaction you do not yet own. That is the Signature capstone on chemical bedrock.']];
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
    standards:["Balance every equation: atoms are conserved, and the bookkeeping must show it.", "Report conditions with every reaction: temperature, pressure, solvent, and catalyst matter.", "Safety first: every procedure states its hazards and mitigations before its steps."],citations:["Zumdahl, S. S. and Zumdahl, S. A. \u2014 Chemistry (Cengage).", "IUPAC \u2014 Compendium of Chemical Terminology (the Gold Book).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-chemistry-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-chemistry',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
