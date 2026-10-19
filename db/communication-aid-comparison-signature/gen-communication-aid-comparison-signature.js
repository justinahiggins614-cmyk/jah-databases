(function(){'use strict';
/* JAH The Communication Aid Comparison Signature Database generator — jahdb-communication-aid-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CACS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Communication Aid Comparison (Signature): Seeing Barriers Clearly — foundations",
  "Communication Aid Comparison (Signature): The Standards Map — foundations",
  "Communication Aid Comparison (Signature): Keyboard-First Testing — foundations",
  "Communication Aid Comparison (Signature): Screen Reader Basics — foundations",
  "Communication Aid Comparison (Signature): Color and Contrast — foundations",
  "Communication Aid Comparison (Signature): Captions Done Right — foundations",
  "Communication Aid Comparison (Signature): Transcripts That Help — foundations",
  "Communication Aid Comparison (Signature): Plain Language Power — foundations",
  "Communication Aid Comparison (Signature): Forms Without Tears — foundations",
  "Communication Aid Comparison (Signature): Navigation That Orients — foundations",
  "Communication Aid Comparison (Signature): Images With Purpose — foundations",
  "Communication Aid Comparison (Signature): Video Accessibility — foundations"
 ],
 "compounded": [
  "Communication Aid Comparison (Signature): Audio Accessibility — compounded",
  "Communication Aid Comparison (Signature): Cognitive Accessibility — compounded",
  "Communication Aid Comparison (Signature): Motor Accessibility — compounded",
  "Communication Aid Comparison (Signature): Hearing Accessibility — compounded",
  "Communication Aid Comparison (Signature): Vision Accessibility — compounded",
  "Communication Aid Comparison (Signature): Speech Accessibility — compounded",
  "Communication Aid Comparison (Signature): Assistive Tech Compatibility — compounded",
  "Communication Aid Comparison (Signature): Accessible Documents — compounded",
  "Communication Aid Comparison (Signature): Accessible Events — compounded",
  "Communication Aid Comparison (Signature): Emergency Accessibility — compounded",
  "Communication Aid Comparison (Signature): Advanced: Accessibility Audits — compounded",
  "Communication Aid Comparison (Signature): Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Communication Aid Comparison (Signature): Advanced: Design Systems Accessibly — advanced",
  "Communication Aid Comparison (Signature): Advanced: Procurement Power — advanced",
  "Communication Aid Comparison (Signature): Advanced: Legal Landscape — advanced",
  "Communication Aid Comparison (Signature): Advanced: Inclusive Research — advanced",
  "Communication Aid Comparison (Signature): Advanced: Accessibility Metrics — advanced",
  "Communication Aid Comparison (Signature): Advanced: Culture Change — advanced",
  "Communication Aid Comparison (Signature): Advanced: Emerging Tech Access — advanced",
  "Communication Aid Comparison (Signature): Advanced: Global Accessibility — advanced",
  "Communication Aid Comparison (Signature): Advanced: Teaching Accessibility — advanced",
  "Communication Aid Comparison (Signature): Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Communication Aid Comparison Signature Database — structural study\n"
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
var gen={version:'jahdb-communication-aid-comparison-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('communication-aid-comparison-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
