(function(){'use strict';
/* JAH The Public Domain Resource Finder Signature Database generator — jahdb-public-domain-resource-finder-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PDRFS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Public Domain Resource Finder (Signature): Know Your Audience — foundations",
  "Public Domain Resource Finder (Signature): The Core Message — foundations",
  "Public Domain Resource Finder (Signature): Structure That Holds — foundations",
  "Public Domain Resource Finder (Signature): Stories That Persuade — foundations",
  "Public Domain Resource Finder (Signature): Listening Deeply — foundations",
  "Public Domain Resource Finder (Signature): Asking Great Questions — foundations",
  "Public Domain Resource Finder (Signature): Feedback That Helps — foundations",
  "Public Domain Resource Finder (Signature): Difficult Conversations — foundations",
  "Public Domain Resource Finder (Signature): De-escalation in Practice — foundations",
  "Public Domain Resource Finder (Signature): Negotiating Communication — foundations",
  "Public Domain Resource Finder (Signature): Presenting With Confidence — foundations",
  "Public Domain Resource Finder (Signature): Writing That Gets Read — foundations"
 ],
 "compounded": [
  "Public Domain Resource Finder (Signature): Email That Works — compounded",
  "Public Domain Resource Finder (Signature): Meetings That Matter — compounded",
  "Public Domain Resource Finder (Signature): Brainstorming That Produces — compounded",
  "Public Domain Resource Finder (Signature): Visual Communication — compounded",
  "Public Domain Resource Finder (Signature): Cross-Cultural Communication — compounded",
  "Public Domain Resource Finder (Signature): Translation Quality — compounded",
  "Public Domain Resource Finder (Signature): Plain Language Mastery — compounded",
  "Public Domain Resource Finder (Signature): Public Domain Gold — compounded",
  "Public Domain Resource Finder (Signature): Copyright Basics — compounded",
  "Public Domain Resource Finder (Signature): Creative Project Planning — compounded",
  "Public Domain Resource Finder (Signature): Advanced: Rhetoric and Persuasion — compounded",
  "Public Domain Resource Finder (Signature): Advanced: Crisis Communication — compounded"
 ],
 "advanced": [
  "Public Domain Resource Finder (Signature): Advanced: Leading Through Story — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Facilitation Mastery — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Mediation Skills — advanced",
  "Public Domain Resource Finder (Signature): Advanced: The Interview Art — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Speechwriting — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Building a Platform — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Communication Audits — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Teaching Communication — advanced",
  "Public Domain Resource Finder (Signature): Advanced: The Lifetime Communicator — advanced",
  "Public Domain Resource Finder (Signature): Advanced: Communication Ethics — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Public Domain Resource Finder Signature Database — structural study\n"
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
var gen={version:'jahdb-public-domain-resource-finder-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-domain-resource-finder-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
