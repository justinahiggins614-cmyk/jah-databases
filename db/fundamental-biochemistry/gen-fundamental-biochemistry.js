(function(){'use strict';
/* JAH Fundamentals of Biochemistry Database generator — jahdb-fundamental-biochemistry-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIO2-";
var FIELDS=["amino acids and proteins", "enzymes", "carbohydrates", "lipids", "metabolism", "regulation"];
var TOPICS=[
    {t: "Water and the Hydrophobic Effect", b: "Life's solvent structures itself around nonpolar groups; burying hydrophobes drives protein folding and membrane formation."},
    {t: "Amino Acids: Twenty Building Blocks", b: "Side-chain chemistry (acidic, basic, polar, nonpolar) encodes everything proteins can do \u2014 the alphabet of function."},
    {t: "Protein Structure: Four Levels", b: "Sequence \u2192 local folds (\u03b1/\u03b2) \u2192 3-D tertiary shape \u2192 multi-subunit quaternary assembly: structure is function."},
    {t: "How Enzymes Work", b: "Active sites stabilize transition states, slashing activation energy: rate enhancements of 10\u2076\u201310\u00b9\u2077 over uncatalyzed reactions."},
    {t: "Enzyme Kinetics", b: "Michaelis-Menten parameters (Km, kcat) quantify affinity and speed; inhibition patterns (competitive, uncompetitive) reveal mechanism."},
    {t: "Carbohydrates: Fuel and Structure", b: "Glucose, glycogen, and cellulose share monomers but differ in linkages \u2014 \u03b1-links digest, \u03b2-links build plant walls."},
    {t: "Lipids and Membranes", b: "Phospholipid bilayers self-assemble into selective barriers; fluidity, rafts, and transporters make membranes smart."},
    {t: "Glycolysis", b: "Ten steps split glucose to pyruvate, netting 2 ATP: the ancient pathway every cell still runs."},
    {t: "The Citric Acid Cycle", b: "Acetyl-CoA oxidizes fully to CO\u2082 in the mitochondrial matrix, harvesting NADH/FADH\u2082 for the electron transport chain."},
    {t: "Oxidative Phosphorylation", b: "Electron flow pumps protons; ATP synthase harvests the gradient \u2014 ~30 ATP per glucose, life's main power plant."},
    {t: "Regulation: Allostery and Hormones", b: "Feedback inhibition, covalent modification, and insulin/glucagon signaling route metabolism to the body's needs."},
    {t: "Signal Transduction", b: "Receptors \u2192 second messengers \u2192 kinase cascades amplify faint signals into decisive cellular responses."}
];
var PRINCIPLES=[
    {n: "Michaelis-Menten", e: "v = Vmax\u00b7[S]/(Km + [S])", s: "Enzyme velocity saturates hyperbolically; Km is the substrate at half-maximum rate."},
    {n: "\u0394G\u00b0\u2032 = \u2212RT ln K\u2032", e: "equilibrium from free energy", s: "Biochemical equilibria follow the same thermodynamics, at pH 7 standard state."},
    {n: "ATP hydrolysis", e: "\u0394G\u00b0\u2032 \u2248 \u221230.5 kJ/mol", s: "The cell's energy currency spends about 30 kJ/mol per hydrolysis to drive work."}
];
var USES=["Designing enzyme inhibitors as drugs", "Diagnosing metabolic disorders", "Engineering fermentation pathways", "Interpreting blood chemistry panels"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Biochemistry"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Biochemistry demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-biochemistry-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-biochemistry-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-biochemistry",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
