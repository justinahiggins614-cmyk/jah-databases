(function(){'use strict';
/* JAH The Personal Privacy Protection Signature Database generator — jahdb-personal-privacy-protection-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPPS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Personal Privacy Protection (Signature): What You Are Protecting — foundations",
  "Personal Privacy Protection (Signature): Thinking Like an Attacker — foundations",
  "Personal Privacy Protection (Signature): The Unsexy Basics — foundations",
  "Personal Privacy Protection (Signature): Passwords Done Right — foundations",
  "Personal Privacy Protection (Signature): Spotting Phishing — foundations",
  "Personal Privacy Protection (Signature): Securing Your Devices — foundations",
  "Personal Privacy Protection (Signature): Home Network Security — foundations",
  "Personal Privacy Protection (Signature): Backups That Save You — foundations",
  "Personal Privacy Protection (Signature): Privacy Settings Audit — foundations",
  "Personal Privacy Protection (Signature): Social Engineering Defense — foundations",
  "Personal Privacy Protection (Signature): Physical Security Basics — foundations",
  "Personal Privacy Protection (Signature): Emergency Kit Essentials — foundations"
 ],
 "compounded": [
  "Personal Privacy Protection (Signature): Family Emergency Plan — compounded",
  "Personal Privacy Protection (Signature): First Aid Readiness — compounded",
  "Personal Privacy Protection (Signature): Finding Real Responders — compounded",
  "Personal Privacy Protection (Signature): When to Call for Help — compounded",
  "Personal Privacy Protection (Signature): After an Incident — compounded",
  "Personal Privacy Protection (Signature): Helping Neighbors Prepare — compounded",
  "Personal Privacy Protection (Signature): Workplace Preparedness — compounded",
  "Personal Privacy Protection (Signature): Travel Safety — compounded",
  "Personal Privacy Protection (Signature): Kids and Safety — compounded",
  "Personal Privacy Protection (Signature): Seniors and Safety — compounded",
  "Personal Privacy Protection (Signature): Advanced: Threat Modeling — compounded",
  "Personal Privacy Protection (Signature): Advanced: Incident Response Plans — compounded"
 ],
 "advanced": [
  "Personal Privacy Protection (Signature): Advanced: Business Continuity — advanced",
  "Personal Privacy Protection (Signature): Advanced: Resilience Assessment — advanced",
  "Personal Privacy Protection (Signature): Advanced: Supply Chain Security — advanced",
  "Personal Privacy Protection (Signature): Advanced: Leading Preparedness — advanced",
  "Personal Privacy Protection (Signature): Advanced: Crisis Communication — advanced",
  "Personal Privacy Protection (Signature): Advanced: Recovery Operations — advanced",
  "Personal Privacy Protection (Signature): Advanced: Exercises and Drills — advanced",
  "Personal Privacy Protection (Signature): Advanced: Community Resilience — advanced",
  "Personal Privacy Protection (Signature): Advanced: Teaching Preparedness — advanced",
  "Personal Privacy Protection (Signature): Advanced: The Resilient Life — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Personal Privacy Protection Signature Database — structural study\n"
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
var gen={version:'jahdb-personal-privacy-protection-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-privacy-protection-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
