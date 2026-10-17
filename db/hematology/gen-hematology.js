(function(){'use strict';
/* JAH The Hematology Database generator — jahdb-hematology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Hematology: The Clinical Specialty of Blood - Foundations",
  "Blood Composition and Hematopoiesis: How the Body Makes Blood - Foundations",
  "The Complete Blood Count: Reading the CBC - Foundations",
  "Hemoglobin and Red Blood Cell Physiology - Foundations",
  "The Bone Marrow: The Body's Blood Factory - Foundations",
  "Iron, Vitamin B12, and Folate: The Red Cell Supply Lines - Foundations",
  "White Blood Cells and the Differential Count - Foundations",
  "The Hematology Clinical Encounter: History, Examination, and Workup - Foundations"
 ],
 "Compounded": [
  "Iron Deficiency Anemia: The Most Common Anemia - Compounded",
  "Vitamin B12 and Folate Deficiency: Megaloblastic Anemia - Compounded",
  "Anemia of Chronic Disease and Inflammation - Compounded",
  "Hemolytic Anemia: When Red Cells Break Apart - Compounded",
  "Thalassemia: The Inherited Hemoglobin Disorders - Compounded",
  "Sickle Cell Disease - Compounded",
  "Aplastic Anemia and Bone Marrow Failure - Compounded",
  "Myelodysplastic Syndromes: Clonal Marrow Disorders - Compounded",
  "Immune Thrombocytopenia (ITP) - Compounded",
  "The Coagulation Cascade: How Blood Clots - Compounded",
  "Hemophilia and von Willebrand Disease - Compounded",
  "Venous Thromboembolism and Thrombophilia - Compounded"
 ],
 "Advanced": [
  "Acute Leukemia: AML and ALL - Advanced",
  "Chronic Leukemias: CLL and CML - Advanced",
  "Lymphoma: Hodgkin and Non-Hodgkin - Advanced",
  "Multiple Myeloma and Plasma Cell Disorders - Advanced",
  "Myeloproliferative Neoplasms: PV, ET, and Myelofibrosis - Advanced",
  "Disseminated Intravascular Coagulation (DIC) - Advanced",
  "Transfusion Medicine: Blood Products and Compatibility - Advanced",
  "Transfusion Reactions and Hemovigilance - Advanced",
  "Hematopoietic Stem Cell Transplantation - Advanced",
  "Anticoagulant and Antiplatelet Therapy - Advanced",
  "Antiphospholipid Syndrome and Heparin-Induced Thrombocytopenia - Advanced",
  "Pediatric Hematology: Blood Disease in Children - Advanced",
  "Pregnancy and Blood: Hematologic Change and Disease - Advanced",
  "The Future of Hematology: Gene Therapy and CAR-T Cells - Advanced"
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
var gen={version:'jahdb-hematology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hematology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
