(function(){'use strict';
/* JAH The Gastroenterology Database generator — jahdb-gastroenterology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Gastroenterology: The Clinical Specialty of the Digestive System - Foundations",
  "The Digestive Tract: A Processing Line from Mouth to Anus - Foundations",
  "Digestion Chemistry: Enzymes, Acid, Bile, and Absorption - Foundations",
  "The Gut Wall: Layers, Motility, and Peristalsis - Foundations",
  "The Liver and Biliary System: Detoxification, Bile, and Metabolism - Foundations",
  "The Pancreas: Digestive Enzymes and the Insulin Balance - Foundations",
  "The Gut Microbiome: Clinical Aspects of the Resident Ecosystem - Foundations",
  "The GI Clinical Encounter: History, Exam, and Basic Tests - Foundations"
 ],
 "Compounded": [
  "GERD: Gastroesophageal Reflux Disease - Compounded",
  "Functional Dyspepsia and Disorders of Gut-Brain Interaction - Compounded",
  "Peptic Ulcer Disease and Helicobacter pylori - Compounded",
  "Upper GI Bleeding - Compounded",
  "Celiac Disease and the Malabsorption Workup - Compounded",
  "Irritable Bowel Syndrome - Compounded",
  "Motility Disorders: Gastroparesis and Esophageal Dysmotility - Compounded",
  "Inflammatory Bowel Disease: Crohn's Disease - Compounded",
  "Inflammatory Bowel Disease: Ulcerative Colitis - Compounded",
  "Lower GI Bleeding and Diverticular Disease - Compounded",
  "Colorectal Polyps and Cancer Screening - Compounded"
 ],
 "Advanced": [
  "Endoscopy and Colonoscopy: Concepts and Techniques - Advanced",
  "Endoscopic Therapy: Polypectomy, Banding, and ERCP - Advanced",
  "Acute Pancreatitis - Advanced",
  "Gallstone Disease and Cholecystitis - Advanced",
  "Biliary Obstruction and Jaundice - Advanced",
  "Chronic Liver Disease and Cirrhosis - Advanced",
  "Viral Hepatitis - Advanced",
  "Fatty Liver Disease: NAFLD and MASLD - Advanced",
  "GI Cancers: Esophageal and Gastric - Advanced",
  "GI Cancers: Colorectal - Advanced",
  "GI Cancers: Pancreatic and Hepatocellular - Advanced",
  "GI Emergencies: Perforation, Obstruction, and Ischemia - Advanced",
  "Nutritional Support: Enteral and Parenteral Feeding - Advanced",
  "Pediatric Gastroenterology - Advanced",
  "The Future of Gastroenterology: AI Endoscopy and Engineered Microbiomes - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Gastroenterology Study — "+safe+"\n"
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
    name:topic+' — gastroenterology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A gastroenterology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"gastroenterology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-gastroenterology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gastroenterology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
