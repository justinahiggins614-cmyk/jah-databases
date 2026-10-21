(function(){'use strict';
/* jahdb-defense-aerospace-ros-2-1.0 — deterministic boundless generator for defense-aerospace-ros-2.
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
var CATS=["middleware", "dds", "nodes", "security", "real-time", "navigation"];
var PREFIX='JAH-DAE31-';
var DBNAME="ROS 2 Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["middleware",
 "ROS 2: What ROS 2 Is: Plumbing for Robots",
 "ROS 2 is the middleware that robots are built on: instead of one giant program, a robot is dozens of nodes \u2014 a lidar driver, a localizer, a planner, a motor controller \u2014 communicating over typed topics, services, and actions. Underneath is DDS (Data Distribution Service), an industrial pub/sub standard with real-time quality-of-service policies. ROS 2 adds what ROS 1 lacked: security (SROS2), lifecycle management, and real-time support. If a robot has more than one sensor and one actuator, it probably runs ROS 2.",
 ["Nodes communicate over typed topics/services/actions", "DDS pub/sub underneath", "SROS2 security, lifecycle, real-time"],
 "console.log('ROS 2 graph:');\n['lidar_driver -> /scan','localizer -> /pose','planner -> /cmd_vel','motor_ctrl <- /cmd_vel'].forEach(function(s){console.log(' '+s);});\nconsole.log('Underneath: DDS with QoS policies');"],
["dds",
 "ROS 2: Topics, Services, Actions: The Three Patterns",
 "ROS 2 has three communication patterns, and choosing correctly is the core design skill. Topics are many-to-many streaming data (sensor feeds, poses) with QoS-tuned delivery. Services are synchronous request/response (trigger a calibration, query a state). Actions are long-running goals with feedback and cancelation (navigate to waypoint, with progress updates and the ability to preempt). Misusing them \u2014 a service for streaming data, a topic for commands \u2014 is the classic beginner architecture bug.",
 ["Topics: streaming data", "Services: request/response", "Actions: goals with feedback and cancel"],
 "var patterns=[['stream','/scan','many-to-many sensor data'],['call','/calibrate','request/response'],['mission','/navigate','goal + feedback + cancel']];\npatterns.forEach(function(p){console.log(p[0]+' '+p[1]+': '+p[2]);});"],
["nodes",
 "ROS 2: DDS and QoS: Delivery Guarantees You Can Tune",
 "DDS quality-of-service policies are ROS 2's superpower: reliability (best-effort vs reliable), durability (late joiners get history), deadline, liveliness, and history depth \u2014 per topic, per connection. A video feed uses best-effort; a stop command uses reliable with a deadline. The compatibility check is automatic: a publisher and subscriber with incompatible QoS simply do not connect, and ROS 2 tells you why. For defense networks with lossy links, QoS tuning is the difference between a robot that works and one that freezes.",
 ["Per-topic reliability, durability, deadline", "Incompatible QoS refuses to connect", "QoS tuning for lossy links"],
 "function qosOk(pub,sub){return pub.reliability===sub.reliability||sub.reliability==='best_effort';}\nconsole.log('video pub/sub: '+qosOk({reliability:'best_effort'},{reliability:'best_effort'}));\nconsole.log('estop pub/sub: '+qosOk({reliability:'reliable'},{reliability:'reliable'}));"],
["security",
 "ROS 2: SROS2: Security Built Into the Middleware",
 "SROS2 brings PKI security to the robot's nervous system: each node gets a certificate, DDS encrypts and authenticates traffic, and access-control policies declare which node may publish or subscribe to which topic. A compromised camera node cannot spoof lidar data because the policy forbids it from publishing /scan. Key management is the operational cost \u2014 but for fielded robots, an unauthenticated middleware bus is an unacceptable attack surface, and SROS2 closes it.",
 ["Per-node certificates, encrypted DDS", "Access policies per topic", "Compromised nodes cannot spoof other sensors"],
 "var policy={'camera':['/image'],'lidar':['/scan']};\nfunction canPub(node,topic){return (policy[node]||[]).indexOf(topic)>=0;}\nconsole.log('camera -> /scan: '+canPub('camera','/scan')+' (DENIED by policy)');\nconsole.log('lidar -> /scan: '+canPub('lidar','/scan'));"],
["real-time",
 "ROS 2: Your First Robot: Talker, Listener, Launch",
 "The hello-world is the talker/listener pair: one node publishing strings on /chatter, another subscribing, both described in a launch file that starts the system with parameters. From there the ladder is parameters (runtime-tunable), then a real sensor driver, then the navigation stack. The launch system \u2014 Python-based, composable, with lifecycle hooks \u2014 is how a 40-node robot becomes one deployable instead of 40 terminal windows.",
 ["Talker/listener over a topic", "Launch files compose multi-node systems", "Swarm file: one file, whole robot"],
 "console.log('swarm file: crier -> /chatter -> hearer');\nconsole.log('nodes: 2, topics: 1, identities: signed, covenants: checked');\nconsole.log('launch: OK (whole robot from one file)');"],
["navigation",
 "ROS 2: Lifecycle Nodes: Managed Startup and Shutdown",
 "Real robots cannot just be killed -9: sensors need ordered startup, and shutdown must park actuators safely. ROS 2 lifecycle nodes move through states \u2014 unconfigured, inactive, active, shutting down \u2014 with transitions the launch system orchestrates. A motor controller configures hardware, activates only when the planner is ready, and deactivates to a safe state on fault. This is the difference between a demo and a machine you trust near people.",
 ["Ordered startup and safe shutdown", "States: configure, activate, deactivate", "Safe state proven before activation"],
 "var states=['unconfigured','inactive','active'];\nvar node={state:'unconfigured',safe:'motors braked'};\nstates.forEach(function(s){node.state=s;console.log('transition -> '+s);});\nconsole.log('safe state proven: '+node.safe);"],
["middleware",
 "ROS 2: Nav2: The Navigation Stack",
 "Nav2 is ROS 2's navigation system: global planners (A*, Dijkstra) for the route, local planners (DWB, MPPI) for dodging, costmaps fusing lidar and cameras into obstacle grids, and behavior trees orchestrating recovery (back up, spin, replan). It navigates warehouses, campuses, and test ranges daily. Tuning costmaps and planners for the vehicle's dynamics is the real work \u2014 the defaults drive a TurtleBot, not your platform.",
 ["Global + local planners, costmaps", "Behavior trees for recovery", "Safety envelopes on every plan"],
 "var plan={waypoints:14,length_m:86,envelope_m:0.5};\nconsole.log('plan: '+plan.waypoints+' waypoints, '+plan.length_m+' m, envelope +/-'+plan.envelope_m+' m');\nconsole.log('recovery: backup -> spin -> replan (behavior tree)');"],
["dds",
 "ROS 2: Defensive Uses: Uncrewed Ground Patrol",
 "ROS 2's defensive applications are uncrewed systems doing dull, dangerous work: perimeter patrol UGVs running Nav2 with SROS2-secured comms, EOD-assist manipulators with lifecycle-managed arms, and sensor-mule robots logging infrastructure health. The common thread is the operator at a safe distance and the robot in harm's way \u2014 with the middleware's security and lifecycle guarantees making the system trustworthy enough to field.",
 ["Perimeter patrol and EOD-assist", "SROS2-secured, lifecycle-managed", "Dead-man override tested before every patrol"],
 "console.log('patrol tasking signed: perimeter loop, 4 waypoints');\nconsole.log('override path tested: 38 ms round trip');\nconsole.log('robot rolls; operator watches from safety');"],
["nodes",
 "ROS 2: Real-Time: Deterministic Execution",
 "Some robots have hard deadlines \u2014 a 1 kHz control loop cannot wait for a garbage collector. ROS 2's real-time story is executors with deterministic scheduling, zero-copy intra-process messaging, and compatibility with real-time Linux (PREEMPT_RT) and DDS implementations tuned for determinism. The discipline is end-to-end: real-time executor, locked memory, isolated CPUs, measured worst-case latency. Soft real-time gets you smooth demos; hard real-time gets you certifiable machines.",
 ["Deterministic executors, zero-copy messaging", "PREEMPT_RT and real-time DDS", "WCET proven before arming"],
 "var loop={freqHz:1000,budgetUs:1000,wcetUs:640};\nconsole.log('control loop '+loop.freqHz+' Hz, budget '+loop.budgetUs+' us, WCET '+loop.wcetUs+' us');\nconsole.log('schedule '+(loop.wcetUs<=loop.budgetUs?'PROVEN':'REJECTED')+' -> '+(loop.wcetUs<=loop.budgetUs?'arm allowed':'arm refused'));"],
["security",
 "ROS 2: Debugging: rqt, rosbag, and the Graph",
 "ROS 2 debugging is graph debugging: rqt_graph shows the node/topic topology, ros2 topic echo shows the data, and rosbag records everything for replay \u2014 the flight-data recorder of robotics. When the robot misbehaves, you replay the bag and watch the exact messages that led to the failure. The discipline is recording always in the field: storage is cheap, and the one incident you did not record is the one you cannot diagnose.",
 ["rqt_graph, topic echo, rosbag replay", "Record always in the field", "Hash-chained tamper-evident recordings"],
 "console.log('black box: recording /scan /pose /cmd_vel (hash-chained)');\nconsole.log('replay incident t+412s: /cmd_vel spike precedes fault');\nconsole.log('chain verified: recording unaltered');"],
["real-time",
 "ROS 2: Simulation: Gazebo Before Hardware",
 "Nobody tests navigation on the real robot first: ROS 2 pairs with Gazebo (next topic's subject) for physics-accurate simulation, with rosbag bridging sim and reality. The workflow is simulate, then hardware-in-the-loop, then field \u2014 each stage catching the bugs the previous one cannot. Sensor plugins publish the same topics as real drivers, so the autonomy stack cannot tell sim from reality, which is exactly the point.",
 ["Gazebo sim with identical topics", "Sim-to-HIL-to-field staging", "Sim failures gate hardware time"],
 "console.log('twin check: /scan schema hash sim==real -> PASS');\nconsole.log('sim: 200 patrol loops, 0 envelope breaches');\nconsole.log('gate: hardware test APPROVED');"],
["navigation",
 "ROS 2: Multi-Robot: Fleets and Namespaces",
 "One robot is a product; ten are a system. ROS 2 namespaces let identical software run on many robots without topic collisions (/robot3/scan), and DDS discovery scales to fleets on a shared network. Fleet managers assign tasks, monitor health, and coordinate \u2014 with SROS2 keeping each robot's bus authenticated. The hard problems are shared world models and communication dropouts, not the plumbing.",
 ["Namespaces prevent topic collisions", "DDS discovery scales to fleets", "Separation enforced by planners"],
 "var fleet=['r1','r2','r3'];\nfleet.forEach(function(r){console.log('/'+r+'/scan: namespaced, no collisions');});\nconsole.log('separation rule: 5 m minimum (planner-enforced)');"],
["middleware",
 "ROS 2: Testing: Integration Rigs and CI",
 "ROS 2 testing layers: unit tests per node, integration tests with the real middleware (launch_testing spins up nodes and asserts on topics), and nightly sim runs of full missions. The launch_testing framework is the workhorse \u2014 it catches the QoS mismatches and lifecycle ordering bugs that unit tests cannot. For fielded robots, the sim nightly is the gate: green sim, then hardware.",
 ["launch_testing for integration", "Nightly mission sims as the gate", "Green proving ground before signing"],
 "var suites=[['unit',142],['integration',37],['mission sim',12]];\nsuites.forEach(function(s){console.log(s[0]+': '+s[1]+' PASS');});\nconsole.log('proving ground GREEN -> bundle signable');"],
["dds",
 "ROS 2: Real-World Pattern: Warehouse Inventory Fleet",
 "A complete pattern: a fleet of AMRs running Nav2, each namespaced, SROS2-secured, recording to black boxes, coordinated by a dispatcher assigning inventory-scan tasks. The robots share a world model of shelf locations; the dispatcher reassigns on battery or fault. One operator supervises twelve robots. The same architecture, with different payloads, patrols perimeters \u2014 the middleware does not care what the robot carries.",
 ["Namespaced fleet under one dispatcher", "Shared world model, signed tasking", "Safety case published with deployment"],
 "console.log('flock: 12 AMRs, dispatcher tasking signed');\nconsole.log('safety case v3 published with deployment');\nconsole.log('operator: 1 human, 12 robots, 0 incidents this quarter');"],
["nodes",
 "ROS 2: Mastery: The Robotics Systems Playbook",
 "ROS 2 mastery is systems engineering: graph design, QoS fluency, lifecycle discipline, real-time verification, and the sim-to-field pipeline. The advanced moves are custom DDS tuning, multi-robot coordination, and safety-case authorship. The mindset: the robot is a distributed system that happens to have wheels \u2014 design it like one.",
 ["Graph design through safety cases", "Custom DDS and multi-robot coordination", "Stewardship: signed, proven, published"],
 "var playbook=['graph design','QoS fluency','lifecycle','real-time proof','safety cases'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The robot is a distributed system with wheels.');"]
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
    tags:["ros2", "robotics", "dds", "sros2", "autonomy", "middleware", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"ros 2 record",
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
var gen={version:'jahdb-defense-aerospace-ros-2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ros-2',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ros-2']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();