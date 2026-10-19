(function(){'use strict';
/* JAH The Mars Colonization Technology Future Technology Database — Signature Edition generator — jahdb-futuretech-92-mars-colonization-technology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT92-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Mars Colonization Technology — the Canals of Mars (Signature Edition)", "Mars Colonization Technology — Lowell's Mars (Signature Edition)", "Mars Colonization Technology — Das Marsprojekt (Signature Edition)", "Mars Colonization Technology — Mariner 4 (Signature Edition)", "Mars Colonization Technology — Mars 3 (Signature Edition)", "Mars Colonization Technology — Viking (Signature Edition)", "Mars Colonization Technology — Mars Direct (Signature Edition)", "Mars Colonization Technology — the Mars Society (Signature Edition)", "Mars Colonization Technology — Pathfinder (Signature Edition)", "Mars Colonization Technology — the Rover Twins (Signature Edition)", "Mars Colonization Technology — Curiosity (Signature Edition)"], "Compounded": ["Mars Colonization Technology — The Martian (Signature Edition)", "Mars Colonization Technology — the Mars Rocket (Signature Edition)", "Mars Colonization Technology — InSight (Signature Edition)", "Mars Colonization Technology — Mars 2020 (Signature Edition)", "Mars Colonization Technology — Perseverance (Signature Edition)", "Mars Colonization Technology — Ingenuity Flies (Signature Edition)", "Mars Colonization Technology — Tianwen-1 (Signature Edition)", "Mars Colonization Technology — Starship Tests (Signature Edition)", "Mars Colonization Technology — Mars Timelines (Signature Edition)", "Mars Colonization Technology — The Mars Base (Signature Edition)", "Mars Colonization Technology — The Mars Village (Signature Edition)", "Mars Colonization Technology — The Mars Town in Colonization Technology (Signature Edition)"], "Advanced": ["Mars Colonization Technology — Martian Industry (Signature Edition)", "Mars Colonization Technology — The Mars City (Signature Edition)", "Mars Colonization Technology — Terraforming Begins (Signature Edition)", "Mars Colonization Technology — The Martian Economy (Signature Edition)", "Mars Colonization Technology — The Mars-Born (Signature Edition)", "Mars Colonization Technology — The Martian Civilization (Signature Edition)", "Mars Colonization Technology — The Interplanetary Species (Signature Edition)", "Mars Colonization Technology — The Mars Republic (Signature Edition)", "Mars Colonization Technology — The Green Mars (Signature Edition)", "Mars Colonization Technology — The Settled Mars (Signature Edition)", "Mars Colonization Technology — Everyday Martian Life - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mars Colonization Technology study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-92-mars-colonization-technology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-92-mars-colonization-technology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
