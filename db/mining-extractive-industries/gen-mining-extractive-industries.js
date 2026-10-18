(function(){'use strict';
/* JAH The Mining and Extractive Industries Database generator — jahdb-mining-extractive-industries-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MNEI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Mining Is — Industry Overview - Foundations",
  "Minerals, Ores, and Grades - Foundations",
  "Geological Mapping - Foundations",
  "Exploration Drilling - Foundations",
  "Sampling and Assaying - Foundations",
  "Open Pit Mining - Foundations",
  "Underground Mining Methods - Foundations",
  "Drilling and Blasting - Foundations",
  "Loading and Hauling - Foundations",
  "Mine Ventilation Basics - Foundations",
  "Mine Safety Fundamentals - Foundations",
  "Mining Math I — Tonnage, Grade, and Metal Content - Foundations",
 ],
 "Compounded": [
  "Resource Estimation - Compounded",
  "JORC and NI 43-101 Reporting - Compounded",
  "Pit Optimization - Compounded",
  "Cut-Off Grade - Compounded",
  "Crushing and Grinding - Compounded",
  "Flotation Separation - Compounded",
  "Leaching — Heap and Tank - Compounded",
  "Smelting and Refining - Compounded",
  "Tailings Management - Compounded",
  "Mine Water Management - Compounded",
  "Geotechnical Engineering - Compounded",
 ],
 "Advanced": [
  "Strip Ratio Economics - Advanced",
  "Mineral Economics and Commodity Markets - Advanced",
  "Mine Planning Software and Scheduling - Advanced",
  "Ground Control - Advanced",
  "Mine Automation - Advanced",
  "Processing Plant Operations - Advanced",
  "Environmental Management - Advanced",
  "Mine Closure and Reclamation - Advanced",
  "Surveying in Mining - Advanced",
  "Metallurgical Accounting - Advanced",
  "Mining Mastery Review — Running the Whole Operation - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# Metal-content structural sample calculator (mining industries)\n"
   + "t, g = 1000000.0, 1.2\n"
   + "metal = t*g/100.0\n"
   + "print('sample tonnes:', t)\n"
   + "print('sample grade %:', g)\n"
   + "print('sample contained metal t:', round(metal,1))\n"
   + "assert metal > 0\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — mining industry record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mining industry record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mining-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mining-extractive-industries-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mining-extractive-industries',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
