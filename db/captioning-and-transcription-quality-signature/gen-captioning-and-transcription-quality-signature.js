(function(){'use strict';
/* JAH The Captioning and Transcription Quality Signature Database generator — jahdb-captioning-and-transcription-quality-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CATQS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Captioning and Transcription Quality (Signature): Seeing Barriers Clearly — foundations",
  "Captioning and Transcription Quality (Signature): The Standards Map — foundations",
  "Captioning and Transcription Quality (Signature): Keyboard-First Testing — foundations",
  "Captioning and Transcription Quality (Signature): Screen Reader Basics — foundations",
  "Captioning and Transcription Quality (Signature): Color and Contrast — foundations",
  "Captioning and Transcription Quality (Signature): Captions Done Right — foundations",
  "Captioning and Transcription Quality (Signature): Transcripts That Help — foundations",
  "Captioning and Transcription Quality (Signature): Plain Language Power — foundations",
  "Captioning and Transcription Quality (Signature): Forms Without Tears — foundations",
  "Captioning and Transcription Quality (Signature): Navigation That Orients — foundations",
  "Captioning and Transcription Quality (Signature): Images With Purpose — foundations",
  "Captioning and Transcription Quality (Signature): Video Accessibility — foundations"
 ],
 "compounded": [
  "Captioning and Transcription Quality (Signature): Audio Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Cognitive Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Motor Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Hearing Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Vision Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Speech Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Assistive Tech Compatibility — compounded",
  "Captioning and Transcription Quality (Signature): Accessible Documents — compounded",
  "Captioning and Transcription Quality (Signature): Accessible Events — compounded",
  "Captioning and Transcription Quality (Signature): Emergency Accessibility — compounded",
  "Captioning and Transcription Quality (Signature): Advanced: Accessibility Audits — compounded",
  "Captioning and Transcription Quality (Signature): Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Captioning and Transcription Quality (Signature): Advanced: Design Systems Accessibly — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Procurement Power — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Legal Landscape — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Inclusive Research — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Accessibility Metrics — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Culture Change — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Emerging Tech Access — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Global Accessibility — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: Teaching Accessibility — advanced",
  "Captioning and Transcription Quality (Signature): Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Captioning and Transcription Quality Signature Database — structural study\n"
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
var gen={version:'jahdb-captioning-and-transcription-quality-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('captioning-and-transcription-quality-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
