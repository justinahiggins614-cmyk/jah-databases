/* ✳ SIGNATURE — JAH JAH Interpretability generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='interpretability', PREFIX='JAH-INTERP-', VERSION='jahdb-interpretability-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["probing", "attribution", "mechanistic", "visualization", "evaluation", "concepts"];
var ANGLES=["method deep dive", "worked example", "finding spotlight", "limitation review", "tooling notes", "research front"];
var TOPICS=[{"t": "Linear probes", "c": "probing", "d": "Linear probes — interpretability technique entry.", "f": {"technique": "Linear probes", "overview": "Tiny classifiers trained on a model’s internal activations to test whether a concept is linearly decodable at some layer.", "how_it_works": ["Freeze the model and collect activations for labeled examples.", "Train a linear classifier per layer on those activations.", "High probe accuracy suggests the concept is represented there."], "example_application": "Testing whether a sentiment classifier’s middle layers encode negation.", "key_finding": "Many linguistic properties are linearly decodable well before the output layer.", "limitations": ["Correlation, not causation: decodability does not prove the model uses the concept.", "Probes can memorize, overstating what is represented."]}, "s": "online", "r": "Alain & Bengio, Understanding Intermediate Layers Using Linear Classifier Probes, 2016"}, {"t": "Contrastive activation addition", "c": "probing", "d": "Contrastive activation addition — interpretability technique entry.", "f": {"technique": "Contrastive activation addition", "overview": "Steering vectors built by contrasting activations on paired prompts (e.g., honest vs. dishonest) and adding the difference at inference.", "how_it_works": ["Collect activations for contrastive prompt pairs.", "Average the activation differences into a steering vector.", "Add the vector during generation to shift behavior."], "example_application": "Steering a chatbot toward more honest completions without retraining.", "key_finding": "Small activation shifts can reliably change high-level behavior.", "limitations": ["Effects may not generalize across contexts.", "Can degrade fluency if the vector is too strong."]}, "s": "signature", "r": null}, {"t": "Integrated gradients", "c": "attribution", "d": "Integrated gradients — interpretability technique entry.", "f": {"technique": "Integrated gradients", "overview": "An attribution method that assigns each input feature a share of the output by integrating gradients along a path from a baseline.", "how_it_works": ["Choose a neutral baseline input.", "Interpolate from baseline to the real input in small steps.", "Accumulate gradients; the sum attributes the prediction."], "example_application": "Finding which words drive a toxicity classifier’s decision.", "key_finding": "Satisfies completeness: attributions sum to the output difference from baseline.", "limitations": ["Results depend on the baseline choice.", "Expensive: needs many gradient evaluations."]}, "s": "online", "r": "Sundararajan et al., Axiomatic Attribution for Deep Networks, 2017"}, {"t": "SHAP values", "c": "attribution", "d": "SHAP values — interpretability technique entry.", "f": {"technique": "SHAP values", "overview": "Shapley-value-based feature attributions that fairly distribute a prediction among input features.", "how_it_works": ["Define a background distribution for missing features.", "Estimate each feature’s marginal contribution over coalitions.", "Report the averaged Shapley values as attributions."], "example_application": "Explaining which customer attributes drive a churn prediction.", "key_finding": "Grounded in cooperative game theory with uniqueness guarantees.", "limitations": ["Exact computation is exponential; approximations add noise.", "Correlated features split credit in ways users misread."]}, "s": "online", "r": "Lundberg & Lee, A Unified Approach to Interpreting Model Predictions, 2017"}, {"t": "LIME", "c": "attribution", "d": "LIME — interpretability technique entry.", "f": {"technique": "LIME", "overview": "Local surrogate explanations: fit a simple interpretable model around one prediction to explain it.", "how_it_works": ["Perturb the input to sample nearby variants.", "Weight samples by closeness to the original.", "Fit a sparse linear model; its weights are the explanation."], "example_application": "Explaining a single image classification to a non-expert.", "key_finding": "Model-agnostic: works for any classifier without opening it.", "limitations": ["Explanations can be unstable across runs.", "Local fidelity does not imply global understanding."]}, "s": "online", "r": "Ribeiro et al., \"Why Should I Trust You?\", 2016"}, {"t": "Activation patching", "c": "mechanistic", "d": "Activation patching — interpretability technique entry.", "f": {"technique": "Activation patching", "overview": "A causal method: replace activations from one run with those from another to find which components cause a behavior.", "how_it_works": ["Run the model on a clean and a corrupted input.", "Patch clean activations into the corrupted run, component by component.", "Components that restore behavior are causally implicated."], "example_application": "Locating where a model stores a factual association.", "key_finding": "Moves beyond correlation to causal claims about components.", "limitations": ["Combinatorial: patching every component is costly.", "Results can depend on the corruption scheme."]}, "s": "signature", "r": null}, {"t": "Sparse autoencoders", "c": "mechanistic", "d": "Sparse autoencoders — interpretability technique entry.", "f": {"technique": "Sparse autoencoders", "overview": "Dictionaries learned over activations that decompose dense, polysemantic activity into sparse, interpretable features.", "how_it_works": ["Train a sparse autoencoder on layer activations.", "Inspect the learned features for interpretable meanings.", "Ablate or amplify features to test causal roles."], "example_application": "Decomposing a language model’s residual stream into thousands of labeled features.", "key_finding": "Features often map to surprisingly crisp human concepts.", "limitations": ["Reconstruction is lossy; some behavior stays unexplained.", "Feature labels still need human verification."]}, "s": "signature", "r": null}, {"t": "Causal tracing", "c": "mechanistic", "d": "Causal tracing — interpretability technique entry.", "f": {"technique": "Causal tracing", "overview": "Corrupt an input, then restore activations layer by layer to trace where a factual recall is mediated.", "how_it_works": ["Corrupt key tokens in the input.", "Restore clean activations at each layer in turn.", "Layers whose restoration recovers the answer mediate the fact."], "example_application": "Tracing where \"The Eiffel Tower is in…\" is completed inside a transformer.", "key_finding": "Pinpoints mid-layer MLP modules as carriers of factual associations.", "limitations": ["Findings are fact- and model-specific.", "Does not explain how the fact got there during training."]}, "s": "signature", "r": null}, {"t": "Attention visualization", "c": "visualization", "d": "Attention visualization — interpretability technique entry.", "f": {"technique": "Attention visualization", "overview": "Heatmaps over attention weights showing which tokens each head attends to.", "how_it_works": ["Extract attention weights for a forward pass.", "Render token-by-token heatmaps per head.", "Compare patterns across layers and inputs."], "example_application": "Checking whether a translation model aligns source and target words.", "key_finding": "Reveals alignment-like and syntactic patterns in many heads.", "limitations": ["Attention is not explanation: weights do not equal importance.", "Many heads show diffuse, hard-to-read patterns."]}, "s": "signature", "r": null}, {"t": "Feature visualization", "c": "visualization", "d": "Feature visualization — interpretability technique entry.", "f": {"technique": "Feature visualization", "overview": "Optimizing an input image to maximally activate a neuron, revealing what the neuron \"looks for\".", "how_it_works": ["Start from noise and gradient-ascent the neuron’s activation.", "Apply regularization for human-readable images.", "Inspect the resulting visualizations per neuron."], "example_application": "Seeing edge, texture, and object-part detectors in vision models.", "key_finding": "Makes individual neurons’ preferences concrete and inspectable.", "limitations": ["Optimized images can be misleading artifacts.", "Scales poorly to very large models."]}, "s": "signature", "r": null}, {"t": "Faithfulness testing", "c": "evaluation", "d": "Faithfulness testing — interpretability technique entry.", "f": {"technique": "Faithfulness testing", "overview": "Checks whether an explanation actually reflects the model’s reasoning, e.g. via perturbation tests.", "how_it_works": ["Take an explanation’s claimed important features.", "Perturb those features and measure output change.", "Faithful explanations predict the change."], "example_application": "Testing whether saliency maps track real model sensitivity.", "key_finding": "Separates plausible-sounding from truly faithful explanations.", "limitations": ["No single agreed metric for faithfulness.", "Perturbations can push inputs off-distribution."]}, "s": "signature", "r": null}, {"t": "TCAV", "c": "concepts", "d": "TCAV — interpretability technique entry.", "f": {"technique": "TCAV", "overview": "Testing with Concept Activation Vectors: measures how sensitive a model’s prediction is to a human-defined concept.", "how_it_works": ["Collect examples embodying a concept (e.g., \"striped\").", "Learn the concept direction in activation space.", "Measure directional sensitivity of predictions to that concept."], "example_application": "Quantifying how much \"striped\" matters to a zebra classifier.", "key_finding": "Brings human concepts into quantitative model analysis.", "limitations": ["Needs curated concept example sets.", "Linear concept directions may miss nonlinear encodings."]}, "s": "online", "r": "Kim et al., Interpretability Beyond Feature Attribution (TCAV), 2018"}];
function pickR(rnd,a){return a[(rnd()*a.length)|0];}
function makeId(seed){var n=(typeof seed==='number'?seed:hashStr(String(seed)));return PREFIX+String((n%1000000)+1).padStart(7,'0');}
function compose(seed,rnd,T,cat){
  var A=pickR(rnd,ANGLES);
  var rec={focus:A};
  for(var k in T.f){rec[k]=T.f[k];}
  return rec;
}
function generate(seed,opts,rnd){
  var r=rnd||mulberry(typeof seed==='number'?seed:hashStr(String(seed)));
  var cat=opts&&opts.category,pool=TOPICS;
  if(cat){var f=TOPICS.filter(function(t){return t.c===cat;});if(f.length)pool=f;}
  var T=pickR(r,pool);
  var rec=compose(seed,r,T,cat);
  if(!rec.id)rec.id=makeId(seed);
  if(!rec.title)rec.title=T.t;
  if(!rec.description)rec.description=T.d;
  if(!rec.category)rec.category=T.c;
  if(!rec.source)rec.source=T.s||'signature';
  if(T.r&&!rec.source_ref)rec.source_ref=T.r;
  rec.signature_mark=MARK;
  return rec;
}
function validate(rec){
  var errs=[],req=["id", "title", "description", "category", "technique", "overview", "how_it_works", "limitations", "source"];
  if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
  req.forEach(function(k){if(rec[k]===undefined||rec[k]===null||rec[k]==='')errs.push('missing '+k);});
  if(rec.id&&!/^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(rec.id))errs.push('bad id format');
  if(rec.source&&['online','signature','fact-checked'].indexOf(rec.source)<0)errs.push('bad source');
  return{ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var key;try{key=JSON.stringify(rec);}catch(e){return{ok:false,errors:['unstringifiable']};}
  sample=sample||[];
  for(var i=0;i<sample.length;i++){try{if(JSON.stringify(sample[i])===key)return{ok:false,errors:['exact duplicate of archive record']};}catch(e){}}
  return{ok:true,errors:[]};
}
var GEN={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator(SLUG,GEN);}catch(e){}}
if(typeof module!=='undefined'){module.exports=GEN;}
function runTests(){
  var pass=0,fail=0;
  function t(name,fn){try{if(fn()){pass++;}else{fail++;console.log('FAIL: '+name);}}catch(e){fail++;console.log('FAIL: '+name+' threw '+e.message);}}
  var i;
  for(i=1;i<=10;i++){(function(s){t('gen+validate seed '+s,function(){return validate(generate(s,{},null)).ok;});})(i);}
  for(i=11;i<=20;i++){(function(s){t('determinism seed '+s,function(){return JSON.stringify(generate(s,{},null))===JSON.stringify(generate(s,{},null));});})(i);}
  for(i=0;i<CATS.length;i++){(function(c){t('category filter '+c,function(){var r=generate(7,{category:c},null);return r.category===c&&validate(r).ok;});})(CATS[i]);}
  t('id format',function(){return /^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(generate(42,{},null).id);});
  t('title non-empty',function(){return String(generate(5,{},null).title).length>3;});
  t('description non-empty',function(){return String(generate(5,{},null).description).length>10;});
  t('source valid',function(){return['online','signature','fact-checked'].indexOf(generate(5,{},null).source)>=0;});
  t('signature mark',function(){return String(generate(5,{},null).signature_mark).indexOf('Signature')>=0;});
  t('reject empty',function(){return !validate({}).ok;});
  t('reject missing title',function(){var r=generate(3,{},null);delete r.title;return !validate(r).ok;});
  t('reject bad id',function(){var r=generate(3,{},null);r.id='nope';return !validate(r).ok;});
  t('driftCheck novel ok',function(){return driftCheck(generate(999,{},null),[]).ok;});
  t('driftCheck dupe caught',function(){var r=generate(999,{},null);return !driftCheck(r,[JSON.parse(JSON.stringify(r))]).ok;});
  t('distinct seeds distinct ids',function(){return generate(1001,{},null).id!==generate(1002,{},null).id;});
  t('json round-trip',function(){var r=generate(77,{},null);return JSON.parse(JSON.stringify(r)).id===r.id;});
  t('extra domain check',function(){var r=generate(9,{},null);return (r.how_it_works.length>=2);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
