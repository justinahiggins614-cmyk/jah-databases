(function(){'use strict';
/* JAH Fundamentals of Toxicology Database generator — jahdb-fundamental-toxicology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TOX-";
var FIELDS=["dose-response", "ADME", "mechanisms", "testing", "risk assessment", "clinical toxicology"];
var TOPICS=[
    {t: "The Dose Makes the Poison", b: "Paracelsus (1538): water kills by overhydration, botulinum kills at nanograms \u2014 toxicity is quantitative, never absolute."},
    {t: "Dose-Response Curves", b: "Threshold, linear, and hormetic shapes describe how effects scale; NOAEL/LOAEL anchor regulatory limits."},
    {t: "ADME: What the Body Does", b: "Absorption, distribution, metabolism, excretion determine internal dose \u2014 the same swallowed dose differs wildly by route and chemistry."},
    {t: "Biotransformation", b: "Phase I (oxidation, often CYP450) and Phase II (conjugation) usually detoxify \u2014 but sometimes activate (acetaminophen, aflatoxin)."},
    {t: "Mechanisms of Harm", b: "Receptor binding, enzyme inhibition, DNA damage, oxidative stress, membrane disruption: the molecular ways poisons work."},
    {t: "Target Organ Toxicity", b: "Liver (metabolism), kidney (excretion), lung (inhalation), nerves (lipophilic access): chemistry predicts the victim organ."},
    {t: "Carcinogenesis", b: "Initiation (mutation), promotion (proliferation), progression: multistage models explain why cancer risk accumulates with dose and time."},
    {t: "Developmental Toxicity", b: "Teratogens strike during narrow windows (thalidomide days 20\u201336): timing matters as much as dose in pregnancy."},
    {t: "Testing: From Cells to Animals", b: "In vitro screens, animal bioassays, and epidemiology form a tiered evidence ladder \u2014 each with strengths and limits."},
    {t: "Risk Assessment", b: "Hazard ID \u2192 dose-response \u2192 exposure assessment \u2192 risk characterization: the four-step framework behind every safety standard."},
    {t: "Clinical Toxicology", b: "Decontamination, antidotes (naloxone, NAC, chelators), and supportive care: treating poisoned patients by mechanism."},
    {t: "Regulatory Toxicology", b: "Reference doses, margins of exposure, and precaution: how agencies turn data into permissible limits."}
];
var PRINCIPLES=[
    {n: "Paracelsus principle", e: "dose makes the poison", s: "Every substance is toxic at some dose; safety is always about amount, not identity."},
    {n: "Dose-response", e: "effect = f(log dose)", s: "Sigmoidal curves relate dose to response; LD50/ED50 mark the midpoints."},
    {n: "Haber\u2019s rule", e: "C \u00d7 t = constant effect", s: "For many gases, concentration times exposure time predicts toxicity."}
];
var USES=["Setting chemical exposure limits", "Treating poisoning cases", "Assessing drug safety", "Investigating environmental contamination"];
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
    id:id, t:tp.t, g:field, name:"Toxicology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Toxicology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-toxicology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-toxicology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-toxicology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
