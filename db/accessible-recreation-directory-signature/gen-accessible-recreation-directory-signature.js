(function(){'use strict';
/* JAH The Accessible Recreation Directory Signature Database generator — jahdb-accessible-recreation-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Accessible Recreation Directory (Signature): Seeing Barriers Clearly — foundations",
  "Accessible Recreation Directory (Signature): The Standards Map — foundations",
  "Accessible Recreation Directory (Signature): Keyboard-First Testing — foundations",
  "Accessible Recreation Directory (Signature): Screen Reader Basics — foundations",
  "Accessible Recreation Directory (Signature): Color and Contrast — foundations",
  "Accessible Recreation Directory (Signature): Captions Done Right — foundations",
  "Accessible Recreation Directory (Signature): Transcripts That Help — foundations",
  "Accessible Recreation Directory (Signature): Plain Language Power — foundations",
  "Accessible Recreation Directory (Signature): Forms Without Tears — foundations",
  "Accessible Recreation Directory (Signature): Navigation That Orients — foundations",
  "Accessible Recreation Directory (Signature): Images With Purpose — foundations",
  "Accessible Recreation Directory (Signature): Video Accessibility — foundations"
 ],
 "compounded": [
  "Accessible Recreation Directory (Signature): Audio Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Cognitive Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Motor Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Hearing Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Vision Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Speech Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Assistive Tech Compatibility — compounded",
  "Accessible Recreation Directory (Signature): Accessible Documents — compounded",
  "Accessible Recreation Directory (Signature): Accessible Events — compounded",
  "Accessible Recreation Directory (Signature): Emergency Accessibility — compounded",
  "Accessible Recreation Directory (Signature): Advanced: Accessibility Audits — compounded",
  "Accessible Recreation Directory (Signature): Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Accessible Recreation Directory (Signature): Advanced: Design Systems Accessibly — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Procurement Power — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Legal Landscape — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Inclusive Research — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Accessibility Metrics — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Culture Change — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Emerging Tech Access — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Global Accessibility — advanced",
  "Accessible Recreation Directory (Signature): Advanced: Teaching Accessibility — advanced",
  "Accessible Recreation Directory (Signature): Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Recreation Directory Signature Database — structural study\n"
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
var gen={version:'jahdb-accessible-recreation-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-recreation-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
