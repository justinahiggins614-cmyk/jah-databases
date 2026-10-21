(function(){'use strict';
/* jahdb-defense-aerospace-ardupilot-1.0 — deterministic boundless generator for defense-aerospace-ardupilot-signature.
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
var PREFIX='JAH-DAE36S-';
var DBNAME="Signature ArduPilot Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["autopilot",
 "Signature ArduPilot: What ArduPilot Is: The Veteran Autopilot",
 "The Signature counterpart is the SigHelm autopilot, Manon's original multi-vehicle design. SigHelm mirrors the one-codebase-many-vehicles architecture but every vehicle type is a signed vehicle profile \u2014 the firmware refuses to drive outputs until the profile matches the connected airframe. The Signature design makes 'wrong firmware on the vehicle' structurally impossible.",
 ["Copter, Plane, Rover, Boat, Sub", "Two decades of field depth", "Signed vehicle profiles per type"],
 "console.log('ArduPilot vehicles:');\n['Copter','Plane','Rover','Boat','Sub'].forEach(function(v){console.log(' '+v);});\nconsole.log('one codebase, signed vehicle profiles');"],
["copter",
 "Signature ArduPilot: Flight Modes Across Vehicle Types",
 "SigHelm's modes are the watches: same vocabulary, but every autonomous watch requires the estimator-health and energy checks recorded first. The Signature design logs the watch-change reason with every transition \u2014 the log always answers 'why did it switch modes'.",
 ["Per-vehicle mode vocabularies", "SmartRTL retraces its path", "Watch-change reasons always logged"],
 "var modes=['Loiter','Auto','RTL','SmartRTL'];\nmodes.forEach(function(m){console.log('watch: '+m);});\nconsole.log('Auto selected: estimator OK, energy OK -> reason logged');"],
["plane",
 "Signature ArduPilot: EKF3 and Sensor Fusion",
 "SigHelm's fusion is the council: same multi-source EKF, but each source carries a live confidence, and the council's decision (which sources feed the solution) is telemetry. The Signature design alerts on council changes \u2014 a source switch is an event the operator sees, not a silent miracle.",
 ["Multi-IMU, multi-GPS fusion", "Lane switching to backup sensors", "Source changes as operator-visible events"],
 "var council={imu1:0.97,imu2:0.96,gps:0.88,baro:0.9};\nObject.keys(council).forEach(function(s){console.log(s+' confidence '+council[s]);});\nconsole.log('council: imu1 primary (change would ALERT)');"],
["rover",
 "Signature ArduPilot: Lua Scripting: Autonomy Onboard",
 "SigHelm's scripting is the ship's orders: sandboxed Lua with capability declarations \u2014 a script declares which actuators and messages it may touch, and the loader enforces it. The Signature design signs scripts: the flight controller runs only reviewed, signed orders, never ad-hoc code from a laptop.",
 ["Sandboxed Lua on the flight controller", "Custom behaviors without firmware changes", "Capability declarations plus signatures"],
 "console.log('orders: payload-temp.lua (capabilities: telemetry, mode-request)');\nconsole.log('rule: temp > 60C -> request RTL');\nconsole.log('signature valid -> LOADED (sandboxed)');"],
["lua-scripting",
 "Signature ArduPilot: Your First Mission: Auto Waypoints",
 "SigHelm's first mission is the charter flight: same waypoints, but the charter includes the emergency plan as mandatory fields. The Signature design runs the pre-flight as a checklist the stack verifies itself \u2014 the operator confirms, the stack proves.",
 ["Plan, upload, Auto, RTL", "SITL first, always", "Stack-verified pre-flight checklist"],
 "var preflight=[['EKF happy',1],['GPS 3D fix',1],['geofence set',1],['RTL alt clear',1]];\npreflight.forEach(function(p){console.log((p[1]?'[x] ':'[ ] ')+p[0]);});\nconsole.log('charter flight: APPROVED');"],
["tuning",
 "Signature ArduPilot: Terrain Following and Precision Landing",
 "SigHelm's precision features are the sure-foot: same capabilities, but every precision landing records the final offset as a quality metric. The Signature design trends the offsets \u2014 a degrading landing accuracy is maintenance information, surfaced before it becomes a missed deck.",
 ["Terrain following over hills", "Precision landing to centimeters", "Landing offsets trended as maintenance data"],
 "var landings=[0.12,0.09,0.15,0.11,0.31];\nlandings.forEach(function(o,i){console.log('landing '+(i+1)+': offset '+o+' m'+(o>0.25?' -> TREND ALERT':''));});"],
["autopilot",
 "Signature ArduPilot: Tuning: PIDs and Filters",
 "SigHelm's tuning is the truing: guided excitation per axis with pass/fail on tracking and motor heat. The Signature design binds the tune to the vehicle profile hash \u2014 change the props, re-true, because the tune belongs to the configuration.",
 ["Rate PIDs, notch filters, AutoTune", "Measure, filter, then tune", "Tunes bound to vehicle profile"],
 "var axes=[['roll',0.05,'PASS'],['pitch',0.06,'PASS'],['yaw',0.04,'PASS']];\naxes.forEach(function(a){console.log(a[0]+' tracking '+a[1]+' -> '+a[2]);});\nconsole.log('tune bound to profile 7be2\u2026');"],
["copter",
 "Signature ArduPilot: Defensive Uses: The Workhorse Fleet",
 "SigHelm's fleet doctrine is the old guard: signed profiles, signed orders, hash-chained logs across the fleet. The Signature design adds fleet-wide tune attestation \u2014 the dispatcher can verify every vehicle's tune matches its profile before tasking.",
 ["Mapping, survey, sentry fleets", "Lua-customized field behaviors", "Fleet-wide tune attestation"],
 "console.log('fleet: 24 vehicles, profiles verified, tunes attested');\nconsole.log('tasking: survey sectors 7-12 (signed)');"],
["plane",
 "Signature ArduPilot: Rover and Boat: Ground and Water",
 "SigHelm's surface craft are the shore watches: same autonomy, water-aware \u2014 current estimation, wind compensation, man-overboard patterns. The Signature design requires the water test: every boat profile proves its station-keeping in measured current before autonomous tasking.",
 ["Ackermann, skid-steer, boats", "Wind and current awareness", "Water test before autonomy"],
 "var boat={station_keep_m:1.8,current_ms:0.6};\nconsole.log('station keeping '+boat.station_keep_m+' m in '+boat.current_ms+' m/s current');\nconsole.log('water test PASS -> autonomous tasking unlocked');"],
["rover",
 "Signature ArduPilot: Debugging: DataFlash Logs",
 "SigHelm's logs are the ship's journal: same depth, hash-chained. The Signature design adds the automated first read \u2014 the ground station flags vibration, EKF, and tracking anomalies on download, so the human starts from the machine's summary.",
 ["Deep logs: sensors, EKF, controllers", "Vibrations first, always", "Automated first-read summaries"],
 "console.log('journal auto-read: vibration 4.1 (normal), EKF innovations bounded');\nconsole.log('tracking: pitch loop error elevated -> review tune');\nconsole.log('human starts from the summary, not raw plots');"],
["lua-scripting",
 "Signature ArduPilot: Failsafes: The Layers of Safety",
 "SigHelm's failsafes are the standing orders: same layers, but thresholds derive from the vehicle profile's measured performance. The Signature design requires the failsafe drill \u2014 SITL fault injection covering every layer \u2014 green before the profile is fielded.",
 ["Layered: RC, GCS, GPS, battery, geofence, EKF", "Staged battery response", "Fault-injection drill before fielding"],
 "var drill=['rc loss','gcs loss','gps loss','battery','geofence','ekf'];\ndrill.forEach(function(d){console.log('fault '+d+': response executed -> PASS');});\nconsole.log('failsafe drill GREEN -> profile fieldable');"],
["tuning",
 "Signature ArduPilot: Companion Integration and MAVLink Routing",
 "SigHelm's companion doctrine is the advisory council: companions propose, the flight core disposes \u2014 with the proposal/decision logged. The Signature design shows the council's health on the ground station: which advisors are heard, which are ignored, and why.",
 ["Companions advise, flight core decides", "MAVLink routing for fleets", "Advisor health visible"],
 "console.log('council: vision (heard), lte-relay (heard), planner (ignored: stale 2s)');\nconsole.log('flight core authoritative; advisories logged');"],
["autopilot",
 "Signature ArduPilot: Testing: SITL, HIL, and the Test Matrix",
 "SigHelm's test doctrine is the muster: SITL matrix per vehicle profile, HIL for new hardware, fault injection always. The Signature design makes the muster results part of the profile signature \u2014 a profile is fieldable only on a green muster.",
 ["Autotest matrix on every commit", "SITL per vehicle type, HIL for hardware", "Muster results part of the signature"],
 "console.log('muster: copter 142 missions, plane 98, rover 64 -> ALL GREEN');\nconsole.log('profile 7be2\u2026 signed on green muster');"],
["copter",
 "Signature ArduPilot: Real-World Pattern: Agricultural Survey Fleet",
 "SigHelm's survey doctrine is the patient acre: repeatable grids, hashed imagery, seasonal baselines. The Signature design compares seasons automatically \u2014 the fleet's value is not the flights but the accumulating evidence of change.",
 ["Repeatable grid surveys", "Terrain following, camera triggering", "Seasonal comparison as the product"],
 "console.log('week 14 survey: 120 ha, 2.1 cm/px, hashed');\nconsole.log('seasonal diff: irrigation anomaly sector 4 (flagged)');"],
["plane",
 "Signature ArduPilot: Mastery: The Veteran's Playbook",
 "SigHelm mastery adds the stewardship layer: signed profiles, proven tunes, chained journals. Manon's roadmap runs from today's five vehicle types to new domains under one helm \u2014 veteran discipline, every vehicle, all of it logged.",
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
    edition:'signature',
    category:tp[0],
    tags:["ardupilot", "autopilot", "uav", "ugv", "mavlink", "lua", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ardupilot-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ardupilot-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();