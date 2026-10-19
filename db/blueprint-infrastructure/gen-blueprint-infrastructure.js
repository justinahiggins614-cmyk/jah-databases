(function(){'use strict';
/* JAH The Infrastructure Blueprint Database generator — jahdb-blueprint-infrastructure-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIP-";
var FIELDS=["Crossings","Energy","Transport","Water"];
var TOPICS={
 "Crossings": [
  "Suspension Bridge - Compact Architectural Blueprint - Crossings",
  "Railway Tunnel - Compact Architectural Blueprint - Crossings",
  "Suspension Bridge - Standard Architectural Blueprint - Crossings",
  "Railway Tunnel - Standard Architectural Blueprint - Crossings",
  "Suspension Bridge - Grand Architectural Blueprint - Crossings",
  "Railway Tunnel - Grand Architectural Blueprint - Crossings"
 ],
 "Energy": [
  "Electrical Substation - Compact Architectural Blueprint - Energy",
  "Cell Tower - Compact Architectural Blueprint - Energy",
  "Solar Farm Array - Compact Architectural Blueprint - Energy",
  "Wind Farm - Compact Architectural Blueprint - Energy",
  "Electrical Substation - Standard Architectural Blueprint - Energy",
  "Cell Tower - Standard Architectural Blueprint - Energy",
  "Solar Farm Array - Standard Architectural Blueprint - Energy",
  "Wind Farm - Standard Architectural Blueprint - Energy",
  "Electrical Substation - Grand Architectural Blueprint - Energy",
  "Cell Tower - Grand Architectural Blueprint - Energy",
  "Solar Farm Array - Grand Architectural Blueprint - Energy"
 ],
 "Transport": [
  "Highway Interchange - Compact Architectural Blueprint - Transport",
  "Airport Terminal - Compact Architectural Blueprint - Transport",
  "Highway Interchange - Standard Architectural Blueprint - Transport",
  "Airport Terminal - Standard Architectural Blueprint - Transport",
  "Highway Interchange - Grand Architectural Blueprint - Transport",
  "Airport Terminal - Grand Architectural Blueprint - Transport"
 ],
 "Water": [
  "Concrete Dam - Compact Architectural Blueprint - Water",
  "Water Treatment Plant - Compact Architectural Blueprint - Water",
  "Sewer Lift Station - Compact Architectural Blueprint - Water",
  "Canal Lock - Compact Architectural Blueprint - Water",
  "Concrete Dam - Standard Architectural Blueprint - Water",
  "Water Treatment Plant - Standard Architectural Blueprint - Water",
  "Sewer Lift Station - Standard Architectural Blueprint - Water",
  "Canal Lock - Standard Architectural Blueprint - Water",
  "Concrete Dam - Grand Architectural Blueprint - Water",
  "Water Treatment Plant - Grand Architectural Blueprint - Water",
  "Sewer Lift Station - Grand Architectural Blueprint - Water"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Infrastructure Blueprint Study — "+safe+"\n"
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
    name:topic+' — infrastructure blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A infrastructure blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-infrastructure-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-infrastructure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
