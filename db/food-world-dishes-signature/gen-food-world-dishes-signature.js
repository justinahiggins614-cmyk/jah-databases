(function(){'use strict';
/* JAH Signature World Dishes Database generator — "jahdb-food-world-dishes-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FWDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Pizza Margherita — Italy (Signature Edition)", "Sushi — Japan (Signature Edition)", "Tacos al Pastor — Mexico (Signature Edition)", "Pad Thai — Thailand (Signature Edition)", "Tagine — Morocco (Signature Edition)", "Butter Chicken — India (Signature Edition)", "Ramen — Japan (Signature Edition)", "Paella — Spain (Signature Edition)", "Hamburger — United States (Signature Edition)", "Pho — Vietnam (Signature Edition)", "Croissant — France (Signature Edition)", "Feijoada — Brazil (Signature Edition)"], "Compounded": ["Dim Sum — China (Signature Edition)", "Ceviche — Peru (Signature Edition)", "Biryani — South Asia (Signature Edition)", "Moussaka — Greece (Signature Edition)", "Gumbo — Louisiana (Signature Edition)", "Sauerbraten — Germany (Signature Edition)", "Bibimbap — Korea (Signature Edition)", "Haggis — Scotland (Signature Edition)", "Falafel — Middle East (Signature Edition)", "Poutine — Canada (Signature Edition)", "Rendang — Indonesia/Malaysia (Signature Edition)", "Khachapuri — Georgia (Signature Edition)"], "Advanced": ["Couscous — North Africa (Signature Edition)", "Mole Poblano — Mexico (Signature Edition)", "Wiener Schnitzel — Austria (Signature Edition)", "Bouillabaisse — France (Signature Edition)", "Peking Duck — China (Signature Edition)", "Moqueca — Brazil (Signature Edition)", "Hákarl — Iceland (Signature Edition)", "Borscht — Eastern Europe (Signature Edition)", "Pastilla — Morocco (Signature Edition)", "Kaiseki — Japan (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — food-world-dishes-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-food-world-dishes-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("food-world-dishes-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
