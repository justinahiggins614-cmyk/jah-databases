(function(){'use strict';
/* JAH The Laser-Propelled Space Probes Future Technology Database generator — jahdb-futuretech-97-laser-propelled-space-probes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT97-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1619: Kepler's Push - Foundations",
  "1873: Maxwell Predicts - Foundations",
  "1901: Pressure Measured - Foundations",
  "1924: the Light Ship - Foundations",
  "1950s: Photon Drive - Foundations",
  "1960: the Laser - Light Becomes a Tool - Foundations",
  "1970s: Forward's Sails - Foundations",
  "1980s: Sail Missions - Foundations",
  "1993: Znamya - Foundations",
  "2005: Cosmos 1 - Foundations",
  "2010: IKAROS - Foundations"
 ],
 "Compounded": [
  "2010: NanoSail-D - Compounded",
  "2015: LightSail - Compounded",
  "2016: Starshot - the Laser Push - Compounded",
  "2019: LightSail 2 - Compounded",
  "2022: ACS3 - Compounded",
  "2023: Sails Mature - Compounded",
  "2024: Beamed Science - Compounded",
  "2025: Pushed Light - Compounded",
  "2025: the Sailing Fleet - Compounded",
  "2025: Laser Sail Tests - Compounded",
  "The Laser Sail - Compounded",
  "The Beamer - Compounded"
 ],
 "Advanced": [
  "0.2c Probes - Advanced",
  "The 100 GW Array - Advanced",
  "The Light Fleet - Advanced",
  "The Sail Network - Advanced",
  "The Interstellar Sail - Advanced",
  "The Photon Highway - Advanced",
  "The Light-Speed Probe - Advanced",
  "The Sail Economy - Advanced",
  "The Pushed Light - Advanced",
  "The Stellar Commute - Advanced",
  "Everyday Laser Sails - Working Version - Advanced"
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
    name:topic+' — laser-propelled probe record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A laser-propelled probe record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-97-laser-propelled-space-probes-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-97-laser-propelled-space-probes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-97-laser-propelled-space-probes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
