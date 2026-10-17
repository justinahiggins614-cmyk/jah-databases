(function(){'use strict';
/* JAH The Endocrinology Database generator — jahdb-endocrinology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ENR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Endocrinology: The Science of Hormones and Chemical Signaling - Foundations",
  "The Endocrine System: Glands, Targets, and Feedback Loops - Foundations",
  "Hormone Classes: Peptides, Steroids, and Amines - Foundations",
  "Hormone Receptors: How Target Cells Read the Signal - Foundations",
  "The Hypothalamus: The Endocrine Command Center of the Brain - Foundations",
  "The Pituitary Gland: The Master Gland and Its Axes - Foundations",
  "Negative Feedback: The Thermostat Logic of Hormones - Foundations",
  "Hormone Synthesis, Storage, and Secretion: From Gene to Bloodstream - Foundations",
  "Measuring Hormones: Immunoassays and the Lab Workup - Foundations",
  "Hormone Half-Lives and Clearance: Timing the Message - Foundations"
 ],
 "Compounded": [
  "The Growth Hormone Axis: GH, IGF-1, and Growth Disorders - Compounded",
  "The Thyroid Axis: TSH, T3, T4, and Metabolic Rate - Compounded",
  "Hyperthyroidism and Hypothyroidism: When the Thyroid Axis Fails - Compounded",
  "The Adrenal Cortex: Cortisol, Aldosterone, and the Stress Response - Compounded",
  "The Adrenal Medulla: Catecholamines and Fight-or-Flight - Compounded",
  "Cushing Syndrome and Adrenal Insufficiency: Cortisol Disorders - Compounded",
  "Blood Glucose Control: Insulin, Glucagon, and the Pancreatic Islets - Compounded",
  "Diabetes Mellitus Type 1 and Type 2: Insulin Failure and Resistance - Compounded"
 ],
 "Advanced": [
  "Calcium Homeostasis: PTH, Vitamin D, and Calcitonin - Advanced",
  "Male Reproductive Endocrinology: Testosterone and Spermatogenesis - Advanced",
  "Female Reproductive Endocrinology: Estrogen, Progesterone, and the Cycle - Advanced",
  "The Posterior Pituitary: Oxytocin, Vasopressin, and Water Balance - Advanced",
  "Neuroendocrinology: The Brain as an Endocrine Organ - Advanced",
  "Endocrine Tumors: Adenomas, Pheochromocytoma, and MEN Syndromes - Advanced",
  "Polycystic Ovary Syndrome: The Commonest Endocrine Disorder - Advanced",
  "Thyroid Nodules and Thyroid Cancer: Evaluation Basics - Advanced",
  "Pituitary Tumors and Hyperprolactinemia: Reading the Sella - Advanced",
  "Dynamic Endocrine Testing: Stimulation and Suppression Tests - Advanced",
  "Congenital Adrenal Hyperplasia: Inborn Errors of Steroidogenesis - Advanced",
  "Obesity and Metabolic Syndrome: Hormones of Energy Balance - Advanced",
  "Therapeutic Hormones: Replacement, Contraception, and Pharmacology - Advanced",
  "Pediatric Endocrinology: Growth Failure and Precocious Puberty - Advanced",
  "Endocrine Emergencies: DKA, Thyroid Storm, and Adrenal Crisis - Advanced",
  "The Future of Endocrinology: GLP-1 Agonists and Hormone Medicine - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Endocrinology Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — endocrinology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A endocrinology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"endocrinology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-endocrinology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('endocrinology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
