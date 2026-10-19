(function(){'use strict';
/* JAH The Captioning and Transcription Quality Database generator — jahdb-captioning-and-transcription-quality-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CATQ-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Captioning and Transcription Quality: Seeing Barriers Clearly — foundations",
  "Captioning and Transcription Quality: The Standards Map — foundations",
  "Captioning and Transcription Quality: Keyboard-First Testing — foundations",
  "Captioning and Transcription Quality: Screen Reader Basics — foundations",
  "Captioning and Transcription Quality: Color and Contrast — foundations",
  "Captioning and Transcription Quality: Captions Done Right — foundations",
  "Captioning and Transcription Quality: Transcripts That Help — foundations",
  "Captioning and Transcription Quality: Plain Language Power — foundations",
  "Captioning and Transcription Quality: Forms Without Tears — foundations",
  "Captioning and Transcription Quality: Navigation That Orients — foundations",
  "Captioning and Transcription Quality: Images With Purpose — foundations",
  "Captioning and Transcription Quality: Video Accessibility — foundations"
 ],
 "compounded": [
  "Captioning and Transcription Quality: Audio Accessibility — compounded",
  "Captioning and Transcription Quality: Cognitive Accessibility — compounded",
  "Captioning and Transcription Quality: Motor Accessibility — compounded",
  "Captioning and Transcription Quality: Hearing Accessibility — compounded",
  "Captioning and Transcription Quality: Vision Accessibility — compounded",
  "Captioning and Transcription Quality: Speech Accessibility — compounded",
  "Captioning and Transcription Quality: Assistive Tech Compatibility — compounded",
  "Captioning and Transcription Quality: Accessible Documents — compounded",
  "Captioning and Transcription Quality: Accessible Events — compounded",
  "Captioning and Transcription Quality: Emergency Accessibility — compounded",
  "Captioning and Transcription Quality: Advanced: Accessibility Audits — compounded",
  "Captioning and Transcription Quality: Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Captioning and Transcription Quality: Advanced: Design Systems Accessibly — advanced",
  "Captioning and Transcription Quality: Advanced: Procurement Power — advanced",
  "Captioning and Transcription Quality: Advanced: Legal Landscape — advanced",
  "Captioning and Transcription Quality: Advanced: Inclusive Research — advanced",
  "Captioning and Transcription Quality: Advanced: Accessibility Metrics — advanced",
  "Captioning and Transcription Quality: Advanced: Culture Change — advanced",
  "Captioning and Transcription Quality: Advanced: Emerging Tech Access — advanced",
  "Captioning and Transcription Quality: Advanced: Global Accessibility — advanced",
  "Captioning and Transcription Quality: Advanced: Teaching Accessibility — advanced",
  "Captioning and Transcription Quality: Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Captioning and Transcription Quality Database — structural study\n"
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
var gen={version:'jahdb-captioning-and-transcription-quality-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('captioning-and-transcription-quality',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
