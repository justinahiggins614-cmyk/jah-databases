(function(){'use strict';
/* JAH The Artificial Habitats for Extreme Environments Future Technology Database generator — jahdb-futuretech-98-artificial-habitats-for-extreme-environments-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT98-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1843: the Sealed Diver - Foundations",
  "1930: the Bathysphere - Foundations",
  "1962: Conshelf - Foundations",
  "1964: Sealab - Foundations",
  "1969: Tektite - Foundations",
  "1986: Aquarius - Foundations",
  "1980s: Ice Stations - Foundations",
  "1991: Biosphere 2 - Foundations",
  "2005: Concordia - Foundations",
  "2013: HI-SEAS - Foundations",
  "2015: Mars Analogs - Foundations"
 ],
 "Compounded": [
  "2017: Analog Growth - Compounded",
  "2019: Abyssal Homes - Compounded",
  "2021: Ocean Labs - Compounded",
  "2023: Proteus - Compounded",
  "2024: Hostile Science - Compounded",
  "2025: Anywhere Homes - Compounded",
  "2025: Extreme Real Estate - Compounded",
  "The Sealed Habitat - Compounded",
  "The Undersea City - Compounded",
  "The Antarctic Metropolis - Compounded",
  "The Desert Arcology - Compounded",
  "The Deep-Sea Colony - Compounded"
 ],
 "Advanced": [
  "The Volcanic Habitat - Advanced",
  "The Radiation-Proof City - Advanced",
  "The Self-Sufficient Dome - Advanced",
  "The Extreme Suburb - Advanced",
  "The Hostile Frontier - Advanced",
  "The Anywhere Habitat - Advanced",
  "The Climate-Proof City - Advanced",
  "The Deep-Earth Colony - Advanced",
  "The Sealed World - Advanced",
  "The Extreme Civilization - Advanced",
  "Everyday Extreme Habitats - Working Version - Advanced"
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
    name:topic+' — extreme habitat record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A extreme habitat record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-98-artificial-habitats-for-extreme-environments-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-98-artificial-habitats-for-extreme-environments-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-98-artificial-habitats-for-extreme-environments',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
