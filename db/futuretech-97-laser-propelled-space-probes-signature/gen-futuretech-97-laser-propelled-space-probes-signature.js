(function(){'use strict';
/* JAH The Laser-Propelled Space Probes Future Technology Database — Signature Edition generator — jahdb-futuretech-97-laser-propelled-space-probes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT97-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Laser Propelled Space Probes — Kepler's Push (Signature Edition)", "Laser Propelled Space Probes — Maxwell Predicts (Signature Edition)", "Laser Propelled Space Probes — Pressure Measured (Signature Edition)", "Laser Propelled Space Probes — the Light Ship (Signature Edition)", "Laser Propelled Space Probes — Photon Drive (Signature Edition)", "Laser Propelled Space Probes — the Laser - Light Becomes a Tool (Signature Edition)", "Laser Propelled Space Probes — Forward's Sails (Signature Edition)", "Laser Propelled Space Probes — Sail Missions (Signature Edition)", "Laser Propelled Space Probes — Znamya (Signature Edition)", "Laser Propelled Space Probes — Cosmos 1 (Signature Edition)", "Laser Propelled Space Probes — IKAROS (Signature Edition)"], "Compounded": ["Laser Propelled Space Probes — NanoSail-D (Signature Edition)", "Laser Propelled Space Probes — LightSail (Signature Edition)", "Laser Propelled Space Probes — Starshot - the Laser Push (Signature Edition)", "Laser Propelled Space Probes — LightSail 2 (Signature Edition)", "Laser Propelled Space Probes — ACS3 (Signature Edition)", "Laser Propelled Space Probes — Sails Mature (Signature Edition)", "Laser Propelled Space Probes — Beamed Science (Signature Edition)", "Laser Propelled Space Probes — Pushed Light (Signature Edition)", "Laser Propelled Space Probes — the Sailing Fleet (Signature Edition)", "Laser Propelled Space Probes — Laser Sail Tests (Signature Edition)", "Laser Propelled Space Probes — The Laser Sail (Signature Edition)", "Laser Propelled Space Probes — The Beamer (Signature Edition)"], "Advanced": ["Laser Propelled Space Probes — 0.2c Probes (Signature Edition)", "Laser Propelled Space Probes — The 100 GW Array (Signature Edition)", "Laser Propelled Space Probes — The Light Fleet (Signature Edition)", "Laser Propelled Space Probes — The Sail Network (Signature Edition)", "Laser Propelled Space Probes — The Interstellar Sail (Signature Edition)", "Laser Propelled Space Probes — The Photon Highway (Signature Edition)", "Laser Propelled Space Probes — The Light-Speed Probe (Signature Edition)", "Laser Propelled Space Probes — The Sail Economy (Signature Edition)", "Laser Propelled Space Probes — The Pushed Light (Signature Edition)", "Laser Propelled Space Probes — The Stellar Commute (Signature Edition)", "Laser Propelled Space Probes — Everyday Laser Sails - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Laser Propelled Space Probes study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-97-laser-propelled-space-probes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-97-laser-propelled-space-probes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
