(function(){'use strict';
/* JAH The Contempt Emotion Database generator — jahdb-emotion-contempt-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMCO-";
var FIELDS=["Description","Inner Experience","Body Signals","Facial Expression","Triggers","Behavior","Healthy Expression","Recognizing It in Others","Related Emotions and Simulation"];
var TOPICS={
 "Description": [
  "What Contempt Is: A Plain-Language Definition - Description",
  "Contempt in the Emotion Family: The Moral Emotions and the CAD Triad - Description",
  "How Strong Contempt Gets: Mild Disdain to Intense Scorn - Description",
  "Myths and Misunderstandings About Contempt - Description"
 ],
 "Inner Experience": [
  "Inside the Feeling: A First-Person Passage Through Contempt - Inner Experience",
  "The Arc of Contempt: Onset, Peak, Fading, and Aftershock - Inner Experience",
  "Contempt at Low Intensity vs High Intensity: Two Lived Snapshots - Inner Experience",
  "Contempt Mixed With Anger: The Indignation Blend - Inner Experience",
  "A Day in the Life: Contempt Running Through an Ordinary Day - Inner Experience"
 ],
 "Body Signals": [
  "What Happens in the Body: Heart, Breath, Muscles, and Energy - Body Signals",
  "Posture and Movement: How the Body Carries Contempt - Body Signals",
  "Sleep, Appetite, and Energy Effects of Contempt - Body Signals",
  "How Body Signals Differ Between People - Body Signals"
 ],
 "Facial Expression": [
  "The Face of Contempt: Eyes, Brows, Mouth, and the Tell-Tale Micro-Signs - Facial Expression",
  "How the Expression Changes With Intensity - Facial Expression",
  "Hiding and Faking Contempt: What Leaks Through - Facial Expression",
  "Drawing Contempt: Notes for Artists and Actors - Facial Expression"
 ],
 "Triggers": [
  "The Classic Triggers: Situations, Words, and Events - Triggers",
  "Personal Triggers: Memories, Anniversaries, and Private Associations - Triggers",
  "Surprise Triggers: The Odd, Unexpected Things That Set It Off - Triggers",
  "Chain Reactions: How One Trigger Sets Off a Cascade - Triggers"
 ],
 "Behavior": [
  "What People Do When They Feel Contempt - Behavior",
  "What People Say: Phrases, Tone, and Speech Patterns of Contempt - Behavior",
  "How Contempt Changes Decisions and Judgment - Behavior",
  "Contempt Under Intensity: How Actions Escalate - Behavior"
 ],
 "Healthy Expression": [
  "Healthy Expression: Saying It, Showing It, Channeling It Well - Healthy Expression",
  "Unhealthy Expression: Bottling Up or Exploding - What Each Costs - Healthy Expression",
  "Everyday Practices: Small Habits That Keep Contempt in Balance - Healthy Expression"
 ],
 "Recognizing It in Others": [
  "Reading the Signs: Recognizing Contempt in Others - Recognizing It in Others",
  "What to Say and Do When Someone Near You Feels Contempt - Recognizing It in Others",
  "What Not to Do: Mistakes That Make Contempt Worse - Recognizing It in Others"
 ],
 "Related Emotions and Simulation": [
  "The Related Emotions Map: Neighbors, Opposites, and Close Cousins - Related Emotions and Simulation",
  "Emotion Mixes: Contempt Blended With Other Emotions - Related Emotions and Simulation",
  "Full Behavioral Simulation: From Trigger Through Peak to Resolution - Related Emotions and Simulation"
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
var gen={version:'jahdb-emotion-contempt-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-contempt',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
