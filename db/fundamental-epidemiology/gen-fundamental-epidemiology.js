(function(){'use strict';
/* JAH Fundamentals of Epidemiology Database generator — jahdb-fundamental-epidemiology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPI-";
var FIELDS=["measures of disease", "transmission", "SIR modeling", "study designs", "bias and confounding", "outbreak response"];
var TOPICS=[
    {t: "Incidence vs Prevalence", b: "Incidence counts new cases per time; prevalence counts existing cases now \u2014 confusing them misleads policy."},
    {t: "The Epidemiologic Triad", b: "Agent, host, and environment interact to produce disease; control works by breaking any leg of the triangle."},
    {t: "Modes of Transmission", b: "Contact, droplet, airborne, vector-borne, and vehicle routes each demand different interventions \u2014 transmission mode dictates control."},
    {t: "R0 and Epidemic Growth", b: "The basic reproduction number sets doubling time and final size; pushing effective R below 1 is the whole strategy of control."},
    {t: "SIR Compartment Models", b: "Susceptible \u2192 Infectious \u2192 Recovered differential equations predict epidemic curves from a few parameters."},
    {t: "Herd Immunity", b: "Immune individuals break chains of transmission, protecting those who cannot be vaccinated \u2014 a population-level shield."},
    {t: "Cohort Studies", b: "Follow exposed and unexposed groups forward in time to compute relative risk \u2014 strong but slow and expensive."},
    {t: "Case-Control Studies", b: "Compare past exposures of cases vs controls: fast and cheap for rare diseases, vulnerable to recall bias."},
    {t: "Randomized Trials", b: "Randomization balances unknown confounders, making RCTs the gold standard for testing interventions."},
    {t: "Confounding and Bias", b: "Confounders distort associations; selection and measurement biases distort samples \u2014 design and analysis must hunt both."},
    {t: "Outbreak Investigation", b: "Case definitions, epidemic curves, and attack rates locate sources fast; shoe-leather epidemiology still solves outbreaks."},
    {t: "Surveillance Systems", b: "Sentinel sites, syndromic feeds, and genomic tracking turn scattered cases into early warnings."}
];
var PRINCIPLES=[
    {n: "Basic reproduction number", e: "R0 = \u03b2/\u03b3", s: "Each case generates R0 new ones in a susceptible population; R0 > 1 means growth."},
    {n: "Herd immunity threshold", e: "pc = 1 \u2212 1/R0", s: "The immune fraction needed to stop spread follows directly from R0."},
    {n: "Odds ratio", e: "OR = (a\u00b7d)/(b\u00b7c)", s: "The 2\u00d72-table measure of association in case-control studies."}
];
var USES=["Modeling epidemic trajectories", "Designing vaccination campaigns", "Investigating foodborne outbreaks", "Evaluating intervention effectiveness"];
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
    id:id, t:tp.t, g:field, name:"Epidemiology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Epidemiology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-epidemiology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-epidemiology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-epidemiology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
