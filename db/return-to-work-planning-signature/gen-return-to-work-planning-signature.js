(function(){'use strict';
/* JAH The Return-to-Work Planning Signature Database generator — jahdb-return-to-work-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTWPS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Return-to-Work Planning (Signature): Mapping Your Real Skills — foundations",
  "Return-to-Work Planning (Signature): Reading Job Postings Critically — foundations",
  "Return-to-Work Planning (Signature): Resumes That Get Read — foundations",
  "Return-to-Work Planning (Signature): Interview Preparation System — foundations",
  "Return-to-Work Planning (Signature): Salary Research and Ranges — foundations",
  "Return-to-Work Planning (Signature): Negotiating Offers — foundations",
  "Return-to-Work Planning (Signature): Evaluating Benefits Deeply — foundations",
  "Return-to-Work Planning (Signature): Onboarding: First 90 Days — foundations",
  "Return-to-Work Planning (Signature): Performance Reviews That Help — foundations",
  "Return-to-Work Planning (Signature): Asking for Raises and Promotions — foundations",
  "Return-to-Work Planning (Signature): Changing Careers Safely — foundations",
  "Return-to-Work Planning (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Return-to-Work Planning (Signature): Workplace Rights Basics — compounded",
  "Return-to-Work Planning (Signature): Handling Difficult Bosses — compounded",
  "Return-to-Work Planning (Signature): Work-Life Boundaries — compounded",
  "Return-to-Work Planning (Signature): Building a Professional Network — compounded",
  "Return-to-Work Planning (Signature): Personal Branding Honestly — compounded",
  "Return-to-Work Planning (Signature): Remote Work Success — compounded",
  "Return-to-Work Planning (Signature): Dealing With Job Loss — compounded",
  "Return-to-Work Planning (Signature): References and Background Checks — compounded",
  "Return-to-Work Planning (Signature): Contracts and Non-Competes — compounded",
  "Return-to-Work Planning (Signature): Planning Parental and Medical Leave — compounded",
  "Return-to-Work Planning (Signature): Advanced: Becoming the Expert — compounded",
  "Return-to-Work Planning (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Return-to-Work Planning (Signature): Advanced: Negotiation Mastery — advanced",
  "Return-to-Work Planning (Signature): Advanced: Building a Practice or Firm — advanced",
  "Return-to-Work Planning (Signature): Advanced: Board and Advisory Roles — advanced",
  "Return-to-Work Planning (Signature): Advanced: Career Portfolio Design — advanced",
  "Return-to-Work Planning (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Return-to-Work Planning (Signature): Advanced: Navigating Politics — advanced",
  "Return-to-Work Planning (Signature): Advanced: The Encore Career — advanced",
  "Return-to-Work Planning (Signature): Advanced: Legacy at Work — advanced",
  "Return-to-Work Planning (Signature): Advanced: When to Walk Away — advanced",
  "Return-to-Work Planning (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Return-to-Work Planning Signature Database — structural study\n"
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
var gen={version:'jahdb-return-to-work-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('return-to-work-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
