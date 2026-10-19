(function(){'use strict';
/* JAH The First Responder Resource Directory Signature Database generator — jahdb-first-responder-resource-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRRDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "First Responder Resource Directory (Signature): What You Are Protecting — foundations",
  "First Responder Resource Directory (Signature): Thinking Like an Attacker — foundations",
  "First Responder Resource Directory (Signature): The Unsexy Basics — foundations",
  "First Responder Resource Directory (Signature): Passwords Done Right — foundations",
  "First Responder Resource Directory (Signature): Spotting Phishing — foundations",
  "First Responder Resource Directory (Signature): Securing Your Devices — foundations",
  "First Responder Resource Directory (Signature): Home Network Security — foundations",
  "First Responder Resource Directory (Signature): Backups That Save You — foundations",
  "First Responder Resource Directory (Signature): Privacy Settings Audit — foundations",
  "First Responder Resource Directory (Signature): Social Engineering Defense — foundations",
  "First Responder Resource Directory (Signature): Physical Security Basics — foundations",
  "First Responder Resource Directory (Signature): Emergency Kit Essentials — foundations"
 ],
 "compounded": [
  "First Responder Resource Directory (Signature): Family Emergency Plan — compounded",
  "First Responder Resource Directory (Signature): First Aid Readiness — compounded",
  "First Responder Resource Directory (Signature): Finding Real Responders — compounded",
  "First Responder Resource Directory (Signature): When to Call for Help — compounded",
  "First Responder Resource Directory (Signature): After an Incident — compounded",
  "First Responder Resource Directory (Signature): Helping Neighbors Prepare — compounded",
  "First Responder Resource Directory (Signature): Workplace Preparedness — compounded",
  "First Responder Resource Directory (Signature): Travel Safety — compounded",
  "First Responder Resource Directory (Signature): Kids and Safety — compounded",
  "First Responder Resource Directory (Signature): Seniors and Safety — compounded",
  "First Responder Resource Directory (Signature): Advanced: Threat Modeling — compounded",
  "First Responder Resource Directory (Signature): Advanced: Incident Response Plans — compounded"
 ],
 "advanced": [
  "First Responder Resource Directory (Signature): Advanced: Business Continuity — advanced",
  "First Responder Resource Directory (Signature): Advanced: Resilience Assessment — advanced",
  "First Responder Resource Directory (Signature): Advanced: Supply Chain Security — advanced",
  "First Responder Resource Directory (Signature): Advanced: Leading Preparedness — advanced",
  "First Responder Resource Directory (Signature): Advanced: Crisis Communication — advanced",
  "First Responder Resource Directory (Signature): Advanced: Recovery Operations — advanced",
  "First Responder Resource Directory (Signature): Advanced: Exercises and Drills — advanced",
  "First Responder Resource Directory (Signature): Advanced: Community Resilience — advanced",
  "First Responder Resource Directory (Signature): Advanced: Teaching Preparedness — advanced",
  "First Responder Resource Directory (Signature): Advanced: The Resilient Life — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The First Responder Resource Directory Signature Database — structural study\n"
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
var gen={version:'jahdb-first-responder-resource-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('first-responder-resource-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
