(function(){'use strict';
/* JAH The Community Legal Clinic Directory Database generator — jahdb-community-legal-clinic-directory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLCD-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Community Legal Clinic Directory: Knowing What Exists — foundations",
  "Community Legal Clinic Directory: Eligibility in Plain Terms — foundations",
  "Community Legal Clinic Directory: The Big Four Documents — foundations",
  "Community Legal Clinic Directory: Applying Without Errors — foundations",
  "Community Legal Clinic Directory: Interviews and Verifications — foundations",
  "Community Legal Clinic Directory: When You Are Denied — foundations",
  "Community Legal Clinic Directory: Renewals and Reporting Changes — foundations",
  "Community Legal Clinic Directory: Combining Multiple Programs — foundations",
  "Community Legal Clinic Directory: Emergency Help Fast — foundations",
  "Community Legal Clinic Directory: Help for Seniors — foundations",
  "Community Legal Clinic Directory: Help for Families With Kids — foundations",
  "Community Legal Clinic Directory: Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Community Legal Clinic Directory: Help for Veterans — compounded",
  "Community Legal Clinic Directory: Rural Access Strategies — compounded",
  "Community Legal Clinic Directory: Language Access — compounded",
  "Community Legal Clinic Directory: Avoiding Benefit Scams — compounded",
  "Community Legal Clinic Directory: Working While Receiving Help — compounded",
  "Community Legal Clinic Directory: Childcare Specifics — compounded",
  "Community Legal Clinic Directory: Housing-Adjacent Help — compounded",
  "Community Legal Clinic Directory: Food-Adjacent Help — compounded",
  "Community Legal Clinic Directory: Health Coverage Navigation — compounded",
  "Community Legal Clinic Directory: Transportation to Services — compounded",
  "Community Legal Clinic Directory: Advanced: Appeals Mastery — compounded",
  "Community Legal Clinic Directory: Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Community Legal Clinic Directory: Advanced: Coordinating a Case — advanced",
  "Community Legal Clinic Directory: Advanced: Policy Change Tracking — advanced",
  "Community Legal Clinic Directory: Advanced: Helping Others Apply — advanced",
  "Community Legal Clinic Directory: Advanced: Community Needs Assessment — advanced",
  "Community Legal Clinic Directory: Advanced: Building a Help Network — advanced",
  "Community Legal Clinic Directory: Advanced: Data and Dignity — advanced",
  "Community Legal Clinic Directory: Advanced: Disaster Response — advanced",
  "Community Legal Clinic Directory: Advanced: Systems Advocacy — advanced",
  "Community Legal Clinic Directory: Advanced: Running a Nonprofit Program — advanced",
  "Community Legal Clinic Directory: Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Community Legal Clinic Directory Database — structural study\n"
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
var gen={version:'jahdb-community-legal-clinic-directory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-legal-clinic-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
