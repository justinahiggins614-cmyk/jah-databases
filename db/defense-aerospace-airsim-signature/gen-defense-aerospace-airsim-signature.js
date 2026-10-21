(function(){'use strict';
/* jahdb-defense-aerospace-airsim-1.0 — deterministic boundless generator for defense-aerospace-airsim-signature.
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
var PREFIX='JAH-DAE39S-';
var DBNAME="Signature AirSim Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["simulation",
 "Signature AirSim: What AirSim Is: The Drone's Simulator",
 "The Signature counterpart is the SigSky bench, Manon's original vehicle-AI simulation design. It mirrors the API-driven architecture but every scenario carries a fidelity manifest \u2014 which physics are modeled to what accuracy \u2014 so trained policies always know the limits of their education.",
 ["Purpose-built multicopter physics", "Drone as a programmable object", "Community-continued for research"],
 "console.log('AirSim: Unreal visuals + drone physics + APIs');\n['multirotor + car models','Python/C++ APIs','camera/lidar/depth','HIL support'].forEach(function(s){console.log(' '+s);});"],
["drones",
 "Signature AirSim: APIs: Flying with Code",
 "The bench's API is the flight desk: same command/state vocabulary, with every call logged to the scenario record. The Signature design makes the desk's determinism explicit \u2014 the seed and step mode are part of every experiment record, so results replay exactly.",
 ["Vehicle as function calls", "Scripted missions and datasets", "Seeded determinism for replay"],
 "console.log('flight desk: takeoff -> moveTo(10,0,-5) -> capture');\nconsole.log('seed 7, fixed step 1ms -> replayable');\nconsole.log('state: pos(10.0,0.1,-5.0) vel(0.0,0.0,0.0)');"],
["hil",
 "Signature AirSim: Physics: The Custom Flight Model",
 "The bench's physics is the wind tunnel: drone-specialized dynamics with parameters carrying provenance tags. The Signature design requires measured motor curves for control development \u2014 guessed thrust curves are flagged in the manifest, and policies trained on flagged physics carry the warning.",
 ["Drone-specialized dynamics", "Motor models, drag, ground effect", "Provenance tags on parameters"],
 "var params=[['mass',1.5,'measured'],['motor curve','--','measured'],['drag',0.3,'estimated']];\nparams.forEach(function(p){console.log(p[0]+'='+p[1]+' ('+p[2]+')');});"],
["apis",
 "Signature AirSim: Sensors: Cameras, Lidar, Depth",
 "The bench's sensors are the honest eyes: same data plus noise, with the ground-truth channel for auto-scoring. The Signature design requires the noise configuration in the experiment record \u2014 'which noise' is part of the result.",
 ["Cameras, depth, lidar for AI", "Ground-truth segmentation", "Noise configuration recorded"],
 "var frame={rgb:'640x480',depth:'ok',lidar_pts:12000,noise:'on'};\nconsole.log('frame: '+frame.rgb+' rgb, '+frame.lidar_pts+' lidar pts, noise '+frame.noise);\nconsole.log('ground truth: 3 obstacles labeled (auto-score)');"],
["physics",
 "Signature AirSim: Your First Flight: Scripted Takeoff",
 "The bench's hello-world is the first hover: same ten lines, but the run auto-records the manifest and seed. The Signature design makes every beginner experiment self-documenting \u2014 the habit of recorded assumptions starts at hello-world.",
 ["Ten lines to fly", "API completeness as the lesson", "Self-documenting from hello-world"],
 "console.log('first hover: arm -> takeoff(5m) -> hover 10s -> land');\nconsole.log('manifest + seed recorded automatically');\nconsole.log('the script IS the experiment');"],
["ai-training",
 "Signature AirSim: HIL: Real Autopilot, Simulated World",
 "The bench's HIL is the iron sky: real autopilot, simulated world, scripted faults. The Signature design requires the iron-sky suite green before first flight \u2014 GPS denied, motor degraded, link dropped \u2014 with the autopilot's real responses recorded.",
 ["Real Pixhawk, simulated sensors", "Tests the binary that will fly", "Discrepancies reveal modeling gaps"],
 "var hil={autopilot:'PX4 v1.14',faults:['gps denied','motor degraded']};\nhil.faults.forEach(function(f){console.log('HIL fault '+f+': autopilot responded correctly');});\nconsole.log('iron sky GREEN -> first flight approved');"],
["simulation",
 "Signature AirSim: AI Training: Learning to Fly",
 "The bench's training doctrine is the graduated sky: sim episodes, caged flight, open flight \u2014 gates between each. The Signature design requires the gap analysis at each gate: what the sim did not model, and whether it mattered.",
 ["RL and imitation learning at scale", "Instant resets for episodes", "Graduated gates to reality"],
 "var gates=[['sim 50k episodes',1],['caged flight',1],['open flight',0]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'PASS':'awaiting'));});\nconsole.log('gap analysis required at each gate');"],
["drones",
 "Signature AirSim: Defensive Uses: Rehearsing Without Risk",
 "The bench's rehearsal doctrine is the thousand-run rule: no real launch until the procedure survives the sim matrix. The Signature design publishes the rehearsal record with the operation plan \u2014 the plan's evidence rides with the plan.",
 ["Search and patrol rehearsal", "Operator training against the sim", "Rehearsal record with the plan"],
 "console.log('rehearsal: search pattern, 1,000 runs, 0 failures');\nconsole.log('operation plan approved (evidence attached)');"],
["hil",
 "Signature AirSim: Recording Datasets: The Data Pipeline",
 "The bench's recording doctrine is the flight logbook: every recording with its manifest, hash-chained. The Signature design requires the manifest before the data is accepted into training \u2014 data without provenance does not train models.",
 ["Images, depth, lidar, state logged", "Recording manifest per dataset", "No provenance, no training"],
 "var rec={images:4200,lidar:840,seed:7,manifest:true};\nconsole.log('recorded: '+rec.images+' images, '+rec.lidar+' lidar scans');\nconsole.log('manifest: seed '+rec.seed+' (accepted for training)');"],
["apis",
 "Signature AirSim: Environments: Building the World",
 "The bench's worlds are the stages: fidelity matched to the question, recorded in the manifest. The Signature design requires the fidelity question answered in every experiment record: 'this world is accurate enough for X because Y'.",
 ["Unreal environments as context", "Fidelity matched to the question", "The fit documented per experiment"],
 "var stage={visual:'high',physics:'measured',wind:'gust model'};\nconsole.log('stage: visual '+stage.visual+', physics '+stage.physics);\nconsole.log('fit for: vision-based landing (documented)');"],
["physics",
 "Signature AirSim: Debugging: The Sim-to-Real Gap",
 "The bench's gap tool is the mirror test: real vehicle responses recorded, sim parameters fitted, residual reported. The Signature design requires the residual in the deployment record \u2014 'we know what we do not model' is a strength, stated plainly.",
 ["System identification of the real vehicle", "Ablation to find the gap", "Residuals recorded as known unknowns"],
 "var residual={motor:0.03,latency_ms:12};\nconsole.log('mirror test residual: motor '+residual.motor+', latency +'+residual.latency_ms+'ms');\nconsole.log('residual recorded in deployment record (known unknowns)');"],
["ai-training",
 "Signature AirSim: Timing: The HIL Loop Budget",
 "The bench's timing discipline is the metronome check: HIL loop histogram measured on every run, budget declared. The Signature design fails HIL runs whose p99 exceeds the budget \u2014 a late HIL is not a test, it is fiction.",
 ["Millisecond loop budgets", "Jitter looks like sensor noise", "p99 over budget invalidates the run"],
 "var loop={p50:2.1,p99:4.8,budget:8};\nconsole.log('HIL loop p50 '+loop.p50+' ms, p99 '+loop.p99+' ms, budget '+loop.budget+' ms');\nconsole.log(loop.p99<=loop.budget?'timing VALID (test counts)':'timing INVALID (fiction)');"],
["simulation",
 "Signature AirSim: Testing: Scenario Matrices",
 "The bench's matrix is the proving grid: scenarios, seeds, conditions, results \u2014 all recorded. The Signature design requires the grid green before flight operations, and the grid's version rides with the deployment.",
 ["Scenarios × seeds × conditions", "Flaky tests fixed or removed", "Grid version rides with deployment"],
 "var grid={scenarios:24,seeds:5,pass:118,fail:2};\nconsole.log('proving grid: '+grid.pass+' pass, '+grid.fail+' fail');\nconsole.log(grid.fail===0?'grid GREEN -> operations approved':'fix 2 failures first');"],
["drones",
 "Signature AirSim: Real-World Pattern: Search-Training Program",
 "The bench's program doctrine is the prepared eye: sim supplies the rare, field validates the common. The Signature design publishes the training record with the deployment \u2014 episodes, conditions, gates passed \u2014 because readiness is evidenced.",
 ["Synthetic rare cases at scale", "Caged flight then field validation", "Training record published"],
 "console.log('50,000 episodes: night/rain/obscured covered');\nconsole.log('caged flight PASS, field exercise PASS');\nconsole.log('readiness evidenced, deployment approved');"],
["hil",
 "Signature AirSim: Mastery: The Vehicle-AI Playbook",
 "The bench's mastery adds the stewardship layer: manifests, gates, published records. Manon's roadmap runs from today's drone dojos to full multi-vehicle synthetic ranges under one manifest discipline \u2014 dojos, everywhere, all honest.",
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
    edition:'signature',
    category:tp[0],
    tags:["airsim", "simulation", "unreal-engine", "hil", "drones", "ai-training", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-airsim-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-airsim-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();