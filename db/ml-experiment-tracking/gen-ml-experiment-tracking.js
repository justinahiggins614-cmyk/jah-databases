(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["platform", "visualization", "reproducibility", "optimization", "registry", "collaboration"] */
var CATS=["platform", "visualization", "reproducibility", "optimization", "registry", "collaboration"];
var PREFIX='JAH-MLEXP-';
var FIELDS=["tool_type", "key_features", "integrations", "pricing_model"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["platform", "Weights & Biases", "The hosted experiment platform: metric dashboards, sweeps, artifacts, and model registry.", "Weights & Biases (W&B) is the most widely used hosted ML experiment tracker: log metrics, hyperparameters, and artifacts from training with a few lines of code; compare runs on interactive dashboards; run hyperparameter sweeps; and version datasets and models. Its Tables and Reports support collaboration, and Weave adds LLM tracing. Free tier for individuals; team/enterprise plans for orgs.", "hosted platform", ["metric dashboards", "sweeps", "artifact versioning", "model registry", "LLM tracing (Weave)"], "PyTorch, TensorFlow, JAX, Hugging Face, Lightning", "Free tier; per-seat team plans", "python", "Log a run to W&B", "import wandb\nwandb.init(project=\"lane-e-demo\", config={\"lr\": 3e-4, \"batch\": 32})\nfor step in range(3):\n    wandb.log({\"loss\": 1.0/(step+1), \"step\": step})\nwandb.finish()\nprint(\"run logged\")"],
 ["platform", "MLflow", "The open-source lifecycle platform: tracking, projects, models, and registry — self-hosted.", "MLflow (Databricks/LF AI) is the open standard for ML lifecycle management: Tracking logs params/metrics/artifacts to a local or remote server; Projects package code reproducibly; Models standardizes deployment flavors; Model Registry versions and stages models. Self-hostable, language-agnostic (Python/R/Java), and the default in many enterprises that need on-prem tracking.", "open-source platform", ["experiment tracking", "model registry", "deployment flavors", "projects"], "Scikit-learn, PyTorch, TensorFlow, Spark, ONNX", "Free/open-source (self-hosted)", "python", "Log a run to MLflow", "import mlflow\nmlflow.set_experiment(\"lane-e-demo\")\nwith mlflow.start_run():\n    mlflow.log_param(\"lr\", 3e-4)\n    mlflow.log_metric(\"loss\", 0.42, step=1)\nprint(\"mlflow run complete\")"],
 ["visualization", "TensorBoard", "TensorFlow's visualizer, now framework-agnostic: scalars, histograms, embeddings, and graphs.", "TensorBoard started as TensorFlow's dashboard but now logs from PyTorch, JAX, and others via event files: scalar curves, histograms of weights, embedding projector, and graph visualization. It is local-first (tensorboard --logdir), free, and still the fastest way to eyeball a training run. The What-If Tool and profiler plugins extend it to fairness and performance analysis.", "visualization", ["scalar/histogram plots", "embedding projector", "graph viz", "profiler"], "TensorFlow, PyTorch, JAX (via event files)", "Free/open-source", "python", "Log scalars to TensorBoard", "from torch.utils.tensorboard import SummaryWriter\nw = SummaryWriter(\"runs/demo\")\nfor i in range(5):\n    w.add_scalar(\"loss\", 1.0/(i+1), i)\nw.close()\nprint(\"run: tensorboard --logdir runs\")"],
 ["platform", "Neptune.ai", "Hosted tracking with strong metadata organization for teams and foundation-model scale.", "Neptune.ai is a hosted experiment tracker emphasizing metadata structure: runs, models, and artifacts organized in queryable namespaces, with collaboration features and SSO for teams. It handles large-scale logging (foundation-model training) and offers flexible metadata schemas versus rigid run tables. Pricing is usage-based.", "hosted platform", ["metadata namespaces", "team collaboration", "large-scale logging", "queryable runs"], "PyTorch, TensorFlow, Optuna, Lightning", "Free tier; usage-based plans", "python", "Log to Neptune", "import neptune\nrun = neptune.init_run(project=\"ws/demo\", api_token=\"ANON\")\nrun[\"params/lr\"] = 3e-4\nrun[\"metrics/loss\"].append(0.42)\nrun.stop()\nprint(\"neptune run logged\")"],
 ["platform", "Comet ML", "Hosted tracking with model production monitoring and LLM observability.", "Comet ML offers experiment tracking plus model production monitoring (drift, performance) and an LLM layer (prompt tracking, evaluations). Its panels and custom visualizations suit teams that want tracking and monitoring from one vendor. Free for individuals; team plans scale by seats.", "hosted platform", ["experiment tracking", "production monitoring", "LLM observability", "custom panels"], "PyTorch, TensorFlow, Hugging Face, LangChain", "Free tier; per-seat plans", "python", "Log to Comet", "from comet_ml import Experiment\nexp = Experiment(project_name=\"lane-e-demo\", api_key=\"dummy\")\nexp.log_parameter(\"lr\", 3e-4)\nexp.log_metric(\"loss\", 0.42, step=1)\nexp.end()\nprint(\"comet run logged\")"],
 ["platform", "ClearML", "Open-source MLOps with automatic code and environment capture — 'it just logs everything'.", "ClearML (formerly Trains) auto-captures code, packages, and configs with minimal instrumentation, plus experiment tracking, pipelines, and remote execution (agents that run jobs on queues). The open-source core is self-hosted; paid tiers add hosted scale. Its strength is low-friction adoption: wrap your script and get full provenance.", "open-source MLOps", ["auto-magic logging", "pipelines", "remote agents", "model registry"], "PyTorch, TensorFlow, XGBoost", "Free/open-source core; hosted tiers", "python", "ClearML auto-logging", "from clearml import Task\ntask = Task.init(project_name=\"lane-e\", task_name=\"demo\")\ntask.connect({\"lr\": 3e-4})\nprint(\"ClearML captures code + env automatically\")"],
 ["visualization", "Aim", "Open-source tracker built for 100K-run scale with a superb query UI.", "Aim is an open-source experiment tracker designed for massive run counts: metrics stored efficiently, a Pythonic query API (run.hparams.lr > 0.001), and rich dashboards. Self-hosted, lightweight, and beloved by researchers who outgrow spreadsheets but distrust vendor lock-in.", "open-source tracker", ["100K-run scale", "query API", "rich dashboards", "images/audio logging"], "PyTorch, TensorFlow, JAX", "Free/open-source", "python", "Log to Aim", "from aim import Run\nrun = Run(experiment=\"lane-e-demo\")\nrun[\"hparams\"] = {\"lr\": 3e-4}\nfor i in range(3):\n    run.track(1.0/(i+1), name=\"loss\", step=i)\nprint(\"aim run logged\")"],
 ["reproducibility", "DVC", "Git for data: version datasets and models alongside code with content-addressed storage.", "DVC (Data Version Control) versions large files via small metafiles committed to Git, with content-addressed remotes (S3, GCS, local). dvc.yaml defines reproducible pipelines (stages with deps/outs); dvc repro reruns what changed; dvc exp run manages experiments. It is the missing piece that makes 'git clone' reproduce the data too.", "data versioning", ["data versioning", "pipelines", "experiment management", "remote storage"], "Git, S3/GCS/Azure, MLflow", "Free/open-source; Studio hosted", "shell", "Version a dataset with DVC", "dvc init\ndvc add data/train.csv\ngit add data/train.csv.dvc .gitignore\ngit commit -m \"track dataset v1\"\ndvc push  # to configured remote"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,title:b[1],t:b[1],g:cat,c:1,summary:b[2],details:b[3]};
  for(var i=0;i<FIELDS.length;i++){rec[FIELDS[i]]=b[4+i];}
  var di=4+FIELDS.length;
  rec.ladder_rank=1+(seed%3);
  rec.demo={language:b[di],title:b[di+1],program:b[di+2]};
  rec.provenance="JAH Databases generator (archive-style records)";
  rec.last_verified='2026-10-20';
  rec.src="public-harvest";
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||!r.summary.length)e.push('summary');
  if(typeof r.details!=='string'||!r.details.length)e.push('details');
  if(CATS.indexOf(r.g)<0)e.push('g');
  for(var i=0;i<FIELDS.length;i++){
    var v=r[FIELDS[i]];
    if(v===undefined||v===null||(typeof v==='string'&&!v.length))e.push('field:'+FIELDS[i]);
  }
  if(!(r.ladder_rank===1||r.ladder_rank===2||r.ladder_rank===3))e.push('ladder_rank');
  var d=r.demo;
  if(!d||typeof d.language!=='string'||!d.language.length||typeof d.title!=='string'||!d.title.length||typeof d.program!=='string'||!d.program.length)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-20')e.push('last_verified');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ml-experiment-tracking-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ml-experiment-tracking',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
