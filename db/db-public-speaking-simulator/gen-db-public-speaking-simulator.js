(function(){'use strict';
/* JAH The Public Speaking Simulator generator — jahdb-db-public-speaking-simulator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PBSS-";
var FIELDS=["Foundations","Delivery","Stage"];
var TOPICS={
 "Foundations": [
  "Why Speaking Matters - Foundations",
  "Know Your Audience - Foundations",
  "The One Message - Foundations",
  "Structure: Tell Them - Foundations",
  "Openings That Hook - Foundations",
  "Stories Beat Statistics - Foundations",
  "Closings That Land - Foundations",
  "Nerves Are Normal - Foundations",
  "Preparation Beats Talent - Foundations",
  "Know Your Material Cold - Foundations",
  "The Rehearsal Ritual - Foundations",
  "Feedback: The Mirror - Foundations"
 ],
 "Delivery": [
  "Voice: Your Instrument - Delivery",
  "Body Language - Delivery",
  "Pacing and Pauses - Delivery",
  "Eye Contact That Connects - Delivery",
  "Gestures With Purpose - Delivery",
  "Handling Filler Words - Delivery",
  "Slides That Support - Delivery",
  "Microphone Technique - Delivery",
  "Q&A: The Real Test - Delivery",
  "Handling Hecklers - Delivery"
 ],
 "Stage": [
  "Virtual Presenting - Stage",
  "Panel Discussions - Stage",
  "Keynotes: The Big Stage - Stage",
  "Impromptu Speaking - Stage",
  "Storytelling on Stage - Stage",
  "Humor That Works - Stage",
  "Reading the Room - Stage",
  "Stage Fright First Aid - Stage",
  "Props and Demos - Stage",
  "Persuasive Talks: Moving to Action - Stage",
  "Your Speaking Journey - Stage",
  "Giving a Toast - Stage"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Public Speaking Study — "+safe+"\n"
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
    name:topic+' — speaking lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A speaking lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"public-speaking-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-public-speaking-simulator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-public-speaking-simulator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
