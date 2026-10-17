(function(){'use strict';
/* JAH The Scientific Method Basics Signature Database generator — jahdb-scientific-method-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCIMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Science (Signature Edition) - Foundations",
  "The Role of Curiosity in Discovery (Signature Edition) - Foundations",
  "Observation: The Starting Point of Inquiry (Signature Edition) - Foundations",
  "Asking Testable Questions (Signature Edition) - Foundations",
  "The Hypothesis: An Educated Prediction (Signature Edition) - Foundations",
  "Fair Experiments and Controls (Signature Edition) - Foundations",
  "Independent and Dependent Variables (Signature Edition) - Foundations",
  "Controlled Variables (Signature Edition) - Foundations",
  "Operational Definitions (Signature Edition) - Foundations",
  "Collecting and Recording Data (Signature Edition) - Foundations",
  "Tables Charts and Graphs (Signature Edition) - Foundations",
  "Drawing Conclusions (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Measurement Accuracy and Precision (Signature Edition) - Compounded",
  "Experimental Error (Signature Edition) - Compounded",
  "Forming an Experimental Design (Signature Edition) - Compounded",
  "Sample Size and Statistics (Signature Edition) - Compounded",
  "Analyzing Data with Averages and Trends (Signature Edition) - Compounded",
  "Correlation and Causation (Signature Edition) - Compounded",
  "The Placebo Effect and Blinding (Signature Edition) - Compounded",
  "Predictions and Models (Signature Edition) - Compounded",
  "Falsifiability (Signature Edition) - Compounded",
  "Data Interpretation Pitfalls (Signature Edition) - Compounded",
  "Writing a Scientific Report (Signature Edition) - Compounded",
  "Scientific Instruments and Tools (Signature Edition) - Compounded",
  "Repeating and Reproducing Results (Signature Edition) - Compounded",
  "Peer Review and Publishing (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Scientific Theories vs Hypotheses (Signature Edition) - Advanced",
  "The Limits of Science (Signature Edition) - Advanced",
  "Ethics in Scientific Research (Signature Edition) - Advanced",
  "The Feedback Loop of Inquiry (Signature Edition) - Advanced",
  "Case Study: The Discovery of Penicillin (Signature Edition) - Advanced",
  "Case Study: Ignaz Semmelweis and Handwashing (Signature Edition) - Advanced",
  "Case Study: The Michelson-Morley Experiment (Signature Edition) - Advanced",
  "Scientific Method in Everyday Life (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Scientific Method Study — "+safe+"\n"
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
    name:topic+' — scientific method record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A scientific method record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"scientific-method-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-scientific-method-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-method-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
