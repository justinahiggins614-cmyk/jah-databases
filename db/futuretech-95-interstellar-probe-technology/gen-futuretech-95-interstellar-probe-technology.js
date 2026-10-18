(function(){'use strict';
/* JAH The Interstellar Probe Technology Future Technology Database generator — jahdb-futuretech-95-interstellar-probe-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT95-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1610: Galileo Sees Stars - Foundations",
  "1838: How Far the Stars - Foundations",
  "1905: the Speed Limit - Foundations",
  "1920s: Goddard's Rockets - Foundations",
  "1958: Project Orion - Foundations",
  "1960: the Bussard Ramjet - Foundations",
  "1973: Daedalus - Foundations",
  "1977: Voyager - Foundations",
  "1980s: Antimatter - Foundations",
  "1990: Forward's Sails - Foundations",
  "2006: New Horizons - Foundations"
 ],
 "Compounded": [
  "2012: Interstellar - Compounded",
  "2015: Pluto - Compounded",
  "2016: Starshot - Compounded",
  "2017: Oumuamua - Compounded",
  "2018: Voyager 2 - Compounded",
  "2019: Starshot Progress - Compounded",
  "2020: the 1000 AU Probe - Compounded",
  "2023: Concepts Advance - Compounded",
  "2025: Star Science - Compounded",
  "The Interstellar Probe - Compounded",
  "Starshot Flies - Compounded",
  "The Gram Starship - Compounded"
 ],
 "Advanced": [
  "The Laser Array - Advanced",
  "Proxima in 20 Years - Advanced",
  "The Interstellar Fleet - Advanced",
  "The Starship - Advanced",
  "The Generation Ship - Advanced",
  "The Sleeper Ship - Advanced",
  "The Warp Question - Advanced",
  "The First Exoplanet Visit - Advanced",
  "The Interstellar Civilization - Advanced",
  "The Stars Reached - Advanced",
  "Everyday Interstellar - Working Version - Advanced"
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
    name:topic+' — interstellar probe record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A interstellar probe record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-95-interstellar-probe-technology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-95-interstellar-probe-technology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-95-interstellar-probe-technology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
