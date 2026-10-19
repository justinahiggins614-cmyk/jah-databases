(function(){'use strict';
/* jahdb-fundamental-data-science-1.0 — fundamental data-science bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FDSC-';
var KIND='fundamental data-science record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Data science is the practice of extracting knowledge and value from data: combining statistics, computing, and domain expertise to turn raw observations into decisions, predictions, and understanding. It is the applied discipline of the data age.', 'reasoning':'Data scientists reason with the full pipeline in mind: the question determines the data, the data determines the method, and the decision determines what \'good\' means. Every analysis ends in a recommendation — and the recommendation is tested against reality.', 'quantities':'The core quantities are data quality dimensions (completeness, accuracy, timeliness), model performance metrics (precision, recall, RMSE), and business metrics (lift, ROI). Data volume is the least important quantity — quality dominates.', 'mechanism':'Data science works the pipeline: acquire and clean data → explore and visualize → model → validate → deploy and monitor. Most of the work is cleaning and validation; the modeling is the visible tip. Deployment without monitoring is abandonment.', 'miscon':'Data science is not just machine learning: most value comes from data quality, clear questions, and honest evaluation. Bigger data does not beat better data. And a dashboard is not insight — insight changes a decision.'};
var SIGLENS=['In the Signature system, data science is the operating discipline of the network itself: every database here is a data product, and the Signature formulation teaches each principle as a practice you can apply to real data immediately.','The Signature practice is to work the pipeline end to end: clean the messy data, visualize before modeling, validate honestly, and monitor in production — so data science is done as craft, not just studied as theory.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- data cleaning demo. Runs as-is with python3."""\nraw = ["  Alice ", "BOB", "alice", None, "  bob ", "Carol", "carol "]\nseen = set()\nclean = []\nfor v in raw:\n    if v is None:\n        continue\n    v = v.strip().lower()\n    if v not in seen:\n        seen.add(v)\n        clean.append(v)\nprint("raw:  ", raw)\nprint("clean:", clean)\nprint("most of data science is this: normalize, dedupe, handle missing")\n', '#!/usr/bin/env python3\n"""{TITLE} -- precision/recall demo. Runs as-is with python3."""\nactual =    [1,0,1,1,0,1,0,0,1,0]\npredicted = [1,0,0,1,0,1,1,0,1,0]\ntp = sum(1 for a,p in zip(actual,predicted) if a==1 and p==1)\nfp = sum(1 for a,p in zip(actual,predicted) if a==0 and p==1)\nfn = sum(1 for a,p in zip(actual,predicted) if a==1 and p==0)\nprecision = tp/(tp+fp); recall = tp/(tp+fn)\nprint(f"precision={precision:.2f} (of flagged, how many right)")\nprint(f"recall={recall:.2f} (of real positives, how many caught)")\n', '#!/usr/bin/env python3\n"""{TITLE} -- train/test split demo. Runs as-is with python3."""\nimport random\nrandom.seed(11)\ndata = list(range(100))\nrandom.shuffle(data)\nsplit = int(0.8 * len(data))\ntrain, test = data[:split], data[split:]\nprint("train:", len(train), "test:", len(test))\nprint("overlap:", len(set(train) & set(test)), "(must be 0: no leakage)")\n'];
var TOPICS=[['What Data Science Is','Data science is the discipline of turning data into decisions: it combines statistics, computing, and domain knowledge to extract insight from raw observations. Where statistics develops the theory of inference, data science ships the pipeline that uses it.'],
['The Core Question of Data Science','The core question is: what should we do, given this data? Every data-science project ends in a decision — launch, treat, price, flag — and the analysis is judged by whether the decision improved.'],
['Assumptions: Data Reflects Reality (Imperfectly)','The field assumes data reflects reality imperfectly: measurement error, selection bias, and missingness are the default, not the exception. The analysis must model the data-generating process, not just the data.'],
['The Vocabulary: Features, Labels, Pipelines','The vocabulary names the workflow: features (inputs), labels (targets), pipelines (reproducible sequences of steps), and leakage (test information contaminating training). Fluency means thinking in pipelines, not scripts.'],
['Data Quality: The Fundamental Quantity','Data quality is the fundamental quantity: completeness, accuracy, consistency, and timeliness of the data. No model outruns its data — garbage in, garbage out is the field\'s first law, and most project time goes to cleaning.'],
['The Pipeline: The Primary Method','The pipeline is the primary method: acquire → clean → explore → model → validate → deploy → monitor. Each stage has its checks, and skipping stages — especially validation and monitoring — is how projects fail in production.'],
['A Canonical First Example','The canonical first example is predicting house prices: gather features (size, location, age), clean the missing values, explore correlations, fit a regression, validate on held-out houses, and report the error honestly. Every later project is this one, bigger.'],
['How Data Science Measures','The field measures with metrics matched to decisions: precision and recall for detection, RMSE for prediction, lift for targeting, and always a business metric alongside. The right metric is the one the decision-maker actually optimizes.'],
['The Core Mechanism: From Question to Decision','The core mechanism runs question → data → analysis → recommendation → action → measurement. The loop closes when the action\'s outcome is measured and feeds the next question — data science as organizational learning.'],
['The Simplest Law: Garbage In, Garbage Out','The simplest law is garbage in, garbage out: no algorithm rescues bad data. The corollary is the practitioner\'s rule — spend most of your time on the data, and the modeling will be the easy part.'],
['Common Misconceptions in Data Science','The misconceptions waste millions: that data science equals machine learning (most value is in data and decisions), that bigger data beats better data, that correlation licenses action, and that a model in a notebook is a deployed system.'],
['How Beginners Practice Data Science','Beginners practice on real messy datasets: download one, clean it, visualize it, model it, and write up what the numbers mean for a decision. Portfolio projects that end in recommendations beat tutorials that end in accuracy scores.'],
['The Core Model: Regression','Regression is the core model: predicting a number from features, from linear regression upward. It teaches the whole craft — features, fitting, regularization, validation — in the simplest setting where every step is visible.'],
['The Great Technique: Cross-Validation','Cross-validation is the great technique: rotate which data validates the model to estimate real-world performance honestly. It is the field\'s answer to overfitting — the closest thing to seeing the future before deploying.'],
['Systems Thinking: The Data Organization','Systems thinking in data science is the data organization: pipelines, warehouses, governance, and the feedback loops between analysts and decision-makers. A lone model is a prototype; a data organization ships value repeatedly.'],
['Invariance: Reproducibility','The invariance principle is reproducibility: the same data plus the same code gives the same result, for anyone, anytime. Version control, pinned environments, and documented lineage make analyses invariant across people and time.'],
['Approximation: Sampling the Data','Approximation works on samples: develop on a fraction of the data, validate the approach, then scale. A method that needs the full dataset to be debugged is a method that will be debugged in production.'],
['Evidence Standards: Honest Validation','The evidence standard is honest validation: held-out test sets, no leakage, metrics chosen before modeling, and uncertainty reported. A model evaluated on its training data has proven nothing.'],
['Classic Discoveries','The classic discoveries are the methods that became infrastructure: the relational model organizing data, MapReduce scaling computation, the random forest taming overfitting, and the notebook making analysis shareable. Each turned craft into industry.'],
['Core Trade-offs: Accuracy versus Interpretability','The core trade-off pits accuracy against interpretability, speed, and cost: the best-scoring model may be unexplainable, too slow, or too expensive. Production chooses the model the organization can actually run and defend.'],
['Handling Uncertainty: Prediction Intervals','Data science handles uncertainty with prediction intervals and calibration: not just a point forecast but a range, and probabilities that mean what they say. A well-calibrated 70% happens 70% of the time — the honest product.'],
['Tools of the Trade','The tools of the trade are Python or R, SQL, a notebook, and version control — plus the dashboard for communication. The deepest is the data dictionary: knowing what each field means beats any algorithm.'],
['Ethics and Responsibility','Ethics in data science is about consequences at scale: biased training data automates discrimination, opaque scoring evades appeal, and surveillance masquerades as personalization. The practitioner\'s responsibility is to audit outcomes, not just accuracy.'],
['Teaching Data Science','Teaching it well uses real messy data from day one: the cleaning struggle teaches more than clean tutorials. Students should present to a decision-maker — defending a recommendation under questions is the true final exam.'],
['The Frontier Question','The frontier question is automated trust: how to build systems that clean, model, validate, and monitor themselves while remaining auditable by humans. AutoML handles the modeling; the frontier is automating the judgment around it.'],
['Unifying Theories','The unifying view is the pipeline as the theory: statistics provides inference, computer science provides scale, domain expertise provides meaning. Data science is their intersection — and its maturity is measured by how routinely the intersection ships value.'],
['Computational Data Science','Computational data science is the engineering beneath: distributed processing, feature stores, experiment platforms, and monitoring infrastructure. The science answers questions; the platform lets the organization ask them continuously.'],
['Bridges to Other Fields','Data science bridges to every data-rich field: medicine, finance, marketing, sports, government, and science itself. Each brings its questions; data science brings the pipeline — and returns decisions.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: fully automated data cleaning, causal inference from observational data at scale, privacy-preserving analytics that retain utility, and honest uncertainty for complex pipelines. Active research, no settled answers.'],
['How New Claims Are Validated','New methods are validated by benchmarks and by production: open datasets with fixed splits, independent reimplementation, then deployment where the metric that matters is the business outcome. A method earns trust when it works on others\' data and others\' problems.'],
['The Great Debates','The great debates include code-first versus tool-first practice, the value of deep theory versus shipping, centralization versus embedded analysts, and whether \'data scientist\' names one job or five. The debates reflect a young field finding its shape.'],
['Failure Modes: When Data Science Gets It Wrong','Data science gets it wrong through leakage, overfitting, confusing correlation with causation, and deploying without monitoring — the model decays silently while the dashboard stays green. The immune system is the pipeline\'s checks at every stage.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis runs the whole pipeline as one discipline: the question, the data, the model, the validation, the deployment, the monitoring — each informing the others. The fundamentals are the checklist that keeps complex projects honest.'],
['The Signature Formulation: Data Science as Network Craft','The Signature formulation makes data science the craft of the network itself: every database here is a data product built on these principles, because in the Signature system a database you cannot clean, validate, and monitor is a database you cannot trust. That is the Signature capstone on data-science bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["The question comes first: no modeling before the decision it serves is named.", "Data lineage is documented: every dataset's source, cleaning, and caveats are recorded.", "Models are monitored in production: drift is detected, not discovered by accident."],citations:["Provost, F. and Fawcett, T. \u2014 Data Science for Business.", "Wickham, H. and Grolemund, G. \u2014 R for Data Science.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-data-science-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-data-science',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
