(function(){'use strict';
/* JAH The Grief Emotion Signature Database generator — jahdb-emotion-grief-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMGRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Grief Is: A Plain-Language Definition (Signature Edition) - Foundations",
  "Where Grief Sits in the Emotion Family (Signature Edition) - Foundations",
  "The Same Grief at Different Volumes: Mild, Moderate, and Intense (Signature Edition) - Foundations",
  "Common Myths and Misunderstandings About Grief (Signature Edition) - Foundations",
  "Inside the Feeling: A First-Person Passage Through Grief (Signature Edition) - Foundations",
  "How Grief Changes Over Time: Onset, Peak, Fading, and Aftershock (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Grief at Low Intensity and High Intensity: Two Lived Snapshots (Signature Edition) - Compounded",
  "Grief Mixed With Its Most Common Partner: Sadness and Anger (Signature Edition) - Compounded",
  "A Day in the Life: Grief Running Through an Ordinary Day (Signature Edition) - Compounded",
  "What Happens in the Body During Grief (Signature Edition) - Compounded",
  "Posture and Movement: How the Body Carries Grief (Signature Edition) - Compounded",
  "Sleep, Appetite, and Energy Under Grief (Signature Edition) - Compounded",
  "How Body Signals Differ From Person to Person (Signature Edition) - Compounded",
  "The Face of Grief: Eyes, Brows, Mouth, and Micro-Signs (Signature Edition) - Compounded",
  "How the Grieving Expression Changes With Intensity (Signature Edition) - Compounded",
  "Hiding and Faking the Grieving Face: What Leaks Through (Signature Edition) - Compounded",
  "Expression Gallery Notes: Describing Grief So an Artist Could Draw It (Signature Edition) - Compounded",
  "The Classic Triggers of Grief (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Personal Triggers: Memories, Anniversaries, and Private Associations (Signature Edition) - Advanced",
  "Surprise Triggers: The Unexpected Things That Set Off Grief (Signature Edition) - Advanced",
  "Chain Reactions: How One Grief Trigger Sets Off a Cascade (Signature Edition) - Advanced",
  "What People Do When They Feel Grief (Signature Edition) - Advanced",
  "What People Say: Grief in Words, Tone, and Speech Patterns (Signature Edition) - Advanced",
  "How Grief Changes Decisions and Judgment (Signature Edition) - Advanced",
  "Behavior Under Intensity: How Grief-Driven Actions Escalate (Signature Edition) - Advanced",
  "Expressing Grief Healthily: Saying It, Showing It, Channeling It (Signature Edition) - Advanced",
  "Bottling Up or Exploding: What Unhealthy Expression Costs (Signature Edition) - Advanced",
  "Everyday Practices That Keep Grief in Balance (Signature Edition) - Advanced",
  "Reading the Signs: Recognizing Grief in Others (Signature Edition) - Advanced",
  "What to Say and Do When Someone Near You Is Grieving (Signature Edition) - Advanced",
  "What Not to Do: The Mistakes That Make Grief Worse (Signature Edition) - Advanced",
  "The Related Emotions Map: Griefs Nearest Neighbors and Opposites (Signature Edition) - Advanced",
  "Emotion Mixes: Grief Blended With Sadness, Anger, Guilt, and Love (Signature Edition) - Advanced",
  "Full Behavioral Simulation: Grief From Trigger to Resolution (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Grief Emotion Study — "+safe+"\n"
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
    demo:{kind:"grief-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-grief-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-grief-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
