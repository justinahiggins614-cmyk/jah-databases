(function(){'use strict';
/* JAH The Everything Energy Database generator — jahdb-everything-energy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVEN-";
var FIELDS=["Fundamentals","Sources","Renewables","Systems","Signature Energy"];
var TOPICS={
 "Fundamentals": [
  "Energy Fundamentals: Forms, Units, Conservation \u2014 Fundamentals"
 ],
 "Sources": [
  "Fossil Fuels: Coal, Oil, and Natural Gas \u2014 Sources",
  "Nuclear Power: Fission and Reactors \u2014 Sources"
 ],
 "Renewables": [
  "Solar Power: Photovoltaics \u2014 Renewables",
  "Wind Power: Turbines and Farms \u2014 Renewables",
  "Hydropower: Dams and Flow \u2014 Renewables"
 ],
 "Systems": [
  "The Electric Grid: Generation to Outlet \u2014 Systems",
  "Energy Efficiency and Conservation \u2014 Systems"
 ],
 "Signature Energy": [
  "Signature Energy Flow Mapper (Signature Edition) \u2014 Signature Energy",
  "Signature Solar Geometry (Signature Edition) \u2014 Signature Energy",
  "Signature Grid Harmonizer (Signature Edition) \u2014 Signature Energy",
  "Signature Consumption Optimizer (Signature Edition) \u2014 Signature Energy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Energy — "+safe+"\n"
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
    name:topic+' — energy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A energy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
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
var gen={version:'jahdb-everything-energy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-energy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
