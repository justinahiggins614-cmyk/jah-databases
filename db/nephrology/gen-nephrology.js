(function(){'use strict';
/* JAH The Nephrology Database generator — jahdb-nephrology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NEPH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Nephrology: The Clinical Specialty of the Kidney - Foundations",
  "Kidney Anatomy and the Nephron: The Filtering Unit - Foundations",
  "Glomerular Filtration: How the Kidney Filters Blood - Foundations",
  "The Renal Tubule: Reabsorption and Secretion - Foundations",
  "Concentration and Dilution: The Countercurrent Multiplier - Foundations",
  "Total Body Water: Fluid Compartments - Foundations",
  "Glomerular Filtration Rate: Measuring Kidney Function - Foundations",
  "Urinalysis and Urine Microscopy: Reading the Urine - Foundations",
  "Sodium and Water Balance: Osmolarity and ADH - Foundations",
  "Acid-Base Balance: The Henderson-Hasselbalch Framework - Foundations",
  "The Nephrology Clinical Encounter: Evaluating Kidney Disease - Foundations"
 ],
 "Compounded": [
  "Hyponatremia: Too Little Sodium - Compounded",
  "Hypernatremia: Too Much Sodium - Compounded",
  "Potassium Disorders: Hyperkalemia and Hypokalemia - Compounded",
  "Calcium, Phosphate, and Magnesium Disorders - Compounded",
  "Metabolic Acidosis: The Anion Gap and the Delta Gap - Compounded",
  "Metabolic Alkalosis and Respiratory Acid-Base Disorders - Compounded",
  "Acute Kidney Injury: KDIGO Staging and Causes - Compounded",
  "Prerenal AKI and Acute Tubular Necrosis - Compounded",
  "Chronic Kidney Disease: Staging and Progression - Compounded",
  "Nephritic Syndrome and Glomerulonephritis - Compounded",
  "Nephrotic Syndrome: Protein in the Urine - Compounded",
  "Diabetic Kidney Disease - Compounded",
  "Hypertension and the Kidney - Compounded"
 ],
 "Advanced": [
  "Polycystic Kidney Disease and Inherited Kidney Disorders - Advanced",
  "Tubulointerstitial Disease and Drug-Induced Kidney Injury - Advanced",
  "Mineral and Bone Disorder of CKD - Advanced",
  "Anemia of Chronic Kidney Disease - Advanced",
  "Hemodialysis: Principles and Prescription - Advanced",
  "Peritoneal Dialysis and Dialysis Adequacy - Advanced",
  "Kidney Transplantation: Immunology and Concepts - Advanced",
  "Pregnancy and the Kidney: Preeclampsia - Advanced",
  "Pediatric Nephrology: The Growing Kidney - Advanced",
  "The Future of Nephrology: Wearable Kidneys and Xenotransplantation - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nephrology Study — "+safe+"\n"
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
    name:topic+' — nephrology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nephrology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nephrology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-nephrology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nephrology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
