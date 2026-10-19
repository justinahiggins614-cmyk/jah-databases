(function(){'use strict';
/* JAH The Creative Project Planning Database generator — jahdb-creative-project-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Creative Project Planning: Know Your Audience — foundations",
  "Creative Project Planning: The Core Message — foundations",
  "Creative Project Planning: Structure That Holds — foundations",
  "Creative Project Planning: Stories That Persuade — foundations",
  "Creative Project Planning: Listening Deeply — foundations",
  "Creative Project Planning: Asking Great Questions — foundations",
  "Creative Project Planning: Feedback That Helps — foundations",
  "Creative Project Planning: Difficult Conversations — foundations",
  "Creative Project Planning: De-escalation in Practice — foundations",
  "Creative Project Planning: Negotiating Communication — foundations",
  "Creative Project Planning: Presenting With Confidence — foundations",
  "Creative Project Planning: Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Creative Project Planning: Email That Works — compounded",
  "Creative Project Planning: Meetings That Matter — compounded",
  "Creative Project Planning: Brainstorming That Produces — compounded",
  "Creative Project Planning: Visual Communication — compounded",
  "Creative Project Planning: Cross-Cultural Communication — compounded",
  "Creative Project Planning: Translation Quality — compounded",
  "Creative Project Planning: Plain Language Mastery — compounded",
  "Creative Project Planning: Public Domain Gold — compounded",
  "Creative Project Planning: Copyright Basics — compounded",
  "Creative Project Planning: Creative Project Planning — compounded",
  "Creative Project Planning: Advanced: Rhetoric and Persuasion — compounded",
  "Creative Project Planning: Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Creative Project Planning: Advanced: Leading Through Story — advanced",
  "Creative Project Planning: Advanced: Facilitation Mastery — advanced",
  "Creative Project Planning: Advanced: Mediation Skills — advanced",
  "Creative Project Planning: Advanced: The Interview Art — advanced",
  "Creative Project Planning: Advanced: Speechwriting — advanced",
  "Creative Project Planning: Advanced: Building a Platform — advanced",
  "Creative Project Planning: Advanced: Communication Audits — advanced",
  "Creative Project Planning: Advanced: Teaching Communication — advanced",
  "Creative Project Planning: Advanced: The Lifetime Communicator — advanced",
  "Creative Project Planning: Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Creative Project Planning Database — structural study\n"
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
var gen={version:'jahdb-creative-project-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('creative-project-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
