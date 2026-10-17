(function(){'use strict';
/* JAH The Disgust Emotion Signature Database generator — jahdb-emotion-disgust-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMDIS-";
var FIELDS=["Description","Inner Experience","Body Signals","Facial Expression","Triggers","Behavior","Healthy Expression","Recognizing It in Others","Related Emotions and Simulation"];
var TOPICS={
 "Description": [
  "What Disgust Is: A Plain-Language Definition (Signature Edition) - Description",
  "Where Disgust Sits in the Emotion Family (Signature Edition) - Description",
  "How Strong Disgust Can Get: Mild to Intense (Signature Edition) - Description",
  "Common Myths About Disgust (Signature Edition) - Description"
 ],
 "Inner Experience": [
  "Inside the Feeling: A First-Person Account of Disgust (Signature Edition) - Inner Experience",
  "The Arc of Disgust: Onset, Peak, and Fading (Signature Edition) - Inner Experience",
  "Disgust at Low Intensity vs High Intensity (Signature Edition) - Inner Experience",
  "Disgust Mixed with Anger (Signature Edition) - Inner Experience",
  "Disgust Through an Ordinary Day (Signature Edition) - Inner Experience"
 ],
 "Body Signals": [
  "What Happens in the Body: The Disgust Response (Signature Edition) - Body Signals",
  "The Posture and Movement Signature of Disgust (Signature Edition) - Body Signals",
  "Sleep, Appetite, and Energy Under Disgust (Signature Edition) - Body Signals",
  "How Bodies Differ in Disgust (Signature Edition) - Body Signals"
 ],
 "Facial Expression": [
  "The Face of Disgust: Eyes, Nose, and Mouth (Signature Edition) - Facial Expression",
  "How the Disgust Expression Changes with Intensity (Signature Edition) - Facial Expression",
  "Hiding or Faking Disgust: What Leaks Through (Signature Edition) - Facial Expression",
  "Drawing the Face of Disgust: A Descriptive Guide (Signature Edition) - Facial Expression"
 ],
 "Triggers": [
  "The Classic Triggers of Disgust (Signature Edition) - Triggers",
  "Personal Triggers: Memory and Association (Signature Edition) - Triggers",
  "Surprise Triggers of Disgust (Signature Edition) - Triggers",
  "Chain Reactions: When Disgust Pulls Other Emotions (Signature Edition) - Triggers"
 ],
 "Behavior": [
  "What People Do When They Feel Disgust (Signature Edition) - Behavior",
  "What People Say When They Feel Disgust (Signature Edition) - Behavior",
  "How Disgust Changes Decisions and Judgment (Signature Edition) - Behavior",
  "Disgust Under Intensity: Escalation (Signature Edition) - Behavior"
 ],
 "Healthy Expression": [
  "Expressing Disgust in Healthy Ways (Signature Edition) - Healthy Expression",
  "Unhealthy Expression: Bottling Up or Exploding (Signature Edition) - Healthy Expression",
  "Everyday Practices for Keeping Disgust in Balance (Signature Edition) - Healthy Expression"
 ],
 "Recognizing It in Others": [
  "Reading Disgust in Others (Signature Edition) - Recognizing It in Others",
  "Responding Supportively to Someone Who Feels Disgust (Signature Edition) - Recognizing It in Others",
  "What Not to Do When Someone Feels Disgust (Signature Edition) - Recognizing It in Others"
 ],
 "Related Emotions and Simulation": [
  "The Disgust Neighbors: Related Emotions and How to Tell Them Apart (Signature Edition) - Related Emotions and Simulation",
  "Disgust Mixes: Blends with Other Emotions (Signature Edition) - Related Emotions and Simulation",
  "Full Behavioral Simulation: Disgust from Trigger to Resolution (Signature Edition) - Related Emotions and Simulation"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Emotion Record — "+safe+"\n"
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
    name:topic+' — emotion record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A emotion record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-disgust-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-disgust-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
