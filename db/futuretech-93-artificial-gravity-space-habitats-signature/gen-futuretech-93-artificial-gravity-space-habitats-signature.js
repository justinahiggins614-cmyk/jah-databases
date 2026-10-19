(function(){'use strict';
/* JAH The Artificial-Gravity Space Habitats Future Technology Database — Signature Edition generator — jahdb-futuretech-93-artificial-gravity-space-habitats-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT93-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Artificial Gravity Space Habitats — the Wheel Imagined (Signature Edition)", "Artificial Gravity Space Habitats — Noordung's Wheel (Signature Edition)", "Artificial Gravity Space Habitats — Von Braun's Wheel (Signature Edition)", "Artificial Gravity Space Habitats — 2001's Wheel (Signature Edition)", "Artificial Gravity Space Habitats — Skylab (Signature Edition)", "Artificial Gravity Space Habitats — Mir (Signature Edition)", "Artificial Gravity Space Habitats — the ISS (Signature Edition)", "Artificial Gravity Space Habitats — Spin Studies (Signature Edition)", "Artificial Gravity Space Habitats — Nautilus-X (Signature Edition)", "Artificial Gravity Space Habitats — BEAM (Signature Edition)", "Artificial Gravity Space Habitats — the Gateway (Signature Edition)"], "Compounded": ["Artificial Gravity Space Habitats — Orbital Reef (Signature Edition)", "Artificial Gravity Space Habitats — Starlab (Signature Edition)", "Artificial Gravity Space Habitats — Haven-1 (Signature Edition)", "Artificial Gravity Space Habitats — Axiom (Signature Edition)", "Artificial Gravity Space Habitats — Gravitics (Signature Edition)", "Artificial Gravity Space Habitats — Private Orbit (Signature Edition)", "Artificial Gravity Space Habitats — Spin Science (Signature Edition)", "Artificial Gravity Space Habitats — The Rotating Station (Signature Edition)", "Artificial Gravity Space Habitats — The Gravity Wheel (Signature Edition)", "Artificial Gravity Space Habitats — The Stanford Torus (Signature Edition)", "Artificial Gravity Space Habitats — The O'Neill Cylinder (Signature Edition)", "Artificial Gravity Space Habitats — The Gravity Deck (Signature Edition)"], "Advanced": ["Artificial Gravity Space Habitats — The Rotating City (Signature Edition)", "Artificial Gravity Space Habitats — The Gravity Hospital (Signature Edition)", "Artificial Gravity Space Habitats — The Space Suburb (Signature Edition)", "Artificial Gravity Space Habitats — The Rotating Nation (Signature Edition)", "Artificial Gravity Space Habitats — The Gravity Civilization (Signature Edition)", "Artificial Gravity Space Habitats — The Spun World (Signature Edition)", "Artificial Gravity Space Habitats — The Comfortable Orbit (Signature Edition)", "Artificial Gravity Space Habitats — The Gravity Economy (Signature Edition)", "Artificial Gravity Space Habitats — The Orbital Home (Signature Edition)", "Artificial Gravity Space Habitats — The 1G Station (Signature Edition)", "Artificial Gravity Space Habitats — Everyday Artificial Gravity - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Artificial Gravity Space Habitats study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-93-artificial-gravity-space-habitats-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-93-artificial-gravity-space-habitats-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
