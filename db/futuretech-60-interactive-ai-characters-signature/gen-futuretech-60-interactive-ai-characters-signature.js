(function(){'use strict';
/* JAH The Interactive AI Characters Future Technology Database — Signature Edition generator — jahdb-futuretech-60-interactive-ai-characters-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT60-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Interactive AI Characters — Ancient: the Told-Again Character (Signature Edition)", "Interactive AI Characters — Sherlock Holmes - the Persistent Character (Signature Edition)", "Interactive AI Characters — D&D - You Become the Character (Signature Edition)", "Interactive AI Characters — Zork - Characters You Can Talk To (Signature Edition)", "Interactive AI Characters — MUDs - Characters Live Online (Signature Edition)", "Interactive AI Characters — Tamagotchi - the Character Needs You (Signature Edition)", "Interactive AI Characters — Creatures - Pets That Learn (Signature Edition)", "Interactive AI Characters — Black & White - the Creature You Raise (Signature Edition)", "Interactive AI Characters — Nintendogs - Pocket Companions (Signature Edition)", "Interactive AI Characters — Siri - the Phone Gets Personality (Signature Edition)", "Interactive AI Characters — Undertale - Characters Who Remember You (Signature Edition)"], "Compounded": ["Interactive AI Characters — Westworld - Drama of the Hosts (Signature Edition)", "Interactive AI Characters — Detroit - Branching Persons (Signature Edition)", "Interactive AI Characters — the Model Becomes a Cast (Signature Edition)", "Interactive AI Characters — Character.AI - Fictional Friends (Signature Edition)", "Interactive AI Characters — Companions Go Mainstream (Signature Edition)", "Interactive AI Characters — Meta's AI Characters (Signature Edition)", "Interactive AI Characters — Story-Living Apps (Signature Edition)", "Interactive AI Characters — Persistent Story Worlds (Signature Edition)", "Interactive AI Characters — Games Ship Living NPCs (Signature Edition)", "Interactive AI Characters — Characters with Lifelong Arcs (Signature Edition)", "Interactive AI Characters — Characters That Age (Signature Edition)", "Interactive AI Characters — Relationships That Deepen (Signature Edition)"], "Advanced": ["Interactive AI Characters — Characters Crossing Stories (Signature Edition)", "Interactive AI Characters — Reader-Shaped Growth (Signature Edition)", "Interactive AI Characters — Characters with Jobs and Lives (Signature Edition)", "Interactive AI Characters — Graceful Farewells (Signature Edition)", "Interactive AI Characters — Shared Character Canon (Signature Edition)", "Interactive AI Characters — Characters Who Teach (Signature Edition)", "Interactive AI Characters — Gentle Companions (Signature Edition)", "Interactive AI Characters — Character Rights Frameworks (Signature Edition)", "Interactive AI Characters — Persistent Ensemble Casts (Signature Edition)", "Interactive AI Characters — The Living Library (Signature Edition)", "Interactive AI Characters — Living Fictional Friends - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Interactive AI Characters study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-60-interactive-ai-characters-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-60-interactive-ai-characters-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
