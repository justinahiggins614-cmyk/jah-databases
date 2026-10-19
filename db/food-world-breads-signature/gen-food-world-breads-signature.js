(function(){'use strict';
/* JAH Signature World Breads Database generator — "jahdb-food-world-breads-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FWBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Baguette — France (Signature Edition)", "Sourdough — Ancient (Signature Edition)", "Naan — South Asia (Signature Edition)", "Tortilla — Mexico (Signature Edition)", "Pita — Middle East (Signature Edition)", "Bagel — Poland/New York (Signature Edition)", "Focaccia — Italy (Signature Edition)", "Pretzel — Germany (Signature Edition)", "Injera — Ethiopia/Eritrea (Signature Edition)", "Croissant — France (Signature Edition)", "Rye Bread — Northern Europe (Signature Edition)", "English Muffin (Signature Edition)"], "Compounded": ["Paratha — South Asia (Signature Edition)", "Lavash — Armenia (Signature Edition)", "Bannock — Scotland (Signature Edition)", "Mantou — China (Signature Edition)", "Arepa — Venezuela/Colombia (Signature Edition)", "Kulcha — Punjab (Signature Edition)", "Crumpet — England (Signature Edition)", "Irish Soda Bread (Signature Edition)", "Challah (Signature Edition)", "Panettone — Italy (Signature Edition)", "Rugbrød — Denmark (Signature Edition)", "Msemen — Maghreb (Signature Edition)"], "Advanced": ["Limpa — Sweden (Signature Edition)", "Pumpernickel — Germany (Signature Edition)", "Khobz — Morocco (Signature Edition)", "Sangak — Iran (Signature Edition)", "Lefse — Norway (Signature Edition)", "Anadama Bread (Signature Edition)", "Hallulla — Chile (Signature Edition)", "Taboon — Levant (Signature Edition)", "Qistibi — Tatarstan (Signature Edition)", "Heritage Grain Revival (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — food-world-breads-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original food record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original food record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-food-world-breads-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("food-world-breads-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
