(function(){'use strict';
/* JAH The Describing Solves Database generator — jahdb-describing-solves-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DSV-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Described Solution Is - Foundations",
  "State the Problem Before the Solution - Foundations",
  "The Worked Example: Watching a Solution Happen - Foundations",
  "Show the Work, Not Just the Answer - Foundations",
  "Step-by-Step Ordering: Sequence Is the Description - Foundations",
  "Naming the Tools and Materials First - Foundations",
  "Given-Find-Plan: The Classic Three-Box Setup - Foundations",
  "Labeling Each Move: Saying What the Step Does - Foundations",
  "The Check Step: Proving the Answer at the End - Foundations",
  "One Sentence per Step: The Think-Aloud Line - Foundations",
  "Pointing at the Work: Labels, Callouts, and Annotation - Foundations",
  "Reading Direction: How a Reader Follows a Solution - Foundations"
 ],
 "Compounded": [
  "Solution Schemas: Reusable Step Skeletons - Compounded",
  "Fill-in Solution Templates - Compounded",
  "Reading a Described Solution Critically - Compounded",
  "Describing a Dead End Honestly - Compounded",
  "Partial Solutions and Progress Marks - Compounded",
  "The Diagnostic Narrative: Describing How You Found the Fault - Compounded",
  "Repair Walkthroughs: Describing How You Fixed It - Compounded",
  "Presenting a Math Solution in Writing - Compounded",
  "Presenting a Science Solution: The Lab-Report Style - Compounded",
  "Presenting an Engineering Solution: The Design Narrative - Compounded",
  "Presenting a Craft and Trade Solution - Compounded",
  "Presenting an Everyday Problem Solution - Compounded"
 ],
 "Advanced": [
  "Proof Write-ups: Formal Solution Description - Advanced",
  "How-to-Describe Methods: Teaching the Skill Itself - Advanced",
  "Solution Storytelling: The Arc of a Fix - Advanced",
  "Describing Trade-offs Inside a Chosen Solution - Advanced",
  "Comparing Two Solutions in Writing - Advanced",
  "The Rubric View: What Graders Look For - Advanced",
  "Solution-Explanation Best Practices - Advanced",
  "Describing Solutions to a Group: The Presentation Layer - Advanced",
  "The Debugging Log Pattern - Advanced",
  "Full Worked-Through Solution System: From Blank Page to Archive - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Describing Solve Study — "+safe+"\n"
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
    name:topic+' — solution-description record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A solution-description record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"describing-solve-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-describing-solves-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('describing-solves',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
