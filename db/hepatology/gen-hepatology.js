(function(){'use strict';
/* JAH The Hepatology Database generator — jahdb-hepatology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Hepatology: The Clinical Specialty of the Liver, Biliary Tract, and Pancreas - Foundations",
  "The Liver: Lobes, Segments, and Vascular Architecture - Foundations",
  "The Biliary Tree and Pancreatic Ducts: Plumbing of the Upper Abdomen - Foundations",
  "Liver Physiology: The Body's Chemical Refinery - Foundations",
  "Bilirubin Metabolism: From Red Cells to Bile - Foundations",
  "Liver Function Testing: Reading the LFT Panel - Foundations",
  "The Hepatology Clinical Encounter: History, Examination, and the Jaundiced Patient - Foundations"
 ],
 "Compounded": [
  "Acute Viral Hepatitis: The A, B, C, D, and E Viruses - Compounded",
  "Chronic Hepatitis B: Natural History and Antiviral Therapy - Compounded",
  "Gallstone Disease: Formation, Symptoms, and Treatment - Compounded",
  "Chronic Hepatitis C: From Interferon to Direct-Acting Cure - Compounded",
  "Autoimmune Hepatitis and Overlap Syndromes - Compounded",
  "Alcoholic Liver Disease: Steatosis to Cirrhosis - Compounded",
  "Acute Pancreatitis: Diagnosis, Severity, and Management in Hepatology - Compounded",
  "Metabolic Liver Disease: MASLD, Hemochromatosis, and Wilson Disease - Compounded",
  "Drug-Induced Liver Injury - Compounded",
  "Cholestatic Liver Disease: PBC and PSC - Compounded",
  "Chronic Pancreatitis and Pancreatic Exocrine Insufficiency - Compounded"
 ],
 "Advanced": [
  "Cirrhosis: From Fibrosis to End-Stage Liver Disease - Advanced",
  "Portal Hypertension: Varices, Shunts, and Bleeding - Advanced",
  "Acute Liver Failure: Kings College Criteria and Transplant Listing - Advanced",
  "Liver Biopsy and Elastography: Measuring Fibrosis - Advanced",
  "ERCP and Biliary Endoscopy: Stenting the Bile Duct - Advanced",
  "Hepatic Encephalopathy: Ammonia and the Brain - Advanced",
  "Ascites and Spontaneous Bacterial Peritonitis - Advanced",
  "Hepatorenal Syndrome and the Kidney in Liver Failure - Advanced",
  "The MELD and Child-Pugh Scores: Predicting Liver Outcomes - Advanced",
  "Hepatocellular Carcinoma: Surveillance and Treatment - Advanced",
  "Cholangiocarcinoma and Biliary Cancers - Advanced",
  "Pancreatic Cancer: Detection and Management - Advanced",
  "Liver Transplantation: Evaluation, Surgery, and Immunosuppression - Advanced",
  "Pediatric Hepatology: Biliary Atresia and Inherited Disease - Advanced",
  "Pregnancy and the Liver: AFLP, HELLP, and Cholestasis - Advanced",
  "The Future of Hepatology: NASH Therapies, Artificial Liver, and Precision Transplantation - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hepatology Study — "+safe+"\n"
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
    name:topic+' — hepatology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hepatology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hepatology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-hepatology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hepatology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
