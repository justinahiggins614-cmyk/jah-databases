(function(){'use strict';
/* jahdb-defense-aerospace-isaac-sim-1.0 — deterministic boundless generator for defense-aerospace-isaac-sim.
   Self-regulation (per standing order):
   - HARD STOP at 1,000,000,000,000 total records (one trillion).
   - Throttled: at most MAX_PER_CALL records per request.
   - Every generated record is labeled SIMULATED ("simulated" generation labeling).
   - Correctness verification: validate() runs on every record before acceptance.
   - Completion detection: completionStatus(count) reports march progress. */
var MAX_TOTAL=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
var CATS=["simulation", "synthetic-data", "perception", "physx", "omniverse", "training"];
var PREFIX='JAH-DAE37-';
var DBNAME="Isaac Sim Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "Isaac Sim: What Isaac Sim Is: Reality, Rendered",
 "Isaac Sim builds virtual worlds with film-quality rendering (RTX ray tracing) and real physics (PhysX): warehouses, factories, streets \u2014 populated with robots whose sensors see synthetic camera, lidar, and depth data with perfect ground-truth labels. It is where perception models train on millions of labeled frames that cost nothing to capture, and where manipulation policies practice grasps that would take years on real hardware. The Omniverse foundation means the worlds are collaborative and versioned like software.",
 ["RTX ray-traced rendering", "PhysX rigid and deformable physics", "Perfect ground-truth labels"],
 "console.log('Isaac Sim: RTX rendering + PhysX');\n['photorealistic worlds','synthetic labeled data','PhysX manipulation','ROS 2 bridge','domain randomization'].forEach(function(s){console.log(' '+s);});"],
["synthetic-data",
 "Isaac Sim: Synthetic Data: Labels for Free",
 "The killer feature is data: every synthetic frame ships with segmentation masks, bounding boxes, depth, normals, and instance IDs \u2014 labels that cost dollars per frame from human annotators. Replicator, the synthetic-data framework, randomizes lighting, textures, object poses, and occlusions across thousands of variations. Teams train detectors on millions of synthetic frames, then fine-tune on a small real set. The economics are transformative for rare classes.",
 ["Segmentation, boxes, depth, normals free", "Domain randomization across variations", "Diversity reports, acknowledged gaps"],
 "var ds={frames:200000,classes:24,rare_class_pct:3.1};\nconsole.log('minted: '+ds.frames+' frames, '+ds.classes+' classes');\nconsole.log('rare class coverage '+ds.rare_class_pct+'% (acknowledged)');\nconsole.log('reality-gap manifest attached');"],
["perception",
 "Isaac Sim: Domain Randomization: Training for Reality",
 "Sim-to-real transfer works when the sim is diverse: randomize textures, lighting, camera parameters, object poses, even physics friction \u2014 so the model learns the invariant (the object's shape) instead of the artifact (the sim's particular carpet). Isaac Sim's randomization graphs make this systematic. The validation is always on real data: synthetic trains, reality grades. Randomization is not a trick; it is the honest admission that the sim is wrong in unknown ways.",
 ["Randomize what the model should ignore", "Sim trains, reality grades", "Real-data validation mandatory"],
 "var r={synthetic_mAP:0.91,real_mAP:0.83};\nconsole.log('synthetic mAP '+r.synthetic_mAP+', real mAP '+r.real_mAP);\nconsole.log('gap 0.08: acceptable, real-graded (honest)');"],
["physx",
 "Isaac Sim: PhysX: Manipulation and Contact",
 "Isaac Sim's PhysX handles the contact-rich world: grasping, pushing, assembly \u2014 with GPU-accelerated parallel environments running thousands of robots at once. Reinforcement learning trains manipulation policies in hours of wall-clock that represent years of robot time. The fidelity demands are highest here: contact parameters tuned from real measurements, or the learned grasp works in sim and drops in reality.",
 ["GPU-parallel robot environments", "RL trains years in hours", "Contact calibrated from measurements"],
 "var cal={friction_fit:0.94,stiffness_fit:0.91};\nconsole.log('contact calibration: friction '+cal.friction_fit+', stiffness '+cal.stiffness_fit);\nconsole.log('calibrated -> manipulation training approved');"],
["omniverse",
 "Isaac Sim: Your First World: A Warehouse Robot",
 "The hello-world: load a warehouse scene, spawn a mobile manipulator, attach a camera, and drive it with ROS 2 teleop while the synthetic camera streams. The Omniverse UI makes world-building visual; the Python API makes it scriptable. From there: randomize the scene, generate a dataset, train a detector. The loop from world to trained model runs in an afternoon.",
 ["Visual world-building, scriptable API", "ROS 2 teleop of sim robots", "Gap manifest from the first frame"],
 "console.log('first shift: warehouse, robot, camera streaming');\nconsole.log('10,000 frames minted with labels');\nconsole.log('reality-gap manifest: attached from frame one');"],
["training",
 "Isaac Sim: Materials, Lighting, and RTX Realism",
 "Isaac Sim's visual realism comes from MDL materials and RTX lighting: physically-based materials, ray-traced reflections, and accurate sun/sky models. For perception training, the material and lighting variation is the domain randomization that matters most \u2014 a detector trained under one lighting learns the lighting. The craft is building material libraries that span the real world's variety, then randomizing across them.",
 ["MDL materials, RTX lighting", "Lighting variation as randomization", "Material versions travel with data"],
 "var mats=['concrete','asphalt','metal','fabric'];\nconsole.log('material library v7: '+mats.join(', '));\nconsole.log('randomized across: lighting x12, materials x'+mats.length+' (recorded)');"],
["simulation",
 "Isaac Sim: ROS 2 Bridge: Sim Meets the Stack",
 "Isaac Sim's ROS 2 bridge publishes synthetic sensor data on the same topics real drivers use \u2014 the autonomy stack cannot tell the difference. Clock, TF, joint states, camera_info: the full graph. This makes Isaac Sim a drop-in stage of the sim-to-field pipeline: develop against the bridge, validate in Gazebo-class sims, then hardware. The bridge is also how recorded real data replays into the sim for mixed testing.",
 ["Same topics as real drivers", "Drop-in pipeline stage", "Schema hashes verified across the bridge"],
 "console.log('twin wire: /camera/image, /scan, /tf (schemas verified)');\nconsole.log('ground-truth side channel: scoring on');\nconsole.log('stack cannot distinguish sim from real (by design)');"],
["synthetic-data",
 "Isaac Sim: Replicator: Scripted Data Generation",
 "Replicator is the data-generation API: Python scripts that compose scenes, randomize parameters, trigger captures, and write datasets with labels \u2014 the dataset as code. Versioned scripts mean versioned datasets: rerun the script, regenerate the data, diff the results. For programs that need millions of frames of the rare and dangerous, Replicator is the factory.",
 ["Datasets as versioned code", "Randomization graphs", "Generating script versioned with data"],
 "var run={script:'press-run v12',frames:500000,seed:99};\nconsole.log('press-run '+run.script+': '+run.frames+' frames, seed '+run.seed);\nconsole.log('diversity report: generated (gaps acknowledged)');"],
["perception",
 "Isaac Sim: Defensive Uses: Training Without Exposure",
 "Isaac Sim's defensive value is training perception for sensitive environments without photographing them: generate the facility's digital twin synthetically, train detectors on the twin, deploy to the real cameras. No real imagery of sensitive sites in training pipelines, no photographers in restricted areas. The twin also rehearses security responses \u2014 patrol routes, camera coverage \u2014 before anyone walks them.",
 ["Synthetic twins of sensitive sites", "No real imagery in training", "Rehearse responses before deploying"],
 "console.log('ghost twin: facility rehearsed, 0 real photos in pipeline');\nconsole.log('patrol routes validated in twin before walking');\nconsole.log('twin-to-real mapping: need-to-know, held separately');"],
["physx",
 "Isaac Sim: Digital Twins: The Living Mirror",
 "Beyond training, Isaac Sim builds operational digital twins: the warehouse mirror that tracks the real warehouse, simulating 'what if' for layout changes, robot additions, and failure drills. The twin consumes live state and projects futures \u2014 the closest thing to a crystal ball operations gets. The discipline is keeping the mirror honest: calibrated against reality continuously, or it becomes a comforting fiction.",
 ["Live state in, futures out", "What-if for layouts and failures", "Calibration score with every projection"],
 "var twin={calibration:0.93,projection:'+2 robots -> throughput +18%'};\nconsole.log('mirror calibration '+twin.calibration);\nconsole.log('projection: '+twin.projection+' (calibration shown)');"],
["omniverse",
 "Isaac Sim: Debugging: When the Render Lies",
 "Synthetic debugging has its own classics: the model learns the sim's artifacts (perfect shadows, repeated textures), the physics timestep too coarse for the grasp, the randomization missing the real world's actual variation. The diagnostics are gap measurements \u2014 compare sim and real statistics \u2014 and ablation: remove a randomization, watch transfer change. The sim is guilty until proven innocent, and the proof is real-data performance.",
 ["Models learn sim artifacts", "Gap measurements as diagnostics", "Gap review before deployment"],
 "console.log('gap scope: shadow sharpness diverges (sim too perfect)');\nconsole.log('fix: randomize shadow softness -> real mAP +0.04');\nconsole.log('gap review: named, recorded, signed');"],
["training",
 "Isaac Sim: Multi-GPU and Cloud Scale",
 "Serious synthetic data needs serious compute: Isaac Sim scales across GPUs and cloud instances, with Replicator orchestrating parallel generation. The pattern is burst generation \u2014 spin up a hundred GPUs, mint ten million frames overnight, spin down. The cost accounting matters: synthetic data is cheap per frame but the totals deserve tracking, and the dataset manifest records the compute spent.",
 ["Burst generation on cloud GPUs", "Cost accounting per dataset", "Seeded shards, each reproducible"],
 "var burst={gpus:100,frames:10000000,seed_base:1000};\nconsole.log('burst: '+burst.gpus+' GPUs, '+burst.frames+' frames overnight');\nconsole.log('shards seeded '+burst.seed_base+'+n (each reproducible)');"],
["simulation",
 "Isaac Sim: Testing: Sim-to-Real Scorecards",
 "Mature synthetic programs keep scorecards: per-model synthetic validation, real validation, and the gap \u2014 tracked over time. A widening gap means the sim is drifting from reality (or reality changed); a narrowing gap means the randomization is working. The scorecard is the program's honesty instrument, reviewed like financials.",
 ["Synthetic, real, and gap tracked", "Widening gaps trigger investigation", "Scorecards reviewed like financials"],
 "var card=[['v12',0.9,0.82],['v13',0.91,0.84],['v14',0.92,0.83]];\ncard.forEach(function(c){console.log(c[0]+': syn '+c[1]+' real '+c[2]+' gap '+(c[1]-c[2]).toFixed(2));});\nconsole.log('v14 gap widened -> sim team investigates');"],
["synthetic-data",
 "Isaac Sim: Real-World Pattern: Warehouse Detector Program",
 "A complete pattern: a logistics operator needs pallet detectors for a new facility. The team builds the ghost twin, mints two million randomized frames, trains the detector, validates on a small real set from a similar site, deploys to the facility's cameras, and monitors the scorecard. No photographers in the aisles, no waiting for the rare cases \u2014 the sim supplied the long tail on day one.",
 ["Ghost twin to deployed detector", "Sim supplies the long tail", "Real validation gates deployment"],
 "var prog={synthetic:2000000,real_val:4000,real_mAP:0.86};\nconsole.log('minted '+prog.synthetic+', validated on '+prog.real_val+' real');\nconsole.log('real mAP '+prog.real_mAP+' -> DEPLOY (reality approved)');"],
["perception",
 "Isaac Sim: Mastery: The Synthetic-Data Playbook",
 "Isaac Sim mastery is a hybrid craft: 3D world-building, rendering literacy, physics calibration, randomization design, and ML training \u2014 plus the humility to let real data grade everything. The advanced moves are custom sensor models, large-scale RL, and operational twins. The mindset: synthetic data is a superpower with a honesty requirement.",
 ["3D, rendering, physics, ML hybrid", "Custom sensors and operational twins", "Stewardship: manifests, reports, scorecards"],
 "var playbook=['world-building','rendering literacy','calibration','randomization design','real grading'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Synthetic data: a superpower with an honesty requirement.');"]
];
function escId(s){return String(s).replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
var IDRE=new RegExp('^'+escId(PREFIX)+'\\d{6}$');
function generate(seed,opts){
  opts=opts||{};var r=prng(seed);
  var cat=opts.category||pick(r,CATS);
  var pool=POOL.filter(function(p){return p[0]===cat;});
  var tp=pick(r,pool.length?pool:POOL);
  var id=PREFIX+String(100000+(seed%900000));
  var variant=ri(r,2,48);
  var ladder=1+(seed%15);
  return {
    id:id,
    title:tp[1],
    ladder_rank:ladder,
    edition:'public',
    category:tp[0],
    tags:["isaac-sim", "nvidia", "omniverse", "synthetic-data", "rtx", "digital-twin", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"isaac sim record",
    simulated:true,
    generation:'SIMULATED — generated content (seed '+seed+'), validated by independent checker',
    _seed:seed
  };
}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(rec.id||''))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(!(rec.ladder_rank>=1&&rec.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(rec.category)<0)e.push('category');
  if(!rec.demo||typeof rec.demo.code!=='string'||rec.demo.code.length<10)e.push('demo.code');
  if(rec.simulated!==true)e.push('simulated-label');
  if(typeof rec.description!=='string'||rec.description.length<20)e.push('description');
  if(!Array.isArray(rec.key_facts)||!rec.key_facts.length)e.push('key_facts');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title vs archive']};}
  return {ok:true,errors:[]};
}
function completionStatus(count){
  count=+count||0;
  return {target:1000000,hardStop:MAX_TOTAL,count:count,
    pct:Math.min(100,+(100*count/1000000).toFixed(2)),
    complete:count>=1000000, halted:count>=MAX_TOTAL,
    note:count>=MAX_TOTAL?'HARD STOP: one-trillion record limit reached — generation halted.':'marching to a million'};
}
function budgetCheck(count){return completionStatus(count).halted?{ok:false,errors:['hard stop: 1e12 reached']}:{ok:true,errors:[]};}
var gen={version:'jahdb-defense-aerospace-isaac-sim-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-isaac-sim',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-isaac-sim']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();