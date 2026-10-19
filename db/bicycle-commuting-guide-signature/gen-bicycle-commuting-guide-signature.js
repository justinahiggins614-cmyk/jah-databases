(function(){'use strict';
/* JAH Bicycle Commuting Guide Database generator — jahdb-bicycle-commuting-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BICYCGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Choosing a Commuter Bike (Signature Edition)", "Bike Fit (Signature Edition)", "Essential Gear (Signature Edition)", "Route Planning (Signature Edition)", "Riding in Traffic (Signature Edition)", "Intersections (Signature Edition)", "Night Riding (Signature Edition)", "Weather Riding (Signature Edition)", "Workplace Logistics (Signature Edition)", "Basic Maintenance (Signature Edition)", "Flat Repair (Signature Edition)"], "Compounded": ["Locking Strategy (Signature Edition)", "E-Bikes (Signature Edition)", "Riding With Cargo (Signature Edition)", "Group and Family Riding (Signature Edition)", "Legal Rights (Signature Edition)", "Fitness Building (Signature Edition)", "Teaching Bike Commuting (Signature Edition)", "The Annual Cycling Review (Signature Edition)", "Bike Types Compared (Signature Edition)", "Buying Used Bikes (Signature Edition)", "Saddles (Signature Edition)", "Tires for Commuting (Signature Edition)"], "Advanced": ["Brakes (Signature Edition)", "Gears (Signature Edition)", "Chain Care (Signature Edition)", "Winter Commuting (Signature Edition)", "Bike Computers (Signature Edition)", "Commuting With Kids (Signature Edition)", "Bike Share (Signature Edition)", "Advocacy (Signature Edition)", "The Car-Free Challenge (Signature Edition)", "Touring (Signature Edition)", "The Upgrade Path (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — cycling guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — cycling guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cycling guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"bicycle-commuting-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-bicycle-commuting-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("bicycle-commuting-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
