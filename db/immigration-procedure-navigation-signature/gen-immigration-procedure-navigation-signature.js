(function(){'use strict';
/* JAH The Immigration Procedure Navigation Signature Database generator — jahdb-immigration-procedure-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IPNS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Immigration Procedure Navigation (Signature): The Law in Plain Words — foundations",
  "Immigration Procedure Navigation (Signature): Your Rights, Stated Simply — foundations",
  "Immigration Procedure Navigation (Signature): Forms: Which Ones and How — foundations",
  "Immigration Procedure Navigation (Signature): Deadlines That Decide Cases — foundations",
  "Immigration Procedure Navigation (Signature): Evidence and Documentation — foundations",
  "Immigration Procedure Navigation (Signature): Filing and Fees — foundations",
  "Immigration Procedure Navigation (Signature): What Happens at Each Stage — foundations",
  "Immigration Procedure Navigation (Signature): Representing Yourself: Basics — foundations",
  "Immigration Procedure Navigation (Signature): When You Must Hire a Lawyer — foundations",
  "Immigration Procedure Navigation (Signature): Free and Low-Cost Legal Help — foundations",
  "Immigration Procedure Navigation (Signature): Common Mistakes That Lose Cases — foundations",
  "Immigration Procedure Navigation (Signature): Negotiation and Settlement — foundations"
 ],
 "compounded": [
  "Immigration Procedure Navigation (Signature): Appeals and Second Chances — compounded",
  "Immigration Procedure Navigation (Signature): Records, Background, and Privacy — compounded",
  "Immigration Procedure Navigation (Signature): Dealing With Agencies — compounded",
  "Immigration Procedure Navigation (Signature): Mediation and Alternatives — compounded",
  "Immigration Procedure Navigation (Signature): Costs: Real Numbers — compounded",
  "Immigration Procedure Navigation (Signature): Timelines: How Long It Takes — compounded",
  "Immigration Procedure Navigation (Signature): Protecting Yourself Going Forward — compounded",
  "Immigration Procedure Navigation (Signature): Helping Others Navigate This — compounded",
  "Immigration Procedure Navigation (Signature): Language Access Rights — compounded",
  "Immigration Procedure Navigation (Signature): Digital Filing and Remote Hearings — compounded",
  "Immigration Procedure Navigation (Signature): Advanced: Reading Statutes — compounded",
  "Immigration Procedure Navigation (Signature): Advanced: Case Law Basics — compounded"
 ],
 "advanced": [
  "Immigration Procedure Navigation (Signature): Advanced: Building a Case File — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Expert Witnesses — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Class and Collective Action — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Cross-Jurisdiction Issues — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Legislative Change Tracking — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Teaching Legal Literacy — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Systemic Advocacy — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Ethics for Non-Lawyers Helping — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Building Precedent — advanced",
  "Immigration Procedure Navigation (Signature): Advanced: Restorative Approaches — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Immigration Procedure Navigation Signature Database — structural study\n"
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
var gen={version:'jahdb-immigration-procedure-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('immigration-procedure-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
