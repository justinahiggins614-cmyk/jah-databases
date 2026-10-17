(function(){'use strict';
/* JAH The Unsolved Neuroscience Database generator — jahdb-unsolved-neuroscience-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why We Dream - Foundations",
  "What Attention Is - Foundations",
  "Why We Forget - Foundations",
  "How Memories Are Consolidated - Foundations",
  "What Causes Deja Vu - Foundations",
  "How the Brain Learns From Prediction Errors - Foundations",
  "What Pain Is in the Brain - Foundations",
  "How the Brain Feels Its Own Body - Foundations",
  "How the Brain Learns From Very Few Examples - Foundations",
  "How the Brain Represents Space - Foundations",
  "How Working Memory Holds So Little - Foundations",
  "How the Brain Predicts and Cancels Its Own Sensations - Foundations"
 ],
 "Compounded": [
  "What the Full Function of Sleep Is - Compounded",
  "How Information Is Encoded in Spike Trains - Compounded",
  "The Binding Problem - Compounded",
  "The Physical Basis of Memory - Compounded",
  "The Rules of Neuroplasticity - Compounded",
  "How the Brain Decides - Compounded",
  "The Neural Basis of Emotion - Compounded",
  "The Neural Basis of Language Comprehension - Compounded",
  "The Neural Basis of Creativity - Compounded",
  "How the Brain Learns for a Lifetime Without Catastrophic Forgetting - Compounded",
  "How General Anesthesia Switches Consciousness Off and On - Compounded",
  "The Neural Correlates of Volition - Compounded"
 ],
 "Advanced": [
  "The Neural Correlates of Consciousness - Advanced",
  "How the Brain Ages - Advanced",
  "Brain-Computer Interface Limits - Advanced",
  "How the Brain Repairs Itself - Advanced",
  "The Receptor-to-Experience Gap - Advanced",
  "The Circuit Basis of Psychosis - Advanced",
  "How to Map and Model the Whole Human Brain - Advanced",
  "The Neural Basis of the Self - Advanced",
  "The Hard Problem of Consciousness - Advanced",
  "A Complete Computational Theory of the Human Brain - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Neuroscience Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-neuroscience-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-neuroscience-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-neuroscience',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
