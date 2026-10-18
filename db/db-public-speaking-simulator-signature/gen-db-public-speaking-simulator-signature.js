(function(){'use strict';
/* JAH The Public Speaking Simulator generator — jahdb-db-public-speaking-simulator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PBSSS-";
var FIELDS=["Foundations","Delivery","Stage"];
var TOPICS={
 "Foundations": [
  "Why Speaking Matters (Signature Edition) - Foundations",
  "Know Your Audience (Signature Edition) - Foundations",
  "The One Message (Signature Edition) - Foundations",
  "Structure: Tell Them (Signature Edition) - Foundations",
  "Openings That Hook (Signature Edition) - Foundations",
  "Stories Beat Statistics (Signature Edition) - Foundations",
  "Closings That Land (Signature Edition) - Foundations",
  "Nerves Are Normal (Signature Edition) - Foundations",
  "Preparation Beats Talent (Signature Edition) - Foundations",
  "Know Your Material Cold (Signature Edition) - Foundations",
  "The Rehearsal Ritual (Signature Edition) - Foundations",
  "Feedback: The Mirror (Signature Edition) - Foundations"
 ],
 "Delivery": [
  "Voice: Your Instrument (Signature Edition) - Delivery",
  "Body Language (Signature Edition) - Delivery",
  "Pacing and Pauses (Signature Edition) - Delivery",
  "Eye Contact That Connects (Signature Edition) - Delivery",
  "Gestures With Purpose (Signature Edition) - Delivery",
  "Handling Filler Words (Signature Edition) - Delivery",
  "Slides That Support (Signature Edition) - Delivery",
  "Microphone Technique (Signature Edition) - Delivery",
  "Q&A: The Real Test (Signature Edition) - Delivery",
  "Handling Hecklers (Signature Edition) - Delivery"
 ],
 "Stage": [
  "Virtual Presenting (Signature Edition) - Stage",
  "Panel Discussions (Signature Edition) - Stage",
  "Keynotes: The Big Stage (Signature Edition) - Stage",
  "Impromptu Speaking (Signature Edition) - Stage",
  "Storytelling on Stage (Signature Edition) - Stage",
  "Humor That Works (Signature Edition) - Stage",
  "Reading the Room (Signature Edition) - Stage",
  "Stage Fright First Aid (Signature Edition) - Stage",
  "Props and Demos (Signature Edition) - Stage",
  "Persuasive Talks: Moving to Action (Signature Edition) - Stage",
  "Your Speaking Journey (Signature Edition) - Stage",
  "Giving a Toast (Signature Edition) - Stage"
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
var gen={version:'jahdb-db-public-speaking-simulator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-public-speaking-simulator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
