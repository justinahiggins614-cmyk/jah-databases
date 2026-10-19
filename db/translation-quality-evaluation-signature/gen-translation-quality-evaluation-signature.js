(function(){'use strict';
/* JAH The Translation Quality Evaluation Signature Database generator — jahdb-translation-quality-evaluation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TQES-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Translation Quality Evaluation (Signature): Know Your Audience — foundations",
  "Translation Quality Evaluation (Signature): The Core Message — foundations",
  "Translation Quality Evaluation (Signature): Structure That Holds — foundations",
  "Translation Quality Evaluation (Signature): Stories That Persuade — foundations",
  "Translation Quality Evaluation (Signature): Listening Deeply — foundations",
  "Translation Quality Evaluation (Signature): Asking Great Questions — foundations",
  "Translation Quality Evaluation (Signature): Feedback That Helps — foundations",
  "Translation Quality Evaluation (Signature): Difficult Conversations — foundations",
  "Translation Quality Evaluation (Signature): De-escalation in Practice — foundations",
  "Translation Quality Evaluation (Signature): Negotiating Communication — foundations",
  "Translation Quality Evaluation (Signature): Presenting With Confidence — foundations",
  "Translation Quality Evaluation (Signature): Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Translation Quality Evaluation (Signature): Email That Works — compounded",
  "Translation Quality Evaluation (Signature): Meetings That Matter — compounded",
  "Translation Quality Evaluation (Signature): Brainstorming That Produces — compounded",
  "Translation Quality Evaluation (Signature): Visual Communication — compounded",
  "Translation Quality Evaluation (Signature): Cross-Cultural Communication — compounded",
  "Translation Quality Evaluation (Signature): Translation Quality — compounded",
  "Translation Quality Evaluation (Signature): Plain Language Mastery — compounded",
  "Translation Quality Evaluation (Signature): Public Domain Gold — compounded",
  "Translation Quality Evaluation (Signature): Copyright Basics — compounded",
  "Translation Quality Evaluation (Signature): Creative Project Planning — compounded",
  "Translation Quality Evaluation (Signature): Advanced: Rhetoric and Persuasion — compounded",
  "Translation Quality Evaluation (Signature): Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Translation Quality Evaluation (Signature): Advanced: Leading Through Story — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Facilitation Mastery — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Mediation Skills — advanced",
  "Translation Quality Evaluation (Signature): Advanced: The Interview Art — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Speechwriting — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Building a Platform — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Communication Audits — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Teaching Communication — advanced",
  "Translation Quality Evaluation (Signature): Advanced: The Lifetime Communicator — advanced",
  "Translation Quality Evaluation (Signature): Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Translation Quality Evaluation Signature Database — structural study\n"
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
var gen={version:'jahdb-translation-quality-evaluation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('translation-quality-evaluation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
