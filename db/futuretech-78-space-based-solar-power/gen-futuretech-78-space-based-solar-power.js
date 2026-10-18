(function(){'use strict';
/* JAH The Space-Based Solar Power Future Technology Database generator — jahdb-futuretech-78-space-based-solar-power-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT78-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1941: Asimov Imagines It - Foundations",
  "1968: Glaser's Concept - Foundations",
  "1979: the Reference System - Foundations",
  "1980s: Japan's SPS - Foundations",
  "1995: Fresh Look - Foundations",
  "2007: the Pentagon's Study - Foundations",
  "2009: a Utility Buys Space Power - Foundations",
  "2010s: JAXA Beams Power - Foundations",
  "2015: China's Orbital Plan - Foundations",
  "2018: 2030s Test Target - Foundations",
  "2019: SSPIDR - Foundations"
 ],
 "Compounded": [
  "2020: PRAM in Orbit - Compounded",
  "2021: Caltech's $100M Bet - Compounded",
  "2023: MAPLE Beams in Space - Compounded",
  "2022: ESA's Solaris - Compounded",
  "2023: Space Solar Momentum - Compounded",
  "2024: China's Test Site - Compounded",
  "2025: Demos Multiply - Compounded",
  "2025: Britain's Design - Compounded",
  "2025: Japan's Orbital Demo - Compounded",
  "2025: Orbital Power Pilots - Compounded",
  "The Orbital Demo Plant - Compounded",
  "Gigawatts from Orbit - Compounded"
 ],
 "Advanced": [
  "Beaming to Rectennas - Advanced",
  "Power for the Moon - Advanced",
  "The Orbital Harvest - Advanced",
  "24/7 Solar - Advanced",
  "The Orbital Utility - Advanced",
  "Power from Orbit - Advanced",
  "The Space Grid - Advanced",
  "The Beamed Civilization - Advanced",
  "Cheap Launch Enables SBSP - Advanced",
  "Orbital Assembly - Advanced",
  "Everyday Orbital Power - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — space-based solar power record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A space-based solar power record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-78-space-based-solar-power-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-78-space-based-solar-power-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-78-space-based-solar-power',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
