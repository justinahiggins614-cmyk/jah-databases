(function(){'use strict';
/* JAH The Fusion-Powered Spacecraft Future Technology Database generator — jahdb-futuretech-96-fusion-powered-spacecraft-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT96-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1903: the Rocket Equation - Fusion's Math - Foundations",
  "1923: Die Rakete - Foundations",
  "1940s: Atomic Spaceships - Foundations",
  "1958: Project Orion - the Fusion Bomb Ship - Foundations",
  "1960s: the Star Drive - Foundations",
  "1961: NERVA - Foundations",
  "1970s: NERVA Fires - Foundations",
  "1973: Daedalus - the Fusion Starship Study - Foundations",
  "1980s: Antimatter Drives - Foundations",
  "1998: VASIMR - Foundations",
  "2000s: Fusion Drive Research - Foundations"
 ],
 "Compounded": [
  "2009: VX-200 - Compounded",
  "2010s: Nuclear Returns - Compounded",
  "2015: VASIMR at Power - Compounded",
  "2017: Direct Fusion Drive - Compounded",
  "2020: Drive Startups - Compounded",
  "2023: Helicity Space - Compounded",
  "2024: Drive Advances - Compounded",
  "2023: DRACO - Compounded",
  "2025: Fast Space - Compounded",
  "The Fusion Rocket - Compounded",
  "Mars in Weeks - Compounded",
  "The Torchship - Compounded"
 ],
 "Advanced": [
  "The 1G Torchship - Advanced",
  "The Fusion Starship - Advanced",
  "Interstellar Fusion - Advanced",
  "The Fusion Fleet - Advanced",
  "The Outer Solar System - Advanced",
  "The Fusion Economy - Advanced",
  "The Starship Era - Advanced",
  "The Fusion Civilization - Advanced",
  "The Fast Solar System - Advanced",
  "The Fusion Highway - Advanced",
  "Everyday Fusion Flight - Working Version - Advanced"
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
    name:topic+' — fusion spacecraft record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fusion spacecraft record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-96-fusion-powered-spacecraft-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-96-fusion-powered-spacecraft-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-96-fusion-powered-spacecraft',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
