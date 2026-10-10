(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="statistics-study";
var SLUG="statistics-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-statistics-study-published-P-";
var FIELD="Statistics";
var GENVER="jahdb-statistics-study-published-1.0";
var CATS=["Probability Theory", "Regression Analysis", "Bayesian Methods", "Experimental Design", "Time Series", "Multivariate Analysis", "Data Visualization", "Statistical Inference"];
var L1=[["The Design of Experiments", ["Ronald A. Fisher"], "Oliver & Boyd, Edinburgh", 1935, 3, "Fisher's founding text of experimental design — randomization, the lady tasting tea, ANOVA. The 20th century's most influential statistics book. Experiments, designed."], ["Statistical Methods for Research Workers", ["Ronald A. Fisher"], "Oliver & Boyd, Edinburgh", 1925, 7, "Fisher's handbook that taught scientists significance testing — the small-sample revolution. Controversial and indispensable. The p-value's origin."], ["The Lady Tasting Tea", ["David Salsburg"], "W. H. Freeman", 2001, 7, "Salsburg's history of statistics through its personalities — Fisher, Gosset, Neyman. The revolution's human story. Tea, tasted."], ["The Theory That Would Not Die", ["Sharon Bertsch McGrayne"], "Yale University Press", 2011, 2, "McGrayne's history of Bayes' rule — from Laplace to Enigma to modern AI. The rule that wouldn't die. Bayes, vindicated."], ["How to Lie with Statistics", ["Darrell Huff"], "W. W. Norton", 1954, 6, "Huff's illustrated exposé of statistical deception — the best-selling statistics book ever. The classic of critical reading. Lies, damned lies, and graphics."], ["The Signal and the Noise", ["Nate Silver"], "Penguin Press", 2012, 6, "Silver's tour of prediction — from baseball to earthquakes — on separating signal from noise. Bayesian thinking for the public. Forecasting, humbled."], ["Naked Statistics", ["Charles Wheelan"], "W. W. Norton", 2013, 7, "Wheelan's stats without the math — stripping the subject to intuition. The friendliest introduction. Statistics, naked."], ["The Art of Statistics", ["David Spiegelhalter"], "Pelican Books", 2019, 7, "Spiegelhalter's masterclass in learning from data — the Winton professor's wisdom. The modern classic. Data, honestly."], ["The Book of Why", ["Judea Pearl", "Dana Mackenzie"], "Basic Books", 2018, 2, "Pearl's causal revolution — the ladder of causation, do-calculus, and why correlation isn't enough. Causality's manifesto. Why, answered."], ["Causality", ["Judea Pearl"], "Cambridge University Press", 2000, 2, "Pearl's technical foundation of causal inference — structural models and the do-operator. The field's bible. Causes, formalized."], ["Thinking, Fast and Slow", ["Daniel Kahneman"], "Farrar, Straus and Giroux", 2011, 7, "Kahneman's Nobel-winning account of judgment under uncertainty — biases, heuristics, and the two systems. Psychology's most important book. Thinking, examined."], ["Fooled by Randomness", ["Nassim Nicholas Taleb"], "Texere", 2001, 0, "Taleb's meditation on luck in markets and life — the hidden role of chance. The first of the Incerto. Randomness, unfooled."], ["The Black Swan", ["Nassim Nicholas Taleb"], "Random House", 2007, 0, "Taleb's theory of high-impact rare events — why we can't predict them. The 2008 crisis made him a prophet. Swans, black."], ["The Drunkard's Walk", ["Leonard Mlodinow"], "Pantheon Books", 2008, 0, "Mlodinow's randomness in everyday life — the mathematics of chance made vivid. The walk, explained. Chance, everywhere."], ["Innumeracy", ["John Allen Paulos"], "Hill and Wang", 1988, 6, "Paulos on mathematical illiteracy — its costs in public life and its cures in the classroom. The 1988 bestseller that named the problem. Numbers, feared no longer."], ["A Mathematician Reads the Newspaper", ["John Allen Paulos"], "Basic Books", 1995, 6, "Paulos dissects the numbers in the news — from polls to prisons. The sequel's delight. News, quantified."], ["The Elements of Statistical Learning", ["Trevor Hastie", "Robert Tibshirani", "Jerome Friedman"], "Springer", 2001, 1, "The machine learning bible — data mining, inference, and prediction. The standard graduate text. Learning, elementized."], ["An Introduction to Statistical Learning", ["Gareth James", "Daniela Witten", "Trevor Hastie", "Robert Tibshirani"], "Springer", 2013, 1, "The accessible ISL — statistical learning in R for practitioners. The classroom favorite. Learning, introduced."], ["Bayesian Data Analysis", ["Andrew Gelman", "John B. Carlin", "Hal S. Stern", "David B. Dunson", "Aki Vehtari", "Donald B. Rubin"], "Chapman & Hall", 1995, 2, "Gelman et al.'s comprehensive Bayesian modeling — the practitioner's reference through three editions. The Bayesian bible. Data, analyzed."], ["Statistical Rethinking", ["Richard McElreath"], "Chapman & Hall", 2015, 2, "McElreath's rethinking — causal models before statistical models. The beloved lectures in book form. Thinking, statistically."], ["Doing Bayesian Data Analysis", ["John K. Kruschke"], "Academic Press", 2010, 2, "Kruschke's puppies-and-BUGS introduction to Bayesian analysis — the gentlest on-ramp to the subject. Beloved by beginners. Bayes, explained with dogs."], ["Time Series Analysis: Forecasting and Control", ["George E. P. Box", "Gwilym M. Jenkins"], "Holden-Day", 1970, 4, "Box and Jenkins's ARIMA methodology — the forecaster's handbook. The standard for decades. Series, analyzed."], ["Categorical Data Analysis", ["Alan Agresti"], "John Wiley & Sons", 1990, 1, "Agresti's definitive treatment of categorical data — contingency tables and logistic models. The categorical bible. Categories, modeled."], ["Generalized Linear Models", ["Peter McCullagh", "John A. Nelder"], "Chapman & Hall", 1983, 1, "McCullagh and Nelder's unifying framework — GLMs for everything. The 1983 revolution. Linearity, generalized."], ["The Cult of Statistical Significance", ["Stephen T. Ziliak", "Deirdre N. McCloskey"], "University of Michigan Press", 2008, 7, "Ziliak and McCloskey's indictment of significance testing without substance. The sizeless stare. Significance, questioned."], ["Statistics as Principled Argument", ["Robert P. Abelson"], "Lawrence Erlbaum", 1995, 7, "Abelson's MAGIC criteria — statistics as rhetoric done right. The graceful classic. Argument, principled."], ["Exploratory Data Analysis", ["John W. Tukey"], "Addison-Wesley", 1977, 6, "Tukey's EDA — box plots, stem-and-leaf, looking at data before modeling. The visual revolution. Data, explored."], ["The Visual Display of Quantitative Information", ["Edward R. Tufte"], "Graphics Press", 1983, 6, "Tufte's masterpiece — graphical excellence and integrity. The design classic. Information, displayed."], ["Probability Theory: The Logic of Science", ["Edwin T. Jaynes"], "Cambridge University Press", 2003, 0, "Jaynes's posthumous Bayesian magnum opus — probability as extended logic. The Bayesian testament. Logic, probable."], ["The Grammar of Science", ["Karl Pearson"], "Walter Scott, London", 1892, 7, "Pearson's positivist philosophy of science — the classic that shaped statistics' worldview. Science, grammaticized. The biometric school's creed."], ["Data Analysis Using Regression and Multilevel/Hierarchical Models", ["Andrew Gelman", "Jennifer Hill"], "Cambridge University Press", 2006, 1, "Gelman and Hill's applied regression — multilevel modeling for social science. The practitioner's guide. Levels, modeled."], ["Superforecasting", ["Philip E. Tetlock", "Dan Gardner"], "Crown", 2015, 7, "Tetlock's Good Judgment Project — what makes some forecasters superb. The science of prediction. Forecasts, super."]];
var L1_TITLES=["The Design of Experiments", "Statistical Methods for Research Workers", "The Lady Tasting Tea", "The Theory That Would Not Die", "How to Lie with Statistics", "The Signal and the Noise", "Naked Statistics", "The Art of Statistics", "The Book of Why", "Causality", "Thinking, Fast and Slow", "Fooled by Randomness", "The Black Swan", "The Drunkard's Walk", "Innumeracy", "A Mathematician Reads the Newspaper", "The Elements of Statistical Learning", "An Introduction to Statistical Learning", "Bayesian Data Analysis", "Statistical Rethinking", "Doing Bayesian Data Analysis", "Time Series Analysis: Forecasting and Control", "Categorical Data Analysis", "Generalized Linear Models", "The Cult of Statistical Significance", "Statistics as Principled Argument", "Exploratory Data Analysis", "The Visual Display of Quantitative Information", "Probability Theory: The Logic of Science", "The Grammar of Science", "Data Analysis Using Regression and Multilevel/Hierarchical Models", "Superforecasting"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["axioms of probability", "conditional probability", "random variables", "expectation", "limit theorems", "stochastic processes"], ["simple linear regression", "multiple regression", "diagnostics", "generalized linear models", "regularization", "model selection"], ["Bayes' theorem", "priors", "MCMC", "hierarchical models", "model checking", "decision theory"], ["randomization", "blocking", "factorial designs", "ANOVA", "power analysis", "quasi-experiments"], ["autocorrelation", "ARIMA models", "state-space models", "forecasting", "spectral analysis", "changepoints"], ["principal components", "factor analysis", "clustering", "discriminant analysis", "canonical correlation", "multidimensional scaling"], ["the grammar of graphics", "exploratory analysis", "dashboards", "misleading charts", "interactive visualization", "storytelling with data"], ["estimation", "hypothesis testing", "confidence intervals", "likelihood", "resampling", "the replication crisis"]];
var FRAMES=["taught a generation how to reason under uncertainty", "made the mathematics serve the science", "is still the clearest treatment of the subject", "settled how experiments should be run", "gave practitioners a code they could trust", "changed what counts as evidence"];
var T2_TOPICS=["causal machine learning", "federated inference", "differential privacy", "large-scale A/B testing", "conformal prediction", "synthetic data validation", "algorithmic fairness audits", "real-time nowcasting", "spatial statistics", "survival analysis at scale", "missing-data methods", "reproducibility standards"];
var T2_ANGLES=["method comparison", "theoretical guarantees", "applied case study", "software benchmarking", "pedagogical synthesis", "standards development"];
var T2_METHODS=["simulation studies", "benchmark datasets", "asymptotic analysis", "cross-validation", "sensitivity analysis", "replication audits"];
var T2_OUTCOMES=["a method with proven guarantees", "an open benchmark suite", "a validated workflow", "a reporting standard", "a diagnostic toolkit", "a decision rule with known error rates"];
var PROJ_BY="JAH Statistics Projection Unit";
function idOk(id){return new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$').test(id||'');}
function sigOk(s){return new RegExp('^\\.\\./'+STUDYSLUG+'/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{6}$').test(s||'');}
function sigLink(addr){var n=1+((addr*13)%5000);return '../'+STUDYSLUG+'/index.html?sig=JAH-'+BASE+'-STUDY-S-'+String(n).padStart(6,'0');}
function buildL1(addr,rnd,catOv){
  var w=pick(rnd,L1);
  var cat=(catOv!==undefined)?catOv:CATS[w[4]];
  var ed=pick(rnd,EDITIONS),ol=pick(rnd,OUTLINES[w[4]]),frame=pick(rnd,FRAMES);
  var id=PREFIX+pad7(addr),auth=w[1].join(', ');
  var fc='This is the full published record for \u201c'+w[0]+'\u201d by '+auth+' ('+fmtYear(w[3])+'), published in '+w[2]+'. '+w[5]
   +' This archival entry preserves the '+ed+' of the work. Its contents are organized around: '+ol+'.'
   +' Its lasting contribution: '+frame+'.'
   +' Archival note: record '+id+' is preserved in the JAH '+FIELD+' Published Archive Database as a Level 1 real published work. Data may be augmented by the archive but never reduced below the original published file.';
  return {id:id,title:w[0],authors:w[1].slice(),publication:w[2],year:w[3],category:cat,full_content:fc,
   source_ref:'Published work catalog: '+w[2]+', '+fmtYear(w[3])+'. Verifiable via WorldCat, the Library of Congress catalog, and publisher records.',
   signature_link:sigLink(addr),level:1};
}
function buildL2(addr,rnd,catOv){
  var topic=pick(rnd,T2_TOPICS),angle=pick(rnd,T2_ANGLES),method=pick(rnd,T2_METHODS),out=pick(rnd,T2_OUTCOMES);
  var cat=(catOv!==undefined)?catOv:pick(rnd,CATS);
  var yr=ri(rnd,2027,2045);
  var bAddr=((addr*7)%500)*10;if(bAddr<10)bAddr=10;
  var b1=buildL1(bAddr,prng(bAddr*31+7)),baseId=PREFIX+pad7(bAddr),id=PREFIX+pad7(addr);
  var title='Level 2 \u2014 Projected '+angle+' in '+topic+': '+method+' outlook to '+yr;
  var fc='Level 2 projection record for the JAH '+FIELD+' Published Archive Database. Projected research direction: '+angle+' in '+topic+'.'
   +' Projected methodology: '+method+', carried through to '+yr+'. Expected findings: '+out+'.'
   +' This projection extends the Level 1 published record \u201c'+b1.title+'\u201d ('+baseId+') into the '+yr+' horizon. It is a model-derived projection of where the field is heading, not a record of an already-published work.'
   +' Archival note: record '+id+' is a Level 2 projection. Projections regenerate deterministically from seed '+addr+' via generator '+GENVER+'.';
  return {id:id,title:title,authors:[PROJ_BY],publication:'JAH Published Archive \u2014 Projection Series',year:yr,category:cat,full_content:fc,
   source_ref:'JAH Archive projection model v1.0 \u2014 projected from Level 1 record '+baseId+'. Reproducible via generator '+GENVER+' seed '+addr+'.',
   signature_link:sigLink(addr),level:2};
}
function generate(seed,opts,rnd){
  seed=(seed>>>0)||1;opts=opts||{};rnd=rnd||prng(seed);
  var addr=((seed-1)%1000000)+1;
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:undefined;
  return (addr%10===0)?buildL1(addr,rnd,cat):buildL2(addr,rnd,cat);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!idOk(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<1||r.title.length>220)e.push('title');
  if(!Array.isArray(r.authors)||!r.authors.length)e.push('authors');
  else r.authors.forEach(function(a){if(typeof a!=='string'||!a.length)e.push('author');});
  if(typeof r.publication!=='string'||!r.publication.length||r.publication.length>160)e.push('publication');
  if(!Number.isInteger(r.year)||r.year<-1000||r.year>2045)e.push('year');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.full_content!=='string'||r.full_content.length<400||r.full_content.length>4000)e.push('full_content');
  if(typeof r.source_ref!=='string'||r.source_ref.length<20)e.push('source_ref');
  if(!sigOk(r.signature_link))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&r.title.indexOf('Level 2')!==0)e.push('l2prefix');
  if(r.level===1&&r.title.indexOf('Level 2')===0)e.push('l1prefix');
  var keys=Object.keys(r).sort().join('|');
  if(keys!=='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year')e.push('keys');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){
   if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
   if(s&&s.full_content===rec.full_content)e.push('duplicate content in archive sample');});
  return {ok:!e.length,errors:e};
}
var CHECKS=[
 {n:"id_format",f:function(r,x){try{return !!(idOk(r.id));}catch(e){return false;}}},
 {n:"id_matches_seed",f:function(r,x){try{return !!(r.id===PREFIX+pad7(x.seed));}catch(e){return false;}}},
 {n:"level_value",f:function(r,x){try{return !!(r.level===1||r.level===2);}catch(e){return false;}}},
 {n:"l2_title_starts_level2",f:function(r,x){try{return !!(r.level!==2||r.title.indexOf('Level 2')===0);}catch(e){return false;}}},
 {n:"l1_title_no_level2",f:function(r,x){try{return !!(r.level!==1||r.title.indexOf('Level 2')!==0);}catch(e){return false;}}},
 {n:"title_length",f:function(r,x){try{return !!(typeof r.title==='string'&&r.title.length>=1&&r.title.length<=220);}catch(e){return false;}}},
 {n:"authors_array",f:function(r,x){try{return !!(Array.isArray(r.authors)&&r.authors.length>=1);}catch(e){return false;}}},
 {n:"authors_strings",f:function(r,x){try{return !!(r.authors.every(function(a){return typeof a==='string'&&a.length>0;}));}catch(e){return false;}}},
 {n:"publication_length",f:function(r,x){try{return !!(typeof r.publication==='string'&&r.publication.length>=1&&r.publication.length<=160);}catch(e){return false;}}},
 {n:"year_integer_range",f:function(r,x){try{return !!(Number.isInteger(r.year)&&r.year>=-1000&&r.year<=2045);}catch(e){return false;}}},
 {n:"content_min_length",f:function(r,x){try{return !!(typeof r.full_content==='string'&&r.full_content.length>=400);}catch(e){return false;}}},
 {n:"content_max_length",f:function(r,x){try{return !!(r.full_content.length<=4000);}catch(e){return false;}}},
 {n:"content_sentences",f:function(r,x){try{return !!((r.full_content.match(/\.\s/g)||[]).length>=3);}catch(e){return false;}}},
 {n:"content_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.full_content));}catch(e){return false;}}},
 {n:"title_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.title));}catch(e){return false;}}},
 {n:"source_ref_length",f:function(r,x){try{return !!(typeof r.source_ref==='string'&&r.source_ref.length>=20);}catch(e){return false;}}},
 {n:"sig_link_format",f:function(r,x){try{return !!(sigOk(r.signature_link));}catch(e){return false;}}},
 {n:"sig_link_range",f:function(r,x){try{return !!((function(){var m=/S-(\d{6})$/.exec(r.signature_link);var n=m?+m[1]:0;return n>=1&&n<=5000;})());}catch(e){return false;}}},
 {n:"category_valid",f:function(r,x){try{return !!(CATS.indexOf(r.category)>=0);}catch(e){return false;}}},
 {n:"category_option_honored",f:function(r,x){try{return !!(generate(x.seed,{category:CATS[2]}).category===CATS[2]);}catch(e){return false;}}},
 {n:"deterministic",f:function(r,x){try{return !!(JSON.stringify(generate(x.seed,{}))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"l2_contains_projection",f:function(r,x){try{return !!(r.level!==2||/projection/i.test(r.full_content));}catch(e){return false;}}},
 {n:"l1_contains_level1_marker",f:function(r,x){try{return !!(r.level!==1||/Level 1/.test(r.full_content));}catch(e){return false;}}},
 {n:"no_data_base_two_words",f:function(r,x){try{return !!(!/database/i.test(r.title+' '+r.full_content));}catch(e){return false;}}},
 {n:"no_original_website_refs",f:function(r,x){try{return !!(!/(JAH Wiki|Signature Math|cyber-patent|spec catalog|mega-mall|AI Olympics|Signature Llama|Wikileaks)/i.test(JSON.stringify(r)));}catch(e){return false;}}},
 {n:"l1_title_in_corpus",f:function(r,x){try{return !!(r.level!==1||L1_TITLES.indexOf(r.title)>=0);}catch(e){return false;}}},
 {n:"word_length_sane",f:function(r,x){try{return !!((r.title+' '+r.full_content).split(/\s+/).every(function(w){return w.length<=60;}));}catch(e){return false;}}},
 {n:"exact_keys",f:function(r,x){try{return !!(Object.keys(r).sort().join('|')==='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year');}catch(e){return false;}}},
 {n:"json_roundtrip",f:function(r,x){try{return !!(JSON.stringify(JSON.parse(JSON.stringify(r)))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"content_substantive",f:function(r,x){try{return !!(r.full_content.length>r.title.length+200);}catch(e){return false;}}},
 {n:"validate_ok",f:function(r,x){try{return !!(validate(r).ok);}catch(e){return false;}}},
 {n:"drift_ok_empty",f:function(r,x){try{return !!(driftCheck(r,[]).ok);}catch(e){return false;}}},
 {n:"addr_space_top",f:function(r,x){try{return !!(generate(1000000,{}).id===PREFIX+'1000000');}catch(e){return false;}}},
 {n:"seed_one_id",f:function(r,x){try{return !!(generate(1,{}).id===PREFIX+'0000001');}catch(e){return false;}}},
 {n:"l2_year_future",f:function(r,x){try{return !!(r.level!==2||(r.year>=2027&&r.year<=2045));}catch(e){return false;}}},
 {n:"l1_year_past",f:function(r,x){try{return !!(r.level!==1||(r.year>=-1000&&r.year<=2026));}catch(e){return false;}}},
 {n:"l2_source_ref_model",f:function(r,x){try{return !!(r.level!==2||/projection model/.test(r.source_ref));}catch(e){return false;}}},
 {n:"l1_source_ref_catalog",f:function(r,x){try{return !!(r.level!==1||/WorldCat/.test(r.source_ref));}catch(e){return false;}}},
 {n:"content_mentions_id",f:function(r,x){try{return !!(r.full_content.indexOf(r.id)>=0);}catch(e){return false;}}},
 {n:"l2_publication_series",f:function(r,x){try{return !!(r.level!==2||/Projection Series/.test(r.publication));}catch(e){return false;}}},
];
function selfTest(){
  var fails=[],total=0,passed=0,ids={},levels={1:0,2:0};
  for(var seed=1;seed<=40;seed++){
    var r=generate(seed,{});
    levels[r.level]++;
    if(ids[r.id])fails.push('suite duplicate id '+r.id);ids[r.id]=1;
    for(var i=0;i<CHECKS.length;i++){total++;
      var ok=false;try{ok=CHECKS[i].f(r,{seed:seed});}catch(e){ok=false;}
      if(ok)passed++;else fails.push('seed '+seed+' ['+CHECKS[i].n+']');}
  }
  if(levels[1]===0)fails.push('suite: no level-1 records in 40 seeds');
  if(levels[2]===0)fails.push('suite: no level-2 records in 40 seeds');
  return {seeds:40,checksPerSeed:CHECKS.length,total:total,passed:passed,
    failed:total-passed+((levels[1]===0||levels[2]===0)?1:0),
    suite:{uniqueIds:Object.keys(ids).length===40,levels:levels},
    failures:fails.slice(0,25),ok:fails.length===0};
}
var api={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,api);
if(typeof module!=='undefined'&&module.exports)module.exports=api;
})();
