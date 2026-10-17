(function(){'use strict';
/* JAH The Guilt Emotion Signature Database generator — jahdb-emotion-guilt-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMGUS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Guilt Is: A Plain-Language Definition (Signature Edition) - Foundations",
  "Guilt in the Emotion Family: Basic Roots and Complex Branches (Signature Edition) - Foundations",
  "Guilt at Three Volumes: Mild, Moderate, and Intense (Signature Edition) - Foundations",
  "Myths and Misunderstandings About Guilt (Signature Edition) - Foundations",
  "Inside the Feeling: A First-Person Passage of Guilt (Signature Edition) - Foundations",
  "The Time Course of Guilt: Onset, Peak, Fading, and Aftershock (Signature Edition) - Foundations",
  "Guilt at Low Intensity and at High Intensity: Two Lived Snapshots (Signature Edition) - Foundations",
  "Guilt Mixed With Its Most Common Partner: Shame (Signature Edition) - Foundations",
  "A Day With Guilt: A Day-in-the-Life Vignette (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Body in Guilt: Heart, Breath, Muscles, Stomach, Skin, and Energy (Signature Edition) - Compounded",
  "Posture and Movement: How Guilt Carries the Body (Signature Edition) - Compounded",
  "Sleep, Appetite, and Energy Under Guilt (Signature Edition) - Compounded",
  "No Two Bodies Guilt Alike: How Body Signals Differ Between People (Signature Edition) - Compounded",
  "The Face of Guilt: Eyes, Brows, Mouth, and Micro-Signs (Signature Edition) - Compounded",
  "How the Guilty Face Changes With Intensity (Signature Edition) - Compounded",
  "Hiding and Faking Guilt: What Leaks Through (Signature Edition) - Compounded",
  "Drawing and Playing Guilt: Expression Gallery Notes (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "The Classic Triggers of Guilt (Signature Edition) - Advanced",
  "Personal Triggers: Memories, Anniversaries, and Private Associations (Signature Edition) - Advanced",
  "Surprise Triggers: The Unexpected Things That Set Off Guilt (Signature Edition) - Advanced",
  "Chain Reactions: When One Trigger Ignites a Cascade (Signature Edition) - Advanced",
  "What People Do When Guilty: Typical Actions and Reactions (Signature Edition) - Advanced",
  "What People Say When Guilty: Phrases, Tone, and Speech Patterns (Signature Edition) - Advanced",
  "How Guilt Changes Decisions and Judgment (Signature Edition) - Advanced",
  "Guilt Under Rising Intensity: How Actions Escalate (Signature Edition) - Advanced",
  "Healthy Expression: Saying It, Showing It, and Channeling It Well (Signature Edition) - Advanced",
  "Unhealthy Expression: Bottling It Up or Exploding - What Each Costs (Signature Edition) - Advanced",
  "Everyday Practices: Small Habits That Keep Guilt in Balance (Signature Edition) - Advanced",
  "Reading Guilt in Others: Face, Body, Voice, and Behavior Cues (Signature Edition) - Advanced",
  "What to Say and Do When Someone Near You Feels Guilty (Signature Edition) - Advanced",
  "What Not to Do: The Mistakes That Make Guilt Worse (Signature Edition) - Advanced",
  "The Guilt Neighborhood: Nearest Neighbors, Opposites, and Close Cousins (Signature Edition) - Advanced",
  "Guilt Blends: Mixes With Four Partner Emotions (Signature Edition) - Advanced",
  "Full Behavioral Simulation: One Guilt From Trigger to Resolution (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Guilt Emotion Study — "+safe+"\n"
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
    demo:{kind:"guilt-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-guilt-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-guilt-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
