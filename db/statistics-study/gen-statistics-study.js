(function(){'use strict';
var SLUG="statistics-study";
var FIELD="Statistics";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-statistics-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Descriptive statistics","summarize datasets with centers, spreads, and shapes, choosing honest visualizations","the median resists outliers that move the mean - robust summaries tell the truth about skewed data","findings hold for univariate summaries; multivariate data needs more","match the summary to the shape"],["Probability distributions","fit binomial, normal, and Poisson models, testing fit against observed frequencies","the normal distribution emerges from sums - the central limit theorem explains its ubiquity","findings hold for sums of independent variables; dependence changes the story","sums become normal"],["Hypothesis testing","run t-tests and chi-square tests, interpreting p-values against significance levels","the p-value is not the probability the hypothesis is true - misreading it is statistics' most common error","findings hold for the frequentist framework; Bayesian methods answer different questions","p is not the probability"],["Confidence intervals","construct intervals for means and proportions, checking coverage by simulation","a 95% interval captures the parameter 95% of the time in repeated sampling - the confidence is in the method","findings hold for the procedure; any single interval either covers or not","confidence is in the method"],["Regression analysis","fit linear models, checking residuals for the assumptions the model requires","residual plots diagnose every regression failure - the assumptions are checked in the residuals, not the raw data","findings hold for linear models; the diagnostic logic generalizes","plot the residuals"],["Bayesian inference","update priors with likelihoods, computing posteriors for estimation problems","Bayes' rule is the optimal way to update beliefs - no other rule uses the evidence as efficiently","findings hold given the prior; sensitivity analysis tests its influence","update with the evidence"],["Sampling methods","design random, stratified, and cluster samples, computing standard errors","random sampling beats large convenience samples - representativeness, not size, controls bias","findings hold for probability samples; non-probability samples need caveats","random beats large"],["Experimental design","randomize treatments and block on confounders, powering the study adequately","randomization balances the unmeasured confounders - it is the reason experiments beat observations","findings hold for randomized designs; the logic is causal","randomize to cause"],["ANOVA","partition variance across groups, testing whether group means differ","ANOVA tests all groups at once, controlling the error rate that multiple t-tests inflate","findings hold under the usual assumptions; the F-test is the workhorse","one test for all groups"],["Time series","decompose trends, seasonality, and noise, forecasting with ARIMA-style models","differencing stationarizes most series - the trend must be removed before the model can see the signal","findings hold for stationary-transformable series; structural breaks need intervention","stationarize first"],["Nonparametric methods","apply rank-based tests when assumptions fail, comparing power to parametric tests","rank tests lose little power when assumptions hold and keep working when they fail - robustness is nearly free","findings hold for the standard rank tests; the efficiency results are classical","ranks resist violations"],["Survey methodology","design questionnaires and sampling frames, adjusting for nonresponse","question wording moves answers more than sampling error - the instrument is the largest error source","findings hold for human surveys; the wording effects are measured","words move answers"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  if(CATS.indexOf(cat)<0)cat=pick(CATS,rnd);
  var tp=pick(TOPICS,rnd),angle=pick(ANGLES,rnd),fr=FRAMING[cat];
  var title=fr.label+' \u2014 '+tp[0]+' ('+angle+')';
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,signature_title:title,field:FIELD,version:'Signature',
    system_lens_review:'System-lens review: '+tp[3],
    refined_findings:'Refined analysis: '+tp[2]+' '+tp[4],
    experiment_solver:{method:fr.pre+tp[1]+fr.post,findings:tp[2]},
    scholar_notes:'Signature version \u2014 scholar notes: '+tp[4],
    year:2026,source:'signature',_seed:seed,_cat:cat};
}
var KEYS=['id','signature_title','field','version','system_lens_review','refined_findings','experiment_solver','scholar_notes','year','source'];
function nonEmptyString(v){return typeof v==='string'&&v.length>0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  KEYS.forEach(function(k){if(r[k]===undefined||r[k]===null)e.push('missing:'+k);});
  Object.keys(r).forEach(function(k){if(KEYS.indexOf(k)<0&&k!=='_seed'&&k!=='_cat')e.push('extra:'+k);});
  if(!/^JAH-[a-z0-9-]+-S-\d{6}$/.test(r.id||''))e.push('id');
  if(!nonEmptyString(r.signature_title))e.push('signature_title');
  if(r.field!==FIELD)e.push('field');
  if(r.version!=='Signature')e.push('version');
  if(!nonEmptyString(r.system_lens_review))e.push('system_lens_review');
  if(!nonEmptyString(r.refined_findings))e.push('refined_findings');
  var es=r.experiment_solver;
  if(!es||typeof es!=='object'||!nonEmptyString(es.method)||!nonEmptyString(es.findings))e.push('experiment_solver');
  if(!nonEmptyString(r.scholar_notes))e.push('scholar_notes');
  if(r.year!==2026)e.push('year');
  if(r.source!=='signature')e.push('source');
  if(r._cat!==undefined&&CATS.indexOf(r._cat)<0)e.push('_cat');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){var s=sample[i];
    if(s&&s.id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-'+SLUG+'-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
