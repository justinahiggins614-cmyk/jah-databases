(function(){'use strict';
/* JAH The Civic Participation Guide Signature Database generator — jahdb-civic-participation-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPGS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Civic Participation Guide (Signature): The Law in Plain Words — foundations",
  "Civic Participation Guide (Signature): Your Rights, Stated Simply — foundations",
  "Civic Participation Guide (Signature): Forms: Which Ones and How — foundations",
  "Civic Participation Guide (Signature): Deadlines That Decide Cases — foundations",
  "Civic Participation Guide (Signature): Evidence and Documentation — foundations",
  "Civic Participation Guide (Signature): Filing and Fees — foundations",
  "Civic Participation Guide (Signature): What Happens at Each Stage — foundations",
  "Civic Participation Guide (Signature): Representing Yourself: Basics — foundations",
  "Civic Participation Guide (Signature): When You Must Hire a Lawyer — foundations",
  "Civic Participation Guide (Signature): Free and Low-Cost Legal Help — foundations",
  "Civic Participation Guide (Signature): Common Mistakes That Lose Cases — foundations",
  "Civic Participation Guide (Signature): Negotiation and Settlement — foundations"
 ],
 "compounded": [
  "Civic Participation Guide (Signature): Appeals and Second Chances — compounded",
  "Civic Participation Guide (Signature): Records, Background, and Privacy — compounded",
  "Civic Participation Guide (Signature): Dealing With Agencies — compounded",
  "Civic Participation Guide (Signature): Mediation and Alternatives — compounded",
  "Civic Participation Guide (Signature): Costs: Real Numbers — compounded",
  "Civic Participation Guide (Signature): Timelines: How Long It Takes — compounded",
  "Civic Participation Guide (Signature): Protecting Yourself Going Forward — compounded",
  "Civic Participation Guide (Signature): Helping Others Navigate This — compounded",
  "Civic Participation Guide (Signature): Language Access Rights — compounded",
  "Civic Participation Guide (Signature): Digital Filing and Remote Hearings — compounded",
  "Civic Participation Guide (Signature): Advanced: Reading Statutes — compounded",
  "Civic Participation Guide (Signature): Advanced: Case Law Basics — compounded"
 ],
 "advanced": [
  "Civic Participation Guide (Signature): Advanced: Building a Case File — advanced",
  "Civic Participation Guide (Signature): Advanced: Expert Witnesses — advanced",
  "Civic Participation Guide (Signature): Advanced: Class and Collective Action — advanced",
  "Civic Participation Guide (Signature): Advanced: Cross-Jurisdiction Issues — advanced",
  "Civic Participation Guide (Signature): Advanced: Legislative Change Tracking — advanced",
  "Civic Participation Guide (Signature): Advanced: Teaching Legal Literacy — advanced",
  "Civic Participation Guide (Signature): Advanced: Systemic Advocacy — advanced",
  "Civic Participation Guide (Signature): Advanced: Ethics for Non-Lawyers Helping — advanced",
  "Civic Participation Guide (Signature): Advanced: Building Precedent — advanced",
  "Civic Participation Guide (Signature): Advanced: Restorative Approaches — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Civic Participation Guide Signature Database — structural study\n"
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
var gen={version:'jahdb-civic-participation-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('civic-participation-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
