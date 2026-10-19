(function(){'use strict';
/* JAH The Domestic Violence Support Directory Database generator — jahdb-domestic-violence-support-directory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DVSD-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Domestic Violence Support Directory: Knowing What Exists — foundations",
  "Domestic Violence Support Directory: Eligibility in Plain Terms — foundations",
  "Domestic Violence Support Directory: The Big Four Documents — foundations",
  "Domestic Violence Support Directory: Applying Without Errors — foundations",
  "Domestic Violence Support Directory: Interviews and Verifications — foundations",
  "Domestic Violence Support Directory: When You Are Denied — foundations",
  "Domestic Violence Support Directory: Renewals and Reporting Changes — foundations",
  "Domestic Violence Support Directory: Combining Multiple Programs — foundations",
  "Domestic Violence Support Directory: Emergency Help Fast — foundations",
  "Domestic Violence Support Directory: Help for Seniors — foundations",
  "Domestic Violence Support Directory: Help for Families With Kids — foundations",
  "Domestic Violence Support Directory: Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Domestic Violence Support Directory: Help for Veterans — compounded",
  "Domestic Violence Support Directory: Rural Access Strategies — compounded",
  "Domestic Violence Support Directory: Language Access — compounded",
  "Domestic Violence Support Directory: Avoiding Benefit Scams — compounded",
  "Domestic Violence Support Directory: Working While Receiving Help — compounded",
  "Domestic Violence Support Directory: Childcare Specifics — compounded",
  "Domestic Violence Support Directory: Housing-Adjacent Help — compounded",
  "Domestic Violence Support Directory: Food-Adjacent Help — compounded",
  "Domestic Violence Support Directory: Health Coverage Navigation — compounded",
  "Domestic Violence Support Directory: Transportation to Services — compounded",
  "Domestic Violence Support Directory: Advanced: Appeals Mastery — compounded",
  "Domestic Violence Support Directory: Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Domestic Violence Support Directory: Advanced: Coordinating a Case — advanced",
  "Domestic Violence Support Directory: Advanced: Policy Change Tracking — advanced",
  "Domestic Violence Support Directory: Advanced: Helping Others Apply — advanced",
  "Domestic Violence Support Directory: Advanced: Community Needs Assessment — advanced",
  "Domestic Violence Support Directory: Advanced: Building a Help Network — advanced",
  "Domestic Violence Support Directory: Advanced: Data and Dignity — advanced",
  "Domestic Violence Support Directory: Advanced: Disaster Response — advanced",
  "Domestic Violence Support Directory: Advanced: Systems Advocacy — advanced",
  "Domestic Violence Support Directory: Advanced: Running a Nonprofit Program — advanced",
  "Domestic Violence Support Directory: Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Domestic Violence Support Directory Database — structural study\n"
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
var gen={version:'jahdb-domestic-violence-support-directory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('domestic-violence-support-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
