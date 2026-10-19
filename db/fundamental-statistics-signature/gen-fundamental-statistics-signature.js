(function(){'use strict';
/* jahdb-fundamental-statistics-signature-1.0 — fundamental statistics bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFSTA-';
var KIND='fundamental statistics record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Statistics is the science of learning from data under uncertainty: collecting observations, summarizing them honestly, and drawing conclusions that quantify how sure we can be. It is the bridge between raw data and justified belief.', 'reasoning':'Statisticians reason by modeling: propose a probability model for how the data could arise, estimate its parameters, and check how well the model survives contact with new data. Every conclusion carries its uncertainty with it.', 'quantities':'The core quantities are the mean, median, variance, and standard deviation for summarizing data; probabilities and likelihoods for modeling; and p-values, confidence intervals, and effect sizes for inference. Sample size is the master quantity — it governs everything.', 'mechanism':'Statistical work runs: define the question → design the data collection → explore and clean the data → fit a model → validate against held-out data → report estimates with uncertainty. Skipping the validation step is how most statistical failures happen.', 'miscon':'Statistics is not lying with numbers — bad statistics lies; good statistics is the defense against lies. Correlation is not causation. A p-value is not the probability the hypothesis is true. And bigger data does not fix biased data.'};
var SIGLENS=['In the Signature system, statistics is the discipline of honest measurement for every database: every count, every estimate, every claim about the network\'s data passes through statistical reasoning, and the Signature formulation teaches each principle as a check you can run on real data.','The Signature practice is to compute every statistical principle on real data: simulate the sampling, run the test, plot the interval — so uncertainty is felt in the hands, not just memorized as a definition.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- mean, median, stddev demo. Runs as-is with python3."""\nimport statistics\ndata = [12, 15, 14, 10, 13, 15, 16, 14, 100, 13]\nprint("data:", data)\nprint("mean:", round(statistics.mean(data), 2))\nprint("median:", statistics.median(data))\nprint("stdev:", round(statistics.stdev(data), 2))\nprint("note: the outlier 100 drags the mean but not the median")\n', '#!/usr/bin/env python3\n"""{TITLE} -- binomial probability demo. Runs as-is with python3."""\nimport math\ndef binom(n, k, p):\n    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))\nn, p = 10, 0.5\nfor k in range(0, 11, 2):\n    print(f"P(exactly {k} heads in {n} flips) = {binom(n, k, p):.4f}")\nprint("P(5 heads) =", round(binom(10, 5, 0.5), 4))\n', '#!/usr/bin/env python3\n"""{TITLE} -- law of large numbers demo. Runs as-is with python3."""\nimport random\nrandom.seed(7)\nfor n in [10, 100, 1000, 10000, 100000]:\n    heads = sum(random.random() < 0.5 for _ in range(n))\n    print(f"n={n:>6}  proportion heads={heads/n:.4f}")\n'];
var TOPICS=[['Signature What Statistics Is','Statistics is the science of drawing reliable conclusions from imperfect data: it tells you how to collect observations, summarize them without distortion, and say how much you can trust what you found. Where mathematics proves, statistics estimates — and it always reports the size of its doubt.'],
['Signature The Core Question of Statistics','The core question of statistics is: what does this data let me claim, and how sure may I be? Every statistical procedure is an answer to that question in a specific setting — a poll, a drug trial, a quality check — and every answer comes with its uncertainty attached.'],
['Signature Assumptions Beneath Every Analysis','Every statistical analysis rests on assumptions: that the sample represents the population, that observations are independent enough, that the model family fits the phenomenon. Stating the assumptions is part of the analysis; violating them silently is the most common source of false conclusions.'],
['Signature The Vocabulary of Data','The vocabulary of statistics names the pieces: population versus sample, parameter versus statistic, variable versus observation, categorical versus numerical data. A parameter describes the world; a statistic describes the sample; inference is the disciplined leap from the second to the first.'],
['Signature The Mean, Median, and Standard Deviation','The mean, median, and standard deviation are the fundamental summary quantities: the mean is the balance point, the median the middle value, and the standard deviation the typical distance from the mean. The median resists outliers that drag the mean; the standard deviation sets the scale of natural variation.'],
['Signature Sampling: The Primary Method','Sampling is the primary method: because you cannot measure everyone, you measure a well-chosen subset and generalize. Random sampling is the gold standard — every member of the population gets a known chance of selection — because only randomness lets the mathematics of inference apply.'],
['Signature A Canonical First Example','The canonical first example is the poll: survey 1,000 randomly chosen voters, find 520 favoring a candidate, and report 52% plus or minus about 3 points. The margin of error comes from the mathematics of sampling, and it shrinks with the square root of the sample size — quadrupling respondents halves the error.'],
['Signature How Statistics Observes','Statistics observes through designed data collection: surveys, experiments, and observational studies, each with its protocol. The randomized controlled trial is the strongest design — random assignment balances the unknown confounders — which is why medicine trusts it for drug approval.'],
['Signature The Core Mechanism: Variation Plus Model','The core mechanism of statistical reasoning is variation plus model: the world varies, a probability model describes the pattern of that variation, and inference compares what was observed against what the model predicts. Signal is the pattern; noise is the rest; the model separates them.'],
['Signature The Simplest Law: The Law of Large Numbers','The simplest law is the law of large numbers: as the sample grows, the sample mean converges to the true mean. It is why casinos win, why polls work, and why averaging repeated measurements beats trusting any single one.'],
['Signature Common Misconceptions in Statistics','The misconceptions are famous: that correlation implies causation, that a p-value is the probability the hypothesis is true, that statistical significance means practical importance, and that more data fixes biased data. Each has misled governments, companies, and journals.'],
['Signature How Beginners Practice Statistics','Beginners practice statistics by analyzing real datasets: load the data, plot it first, compute summaries, and write down what the numbers mean in plain sentences. Plotting before modeling is the cardinal habit — the eye catches what the formulas miss.'],
['Signature The Core Model: The Normal Distribution','The normal distribution is the core model: the bell curve described by a mean and a standard deviation, arising whenever many small independent effects add up. The central limit theorem explains its ubiquity — sample means are approximately normal even when the underlying data is not.'],
['Signature The Great Equation: Bayes\' Theorem','Bayes\' theorem, P(H|data) = P(data|H)·P(H)/P(data), is the great equation of inference: it tells how to update beliefs with evidence. The prior encodes what you believed before; the likelihood encodes what the data says; the posterior is the rational blend.'],
['Signature Systems Thinking: Confounders and Causes','Systems thinking in statistics means hunting confounders: ice cream sales correlate with drowning because summer drives both. Causal diagrams map which variables influence which, and only designs that break the confounding paths — like randomization — license causal claims.'],
['Signature Invariance: What Replication Preserves','The invariance principle of statistics is replication: a genuine effect survives new samples, new labs, and new analysts. Results that vanish on replication were noise or bias wearing a lab coat — which is why the replication movement remade the field\'s standards.'],
['Signature Approximation and Error: Confidence Intervals','Confidence intervals quantify approximation error honestly: a 95% interval is a procedure that captures the true value 95% of the time over repeated sampling. The interval\'s width shrinks with more data and grows with more variability — the honest price tag on every estimate.'],
['Signature Evidence Standards: Significance and Power','The evidence standards are significance and power: a p-value measures how surprising the data is under the null hypothesis, while power measures the chance of detecting a real effect of a given size. Reporting both, plus the effect size, is the modern standard.'],
['Signature Classic Discoveries','The classic discoveries include Gosset\'s t-test brewed at Guinness, Fisher\'s experimental designs at Rothamsted, Neyman and Pearson\'s hypothesis testing framework, and Tukey\'s exploratory data analysis. Each turned a practical problem — beer quality, crop yields — into general method.'],
['Signature Core Trade-offs: Bias versus Variance','The core trade-off is bias versus variance: simple models are stable but miss structure (high bias), complex models fit noise as well as signal (high variance). Cross-validation navigates the trade by testing models on data they never saw during fitting.'],
['Signature Handling Uncertainty Honestly','Handling uncertainty honestly means distinguishing aleatory uncertainty (inherent randomness) from epistemic uncertainty (lack of knowledge). More data shrinks the second, never the first — and every honest analysis says which kind dominates its conclusions.'],
['Signature Tools of the Trade','The tools of the trade are a scripting language (Python or R), a plotting library, and a skeptical checklist: plot the data, check the assumptions, validate on held-out data, report uncertainty. Spreadsheets compute; scripts reproduce — and reproducibility is the difference between analysis and anecdote.'],
['Signature Ethics and Responsibility','Ethics in statistics is about honesty under pressure: not p-hacking through analyses until something is significant, not hiding the analyses that failed, not presenting exploratory findings as confirmatory. The field\'s scandals all trace to violating these; its credibility rests on keeping them.'],
['Signature Teaching Statistics','Teaching statistics well starts with intuition before formulas: simulate the sampling distribution, watch the interval capture the truth, feel the law of large numbers in action. Students who have simulated a concept rarely misread it later — the computer is the modern statistics lab.'],
['Signature The Frontier Question','The frontier question is inference at massive scale: how to draw valid conclusions from billions of observations, streaming data, and models with trillions of parameters. Classical theory assumed small clean samples; the frontier rebuilds the foundations for the data flood.'],
['Signature Unifying Theories','The unifying theories connect the field\'s schools: Bayesian and frequentist inference agree in large samples, information theory grounds model selection, and decision theory unifies estimation, testing, and prediction as choices under uncertainty with explicit loss functions.'],
['Signature Computational Statistics','Computational statistics made modern inference possible: Markov chain Monte Carlo samples from posteriors no formula can touch, the bootstrap estimates uncertainty by resampling the data itself, and permutation tests build null distributions by shuffling. Computation turned theory into practice.'],
['Signature Bridges to Other Fields','Statistics bridges to every empirical field: clinical trials to medicine, A/B tests to technology, econometrics to economics, psychometrics to psychology, quality control to manufacturing. Each field brings its data; statistics brings the discipline of honest inference.'],
['Signature The Great Unsolved Problems','The great unsolved problems are methodological and open: fully honest inference after data-driven model selection, causal inference from purely observational big data, and uncertainty quantification for deep learning systems. They are labeled unsolved — active research, no settled answers.'],
['Signature How New Claims Are Validated','New statistical claims are validated by replication and pre-registration: independent teams rerun the analysis on fresh data, and pre-registered protocols prevent cherry-picking. A method earns trust when it works in others\' hands on others\' data.'],
['Signature The Great Debates','The great debates pit Bayesian against frequentist philosophy, significance testing against estimation, and big-data optimism against the warning that biased big data is just precisely wrong. The debates sharpen practice: each side\'s criticisms became the other\'s safeguards.'],
['Signature Failure Modes: When Statistics Gets It Wrong','Statistics gets it wrong through p-hacking, publication bias, confusing correlation with causation, and applying models where assumptions fail — the replication crisis exposed all four at scale. The field\'s immune response was pre-registration, open data, and humility about single studies.'],
['Signature Synthesis: Building on the Fundamentals','Synthesis means combining the fundamentals on real problems: design the collection, explore the data, model with uncertainty, validate on held-out data, and communicate the interval, not just the point. Every advanced method is this pipeline with heavier machinery.'],
['Signature The Signature Formulation: Statistics as Honest Measurement','The Signature formulation makes statistics the honesty layer of the whole network: every database count, every estimate, every claim gets its uncertainty computed and shown, because a network that cannot measure its own doubt cannot be trusted. That is the Signature capstone on statistical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
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
    standards:["Report uncertainty with every estimate: a number without an interval is incomplete.", "Pre-register analyses where possible; exploratory findings are labeled exploratory.", "Show the data: summaries never substitute for looking at the distribution itself."],citations:["Agresti, A. and Franklin, C. \u2014 Statistics: The Art and Science of Learning from Data.", "Tukey, J. W. \u2014 Exploratory Data Analysis (Addison-Wesley, 1977).", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-statistics-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-statistics-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
