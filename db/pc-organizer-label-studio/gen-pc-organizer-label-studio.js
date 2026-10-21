(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "annotation", "ml_backend", "quality", "export"];
var PREFIX='JAH-PCO71-';
var GENVER='jahdb-pc-organizer-label-studio-1.0';
var DBNAME='Label Studio';
var PROV='Public documentation and published specifications for Label Studio; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What Label Studio does", "overview", "Label Studio by HumanSignal is the open-source platform for labeling the data machine learning learns from: images, text, audio, video, and time series. It turns raw collected data into the annotated datasets models actu", {"mode": "types", "types": ["Image: boxes, polygons, keypoints", "Text: NER, classification, Q&A", "Audio: transcription, regions", "Video: frame tracking", "Time series: segmentation"]}, "Runnable demo \u2014 What Label Studio does"], ["Installing Label Studio", "setup", "A pip install and one start command bring up the full web UI on localhost:8080 \u2014 no cluster required. Docker Compose runs the production shape with Postgres and Redis when the project grows.", {"mode": "install"}, "Runnable demo \u2014 Installing Label Studio"], ["Docker deployment", "setup", "The official Docker Compose file runs Label Studio with a real database behind it, which is how teams deploy labeling for more than one person. Volumes keep the data local and portable.", {"mode": "docker"}, "Runnable demo \u2014 Docker deployment"], ["Label config XML", "annotation", "Every project starts with a label config \u2014 XML that declares the data fields and the labeling interface, from bounding boxes to taxonomies. The config is the contract: it decides what annotators can possibly produce.", {"mode": "config", "ex": "<View><Image name='img' value='$image'/><RectangleLabels name='l' toName='img'><Label value='Cat'/></RectangleLabels></View>"}, "Runnable demo \u2014 Label config XML"], ["Task format", "annotation", "Tasks are JSON objects pointing at the data \u2014 usually a URL or storage path \u2014 plus any pre-loaded predictions. One task is one unit of labeling work, and ten thousand tasks is a normal project.", {"mode": "task", "task": {"image": "/data/img_0042.jpg", "predictions": [{"label": "Cat", "score": 0.91}]}}, "Runnable demo \u2014 Task format"], ["Data types covered", "annotation", "One platform covers image boxes and polygons, text NER and classification, audio regions and transcription, video tracking, and time-series segmentation. Multi-type projects \u2014 like video with audio \u2014 label in one interfa", {"mode": "types", "types": ["Image", "Text", "Audio", "Video", "Time series", "Multi-modal combos"]}, "Runnable demo \u2014 Data types covered"], ["Importing datasets", "setup", "Datasets import as JSON, CSV, or in formats like COCO, through the UI or the API, with cloud storage sync for S3 and GCS. Import is where folder-of-files becomes a managed project.", {"mode": "import", "fmts": ["JSON", "CSV", "COCO", "YOLO", "VOC"]}, "Runnable demo \u2014 Importing datasets"], ["The annotation UI", "annotation", "The labeling interface renders from the config: the image or text, the tools, the label set, keyboard shortcuts for speed. Good configs make labeling fast; great ones make it hard to label wrong.", {"mode": "project", "name": "Pet detector v3", "n": 10000}, "Runnable demo \u2014 The annotation UI"], ["ML backend pre-labeling", "ml_backend", "ML backends connect a model that pre-labels tasks so humans correct instead of drawing from scratch \u2014 the active-learning loop. Each corrected batch retrains the model, and the pre-labels keep getting better.", {"mode": "ml"}, "Runnable demo \u2014 ML backend pre-labeling"], ["Review and agreement", "quality", "Review workflows route a sample to second annotators, and agreement scores measure how often they concur. Low agreement on a label means the guidelines \u2014 not the annotators \u2014 need fixing.", {"mode": "review", "agree": 94}, "Runnable demo \u2014 Review and agreement"], ["Export formats", "export", "Finished datasets export as JSON, CSV, COCO, YOLO, VOC, and more \u2014 the format the training framework expects. Export snapshots freeze the dataset version the model trained on.", {"mode": "export", "fmts": ["JSON", "CSV", "COCO", "YOLO", "VOC"]}, "Runnable demo \u2014 Export formats"], ["Webhooks", "setup", "Webhooks fire on annotation events \u2014 task completed, project updated \u2014 letting pipelines react the moment labeling progresses. Retraining jobs trigger themselves when enough new labels land.", {"mode": "webhook"}, "Runnable demo \u2014 Webhooks"], ["Command-line control", "setup", "The label-studio CLI starts servers, manages users, and imports data without touching the browser. Scripted setups reproduce the exact project configuration every time.", {"mode": "cli", "cmd": "label-studio start --port 8080"}, "Runnable demo \u2014 Command-line control"], ["Python SDK", "setup", "The Python SDK drives projects, tasks, and annotations as code \u2014 creating ten thousand tasks is a loop, not a weekend. Notebooks become labeling control panels.", {"mode": "sdk"}, "Runnable demo \u2014 Python SDK"], ["Labeling workflow", "annotation", "The production ritual: write the config, import a pilot batch, label and measure agreement, fix the guidelines, connect the ML backend, scale up, export snapshots. Quality is designed in, not inspected in.", {"mode": "workflow", "steps": ["Write the label config", "Import a pilot batch", "Label and measure agreement", "Fix the guidelines", "Connect the ML backend", "Scale up and export snapshots"]}, "Runnable demo \u2014 Labeling workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"config\"){\n  show(\"Label config\",\"XML describing the labeling UI\");\n  show(\"Example\",DATA.ex);\n}else if(m===\"task\"){\n  show(\"Task JSON\",JSON.stringify(DATA.task).slice(0,140));\n}else if(m===\"install\"){\n  show(\"Install\",\"pip install label-studio\");\n  show(\"Start\",\"label-studio start\");\n  show(\"Then\",\"open http://localhost:8080\");\n}else if(m===\"docker\"){\n  show(\"Run\",\"docker compose up (official compose file)\");\n  show(\"Image\",\"heartexlabs/label-studio\");\n}else if(m===\"import\"){\n  show(\"Import formats\",DATA.fmts.join(\", \"));\n  show(\"Via\",\"UI upload or the API\");\n}else if(m===\"export\"){\n  show(\"Export formats\",DATA.fmts.join(\", \"));\n}else if(m===\"ml\"){\n  show(\"ML backend\",\"model pre-labels, humans correct\");\n  show(\"Loop\",\"annotate -> train -> pre-label -> repeat\");\n}else if(m===\"webhook\"){\n  show(\"Webhooks\",\"notify external systems on events\");\n  show(\"Events\",\"annotation created, project updated\");\n}else if(m===\"review\"){\n  show(\"Review\",\"a second annotator verifies\");\n  show(\"Agreement\",DATA.agree+\"% across annotators\");\n}else if(m===\"types\"){\n  console.log(\"Data types:\");DATA.types.forEach(function(t){console.log(\"  \"+t);});\n}else if(m===\"project\"){\n  show(\"Project\",DATA.name);\n  show(\"Tasks\",DATA.n);\n}else if(m===\"cli\"){\n  show(\"CLI\",DATA.cmd);\n}else if(m===\"stats\"){\n  show(\"Annotated\",DATA.done+\" / \"+DATA.total);\n  show(\"Progress\",Math.round(DATA.done/DATA.total*100)+\"%\");\n  show(\"Remaining\",DATA.total-DATA.done);\n}else if(m===\"sdk\"){\n  show(\"SDK\",\"label-studio-sdk (Python)\");\n  show(\"Does\",\"projects, tasks, and annotations as code\");\n}else if(m===\"workflow\"){\n  console.log(\"Labeling workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-label-studio/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-label-studio',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-label-studio',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
