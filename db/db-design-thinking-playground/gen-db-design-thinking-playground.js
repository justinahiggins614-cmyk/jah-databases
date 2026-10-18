(function(){'use strict';
/* JAH The Design Thinking Playground generator — jahdb-db-design-thinking-playground-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DTHP-";
var FIELDS=["Empathize","Ideate & Prototype","Test"];
var TOPICS={
 "Empathize": [
  "What Is Design Thinking - Empathize",
  "Empathy: Watch and Listen - Empathize",
  "The 5 Whys: Digging to Roots - Empathize",
  "Journey Mapping - Empathize",
  "Personas: Designing for Someone - Empathize",
  "Define: The Point of View - Empathize",
  "How Might We: Questions That Open - Empathize",
  "Observation Without Judgment - Empathize",
  "Interviewing Users - Empathize",
  "Extreme Users - Empathize",
  "Empathy Maps - Empathize",
  "From Data to Insight - Empathize"
 ],
 "Ideate & Prototype": [
  "Ideation: Quantity First - Ideate & Prototype",
  "Brainstorming Formats - Ideate & Prototype",
  "Sketching Ideas - Ideate & Prototype",
  "Paper Prototypes - Ideate & Prototype",
  "Storyboarding the Experience - Ideate & Prototype",
  "Prototyping Mindsets - Ideate & Prototype",
  "The Design Critique - Ideate & Prototype",
  "Iteration Loops - Ideate & Prototype",
  "Choosing Concepts - Ideate & Prototype",
  "Crazy 8s: Eight Ideas in Eight Minutes - Ideate & Prototype",
  "Story Pitch: Selling the Idea - Ideate & Prototype",
  "Experience Prototyping - Ideate & Prototype"
 ],
 "Test": [
  "Test With Users - Test",
  "The 5-Second Test - Test",
  "A/B Testing Basics - Test",
  "Feedback That Helps - Test",
  "Pilots: Testing in the Wild - Test",
  "Measuring What Matters - Test",
  "Accessibility Testing - Test",
  "The Debrief: Learning From Tests - Test",
  "Launching What You Learned - Test",
  "Design Thinking for Life - Test"
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
var gen={version:'jahdb-db-design-thinking-playground-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-design-thinking-playground',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
