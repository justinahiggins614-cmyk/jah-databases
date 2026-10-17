(function(){'use strict';
/* JAH The Anxiety Emotion Database generator — jahdb-emotion-anxiety-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMAX-";
var FIELDS=["What Anxiety Is","How Anxiety Feels","Body Signals","Facial Expression","Triggers","Anxiety in Behavior","Healthy Expression","Recognizing Anxiety in Others","Emotion Mixes and Simulation"];
var TOPICS={
 "What Anxiety Is": [
  "What Anxiety Is: A Plain-Language Definition - What Anxiety Is",
  "Anxiety in the Emotion Family - What Anxiety Is",
  "Anxiety at Three Volumes: Mild, Moderate, Intense - What Anxiety Is",
  "Myths and Misunderstandings About Anxiety - What Anxiety Is"
 ],
 "How Anxiety Feels": [
  "Inside the Feeling: Anxiety in First Person - How Anxiety Feels",
  "The Arc of Anxiety: Onset, Peak, Fading, Aftershock - How Anxiety Feels",
  "Anxiety at Low and High Intensity: Two Lived Snapshots - How Anxiety Feels",
  "When Anxiety Meets Irritation: The Most Common Blend - How Anxiety Feels",
  "A Day in the Life: Anxiety Running Through an Ordinary Day - How Anxiety Feels"
 ],
 "Body Signals": [
  "What Happens in the Body: The Physical Signals of Anxiety - Body Signals",
  "Posture and Movement: How the Body Carries Anxiety - Body Signals",
  "Sleep, Appetite, and Energy Under Anxiety - Body Signals",
  "Different Bodies, Different Anxiety: How Signals Vary - Body Signals"
 ],
 "Facial Expression": [
  "The Face of Anxiety: Eyes, Brows, Mouth, and Micro-Signs - Facial Expression",
  "How the Anxious Face Changes With Intensity - Facial Expression",
  "Hiding Anxiety: Masks and What Leaks Through - Facial Expression",
  "Drawing Anxiety: Notes for Artists and Actors - Facial Expression"
 ],
 "Triggers": [
  "Classic Triggers: What Commonly Sets Anxiety Off - Triggers",
  "Personal Triggers: Memory, Dates, and Private Associations - Triggers",
  "Surprise Triggers: The Odd and Unexpected - Triggers",
  "Chain Reactions: How One Trigger Starts a Cascade - Triggers"
 ],
 "Anxiety in Behavior": [
  "What People Do: Typical Actions and Reactions Under Anxiety - Anxiety in Behavior",
  "What People Say: Words, Tone, and Speech Patterns - Anxiety in Behavior",
  "Anxious Decisions: How Anxiety Shapes Choices - Anxiety in Behavior",
  "Escalation: How Behavior Changes as Anxiety Grows - Anxiety in Behavior"
 ],
 "Healthy Expression": [
  "Healthy Expression: Saying It, Showing It, Channeling It - Healthy Expression",
  "Unhealthy Expression: Bottling Up or Boiling Over - Healthy Expression",
  "Everyday Practices: Small Habits That Keep Anxiety in Balance - Healthy Expression"
 ],
 "Recognizing Anxiety in Others": [
  "Reading the Signs: Anxiety Cues in Other People - Recognizing Anxiety in Others",
  "What to Say and Do When Someone Near You Is Anxious - Recognizing Anxiety in Others",
  "What Not to Do: Common Mistakes That Make Anxiety Worse - Recognizing Anxiety in Others"
 ],
 "Emotion Mixes and Simulation": [
  "The Anxiety Neighborhood: Related Emotions and Close Cousins - Emotion Mixes and Simulation",
  "Emotion Mixes: Anxiety Blended With Other Emotions - Emotion Mixes and Simulation",
  "Full Simulation: Anxiety From Trigger to Resolution - Emotion Mixes and Simulation"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Anxiety Emotion Study — "+safe+"\n"
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
    demo:{kind:"anxiety-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-anxiety-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-anxiety',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
