(function(){'use strict';
/* JAH The Mobility Aid Comparison Database generator — jahdb-mobility-aid-comparison-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Mobility Aid Comparison: Seeing Barriers Clearly — foundations",
  "Mobility Aid Comparison: The Standards Map — foundations",
  "Mobility Aid Comparison: Keyboard-First Testing — foundations",
  "Mobility Aid Comparison: Screen Reader Basics — foundations",
  "Mobility Aid Comparison: Color and Contrast — foundations",
  "Mobility Aid Comparison: Captions Done Right — foundations",
  "Mobility Aid Comparison: Transcripts That Help — foundations",
  "Mobility Aid Comparison: Plain Language Power — foundations",
  "Mobility Aid Comparison: Forms Without Tears — foundations",
  "Mobility Aid Comparison: Navigation That Orients — foundations",
  "Mobility Aid Comparison: Images With Purpose — foundations",
  "Mobility Aid Comparison: Video Accessibility — foundations"
 ],
 "compounded": [
  "Mobility Aid Comparison: Audio Accessibility — compounded",
  "Mobility Aid Comparison: Cognitive Accessibility — compounded",
  "Mobility Aid Comparison: Motor Accessibility — compounded",
  "Mobility Aid Comparison: Hearing Accessibility — compounded",
  "Mobility Aid Comparison: Vision Accessibility — compounded",
  "Mobility Aid Comparison: Speech Accessibility — compounded",
  "Mobility Aid Comparison: Assistive Tech Compatibility — compounded",
  "Mobility Aid Comparison: Accessible Documents — compounded",
  "Mobility Aid Comparison: Accessible Events — compounded",
  "Mobility Aid Comparison: Emergency Accessibility — compounded",
  "Mobility Aid Comparison: Advanced: Accessibility Audits — compounded",
  "Mobility Aid Comparison: Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Mobility Aid Comparison: Advanced: Design Systems Accessibly — advanced",
  "Mobility Aid Comparison: Advanced: Procurement Power — advanced",
  "Mobility Aid Comparison: Advanced: Legal Landscape — advanced",
  "Mobility Aid Comparison: Advanced: Inclusive Research — advanced",
  "Mobility Aid Comparison: Advanced: Accessibility Metrics — advanced",
  "Mobility Aid Comparison: Advanced: Culture Change — advanced",
  "Mobility Aid Comparison: Advanced: Emerging Tech Access — advanced",
  "Mobility Aid Comparison: Advanced: Global Accessibility — advanced",
  "Mobility Aid Comparison: Advanced: Teaching Accessibility — advanced",
  "Mobility Aid Comparison: Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Mobility Aid Comparison Database — structural study\n"
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
var gen={version:'jahdb-mobility-aid-comparison-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mobility-aid-comparison',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
