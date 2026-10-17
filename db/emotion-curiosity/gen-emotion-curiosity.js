(function(){'use strict';
/* JAH The Curiosity Emotion Database generator — jahdb-emotion-curiosity-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMCU-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Curiosity Is: A Plain-Language Definition - Foundations",
  "Where Curiosity Sits in the Emotion Family - Foundations",
  "How Strong Curiosity Gets: Mild to Moderate to Intense - Foundations",
  "Myths and Misunderstandings About Curiosity - Foundations",
  "Inside the Feeling: A First-Person Passage - Foundations",
  "How Curiosity Changes Over Time: Onset, Peak, Fading, Aftershock - Foundations",
  "Curiosity at Low Intensity Versus High Intensity: Two Snapshots - Foundations",
  "Curiosity Mixed With Joy: Its Most Common Partner - Foundations",
  "A Day in the Life: Curiosity Running Through an Ordinary Day - Foundations"
 ],
 "Compounded": [
  "What Happens in the Body: The Signals of Curiosity - Compounded",
  "Posture and Movement: How the Body Carries Curiosity - Compounded",
  "Sleep, Appetite, and Energy: Curiosity's Effect on the Day - Compounded",
  "How Body Signals Differ Between People - Compounded",
  "The Face of Curiosity: Eyes, Brows, Mouth, Micro-Signs - Compounded",
  "How the Expression Changes With Intensity - Compounded",
  "Hiding or Faking Curiosity: What Leaks Through - Compounded",
  "Expression Gallery Notes: Drawing and Playing Curiosity - Compounded",
  "The Classic Triggers: What Commonly Sets Curiosity Off - Compounded",
  "Personal Triggers: Memories, Anniversaries, Private Associations - Compounded",
  "Surprise Triggers: The Odd, Unexpected Things That Set It Off - Compounded",
  "Chain Reactions: How One Trigger Sets Off a Cascade - Compounded"
 ],
 "Advanced": [
  "What People Do When They Feel Curious: Actions and Reactions - Advanced",
  "What Curious People Say: Phrases, Tone, and Speech Patterns - Advanced",
  "Curiosity and Decisions: What the Emotion Makes People Choose - Advanced",
  "Behavior Under Intensity: How Curiosity Escalates - Advanced",
  "Healthy Expression: Saying It, Showing It, Channeling It Well - Advanced",
  "Unhealthy Expression: Bottling It Up or Exploding - Advanced",
  "Everyday Practices: Small Habits That Keep Curiosity in Balance - Advanced",
  "Reading the Signs: Curiosity in Other People - Advanced",
  "What to Say and Do When Someone Near You Is Curious - Advanced",
  "What NOT to Do: Mistakes That Kill Curiosity - Advanced",
  "Related Emotions Map: Neighbors, Opposites, Close Cousins - Advanced",
  "Emotion Mixes: Curiosity Blended With Four Partners - Advanced",
  "Full Behavioral Simulation: The Attic Box, Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Curiosity Emotion Study — "+safe+"\n"
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
    demo:{kind:"curiosity-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-curiosity-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-curiosity',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
