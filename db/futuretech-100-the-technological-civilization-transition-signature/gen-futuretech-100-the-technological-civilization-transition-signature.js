(function(){'use strict';
/* JAH The Technological Civilization Transition Future Technology Database — Signature Edition generator — jahdb-futuretech-100-the-technological-civilization-transition-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT100-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Technological Civilization Transition — Steam Power (Signature Edition)", "The Technological Civilization Transition — the Steam Age (Signature Edition)", "The Technological Civilization Transition — Electric Light (Signature Edition)", "The Technological Civilization Transition — Mass Production (Signature Edition)", "The Technological Civilization Transition — the Atomic Age (Signature Edition)", "The Technological Civilization Transition — Sputnik (Signature Edition)", "The Technological Civilization Transition — the Moon (Signature Edition)", "The Technological Civilization Transition — the Microprocessor (Signature Edition)", "The Technological Civilization Transition — the PC (Signature Edition)", "The Technological Civilization Transition — the Web (Signature Edition)", "The Technological Civilization Transition — the Smartphone (Signature Edition)"], "Compounded": ["The Technological Civilization Transition — the Cloud (Signature Edition)", "The Technological Civilization Transition — the AI Age (Signature Edition)", "The Technological Civilization Transition — AI Transforms (Signature Edition)", "The Technological Civilization Transition — The Transition Begins (Signature Edition)", "The Technological Civilization Transition — Kardashev I (Signature Edition)", "The Technological Civilization Transition — The Planetary Civilization (Signature Edition)", "The Technological Civilization Transition — The Post-Scarcity Transition (Signature Edition)", "The Technological Civilization Transition — The Merged Humanity (Signature Edition)", "The Technological Civilization Transition — The Interplanetary Civilization (Signature Edition)", "The Technological Civilization Transition — Kardashev II (Signature Edition)", "The Technological Civilization Transition — The Stellar Civilization (Signature Edition)", "The Technological Civilization Transition — The Post-Biological (Signature Edition)"], "Advanced": ["The Technological Civilization Transition — The Galactic Civilization (Signature Edition)", "The Technological Civilization Transition — Kardashev III (Signature Edition)", "The Technological Civilization Transition — The Universal Civilization (Signature Edition)", "The Technological Civilization Transition — The Omega Transition (Signature Edition)", "The Technological Civilization Transition — The Transcendent Humanity (Signature Edition)", "The Technological Civilization Transition — The Eternal Civilization (Signature Edition)", "The Technological Civilization Transition — The Cosmic Mind (Signature Edition)", "The Technological Civilization Transition — The Type IV Question (Signature Edition)", "The Technological Civilization Transition — The Completed Transition (Signature Edition)", "The Technological Civilization Transition — The New Beginning (Signature Edition)", "The Technological Civilization Transition — Everyday Transcendence - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Technological Civilization Transition study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-100-the-technological-civilization-transition-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-100-the-technological-civilization-transition-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
