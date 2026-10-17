(function(){'use strict';
/* JAH The Shame Emotion Signature Database generator — jahdb-emotion-shame-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMSHS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Shame Is: A Plain-Language Definition (Signature Edition) - Foundations",
  "Shame in the Emotion Family (Signature Edition) - Foundations",
  "How Strong Shame Can Get: Mild, Moderate, Intense (Signature Edition) - Foundations",
  "Myths and Misunderstandings About Shame (Signature Edition) - Foundations",
  "Inside Shame: A First-Person Passage (Signature Edition) - Foundations",
  "Shame Over Time: Onset, Peak, Fading, Aftershock (Signature Edition) - Foundations",
  "Shame at Low Intensity vs High Intensity: Two Snapshots (Signature Edition) - Foundations",
  "Shame Mixed With Guilt: The Most Common Partnership (Signature Edition) - Foundations",
  "A Day With Shame: An Ordinary-Day Vignette (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Body in Shame: Heart, Breath, Muscles, Stomach, Skin, Energy (Signature Edition) - Compounded",
  "The Posture of Shame: How the Body Carries It (Signature Edition) - Compounded",
  "Shame, Sleep, Appetite, and Energy (Signature Edition) - Compounded",
  "How Shame Feels Different in Different Bodies (Signature Edition) - Compounded",
  "The Face of Shame: Eyes, Brows, Mouth, and Micro-Signs (Signature Edition) - Compounded",
  "The Shame Face Across Intensities (Signature Edition) - Compounded",
  "Hiding and Faking the Shame Expression - and What Leaks Through (Signature Edition) - Compounded",
  "Drawing Shame: Expression Notes for Artists and Actors (Signature Edition) - Compounded",
  "The Classic Triggers of Shame (Signature Edition) - Compounded",
  "Personal Shame Triggers: Memories, Anniversaries, Private Associations (Signature Edition) - Compounded",
  "Surprise Triggers: The Odd, Unexpected Ones (Signature Edition) - Compounded",
  "Chain Reactions: How One Trigger Sets Off a Cascade (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "What People Do in Shame: Actions and Reactions (Signature Edition) - Advanced",
  "The Voice of Shame: Speech Patterns (Signature Edition) - Advanced",
  "Shame and Judgment: What It Makes People Choose (Signature Edition) - Advanced",
  "Shame Under Intensity: How Actions Escalate (Signature Edition) - Advanced",
  "Expressing Shame Healthily: Saying It, Showing It, Channeling It (Signature Edition) - Advanced",
  "The Two Costly Paths: Bottling Up and Melting Down (Signature Edition) - Advanced",
  "Everyday Practices That Keep Shame in Balance (Signature Edition) - Advanced",
  "Reading the Signs: Shame in Other People (Signature Edition) - Advanced",
  "What to Say and Do When Someone Near You Feels Shame (Signature Edition) - Advanced",
  "What NOT to Do: The Mistakes That Make Shame Worse (Signature Edition) - Advanced",
  "Shame's Neighbors: Guilt, Embarrassment, Humiliation, Pride (Signature Edition) - Advanced",
  "Shame Blends: Plutchik-Style Dyads (Signature Edition) - Advanced",
  "The Full Shame Simulation: Trigger to Resolution (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Shame Emotion Study — "+safe+"\n"
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
    demo:{kind:"shame-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-shame-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-shame-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
