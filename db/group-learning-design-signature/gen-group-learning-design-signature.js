(function(){'use strict';
/* JAH The Group Learning Design Signature Database generator — jahdb-group-learning-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GLDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Group Learning Design (Signature): What You Must Know First — foundations",
  "Group Learning Design (Signature): The Core Idea in Plain Words — foundations",
  "Group Learning Design (Signature): Worked Example, Step by Step — foundations",
  "Group Learning Design (Signature): Practice Problems With Answers — foundations",
  "Group Learning Design (Signature): Common Misconceptions — foundations",
  "Group Learning Design (Signature): How to Verify Your Answers — foundations",
  "Group Learning Design (Signature): Memory Techniques That Work — foundations",
  "Group Learning Design (Signature): Taking Useful Notes — foundations",
  "Group Learning Design (Signature): Study Schedules That Hold — foundations",
  "Group Learning Design (Signature): Learning From Mistakes — foundations",
  "Group Learning Design (Signature): Asking for Help Effectively — foundations",
  "Group Learning Design (Signature): Test-Taking Strategy — foundations"
 ],
 "compounded": [
  "Group Learning Design (Signature): Group Study That Works — compounded",
  "Group Learning Design (Signature): Teaching What You Learn — compounded",
  "Group Learning Design (Signature): Connecting Ideas Across Subjects — compounded",
  "Group Learning Design (Signature): Reading Textbooks Actively — compounded",
  "Group Learning Design (Signature): Research Skills Basics — compounded",
  "Group Learning Design (Signature): Writing About What You Learn — compounded",
  "Group Learning Design (Signature): Presenting Your Knowledge — compounded",
  "Group Learning Design (Signature): Online Learning Discipline — compounded",
  "Group Learning Design (Signature): Adult Learner Strategies — compounded",
  "Group Learning Design (Signature): Helping Kids Learn This — compounded",
  "Group Learning Design (Signature): Advanced: Designing Curricula — compounded",
  "Group Learning Design (Signature): Advanced: Assessing Understanding — compounded"
 ],
 "advanced": [
  "Group Learning Design (Signature): Advanced: Adaptive Learning Paths — advanced",
  "Group Learning Design (Signature): Advanced: The Science of Expertise — advanced",
  "Group Learning Design (Signature): Advanced: Peer Teaching Systems — advanced",
  "Group Learning Design (Signature): Advanced: Learning Analytics — advanced",
  "Group Learning Design (Signature): Advanced: Credentialing and Proof — advanced",
  "Group Learning Design (Signature): Advanced: Lifelong Learning Systems — advanced",
  "Group Learning Design (Signature): Advanced: Teaching Teachers — advanced",
  "Group Learning Design (Signature): Advanced: Research on Learning Itself — advanced",
  "Group Learning Design (Signature): Advanced: Building Learning Organizations — advanced",
  "Group Learning Design (Signature): Advanced: The Future of Learning This — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Group Learning Design Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-group-learning-design-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('group-learning-design-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
