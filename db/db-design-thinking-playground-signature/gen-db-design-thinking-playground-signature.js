(function(){'use strict';
/* JAH The Design Thinking Playground generator — jahdb-db-design-thinking-playground-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DTHPS-";
var FIELDS=["Empathize","Ideate & Prototype","Test"];
var TOPICS={
 "Empathize": [
  "What Is Design Thinking (Signature Edition) - Empathize",
  "Empathy: Watch and Listen (Signature Edition) - Empathize",
  "The 5 Whys: Digging to Roots (Signature Edition) - Empathize",
  "Journey Mapping (Signature Edition) - Empathize",
  "Personas: Designing for Someone (Signature Edition) - Empathize",
  "Define: The Point of View (Signature Edition) - Empathize",
  "How Might We: Questions That Open (Signature Edition) - Empathize",
  "Observation Without Judgment (Signature Edition) - Empathize",
  "Interviewing Users (Signature Edition) - Empathize",
  "Extreme Users (Signature Edition) - Empathize",
  "Empathy Maps (Signature Edition) - Empathize",
  "From Data to Insight (Signature Edition) - Empathize"
 ],
 "Ideate & Prototype": [
  "Ideation: Quantity First (Signature Edition) - Ideate & Prototype",
  "Brainstorming Formats (Signature Edition) - Ideate & Prototype",
  "Sketching Ideas (Signature Edition) - Ideate & Prototype",
  "Paper Prototypes (Signature Edition) - Ideate & Prototype",
  "Storyboarding the Experience (Signature Edition) - Ideate & Prototype",
  "Prototyping Mindsets (Signature Edition) - Ideate & Prototype",
  "The Design Critique (Signature Edition) - Ideate & Prototype",
  "Iteration Loops (Signature Edition) - Ideate & Prototype",
  "Choosing Concepts (Signature Edition) - Ideate & Prototype",
  "Crazy 8s: Eight Ideas in Eight Minutes (Signature Edition) - Ideate & Prototype",
  "Story Pitch: Selling the Idea (Signature Edition) - Ideate & Prototype",
  "Experience Prototyping (Signature Edition) - Ideate & Prototype"
 ],
 "Test": [
  "Test With Users (Signature Edition) - Test",
  "The 5-Second Test (Signature Edition) - Test",
  "A/B Testing Basics (Signature Edition) - Test",
  "Feedback That Helps (Signature Edition) - Test",
  "Pilots: Testing in the Wild (Signature Edition) - Test",
  "Measuring What Matters (Signature Edition) - Test",
  "Accessibility Testing (Signature Edition) - Test",
  "The Debrief: Learning From Tests (Signature Edition) - Test",
  "Launching What You Learned (Signature Edition) - Test",
  "Design Thinking for Life (Signature Edition) - Test"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Design Thinking Study — "+safe+"\n"
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
    name:topic+' — design thinking lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design thinking lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"design-thinking-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-design-thinking-playground-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-design-thinking-playground-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
