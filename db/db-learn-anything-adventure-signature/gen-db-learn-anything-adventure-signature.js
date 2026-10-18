(function(){'use strict';
/* JAH The Learn Anything Adventure Signature Database generator — jahdb-db-learn-anything-adventure-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LAAS-";
var FIELDS=["Learning Foundations","Study Systems","Mastery Projects"];
var TOPICS={
 "Learning Foundations": [
  "Your Brain Learns by Building (Signature Edition) - Learning Foundations",
  "Attention Is the Gatekeeper (Signature Edition) - Learning Foundations",
  "Working Memory Has Limits (Signature Edition) - Learning Foundations",
  "Spacing Beats Cramming (Signature Edition) - Learning Foundations",
  "Sleep Locks In Learning (Signature Edition) - Learning Foundations",
  "Confusion Is the Feeling of Learning (Signature Edition) - Learning Foundations",
  "Teach It to Learn It (Signature Edition) - Learning Foundations",
  "Examples Before Rules (Signature Edition) - Learning Foundations",
  "Mistakes Are Data (Signature Edition) - Learning Foundations",
  "Curiosity Opens the Brain (Signature Edition) - Learning Foundations",
  "The Forgetting Curve Is Normal (Signature Edition) - Learning Foundations",
  "Interleave, Don't Block (Signature Edition) - Learning Foundations"
 ],
 "Study Systems": [
  "Build a 25-Minute Focus Ritual (Signature Edition) - Study Systems",
  "The Cornell Note Method (Signature Edition) - Study Systems",
  "Flashcards Done Right (Signature Edition) - Study Systems",
  "The Weekly Review Habit (Signature Edition) - Study Systems",
  "Map the Territory First (Signature Edition) - Study Systems",
  "Study With a Partner Protocol (Signature Edition) - Study Systems",
  "The Two-Pass Reading Method (Signature Edition) - Study Systems",
  "Error Log: Your Personal Textbook (Signature Edition) - Study Systems",
  "Timebox the Hard Part (Signature Edition) - Study Systems",
  "Environment Design Beats Willpower (Signature Edition) - Study Systems",
  "The 85% Rule for Practice (Signature Edition) - Study Systems",
  "Deliberate Practice Protocol (Signature Edition) - Study Systems"
 ],
 "Mastery Projects": [
  "Design Your 30-Day Challenge (Signature Edition) - Mastery Projects",
  "Build a Portfolio, Not a Transcript (Signature Edition) - Mastery Projects",
  "Teach a Beginner (Signature Edition) - Mastery Projects",
  "Enter the Arena: Compete (Signature Edition) - Mastery Projects",
  "The Capstone: Ship Something Real (Signature Edition) - Mastery Projects",
  "Learn in Public (Signature Edition) - Mastery Projects",
  "Find Your Mastermind (Signature Edition) - Mastery Projects",
  "The 100-Hour Rule (Signature Edition) - Mastery Projects",
  "Specialize, Then Broaden (Signature Edition) - Mastery Projects",
  "Become the Person Who Ships (Signature Edition) - Mastery Projects"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Learn Anything Study — "+safe+"\n"
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
    name:topic+' — learning adventure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A learning adventure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"learn-anything-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-learn-anything-adventure-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-learn-anything-adventure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
