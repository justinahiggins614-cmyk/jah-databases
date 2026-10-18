(function(){'use strict';
/* JAH The Weather Modification Technologies Future Technology Database generator — jahdb-futuretech-77-weather-modification-technologies-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT77-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1891: the Rainmakers - Foundations",
  "1946: First Cloud Seeding - Foundations",
  "1947: Project Cirrus - Foundations",
  "1950s: Rain for Hire - Foundations",
  "1962: Project Stormfury - Foundations",
  "1970s: Rockets vs Hail - Foundations",
  "1977: Weather Weapons Banned - Foundations",
  "1980s: China's Weather Office - Foundations",
  "1990s: the Industry Organizes - Foundations",
  "2008: Clear Skies for the Games - Foundations",
  "2010s: the King's Rain - Foundations"
 ],
 "Compounded": [
  "2015: the UAE's Rain - Compounded",
  "2017: Half of China Covered - Compounded",
  "2021: Drones Make Rain - Compounded",
  "2022: Routine Weather Work - Compounded",
  "2023: the Rain Business - Compounded",
  "2024: Dubai's Deluge Debate - Compounded",
  "2024: Seeding the Snowpack - Compounded",
  "2025: the Professional Rain - Compounded",
  "2025: Science Returns - Compounded",
  "2025: Taming Hurricanes Again - Compounded",
  "2025: Who Made the Rain? - Compounded",
  "Rain on Schedule - Compounded"
 ],
 "Advanced": [
  "Steering Hurricanes - Advanced",
  "Drought on Demand Ended - Advanced",
  "Global Hail Suppression - Advanced",
  "Fog-Free Airports - Advanced",
  "Managed Snowpack - Advanced",
  "The Weather Utility - Advanced",
  "Climate-Weather Integration - Advanced",
  "The Tamed Storm - Advanced",
  "The Managed Sky - Advanced",
  "Weather Governance - Advanced",
  "Everyday Weather Control - Working Version - Advanced"
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
    name:topic+' — weather modification record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A weather modification record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-77-weather-modification-technologies-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-77-weather-modification-technologies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-77-weather-modification-technologies',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
