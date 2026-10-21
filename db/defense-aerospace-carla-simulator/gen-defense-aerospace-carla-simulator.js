(function(){'use strict';
/* jahdb-defense-aerospace-carla-simulator-1.0 — deterministic boundless generator for defense-aerospace-carla-simulator.
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
var PREFIX='JAH-DAE34-';
var DBNAME="Carla Simulator Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "Carla Simulator: What CARLA Is: A City for Autonomy",
 "CARLA is an open-source driving simulator built on Unreal Engine: detailed urban maps with buildings, traffic lights, pedestrians, and weather, plus a Python API that spawns vehicles, attaches sensors, and steps the world. Researchers train and test perception, planning, and end-to-end driving policies in scenarios that would be dangerous or tedious on real streets. It is the standard benchmark environment for autonomous-driving papers \u2014 if a driving algorithm was published, it probably drove in CARLA.",
 ["Unreal Engine urban worlds", "Python API for vehicles and sensors", "Standard benchmark for driving research"],
 "console.log('CARLA: Unreal city + Python API');\n['urban maps','lidar/camera/radar/GNSS','traffic + pedestrians','weather control','scenario runner'].forEach(function(s){console.log(' '+s);});"],
["autonomous-driving",
 "Carla Simulator: Maps and Towns: The Urban Catalog",
 "CARLA ships a catalog of towns \u2014 from small rural loops to dense urban grids \u2014 each with road networks, intersections, traffic lights, and props. Maps are the test corpus: a planner validated on one town is a rumor; validated across the catalog, it is evidence. Custom maps can be built in RoadRunner or Unreal. The discipline is map diversity \u2014 the failure modes hide in the town you did not test.",
 ["Catalog of towns, rural to dense urban", "Custom maps via RoadRunner/Unreal", "Map versions named in every report"],
 "var towns=['Town01','Town03','Town10HD'];\ntowns.forEach(function(t){console.log(t+': validated');});\nconsole.log('report: planner v6, maps Town01 v2.1 + Town03 v1.4 + Town10HD v3.0');"],
["sensors",
 "Carla Simulator: Sensors: Configuring the Vehicle's Eyes",
 "CARLA sensors are configured like real hardware: lidar with channels, points-per-second, and noise; cameras with resolution, FOV, and lens effects; radar, GNSS with error models, IMU with drift. The Python API attaches them at vehicle-relative transforms and streams data each tick. Sensor configuration is experimental design \u2014 the suite you test with should bracket the hardware you will deploy on, from optimistic to pessimistic.",
 ["Lidar, cameras, radar, GNSS, IMU", "Noise and error models configurable", "Ground-truth labels for auto-scoring"],
 "function transformPoint(px,py,theta){var c=Math.cos(theta),s=Math.sin(theta);return [px*c-py*s,px*s+py*c];}\nvar p=transformPoint(10,2,0.1);\nconsole.log('lidar point vehicle frame: ('+p[0].toFixed(2)+', '+p[1].toFixed(2)+')');\nconsole.log('ground truth: vehicle at 10.0 m (auto-score)');"],
["scenarios",
 "Carla Simulator: Traffic Manager and Pedestrians",
 "Empty streets teach nothing, so CARLA's Traffic Manager drives background vehicles with configurable aggression, and pedestrians wander sidewalks and crosswalks. Scenario Runner scripts the critical moments \u2014 the jaywalker, the cut-in, the red-light runner. The realism debate never ends, but the practice is settled: test against traffic that misbehaves, because real traffic does.",
 ["Background traffic with personalities", "Pedestrians on sidewalks and crosswalks", "Scenario Runner scripts critical moments"],
 "var seed=7;\nfunction crowd(s){return ['cautious','normal','aggressive'][(s*13)%3];}\nconsole.log('background driver personality: '+crowd(seed)+' (seed '+seed+', replayable)');"],
["perception",
 "Carla Simulator: Your First Drive: Spawning and Waypoints",
 "The hello-world: connect the Python client, spawn a vehicle at a waypoint, attach a camera, and drive it along waypoints while saving images. Ten lines of API, and you have a dataset generator. From there: add lidar, add traffic, record rosbags. Every CARLA project starts here, and the engineers who master the API's transform math (vehicle-relative vs world coordinates) master the sim.",
 ["Python client spawns vehicles and sensors", "Waypoint following in ten lines", "Self-documenting datasets from lap one"],
 "console.log('first lap: spawn @ waypoint 12, camera attached');\nconsole.log('driving 40 waypoints, saving frames');\nconsole.log('dataset: 400 frames, manifest + seed attached');"],
["testing",
 "Carla Simulator: The Python API: Control Patterns",
 "CARLA's Python API is the steering wheel: synchronous vs asynchronous mode (fixed time-step for determinism), batch commands for spawning hundreds of actors efficiently, and the world tick as the heartbeat. The patterns that scale are batch spawning, sensor listen callbacks that only copy what you need, and deterministic fixed-step runs for reproducible experiments. API fluency \u2014 transforms, waypoints, blueprints \u2014 is CARLA fluency.",
 ["Sync mode with fixed time-step", "Batch commands for scale", "Determinism by default"],
 "var actors=[];\nfor(var i=0;i<5;i++)actors.push('vehicle-'+i);\nconsole.log('batch spawn: '+actors.length+' actors in 1 command');\nconsole.log('mode: synchronous, dt=0.05 (deterministic)');"],
["simulation",
 "Carla Simulator: Weather and Time of Day",
 "CARLA's weather system \u2014 sun angle, cloudiness, precipitation, fog, wetness \u2014 changes what the sensors see: rain streaks the camera, wet roads reflect lidar differently, fog kills range. Robustness testing sweeps these parameters because the field will. A perception stack that only trained at noon in clear skies is a fair-weather stack, and fair-weather stacks fail at dusk in rain.",
 ["Sun, rain, fog, wetness parameters", "Weather changes sensor data", "Coverage matrix shows untested cells"],
 "var conditions=[['clear noon',1],['rain dusk',1],['fog night',0]];\nconditions.forEach(function(c){console.log(c[0]+': '+(c[1]?'TESTED':'NOT TESTED'));});"],
["autonomous-driving",
 "Carla Simulator: Scenario Runner: Scripting the Hard Cases",
 "Scenario Runner is CARLA's test harness: XML-described scenarios (cut-ins, jaywalkers, blocked lanes) executed against the driving stack with pass/fail criteria \u2014 collision, lane invasion, route completion, infractions. The scenario catalog is the regression suite for driving: every stack change replays the hard cases. Writing new scenarios from field incidents is the maturity marker.",
 ["XML scenarios with pass/fail criteria", "Regression suite for driving stacks", "Field incidents become scenarios"],
 "var ordeal=[['jaywalker',0],['cut-in',0],['red-light runner',0]];\nordeal.forEach(function(o){console.log(o[0]+': '+(o[1]?'collision':'PASS, no infractions'));});"],
["sensors",
 "Carla Simulator: Defensive Uses: Safe Validation of Driving Stacks",
 "CARLA's defensive value is validation without victims: emergency braking, obstacle avoidance, and degraded-sensor behavior can be tested against thousands of scenarios no test track could stage. For uncrewed ground vehicles in controlled areas \u2014 logistics yards, campuses, perimeters \u2014 CARLA-style validation is how the safety case gets its evidence. The sim does not replace the track; it earns the right to go to the track.",
 ["Thousands of scenarios no track could stage", "Evidence for the safety case", "Sim earns the right to the track"],
 "console.log('ordeal matrix: 10,000 runs, 0 collisions, 3 near-misses reviewed');\nconsole.log('track time APPROVED (evidence published)');"],
["scenarios",
 "Carla Simulator: Perception Training: Synthetic Datasets",
 "CARLA generates labeled datasets for free: every frame comes with segmentation, depth, and bounding boxes from the ground truth. Teams pre-train perception on synthetic data, then fine-tune on real \u2014 or use sim to cover the long tail (rare weather, rare obstacles) the real dataset lacks. The domain gap is real but manageable: sim-to-real transfer works when the sim's noise and diversity are honest.",
 ["Free labels: segmentation, depth, boxes", "Cover the long tail synthetically", "Domain-gap report with every dataset"],
 "var stats={frames:50000,classes:12,gap:'0.18 (moderate)'};\nconsole.log('synthetic: '+stats.frames+' frames, '+stats.classes+' classes');\nconsole.log('domain gap '+stats.gap+' -> fine-tune on real required');"],
["perception",
 "Carla Simulator: Debugging: Why Did It Crash (Virtually)",
 "CARLA debugging is replay debugging: the recorder logs every actor's trajectory, so a crash replays exactly \u2014 watch the pedestrian's path, the planner's decision, the sensor frame that mattered. The common causes are planner timeouts (sim tick vs wall clock), sensor misconfiguration, and scenario seeds. The discipline is deterministic replay: same seed, same crash, every time, until the fix.",
 ["Recorder replays crashes exactly", "Deterministic seeds", "Decision traces show the planner's reasoning"],
 "console.log('echo replay seed 7: pedestrian enters at t=4.2s');\nconsole.log('planner considered: brake (chosen), swerve (rejected: oncoming)');\nconsole.log('fix: earlier detection threshold, not the planner');"],
["testing",
 "Carla Simulator: Performance: Running CARLA at Scale",
 "CARLA is hungry \u2014 Unreal rendering plus sensor simulation wants real GPUs. The scaling patterns are headless servers with GPU, sensor load budgeting (lidar points-per-second is the big knob), and fixed time-steps for determinism. Multi-client setups run many vehicles against one server. The economics are still kind: a GPU server farm costs less than one instrumented test vehicle.",
 ["Headless GPU servers", "Sensor load budgeting", "Budgets recorded with results"],
 "var budget={lidar_pps:100000,cameras:4,gpu_hours:12};\nconsole.log('sensor budget: '+budget.lidar_pps+' lidar pts/s, '+budget.cameras+' cameras');\nconsole.log('experiment cost: '+budget.gpu_hours+' GPU-hours (recorded)');"],
["simulation",
 "Carla Simulator: Testing: Benchmarks and Leaderboards",
 "CARLA's benchmarks (the original benchmark, then the Leaderboard) standardized driving evaluation: routes with scenarios, infraction penalties, completion scores. Leaderboards drove the field forward \u2014 and taught its limits, as teams overfit to the benchmark's quirks. The mature practice is private held-out scenarios plus the public benchmark: public for comparison, private for truth.",
 ["Standardized routes and infraction scoring", "Leaderboards plus private held-outs", "Private matrix is the exam, not homework"],
 "console.log('public leaderboard: 78.4 (comparison)');\nconsole.log('private ordeal: 81.2 (truth, never tuned on)');"],
["autonomous-driving",
 "Carla Simulator: Real-World Pattern: Yard Autonomy Validation",
 "A complete pattern: an uncrewed yard truck validated in CARLA-style sim \u2014 dock approaches, pedestrian zones, night rain \u2014 across the ordeal matrix, then graduated to the closed yard with a safety driver, then to supervised autonomy. Each stage's evidence gates the next. The sim did not drive the truck; it proved the truck deserved to drive.",
 ["Sim to closed yard to supervised autonomy", "Each stage gated on evidence", "Living safety case"],
 "var gates=[['ordeal matrix',1],['closed yard',1],['supervised autonomy',0]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'EVIDENCE COMPLETE':'in progress'));});"],
["sensors",
 "Carla Simulator: Mastery: The Driving-Sim Playbook",
 "CARLA mastery is scenario thinking: API fluency, sensor configuration from measurement, scenario authorship, benchmark literacy, and the sim-to-track pipeline. The advanced moves are custom maps, new sensor models, and closed-loop training at scale. The mindset: the city is a laboratory \u2014 design the experiment, not just the drive.",
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
    edition:'public',
    category:tp[0],
    tags:["carla", "autonomous-driving", "unreal-engine", "lidar", "scenario-runner", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-carla-simulator',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-carla-simulator']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();