(function(){'use strict';
/* JAH Signature Carpenter Profession Database generator — "jahdb-profession-carpenter-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Carpenters Do (Signature Edition)", "History of the Carpentry Trade (Signature Edition)", "Core Carpentry Skills (Signature Edition)", "The Apprenticeship Path (Signature Edition)", "Certification and Licensing (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life (Signature Edition)", "Divisions and Specialties (Signature Edition)", "Trade Ethics (Signature Edition)", "Pay and Career Outlook (Signature Edition)", "Giants of the Trade (Signature Edition)", "Getting Started (Signature Edition)"], "Compounded": ["Framing: The Structure (Signature Edition)", "Finish Carpentry (Signature Edition)", "Formwork: Molds for Concrete (Signature Edition)", "Reading Blueprints (Signature Edition)", "Stairs: The Geometry (Signature Edition)", "Roof Framing (Signature Edition)", "Decks and Outdoor Structures (Signature Edition)", "Cabinetmaking (Signature Edition)", "Remodeling (Signature Edition)", "Timber Framing (Signature Edition)", "Estimating Carpentry Work (Signature Edition)", "Running the Carpentry Business (Signature Edition)"], "Advanced": ["The Master Carpenter (Signature Edition)", "Safety: Saws and Heights (Signature Edition)", "The Union Brotherhood (Signature Edition)", "Green Building (Signature Edition)", "Technology in the Trade (Signature Edition)", "Teaching the Trade (Signature Edition)", "The Carpenter's Legacy (Signature Edition)", "The Business Philosophy (Signature Edition)", "The Trade's Impact (Signature Edition)", "The Master's Philosophy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-carpenter-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original profession record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original profession record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-profession-carpenter-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-carpenter-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
