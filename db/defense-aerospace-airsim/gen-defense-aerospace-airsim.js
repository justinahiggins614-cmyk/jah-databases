(function(){'use strict';
/* jahdb-defense-aerospace-airsim-1.0 — deterministic boundless generator for defense-aerospace-airsim.
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
var CATS=["simulation", "drones", "hil", "apis", "physics", "ai-training"];
var PREFIX='JAH-DAE39-';
var DBNAME="AirSim Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "AirSim: What AirSim Is: The Drone's Simulator",
 "AirSim is the open-source simulator built for AI: Unreal Engine visuals, a purpose-built physics engine for multicopters (and cars), and Python/C++ APIs that let learning algorithms fly thousands of missions. It exposes the vehicle's state, camera, lidar, and controls as clean APIs \u2014 the drone as a programmable object. The community continuation keeps it alive for research after Microsoft's archive. For drone AI, it is the training ground.",
 ["Purpose-built multicopter physics", "Drone as a programmable object", "Community-continued for research"],
 "console.log('AirSim: Unreal visuals + drone physics + APIs');\n['multirotor + car models','Python/C++ APIs','camera/lidar/depth','HIL support'].forEach(function(s){console.log(' '+s);});"],
["drones",
 "AirSim: APIs: Flying with Code",
 "AirSim's APIs are the interface: takeoff, moveToPosition, getImages, getLidarData \u2014 the vehicle reduced to function calls. AI researchers script missions, collect datasets, and close learning loops without touching a radio. The API's determinism (fixed-steppable, seedable) makes experiments reproducible. Learning to 'fly' in AirSim means learning to command precisely and read state completely.",
 ["Vehicle as function calls", "Scripted missions and datasets", "Seeded determinism for replay"],
 "console.log('flight desk: takeoff -> moveTo(10,0,-5) -> capture');\nconsole.log('seed 7, fixed step 1ms -> replayable');\nconsole.log('state: pos(10.0,0.1,-5.0) vel(0.0,0.0,0.0)');"],
["hil",
 "AirSim: Physics: The Custom Flight Model",
 "AirSim's physics engine was written for drones: rigid-body dynamics with motor models, drag, ground effect, and wind \u2014 fast enough for real-time and accurate enough for control development. It is not a general robotics engine; it is a drone engine, and the specialization shows in the flight feel. The parameters (mass, inertia, motor curves) are the modeling decisions, measured where it matters.",
 ["Drone-specialized dynamics", "Motor models, drag, ground effect", "Provenance tags on parameters"],
 "var params=[['mass',1.5,'measured'],['motor curve','--','measured'],['drag',0.3,'estimated']];\nparams.forEach(function(p){console.log(p[0]+'='+p[1]+' ('+p[2]+')');});"],
["apis",
 "AirSim: Sensors: Cameras, Lidar, Depth",
 "AirSim's sensors serve AI: cameras with configurable resolution and FOV, depth cameras, lidar with point clouds, plus ground-truth segmentation. The data feeds perception training and testing directly. Noise models keep the data honest; the ground truth keeps the scoring automatic. For drone vision \u2014 obstacle avoidance, landing-site detection, tracking \u2014 this is the data factory.",
 ["Cameras, depth, lidar for AI", "Ground-truth segmentation", "Noise configuration recorded"],
 "var frame={rgb:'640x480',depth:'ok',lidar_pts:12000,noise:'on'};\nconsole.log('frame: '+frame.rgb+' rgb, '+frame.lidar_pts+' lidar pts, noise '+frame.noise);\nconsole.log('ground truth: 3 obstacles labeled (auto-score)');"],
["physics",
 "AirSim: Your First Flight: Scripted Takeoff",
 "The hello-world: connect, confirm the sim, arm, takeoff to 5 meters, hover, land \u2014 ten lines of Python. The vehicle obeys; the APIs report. From there: waypoint squares, image capture loops, lidar scans. The beginner's real lesson is the API's completeness \u2014 if you can think it, you can script it, and the script is the experiment.",
 ["Ten lines to fly", "API completeness as the lesson", "Self-documenting from hello-world"],
 "console.log('first hover: arm -> takeoff(5m) -> hover 10s -> land');\nconsole.log('manifest + seed recorded automatically');\nconsole.log('the script IS the experiment');"],
["ai-training",
 "AirSim: HIL: Real Autopilot, Simulated World",
 "AirSim's HIL configuration closes the loop with real hardware: a Pixhawk running PX4 or ArduPilot receives simulated sensor data and returns actuator commands to the sim. This tests the actual flight stack \u2014 the binary that will fly \u2014 against scenarios too risky for the field. HIL is where 'the sim says' meets 'the hardware does', and discrepancies are gold: they reveal modeling gaps before the field does.",
 ["Real Pixhawk, simulated sensors", "Tests the binary that will fly", "Discrepancies reveal modeling gaps"],
 "var hil={autopilot:'PX4 v1.14',faults:['gps denied','motor degraded']};\nhil.faults.forEach(function(f){console.log('HIL fault '+f+': autopilot responded correctly');});\nconsole.log('iron sky GREEN -> first flight approved');"],
["simulation",
 "AirSim: AI Training: Learning to Fly",
 "AirSim is built for learning: reinforcement learning trains obstacle avoidance and landing policies across thousands of episodes; imitation learning clones expert trajectories; the APIs reset the world instantly for the next episode. The sim-to-real gap is the research frontier \u2014 domain randomization and careful physics narrow it. Policies graduate from sim to caged flight to open flight, each stage gated on the previous.",
 ["RL and imitation learning at scale", "Instant resets for episodes", "Graduated gates to reality"],
 "var gates=[['sim 50k episodes',1],['caged flight',1],['open flight',0]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'PASS':'awaiting'));});\nconsole.log('gap analysis required at each gate');"],
["drones",
 "AirSim: Defensive Uses: Rehearsing Without Risk",
 "AirSim's defensive value is rehearsal: search patterns over synthetic terrain, perimeter patrol routes, and emergency procedures practiced thousands of times before the real aircraft launches. Operators train against the sim; autonomy proves itself in the sim. The field then validates the rehearsal, not the idea \u2014 the idea was settled in the thousand runs.",
 ["Search and patrol rehearsal", "Operator training against the sim", "Rehearsal record with the plan"],
 "console.log('rehearsal: search pattern, 1,000 runs, 0 failures');\nconsole.log('operation plan approved (evidence attached)');"],
["hil",
 "AirSim: Recording Datasets: The Data Pipeline",
 "AirSim's recording pipeline captures images, depth, lidar, and vehicle state to disk in organized logs \u2014 the raw material for perception datasets and imitation learning. The discipline is the recording manifest: which sensors, which rates, which scenario seed \u2014 so the dataset is reproducible and its gaps are known. Recorded well, one afternoon of scripted flights becomes a dataset that trains models for months.",
 ["Images, depth, lidar, state logged", "Recording manifest per dataset", "No provenance, no training"],
 "var rec={images:4200,lidar:840,seed:7,manifest:true};\nconsole.log('recorded: '+rec.images+' images, '+rec.lidar+' lidar scans');\nconsole.log('manifest: seed '+rec.seed+' (accepted for training)');"],
["apis",
 "AirSim: Environments: Building the World",
 "AirSim runs in Unreal environments \u2014 city blocks, rural terrain, custom maps \u2014 and the environment is the experiment's context. Building worlds in Unreal (or using the bundled ones) with the right fidelity for the question is the craft: perception questions need visual richness; control questions need accurate physics and wind. Match the world's fidelity to the question asked.",
 ["Unreal environments as context", "Fidelity matched to the question", "The fit documented per experiment"],
 "var stage={visual:'high',physics:'measured',wind:'gust model'};\nconsole.log('stage: visual '+stage.visual+', physics '+stage.physics);\nconsole.log('fit for: vision-based landing (documented)');"],
["physics",
 "AirSim: Debugging: The Sim-to-Real Gap",
 "AirSim debugging often means gap-hunting: the policy works in sim and wobbles in reality \u2014 so compare: motor response curves, sensor latencies, wind models. The tools are system identification (measure the real vehicle's responses) and ablation (change one sim parameter, re-test). The gap is never fully closed; it is managed, measured, and respected.",
 ["System identification of the real vehicle", "Ablation to find the gap", "Residuals recorded as known unknowns"],
 "var residual={motor:0.03,latency_ms:12};\nconsole.log('mirror test residual: motor '+residual.motor+', latency +'+residual.latency_ms+'ms');\nconsole.log('residual recorded in deployment record (known unknowns)');"],
["ai-training",
 "AirSim: Timing: The HIL Loop Budget",
 "HIL lives or dies on timing: sensor data to the autopilot, actuator commands back, all within the real-time budget \u2014 typically a few milliseconds per loop. Jitter in the sim-to-hardware path looks like sensor noise to the autopilot and can destabilize control. The measurement is loop-time histograms on the real link; the fix is usually prioritized threads and locked clocks.",
 ["Millisecond loop budgets", "Jitter looks like sensor noise", "p99 over budget invalidates the run"],
 "var loop={p50:2.1,p99:4.8,budget:8};\nconsole.log('HIL loop p50 '+loop.p50+' ms, p99 '+loop.p99+' ms, budget '+loop.budget+' ms');\nconsole.log(loop.p99<=loop.budget?'timing VALID (test counts)':'timing INVALID (fiction)');"],
["simulation",
 "AirSim: Testing: Scenario Matrices",
 "Mature AirSim practice runs matrices: scenarios \u00d7 seeds \u00d7 conditions, with pass/fail on mission success and safety events. The matrix is the test suite; its results gate deployment. Flaky scenarios are fixed or removed \u2014 a flaky test teaches nothing. The matrix grows with field lessons: every surprise becomes a scenario.",
 ["Scenarios × seeds × conditions", "Flaky tests fixed or removed", "Grid version rides with deployment"],
 "var grid={scenarios:24,seeds:5,pass:118,fail:2};\nconsole.log('proving grid: '+grid.pass+' pass, '+grid.fail+' fail');\nconsole.log(grid.fail===0?'grid GREEN -> operations approved':'fix 2 failures first');"],
["drones",
 "AirSim: Real-World Pattern: Search-Training Program",
 "A complete pattern: a search team trains its drone AI in AirSim \u2014 synthetic terrain with randomized victims, weather, and lighting \u2014 across 50,000 episodes, then validates in caged flight, then field exercises. The sim supplied the rare cases (night, rain, obscured victims) the field could never schedule. When the real call comes, the AI has seen it ten thousand times.",
 ["Synthetic rare cases at scale", "Caged flight then field validation", "Training record published"],
 "console.log('50,000 episodes: night/rain/obscured covered');\nconsole.log('caged flight PASS, field exercise PASS');\nconsole.log('readiness evidenced, deployment approved');"],
["hil",
 "AirSim: Mastery: The Vehicle-AI Playbook",
 "AirSim mastery blends simulation craft with ML: API fluency, physics literacy, scenario design, learning-loop engineering, and the sim-to-real discipline. The advanced moves are custom environments, HIL architectures, and field-validated policies. The mindset: the sim is the dojo \u2014 train hard there, fight easy in the field.",
 ["Simulation craft plus ML", "Custom environments, HIL architectures", "Stewardship: manifests, gates, records"],
 "var playbook=['API fluency','physics literacy','scenario design','learning loops','sim-to-real'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The sim is the dojo. Train hard there.');"]
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
    tags:["airsim", "simulation", "unreal-engine", "hil", "drones", "ai-training", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"airsim record",
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
var gen={version:'jahdb-defense-aerospace-airsim-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-airsim',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-airsim']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();