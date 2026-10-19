(function(){'use strict';
/* JAH The Fusion-Powered Spacecraft Future Technology Database — Signature Edition generator — jahdb-futuretech-96-fusion-powered-spacecraft-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT96-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Fusion Powered Spacecraft — the Rocket Equation - Fusion's Math (Signature Edition)", "Fusion Powered Spacecraft — Die Rakete (Signature Edition)", "Fusion Powered Spacecraft — Atomic Spaceships (Signature Edition)", "Fusion Powered Spacecraft — Project Orion - the Fusion Bomb Ship (Signature Edition)", "Fusion Powered Spacecraft — the Star Drive (Signature Edition)", "Fusion Powered Spacecraft — NERVA (Signature Edition)", "Fusion Powered Spacecraft — NERVA Fires (Signature Edition)", "Fusion Powered Spacecraft — Daedalus - the Fusion Starship Study (Signature Edition)", "Fusion Powered Spacecraft — Antimatter Drives (Signature Edition)", "Fusion Powered Spacecraft — VASIMR (Signature Edition)", "Fusion Powered Spacecraft — Fusion Drive Research (Signature Edition)"], "Compounded": ["Fusion Powered Spacecraft — VX-200 (Signature Edition)", "Fusion Powered Spacecraft — Nuclear Returns (Signature Edition)", "Fusion Powered Spacecraft — VASIMR at Power (Signature Edition)", "Fusion Powered Spacecraft — Direct Fusion Drive (Signature Edition)", "Fusion Powered Spacecraft — Drive Startups (Signature Edition)", "Fusion Powered Spacecraft — Helicity Space (Signature Edition)", "Fusion Powered Spacecraft — Drive Advances (Signature Edition)", "Fusion Powered Spacecraft — DRACO (Signature Edition)", "Fusion Powered Spacecraft — Fast Space (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Rocket (Signature Edition)", "Fusion Powered Spacecraft — Mars in Weeks (Signature Edition)", "Fusion Powered Spacecraft — The Torchship (Signature Edition)"], "Advanced": ["Fusion Powered Spacecraft — The 1G Torchship (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Starship (Signature Edition)", "Fusion Powered Spacecraft — Interstellar Fusion (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Fleet (Signature Edition)", "Fusion Powered Spacecraft — The Outer Solar System (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Economy (Signature Edition)", "Fusion Powered Spacecraft — The Starship Era (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Civilization (Signature Edition)", "Fusion Powered Spacecraft — The Fast Solar System (Signature Edition)", "Fusion Powered Spacecraft — The Fusion Highway (Signature Edition)", "Fusion Powered Spacecraft — Everyday Fusion Flight - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fusion Powered Spacecraft study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-96-fusion-powered-spacecraft-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-96-fusion-powered-spacecraft-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
