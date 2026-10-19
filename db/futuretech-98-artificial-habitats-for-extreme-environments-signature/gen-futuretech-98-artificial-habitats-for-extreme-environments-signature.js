(function(){'use strict';
/* JAH The Artificial Habitats for Extreme Environments Future Technology Database — Signature Edition generator — jahdb-futuretech-98-artificial-habitats-for-extreme-environments-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT98-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Artificial Habitats For Extreme Environments — the Sealed Diver (Signature Edition)", "Artificial Habitats For Extreme Environments — the Bathysphere (Signature Edition)", "Artificial Habitats For Extreme Environments — Conshelf (Signature Edition)", "Artificial Habitats For Extreme Environments — Sealab (Signature Edition)", "Artificial Habitats For Extreme Environments — Tektite (Signature Edition)", "Artificial Habitats For Extreme Environments — Aquarius (Signature Edition)", "Artificial Habitats For Extreme Environments — Ice Stations (Signature Edition)", "Artificial Habitats For Extreme Environments — Biosphere 2 (Signature Edition)", "Artificial Habitats For Extreme Environments — Concordia (Signature Edition)", "Artificial Habitats For Extreme Environments — HI-SEAS (Signature Edition)", "Artificial Habitats For Extreme Environments — Mars Analogs (Signature Edition)"], "Compounded": ["Artificial Habitats For Extreme Environments — Analog Growth (Signature Edition)", "Artificial Habitats For Extreme Environments — Abyssal Homes (Signature Edition)", "Artificial Habitats For Extreme Environments — Ocean Labs (Signature Edition)", "Artificial Habitats For Extreme Environments — Proteus (Signature Edition)", "Artificial Habitats For Extreme Environments — Hostile Science (Signature Edition)", "Artificial Habitats For Extreme Environments — Anywhere Homes (Signature Edition)", "Artificial Habitats For Extreme Environments — Extreme Real Estate (Signature Edition)", "Artificial Habitats For Extreme Environments — The Sealed Habitat (Signature Edition)", "Artificial Habitats For Extreme Environments — The Undersea City (Signature Edition)", "Artificial Habitats For Extreme Environments — The Antarctic Metropolis (Signature Edition)", "Artificial Habitats For Extreme Environments — The Desert Arcology (Signature Edition)", "Artificial Habitats For Extreme Environments — The Deep-Sea Colony (Signature Edition)"], "Advanced": ["Artificial Habitats For Extreme Environments — The Volcanic Habitat (Signature Edition)", "Artificial Habitats For Extreme Environments — The Radiation-Proof City (Signature Edition)", "Artificial Habitats For Extreme Environments — The Self-Sufficient Dome (Signature Edition)", "Artificial Habitats For Extreme Environments — The Extreme Suburb (Signature Edition)", "Artificial Habitats For Extreme Environments — The Hostile Frontier (Signature Edition)", "Artificial Habitats For Extreme Environments — The Anywhere Habitat (Signature Edition)", "Artificial Habitats For Extreme Environments — The Climate-Proof City (Signature Edition)", "Artificial Habitats For Extreme Environments — The Deep-Earth Colony (Signature Edition)", "Artificial Habitats For Extreme Environments — The Sealed World (Signature Edition)", "Artificial Habitats For Extreme Environments — The Extreme Civilization (Signature Edition)", "Artificial Habitats For Extreme Environments — Everyday Extreme Habitats - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Artificial Habitats For Extreme Environments study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-98-artificial-habitats-for-extreme-environments-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-98-artificial-habitats-for-extreme-environments-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
