(function(){'use strict';
/* JAH The Pride Emotion Database generator — jahdb-emotion-pride-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMPR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Pride Is: A Plain-Language Definition - Foundations",
  "Pride in the Emotion Family: A Self-Conscious Emotion - Foundations",
  "The Three Volumes of Pride: Mild, Moderate, and Intense - Foundations",
  "Myths and Misunderstandings About Pride - Foundations",
  "Inside Pride: A First-Person Passage - Foundations",
  "The Time Course of Pride: Onset, Peak, Fading, Aftershock - Foundations",
  "Pride at Low Intensity Versus High Intensity - Foundations",
  "Pride Mixed With Joy: The Triumph Blend - Foundations",
  "A Day With Pride: An Ordinary-Day Vignette - Foundations"
 ],
 "Compounded": [
  "The Body on Pride: Heart, Breath, Muscles, and Energy - Compounded",
  "The Pride Posture: How the Body Carries It - Compounded",
  "Pride, Sleep, Appetite, and Energy - Compounded",
  "No Two Bodies React Alike: Individual Differences - Compounded",
  "The Face of Pride: Eyes, Brows, Mouth, and Tell-Tale Signs - Compounded",
  "The Pride Face Across Intensities - Compounded",
  "Hiding and Faking Pride: What Leaks Through - Compounded",
  "Expression Gallery: Drawing and Playing Pride - Compounded",
  "The Classic Triggers of Pride - Compounded"
 ],
 "Advanced": [
  "Personal Triggers: Memories and Private Associations - Advanced",
  "Surprise Triggers: The Unexpected Pride Set-Offs - Advanced",
  "Chain Reactions: Pride's Emotional Cascades - Advanced",
  "What People Do When They Feel Pride - Advanced",
  "What People Say: The Sound of Pride - Advanced",
  "Pride and Judgment: How It Changes Decisions - Advanced",
  "Escalation: Pride Under Rising Intensity - Advanced",
  "Expressing Pride Healthily - Advanced",
  "Bottling and Exploding: The Costs of Unhealthy Pride - Advanced",
  "Everyday Practices: Keeping Pride in Balance - Advanced",
  "Reading Pride in Others - Advanced",
  "Supportive Responses: What to Say and Do - Advanced",
  "What Not to Do: Mistakes That Make It Worse - Advanced",
  "The Pride Neighborhood: Related Emotions Mapped - Advanced",
  "Pride Blends: Four Plutchik-Style Dyads - Advanced",
  "Full Behavioral Simulation: One Pride From Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Pride Emotion Study — "+safe+"\n"
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
    demo:{kind:"pride-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-pride-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-pride',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
