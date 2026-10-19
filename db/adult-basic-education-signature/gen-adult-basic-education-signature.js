(function(){'use strict';
/* JAH The Adult Basic Education Signature Database generator — jahdb-adult-basic-education-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ABES-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Adult Basic Education (Signature): What You Must Know First — foundations",
  "Adult Basic Education (Signature): The Core Idea in Plain Words — foundations",
  "Adult Basic Education (Signature): Worked Example, Step by Step — foundations",
  "Adult Basic Education (Signature): Practice Problems With Answers — foundations",
  "Adult Basic Education (Signature): Common Misconceptions — foundations",
  "Adult Basic Education (Signature): How to Verify Your Answers — foundations",
  "Adult Basic Education (Signature): Memory Techniques That Work — foundations",
  "Adult Basic Education (Signature): Taking Useful Notes — foundations",
  "Adult Basic Education (Signature): Study Schedules That Hold — foundations",
  "Adult Basic Education (Signature): Learning From Mistakes — foundations",
  "Adult Basic Education (Signature): Asking for Help Effectively — foundations",
  "Adult Basic Education (Signature): Test-Taking Strategy — foundations"
 ],
 "compounded": [
  "Adult Basic Education (Signature): Group Study That Works — compounded",
  "Adult Basic Education (Signature): Teaching What You Learn — compounded",
  "Adult Basic Education (Signature): Connecting Ideas Across Subjects — compounded",
  "Adult Basic Education (Signature): Reading Textbooks Actively — compounded",
  "Adult Basic Education (Signature): Research Skills Basics — compounded",
  "Adult Basic Education (Signature): Writing About What You Learn — compounded",
  "Adult Basic Education (Signature): Presenting Your Knowledge — compounded",
  "Adult Basic Education (Signature): Online Learning Discipline — compounded",
  "Adult Basic Education (Signature): Adult Learner Strategies — compounded",
  "Adult Basic Education (Signature): Helping Kids Learn This — compounded",
  "Adult Basic Education (Signature): Advanced: Designing Curricula — compounded",
  "Adult Basic Education (Signature): Advanced: Assessing Understanding — compounded"
 ],
 "advanced": [
  "Adult Basic Education (Signature): Advanced: Adaptive Learning Paths — advanced",
  "Adult Basic Education (Signature): Advanced: The Science of Expertise — advanced",
  "Adult Basic Education (Signature): Advanced: Peer Teaching Systems — advanced",
  "Adult Basic Education (Signature): Advanced: Learning Analytics — advanced",
  "Adult Basic Education (Signature): Advanced: Credentialing and Proof — advanced",
  "Adult Basic Education (Signature): Advanced: Lifelong Learning Systems — advanced",
  "Adult Basic Education (Signature): Advanced: Teaching Teachers — advanced",
  "Adult Basic Education (Signature): Advanced: Research on Learning Itself — advanced",
  "Adult Basic Education (Signature): Advanced: Building Learning Organizations — advanced",
  "Adult Basic Education (Signature): Advanced: The Future of Learning This — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Adult Basic Education Signature Database — structural study\n"
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
var gen={version:'jahdb-adult-basic-education-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('adult-basic-education-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
