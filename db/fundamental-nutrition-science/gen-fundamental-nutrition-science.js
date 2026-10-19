(function(){'use strict';
/* JAH Fundamentals of Nutrition Science Database generator — jahdb-fundamental-nutrition-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NS-";
var FIELDS=["macronutrients", "micronutrients", "energy balance", "digestion", "dietary patterns", "research methods"];
var TOPICS=[
    {t: "Why We Eat: Energy and Building Blocks", b: "Food supplies fuel (ATP) and materials (amino acids, fatty acids) \u2014 every nutrient serves one or both roles."},
    {t: "Protein: Structure and Repair", b: "Essential amino acids must come from diet; protein needs rise with growth, training, illness, and age-related muscle loss."},
    {t: "Carbohydrates: Fast Fuel", b: "Glucose powers the brain; glycemic index ranks how fast foods raise blood sugar \u2014 fiber slows the whole process."},
    {t: "Fats: Essential and Misunderstood", b: "Essential fatty acids, fat-soluble vitamins, and hormones all need dietary fat; type matters more than total amount."},
    {t: "Vitamins: Cofactors of Life", b: "Thirteen vitamins enable enzymes to work: C and B-complex dissolve in water, A/D/E/K in fat \u2014 each deficiency has a signature disease."},
    {t: "Minerals and Electrolytes", b: "Iron carries oxygen, calcium builds bone, sodium and potassium run nerves \u2014 minerals are elements the body cannot make."},
    {t: "Water: The Forgotten Nutrient", b: "Water is the body's most abundant molecule and most essential nutrient; even mild dehydration impairs cognition and performance."},
    {t: "Digestion and Absorption", b: "Enzymes dismantle food stepwise from mouth to intestine; the gut microbiome ferments what human enzymes cannot."},
    {t: "Energy Balance and Weight", b: "Sustained calorie surplus stores fat, deficit burns it \u2014 hormones, sleep, and food environment modulate the simple equation."},
    {t: "Dietary Patterns, Not Single Foods", b: "Mediterranean, DASH, and balanced plant-rich patterns outperform single-nutrient fixes in the long-term evidence."},
    {t: "Nutrition Across the Lifespan", b: "Pregnancy, infancy, adolescence, and older age each shift requirements \u2014 one diet never fits all stages."},
    {t: "Reading Nutrition Research", b: "RCTs, cohorts, and meta-analyses form an evidence hierarchy; funding, confounding, and effect size separate signal from hype."}
];
var PRINCIPLES=[
    {n: "Energy balance", e: "\u0394stores = intake \u2212 expenditure", s: "Body energy stores change by the difference between calories in and calories out."},
    {n: "Atwater factors", e: "4 / 4 / 9 kcal per gram", s: "Protein and carbohydrate yield ~4 kcal/g, fat ~9, alcohol ~7 \u2014 the calorie accounting basis."},
    {n: "BMR estimation (Mifflin-St Jeor)", e: "BMR from weight, height, age, sex", s: "Resting metabolic rate is predictable from body size and composition."}
];
var USES=["Planning balanced institutional menus", "Counseling on weight management", "Preventing micronutrient deficiencies", "Evaluating diet claims critically"];
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
    id:id, t:tp.t, g:field, name:"Nutrition Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Nutrition Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-nutrition-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-nutrition-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-nutrition-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
