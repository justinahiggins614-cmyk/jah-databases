(function(){'use strict';
/* JAH The Answer Verification Methods Database generator — jahdb-answer-verification-methods-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AVM-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Answer Verification Methods: What You Must Know First — foundations",
  "Answer Verification Methods: The Core Idea in Plain Words — foundations",
  "Answer Verification Methods: Worked Example, Step by Step — foundations",
  "Answer Verification Methods: Practice Problems With Answers — foundations",
  "Answer Verification Methods: Common Misconceptions — foundations",
  "Answer Verification Methods: How to Verify Your Answers — foundations",
  "Answer Verification Methods: Memory Techniques That Work — foundations",
  "Answer Verification Methods: Taking Useful Notes — foundations",
  "Answer Verification Methods: Study Schedules That Hold — foundations",
  "Answer Verification Methods: Learning From Mistakes — foundations",
  "Answer Verification Methods: Asking for Help Effectively — foundations",
  "Answer Verification Methods: Test-Taking Strategy — foundations"
 ],
 "compounded": [
  "Answer Verification Methods: Group Study That Works — compounded",
  "Answer Verification Methods: Teaching What You Learn — compounded",
  "Answer Verification Methods: Connecting Ideas Across Subjects — compounded",
  "Answer Verification Methods: Reading Textbooks Actively — compounded",
  "Answer Verification Methods: Research Skills Basics — compounded",
  "Answer Verification Methods: Writing About What You Learn — compounded",
  "Answer Verification Methods: Presenting Your Knowledge — compounded",
  "Answer Verification Methods: Online Learning Discipline — compounded",
  "Answer Verification Methods: Adult Learner Strategies — compounded",
  "Answer Verification Methods: Helping Kids Learn This — compounded",
  "Answer Verification Methods: Advanced: Designing Curricula — compounded",
  "Answer Verification Methods: Advanced: Assessing Understanding — compounded"
 ],
 "advanced": [
  "Answer Verification Methods: Advanced: Adaptive Learning Paths — advanced",
  "Answer Verification Methods: Advanced: The Science of Expertise — advanced",
  "Answer Verification Methods: Advanced: Peer Teaching Systems — advanced",
  "Answer Verification Methods: Advanced: Learning Analytics — advanced",
  "Answer Verification Methods: Advanced: Credentialing and Proof — advanced",
  "Answer Verification Methods: Advanced: Lifelong Learning Systems — advanced",
  "Answer Verification Methods: Advanced: Teaching Teachers — advanced",
  "Answer Verification Methods: Advanced: Research on Learning Itself — advanced",
  "Answer Verification Methods: Advanced: Building Learning Organizations — advanced",
  "Answer Verification Methods: Advanced: The Future of Learning This — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Answer Verification Methods Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-answer-verification-methods-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('answer-verification-methods',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
