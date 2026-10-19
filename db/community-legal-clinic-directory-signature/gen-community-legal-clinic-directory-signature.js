(function(){'use strict';
/* JAH The Community Legal Clinic Directory Signature Database generator — jahdb-community-legal-clinic-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLCDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Community Legal Clinic Directory (Signature): Knowing What Exists — foundations",
  "Community Legal Clinic Directory (Signature): Eligibility in Plain Terms — foundations",
  "Community Legal Clinic Directory (Signature): The Big Four Documents — foundations",
  "Community Legal Clinic Directory (Signature): Applying Without Errors — foundations",
  "Community Legal Clinic Directory (Signature): Interviews and Verifications — foundations",
  "Community Legal Clinic Directory (Signature): When You Are Denied — foundations",
  "Community Legal Clinic Directory (Signature): Renewals and Reporting Changes — foundations",
  "Community Legal Clinic Directory (Signature): Combining Multiple Programs — foundations",
  "Community Legal Clinic Directory (Signature): Emergency Help Fast — foundations",
  "Community Legal Clinic Directory (Signature): Help for Seniors — foundations",
  "Community Legal Clinic Directory (Signature): Help for Families With Kids — foundations",
  "Community Legal Clinic Directory (Signature): Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Community Legal Clinic Directory (Signature): Help for Veterans — compounded",
  "Community Legal Clinic Directory (Signature): Rural Access Strategies — compounded",
  "Community Legal Clinic Directory (Signature): Language Access — compounded",
  "Community Legal Clinic Directory (Signature): Avoiding Benefit Scams — compounded",
  "Community Legal Clinic Directory (Signature): Working While Receiving Help — compounded",
  "Community Legal Clinic Directory (Signature): Childcare Specifics — compounded",
  "Community Legal Clinic Directory (Signature): Housing-Adjacent Help — compounded",
  "Community Legal Clinic Directory (Signature): Food-Adjacent Help — compounded",
  "Community Legal Clinic Directory (Signature): Health Coverage Navigation — compounded",
  "Community Legal Clinic Directory (Signature): Transportation to Services — compounded",
  "Community Legal Clinic Directory (Signature): Advanced: Appeals Mastery — compounded",
  "Community Legal Clinic Directory (Signature): Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Community Legal Clinic Directory (Signature): Advanced: Coordinating a Case — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Policy Change Tracking — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Helping Others Apply — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Community Needs Assessment — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Building a Help Network — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Data and Dignity — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Disaster Response — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Systems Advocacy — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Running a Nonprofit Program — advanced",
  "Community Legal Clinic Directory (Signature): Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Community Legal Clinic Directory Signature Database — structural study\n"
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
var gen={version:'jahdb-community-legal-clinic-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-legal-clinic-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
