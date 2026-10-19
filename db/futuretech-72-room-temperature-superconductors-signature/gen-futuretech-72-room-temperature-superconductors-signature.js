(function(){'use strict';
/* JAH The Room-Temperature Superconductors Future Technology Database — Signature Edition generator — jahdb-futuretech-72-room-temperature-superconductors-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT72-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Room Temperature Superconductors — Onnes Finds Zero Resistance (Signature Edition)", "Room Temperature Superconductors — the Meissner Effect (Signature Edition)", "Room Temperature Superconductors — BCS Theory (Signature Edition)", "Room Temperature Superconductors — the Josephson Junction (Signature Edition)", "Room Temperature Superconductors — 23 Kelvin - the Bar (Signature Edition)", "Room Temperature Superconductors — Cuprates - the Ceramic Shock (Signature Edition)", "Room Temperature Superconductors — YBCO - Above Liquid Nitrogen (Signature Edition)", "Room Temperature Superconductors — 110 Kelvin (Signature Edition)", "Room Temperature Superconductors — 138K - the Standing Record (Signature Edition)", "Room Temperature Superconductors — MgB2 - the Simple Surprise (Signature Edition)", "Room Temperature Superconductors — Iron Pnictides (Signature Edition)"], "Compounded": ["Room Temperature Superconductors — 203K Under Pressure (Signature Edition)", "Room Temperature Superconductors — 250K - So Close (Signature Edition)", "Room Temperature Superconductors — Nickelates (Signature Edition)", "Room Temperature Superconductors — the Claim and the Retraction (Signature Edition)", "Room Temperature Superconductors — LK-99 Summer (Signature Edition)", "Room Temperature Superconductors — the Second Retraction (Signature Edition)", "Room Temperature Superconductors — Careful Hydrides (Signature Edition)", "Room Temperature Superconductors — Ambient Superconductor Hunts (Signature Edition)", "Room Temperature Superconductors — Verified Room-Temperature Superconductivity (Signature Edition)", "Room Temperature Superconductors — Ambient-Pressure Room-Temp (Signature Edition)", "Room Temperature Superconductors — Superconducting Wire (Signature Edition)", "Room Temperature Superconductors — The Lossless Grid (Signature Edition)"], "Advanced": ["Room Temperature Superconductors — Cheap MRI Everywhere (Signature Edition)", "Room Temperature Superconductors — Maglev Everywhere (Signature Edition)", "Room Temperature Superconductors — Fusion's Cheap Magnets (Signature Edition)", "Room Temperature Superconductors — Superconducting Electronics (Signature Edition)", "Room Temperature Superconductors — Superconducting Motors (Signature Edition)", "Room Temperature Superconductors — Maglev Cars (Signature Edition)", "Room Temperature Superconductors — Quantum at Scale (Signature Edition)", "Room Temperature Superconductors — Room-Temp Quantum Chips (Signature Edition)", "Room Temperature Superconductors — Superconductors at Home (Signature Edition)", "Room Temperature Superconductors — The Lossless Civilization (Signature Edition)", "Room Temperature Superconductors — Everyday Superconductors - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Room Temperature Superconductors study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-72-room-temperature-superconductors-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-72-room-temperature-superconductors-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
