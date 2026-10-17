(function(){'use strict';
/* JAH The Psychometrics Signature Database generator — jahdb-psychometrics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Psychometrics Is: The Science of Psychological Measurement (Signature Edition) - Foundations",
  "Levels of Measurement: Nominal, Ordinal, Interval, Ratio (Signature Edition) - Foundations",
  "The True-Score Model: X = T + E (Signature Edition) - Foundations",
  "Reliability: The Signal in the Noise (Signature Edition) - Foundations",
  "Test-Retest Reliability: Stability Across Time (Signature Edition) - Foundations",
  "Split-Half and Internal Consistency: One Test, Two Halves (Signature Edition) - Foundations",
  "Cronbach's Alpha: The Workhorse of Internal Consistency (Signature Edition) - Foundations",
  "Kuder-Richardson Formulas: Reliability for Right-or-Wrong Items (Signature Edition) - Foundations",
  "Standard Error of Measurement: The Margin Around Every Score (Signature Edition) - Foundations",
  "Validity: Does the Test Measure What It Claims? (Signature Edition) - Foundations",
  "Content Validity: Does the Test Cover the Territory? (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Criterion Validity: Predicting Real Outcomes (Signature Edition) - Compounded",
  "Construct Validity: The Master Argument (Signature Edition) - Compounded",
  "Convergent and Discriminant Validity: The Company Scores Keep (Signature Edition) - Compounded",
  "Item Analysis: Difficulty and Discrimination (Signature Edition) - Compounded",
  "Distractor Analysis: Reading the Wrong Answers (Signature Edition) - Compounded",
  "Test Length and the Spearman-Brown Prophecy Formula (Signature Edition) - Compounded",
  "Interrater Reliability: When Humans Are the Instrument (Signature Edition) - Compounded",
  "Cohen's Kappa: Agreement Beyond Chance (Signature Edition) - Compounded",
  "Norming and Standardization: Giving Scores Meaning (Signature Edition) - Compounded",
  "Standard Scores: z, T, Stanines, and the IQ Scale (Signature Edition) - Compounded",
  "Cognitive Ability Testing: Measuring the Mind's Engine (Signature Edition) - Compounded",
  "Personality Measurement: Scaling the Self (Signature Edition) - Compounded",
  "Factor Analysis: Finding the Hidden Dimensions (Signature Edition) - Compounded",
  "Exploratory vs Confirmatory Factor Analysis: Discovery vs Proof (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Item Response Theory: The Rasch (1PL) Model (Signature Edition) - Advanced",
  "The 2PL and 3PL Models: Discrimination and Guessing (Signature Edition) - Advanced",
  "Item and Test Information: Precision Where It Counts (Signature Edition) - Advanced",
  "Differential Item Functioning: The Fairness Microscope (Signature Edition) - Advanced",
  "Test Equating: Making Different Forms Interchangeable (Signature Edition) - Advanced",
  "Vertical Scaling: One Ruler for Many Grades (Signature Edition) - Advanced",
  "Computerized Adaptive Testing: The Test That Listens (Signature Edition) - Advanced",
  "Test Fairness and Bias: Impact Is Not Bias (Signature Edition) - Advanced",
  "Generalizability Theory: Reliability Grown Up (Signature Edition) - Advanced",
  "Structural Equation Modeling: Theories as Equations (Signature Edition) - Advanced",
  "The Standards for Educational and Psychological Testing (Signature Edition) - Advanced",
  "Building a Test: The Full Professional Workflow (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Psychometrics Study — "+safe+"\n"
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
    name:topic+' — psychometrics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A psychometrics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"psychometrics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-psychometrics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('psychometrics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
