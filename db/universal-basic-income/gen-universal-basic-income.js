(function(){'use strict';
/* Signature Universal Basic Income Database generator — jahdb-universal-basic-income-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-UBI-';
var TOPICS=[["What UBI Is", "Unconditional cash for everyone; the simplicity is the point."], ["The Alaska Permanent Fund", "Oil dividends since 1982; the longest-running example."], ["Finland's 2017 Experiment", "2,000 unemployed got monthly payments; wellbeing rose, employment didn't."], ["Kenya's GiveDirectly Trial", "The largest UBI experiment; results show real benefits."], ["Stockton's SEED Program", "Mayor Tubbs's pilot; employment actually rose."], ["The Mincome Experiment", "1970s Manitoba trial; health and education improved."], ["Iran's Cash Transfers", "Nationwide payments since 2010; the scale is unmatched."], ["How to Pay for It", "Taxes, dividends, or money creation; the math is debated."], ["UBI vs. Welfare", "Replacing bureaucracy with cash; the efficiency argument."], ["The Work Disincentive Question", "Do people stop working?; evidence says mostly no."], ["Automation Justification", "Robots take jobs, UBI shares gains; the logic is popular."], ["Milton Friedman's Negative Income Tax", "The conservative case; the idea crosses ideologies."], ["MLK's Support", "The civil rights leader backed guaranteed income; the history is deep."], ["The 2020 Pandemic Checks", "Stimulus as accidental UBI; the natural experiment."], ["Crypto UBI Projects", "Worldcoin and others; the tech experiments."], ["UBI and Gender", "Cash empowers caregivers; the feminist case."], ["UBI and Health", "Pilots show better mental health; the mechanism is security."], ["The Freedom Dividend", "Andrew Yang's $1,000/month; the campaign mainstreamed it."], ["UBI Pilots Worldwide Map", "Dozens of trials; the evidence base grows."], ["Criticisms: Inflation", "Would landlords capture it?; the concern is serious."], ["Criticisms: Affordability", "The price tag is trillions; the funding gap."], ["Partial vs. Full UBI", "Modest payments vs. livable; the design spectrum."], ["UBI and Immigration", "Who qualifies?; the boundary question."], ["The Political Prospects", "Support rises in crises; the window opens and closes."], ["Alternative: Job Guarantee", "The rival proposal; the debate continues."], ["Alternative: Basic Services", "Free housing and healthcare instead; the UBS model."], ["What Experiments Teach", "Cash works, design matters; the lessons accumulate."], ["The 2030 Outlook", "More pilots, no national UBI yet; the trajectory is gradual."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'universal basic income exploration', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('universal-basic-income',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();