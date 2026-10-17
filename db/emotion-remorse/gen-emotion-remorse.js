(function(){'use strict';
/* JAH The Remorse Emotion Database generator — jahdb-emotion-remorse-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMRM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Remorse Is: A Plain-Language Definition - Foundations",
  "Remorse in the Emotion Family - Foundations",
  "How Strong Remorse Can Get: Mild, Moderate, Intense - Foundations",
  "Myths and Misunderstandings About Remorse - Foundations",
  "Inside Remorse: A First-Person Passage - Foundations",
  "Remorse Over Time: Onset, Peak, Fading, Aftershock - Foundations",
  "Remorse at Low Intensity vs High Intensity: Two Snapshots - Foundations",
  "Remorse Mixed With Guilt: The Most Common Partnership - Foundations",
  "A Day With Remorse: The Emotion Running Through an Ordinary Day - Foundations"
 ],
 "Compounded": [
  "What Remorse Does in the Body - Compounded",
  "The Posture and Movement Signature of Remorse - Compounded",
  "Remorse, Sleep, Appetite, and Energy - Compounded",
  "How Remorse Feels Different in Different Bodies - Compounded",
  "The Face of Remorse: Eyes, Brows, Mouth, and Micro-Signs - Compounded",
  "The Face of Remorse Across Intensities - Compounded",
  "Hiding or Faking Remorse: What Leaks Through - Compounded",
  "Remorse in Words for Artists and Actors - Compounded",
  "The Classic Triggers of Remorse - Compounded",
  "Personal Triggers: Memory, Anniversaries, Private Associations - Compounded",
  "Surprise Triggers: The Unexpected Sparks of Remorse - Compounded",
  "Chain Reactions: One Trigger, a Cascade of Emotions - Compounded"
 ],
 "Advanced": [
  "What People Do When They Feel Remorse - Advanced",
  "What People Say When They Feel Remorse - Advanced",
  "How Remorse Changes Decisions and Judgment - Advanced",
  "Remorse Under Pressure: How Behavior Escalates - Advanced",
  "Healthy Expression of Remorse - Advanced",
  "Unhealthy Expression: Bottling Up or Boiling Over - Advanced",
  "Everyday Practices That Keep Remorse in Balance - Advanced",
  "Reading Remorse in Other People - Advanced",
  "How to Respond When Someone Feels Remorse - Advanced",
  "Mistakes to Avoid Around Someone Feeling Remorse - Advanced",
  "The Remorse Neighborhood: Guilt, Regret, Shame, Contrition - Advanced",
  "Remorse Blends: Dyads With Four Partner Emotions - Advanced",
  "Full Simulation: Remorse From Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Remorse Emotion Study — "+safe+"\n"
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
    demo:{kind:"remorse-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-remorse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-remorse',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
