(function(){'use strict';
/* JAH The Interstellar Probe Technology Future Technology Database — Signature Edition generator — jahdb-futuretech-95-interstellar-probe-technology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT95-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Interstellar Probe Technology — Galileo Sees Stars (Signature Edition)", "Interstellar Probe Technology — How Far the Stars (Signature Edition)", "Interstellar Probe Technology — the Speed Limit (Signature Edition)", "Interstellar Probe Technology — Goddard's Rockets (Signature Edition)", "Interstellar Probe Technology — Project Orion (Signature Edition)", "Interstellar Probe Technology — the Bussard Ramjet (Signature Edition)", "Interstellar Probe Technology — Daedalus (Signature Edition)", "Interstellar Probe Technology — Voyager (Signature Edition)", "Interstellar Probe Technology — Antimatter (Signature Edition)", "Interstellar Probe Technology — Forward's Sails (Signature Edition)", "Interstellar Probe Technology — New Horizons (Signature Edition)"], "Compounded": ["Interstellar Probe Technology — Interstellar (Signature Edition)", "Interstellar Probe Technology — Pluto (Signature Edition)", "Interstellar Probe Technology — Starshot (Signature Edition)", "Interstellar Probe Technology — Oumuamua (Signature Edition)", "Interstellar Probe Technology — Voyager 2 (Signature Edition)", "Interstellar Probe Technology — Starshot Progress (Signature Edition)", "Interstellar Probe Technology — the 1000 AU Probe (Signature Edition)", "Interstellar Probe Technology — Concepts Advance (Signature Edition)", "Interstellar Probe Technology — Star Science (Signature Edition)", "Interstellar Probe Technology — The Interstellar Probe Mission (Signature Edition)", "Interstellar Probe Technology — Starshot Flies (Signature Edition)", "Interstellar Probe Technology — The Gram Starship (Signature Edition)"], "Advanced": ["Interstellar Probe Technology — The Laser Array (Signature Edition)", "Interstellar Probe Technology — Proxima in 20 Years (Signature Edition)", "Interstellar Probe Technology — The Interstellar Fleet (Signature Edition)", "Interstellar Probe Technology — The Starship (Signature Edition)", "Interstellar Probe Technology — The Generation Ship in Interstellar Probe Technology (Signature Edition)", "Interstellar Probe Technology — The Sleeper Ship (Signature Edition)", "Interstellar Probe Technology — The Warp Question (Signature Edition)", "Interstellar Probe Technology — The First Exoplanet Visit (Signature Edition)", "Interstellar Probe Technology — The Interstellar Civilization (Signature Edition)", "Interstellar Probe Technology — The Stars Reached (Signature Edition)", "Interstellar Probe Technology — Everyday Interstellar - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Interstellar Probe Technology study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-95-interstellar-probe-technology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-95-interstellar-probe-technology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
