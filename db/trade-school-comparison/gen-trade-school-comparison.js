(function(){'use strict';
/* JAH The Trade School Comparison Database generator — jahdb-trade-school-comparison-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSC-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Trade School Comparison: What You Must Know First — foundations",
  "Trade School Comparison: The Core Idea in Plain Words — foundations",
  "Trade School Comparison: Worked Example, Step by Step — foundations",
  "Trade School Comparison: Practice Problems With Answers — foundations",
  "Trade School Comparison: Common Misconceptions — foundations",
  "Trade School Comparison: How to Verify Your Answers — foundations",
  "Trade School Comparison: Memory Techniques That Work — foundations",
  "Trade School Comparison: Taking Useful Notes — foundations",
  "Trade School Comparison: Study Schedules That Hold — foundations",
  "Trade School Comparison: Learning From Mistakes — foundations",
  "Trade School Comparison: Asking for Help Effectively — foundations",
  "Trade School Comparison: Test-Taking Strategy — foundations"
 ],
 "compounded": [
  "Trade School Comparison: Group Study That Works — compounded",
  "Trade School Comparison: Teaching What You Learn — compounded",
  "Trade School Comparison: Connecting Ideas Across Subjects — compounded",
  "Trade School Comparison: Reading Textbooks Actively — compounded",
  "Trade School Comparison: Research Skills Basics — compounded",
  "Trade School Comparison: Writing About What You Learn — compounded",
  "Trade School Comparison: Presenting Your Knowledge — compounded",
  "Trade School Comparison: Online Learning Discipline — compounded",
  "Trade School Comparison: Adult Learner Strategies — compounded",
  "Trade School Comparison: Helping Kids Learn This — compounded",
  "Trade School Comparison: Advanced: Designing Curricula — compounded",
  "Trade School Comparison: Advanced: Assessing Understanding — compounded"
 ],
 "advanced": [
  "Trade School Comparison: Advanced: Adaptive Learning Paths — advanced",
  "Trade School Comparison: Advanced: The Science of Expertise — advanced",
  "Trade School Comparison: Advanced: Peer Teaching Systems — advanced",
  "Trade School Comparison: Advanced: Learning Analytics — advanced",
  "Trade School Comparison: Advanced: Credentialing and Proof — advanced",
  "Trade School Comparison: Advanced: Lifelong Learning Systems — advanced",
  "Trade School Comparison: Advanced: Teaching Teachers — advanced",
  "Trade School Comparison: Advanced: Research on Learning Itself — advanced",
  "Trade School Comparison: Advanced: Building Learning Organizations — advanced",
  "Trade School Comparison: Advanced: The Future of Learning This — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Trade School Comparison Database — structural study\n"
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
var gen={version:'jahdb-trade-school-comparison-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('trade-school-comparison',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
