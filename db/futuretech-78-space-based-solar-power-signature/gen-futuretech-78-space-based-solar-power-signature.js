(function(){'use strict';
/* JAH The Space-Based Solar Power Future Technology Database — Signature Edition generator — jahdb-futuretech-78-space-based-solar-power-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT78-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Space Based Solar Power — Asimov Imagines It (Signature Edition)", "Space Based Solar Power — Glaser's Concept (Signature Edition)", "Space Based Solar Power — the Reference System (Signature Edition)", "Space Based Solar Power — Japan's SPS (Signature Edition)", "Space Based Solar Power — Fresh Look (Signature Edition)", "Space Based Solar Power — the Pentagon's Study (Signature Edition)", "Space Based Solar Power — a Utility Buys Space Power (Signature Edition)", "Space Based Solar Power — JAXA Beams Power (Signature Edition)", "Space Based Solar Power — China's Orbital Plan (Signature Edition)", "Space Based Solar Power — 2030s Test Target (Signature Edition)", "Space Based Solar Power — SSPIDR (Signature Edition)"], "Compounded": ["Space Based Solar Power — PRAM in Orbit (Signature Edition)", "Space Based Solar Power — Caltech's $100M Bet (Signature Edition)", "Space Based Solar Power — MAPLE Beams in Space (Signature Edition)", "Space Based Solar Power — ESA's Solaris (Signature Edition)", "Space Based Solar Power — Space Solar Momentum (Signature Edition)", "Space Based Solar Power — China's Test Site (Signature Edition)", "Space Based Solar Power — Demos Multiply (Signature Edition)", "Space Based Solar Power — Britain's Design (Signature Edition)", "Space Based Solar Power — Japan's Orbital Demo (Signature Edition)", "Space Based Solar Power — Orbital Power Pilots (Signature Edition)", "Space Based Solar Power — The Orbital Demo Plant (Signature Edition)", "Space Based Solar Power — Gigawatts from Orbit (Signature Edition)"], "Advanced": ["Space Based Solar Power — Beaming to Rectennas (Signature Edition)", "Space Based Solar Power — Power for the Moon (Signature Edition)", "Space Based Solar Power — The Orbital Harvest (Signature Edition)", "Space Based Solar Power — 24/7 Solar (Signature Edition)", "Space Based Solar Power — The Orbital Utility (Signature Edition)", "Space Based Solar Power — Power from Orbit (Signature Edition)", "Space Based Solar Power — The Space Grid (Signature Edition)", "Space Based Solar Power — The Beamed Civilization (Signature Edition)", "Space Based Solar Power — Cheap Launch Enables SBSP (Signature Edition)", "Space Based Solar Power — Orbital Assembly (Signature Edition)", "Space Based Solar Power — Everyday Orbital Power - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Space Based Solar Power study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-78-space-based-solar-power-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-78-space-based-solar-power-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
