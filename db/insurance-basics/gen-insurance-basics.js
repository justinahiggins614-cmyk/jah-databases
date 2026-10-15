(function(){'use strict';
/* Insurance Basics Database generator — jahdb-insurance-basics-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-INSUR-BAS-';
var TOPICS=[["What Is Insurance", "Paying a small regular amount to protect against large losses."], ["Premiums", "The regular payments that keep a policy active."], ["Deductibles", "The amount paid out of pocket before insurance helps."], ["Policies", "The contracts spelling out what insurance covers."], ["Claims", "Requests for the insurer to pay for a covered loss."], ["Coverage", "What a policy protects against."], ["Health Insurance", "Coverage for medical care costs."], ["Auto Insurance", "Coverage for vehicle damage and liability."], ["Homeowners Insurance", "Protection for houses against damage and theft."], ["Renters Insurance", "Coverage for tenants' belongings and liability."], ["Life Insurance", "Payments to beneficiaries after the policyholder's death."], ["Term Life Insurance", "Life coverage for a set number of years."], ["Whole Life Insurance", "Lifelong coverage that builds cash value."], ["Liability", "Responsibility for harm to others, a core thing insurance covers."], ["Risk", "The chance of loss that insurance is priced on."], ["Underwriting", "How insurers evaluate risk before issuing a policy."], ["Copayments", "Fixed amounts paid for medical visits under a health plan."], ["Exclusions", "What a policy does not cover."], ["Beneficiaries", "The people who receive insurance payouts."], ["Umbrella Policies", "Extra liability coverage beyond standard limits."], ["Disability Insurance", "Income protection if injury or illness prevents work."], ["Travel Insurance", "Coverage for trip cancellations and medical emergencies abroad."], ["Flood Insurance", "Separate coverage for flood damage."], ["Insurance Agents", "The professionals who sell and service policies."], ["Shopping for Insurance", "Comparing quotes, coverage, and company reputation."], ["Filing a Claim", "Documenting losses and working with adjusters."], ["Insurance Fraud", "False claims that raise costs for everyone."], ["Self-Insurance", "Setting aside your own funds instead of buying coverage."]];
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
    type:'insurance basics record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('insurance-basics',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();