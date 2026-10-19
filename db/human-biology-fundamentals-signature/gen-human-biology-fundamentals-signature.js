(function(){'use strict';
/* JAH Human Biology Fundamentals Database generator — jahdb-human-biology-fundamentals-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HUMABFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Cells (Signature Edition)", "DNA and Genes (Signature Edition)", "The Skeletal System (Signature Edition)", "Muscles (Signature Edition)", "The Nervous System (Signature Edition)", "The Brain (Signature Edition)", "Senses (Signature Edition)", "The Circulatory System (Signature Edition)", "Blood (Signature Edition)", "The Respiratory System (Signature Edition)", "The Digestive System (Signature Edition)"], "Compounded": ["The Immune System (Signature Edition)", "The Endocrine System (Signature Edition)", "The Urinary System (Signature Edition)", "The Reproductive System (Signature Edition)", "Skin (Signature Edition)", "Homeostasis (Signature Edition)", "Metabolism (Signature Edition)", "The Microbiome (Signature Edition)", "Aging (Signature Edition)", "Genetics and Health (Signature Edition)", "The Stress Response (Signature Edition)", "Sleep Biology (Signature Edition)"], "Advanced": ["Nutrition Biology (Signature Edition)", "Exercise Physiology (Signature Edition)", "The Annual Body Review (Signature Edition)", "Teaching Biology (Signature Edition)", "Medical Literacy (Signature Edition)", "Frontiers (Signature Edition)", "The Wonder of the Body (Signature Edition)", "The Lymphatic System (Signature Edition)", "The Endocrine Feedback (Signature Edition)", "Connective Tissue (Signature Edition)", "The Annual Curiosity Review (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — biology guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — biology guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A biology guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"human-biology-fundamentals-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-human-biology-fundamentals-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("human-biology-fundamentals-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
