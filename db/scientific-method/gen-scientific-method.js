(function(){'use strict';
/* JAH The Scientific Method Basics Database generator — jahdb-scientific-method-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCIM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Science - Foundations",
  "The Role of Curiosity in Discovery - Foundations",
  "Observation: The Starting Point of Inquiry - Foundations",
  "Asking Testable Questions - Foundations",
  "The Hypothesis: An Educated Prediction - Foundations",
  "Fair Experiments and Controls - Foundations",
  "Independent and Dependent Variables - Foundations",
  "Controlled Variables - Foundations",
  "Operational Definitions - Foundations",
  "Collecting and Recording Data - Foundations",
  "Tables Charts and Graphs - Foundations",
  "Drawing Conclusions - Foundations"
 ],
 "Compounded": [
  "Measurement Accuracy and Precision - Compounded",
  "Experimental Error - Compounded",
  "Forming an Experimental Design - Compounded",
  "Sample Size and Statistics - Compounded",
  "Analyzing Data with Averages and Trends - Compounded",
  "Correlation and Causation - Compounded",
  "The Placebo Effect and Blinding - Compounded",
  "Predictions and Models - Compounded",
  "Falsifiability - Compounded",
  "Data Interpretation Pitfalls - Compounded",
  "Writing a Scientific Report - Compounded",
  "Scientific Instruments and Tools - Compounded",
  "Repeating and Reproducing Results - Compounded",
  "Peer Review and Publishing - Compounded"
 ],
 "Advanced": [
  "Scientific Theories vs Hypotheses - Advanced",
  "The Limits of Science - Advanced",
  "Ethics in Scientific Research - Advanced",
  "The Feedback Loop of Inquiry - Advanced",
  "Case Study: The Discovery of Penicillin - Advanced",
  "Case Study: Ignaz Semmelweis and Handwashing - Advanced",
  "Case Study: The Michelson-Morley Experiment - Advanced",
  "Scientific Method in Everyday Life - Advanced"
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
var gen={version:'jahdb-scientific-method-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-method',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
