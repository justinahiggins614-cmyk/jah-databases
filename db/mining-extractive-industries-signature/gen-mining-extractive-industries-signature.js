(function(){'use strict';
/* JAH The Mining and Extractive Industries Signature Database generator — jahdb-mining-extractive-industries-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MNEIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Delving Art — The Signature View (Signature Edition) - Foundations",
  "The Earth's Ledger — Signature Minerals and Grades (Signature Edition) - Foundations",
  "Reading the Ground — Signature Mapping (Signature Edition) - Foundations",
  "The Questioning Holes — Signature Drilling (Signature Edition) - Foundations",
  "Sworn Testimony — Signature Sampling and Assay (Signature Edition) - Foundations",
  "The Open Bowl — Signature Open Pit (Signature Edition) - Foundations",
  "The Deep Ways — Signature Underground Methods (Signature Edition) - Foundations",
  "The Breaking Art — Signature Drilling and Blasting (Signature Edition) - Foundations",
  "The Endless Caravan — Signature Loading and Hauling (Signature Edition) - Foundations",
  "The Breath Below — Signature Ventilation (Signature Edition) - Foundations",
  "The Homecoming Vow — Signature Mine Safety (Signature Edition) - Foundations",
  "The Founding Sum — Signature Mining Math (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "Numbering the Hidden — Signature Resource Estimation (Signature Edition) - Compounded",
  "The Honest Proclamation — Signature Reporting Codes (Signature Edition) - Compounded",
  "The Wisest Bowl — Signature Pit Optimization (Signature Edition) - Compounded",
  "The Ruling Line — Signature Cut-Off Grade (Signature Edition) - Compounded",
  "The Liberation — Signature Crushing and Grinding (Signature Edition) - Compounded",
  "The Floating Harvest — Signature Flotation (Signature Edition) - Compounded",
  "The Dissolving — Signature Leaching (Signature Edition) - Compounded",
  "The Refining Fire — Signature Smelting (Signature Edition) - Compounded",
  "The Forever Dam — Signature Tailings (Signature Edition) - Compounded",
  "The Counted Waters — Signature Mine Water (Signature Edition) - Compounded",
  "The Standing Ground — Signature Geotechnics (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Pit's Pulse — Signature Strip Ratios (Signature Edition) - Advanced",
  "The Market's Tides — Signature Mineral Economics (Signature Edition) - Advanced",
  "The Promised Sequence — Signature Mine Scheduling (Signature Edition) - Advanced",
  "The Held Earth — Signature Ground Control (Signature Edition) - Advanced",
  "The Unmanned Shift — Signature Automation (Signature Edition) - Advanced",
  "The Night-and-Day Mill — Signature Plant Operations (Signature Edition) - Advanced",
  "The Kept Footprint — Signature Environment (Signature Edition) - Advanced",
  "The Healed Land — Signature Closure (Signature Edition) - Advanced",
  "The Measurers — Signature Surveying (Signature Edition) - Advanced",
  "The Counted Metal — Signature Metallurgical Accounting (Signature Edition) - Advanced",
  "The Delver's Review — Signature Mastery (Signature Edition) - Advanced",
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mining-extractive-industries-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
