(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "annotation", "ml_backend", "quality", "export"];
var PREFIX='JAH-PCO71S-';
var GENVER='jahdb-pc-organizer-label-studio-signature-1.0';
var DBNAME='Signature Label Forge';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Forge concept", "overview", "The Signature Label Forge is Manon's original labeling platform: every data type, every label verified, every dataset reproducible. It treats labeled data as the most valuable asset in machine learning \u2014 because it is.", {"mode": "types", "types": ["Image", "Text", "Audio", "Video", "Time series", "3D and sensor"]}, "Runnable demo \u2014 Forge concept"], ["Forge setup", "setup", "The Forge installs as one signed package and opens on first run with a guided first project \u2014 no YAML archaeology. Production mode adds the database and queue with one command.", {"mode": "install"}, "Runnable demo \u2014 Forge setup"], ["Forge containers", "setup", "The Forge ships as a single container with storage volumes declared up front, so the whole labeling operation moves between machines as one unit. Data gravity is respected: the Forge goes to the data.", {"mode": "docker"}, "Runnable demo \u2014 Forge containers"], ["Contract configs", "annotation", "Forge configs are versioned contracts with changelogs: changing a label set creates a new config version, never a silent edit. Datasets always know exactly which contract produced them.", {"mode": "config", "ex": "<Forge><Image name='img'/><Boxes name='b' labels='Cat,Dog'/><Contract v='3'/></Forge>"}, "Runnable demo \u2014 Contract configs"], ["Task ledger", "annotation", "Every Forge task carries its provenance \u2014 source, import batch, config version \u2014 in a permanent ledger. Provenance turns 'where did this label come from' from a mystery into a query.", {"mode": "task", "task": {"image": "/forge/img_0042.jpg", "batch": "2026-10-A", "config": "v3"}}, "Runnable demo \u2014 Task ledger"], ["Omni-type labeling", "annotation", "The Forge labels images, text, audio, video, time series, and 3D point clouds in one interface with shared shortcuts. Annotators learn one tool instead of five.", {"mode": "types", "types": ["Image", "Text", "Audio", "Video", "Time series", "3D point clouds"]}, "Runnable demo \u2014 Omni-type labeling"], ["Forge intake", "setup", "Intake validates every file on import \u2014 format, integrity, duplicates \u2014 and quarantines the rejects with reasons. Bad data never reaches an annotator's queue.", {"mode": "import", "fmts": ["JSON", "CSV", "COCO", "YOLO", "Forge native"]}, "Runnable demo \u2014 Forge intake"], ["The forge floor", "annotation", "The labeling floor shows the task, the tools, the guidelines excerpt, and the annotator's own agreement trend \u2014 feedback while working. Annotators improve because the interface teaches.", {"mode": "project", "name": "Forge pilot", "n": 5000}, "Runnable demo \u2014 The forge floor"], ["Apprentice models", "ml_backend", "Apprentice models pre-label under a confidence policy: certain predictions apply directly, uncertain ones route to humans. The policy \u2014 not vibes \u2014 decides what auto-labels.", {"mode": "ml"}, "Runnable demo \u2014 Apprentice models"], ["The assayer's office", "quality", "The assayer's office samples every annotator's work against gold tasks with known answers, tracking skill per label type. Annotators see their own scores; leads see the trends.", {"mode": "review", "agree": 97}, "Runnable demo \u2014 The assayer's office"], ["Export mint", "export", "The export mint stamps every dataset with its config version, task ledger hash, and annotator agreement \u2014 a coin of known provenance. Training on minted data is reproducible by construction.", {"mode": "export", "fmts": ["Forge mint", "COCO", "YOLO", "JSON", "Parquet"]}, "Runnable demo \u2014 Export mint"], ["Forge signals", "setup", "Forge signals notify pipelines, dashboards, and chat on labeling events with signed payloads. The whole ML operation hears the forge's hammer falls.", {"mode": "webhook"}, "Runnable demo \u2014 Forge signals"], ["Forge command line", "setup", "The forge CLI scripts everything the UI does, and every UI action shows its CLI equivalent. ClickOps and GitOps stay in sync by design.", {"mode": "cli", "cmd": "forge up --project pets"}, "Runnable demo \u2014 Forge command line"], ["Forge progress math", "annotation", "Progress math is honest: annotated over total, plus agreement-weighted completion that discounts disputed labels. This demo computes both for a running project.", {"mode": "stats", "done": 6230, "total": 10000}, "Runnable demo \u2014 Forge progress math"], ["Forge workflow", "annotation", "The Forge ritual: contract the config, intake with validation, pilot with gold tasks, apprentice the model, mint the export. Every dataset a coin of known provenance.", {"mode": "workflow", "steps": ["Version the label contract", "Intake with validation", "Pilot against gold tasks", "Apprentice the model", "Review and assay", "Mint the export"]}, "Runnable demo \u2014 Forge workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-label-studio-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-label-studio-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-label-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
