(function(){'use strict';
/* Signature Remote Work Database generator — jahdb-remote-work-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-REMOTE-';
var TOPICS=[["The Pandemic Shift", "2020's experiment; the scale."], ["The Great Resignation", "The reevaluation; the leverage."], ["Return-to-Office Fights", "The mandates; the resistance."], ["The Hybrid Compromise", "The 3-2 split; the norm."], ["Digital Nomad Visas", "The countries compete; the programs."], ["The Home Office Setup", "The ergonomics; the gear."], ["Async Communication", "The documentation; the culture."], ["Zoom Fatigue", "The exhaustion; the research."], ["The Collaboration Tools", "Slack to Notion; the stack."], ["Managing Remotely", "The trust; the outcomes."], ["The Proximity Bias", "The visibility; the inequity."], ["Hiring Globally", "The talent pool; the compliance."], ["The Salary Geography", "The location pay; the debates."], ["Time Zone Hell", "The coordination; the strategies."], ["The Loneliness Problem", "The isolation; the solutions."], ["Work-Life Boundaries", "The blur; the rituals."], ["The Right to Disconnect", "The laws; the movement."], ["Rural Revival", "The Zoom towns; the impact."], ["The Office's Future", "The clubhouse; the redesign."], ["Commercial Real Estate", "The vacancy; the conversion."], ["The Environmental Win", "The commute cut; the data."], ["Cybersecurity at Home", "The risks; the zero trust."], ["The Four-Day Week Link", "The flexibility; the pilots."], ["Freelance Platforms", "The marketplaces; the gig."], ["The 2030 Workplace", "The distributed; the prediction."], ["The Culture Question", "Building belonging; the rituals."], ["Measuring Output", "The results; the metrics."], ["The Verdict", "The hybrid wins; the nuance."]];
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
    type:'remote work exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('remote-work',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();