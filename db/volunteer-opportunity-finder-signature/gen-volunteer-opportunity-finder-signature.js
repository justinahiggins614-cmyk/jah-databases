(function(){'use strict';
/* JAH The Volunteer Opportunity Finder Signature Database generator — jahdb-volunteer-opportunity-finder-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VOFS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Volunteer Opportunity Finder (Signature): Knowing What Exists — foundations",
  "Volunteer Opportunity Finder (Signature): Eligibility in Plain Terms — foundations",
  "Volunteer Opportunity Finder (Signature): The Big Four Documents — foundations",
  "Volunteer Opportunity Finder (Signature): Applying Without Errors — foundations",
  "Volunteer Opportunity Finder (Signature): Interviews and Verifications — foundations",
  "Volunteer Opportunity Finder (Signature): When You Are Denied — foundations",
  "Volunteer Opportunity Finder (Signature): Renewals and Reporting Changes — foundations",
  "Volunteer Opportunity Finder (Signature): Combining Multiple Programs — foundations",
  "Volunteer Opportunity Finder (Signature): Emergency Help Fast — foundations",
  "Volunteer Opportunity Finder (Signature): Help for Seniors — foundations",
  "Volunteer Opportunity Finder (Signature): Help for Families With Kids — foundations",
  "Volunteer Opportunity Finder (Signature): Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Volunteer Opportunity Finder (Signature): Help for Veterans — compounded",
  "Volunteer Opportunity Finder (Signature): Rural Access Strategies — compounded",
  "Volunteer Opportunity Finder (Signature): Language Access — compounded",
  "Volunteer Opportunity Finder (Signature): Avoiding Benefit Scams — compounded",
  "Volunteer Opportunity Finder (Signature): Working While Receiving Help — compounded",
  "Volunteer Opportunity Finder (Signature): Childcare Specifics — compounded",
  "Volunteer Opportunity Finder (Signature): Housing-Adjacent Help — compounded",
  "Volunteer Opportunity Finder (Signature): Food-Adjacent Help — compounded",
  "Volunteer Opportunity Finder (Signature): Health Coverage Navigation — compounded",
  "Volunteer Opportunity Finder (Signature): Transportation to Services — compounded",
  "Volunteer Opportunity Finder (Signature): Advanced: Appeals Mastery — compounded",
  "Volunteer Opportunity Finder (Signature): Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Volunteer Opportunity Finder (Signature): Advanced: Coordinating a Case — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Policy Change Tracking — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Helping Others Apply — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Community Needs Assessment — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Building a Help Network — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Data and Dignity — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Disaster Response — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Systems Advocacy — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Running a Nonprofit Program — advanced",
  "Volunteer Opportunity Finder (Signature): Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Volunteer Opportunity Finder Signature Database — structural study\n"
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
var gen={version:'jahdb-volunteer-opportunity-finder-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('volunteer-opportunity-finder-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
