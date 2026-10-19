(function(){'use strict';
/* JAH Fundamentals of Endocrinology Database generator — jahdb-fundamental-endocrinology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-END-";
var FIELDS=["hormone signaling", "pituitary axes", "thyroid", "pancreas and diabetes", "adrenals", "reproductive hormones"];
var TOPICS=[
    {t: "What Hormones Are", b: "Chemical messengers secreted into blood to coordinate distant tissues \u2014 slow, sustained signaling complementing nerves' speed."},
    {t: "Endocrine vs Paracrine vs Autocrine", b: "Hormones travel by blood, paracrine signals diffuse locally, autocrine signals feed back on the sender \u2014 three broadcast ranges."},
    {t: "The Pituitary: Master Gland", b: "Anterior pituitary tropic hormones (TSH, ACTH, LH/FSH, GH, prolactin) command the downstream glands under hypothalamic control."},
    {t: "HPA Axis: Stress", b: "Hypothalamus \u2192 pituitary \u2192 adrenal cortisol: the stress axis mobilizes energy and suppresses non-essentials \u2014 chronic activation harms."},
    {t: "Thyroid: Metabolic Throttle", b: "T4/T3 set basal metabolic rate; iodine deficiency, Hashimoto's, and Graves' disease show what happens when the throttle sticks."},
    {t: "Insulin and Glucagon", b: "Pancreatic islets balance blood glucose minute by minute; type 1 diabetes lacks insulin, type 2 resists it."},
    {t: "Diabetes Pathophysiology", b: "Hyperglycemia damages vessels, nerves, kidneys, and eyes over years \u2014 control of A1C is control of complications."},
    {t: "Adrenal Glands", b: "Cortisol (stress/metabolism), aldosterone (salt/water), adrenaline (fight-or-flight): three hormones, three survival systems."},
    {t: "Calcium: PTH and Vitamin D", b: "Parathyroid hormone and vitamin D defend blood calcium for nerves and bone \u2014 feedback loops spanning gut, kidney, and skeleton."},
    {t: "Reproductive Hormones", b: "GnRH \u2192 LH/FSH \u2192 estrogen/testosterone orchestrate puberty, cycles, and fertility \u2014 pulsatility encodes the message."},
    {t: "Growth Hormone Axis", b: "GH plus IGF-1 drive childhood growth; excess makes giants, deficiency makes short stature \u2014 timing is everything."},
    {t: "Endocrine Disruptors", b: "Some chemicals mimic or block hormones (BPA, phthalates): dose, timing, and developmental windows determine risk."}
];
var PRINCIPLES=[
    {n: "Negative feedback", e: "hormone \u2191 \u2192 signal \u2193", s: "Endocrine axes self-regulate: rising hormone suppresses its own stimulators \u2014 homeostasis by loop."},
    {n: "Half-life sets dynamics", e: "effect duration \u221d t\u00bd", s: "Peptide hormones act in minutes, steroids in hours, thyroid hormone for days."},
    {n: "Receptor specificity", e: "response = hormone \u00d7 receptor", s: "A hormone acts only where its receptor is expressed \u2014 distribution, not circulation, targets action."}
];
var USES=["Managing diabetes treatment", "Diagnosing thyroid disorders", "Treating hormone deficiencies", "Evaluating growth disorders"];
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
    id:id, t:tp.t, g:field, name:"Endocrinology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Endocrinology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-endocrinology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-endocrinology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-endocrinology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
