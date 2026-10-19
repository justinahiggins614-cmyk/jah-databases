(function(){'use strict';
/* JAH The Conflict De-escalation Communication Database generator — jahdb-conflict-de-escalation-communication-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CDEC-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Conflict De-escalation Communication: Know Your Audience — foundations",
  "Conflict De-escalation Communication: The Core Message — foundations",
  "Conflict De-escalation Communication: Structure That Holds — foundations",
  "Conflict De-escalation Communication: Stories That Persuade — foundations",
  "Conflict De-escalation Communication: Listening Deeply — foundations",
  "Conflict De-escalation Communication: Asking Great Questions — foundations",
  "Conflict De-escalation Communication: Feedback That Helps — foundations",
  "Conflict De-escalation Communication: Difficult Conversations — foundations",
  "Conflict De-escalation Communication: De-escalation in Practice — foundations",
  "Conflict De-escalation Communication: Negotiating Communication — foundations",
  "Conflict De-escalation Communication: Presenting With Confidence — foundations",
  "Conflict De-escalation Communication: Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Conflict De-escalation Communication: Email That Works — compounded",
  "Conflict De-escalation Communication: Meetings That Matter — compounded",
  "Conflict De-escalation Communication: Brainstorming That Produces — compounded",
  "Conflict De-escalation Communication: Visual Communication — compounded",
  "Conflict De-escalation Communication: Cross-Cultural Communication — compounded",
  "Conflict De-escalation Communication: Translation Quality — compounded",
  "Conflict De-escalation Communication: Plain Language Mastery — compounded",
  "Conflict De-escalation Communication: Public Domain Gold — compounded",
  "Conflict De-escalation Communication: Copyright Basics — compounded",
  "Conflict De-escalation Communication: Creative Project Planning — compounded",
  "Conflict De-escalation Communication: Advanced: Rhetoric and Persuasion — compounded",
  "Conflict De-escalation Communication: Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Conflict De-escalation Communication: Advanced: Leading Through Story — advanced",
  "Conflict De-escalation Communication: Advanced: Facilitation Mastery — advanced",
  "Conflict De-escalation Communication: Advanced: Mediation Skills — advanced",
  "Conflict De-escalation Communication: Advanced: The Interview Art — advanced",
  "Conflict De-escalation Communication: Advanced: Speechwriting — advanced",
  "Conflict De-escalation Communication: Advanced: Building a Platform — advanced",
  "Conflict De-escalation Communication: Advanced: Communication Audits — advanced",
  "Conflict De-escalation Communication: Advanced: Teaching Communication — advanced",
  "Conflict De-escalation Communication: Advanced: The Lifetime Communicator — advanced",
  "Conflict De-escalation Communication: Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Conflict De-escalation Communication Database — structural study\n"
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
var gen={version:'jahdb-conflict-de-escalation-communication-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('conflict-de-escalation-communication',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
