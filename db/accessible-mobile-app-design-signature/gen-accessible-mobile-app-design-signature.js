(function(){'use strict';
/* JAH The Accessible Mobile App Design Signature Database generator — jahdb-accessible-mobile-app-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AMADS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Accessible Mobile App Design (Signature): Seeing Barriers Clearly — foundations",
  "Accessible Mobile App Design (Signature): The Standards Map — foundations",
  "Accessible Mobile App Design (Signature): Keyboard-First Testing — foundations",
  "Accessible Mobile App Design (Signature): Screen Reader Basics — foundations",
  "Accessible Mobile App Design (Signature): Color and Contrast — foundations",
  "Accessible Mobile App Design (Signature): Captions Done Right — foundations",
  "Accessible Mobile App Design (Signature): Transcripts That Help — foundations",
  "Accessible Mobile App Design (Signature): Plain Language Power — foundations",
  "Accessible Mobile App Design (Signature): Forms Without Tears — foundations",
  "Accessible Mobile App Design (Signature): Navigation That Orients — foundations",
  "Accessible Mobile App Design (Signature): Images With Purpose — foundations",
  "Accessible Mobile App Design (Signature): Video Accessibility — foundations"
 ],
 "compounded": [
  "Accessible Mobile App Design (Signature): Audio Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Cognitive Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Motor Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Hearing Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Vision Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Speech Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Assistive Tech Compatibility — compounded",
  "Accessible Mobile App Design (Signature): Accessible Documents — compounded",
  "Accessible Mobile App Design (Signature): Accessible Events — compounded",
  "Accessible Mobile App Design (Signature): Emergency Accessibility — compounded",
  "Accessible Mobile App Design (Signature): Advanced: Accessibility Audits — compounded",
  "Accessible Mobile App Design (Signature): Advanced: Remediation Planning — compounded"
 ],
 "advanced": [
  "Accessible Mobile App Design (Signature): Advanced: Design Systems Accessibly — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Procurement Power — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Legal Landscape — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Inclusive Research — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Accessibility Metrics — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Culture Change — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Emerging Tech Access — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Global Accessibility — advanced",
  "Accessible Mobile App Design (Signature): Advanced: Teaching Accessibility — advanced",
  "Accessible Mobile App Design (Signature): Advanced: The Business Case — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Mobile App Design Signature Database — structural study\n"
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
var gen={version:'jahdb-accessible-mobile-app-design-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-mobile-app-design-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
