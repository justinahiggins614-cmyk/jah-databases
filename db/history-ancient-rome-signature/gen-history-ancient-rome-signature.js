(function(){'use strict';
/* JAH Signature Ancient Rome Database generator — "jahdb-history-ancient-rome-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HRMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Founding of Rome (Signature Edition)", "The Roman Republic (Signature Edition)", "The Punic Wars (Signature Edition)", "Julius Caesar (Signature Edition)", "Augustus and the Birth of Empire (Signature Edition)", "The Legions (Signature Edition)", "Roman Law (Signature Edition)", "The City of Rome (Signature Edition)", "Roman Engineering: Roads, Aqueducts, Concrete (Signature Edition)", "The Colosseum and the Games (Signature Edition)", "The Pax Romana (Signature Edition)", "The Fall of Rome (Signature Edition)"], "Compounded": ["The Gracchi: Reform and Murder (Signature Edition)", "Marius and Sulla (Signature Edition)", "Cicero: Voice of the Republic (Signature Edition)", "Pompey the Great (Signature Edition)", "Nero: The Performer Emperor (Signature Edition)", "The Five Good Emperors (Signature Edition)", "Hadrian's Wall (Signature Edition)", "The Crisis of the Third Century (Signature Edition)", "Diocletian: The Rebuilder (Signature Edition)", "Constantine: The Turning Point (Signature Edition)", "The Division of the Empire (Signature Edition)", "The Senate Under the Emperors (Signature Edition)"], "Advanced": ["The Pantheon (Signature Edition)", "Virgil and the Aeneid (Signature Edition)", "Slavery in Rome (Signature Edition)", "Women in Rome (Signature Edition)", "The Roman Economy (Signature Edition)", "The Barbarian Migrations (Signature Edition)", "Byzantium: Rome's Eastern Afterlife (Signature Edition)", "Roman Britain (Signature Edition)", "The Auxiliaries: Rome's Global Army (Signature Edition)", "The Legacy of Rome (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-rome-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original history record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-history-ancient-rome-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-rome-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
