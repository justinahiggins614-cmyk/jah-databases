(function(){'use strict';
/* JAH The Organizational Resilience Assessment Database generator — jahdb-organizational-resilience-assessment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ORA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Organizational Resilience Assessment: What You Are Protecting — foundations",
  "Organizational Resilience Assessment: Thinking Like an Attacker — foundations",
  "Organizational Resilience Assessment: The Unsexy Basics — foundations",
  "Organizational Resilience Assessment: Passwords Done Right — foundations",
  "Organizational Resilience Assessment: Spotting Phishing — foundations",
  "Organizational Resilience Assessment: Securing Your Devices — foundations",
  "Organizational Resilience Assessment: Home Network Security — foundations",
  "Organizational Resilience Assessment: Backups That Save You — foundations",
  "Organizational Resilience Assessment: Privacy Settings Audit — foundations",
  "Organizational Resilience Assessment: Social Engineering Defense — foundations",
  "Organizational Resilience Assessment: Physical Security Basics — foundations",
  "Organizational Resilience Assessment: Emergency Kit Essentials — foundations"
 ],
 "compounded": [
  "Organizational Resilience Assessment: Family Emergency Plan — compounded",
  "Organizational Resilience Assessment: First Aid Readiness — compounded",
  "Organizational Resilience Assessment: Finding Real Responders — compounded",
  "Organizational Resilience Assessment: When to Call for Help — compounded",
  "Organizational Resilience Assessment: After an Incident — compounded",
  "Organizational Resilience Assessment: Helping Neighbors Prepare — compounded",
  "Organizational Resilience Assessment: Workplace Preparedness — compounded",
  "Organizational Resilience Assessment: Travel Safety — compounded",
  "Organizational Resilience Assessment: Kids and Safety — compounded",
  "Organizational Resilience Assessment: Seniors and Safety — compounded",
  "Organizational Resilience Assessment: Advanced: Threat Modeling — compounded",
  "Organizational Resilience Assessment: Advanced: Incident Response Plans — compounded"
 ],
 "advanced": [
  "Organizational Resilience Assessment: Advanced: Business Continuity — advanced",
  "Organizational Resilience Assessment: Advanced: Resilience Assessment — advanced",
  "Organizational Resilience Assessment: Advanced: Supply Chain Security — advanced",
  "Organizational Resilience Assessment: Advanced: Leading Preparedness — advanced",
  "Organizational Resilience Assessment: Advanced: Crisis Communication — advanced",
  "Organizational Resilience Assessment: Advanced: Recovery Operations — advanced",
  "Organizational Resilience Assessment: Advanced: Exercises and Drills — advanced",
  "Organizational Resilience Assessment: Advanced: Community Resilience — advanced",
  "Organizational Resilience Assessment: Advanced: Teaching Preparedness — advanced",
  "Organizational Resilience Assessment: Advanced: The Resilient Life — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Organizational Resilience Assessment Database — structural study\n"
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
var gen={version:'jahdb-organizational-resilience-assessment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('organizational-resilience-assessment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
