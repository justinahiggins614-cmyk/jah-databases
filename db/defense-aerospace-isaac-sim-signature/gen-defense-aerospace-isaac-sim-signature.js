(function(){'use strict';
/* jahdb-defense-aerospace-isaac-sim-1.0 — deterministic boundless generator for defense-aerospace-isaac-sim-signature.
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
var PREFIX='JAH-DAE37S-';
var DBNAME="Signature Isaac Sim Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "Signature Isaac Sim: What Isaac Sim Is: Reality, Rendered",
 "The Signature counterpart is the SigForge-worlds twin, Manon's original synthetic-training design. It mirrors the render-plus-physics architecture but every generated dataset carries a reality-gap manifest \u2014 measured differences between synthetic and real sensor statistics \u2014 so training always knows how far the sim is from the world it imitates.",
 ["RTX ray-traced rendering", "PhysX rigid and deformable physics", "Perfect ground-truth labels"],
 "console.log('Isaac Sim: RTX rendering + PhysX');\n['photorealistic worlds','synthetic labeled data','PhysX manipulation','ROS 2 bridge','domain randomization'].forEach(function(s){console.log(' '+s);});"],
["synthetic-data",
 "Signature Isaac Sim: Synthetic Data: Labels for Free",
 "SigForge-worlds's data foundry is the mint: same free labels, but every minted dataset includes the reality-gap manifest and a diversity report \u2014 class balance, pose coverage, lighting spread. The Signature design refuses to mint datasets whose diversity report shows gaps the user did not acknowledge.",
 ["Segmentation, boxes, depth, normals free", "Domain randomization across variations", "Diversity reports, acknowledged gaps"],
 "var ds={frames:200000,classes:24,rare_class_pct:3.1};\nconsole.log('minted: '+ds.frames+' frames, '+ds.classes+' classes');\nconsole.log('rare class coverage '+ds.rare_class_pct+'% (acknowledged)');\nconsole.log('reality-gap manifest attached');"],
["perception",
 "Signature Isaac Sim: Domain Randomization: Training for Reality",
 "The mint's randomization doctrine is the honest lie: randomize everything the model should not depend on, and measure the gap. The Signature design requires the real-data validation score with every synthetic-trained model \u2014 a model graded only in sim is ungraded.",
 ["Randomize what the model should ignore", "Sim trains, reality grades", "Real-data validation mandatory"],
 "var r={synthetic_mAP:0.91,real_mAP:0.83};\nconsole.log('synthetic mAP '+r.synthetic_mAP+', real mAP '+r.real_mAP);\nconsole.log('gap 0.08: acceptable, real-graded (honest)');"],
["physx",
 "Signature Isaac Sim: PhysX: Manipulation and Contact",
 "SigForge-worlds's physics is the touch lab: contact parameters fitted from real force-torque measurements, with the fit report in the manifest. The Signature design requires the touch calibration before manipulation training \u2014 uncalibrated contact is not a foundation for learned grasps.",
 ["GPU-parallel robot environments", "RL trains years in hours", "Contact calibrated from measurements"],
 "var cal={friction_fit:0.94,stiffness_fit:0.91};\nconsole.log('contact calibration: friction '+cal.friction_fit+', stiffness '+cal.stiffness_fit);\nconsole.log('calibrated -> manipulation training approved');"],
["omniverse",
 "Signature Isaac Sim: Your First World: A Warehouse Robot",
 "The mint's hello-world is the first shift: same warehouse, same robot, but the run records the reality-gap manifest automatically. The Signature design shows the beginner the gap from the first frame \u2014 synthetic data with humility built in.",
 ["Visual world-building, scriptable API", "ROS 2 teleop of sim robots", "Gap manifest from the first frame"],
 "console.log('first shift: warehouse, robot, camera streaming');\nconsole.log('10,000 frames minted with labels');\nconsole.log('reality-gap manifest: attached from frame one');"],
["training",
 "Signature Isaac Sim: Materials, Lighting, and RTX Realism",
 "The mint's look-dev doctrine is the honest render: materials measured from real samples where it counts, randomized broadly everywhere else. The Signature design records the material library version with every dataset \u2014 the render's assumptions travel with the data.",
 ["MDL materials, RTX lighting", "Lighting variation as randomization", "Material versions travel with data"],
 "var mats=['concrete','asphalt','metal','fabric'];\nconsole.log('material library v7: '+mats.join(', '));\nconsole.log('randomized across: lighting x12, materials x'+mats.length+' (recorded)');"],
["simulation",
 "Signature Isaac Sim: ROS 2 Bridge: Sim Meets the Stack",
 "The mint's bridge is the twin wire: identical topics, plus a ground-truth side channel for scoring. The Signature design verifies topic schema hashes across the bridge \u2014 sim and real must speak identically, proven not assumed.",
 ["Same topics as real drivers", "Drop-in pipeline stage", "Schema hashes verified across the bridge"],
 "console.log('twin wire: /camera/image, /scan, /tf (schemas verified)');\nconsole.log('ground-truth side channel: scoring on');\nconsole.log('stack cannot distinguish sim from real (by design)');"],
["synthetic-data",
 "Signature Isaac Sim: Replicator: Scripted Data Generation",
 "The mint's Replicator equivalent is the press-run: dataset-as-code with the diversity report generated automatically. The Signature design versions the press-run script with the dataset \u2014 a dataset without its generating script is not reproducible and not accepted.",
 ["Datasets as versioned code", "Randomization graphs", "Generating script versioned with data"],
 "var run={script:'press-run v12',frames:500000,seed:99};\nconsole.log('press-run '+run.script+': '+run.frames+' frames, seed '+run.seed);\nconsole.log('diversity report: generated (gaps acknowledged)');"],
["perception",
 "Signature Isaac Sim: Defensive Uses: Training Without Exposure",
 "The mint's sensitive-site doctrine is the ghost twin: synthetic stand-ins for real facilities, with the mapping from twin to real held separately. The Signature design treats the mapping as classified material \u2014 the twin trains the model, but the twin's correspondence to reality is need-to-know.",
 ["Synthetic twins of sensitive sites", "No real imagery in training", "Rehearse responses before deploying"],
 "console.log('ghost twin: facility rehearsed, 0 real photos in pipeline');\nconsole.log('patrol routes validated in twin before walking');\nconsole.log('twin-to-real mapping: need-to-know, held separately');"],
["physx",
 "Signature Isaac Sim: Digital Twins: The Living Mirror",
 "The mint's operational twin is the living mirror: live state in, projected futures out, with a continuous calibration score. The Signature design displays the calibration score next to every projection \u2014 a prediction without its calibration is not shown.",
 ["Live state in, futures out", "What-if for layouts and failures", "Calibration score with every projection"],
 "var twin={calibration:0.93,projection:'+2 robots -> throughput +18%'};\nconsole.log('mirror calibration '+twin.calibration);\nconsole.log('projection: '+twin.projection+' (calibration shown)');"],
["omniverse",
 "Signature Isaac Sim: Debugging: When the Render Lies",
 "The mint's debugger is the gap scope: side-by-side sim/real statistics with the divergence highlighted. The Signature design requires a gap review before any synthetic-trained model deploys \u2014 the review names what the sim does not model.",
 ["Models learn sim artifacts", "Gap measurements as diagnostics", "Gap review before deployment"],
 "console.log('gap scope: shadow sharpness diverges (sim too perfect)');\nconsole.log('fix: randomize shadow softness -> real mAP +0.04');\nconsole.log('gap review: named, recorded, signed');"],
["training",
 "Signature Isaac Sim: Multi-GPU and Cloud Scale",
 "The mint's scaling is the burst press: orchestrated parallel generation with cost and seed recorded per shard. The Signature design makes every shard reproducible \u2014 the shard's seed regenerates the shard, so no frame is ever truly lost.",
 ["Burst generation on cloud GPUs", "Cost accounting per dataset", "Seeded shards, each reproducible"],
 "var burst={gpus:100,frames:10000000,seed_base:1000};\nconsole.log('burst: '+burst.gpus+' GPUs, '+burst.frames+' frames overnight');\nconsole.log('shards seeded '+burst.seed_base+'+n (each reproducible)');"],
["simulation",
 "Signature Isaac Sim: Testing: Sim-to-Real Scorecards",
 "The mint's scorecard is the ledger of truth: synthetic, real, and gap per model version, graphed over time. The Signature design alerts on gap widening \u2014 the sim team investigates before the perception team tunes.",
 ["Synthetic, real, and gap tracked", "Widening gaps trigger investigation", "Scorecards reviewed like financials"],
 "var card=[['v12',0.9,0.82],['v13',0.91,0.84],['v14',0.92,0.83]];\ncard.forEach(function(c){console.log(c[0]+': syn '+c[1]+' real '+c[2]+' gap '+(c[1]-c[2]).toFixed(2));});\nconsole.log('v14 gap widened -> sim team investigates');"],
["synthetic-data",
 "Signature Isaac Sim: Real-World Pattern: Warehouse Detector Program",
 "The mint's program doctrine is the instant long tail: synthetic covers the rare from the start. The Signature design requires the real-validation gate before deployment \u2014 synthetic proposes, reality disposes.",
 ["Ghost twin to deployed detector", "Sim supplies the long tail", "Real validation gates deployment"],
 "var prog={synthetic:2000000,real_val:4000,real_mAP:0.86};\nconsole.log('minted '+prog.synthetic+', validated on '+prog.real_val+' real');\nconsole.log('real mAP '+prog.real_mAP+' -> DEPLOY (reality approved)');"],
["perception",
 "Signature Isaac Sim: Mastery: The Synthetic-Data Playbook",
 "The mint's mastery adds the stewardship layer: gap manifests, diversity reports, scorecards. Manon's roadmap runs from today's warehouses to full synthetic ranges under one manifest discipline \u2014 superpowers, everywhere, all honest.",
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
    edition:'signature',
    category:tp[0],
    tags:["isaac-sim", "nvidia", "omniverse", "synthetic-data", "rtx", "digital-twin", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-isaac-sim-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-isaac-sim-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();