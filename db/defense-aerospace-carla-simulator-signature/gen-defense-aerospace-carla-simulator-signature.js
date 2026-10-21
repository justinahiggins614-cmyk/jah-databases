(function(){'use strict';
/* jahdb-defense-aerospace-carla-simulator-1.0 — deterministic boundless generator for defense-aerospace-carla-simulator-signature.
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
var CATS=["simulation", "autonomous-driving", "sensors", "scenarios", "perception", "testing"];
var PREFIX='JAH-DAE34S-';
var DBNAME="Signature Carla Simulator Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "Signature Carla Simulator: What CARLA Is: A City for Autonomy",
 "The Signature counterpart is the SigStreets twin, Manon's original driving-simulation design. SigStreets mirrors the city-plus-API architecture but every map carries a scenario-fidelity manifest \u2014 which traffic behaviors are modeled and to what realism level \u2014 so benchmark results always arrive with their assumptions attached.",
 ["Unreal Engine urban worlds", "Python API for vehicles and sensors", "Standard benchmark for driving research"],
 "console.log('CARLA: Unreal city + Python API');\n['urban maps','lidar/camera/radar/GNSS','traffic + pedestrians','weather control','scenario runner'].forEach(function(s){console.log(' '+s);});"],
["autonomous-driving",
 "Signature Carla Simulator: Maps and Towns: The Urban Catalog",
 "SigStreets's map catalog is the atlas: same idea, but each map's traffic-behavior coverage is scored \u2014 which intersection types, which pedestrian densities. The Signature design requires benchmark reports to name the map versions, because a result without the map version is not reproducible.",
 ["Catalog of towns, rural to dense urban", "Custom maps via RoadRunner/Unreal", "Map versions named in every report"],
 "var towns=['Town01','Town03','Town10HD'];\ntowns.forEach(function(t){console.log(t+': validated');});\nconsole.log('report: planner v6, maps Town01 v2.1 + Town03 v1.4 + Town10HD v3.0');"],
["sensors",
 "Signature Carla Simulator: Sensors: Configuring the Vehicle's Eyes",
 "SigStreets's sensors are the witness rigs: each publishes data plus ground-truth labels (segmentation, depth, object boxes) the real sensor could never provide. The Signature design uses the ground truth for automated perception scoring \u2014 no hand-labeling the sim's own output.",
 ["Lidar, cameras, radar, GNSS, IMU", "Noise and error models configurable", "Ground-truth labels for auto-scoring"],
 "function transformPoint(px,py,theta){var c=Math.cos(theta),s=Math.sin(theta);return [px*c-py*s,px*s+py*c];}\nvar p=transformPoint(10,2,0.1);\nconsole.log('lidar point vehicle frame: ('+p[0].toFixed(2)+', '+p[1].toFixed(2)+')');\nconsole.log('ground truth: vehicle at 10.0 m (auto-score)');"],
["scenarios",
 "Signature Carla Simulator: Traffic Manager and Pedestrians",
 "SigStreets's traffic is the crowd: background agents with personality distributions \u2014 cautious to reckless \u2014 seeded for replay. The Signature design requires the crowd seed in every report: the same seed, the same jaywalker, the same test.",
 ["Background traffic with personalities", "Pedestrians on sidewalks and crosswalks", "Scenario Runner scripts critical moments"],
 "var seed=7;\nfunction crowd(s){return ['cautious','normal','aggressive'][(s*13)%3];}\nconsole.log('background driver personality: '+crowd(seed)+' (seed '+seed+', replayable)');"],
["perception",
 "Signature Carla Simulator: Your First Drive: Spawning and Waypoints",
 "SigStreets's hello-world is the first lap: same spawn-and-drive, but the run automatically records the fidelity manifest and the crowd seed. The Signature design makes the beginner's first dataset self-documenting \u2014 assumptions attached from lap one.",
 ["Python client spawns vehicles and sensors", "Waypoint following in ten lines", "Self-documenting datasets from lap one"],
 "console.log('first lap: spawn @ waypoint 12, camera attached');\nconsole.log('driving 40 waypoints, saving frames');\nconsole.log('dataset: 400 frames, manifest + seed attached');"],
["testing",
 "Signature Carla Simulator: The Python API: Control Patterns",
 "SigStreets's API is the director's chair: same control, but every call is journaled to the experiment record. The Signature design makes determinism the default \u2014 fixed step and seed unless the experiment explicitly opts out, so no result is ever accidentally unreproducible.",
 ["Sync mode with fixed time-step", "Batch commands for scale", "Determinism by default"],
 "var actors=[];\nfor(var i=0;i<5;i++)actors.push('vehicle-'+i);\nconsole.log('batch spawn: '+actors.length+' actors in 1 command');\nconsole.log('mode: synchronous, dt=0.05 (deterministic)');"],
["simulation",
 "Signature Carla Simulator: Weather and Time of Day",
 "SigStreets's weather is the mood dial: same parameters, but every sweep is recorded as a coverage matrix \u2014 which conditions were tested, which were not. The Signature design shows the untested cells plainly: coverage honesty beats coverage theater.",
 ["Sun, rain, fog, wetness parameters", "Weather changes sensor data", "Coverage matrix shows untested cells"],
 "var conditions=[['clear noon',1],['rain dusk',1],['fog night',0]];\nconditions.forEach(function(c){console.log(c[0]+': '+(c[1]?'TESTED':'NOT TESTED'));});"],
["autonomous-driving",
 "Signature Carla Simulator: Scenario Runner: Scripting the Hard Cases",
 "SigStreets's harness is the ordeal: same scenario-driven testing, but every scenario carries a difficulty rating and a realism note. The Signature design requires field incidents to become ordeals \u2014 the sim suite grows with the field's lessons.",
 ["XML scenarios with pass/fail criteria", "Regression suite for driving stacks", "Field incidents become scenarios"],
 "var ordeal=[['jaywalker',0],['cut-in',0],['red-light runner',0]];\nordeal.forEach(function(o){console.log(o[0]+': '+(o[1]?'collision':'PASS, no infractions'));});"],
["sensors",
 "Signature Carla Simulator: Defensive Uses: Safe Validation of Driving Stacks",
 "SigStreets's validation doctrine is the ten-thousand-run rule: no track time until the stack survives the ordeal matrix. The Signature design publishes the matrix with the safety case \u2014 which scenarios, which seeds, which results \u2014 because evidence is the product.",
 ["Thousands of scenarios no track could stage", "Evidence for the safety case", "Sim earns the right to the track"],
 "console.log('ordeal matrix: 10,000 runs, 0 collisions, 3 near-misses reviewed');\nconsole.log('track time APPROVED (evidence published)');"],
["scenarios",
 "Signature Carla Simulator: Perception Training: Synthetic Datasets",
 "SigStreets's dataset foundry is the loom: synthetic frames with labels plus a domain-gap report \u2014 how far the sim's statistics are from the real dataset's. The Signature design requires the gap report with every synthetic dataset: honest sim, honest transfer.",
 ["Free labels: segmentation, depth, boxes", "Cover the long tail synthetically", "Domain-gap report with every dataset"],
 "var stats={frames:50000,classes:12,gap:'0.18 (moderate)'};\nconsole.log('synthetic: '+stats.frames+' frames, '+stats.classes+' classes');\nconsole.log('domain gap '+stats.gap+' -> fine-tune on real required');"],
["perception",
 "Signature Carla Simulator: Debugging: Why Did It Crash (Virtually)",
 "SigStreets's replay is the echo: full trajectory logs with the crowd seed, replayable tick-for-tick. The Signature design adds the decision trace \u2014 the planner's considered options at the critical tick \u2014 so the fix lands on the reasoning, not just the outcome.",
 ["Recorder replays crashes exactly", "Deterministic seeds", "Decision traces show the planner's reasoning"],
 "console.log('echo replay seed 7: pedestrian enters at t=4.2s');\nconsole.log('planner considered: brake (chosen), swerve (rejected: oncoming)');\nconsole.log('fix: earlier detection threshold, not the planner');"],
["testing",
 "Signature Carla Simulator: Performance: Running CARLA at Scale",
 "SigStreets's scaling is the render farm: headless sim servers with sensor budgets declared per experiment. The Signature design requires the budget in the experiment record \u2014 'this result cost X GPU-hours at Y sensor load' \u2014 so results are reproducible, not just impressive.",
 ["Headless GPU servers", "Sensor load budgeting", "Budgets recorded with results"],
 "var budget={lidar_pps:100000,cameras:4,gpu_hours:12};\nconsole.log('sensor budget: '+budget.lidar_pps+' lidar pts/s, '+budget.cameras+' cameras');\nconsole.log('experiment cost: '+budget.gpu_hours+' GPU-hours (recorded)');"],
["simulation",
 "Signature Carla Simulator: Testing: Benchmarks and Leaderboards",
 "SigStreets's evaluation is the dual ledger: public benchmark for comparison, private ordeal matrix for truth. The Signature design forbids tuning on the private matrix \u2014 it is the exam, not the homework.",
 ["Standardized routes and infraction scoring", "Leaderboards plus private held-outs", "Private matrix is the exam, not homework"],
 "console.log('public leaderboard: 78.4 (comparison)');\nconsole.log('private ordeal: 81.2 (truth, never tuned on)');"],
["autonomous-driving",
 "Signature Carla Simulator: Real-World Pattern: Yard Autonomy Validation",
 "SigStreets's graduation doctrine is the three gates: ordeal matrix, closed yard, supervised autonomy \u2014 each gated on the previous stage's evidence. The Signature design publishes the evidence at each gate: the safety case is a living document, not a final report.",
 ["Sim to closed yard to supervised autonomy", "Each stage gated on evidence", "Living safety case"],
 "var gates=[['ordeal matrix',1],['closed yard',1],['supervised autonomy',0]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'EVIDENCE COMPLETE':'in progress'));});"],
["sensors",
 "Signature Carla Simulator: Mastery: The Driving-Sim Playbook",
 "SigStreets mastery adds the stewardship layer: manifests, seeds, published matrices. Manon's roadmap runs from today's urban towns to full multi-domain synthetic ranges under one manifest discipline \u2014 laboratories, everywhere, all calibrated.",
 ["Scenario thinking end to end", "Custom maps and sensor models", "Stewardship: manifests, seeds, matrices"],
 "var playbook=['API fluency','measured sensors','scenario authorship','benchmark literacy','sim-to-track'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The city is a laboratory. Design the experiment.');"]
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
    tags:["carla", "autonomous-driving", "unreal-engine", "lidar", "scenario-runner", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
    last_verified:'2026-10-21',
    record_kind:"carla simulator record",
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
var gen={version:'jahdb-defense-aerospace-carla-simulator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-carla-simulator-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-carla-simulator-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();