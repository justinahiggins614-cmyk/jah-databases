(function(){'use strict';
/* JAH The Jealousy Emotion Database generator — jahdb-emotion-jealousy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMJE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Jealousy Is: A Plain-Language Definition - Foundations",
  "Jealousy in the Emotion Family: A Complex Emotion's Roots - Foundations",
  "How Strong Jealousy Can Get: Mild, Moderate, and Intense - Foundations",
  "Myths and Misunderstandings About Jealousy - Foundations",
  "Inside the Feeling: Jealousy in the First Person - Foundations",
  "How Jealousy Changes Over Time: Onset, Peak, and Fading - Foundations",
  "Jealousy at Low Intensity Versus High Intensity - Foundations",
  "Jealousy Mixed with Fear: The Feeling's Most Common Partner - Foundations",
  "A Day in the Life: Jealousy Running Through an Ordinary Day - Foundations"
 ],
 "Compounded": [
  "Jealousy in the Body: Heart, Breath, Muscles, Stomach, and Skin - Compounded",
  "Posture and Movement: How the Body Carries Jealousy - Compounded",
  "Sleep, Appetite, and Energy Under Jealousy - Compounded",
  "How Jealousy Feels in Different Bodies: No Two Alike - Compounded",
  "The Face of Jealousy: Eyes, Brows, Mouth, and Micro-Signs - Compounded",
  "How the Jealous Expression Changes with Intensity - Compounded",
  "Hiding and Faking Jealousy: What Leaks Through - Compounded",
  "Expression Gallery Notes: Drawing and Playing Jealousy - Compounded",
  "The Classic Triggers of Jealousy - Compounded",
  "Personal Triggers: Memories, Anniversaries, and Private Associations - Compounded",
  "Surprise Triggers: The Unexpected Things That Spark Jealousy - Compounded",
  "Chain Reactions: How One Jealous Trigger Sets Off a Cascade - Compounded"
 ],
 "Advanced": [
  "What People Do When They Feel Jealous: Actions and Reactions - Advanced",
  "What Jealous People Say: Phrases, Tone, and Speech Patterns - Advanced",
  "How Jealousy Changes Decisions and Judgment - Advanced",
  "Jealousy Under Intensity: How Actions Escalate - Advanced",
  "Healthy Expression: Saying, Showing, and Channeling Jealousy Well - Advanced",
  "Unhealthy Expression: Bottling Up or Exploding - What Each Costs - Advanced",
  "Everyday Practices: Small Habits That Keep Jealousy in Balance - Advanced",
  "Reading the Signs: Jealousy in Other People - Advanced",
  "What to Say and Do When Someone Near You Feels Jealous - Advanced",
  "What NOT to Do: Mistakes That Make Jealousy Worse - Advanced",
  "The Jealousy Neighborhood: Related Emotions, Opposites, and Close Cousins - Advanced",
  "Jealousy Blends: This Emotion Mixed with Four Others - Advanced",
  "Full Behavioral Simulation: Jealousy from Trigger to Resolution - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Jealousy Emotion Study — "+safe+"\n"
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
    demo:{kind:"jealousy-emotion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emotion-jealousy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emotion-jealousy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
