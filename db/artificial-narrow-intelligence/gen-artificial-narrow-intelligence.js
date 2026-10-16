(function(){'use strict';
/* JAH The Artificial Narrow Intelligence Database generator — jahdb-artificial-narrow-intelligence-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NARAI-";
var FIELDS=["intelligence-scale abilities"];
var TOPICS={
 "intelligence-scale abilities": [
  "Machine Vision Object Recognition \u2014 intelligence-scale abilities",
  "Machine Vision Object Recognition (Signature Edition) \u2014 intelligence-scale abilities",
  "Automatic Speech Recognition \u2014 intelligence-scale abilities",
  "Automatic Speech Recognition (Signature Edition) \u2014 intelligence-scale abilities",
  "Machine Translation \u2014 intelligence-scale abilities",
  "Machine Translation (Signature Edition) \u2014 intelligence-scale abilities",
  "Game-Playing Agents \u2014 intelligence-scale abilities",
  "Game-Playing Agents (Signature Edition) \u2014 intelligence-scale abilities",
  "Protein Structure Prediction \u2014 intelligence-scale abilities",
  "Protein Structure Prediction (Signature Edition) \u2014 intelligence-scale abilities",
  "Robotic Manipulation \u2014 intelligence-scale abilities",
  "Robotic Manipulation (Signature Edition) \u2014 intelligence-scale abilities",
  "Recommender Systems \u2014 intelligence-scale abilities",
  "Recommender Systems (Signature Edition) \u2014 intelligence-scale abilities",
  "Industrial Anomaly Detection \u2014 intelligence-scale abilities",
  "Industrial Anomaly Detection (Signature Edition) \u2014 intelligence-scale abilities",
  "Medical Image Diagnosis Assistance \u2014 intelligence-scale abilities",
  "Medical Image Diagnosis Assistance (Signature Edition) \u2014 intelligence-scale abilities",
  "Autonomous Vehicle Perception \u2014 intelligence-scale abilities",
  "Autonomous Vehicle Perception (Signature Edition) \u2014 intelligence-scale abilities"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Artificial Narrow Intelligence — "+safe+"\n"
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
    name:topic+' — narrow AI ability',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A narrow AI ability of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-artificial-narrow-intelligence-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('artificial-narrow-intelligence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
