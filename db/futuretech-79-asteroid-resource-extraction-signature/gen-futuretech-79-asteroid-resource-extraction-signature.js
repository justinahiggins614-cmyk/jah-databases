(function(){'use strict';
/* JAH The Asteroid Resource Extraction Future Technology Database — Signature Edition generator — jahdb-futuretech-79-asteroid-resource-extraction-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT79-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Asteroid Resource Extraction — Ceres Found (Signature Edition)", "Asteroid Resource Extraction — Eros - the Neighbor (Signature Edition)", "Asteroid Resource Extraction — the High Frontier (Signature Edition)", "Asteroid Resource Extraction — Mapping the Belt (Signature Edition)", "Asteroid Resource Extraction — Landing on Eros (Signature Edition)", "Asteroid Resource Extraction — Hayabusa Launches (Signature Edition)", "Asteroid Resource Extraction — Itokawa (Signature Edition)", "Asteroid Resource Extraction — First Sample Returns (Signature Edition)", "Asteroid Resource Extraction — the Asteroid Miners (Signature Edition)", "Asteroid Resource Extraction — Deep Space Industries (Signature Edition)", "Asteroid Resource Extraction — Hayabusa2 Launches (Signature Edition)"], "Compounded": ["Asteroid Resource Extraction — Miners Get Rights (Signature Edition)", "Asteroid Resource Extraction — OSIRIS-REx Launches (Signature Edition)", "Asteroid Resource Extraction — Ryugu (Signature Edition)", "Asteroid Resource Extraction — the First Rush Ends (Signature Edition)", "Asteroid Resource Extraction — Sampling Bennu (Signature Edition)", "Asteroid Resource Extraction — Ryugu Returns (Signature Edition)", "Asteroid Resource Extraction — DART Moves an Asteroid (Signature Edition)", "Asteroid Resource Extraction — Bennu Returns (Signature Edition)", "Asteroid Resource Extraction — Psyche Launches (Signature Edition)", "Asteroid Resource Extraction — AstroForge (Signature Edition)", "Asteroid Resource Extraction — TransAstra (Signature Edition)", "Asteroid Resource Extraction — Prospectors Multiply (Signature Edition)"], "Advanced": ["Asteroid Resource Extraction — Prospecting Grows (Signature Edition)", "Asteroid Resource Extraction — The First Asteroid Mined (Signature Edition)", "Asteroid Resource Extraction — Water from Asteroids (Signature Edition)", "Asteroid Resource Extraction — Platinum Asteroids (Signature Edition)", "Asteroid Resource Extraction — Orbital Refineries (Signature Edition)", "Asteroid Resource Extraction — The Trillion-Dollar Rock (Signature Edition)", "Asteroid Resource Extraction — The Space Resource Economy (Signature Edition)", "Asteroid Resource Extraction — Asteroid Redirection (Signature Edition)", "Asteroid Resource Extraction — The Belt Economy (Signature Edition)", "Asteroid Resource Extraction — Self-Sustaining Space Industry (Signature Edition)", "Asteroid Resource Extraction — Everyday Asteroid Resources - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Asteroid Resource Extraction study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-79-asteroid-resource-extraction-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-79-asteroid-resource-extraction-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
