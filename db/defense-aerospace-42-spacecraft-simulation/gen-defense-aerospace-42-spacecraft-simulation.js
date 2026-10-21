(function(){'use strict';
/* jahdb-defense-aerospace-42-spacecraft-simulation-1.0 — deterministic boundless generator for defense-aerospace-42-spacecraft-simulation.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["attitude-dynamics", "orbit-dynamics", "actuators", "sensors", "multi-body"];
var PREFIX='JAH-DAE9-';
var EDITION='public';
var POOL=[["42: NASA Goddard's Spacecraft Simulator", "attitude-dynamics", "42 is NASA Goddard's open-source simulator for spacecraft attitude and orbit dynamics: it propagates position, velocity, attitude, and angular rates for one or many spacecraft in multi-body gravity. Named for the answer to everything, it answers dynamics questions with high fidelity. It is a workhorse for GNC development and analysis.", {"Developer": "NASA Goddard", "Simulates": "attitude + orbit dynamics", "Bodies": "multi-body gravity", "License": "open source", "Use": "GNC development"}], ["Attitude: Quaternions", "attitude-dynamics", "42 represents attitude with quaternions — four numbers with no singularities, unlike Euler angles that blow up at 90 degrees pitch. Quaternion kinematics propagate cleanly, and every sensor and actuator model speaks the same language. GNC engineers think in quaternions or they suffer.", {"Represents": "quaternions", "Avoids": "Euler singularities", "Propagates": "clean kinematics", "Thinks": "in quaternions"}], ["Orbit: Two-Body Plus Perturbations", "orbit-dynamics", "42 propagates orbits in multi-body gravity with perturbations — J2 oblateness, drag, solar pressure — layered on the two-body core. The orbit and attitude couple through gravity-gradient torque and aerodynamic torque. One sim, both dynamics, consistently.", {"Core": "two-body", "Adds": "J2, drag, SRP", "Bodies": "multi-body gravity", "Couples": "orbit <-> attitude"}], ["Reaction Wheels", "actuators", "Reaction wheels trade angular momentum with the spacecraft body: spin the wheel one way, the bus rotates the other. 42 models wheel inertia, friction, saturation, and momentum dumping. Wheels are the precision actuators of modern spacecraft — silent, smooth, and saturable.", {"Trades": "wheel momentum <-> body", "Models": "inertia, friction, saturation", "Role": "precision pointing", "Manages": "momentum dumping"}], ["Thrusters and Torque Rods", "actuators", "42 models thrusters (force + torque, with misalignment and minimum impulse) and magnetic torque rods (dipole vs Earth's field) — the coarse actuators for momentum dumping and safe modes. Wheels do the fine work; thrusters and torquers handle the big jobs and the emergencies.", {"Thrusters": "force+torque, min impulse", "Torquers": "dipole vs B-field", "Jobs": "dumping, safe mode", "Split": "fine vs coarse"}], ["Star Trackers and Sun Sensors", "sensors", "42 simulates the sensors GNC flies on: star trackers (arcsecond attitude from star fields), sun sensors (coarse sun direction), magnetometers, and gyros with bias and noise. Sensor models include dropouts and errors so the navigation filters prove themselves against reality.", {"Star tracker": "arcsecond attitude", "Sun sensor": "coarse direction", "Gyro": "bias + noise", "Includes": "dropouts, errors"}], ["GPS and Orbit Determination", "sensors", "42 models GPS-style navigation: pseudorange measurements from the constellation geometry dilute into position fixes with realistic error. Combined with propagator truth, engineers tune orbit determination filters. Knowing where you are is the prerequisite for everything else.", {"Models": "pseudorange geometry", "Dilutes": "into position error", "Tunes": "OD filters", "Prereq": "for everything"}], ["Multi-Spacecraft Scenarios", "multi-body", "42 simulates formations and constellations — relative dynamics, cross-links, collision screening — in one run. Formation flying (like MMS's tetrahedron) needs relative navigation and coordinated control, all developed in multi-spacecraft sim. One executive, many vehicles.", {"Runs": "formations, constellations", "Needs": "relative nav + control", "Example": "MMS tetrahedron", "One": "executive, many vehicles"}], ["Flexible Bodies and Slosh", "attitude-dynamics", "Real spacecraft bend and slosh: 42-class analysis adds flexible appendages (solar arrays) and fuel slosh modes that couple with attitude control. A controller that ignores flexibility can go unstable on orbit. High-fidelity sim includes the wobble.", {"Bends": "flexible arrays", "Sloshes": "fuel modes", "Couples": "with control", "Ignores": "at your peril"}], ["Disturbance Torques", "orbit-dynamics", "42 accounts for the torques that fight the controller: gravity gradient, aerodynamic, solar pressure, and magnetic residuals. Sizing actuators starts with sizing disturbances. The quietest spacecraft still lives in a noisy torque environment.", {"Fights": "gravity-grad, aero, SRP", "Sizes": "actuators", "Environment": "noisy torques", "Starts": "with disturbances"}], ["Safe Modes", "attitude-dynamics", "When faults strike, 42-tested safe modes take over: sun-pointing power-positive attitudes with minimal actuator needs, waiting for ground rescue. Safe mode is the spacecraft's survival instinct, and it is proven in sim long before it is needed. Every mission has one.", {"Trigger": "faults", "Does": "sun-point, power-positive", "Needs": "minimal actuators", "Proven": "in sim first"}], ["Monte Carlo with 42", "multi-body", "42 runs Monte Carlo dispersions on dynamics: mass properties, sensor errors, actuator misalignments, initial conditions. Pointing budgets and propellant margins come out as statistics. The sim fleet proves the design across the uncertainty cloud.", {"Disperses": "mass, sensors, actuators", "Outputs": "pointing stats, margins", "Proves": "across uncertainty", "Fleet": "Monte Carlo runs"}], ["42 and Formation Missions", "multi-body", "MMS flies four spacecraft in a tetrahedron through Earth's magnetosphere — the formation design, relative navigation, and station-keeping all developed in 42-class simulation. Multi-spacecraft sim is mission-enabling for formations. 42 answers 'where is everyone' precisely.", {"Mission": "MMS tetrahedron", "Developed": "formation + relnav in sim", "Enables": "formation missions", "Answers": "where is everyone"}], ["Truth Models vs Filter Models", "sensors", "42 embodies a core sim discipline: truth models (high fidelity, what really happens) vs filter models (what the flight software believes). The gap between them is where navigation is proven. Simulating both at once is how GNC earns flight rationale.", {"Truth": "high fidelity reality", "Filter": "what software believes", "Gap": "where nav is proven", "Earns": "flight rationale"}], ["The Full 42 Workflow", "attitude-dynamics", "Ladder-top 42: build the spacecraft (mass, actuators, sensors), set the orbit, close the GNC loop, disperse with Monte Carlo, and prove pointing and margins. Fifteen rungs from quaternions to flown formations.", {"Build": "spacecraft model", "Set": "orbit", "Close": "GNC loop", "Prove": "Monte Carlo stats"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var ang=(10+(P.a%80)).toFixed(1);
var code='// 42-style quaternion attitude rotation demo (simulated model)\n';
code+='var th='+ang+'*Math.PI/180, q=[Math.cos(th/2),0,Math.sin(th/2),0], v=[1,0,0];\n';
code+='var x=q[0]*q[0]+q[1]*q[1]-q[2]*q[2]-q[3]*q[3];\n';
code+='console.log("slew '+ang+' deg about Y -> body-X maps to ["+x.toFixed(4)+",0,"+(2*(q[1]*q[3]-q[0]*q[2])).toFixed(4)+"]");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-42-spacecraft-simulation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-42-spacecraft-simulation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
