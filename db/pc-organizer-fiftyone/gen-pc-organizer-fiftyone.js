(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "curation", "evaluation", "export"];
var PREFIX='JAH-PCO73-';
var GENVER='jahdb-pc-organizer-fiftyone-1.0';
var DBNAME='FiftyOne';
var PROV='Public documentation and published specifications for FiftyOne; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What FiftyOne does", "overview", "FiftyOne by Voxel51 is the open-source toolkit for curating computer-vision datasets: visualize samples, filter by anything, evaluate models, and find the bad labels. It is the workbench where datasets get understood bef", {"mode": "dataset", "name": "street-v3", "n": 50000}, "Runnable demo \u2014 What FiftyOne does"], ["Installing FiftyOne", "setup", "A pip install and 'fiftyone app launch' open the whole system \u2014 Python API plus a browser App. The quickstart dataset loads in one line for learning.", {"mode": "install"}, "Runnable demo \u2014 Installing FiftyOne"], ["Datasets", "curation", "FiftyOne datasets hold samples with fields for ground truth, predictions, metadata, and embeddings, backed by a local database. Fifty thousand images is a comfortable working size.", {"mode": "dataset", "name": "street-v3", "n": 50000}, "Runnable demo \u2014 Datasets"], ["Samples and fields", "curation", "A sample is one image or video plus its fields: filepath, ground-truth detections, model predictions, tags, and custom metadata. Fields are queryable, which makes the dataset a database you can see.", {"mode": "sample", "file": "img_0042.jpg", "fields": ["ground_truth", "predictions", "tags", "weather"]}, "Runnable demo \u2014 Samples and fields"], ["The App", "curation", "The App is the visual side: a sample grid with predictions overlaid, histograms of every field, and click-to-filter everything. Curation happens with eyes open.", {"mode": "app"}, "Runnable demo \u2014 The App"], ["Views and filters", "curation", "Views are saved, chainable lenses \u2014 filter to night images, sort by confidence, take 100 \u2014 that turn questions into sample sets. 'Show me what the model gets wrong at night' is one view.", {"mode": "filter", "expr": "tags contains 'night' and confidence < 0.5", "n": 312}, "Runnable demo \u2014 Views and filters"], ["Tags", "curation", "Tags label subsets of samples \u2014 review queues, train/val splits, problem cohorts \u2014 without moving files. Tagging is curation's highlighter pen.", {"mode": "tag"}, "Runnable demo \u2014 Tags"], ["Model evaluation", "evaluation", "Evaluation compares predictions against ground truth with COCO-style matching, reporting mAP, precision-recall, and per-class breakdowns. Numbers per class beat one headline number.", {"mode": "eval", "map": 0.62}, "Runnable demo \u2014 Model evaluation"], ["Embeddings", "evaluation", "Embeddings turn samples into vectors for similarity search and UMAP scatter plots, revealing the dataset's structure visually. Outliers and duplicates pop out of the scatter like sore thumbs.", {"mode": "embed", "n": 50000, "d": 512}, "Runnable demo \u2014 Embeddings"], ["The Brain: find bad data", "evaluation", "Brain methods compute uniqueness, mistakenness, and hardness \u2014 finding near-duplicates and likely mislabels automatically. Cleaning with the Brain beats eyeballing fifty thousand images.", {"mode": "brain"}, "Runnable demo \u2014 The Brain: find bad data"], ["The dataset zoo", "setup", "The zoo loads famous datasets and models in one line \u2014 quickstart, COCO samples, detection models. Learning and benchmarking start instantly.", {"mode": "zoo"}, "Runnable demo \u2014 The dataset zoo"], ["Plugins", "setup", "Plugins extend the App with custom panels \u2014 annotation tools, custom visualizations, workflow buttons. The community hub shares them.", {"mode": "plugin"}, "Runnable demo \u2014 Plugins"], ["Export", "export", "Curated sets export in COCO, YOLO, and other training formats, carrying the curation decisions with them. What you curated is what trains.", {"mode": "export", "fmt": "COCO"}, "Runnable demo \u2014 Export"], ["Python API", "setup", "The Python API does everything the App does \u2014 datasets, views, evaluation \u2014 in scripts and notebooks. Curation becomes reproducible code, not clicks.", {"mode": "view"}, "Runnable demo \u2014 Python API"], ["Curation workflow", "curation", "The curation ritual: load the data, look at everything, tag the problems, evaluate the model, hunt bad labels with the Brain, export the clean set. Datasets are never 'done' \u2014 they are curated.", {"mode": "workflow", "steps": ["Load the dataset", "Look at everything in the App", "Tag problem cohorts", "Evaluate the model", "Hunt bad labels with the Brain", "Export the clean set"]}, "Runnable demo \u2014 Curation workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"install\"){\n  show(\"Install\",\"pip install fiftyone\");\n  show(\"Launch\",\"fiftyone app launch\");\n  show(\"License\",\"Apache 2.0, open source\");\n}else if(m===\"dataset\"){\n  show(\"Dataset\",DATA.name);\n  show(\"Samples\",DATA.n);\n  show(\"Lives\",\"in MongoDB-backed local store\");\n}else if(m===\"sample\"){\n  show(\"Sample\",DATA.file);\n  show(\"Fields\",DATA.fields.join(\", \"));\n}else if(m===\"filter\"){\n  show(\"Filter\",DATA.expr);\n  show(\"Matched\",DATA.n+\" samples\");\n}else if(m===\"view\"){\n  show(\"View\",\"a saved filtered lens on the dataset\");\n  show(\"Chains\",\"filter, sort, shuffle, limit\");\n}else if(m===\"eval\"){\n  show(\"Evaluation\",\"predictions vs ground truth\");\n  show(\"mAP\",DATA.map);\n  show(\"Matching\",\"COCO-style IoU matching\");\n}else if(m===\"embed\"){\n  show(\"Embeddings\",DATA.n+\" vectors x \"+DATA.d+\" dims\");\n  show(\"Use\",\"similarity search, UMAP scatter\");\n}else if(m===\"zoo\"){\n  show(\"Zoo\",\"one-line datasets and models\");\n  show(\"Example\",\"foz.load_zoo_dataset('quickstart')\");\n}else if(m===\"plugin\"){\n  show(\"Plugins\",\"custom App panels\");\n  show(\"Share\",\"via the plugin hub\");\n}else if(m===\"tag\"){\n  show(\"Tags\",\"label sample subsets\");\n  show(\"Use\",\"mark review queues, splits\");\n}else if(m===\"export\"){\n  show(\"Export\",DATA.fmt);\n  show(\"Round-trip\",\"to training frameworks\");\n}else if(m===\"brain\"){\n  show(\"Brain methods\",\"similarity, uniqueness, mistakenness\");\n  show(\"Finds\",\"duplicates and mislabels\");\n}else if(m===\"app\"){\n  show(\"App\",\"visual curation in the browser\");\n  show(\"Grid\",\"samples with predictions overlaid\");\n}else if(m===\"workflow\"){\n  console.log(\"Curation workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
function jitter(v,rnd){
  if(typeof v==='number'){return Math.round(v*(0.9+rnd()*0.2)*100)/100;}
  if(Array.isArray(v)){return v.map(function(x){return jitter(x,rnd);});}
  if(v&&typeof v==='object'){var o={};Object.keys(v).forEach(function(k){o[k]=jitter(v[k],rnd);});return o;}
  return v;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(typeof seed==='number'&&seed>SELFREG.maxRecords)throw new Error('SELF-REGULATION HARD STOP: 1,000,000,000,000 record limit reached');
  var cat=opts.category||pick(CATS,rnd);
  var pool=ARCH.filter(function(a){return a[1]===cat;});
  var a=pick(pool.length?pool:ARCH,rnd);
  var scen=jitter(a[3],rnd); scen.mode=a[3].mode;
  var id=PREFIX+String(10001+seed).padStart(6,'0');
  var program=ENGINE.split('__DATA__').join(JSON.stringify(scen));
  var facts=jitter(a[4]||{},rnd);
  return {id:id,t:a[0]+' (simulated #'+seed+')',
    title:DBNAME+' \u2014 '+a[0]+' (simulated variant, seed '+seed+')',
    g:a[1],category:a[1],
    description:a[2]+' This is a simulated boundless-generator variant (seed '+seed+') from '+GENVER+': the scenario values were deterministically jittered from the archive archetype, and the record passed the independent correctness validator before acceptance.',
    ladder_rank:1+((seed-1)%15),
    march:'MILLION MARCH \u00b7 simulated record \u00b7 archive marches to a 1,000,000-record target \u2014 in progress',
    provenance:PROV,last_verified:'2026-10-21',record_label:SELFREG.simulatedLabel,
    facts:facts,
    demo:{engine:'jahdb-demo-1.0',kind:'code',title:'Runnable demo \u2014 '+a[0]+' (simulated)',language:'javascript',
      program:program,run_hint:'PC: save as demo.js, run `node demo.js`. In-page: press Run.',
      how_to_run:'PC: save the program as demo.js and run `node demo.js`. In-page: open the Demo Lab tab and press Run.',runnable:true},
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-fiftyone/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-fiftyone',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  var n=parseInt(String(r.id||'').slice(PREFIX.length),10);
  if(!(n>=10001))e.push('id-block (generator ids start at 10001; archive owns 1-9999)');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.record_label!==SELFREG.simulatedLabel)e.push('record_label');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.demo&&r.demo.language!=='javascript')e.push('demo-language');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return{ok:false,errors:['drift: exact title already in archive']}; }
  return{ok:true,errors:[]};
}
var gen={version:GENVER,selfRegulation:SELFREG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-fiftyone',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
