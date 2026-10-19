(function(){'use strict';
/* JAH The Academic Integrity Education Database generator — jahdb-academic-integrity-education-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AIE-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Academic Integrity Education: What You Must Know First — foundations",
  "Academic Integrity Education: The Core Idea in Plain Words — foundations",
  "Academic Integrity Education: Worked Example, Step by Step — foundations",
  "Academic Integrity Education: Practice Problems With Answers — foundations",
  "Academic Integrity Education: Common Misconceptions — foundations",
  "Academic Integrity Education: How to Verify Your Answers — foundations",
  "Academic Integrity Education: Memory Techniques That Work — foundations",
  "Academic Integrity Education: Taking Useful Notes — foundations",
  "Academic Integrity Education: Study Schedules That Hold — foundations",
  "Academic Integrity Education: Learning From Mistakes — foundations",
  "Academic Integrity Education: Asking for Help Effectively — foundations",
  "Academic Integrity Education: Test-Taking Strategy — foundations"
 ],
 "compounded": [
  "Academic Integrity Education: Group Study That Works — compounded",
  "Academic Integrity Education: Teaching What You Learn — compounded",
  "Academic Integrity Education: Connecting Ideas Across Subjects — compounded",
  "Academic Integrity Education: Reading Textbooks Actively — compounded",
  "Academic Integrity Education: Research Skills Basics — compounded",
  "Academic Integrity Education: Writing About What You Learn — compounded",
  "Academic Integrity Education: Presenting Your Knowledge — compounded",
  "Academic Integrity Education: Online Learning Discipline — compounded",
  "Academic Integrity Education: Adult Learner Strategies — compounded",
  "Academic Integrity Education: Helping Kids Learn This — compounded",
  "Academic Integrity Education: Advanced: Designing Curricula — compounded",
  "Academic Integrity Education: Advanced: Assessing Understanding — compounded"
 ],
 "advanced": [
  "Academic Integrity Education: Advanced: Adaptive Learning Paths — advanced",
  "Academic Integrity Education: Advanced: The Science of Expertise — advanced",
  "Academic Integrity Education: Advanced: Peer Teaching Systems — advanced",
  "Academic Integrity Education: Advanced: Learning Analytics — advanced",
  "Academic Integrity Education: Advanced: Credentialing and Proof — advanced",
  "Academic Integrity Education: Advanced: Lifelong Learning Systems — advanced",
  "Academic Integrity Education: Advanced: Teaching Teachers — advanced",
  "Academic Integrity Education: Advanced: Research on Learning Itself — advanced",
  "Academic Integrity Education: Advanced: Building Learning Organizations — advanced",
  "Academic Integrity Education: Advanced: The Future of Learning This — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Academic Integrity Education Database — structural study\n"
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
var gen={version:'jahdb-academic-integrity-education-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('academic-integrity-education',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
