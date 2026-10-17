(function(){'use strict';
/* JAH The Gastroenterology Signature Database generator — jahdb-gastroenterology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GASS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Gastroenterology: The Clinical Specialty of the Digestive System (Signature Edition) - Foundations",
  "The Digestive Tract: A Processing Line from Mouth to Anus (Signature Edition) - Foundations",
  "Digestion Chemistry: Enzymes, Acid, Bile, and Absorption (Signature Edition) - Foundations",
  "The Gut Wall: Layers, Motility, and Peristalsis (Signature Edition) - Foundations",
  "The Liver and Biliary System: Detoxification, Bile, and Metabolism (Signature Edition) - Foundations",
  "The Pancreas: Digestive Enzymes and the Insulin Balance (Signature Edition) - Foundations",
  "The Gut Microbiome: Clinical Aspects of the Resident Ecosystem (Signature Edition) - Foundations",
  "The GI Clinical Encounter: History, Exam, and Basic Tests (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "GERD: Gastroesophageal Reflux Disease (Signature Edition) - Compounded",
  "Functional Dyspepsia and Disorders of Gut-Brain Interaction (Signature Edition) - Compounded",
  "Peptic Ulcer Disease and Helicobacter pylori (Signature Edition) - Compounded",
  "Upper GI Bleeding (Signature Edition) - Compounded",
  "Celiac Disease and the Malabsorption Workup (Signature Edition) - Compounded",
  "Irritable Bowel Syndrome (Signature Edition) - Compounded",
  "Motility Disorders: Gastroparesis and Esophageal Dysmotility (Signature Edition) - Compounded",
  "Inflammatory Bowel Disease: Crohn's Disease (Signature Edition) - Compounded",
  "Inflammatory Bowel Disease: Ulcerative Colitis (Signature Edition) - Compounded",
  "Lower GI Bleeding and Diverticular Disease (Signature Edition) - Compounded",
  "Colorectal Polyps and Cancer Screening (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Endoscopy and Colonoscopy: Concepts and Techniques (Signature Edition) - Advanced",
  "Endoscopic Therapy: Polypectomy, Banding, and ERCP (Signature Edition) - Advanced",
  "Acute Pancreatitis (Signature Edition) - Advanced",
  "Gallstone Disease and Cholecystitis (Signature Edition) - Advanced",
  "Biliary Obstruction and Jaundice (Signature Edition) - Advanced",
  "Chronic Liver Disease and Cirrhosis (Signature Edition) - Advanced",
  "Viral Hepatitis (Signature Edition) - Advanced",
  "Fatty Liver Disease: NAFLD and MASLD (Signature Edition) - Advanced",
  "GI Cancers: Esophageal and Gastric (Signature Edition) - Advanced",
  "GI Cancers: Colorectal (Signature Edition) - Advanced",
  "GI Cancers: Pancreatic and Hepatocellular (Signature Edition) - Advanced",
  "GI Emergencies: Perforation, Obstruction, and Ischemia (Signature Edition) - Advanced",
  "Nutritional Support: Enteral and Parenteral Feeding (Signature Edition) - Advanced",
  "Pediatric Gastroenterology (Signature Edition) - Advanced",
  "The Future of Gastroenterology: AI Endoscopy and Engineered Microbiomes (Signature Edition) - Advanced"
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
var gen={version:'jahdb-gastroenterology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gastroenterology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
