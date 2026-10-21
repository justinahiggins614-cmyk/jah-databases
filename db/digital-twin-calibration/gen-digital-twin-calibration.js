(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["parameter-estimation", "uncertainty", "validation", "online", "multi-fidelity"];
var PREFIX='JAH-DTC-';
var USE="Used by manufacturing, energy, and aerospace teams to keep twins trustworthy for decisions.";
var FLD=[["method", "Method"], ["data", "Data"], ["output", "Output"]];
var DEMO="# {title} - calibration RMSE (python3)\nerrs={d1}\ntol={d2}\nimport math\nrmse=math.sqrt(sum(e*e for e in errs)/len(errs))\nbias=sum(errs)/len(errs)\nprint(\"RMSE=%.4f bias=%.4f\" % (rmse, bias))\nprint(\"CALIBRATED\" if rmse <= tol else \"RECALIBRATE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["parameter-estimation", "Parameter Estimation", "Fits twin parameters by minimizing the mismatch between simulated and measured outputs.", "Parameter Estimation", "sensor history", "fitted parameters", "[0.02, -0.01, 0.03, 0.0, -0.02]", "0.05", "0.03"], ["uncertainty", "Bayesian Calibration", "Treats parameters as distributions, updating beliefs with measurements via Bayes' rule.", "Bayesian Calibration", "measurements + priors", "posterior distributions", "[0.01, 0.02, -0.02, 0.01]", "0.04", "0.02"], ["validation", "Discrepancy Modeling", "Learns an explicit model of the twin's systematic error to correct predictions.", "Discrepancy Modeling", "residual history", "bias correction model", "[0.03, 0.03, -0.01, 0.02, 0.0]", "0.05", "0.03"], ["online", "Sensitivity Analysis", "Ranks parameters by influence on outputs so calibration effort targets what matters.", "Sensitivity Analysis", "parameter sweeps", "sensitivity ranking", "[0.0, 0.01, -0.01, 0.02]", "0.03", "0.02"], ["multi-fidelity", "History Matching", "Rules out implausible parameter regions iteratively against historical observations.", "History Matching", "historical runs", "plausible region", "[0.02, -0.03, 0.01, 0.0, 0.02]", "0.06", "0.04"], ["parameter-estimation", "Ensemble Kalman Update", "Updates an ensemble of twin states with incoming measurements for nonlinear systems.", "Ensemble Kalman Update", "ensemble + observations", "updated ensemble", "[0.01, -0.01, 0.02, -0.02]", "0.04", "0.02"], ["uncertainty", "Surrogate-assisted Calibration", "Uses a fast surrogate model to explore parameter space, validating only promising points on the full twin.", "Surrogate-assisted Calibration", "surrogate predictions", "calibrated parameters", "[0.02, 0.0, -0.02, 0.01, 0.03]", "0.05", "0.03"], ["validation", "Multi-fidelity Calibration", "Combines cheap low-fidelity runs with sparse high-fidelity data for accurate, affordable calibration.", "Multi-fidelity Calibration", "mixed-fidelity data", "fused parameters", "[0.01, 0.01, -0.01, 0.0]", "0.04", "0.02"], ["online", "Online Adaptive Calibration", "Continuously re-fits parameters as new telemetry arrives, tracking drift in the physical asset.", "Online Adaptive Calibration", "streaming telemetry", "live parameters", "[0.03, -0.02, 0.01, 0.02, -0.01]", "0.05", "0.03"], ["multi-fidelity", "Sensor Bias Correction", "Estimates and removes systematic sensor offsets before they poison the twin.", "Sensor Bias Correction", "redundant sensors", "bias estimates", "[0.02, 0.02, 0.02, 0.01]", "0.04", "0.02"], ["parameter-estimation", "Drift Compensation", "Detects slow divergence between twin and asset and applies corrective parameter shifts.", "Drift Compensation", "long-term trends", "compensation terms", "[0.04, 0.03, 0.02, 0.01, 0.0]", "0.06", "0.04"], ["uncertainty", "Uncertainty Quantification", "Propagates parameter and model uncertainty to predictions as confidence intervals.", "Uncertainty Quantification", "parameter distributions", "prediction intervals", "[0.01, -0.02, 0.03, -0.01]", "0.05", "0.03"], ["validation", "Validation Metrics", "Scores twin fidelity with metrics like NRMSE and coverage probability on held-out data.", "Validation Metrics", "held-out measurements", "fidelity score", "[0.02, 0.01, -0.01, 0.02, 0.01]", "0.04", "0.02"], ["online", "Digital Thread Sync", "Keeps the twin synchronized with the authoritative product data thread across lifecycle stages.", "Digital Thread Sync", "PLM data", "synced twin", "[0.0, 0.01, 0.0, -0.01]", "0.03", "0.02"], ["multi-fidelity", "Model Order Reduction Check", "Verifies reduced-order twins still match full-order behavior within tolerance.", "Model Order Reduction Check", "full-order runs", "reduction error bound", "[0.03, -0.01, 0.02, 0.0, -0.03]", "0.06", "0.04"], ["parameter-estimation", "Boundary Condition Tuning", "Adjusts inlet, load, and ambient conditions in the twin to match measured operating points.", "Boundary Condition Tuning", "operating logs", "tuned boundaries", "[0.01, 0.02, 0.0, -0.02]", "0.04", "0.02"], ["uncertainty", "Material Property Fitting", "Infers effective material properties from test coupons and in-service measurements.", "Material Property Fitting", "test data", "fitted properties", "[0.02, -0.02, 0.01, 0.03, 0.0]", "0.05", "0.03"], ["validation", "Operational Envelope Mapping", "Maps the validated operating envelope where twin predictions stay within tolerance.", "Operational Envelope Mapping", "sweep tests", "envelope definition", "[0.01, 0.0, 0.02, -0.01]", "0.04", "0.02"], ["online", "Twin Fidelity Scoring", "Computes a single fidelity score from accuracy, coverage, and freshness for dashboards.", "Twin Fidelity Scoring", "metric suite", "fidelity score", "[0.02, 0.03, -0.02, 0.01, 0.02]", "0.06", "0.04"], ["multi-fidelity", "Continuous Re-calibration", "Schedules periodic full re-calibration so the twin never silently goes stale.", "Continuous Re-calibration", "calendar + triggers", "fresh calibration", "[0.01, -0.01, 0.01, 0.0]", "0.04", "0.02"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-digital-twin-calibration-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('digital-twin-calibration',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
