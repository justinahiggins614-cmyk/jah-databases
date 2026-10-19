(function(){'use strict';
/* JAH The Creative Brainstorming Methods Signature Database generator — jahdb-creative-brainstorming-methods-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBMS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Creative Brainstorming Methods (Signature): Know Your Audience — foundations",
  "Creative Brainstorming Methods (Signature): The Core Message — foundations",
  "Creative Brainstorming Methods (Signature): Structure That Holds — foundations",
  "Creative Brainstorming Methods (Signature): Stories That Persuade — foundations",
  "Creative Brainstorming Methods (Signature): Listening Deeply — foundations",
  "Creative Brainstorming Methods (Signature): Asking Great Questions — foundations",
  "Creative Brainstorming Methods (Signature): Feedback That Helps — foundations",
  "Creative Brainstorming Methods (Signature): Difficult Conversations — foundations",
  "Creative Brainstorming Methods (Signature): De-escalation in Practice — foundations",
  "Creative Brainstorming Methods (Signature): Negotiating Communication — foundations",
  "Creative Brainstorming Methods (Signature): Presenting With Confidence — foundations",
  "Creative Brainstorming Methods (Signature): Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Creative Brainstorming Methods (Signature): Email That Works — compounded",
  "Creative Brainstorming Methods (Signature): Meetings That Matter — compounded",
  "Creative Brainstorming Methods (Signature): Brainstorming That Produces — compounded",
  "Creative Brainstorming Methods (Signature): Visual Communication — compounded",
  "Creative Brainstorming Methods (Signature): Cross-Cultural Communication — compounded",
  "Creative Brainstorming Methods (Signature): Translation Quality — compounded",
  "Creative Brainstorming Methods (Signature): Plain Language Mastery — compounded",
  "Creative Brainstorming Methods (Signature): Public Domain Gold — compounded",
  "Creative Brainstorming Methods (Signature): Copyright Basics — compounded",
  "Creative Brainstorming Methods (Signature): Creative Project Planning — compounded",
  "Creative Brainstorming Methods (Signature): Advanced: Rhetoric and Persuasion — compounded",
  "Creative Brainstorming Methods (Signature): Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Creative Brainstorming Methods (Signature): Advanced: Leading Through Story — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Facilitation Mastery — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Mediation Skills — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: The Interview Art — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Speechwriting — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Building a Platform — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Communication Audits — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Teaching Communication — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: The Lifetime Communicator — advanced",
  "Creative Brainstorming Methods (Signature): Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Creative Brainstorming Methods Signature Database — structural study\n"
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
var gen={version:'jahdb-creative-brainstorming-methods-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('creative-brainstorming-methods-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
