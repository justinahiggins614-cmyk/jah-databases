(function(){'use strict';
/* JAH The Immigration Procedure Navigation Database generator — jahdb-immigration-procedure-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IPN-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Immigration Procedure Navigation: The Law in Plain Words — foundations",
  "Immigration Procedure Navigation: Your Rights, Stated Simply — foundations",
  "Immigration Procedure Navigation: Forms: Which Ones and How — foundations",
  "Immigration Procedure Navigation: Deadlines That Decide Cases — foundations",
  "Immigration Procedure Navigation: Evidence and Documentation — foundations",
  "Immigration Procedure Navigation: Filing and Fees — foundations",
  "Immigration Procedure Navigation: What Happens at Each Stage — foundations",
  "Immigration Procedure Navigation: Representing Yourself: Basics — foundations",
  "Immigration Procedure Navigation: When You Must Hire a Lawyer — foundations",
  "Immigration Procedure Navigation: Free and Low-Cost Legal Help — foundations",
  "Immigration Procedure Navigation: Common Mistakes That Lose Cases — foundations",
  "Immigration Procedure Navigation: Negotiation and Settlement — foundations"
 ],
 "compounded": [
  "Immigration Procedure Navigation: Appeals and Second Chances — compounded",
  "Immigration Procedure Navigation: Records, Background, and Privacy — compounded",
  "Immigration Procedure Navigation: Dealing With Agencies — compounded",
  "Immigration Procedure Navigation: Mediation and Alternatives — compounded",
  "Immigration Procedure Navigation: Costs: Real Numbers — compounded",
  "Immigration Procedure Navigation: Timelines: How Long It Takes — compounded",
  "Immigration Procedure Navigation: Protecting Yourself Going Forward — compounded",
  "Immigration Procedure Navigation: Helping Others Navigate This — compounded",
  "Immigration Procedure Navigation: Language Access Rights — compounded",
  "Immigration Procedure Navigation: Digital Filing and Remote Hearings — compounded",
  "Immigration Procedure Navigation: Advanced: Reading Statutes — compounded",
  "Immigration Procedure Navigation: Advanced: Case Law Basics — compounded"
 ],
 "advanced": [
  "Immigration Procedure Navigation: Advanced: Building a Case File — advanced",
  "Immigration Procedure Navigation: Advanced: Expert Witnesses — advanced",
  "Immigration Procedure Navigation: Advanced: Class and Collective Action — advanced",
  "Immigration Procedure Navigation: Advanced: Cross-Jurisdiction Issues — advanced",
  "Immigration Procedure Navigation: Advanced: Legislative Change Tracking — advanced",
  "Immigration Procedure Navigation: Advanced: Teaching Legal Literacy — advanced",
  "Immigration Procedure Navigation: Advanced: Systemic Advocacy — advanced",
  "Immigration Procedure Navigation: Advanced: Ethics for Non-Lawyers Helping — advanced",
  "Immigration Procedure Navigation: Advanced: Building Precedent — advanced",
  "Immigration Procedure Navigation: Advanced: Restorative Approaches — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Immigration Procedure Navigation Database — structural study\n"
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
var gen={version:'jahdb-immigration-procedure-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('immigration-procedure-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
