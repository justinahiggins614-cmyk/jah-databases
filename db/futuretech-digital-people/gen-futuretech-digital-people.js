(function(){'use strict';
/* JAH The Digital People Technology Database generator — jahdb-futuretech-digital-people-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT003-";
var FIELDS=["Oldest Concepts","Early Development","Working Versions","State of the Art"];
var TOPICS={
 "Oldest Concepts": [
  "Digital People \u2014 Golems and homunculi: artificial people in myth",
  "Digital People \u2014 Pygmalion: the statue come alive",
  "Digital People \u2014 Yan Shi's automaton: the artificial courtier",
  "Digital People \u2014 The Turk: the fake automaton person",
  "Digital People \u2014 Hoffmann's Olimpia: the beloved automaton",
  "Digital People \u2014 Capek's R.U.R.: the word 'robot' is born",
  "Digital People \u2014 Metropolis: the Machine-Man",
  "Digital People \u2014 MUDs and early avatars: persistent digital identities"
 ],
 "Early Development": [
  "Digital People \u2014 The Sims: simulated people",
  "Digital People \u2014 Second Life avatars: living a second life",
  "Digital People \u2014 XiaoIce: the empathic chatbot at scale",
  "Digital People \u2014 Lil Miquela: the AI influencer",
  "Digital People \u2014 Replika: AI companions go mainstream",
  "Digital People \u2014 Digital doubles in film: de-aging and resurrection",
  "Digital People \u2014 Voice cloning: early systems",
  "Digital People \u2014 Grief tech: early memorial chatbots",
  "Digital People \u2014 Persistent memory in companions"
 ],
 "Working Versions": [
  "Digital People \u2014 Modern AI companions with memory",
  "Digital People \u2014 Photorealistic avatars: MetaHuman and neural rendering",
  "Digital People \u2014 Real-time voice and face cloning combined",
  "Digital People \u2014 VTubers as an industry",
  "Digital People \u2014 AI customer personas that work continuously",
  "Digital People \u2014 Consensual digital twins of real people",
  "Digital People \u2014 NPCs with persistent memory in games",
  "Digital People \u2014 Legal frameworks: likeness rights",
  "Digital People \u2014 Detection: telling digital people apart"
 ],
 "State of the Art": [
  "Digital People \u2014 State of the art 2026: convincing but detectable",
  "Digital People \u2014 The uncanny valley: current science",
  "Digital People \u2014 Full human-level equivalence: what it would take",
  "Digital People \u2014 Digital people at work: the economics",
  "Digital People \u2014 Relationships with digital people: the psychology",
  "Digital People \u2014 Consent and likeness: the governance frontier",
  "Digital People \u2014 Indistinguishability scenarios",
  "Digital People \u2014 The working version: persistent, personable, not people"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Digital People study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
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
var gen={version:'jahdb-futuretech-digital-people-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-digital-people',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
