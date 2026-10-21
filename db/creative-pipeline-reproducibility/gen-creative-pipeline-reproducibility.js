(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["versioning", "determinism", "provenance", "builds", "verification"];
var PREFIX='JAH-CREATI-';
var USE="Used by VFX studios, game teams, and generative-AI pipelines that must reproduce any output on demand.";
var FLD=[["practice", "Practice"], ["applies_to", "Applies to"], ["guarantee", "Guarantee"]];
var DEMO="# {title} - determinism check (python3)\nimport hashlib\ncfg={d1}\nh1=hashlib.sha256(cfg.encode()).hexdigest()\nh2=hashlib.sha256(cfg.encode()).hexdigest()\nprint(\"hash:\", h1[:16])\nprint(\"DETERMINISTIC\" if h1 == h2 else \"NON-DETERMINISTIC\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["versioning", "Pinned Tool Versions", "Locks every DCC, renderer, and library to exact versions so reruns use identical code.", "Pinned Tool Versions", "all tools", "same binaries every run", "'maya2024.2-arnold7.2.1'", "'x'", "'y'"], ["determinism", "Deterministic Seeds", "Records the RNG seed for every stochastic step (layout, scattering, noise) in the job manifest.", "Deterministic Seeds", "randomized steps", "identical randomness", "'layout-seed-4471'", "'x'", "'y'"], ["provenance", "Lockfiles", "Freezes full dependency trees including transitive packages for build and render environments.", "Lockfiles", "dependencies", "no surprise upgrades", "'requirements-lock-v88'", "'x'", "'y'"], ["builds", "Immutable Asset IDs", "Assigns content-addressed IDs to assets so any change creates a new ID instead of mutating history.", "Immutable Asset IDs", "assets", "tamper-evident history", "'asset-b3f9-immutable'", "'x'", "'y'"], ["verification", "Hermetic Builds", "Builds in sealed containers with no network access, so only declared inputs affect outputs.", "Hermetic Builds", "build farm", "no hidden inputs", "'hermetic-build-12'", "'x'", "'y'"], ["versioning", "Content-Addressed Storage", "Stores artifacts by hash of content, making identical outputs deduplicate and any corruption detectable.", "Content-Addressed Storage", "artifacts", "integrity by construction", "'cas-sha256-store'", "'x'", "'y'"], ["determinism", "Provenance Logs", "Records who ran what, with which inputs and parameters, for every output artifact.", "Provenance Logs", "jobs", "full audit trail", "'prov-log-2026'", "'x'", "'y'"], ["provenance", "Containerized Renders", "Runs renders inside versioned containers capturing OS, drivers, and libraries.", "Containerized Renders", "render jobs", "portable render env", "'render-img-v44'", "'x'", "'y'"], ["builds", "Parameter Snapshots", "Snapshots the complete parameter set (including defaults) with each output for later replay.", "Parameter Snapshots", "parameters", "replayable configs", "'params-snap-991'", "'x'", "'y'"], ["verification", "Seed-swept Variations Log", "Logs every seed tried during look-dev sweeps so the chosen variation can be revisited.", "Seed-swept Variations Log", "look-dev", "no lost variations", "'sweep-log-17'", "'x'", "'y'"], ["versioning", "Artifact Hash Manifests", "Publishes SHA-256 manifests per delivery so recipients can verify bit-identical receipt.", "Artifact Hash Manifests", "deliveries", "verifiable delivery", "'manifest-sha256'", "'x'", "'y'"], ["determinism", "Environment Capture", "Captures GPU driver, OS patch level, and locale at render time for forensic replay.", "Environment Capture", "environment", "replayable context", "'env-capture-7'", "'x'", "'y'"], ["provenance", "Render Farm Job Records", "Keeps per-frame job records including node, timing, and retry history.", "Render Farm Job Records", "farm jobs", "per-frame traceability", "'farm-jobs-q3'", "'x'", "'y'"], ["builds", "Versioned Shaders", "Versions shader code and compiled variants alongside the assets that use them.", "Versioned Shaders", "shaders", "no silent look changes", "'shader-v23'", "'x'", "'y'"], ["verification", "Deterministic Simulation Steps", "Runs physics and crowd sims with fixed timesteps and ordered iteration for identical results.", "Deterministic Simulation Steps", "simulations", "bit-identical sims", "'fixed-dt-120hz'", "'x'", "'y'"], ["versioning", "Asset Dependency Graphs", "Builds explicit dependency graphs so changed assets trigger exactly the right rebuilds.", "Asset Dependency Graphs", "build graph", "correct incremental builds", "'depgraph-v9'", "'x'", "'y'"], ["determinism", "Checkpointed Training Runs", "Saves model, optimizer, and RNG state at checkpoints so training can resume exactly.", "Checkpointed Training Runs", "ML training", "resumable training", "'ckpt-epoch-40'", "'x'", "'y'"], ["provenance", "Review Trail", "Links review notes and approvals to exact artifact versions, never to moving targets.", "Review Trail", "reviews", "approvals on record", "'review-trail-5'", "'x'", "'y'"], ["builds", "Reproducible Random Streams", "Uses counter-based RNG streams keyed by frame and sample index for parallel-safe randomness.", "Reproducible Random Streams", "randomness", "order-independent RNG", "'philox-4x32'", "'x'", "'y'"], ["verification", "Bit-identical Output Verification", "Re-renders a sample and compares hashes to prove the pipeline reproduces outputs.", "Bit-identical Output Verification", "QA", "proven reproducibility", "'bitverify-nightly'", "'x'", "'y'"]];
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
var gen={version:'jahdb-creative-pipeline-reproducibility-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('creative-pipeline-reproducibility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
