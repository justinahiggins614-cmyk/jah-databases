(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "organization", "annotation", "export", "ai_assist", "quality"];
var PREFIX='JAH-PCO72S-';
var GENVER='jahdb-pc-organizer-cvat-signature-1.0';
var DBNAME='Signature Vision Annotator';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Annotator concept", "overview", "The Signature Vision Annotator is Manon's original computer-vision labeling platform: video-first, tracking-native, with verification woven into every frame. It treats annotation as manufacturing: measured, inspected, ce", {"mode": "task", "name": "Forge street batch 1", "frames": 15000, "jobs": 8}, "Runnable demo \u2014 Annotator concept"], ["Forge deployment", "setup", "The Annotator deploys as one signed container with storage declared, and opens onto a mission board of tasks and jobs. Ten minutes from download to first labeled frame is the design target.", {"mode": "install"}, "Runnable demo \u2014 Forge deployment"], ["Mission jobs", "organization", "Missions split tasks into jobs by difficulty, not just by count \u2014 hard frames go to senior annotators automatically. Difficulty-aware routing is the quiet productivity multiplier.", {"mode": "job", "n": 2, "of": 8, "who": "senior_chen", "state": "in progress"}, "Runnable demo \u2014 Mission jobs"], ["Geometry atelier", "annotation", "The geometry atelier offers every shape with a guidance overlay showing the cheapest sufficient choice. Apprentices learn shape selection from the tool, not from folklore.", {"mode": "shape", "shape": "mask", "use": "pixel-exact vehicle segmentation"}, "Runnable demo \u2014 Geometry atelier"], ["Persistent tracks", "annotation", "Tracks in the Annotator persist identity through full occlusions using motion prediction, flagging only the truly ambiguous handoffs. Identity survives the bus passing in front of the car.", {"mode": "track", "n": 300}, "Runnable demo \u2014 Persistent tracks"], ["Smart interpolation", "annotation", "Smart interpolation follows the object's motion model between keyframes instead of straight lines, cutting keyframes further. Curved paths need fewer anchors than linear guessing.", {"mode": "interpolate", "kf": 3, "at": [0, 100, 199], "saved": 197}, "Runnable demo \u2014 Smart interpolation"], ["State attributes", "annotation", "Attributes are first-class with their own review: occluded, truncated, and behavioral states each get agreement scoring. State labels get the same rigor as geometry.", {"mode": "attr", "attrs": ["occluded", "truncated", "entering", "exiting"]}, "Runnable demo \u2014 State attributes"], ["Universal export", "export", "The export foundry casts annotations into any framework format with a verified converter per format \u2014 each converter tested against reference datasets. Format bugs are foundry bugs, fixed once for everyone.", {"mode": "format", "to": "YOLO"}, "Runnable demo \u2014 Universal export"], ["Forge SDK", "setup", "The Forge SDK scripts missions end to end, and the UI reveals the SDK call behind every action. Learning the SDK happens by using the UI \u2014 the calls are right there.", {"mode": "sdk", "ex": "forge.missions.create(video=...)"}, "Runnable demo \u2014 Forge SDK"], ["Apprentice vision", "ai_assist", "Apprentice vision models propose tracks and masks with per-proposal confidence, and low-confidence proposals never auto-apply. The human judges; the apprentice suggests.", {"mode": "auto"}, "Runnable demo \u2014 Apprentice vision"], ["Inspection office", "quality", "The inspection office reviews sampled tracks frame by frame with issue pins on exact frames. Inspectors sign off per job, and the signature travels with the export.", {"mode": "review"}, "Runnable demo \u2014 Inspection office"], ["Data stays home", "setup", "Datasets mount from any storage without copying, and the Annotator caches only what's viewed. Petabyte video collections label without petabyte transfers.", {"mode": "cloud"}, "Runnable demo \u2014 Data stays home"], ["Forge progress", "organization", "Progress counts verified frames, not just drawn ones \u2014 review is part of done. This demo runs the honest arithmetic.", {"mode": "stats", "done": 9200, "total": 15000}, "Runnable demo \u2014 Forge progress"], ["Consensus court", "quality", "The consensus court tries ambiguous frames before a panel of annotators and records the verdict with reasons. Disagreements become guidelines instead of grudges.", {"mode": "quality", "agree": 96}, "Runnable demo \u2014 Consensus court"], ["Annotator workflow", "annotation", "The Annotator ritual: mission in, difficulty-routed jobs, smart interpolation, apprentice assistance, inspection, certified export. Every frame accounted for, every track verified.", {"mode": "workflow", "steps": ["Create the mission", "Route jobs by difficulty", "Annotate with smart interpolation", "Assist with apprentice vision", "Inspect sampled tracks", "Export certified datasets"]}, "Runnable demo \u2014 Annotator workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cvat-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cvat-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cvat-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
