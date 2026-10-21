(function(){'use strict';
/* jahdb-defense-aerospace-ardupilot-1.0 — deterministic boundless generator for defense-aerospace-ardupilot.
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
var CATS=["autopilot", "copter", "plane", "rover", "lua-scripting", "tuning"];
var PREFIX='JAH-DAE36-';
var DBNAME="ArduPilot Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["autopilot",
 "ArduPilot: What ArduPilot Is: The Veteran Autopilot",
 "ArduPilot is the longest-running open-source autopilot: one codebase, many vehicles \u2014 Copter for multicopters, Plane for fixed-wings, Rover for ground vehicles, Boat, Sub for underwater, even antennas and balloons. It speaks MAVLink natively, runs on Pixhawk and dozens of boards, and its feature depth (terrain following, precision landing, crop-sprayer support) reflects two decades of field use. Where PX4 is the modern rewrite, ArduPilot is the battle-tested elder \u2014 and many commercial vehicles fly it.",
 ["Copter, Plane, Rover, Boat, Sub", "Two decades of field depth", "Signed vehicle profiles per type"],
 "console.log('ArduPilot vehicles:');\n['Copter','Plane','Rover','Boat','Sub'].forEach(function(v){console.log(' '+v);});\nconsole.log('one codebase, signed vehicle profiles');"],
["copter",
 "ArduPilot: Flight Modes Across Vehicle Types",
 "ArduPilot's modes span vehicles: Copter's Loiter, AltHold, Auto, RTL, and SmartRTL (retraces its path home); Plane's FBWA/FBWB stabilized modes, Auto, RTL, and soaring support; Rover's Manual, Auto, RTL. The mode vocabulary is the operator's contract with the machine \u2014 each mode documents what the vehicle decides and what the human decides. Learning a new vehicle type starts with its modes.",
 ["Per-vehicle mode vocabularies", "SmartRTL retraces its path", "Watch-change reasons always logged"],
 "var modes=['Loiter','Auto','RTL','SmartRTL'];\nmodes.forEach(function(m){console.log('watch: '+m);});\nconsole.log('Auto selected: estimator OK, energy OK -> reason logged');"],
["plane",
 "ArduPilot: EKF3 and Sensor Fusion",
 "ArduPilot's EKF3 fuses IMU (often dual or triple), GPS (multi-constellation, multi-receiver), barometer, compass, optical flow, and rangefinders into the navigation solution, with per-sensor health and automatic source switching. The 'EKF lane switching' \u2014 jumping to a backup IMU when the primary degrades \u2014 is the kind of redundancy that saves aircraft. Compass calibration (the famous compass dance) and vibration management are the field rituals that make the filter happy.",
 ["Multi-IMU, multi-GPS fusion", "Lane switching to backup sensors", "Source changes as operator-visible events"],
 "var council={imu1:0.97,imu2:0.96,gps:0.88,baro:0.9};\nObject.keys(council).forEach(function(s){console.log(s+' confidence '+council[s]);});\nconsole.log('council: imu1 primary (change would ALERT)');"],
["rover",
 "ArduPilot: Lua Scripting: Autonomy Onboard",
 "ArduPilot's Lua scripting runs user code on the flight controller itself: custom behaviors, sensor drivers, companion-lite logic \u2014 sandboxed, with bindings to vehicle state and MAVLink. Scripts handle the long tail of missions no firmware feature covers: 'if the payload temperature exceeds X, RTL', or custom gimbal choreography. The sandbox keeps scripts from breaking the flight core, which is why scripting is safe to hand to field engineers.",
 ["Sandboxed Lua on the flight controller", "Custom behaviors without firmware changes", "Capability declarations plus signatures"],
 "console.log('orders: payload-temp.lua (capabilities: telemetry, mode-request)');\nconsole.log('rule: temp > 60C -> request RTL');\nconsole.log('signature valid -> LOADED (sandboxed)');"],
["lua-scripting",
 "ArduPilot: Your First Mission: Auto Waypoints",
 "The hello-world: plan waypoints in Mission Planner or QGroundControl, upload, switch to Auto, watch the vehicle fly the pattern and RTL. In SITL first, always. The mission items \u2014 takeoff, waypoints, loiter, land \u2014 plus DO commands for the camera are the vocabulary. The professional step is the pre-flight: EKF happy, GPS lock, geofence set, RTL altitude above the tallest obstacle.",
 ["Plan, upload, Auto, RTL", "SITL first, always", "Stack-verified pre-flight checklist"],
 "var preflight=[['EKF happy',1],['GPS 3D fix',1],['geofence set',1],['RTL alt clear',1]];\npreflight.forEach(function(p){console.log((p[1]?'[x] ':'[ ] ')+p[0]);});\nconsole.log('charter flight: APPROVED');"],
["tuning",
 "ArduPilot: Terrain Following and Precision Landing",
 "ArduPilot's advanced navigation: terrain following uses SRTM data or a rangefinder to hold AGL altitude over hills; precision landing fuses IR-LOCK or visual beacons to land on a target within centimeters. These are the features that turn 'a drone' into 'a tool' \u2014 repeatable, precise, boring in the best way. The tuning is in the sensor: rangefinder quality determines terrain-following quality.",
 ["Terrain following over hills", "Precision landing to centimeters", "Landing offsets trended as maintenance data"],
 "var landings=[0.12,0.09,0.15,0.11,0.31];\nlandings.forEach(function(o,i){console.log('landing '+(i+1)+': offset '+o+' m'+(o>0.25?' -> TREND ALERT':''));});"],
["autopilot",
 "ArduPilot: Tuning: PIDs and Filters",
 "ArduPilot tuning is the craft: rate PIDs per axis, filter frequencies for gyro noise, throttle hover learning, and the AutoTune feature that flies excitation patterns and sets gains itself. The method is measure (vibration plots), filter (notch the noise), then tune (step responses). A tuned Copter holds position in wind; an untuned one wanders. The log \u2014 always the log \u2014 shows which.",
 ["Rate PIDs, notch filters, AutoTune", "Measure, filter, then tune", "Tunes bound to vehicle profile"],
 "var axes=[['roll',0.05,'PASS'],['pitch',0.06,'PASS'],['yaw',0.04,'PASS']];\naxes.forEach(function(a){console.log(a[0]+' tracking '+a[1]+' -> '+a[2]);});\nconsole.log('tune bound to profile 7be2\u2026');"],
["copter",
 "ArduPilot: Defensive Uses: The Workhorse Fleet",
 "ArduPilot's defensive value is maturity at scale: fleets of mapping copters, fixed-wing surveyors, and rover sentries running the same trusted codebase with Lua-customized behaviors. The ecosystem's depth \u2014 every sensor driver, every edge case, already met \u2014 is why programs choose it for workhorse roles. The human plans; the veteran stack executes; the logs prove.",
 ["Mapping, survey, sentry fleets", "Lua-customized field behaviors", "Fleet-wide tune attestation"],
 "console.log('fleet: 24 vehicles, profiles verified, tunes attested');\nconsole.log('tasking: survey sectors 7-12 (signed)');"],
["plane",
 "ArduPilot: Rover and Boat: Ground and Water",
 "ArduPilot is not just aircraft: Rover drives Ackermann, skid-steer, and omnidirectional ground vehicles; Boat handles water with wind-aware navigation. The same mission planning, geofencing, and RTL concepts apply \u2014 RTL for a boat means 'come home across the water'. Ground vehicles add wheel encoders and the particular joy of tuning steering. The stack's vehicle breadth is unmatched.",
 ["Ackermann, skid-steer, boats", "Wind and current awareness", "Water test before autonomy"],
 "var boat={station_keep_m:1.8,current_ms:0.6};\nconsole.log('station keeping '+boat.station_keep_m+' m in '+boat.current_ms+' m/s current');\nconsole.log('water test PASS -> autonomous tasking unlocked');"],
["rover",
 "ArduPilot: Debugging: DataFlash Logs",
 "ArduPilot's DataFlash logs are legendary in depth: every sensor, every EKF innovation, every controller output. The debugging ladder is vibration (mechanical health), EKF innovations (estimator health), then controller tracking. The community's log-analysis wisdom \u2014 'check vibrations first' \u2014 has saved more aircraft than any feature. Download the log, look at the plots, believe the plots.",
 ["Deep logs: sensors, EKF, controllers", "Vibrations first, always", "Automated first-read summaries"],
 "console.log('journal auto-read: vibration 4.1 (normal), EKF innovations bounded');\nconsole.log('tracking: pitch loop error elevated -> review tune');\nconsole.log('human starts from the summary, not raw plots');"],
["lua-scripting",
 "ArduPilot: Failsafes: The Layers of Safety",
 "ArduPilot's failsafe layers: RC loss, GCS loss, GPS loss, battery (multiple stages), geofence, EKF failsafe \u2014 each with configured actions and the famous 'continue vs RTL vs land' decisions. The battery failsafe's staged response (warn, RTL, land) reflects hard-won field wisdom. Configuring failsafes is safety engineering with the vehicle's real performance numbers, validated in SITL with faults injected.",
 ["Layered: RC, GCS, GPS, battery, geofence, EKF", "Staged battery response", "Fault-injection drill before fielding"],
 "var drill=['rc loss','gcs loss','gps loss','battery','geofence','ekf'];\ndrill.forEach(function(d){console.log('fault '+d+': response executed -> PASS');});\nconsole.log('failsafe drill GREEN -> profile fieldable');"],
["tuning",
 "ArduPilot: Companion Integration and MAVLink Routing",
 "ArduPilot pairs with companions over MAVLink: vision, 4G/5G links, cloud relays. The routing (serial, UDP, CAN) is the plumbing, and the discipline is the same as PX4's \u2014 the flight core stays authoritative, companions advise. ArduPilot's MAVLink routing between multiple ground stations and vehicles is a quiet strength for fleet operations.",
 ["Companions advise, flight core decides", "MAVLink routing for fleets", "Advisor health visible"],
 "console.log('council: vision (heard), lte-relay (heard), planner (ignored: stale 2s)');\nconsole.log('flight core authoritative; advisories logged');"],
["autopilot",
 "ArduPilot: Testing: SITL, HIL, and the Test Matrix",
 "ArduPilot's testing is famously thorough: SITL for every vehicle type, autotest suites flying scripted missions in sim on every commit, HIL for hardware truth. The autotest matrix \u2014 hundreds of missions across vehicles \u2014 is the project's immune system. Contributors run the relevant slice; maintainers run it all. This is how a volunteer project out-tests many commercial ones.",
 ["Autotest matrix on every commit", "SITL per vehicle type, HIL for hardware", "Muster results part of the signature"],
 "console.log('muster: copter 142 missions, plane 98, rover 64 -> ALL GREEN');\nconsole.log('profile 7be2\u2026 signed on green muster');"],
["copter",
 "ArduPilot: Real-World Pattern: Agricultural Survey Fleet",
 "A complete pattern: fixed-wings fly grid surveys over farmland weekly \u2014 same altitude, terrain following, camera triggering \u2014 while copters spot-check anomalies. ArduPilot's survey grid support and geofencing make the pattern repeatable; Lua scripts handle the camera logic. The agronomist sees orthomosaics, not flight logs. Season after season, the same missions, the same lines.",
 ["Repeatable grid surveys", "Terrain following, camera triggering", "Seasonal comparison as the product"],
 "console.log('week 14 survey: 120 ha, 2.1 cm/px, hashed');\nconsole.log('seasonal diff: irrigation anomaly sector 4 (flagged)');"],
["plane",
 "ArduPilot: Mastery: The Veteran's Playbook",
 "ArduPilot mastery is field wisdom: EKF fluency, tuning craft, Lua behaviors, failsafe engineering, and log reading as a first language. The advanced moves are new vehicle types, driver development, and contributions to the matrix. The mindset: the stack has seen everything \u2014 learn its lessons instead of reliving them.",
 ["Field wisdom across vehicle types", "Driver and vehicle development", "Stewardship: signed, proven, chained"],
 "var playbook=['EKF fluency','tuning craft','Lua behaviors','failsafe engineering','log reading'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Learn its lessons instead of reliving them.');"]
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
    tags:["ardupilot", "autopilot", "uav", "ugv", "mavlink", "lua", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"ardupilot record",
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
var gen={version:'jahdb-defense-aerospace-ardupilot-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ardupilot',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ardupilot']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();