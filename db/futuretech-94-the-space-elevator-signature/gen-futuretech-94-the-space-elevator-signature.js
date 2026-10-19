(function(){'use strict';
/* JAH The Space Elevator Future Technology Database — Signature Edition generator — jahdb-futuretech-94-the-space-elevator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT94-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Space Elevator — the Celestial Castle (Signature Edition)", "The Space Elevator — Artsutanov's Elevator (Signature Edition)", "The Space Elevator — Isaacs Analyzes (Signature Edition)", "The Space Elevator — Pearson Revives (Signature Edition)", "The Space Elevator — Fountains of Paradise (Signature Edition)", "The Space Elevator — Nanotubes (Signature Edition)", "The Space Elevator — the NIAC Study (Signature Edition)", "The Space Elevator — LiftPort (Signature Edition)", "The Space Elevator — the Elevator Games (Signature Edition)", "The Space Elevator — ISEC (Signature Edition)", "The Space Elevator — Obayashi's 2050 (Signature Edition)"], "Compounded": ["The Space Elevator — Stronger Fibers (Signature Edition)", "The Space Elevator — STARS-Me (Signature Edition)", "The Space Elevator — Obayashi Advances (Signature Edition)", "The Space Elevator — Skyhooks (Signature Edition)", "The Space Elevator — Tether Research (Signature Edition)", "The Space Elevator — the Elevator Thread (Signature Edition)", "The Space Elevator — Longer Tethers (Signature Edition)", "The Space Elevator — Concepts Advance (Signature Edition)", "The Space Elevator — Tether Demos (Signature Edition)", "The Space Elevator — The Beanstalk (Signature Edition)", "The Space Elevator — The Ribbon (Signature Edition)", "The Space Elevator — The Climber (Signature Edition)"], "Advanced": ["The Space Elevator — The Counterweight (Signature Edition)", "The Space Elevator — The Orbital Ring in Space Elevator Technology (Signature Edition)", "The Space Elevator — The Elevator Port (Signature Edition)", "The Space Elevator — Cheap Orbit (Signature Edition)", "The Space Elevator — $100/kg to Orbit (Signature Edition)", "The Space Elevator — The Space Highway (Signature Edition)", "The Space Elevator — The Tether Network (Signature Edition)", "The Space Elevator — The Beanstalk Economy (Signature Edition)", "The Space Elevator — The Elevator Civilization (Signature Edition)", "The Space Elevator — The Stairway to Orbit (Signature Edition)", "The Space Elevator — Everyday Space Elevators - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Space Elevator study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-94-the-space-elevator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-94-the-space-elevator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
