(function(){'use strict';
/* JAH The Occupation Requirements Signature Database generator — jahdb-occupation-requirements-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ORS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Occupation Requirements (Signature): Mapping Your Real Skills — foundations",
  "Occupation Requirements (Signature): Reading Job Postings Critically — foundations",
  "Occupation Requirements (Signature): Resumes That Get Read — foundations",
  "Occupation Requirements (Signature): Interview Preparation System — foundations",
  "Occupation Requirements (Signature): Salary Research and Ranges — foundations",
  "Occupation Requirements (Signature): Negotiating Offers — foundations",
  "Occupation Requirements (Signature): Evaluating Benefits Deeply — foundations",
  "Occupation Requirements (Signature): Onboarding: First 90 Days — foundations",
  "Occupation Requirements (Signature): Performance Reviews That Help — foundations",
  "Occupation Requirements (Signature): Asking for Raises and Promotions — foundations",
  "Occupation Requirements (Signature): Changing Careers Safely — foundations",
  "Occupation Requirements (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Occupation Requirements (Signature): Workplace Rights Basics — compounded",
  "Occupation Requirements (Signature): Handling Difficult Bosses — compounded",
  "Occupation Requirements (Signature): Work-Life Boundaries — compounded",
  "Occupation Requirements (Signature): Building a Professional Network — compounded",
  "Occupation Requirements (Signature): Personal Branding Honestly — compounded",
  "Occupation Requirements (Signature): Remote Work Success — compounded",
  "Occupation Requirements (Signature): Dealing With Job Loss — compounded",
  "Occupation Requirements (Signature): References and Background Checks — compounded",
  "Occupation Requirements (Signature): Contracts and Non-Competes — compounded",
  "Occupation Requirements (Signature): Planning Parental and Medical Leave — compounded",
  "Occupation Requirements (Signature): Advanced: Becoming the Expert — compounded",
  "Occupation Requirements (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Occupation Requirements (Signature): Advanced: Negotiation Mastery — advanced",
  "Occupation Requirements (Signature): Advanced: Building a Practice or Firm — advanced",
  "Occupation Requirements (Signature): Advanced: Board and Advisory Roles — advanced",
  "Occupation Requirements (Signature): Advanced: Career Portfolio Design — advanced",
  "Occupation Requirements (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Occupation Requirements (Signature): Advanced: Navigating Politics — advanced",
  "Occupation Requirements (Signature): Advanced: The Encore Career — advanced",
  "Occupation Requirements (Signature): Advanced: Legacy at Work — advanced",
  "Occupation Requirements (Signature): Advanced: When to Walk Away — advanced",
  "Occupation Requirements (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Occupation Requirements Signature Database — structural study\n"
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
var gen={version:'jahdb-occupation-requirements-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('occupation-requirements-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
