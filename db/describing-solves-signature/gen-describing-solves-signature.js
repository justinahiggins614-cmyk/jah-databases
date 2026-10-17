(function(){'use strict';
/* JAH The Describing Solves Signature Database generator — jahdb-describing-solves-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DSVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Described Solution Is (Signature Edition) - Foundations",
  "State the Problem Before the Solution (Signature Edition) - Foundations",
  "The Worked Example: Watching a Solution Happen (Signature Edition) - Foundations",
  "Show the Work, Not Just the Answer (Signature Edition) - Foundations",
  "Step-by-Step Ordering: Sequence Is the Description (Signature Edition) - Foundations",
  "Naming the Tools and Materials First (Signature Edition) - Foundations",
  "Given-Find-Plan: The Classic Three-Box Setup (Signature Edition) - Foundations",
  "Labeling Each Move: Saying What the Step Does (Signature Edition) - Foundations",
  "The Check Step: Proving the Answer at the End (Signature Edition) - Foundations",
  "One Sentence per Step: The Think-Aloud Line (Signature Edition) - Foundations",
  "Pointing at the Work: Labels, Callouts, and Annotation (Signature Edition) - Foundations",
  "Reading Direction: How a Reader Follows a Solution (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Solution Schemas: Reusable Step Skeletons (Signature Edition) - Compounded",
  "Fill-in Solution Templates (Signature Edition) - Compounded",
  "Reading a Described Solution Critically (Signature Edition) - Compounded",
  "Describing a Dead End Honestly (Signature Edition) - Compounded",
  "Partial Solutions and Progress Marks (Signature Edition) - Compounded",
  "The Diagnostic Narrative: Describing How You Found the Fault (Signature Edition) - Compounded",
  "Repair Walkthroughs: Describing How You Fixed It (Signature Edition) - Compounded",
  "Presenting a Math Solution in Writing (Signature Edition) - Compounded",
  "Presenting a Science Solution: The Lab-Report Style (Signature Edition) - Compounded",
  "Presenting an Engineering Solution: The Design Narrative (Signature Edition) - Compounded",
  "Presenting a Craft and Trade Solution (Signature Edition) - Compounded",
  "Presenting an Everyday Problem Solution (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Proof Write-ups: Formal Solution Description (Signature Edition) - Advanced",
  "How-to-Describe Methods: Teaching the Skill Itself (Signature Edition) - Advanced",
  "Solution Storytelling: The Arc of a Fix (Signature Edition) - Advanced",
  "Describing Trade-offs Inside a Chosen Solution (Signature Edition) - Advanced",
  "Comparing Two Solutions in Writing (Signature Edition) - Advanced",
  "The Rubric View: What Graders Look For (Signature Edition) - Advanced",
  "Solution-Explanation Best Practices (Signature Edition) - Advanced",
  "Describing Solutions to a Group: The Presentation Layer (Signature Edition) - Advanced",
  "The Debugging Log Pattern (Signature Edition) - Advanced",
  "Full Worked-Through Solution System: From Blank Page to Archive (Signature Edition) - Advanced"
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
var gen={version:'jahdb-describing-solves-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('describing-solves-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
