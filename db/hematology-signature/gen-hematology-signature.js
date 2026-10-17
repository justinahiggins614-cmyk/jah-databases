(function(){'use strict';
/* JAH The Hematology Signature Database generator — jahdb-hematology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Hematology: The Clinical Specialty of Blood (Signature Edition) - Foundations",
  "Blood Composition and Hematopoiesis: How the Body Makes Blood (Signature Edition) - Foundations",
  "The Complete Blood Count: Reading the CBC (Signature Edition) - Foundations",
  "Hemoglobin and Red Blood Cell Physiology (Signature Edition) - Foundations",
  "The Bone Marrow: The Body's Blood Factory (Signature Edition) - Foundations",
  "Iron, Vitamin B12, and Folate: The Red Cell Supply Lines (Signature Edition) - Foundations",
  "White Blood Cells and the Differential Count (Signature Edition) - Foundations",
  "The Hematology Clinical Encounter: History, Examination, and Workup (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Iron Deficiency Anemia: The Most Common Anemia (Signature Edition) - Compounded",
  "Vitamin B12 and Folate Deficiency: Megaloblastic Anemia (Signature Edition) - Compounded",
  "Anemia of Chronic Disease and Inflammation (Signature Edition) - Compounded",
  "Hemolytic Anemia: When Red Cells Break Apart (Signature Edition) - Compounded",
  "Thalassemia: The Inherited Hemoglobin Disorders (Signature Edition) - Compounded",
  "Sickle Cell Disease (Signature Edition) - Compounded",
  "Aplastic Anemia and Bone Marrow Failure (Signature Edition) - Compounded",
  "Myelodysplastic Syndromes: Clonal Marrow Disorders (Signature Edition) - Compounded",
  "Immune Thrombocytopenia (ITP) (Signature Edition) - Compounded",
  "The Coagulation Cascade: How Blood Clots (Signature Edition) - Compounded",
  "Hemophilia and von Willebrand Disease (Signature Edition) - Compounded",
  "Venous Thromboembolism and Thrombophilia (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Acute Leukemia: AML and ALL (Signature Edition) - Advanced",
  "Chronic Leukemias: CLL and CML (Signature Edition) - Advanced",
  "Lymphoma: Hodgkin and Non-Hodgkin (Signature Edition) - Advanced",
  "Multiple Myeloma and Plasma Cell Disorders (Signature Edition) - Advanced",
  "Myeloproliferative Neoplasms: PV, ET, and Myelofibrosis (Signature Edition) - Advanced",
  "Disseminated Intravascular Coagulation (DIC) (Signature Edition) - Advanced",
  "Transfusion Medicine: Blood Products and Compatibility (Signature Edition) - Advanced",
  "Transfusion Reactions and Hemovigilance (Signature Edition) - Advanced",
  "Hematopoietic Stem Cell Transplantation (Signature Edition) - Advanced",
  "Anticoagulant and Antiplatelet Therapy (Signature Edition) - Advanced",
  "Antiphospholipid Syndrome and Heparin-Induced Thrombocytopenia (Signature Edition) - Advanced",
  "Pediatric Hematology: Blood Disease in Children (Signature Edition) - Advanced",
  "Pregnancy and Blood: Hematologic Change and Disease (Signature Edition) - Advanced",
  "The Future of Hematology: Gene Therapy and CAR-T Cells (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hematology Study — "+safe+"\n"
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
    name:topic+' — hematology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hematology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hematology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-hematology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hematology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
