(function(){'use strict';
/* JAH The Accessible Recreation Directory Database generator — jahdb-accessible-recreation-directory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARD-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Accessible Recreation Directory: Seeing Barriers Clearly — foundations",
  "Accessible Recreation Directory: The Standards Map — foundations",
  "Accessible Recreation Directory: Keyboard-First Testing — foundations",
  "Accessible Recreation Directory: Screen Reader Basics — foundations",
  "Accessible Recreation Directory: Color and Contrast — foundations",
  "Accessible Recreation Directory: Captions Done Right — foundations",
  "Accessible Recreation Directory: Transcripts That Help — foundations",
  "Accessible Recreation Directory: Plain Language Power — foundations",
  "Accessible Recreation Directory: Forms Without Tears — foundations",
  "Accessible Recreation Directory: Navigation That Orients — foundations",
  "Accessible Recreation Directory: Images With Purpose — foundations",
  "Accessible Recreation Directory: Video Accessibility — foundations"
 ],
 "compounded": [
  "Accessible Recreation Directory: Audio Accessibility — compounded",
  "Accessible Recreation Directory: Cognitive Accessibility — compounded",
  "Accessible Recreation Directory: Motor Accessibility — compounded",
  "Accessible Recreation Directory: Hearing Accessibility — compounded",
  "Accessible Recreation Directory: Vision Accessibility — compounded",
  "Accessible Recreation Directory: Speech Accessibility — compounded",
  "Accessible Recreation Directory: Assistive Tech Compatibility — compounded",
  "Accessible Recreation Directory: Accessible Documents — compounded",
  "Accessible Recreation Directory: Accessible Events — compounded",
  "Accessible Recreation Directory: Emergency Accessibility — compounded",
  "Accessible Recreation Directory: Advanced: Accessibility Audits — compounded",
  "Accessible Recreation Directory: Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Accessible Recreation Directory: Advanced: Design Systems Accessibly — advanced",
  "Accessible Recreation Directory: Advanced: Procurement Power — advanced",
  "Accessible Recreation Directory: Advanced: Legal Landscape — advanced",
  "Accessible Recreation Directory: Advanced: Inclusive Research — advanced",
  "Accessible Recreation Directory: Advanced: Accessibility Metrics — advanced",
  "Accessible Recreation Directory: Advanced: Culture Change — advanced",
  "Accessible Recreation Directory: Advanced: Emerging Tech Access — advanced",
  "Accessible Recreation Directory: Advanced: Global Accessibility — advanced",
  "Accessible Recreation Directory: Advanced: Teaching Accessibility — advanced",
  "Accessible Recreation Directory: Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Recreation Directory Database — structural study\n"
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
var gen={version:'jahdb-accessible-recreation-directory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-recreation-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
