(function(){'use strict';
/* JAH The Translation Quality Evaluation Database generator — jahdb-translation-quality-evaluation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TQE-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Translation Quality Evaluation: Know Your Audience — foundations",
  "Translation Quality Evaluation: The Core Message — foundations",
  "Translation Quality Evaluation: Structure That Holds — foundations",
  "Translation Quality Evaluation: Stories That Persuade — foundations",
  "Translation Quality Evaluation: Listening Deeply — foundations",
  "Translation Quality Evaluation: Asking Great Questions — foundations",
  "Translation Quality Evaluation: Feedback That Helps — foundations",
  "Translation Quality Evaluation: Difficult Conversations — foundations",
  "Translation Quality Evaluation: De-escalation in Practice — foundations",
  "Translation Quality Evaluation: Negotiating Communication — foundations",
  "Translation Quality Evaluation: Presenting With Confidence — foundations",
  "Translation Quality Evaluation: Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Translation Quality Evaluation: Email That Works — compounded",
  "Translation Quality Evaluation: Meetings That Matter — compounded",
  "Translation Quality Evaluation: Brainstorming That Produces — compounded",
  "Translation Quality Evaluation: Visual Communication — compounded",
  "Translation Quality Evaluation: Cross-Cultural Communication — compounded",
  "Translation Quality Evaluation: Translation Quality — compounded",
  "Translation Quality Evaluation: Plain Language Mastery — compounded",
  "Translation Quality Evaluation: Public Domain Gold — compounded",
  "Translation Quality Evaluation: Copyright Basics — compounded",
  "Translation Quality Evaluation: Creative Project Planning — compounded",
  "Translation Quality Evaluation: Advanced: Rhetoric and Persuasion — compounded",
  "Translation Quality Evaluation: Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Translation Quality Evaluation: Advanced: Leading Through Story — advanced",
  "Translation Quality Evaluation: Advanced: Facilitation Mastery — advanced",
  "Translation Quality Evaluation: Advanced: Mediation Skills — advanced",
  "Translation Quality Evaluation: Advanced: The Interview Art — advanced",
  "Translation Quality Evaluation: Advanced: Speechwriting — advanced",
  "Translation Quality Evaluation: Advanced: Building a Platform — advanced",
  "Translation Quality Evaluation: Advanced: Communication Audits — advanced",
  "Translation Quality Evaluation: Advanced: Teaching Communication — advanced",
  "Translation Quality Evaluation: Advanced: The Lifetime Communicator — advanced",
  "Translation Quality Evaluation: Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Translation Quality Evaluation Database — structural study\n"
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
var gen={version:'jahdb-translation-quality-evaluation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('translation-quality-evaluation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
