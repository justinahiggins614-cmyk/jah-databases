(function(){'use strict';
/* JAH The Fear Emotion Database generator — jahdb-emotion-fear-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMFE-";
var FIELDS=["What Fear Is","How Fear Feels","Body Signals","Facial Expression","Triggers","Fear in Behavior","Healthy Expression","Recognizing Fear in Others","Emotion Mixes and Simulation"];
var TOPICS={
 "What Fear Is": [
  "What Fear Is: A Plain-Language Definition - What Fear Is",
  "Fear in the Emotion Family - What Fear Is",
  "Fear at Three Volumes: Mild, Moderate, Intense - What Fear Is",
  "Myths and Misunderstandings About Fear - What Fear Is"
 ],
 "How Fear Feels": [
  "Inside Fear: A First-Person Passage - How Fear Feels",
  "The Arc of Fear: Onset, Peak, Fading, Aftershock - How Fear Feels",
  "Low Fear and High Fear: Two Lived Snapshots - How Fear Feels",
  "Fear Mixed With Anger: The Fight-or-Flight Blend - How Fear Feels",
  "A Day With Fear: Morning Alarm to Midnight - How Fear Feels"
 ],
 "Body Signals": [
  "Fear in the Body: Heart, Breath, Muscles, Stomach, Skin - Body Signals",
  "The Posture of Fear: How the Body Carries It - Body Signals",
  "Fear, Sleep, Appetite, and Energy - Body Signals",
  "No Two Bodies Fear Alike - Body Signals"
 ],
 "Facial Expression": [
  "The Face of Fear: Eyes, Brows, Mouth, Micro-Signs - Facial Expression",
  "Fear on the Face at Different Intensities - Facial Expression",
  "Hiding and Faking Fear: What Leaks Through - Facial Expression",
  "Drawing Fear: Notes for Artists and Actors - Facial Expression"
 ],
 "Triggers": [
  "Classic Fear Triggers - Triggers",
  "Personal Fear Triggers: Memories and Associations - Triggers",
  "Surprise Triggers: The Odd and Unexpected - Triggers",
  "Fear Chain Reactions: From One Trigger to Many - Triggers"
 ],
 "Fear in Behavior": [
  "What People Do When Afraid - Fear in Behavior",
  "What People Say When Afraid: Words, Tone, Speech - Fear in Behavior",
  "How Fear Changes Decisions and Judgment - Fear in Behavior",
  "Fear Under Rising Intensity: Escalating Behavior - Fear in Behavior"
 ],
 "Healthy Expression": [
  "Expressing Fear in Healthy Ways - Healthy Expression",
  "Bottled or Exploding: The Costs of Unhealthy Expression - Healthy Expression",
  "Everyday Practices That Keep Fear in Balance - Healthy Expression"
 ],
 "Recognizing Fear in Others": [
  "Reading Fear in Others: Face, Body, Voice, Behavior - Recognizing Fear in Others",
  "What to Say and Do When Someone Is Afraid - Recognizing Fear in Others",
  "What NOT to Do Around a Frightened Person - Recognizing Fear in Others"
 ],
 "Emotion Mixes and Simulation": [
  "The Neighbors and Opposites of Fear: A Related-Emotions Map - Emotion Mixes and Simulation",
  "Fear in Blends: Dyads With Other Emotions - Emotion Mixes and Simulation",
  "Fear From Trigger to Resolution: A Full Behavioral Simulation - Emotion Mixes and Simulation"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fear Emotion Study — "+safe+"\n"
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
    demo:{kind:"fear-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-fear-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-fear',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
