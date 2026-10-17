(function(){'use strict';
/* JAH The Embarrassment Emotion Database generator — jahdb-emotion-embarrassment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMEB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Embarrassment Is: A Plain-Language Definition - Foundations",
  "Where Embarrassment Sits in the Emotion Family - Foundations",
  "Mild, Moderate, and Intense: Embarrassment at Three Volumes - Foundations",
  "Common Myths and Misunderstandings About Embarrassment - Foundations",
  "Inside the Feeling: Embarrassment in the First Person - Foundations",
  "Onset, Peak, Fade, Aftershock: The Time Course of Embarrassment - Foundations",
  "Two Snapshots: Embarrassment at Low and High Intensity - Foundations",
  "Embarrassment Mixed with Its Most Common Partner: Anxiety - Foundations",
  "A Day in the Life: Embarrassment Running Through an Ordinary Day - Foundations",
  "What Happens in the Body: The Physiology of Embarrassment - Foundations",
  "Posture and Movement: How the Body Carries Embarrassment - Foundations",
  "Sleep, Appetite, and Energy: Embarrassment's Quiet After-Effects - Foundations",
  "No Two Bodies React Identically: How Embarrassment Differs Between People - Foundations"
 ],
 "Compounded": [
  "The Face of Embarrassment: Eyes, Brows, Mouth, and Micro-Signs - Compounded",
  "How the Expression Changes with Intensity - Compounded",
  "Hiding It, Faking It: What Leaks Through - Compounded",
  "Expression Gallery Notes: Drawing and Playing Embarrassment - Compounded",
  "The Classic Triggers: What Commonly Sets It Off - Compounded",
  "Personal Triggers: Memories, Anniversaries, and Private Associations - Compounded",
  "Surprise Triggers: The Odd, Unexpected Things That Set It Off - Compounded",
  "Chain Reactions: How One Trigger Sets Off a Cascade - Compounded",
  "What People Do: The Typical Actions and Reactions - Compounded",
  "What People Say: Phrases, Tone, and Speech Patterns - Compounded"
 ],
 "Advanced": [
  "How Embarrassment Changes Decisions and Judgment - Advanced",
  "Behavior Under Intensity: How Actions Escalate as the Feeling Grows - Advanced",
  "Healthy Expression: Saying It, Showing It, Channeling It Well - Advanced",
  "Unhealthy Expression: Bottling It Up or Exploding - What Each Costs - Advanced",
  "Everyday Practices: Small Habits That Keep Embarrassment in Balance - Advanced",
  "Reading the Signs: Recognizing Embarrassment in Other People - Advanced",
  "What to Say and Do: Supportive Responses That Actually Help - Advanced",
  "What NOT to Do: The Common Mistakes That Make It Worse - Advanced",
  "Related Emotions Map: Neighbors, Opposites, and Close Cousins - Advanced",
  "Emotion Mixes: Embarrassment Blended with Four Partners - Advanced",
  "Full Behavioral Simulation: From Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Embarrassment Emotion Study — "+safe+"\n"
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
    demo:{kind:"embarrassment-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-embarrassment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-embarrassment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
