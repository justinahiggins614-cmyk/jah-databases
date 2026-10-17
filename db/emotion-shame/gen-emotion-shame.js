(function(){'use strict';
/* JAH The Shame Emotion Database generator — jahdb-emotion-shame-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMSH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Shame Is: A Plain-Language Definition - Foundations",
  "Shame in the Emotion Family - Foundations",
  "How Strong Shame Can Get: Mild, Moderate, Intense - Foundations",
  "Myths and Misunderstandings About Shame - Foundations",
  "Inside Shame: A First-Person Passage - Foundations",
  "Shame Over Time: Onset, Peak, Fading, Aftershock - Foundations",
  "Shame at Low Intensity vs High Intensity: Two Snapshots - Foundations",
  "Shame Mixed With Guilt: The Most Common Partnership - Foundations",
  "A Day With Shame: An Ordinary-Day Vignette - Foundations"
 ],
 "Compounded": [
  "The Body in Shame: Heart, Breath, Muscles, Stomach, Skin, Energy - Compounded",
  "The Posture of Shame: How the Body Carries It - Compounded",
  "Shame, Sleep, Appetite, and Energy - Compounded",
  "How Shame Feels Different in Different Bodies - Compounded",
  "The Face of Shame: Eyes, Brows, Mouth, and Micro-Signs - Compounded",
  "The Shame Face Across Intensities - Compounded",
  "Hiding and Faking the Shame Expression - and What Leaks Through - Compounded",
  "Drawing Shame: Expression Notes for Artists and Actors - Compounded",
  "The Classic Triggers of Shame - Compounded",
  "Personal Shame Triggers: Memories, Anniversaries, Private Associations - Compounded",
  "Surprise Triggers: The Odd, Unexpected Ones - Compounded",
  "Chain Reactions: How One Trigger Sets Off a Cascade - Compounded"
 ],
 "Advanced": [
  "What People Do in Shame: Actions and Reactions - Advanced",
  "The Voice of Shame: Speech Patterns - Advanced",
  "Shame and Judgment: What It Makes People Choose - Advanced",
  "Shame Under Intensity: How Actions Escalate - Advanced",
  "Expressing Shame Healthily: Saying It, Showing It, Channeling It - Advanced",
  "The Two Costly Paths: Bottling Up and Melting Down - Advanced",
  "Everyday Practices That Keep Shame in Balance - Advanced",
  "Reading the Signs: Shame in Other People - Advanced",
  "What to Say and Do When Someone Near You Feels Shame - Advanced",
  "What NOT to Do: The Mistakes That Make Shame Worse - Advanced",
  "Shame's Neighbors: Guilt, Embarrassment, Humiliation, Pride - Advanced",
  "Shame Blends: Plutchik-Style Dyads - Advanced",
  "The Full Shame Simulation: Trigger to Resolution - Advanced"
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
var gen={version:'jahdb-emotion-shame-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-shame',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
