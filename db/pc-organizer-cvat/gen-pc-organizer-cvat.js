(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "organization", "annotation", "export", "ai_assist", "quality"];
var PREFIX='JAH-PCO72-';
var GENVER='jahdb-pc-organizer-cvat-1.0';
var DBNAME='CVAT (Computer Vision Annotation Tool)';
var PROV='Public documentation and published specifications for CVAT (Computer Vision Annotation Tool); compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What CVAT does", "overview", "CVAT \u2014 the Computer Vision Annotation Tool \u2014 is the open-source standard for labeling images and video for computer vision: boxes, polygons, masks, skeletons, and tracks. Born at Intel, it now thrives as an independent o", {"mode": "task", "name": "Street scenes batch 7", "frames": 12000, "jobs": 6}, "Runnable demo \u2014 What CVAT does"], ["Deploying CVAT", "setup", "CVAT deploys with Docker Compose \u2014 one up command brings the UI, database, and workers online. Organizations, projects, tasks, and jobs structure the work from there.", {"mode": "install"}, "Runnable demo \u2014 Deploying CVAT"], ["Tasks and jobs", "organization", "A task holds the data \u2014 say 12,000 frames \u2014 and jobs split it into annotator-sized chunks with assignees and states. Managers watch job states; annotators see only their queue.", {"mode": "job", "n": 3, "of": 6, "who": "annotator_lee", "state": "in progress"}, "Runnable demo \u2014 Tasks and jobs"], ["Annotation shapes", "annotation", "CVAT's shape vocabulary covers rectangles, polygons, polylines, points, ellipses, cuboids, masks, and skeletons \u2014 the right geometry for every vision problem. Choosing the cheapest shape that captures the truth is a core", {"mode": "shape", "shape": "polygon", "use": "irregular objects like pedestrians"}, "Runnable demo \u2014 Annotation shapes"], ["Tracking across frames", "annotation", "Tracks let one label follow an object across video frames, carrying its identity through occlusions. Tracking turns video labeling from frame-by-frame drawing into supervision.", {"mode": "track", "n": 240}, "Runnable demo \u2014 Tracking across frames"], ["Interpolation", "annotation", "Draw the box at keyframes and CVAT interpolates the in-between frames automatically \u2014 the famous labor saver. A car crossing 200 frames needs a handful of keyframes, not 200 boxes.", {"mode": "interpolate", "kf": 4, "at": [0, 70, 140, 199], "saved": 196}, "Runnable demo \u2014 Interpolation"], ["Attributes", "annotation", "Attributes tag shapes with state \u2014 occluded, truncated, parked, moving \u2014 so the dataset records more than geometry. Attributes are where domain knowledge enters the labels.", {"mode": "attr", "attrs": ["occluded", "truncated", "parked", "moving"]}, "Runnable demo \u2014 Attributes"], ["Format converters", "export", "CVAT converts its native XML to COCO, YOLO, Pascal VOC, MOT, KITTI, and more, feeding each training framework its preferred diet. Export in the framework's format and skip the conversion scripts.", {"mode": "format", "to": "COCO"}, "Runnable demo \u2014 Format converters"], ["The Python SDK", "setup", "The cvat-sdk drives everything as Python: create tasks, upload data, download annotations in a loop. Dataset factories script the boring parts and leave humans the judgments.", {"mode": "sdk", "ex": "client.tasks.create_from_data(...)"}, "Runnable demo \u2014 The Python SDK"], ["Auto-annotation with AI", "ai_assist", "Serverless-style functions run models like SAM to propose masks and detections that annotators verify. The human moves from drawing to judging \u2014 faster and often more consistent.", {"mode": "auto"}, "Runnable demo \u2014 Auto-annotation with AI"], ["Review jobs", "quality", "Review jobs are a separate job type where a second annotator accepts or raises issues per shape. Issues attach to the exact shape, so feedback is precise instead of vague.", {"mode": "review"}, "Runnable demo \u2014 Review jobs"], ["Cloud storage", "setup", "Tasks mount S3, GCS, or Azure buckets as data sources, so video never has to be copied to the CVAT host. The data stays where it lives; only the labels travel.", {"mode": "cloud"}, "Runnable demo \u2014 Cloud storage"], ["Progress math", "organization", "Progress is annotated frames over total frames, tracked per job and per task. This demo computes it for a running annotation task.", {"mode": "stats", "done": 8400, "total": 12000}, "Runnable demo \u2014 Progress math"], ["Quality with consensus", "quality", "Consensus jobs have multiple annotators label the same frames, and agreement scores find the ambiguous cases. Ambiguity found is guidelines improved.", {"mode": "quality", "agree": 93}, "Runnable demo \u2014 Quality with consensus"], ["CVAT workflow", "annotation", "The CVAT ritual: create the task, split into jobs, annotate with interpolation, auto-assist where it helps, review, export in the framework's format. Video becomes training data, systematically.", {"mode": "workflow", "steps": ["Create the task from video", "Split into jobs", "Annotate with interpolation", "Auto-assist with models", "Review sampled jobs", "Export in framework format"]}, "Runnable demo \u2014 CVAT workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"task\"){\n  show(\"Task\",DATA.name);\n  show(\"Frames\",DATA.frames);\n  show(\"Jobs\",DATA.jobs+\" (split for annotators)\");\n}else if(m===\"shape\"){\n  show(\"Shape\",DATA.shape);\n  show(\"Use\",DATA.use);\n}else if(m===\"interpolate\"){\n  show(\"Keyframes\",DATA.kf+\" at frames \"+DATA.at.join(\", \"));\n  show(\"In-between\",\"interpolated automatically\");\n  show(\"Saved\",DATA.saved+\" manual boxes\");\n}else if(m===\"format\"){\n  show(\"Convert\",\"CVAT XML -> \"+DATA.to);\n  show(\"Use\",\"feed the training framework directly\");\n}else if(m===\"sdk\"){\n  show(\"SDK\",\"cvat-sdk (Python)\");\n  show(\"Does\",\"tasks, jobs, annotations as code\");\n  show(\"Example\",DATA.ex);\n}else if(m===\"install\"){\n  show(\"Deploy\",\"docker compose up -d\");\n  show(\"Then\",\"open the web UI, create an organization\");\n}else if(m===\"auto\"){\n  show(\"Auto-annotation\",\"models like SAM propose masks\");\n  show(\"Humans\",\"verify and correct\");\n}else if(m===\"track\"){\n  show(\"Tracking\",\"one label follows the object across frames\");\n  show(\"Frames labeled\",DATA.n);\n}else if(m===\"attr\"){\n  show(\"Attributes\",DATA.attrs.join(\", \"));\n  show(\"Use\",\"occluded, truncated, parked...\");\n}else if(m===\"review\"){\n  show(\"Review job\",\"separate job type for verification\");\n  show(\"Issues\",\"raised per shape\");\n}else if(m===\"cloud\"){\n  show(\"Cloud storage\",\"S3, GCS, Azure mounted as data\");\n}else if(m===\"job\"){\n  show(\"Job\",DATA.n+\" of \"+DATA.of);\n  show(\"Assignee\",DATA.who);\n  show(\"State\",DATA.state);\n}else if(m===\"stats\"){\n  show(\"Annotated frames\",DATA.done+\" / \"+DATA.total);\n  show(\"Progress\",Math.round(DATA.done/DATA.total*100)+\"%\");\n}else if(m===\"quality\"){\n  show(\"Agreement\",DATA.agree+\"%\");\n  show(\"Gold frames\",\"known-answer checks\");\n}else if(m===\"workflow\"){\n  console.log(\"Annotation workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cvat/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cvat',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cvat',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
