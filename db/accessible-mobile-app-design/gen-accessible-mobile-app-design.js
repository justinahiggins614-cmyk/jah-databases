(function(){'use strict';
/* JAH The Accessible Mobile App Design Database generator — jahdb-accessible-mobile-app-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AMAD-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Accessible Mobile App Design: Seeing Barriers Clearly — foundations",
  "Accessible Mobile App Design: The Standards Map — foundations",
  "Accessible Mobile App Design: Keyboard-First Testing — foundations",
  "Accessible Mobile App Design: Screen Reader Basics — foundations",
  "Accessible Mobile App Design: Color and Contrast — foundations",
  "Accessible Mobile App Design: Captions Done Right — foundations",
  "Accessible Mobile App Design: Transcripts That Help — foundations",
  "Accessible Mobile App Design: Plain Language Power — foundations",
  "Accessible Mobile App Design: Forms Without Tears — foundations",
  "Accessible Mobile App Design: Navigation That Orients — foundations",
  "Accessible Mobile App Design: Images With Purpose — foundations",
  "Accessible Mobile App Design: Video Accessibility — foundations"
 ],
 "compounded": [
  "Accessible Mobile App Design: Audio Accessibility — compounded",
  "Accessible Mobile App Design: Cognitive Accessibility — compounded",
  "Accessible Mobile App Design: Motor Accessibility — compounded",
  "Accessible Mobile App Design: Hearing Accessibility — compounded",
  "Accessible Mobile App Design: Vision Accessibility — compounded",
  "Accessible Mobile App Design: Speech Accessibility — compounded",
  "Accessible Mobile App Design: Assistive Tech Compatibility — compounded",
  "Accessible Mobile App Design: Accessible Documents — compounded",
  "Accessible Mobile App Design: Accessible Events — compounded",
  "Accessible Mobile App Design: Emergency Accessibility — compounded",
  "Accessible Mobile App Design: Advanced: Accessibility Audits — compounded",
  "Accessible Mobile App Design: Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Accessible Mobile App Design: Advanced: Design Systems Accessibly — advanced",
  "Accessible Mobile App Design: Advanced: Procurement Power — advanced",
  "Accessible Mobile App Design: Advanced: Legal Landscape — advanced",
  "Accessible Mobile App Design: Advanced: Inclusive Research — advanced",
  "Accessible Mobile App Design: Advanced: Accessibility Metrics — advanced",
  "Accessible Mobile App Design: Advanced: Culture Change — advanced",
  "Accessible Mobile App Design: Advanced: Emerging Tech Access — advanced",
  "Accessible Mobile App Design: Advanced: Global Accessibility — advanced",
  "Accessible Mobile App Design: Advanced: Teaching Accessibility — advanced",
  "Accessible Mobile App Design: Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Mobile App Design Database — structural study\n"
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
var gen={version:'jahdb-accessible-mobile-app-design-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-mobile-app-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
