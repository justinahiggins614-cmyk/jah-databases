(function(){'use strict';
/* JAH The Personal Privacy Protection Database generator — jahdb-personal-privacy-protection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Personal Privacy Protection: What You Are Protecting — foundations",
  "Personal Privacy Protection: Thinking Like an Attacker — foundations",
  "Personal Privacy Protection: The Unsexy Basics — foundations",
  "Personal Privacy Protection: Passwords Done Right — foundations",
  "Personal Privacy Protection: Spotting Phishing — foundations",
  "Personal Privacy Protection: Securing Your Devices — foundations",
  "Personal Privacy Protection: Home Network Security — foundations",
  "Personal Privacy Protection: Backups That Save You — foundations",
  "Personal Privacy Protection: Privacy Settings Audit — foundations",
  "Personal Privacy Protection: Social Engineering Defense — foundations",
  "Personal Privacy Protection: Physical Security Basics — foundations",
  "Personal Privacy Protection: Emergency Kit Essentials — foundations"
 ],
 "compounded": [
  "Personal Privacy Protection: Family Emergency Plan — compounded",
  "Personal Privacy Protection: First Aid Readiness — compounded",
  "Personal Privacy Protection: Finding Real Responders — compounded",
  "Personal Privacy Protection: When to Call for Help — compounded",
  "Personal Privacy Protection: After an Incident — compounded",
  "Personal Privacy Protection: Helping Neighbors Prepare — compounded",
  "Personal Privacy Protection: Workplace Preparedness — compounded",
  "Personal Privacy Protection: Travel Safety — compounded",
  "Personal Privacy Protection: Kids and Safety — compounded",
  "Personal Privacy Protection: Seniors and Safety — compounded",
  "Personal Privacy Protection: Advanced: Threat Modeling — compounded",
  "Personal Privacy Protection: Advanced: Incident Response Plans — compounded"
 ],
 "advanced": [
  "Personal Privacy Protection: Advanced: Business Continuity — advanced",
  "Personal Privacy Protection: Advanced: Resilience Assessment — advanced",
  "Personal Privacy Protection: Advanced: Supply Chain Security — advanced",
  "Personal Privacy Protection: Advanced: Leading Preparedness — advanced",
  "Personal Privacy Protection: Advanced: Crisis Communication — advanced",
  "Personal Privacy Protection: Advanced: Recovery Operations — advanced",
  "Personal Privacy Protection: Advanced: Exercises and Drills — advanced",
  "Personal Privacy Protection: Advanced: Community Resilience — advanced",
  "Personal Privacy Protection: Advanced: Teaching Preparedness — advanced",
  "Personal Privacy Protection: Advanced: The Resilient Life — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Personal Privacy Protection Database — structural study\n"
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
var gen={version:'jahdb-personal-privacy-protection-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-privacy-protection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
