(function(){'use strict';
/* JAH The Debate Skills Arena generator — jahdb-db-debate-skills-arena-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEBSS-";
var FIELDS=["Argument Building","Rebuttal","Formats"];
var TOPICS={
 "Argument Building": [
  "What Is Debate (Signature Edition) - Argument Building",
  "The Motion: What You're Debating (Signature Edition) - Argument Building",
  "ARE: Assertion, Reasoning, Evidence (Signature Edition) - Argument Building",
  "Building a Case (Signature Edition) - Argument Building",
  "Framing: Setting the Terms (Signature Edition) - Argument Building",
  "Evidence That Persuades (Signature Edition) - Argument Building",
  "Impacts: Why It Matters (Signature Edition) - Argument Building",
  "Signposting: Guiding the Judge (Signature Edition) - Argument Building",
  "Note-Taking (Flowing) (Signature Edition) - Argument Building",
  "Time Management in Speeches (Signature Edition) - Argument Building",
  "Partner Coordination (Signature Edition) - Argument Building",
  "The First Speaker's Job (Signature Edition) - Argument Building"
 ],
 "Rebuttal": [
  "Listening to Rebut (Signature Edition) - Rebuttal",
  "The 4-Step Rebuttal (Signature Edition) - Rebuttal",
  "Turning Their Arguments (Signature Edition) - Rebuttal",
  "Handling Evidence Challenges (Signature Edition) - Rebuttal",
  "Spotting Fallacies Live (Signature Edition) - Rebuttal",
  "Defense: Protecting Your Case (Signature Edition) - Rebuttal",
  "Clash: The Heart of Debate (Signature Edition) - Rebuttal",
  "POIs: Points of Information (Signature Edition) - Rebuttal",
  "Summary Speeches (Signature Edition) - Rebuttal",
  "Weighing: Why You Win (Signature Edition) - Rebuttal",
  "Preemptive Rebuttal: Blocking Attacks (Signature Edition) - Rebuttal"
 ],
 "Formats": [
  "British Parliamentary Format (Signature Edition) - Formats",
  "Policy Debate Format (Signature Edition) - Formats",
  "Lincoln-Douglas: Values Debate (Signature Edition) - Formats",
  "Public Forum Format (Signature Edition) - Formats",
  "Impromptu Debating (Signature Edition) - Formats",
  "Moot Court (Signature Edition) - Formats",
  "Debating Online (Signature Edition) - Formats",
  "Judging Debates (Signature Edition) - Formats",
  "Tournament Survival (Signature Edition) - Formats",
  "The Debate Career (Signature Edition) - Formats",
  "World Schools Format (Signature Edition) - Formats"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Debate Arena Study — "+safe+"\n"
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
    name:topic+' — debate lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A debate lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"debate-arena-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-debate-skills-arena-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-debate-skills-arena-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
