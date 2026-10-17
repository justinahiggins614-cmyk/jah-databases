(function(){'use strict';
/* JAH The Boredom Emotion Database generator — jahdb-emotion-boredom-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMBO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Boredom Is: A Plain-Language Definition - Foundations",
  "Where Boredom Sits in the Emotion Family - Foundations",
  "The Three Volumes: Mild, Moderate, and Intense Boredom - Foundations",
  "Myths and Misunderstandings About Boredom - Foundations",
  "Inside the Feeling: A First-Person Account of Boredom - Foundations",
  "How Boredom Moves Through Time: Onset, Peak, Fading, Aftershock - Foundations",
  "Boredom at Low vs High Intensity: Two Lived Snapshots - Foundations",
  "Boredom Mixed With Restlessness: The Most Common Blend - Foundations",
  "A Day in the Life: Boredom Running Through an Ordinary Day - Foundations"
 ],
 "Compounded": [
  "What Happens in the Body During Boredom - Compounded",
  "The Posture and Movement Signature of Boredom - Compounded",
  "Boredom, Sleep, Appetite, and Energy - Compounded",
  "How Boredom Feels Different in Different Bodies - Compounded",
  "The Face of Boredom: Eyes, Brows, Mouth, and Micro-Signs - Compounded",
  "How Boredom's Expression Changes With Intensity - Compounded",
  "Hiding Boredom and Faking Interest: What Leaks Through - Compounded",
  "Expression Gallery Notes: Boredom for Artists and Actors - Compounded",
  "The Classic Triggers of Boredom - Compounded",
  "Personal Triggers: Memories, Anniversaries, and Private Associations - Compounded",
  "Surprise Triggers: The Odd Things That Set Boredom Off - Compounded",
  "Chain Reactions: How One Boredom Trigger Cascades - Compounded"
 ],
 "Advanced": [
  "What People Do When They Are Bored - Advanced",
  "What Bored People Say: Phrases, Tone, and Speech Patterns - Advanced",
  "How Boredom Changes Decisions and Judgment - Advanced",
  "Escalation: How Boredom Behaviors Intensify - Advanced",
  "Expressing Boredom Well: Saying It, Showing It, Channeling It - Advanced",
  "Bottling It Up or Exploding: What Each Costs - Advanced",
  "Everyday Practices That Keep Boredom in Balance - Advanced",
  "Reading Boredom in Others: Face, Body, Voice, Behavior - Advanced",
  "What to Say and Do When Someone Near You Is Bored - Advanced",
  "What NOT to Do: Mistakes That Make Boredom Worse - Advanced",
  "The Boredom Neighborhood: Neighbors, Opposites, and Close Cousins - Advanced",
  "Boredom Blends: Four Mixes and What Each Feels Like - Advanced",
  "Full Behavioral Simulation: Boredom From Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Boredom Emotion Study — "+safe+"\n"
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
    demo:{kind:"boredom-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-boredom-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-boredom',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
