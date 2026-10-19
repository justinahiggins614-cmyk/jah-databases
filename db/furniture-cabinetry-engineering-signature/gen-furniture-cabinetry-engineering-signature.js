(function(){'use strict';
/* JAH Signature Furniture and Cabinetry Engineering Database generator — "jahdb-furniture-cabinetry-engineering-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FURCAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Furniture Loads (Signature Edition)", "Wood as a Material (Signature Edition)", "Basic Joinery (Signature Edition)", "Sheet Goods (Plywood, MDF) (Signature Edition)", "Ergonomics: Chair Dimensions (Signature Edition)", "Ergonomics: Tables and Storage (Signature Edition)", "Finishing Basics (Signature Edition)"], "Compounded": ["Case Construction (Signature Edition)", "Drawers That Work (Signature Edition)", "Doors That Hang True (Signature Edition)", "Upholstery Basics (Signature Edition)", "Knock-Down Design (Signature Edition)", "Wood Movement Management (Signature Edition)", "Furniture Testing (Signature Edition)"], "Advanced": ["Custom Cabinetry (Signature Edition)", "Curved and Sculpted Work (Signature Edition)", "Production Furniture (Signature Edition)", "Restoration (Signature Edition)", "The Furniture Master Reference (Signature Edition)", "Heirloom Design Philosophy (Signature Edition)", "The Furniture and Cabinetry Engineering Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — furniture-cabinetry-engineering-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original furniture record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original furniture record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-furniture-cabinetry-engineering-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("furniture-cabinetry-engineering-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
