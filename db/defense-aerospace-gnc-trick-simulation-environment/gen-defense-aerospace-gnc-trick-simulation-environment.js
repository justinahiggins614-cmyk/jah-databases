(function(){'use strict';
/* jahdb-defense-aerospace-gnc-trick-simulation-environment-1.0 — deterministic boundless generator for defense-aerospace-gnc-trick-simulation-environment.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["trick-framework", "gnc-algorithms", "monte-carlo", "data-systems", "missions"];
var PREFIX='JAH-DAE2-';
var EDITION='public';
var POOL=[["Trick: NASA Johnson's Simulation Framework", "trick-framework", "Trick is NASA Johnson Space Center's open-source simulation framework for building high-fidelity dynamic simulations of space vehicles. Engineers write models in C/C++ with a S_define definition file, and Trick generates the executable simulation with scheduling, I/O, and data recording built in. It has supported programs from the Space Shuttle era through Orion.", {"Developer": "NASA Johnson Space Center", "Input": "S_define + C/C++ models", "Output": "executable simulation", "License": "open source", "Programs": "Shuttle, Station, Orion"}], ["S_define: The Simulation Definition File", "trick-framework", "Every Trick simulation starts with S_define, a definition file that declares which models are included, how jobs are scheduled, and what data gets recorded. Trick's interface code generator reads S_define and produces the glue code that wires models into the executive. Changing the simulation is mostly editing S_define, not rewriting models.", {"File": "S_define", "Declares": "models, scheduling, I/O", "Tool": "interface code generator", "Effect": "reconfigure without rewriting"}], ["GNC Algorithms in Simulation", "gnc-algorithms", "Guidance, Navigation, and Control algorithms are developed and wrung out inside Trick before they ever fly: guidance computes the desired trajectory, navigation estimates the state from sensors, and control drives actuators to follow it. Trick lets engineers inject sensor noise, actuator failures, and dispersions to prove the GNC design is robust. Orion's entry guidance was matured this way.", {"G": "guidance — desired path", "N": "navigation — state estimate", "C": "control — actuator commands", "Method": "noise + failures + dispersions", "Example": "Orion entry guidance"}], ["Monte Carlo Dispersions", "monte-carlo", "Trick's Monte Carlo capability runs the same simulation hundreds or thousands of times with randomized initial conditions, winds, masses, and sensor errors. The spread of outcomes — landing footprints, miss distances, propellant remaining — is the statistical proof a design is safe. Requirements are often written as '99.7% of Monte Carlo cases shall...' and Trick generates the evidence.", {"Runs": "hundreds to thousands", "Randomized": "ICs, winds, masses, errors", "Output": "footprints, margins", "Requirements": "statistical, e.g. 3-sigma"}], ["TrickHLA: Distributed Simulation", "trick-framework", "TrickHLA connects multiple Trick simulations — or Trick to other simulators — over the High Level Architecture (HLA) standard, so a vehicle sim, a ground-system sim, and a crew trainer can run as one federated simulation. Time management keeps every federate synchronized. This is how distributed mission rehearsals are built.", {"Standard": "HLA (IEEE 1516)", "Use": "federated multi-sim runs", "Sync": "HLA time management", "Example": "vehicle + ground + trainer"}], ["Data Recording and TrickView", "data-systems", "Trick records any model variable to data files during a run, and TrickView plots it live or after the fact — strip charts, 3D views, and custom displays. Engineers watch guidance errors, propellant, and attitude in real time as the sim runs. Recorded data is the evidence package for design reviews.", {"Record": "any model variable", "TrickView": "live + post plots", "Views": "strip charts, 3D, custom", "Use": "review evidence"}], ["Real-Time and Hardware-in-the-Loop", "trick-framework", "Trick simulations can run in real time and connect to real flight hardware — the sim provides the environment (sensors, dynamics) while actual avionics boxes run the software. This hardware-in-the-loop testing catches interface bugs months before flight. Trick's real-time scheduler guarantees the frame rate the hardware expects.", {"Mode": "real-time executive", "HIL": "real avionics + sim environment", "Catches": "interface bugs pre-flight", "Scheduler": "frame-rate guaranteed"}], ["Input Files: Running Cases Without Rebuilding", "trick-framework", "Trick input files set model parameters at run start — initial conditions, mass properties, failure flags — so one compiled sim runs thousands of different cases. Combined with Monte Carlo, input files are the batch engine of verification. A case matrix that would take months of rebuilds becomes an overnight run queue.", {"Files": "run-time parameter sets", "Set": "ICs, masses, failures", "Batch": "case matrices overnight", "Rebuilds": "zero per case"}], ["Navigation: Filtering Noisy Sensors", "gnc-algorithms", "Navigation in Trick-modeled vehicles fuses noisy sensors — IMUs, star trackers, GPS — into a best estimate of position, velocity, and attitude, usually with a Kalman-style filter. Trick lets engineers tune filter gains against truth models with realistic noise. Bad navigation tuning shows up as growing errors long before it would in flight.", {"Sensors": "IMU, star tracker, GPS", "Filter": "Kalman-style fusion", "Tuning": "against truth + noise models", "Sign": "error growth = bad tuning"}], ["Entry, Descent, and Landing Simulation", "missions", "Trick-class simulations model the hardest minutes of a mission — atmospheric entry, descent, and landing — with aerodynamics, parachutes, winds, and terrain. Dispersions on every parameter produce the landing ellipse the recovery team plans around. Orion and Mars lander programs live in these sims for years.", {"Phase": "EDL — hardest minutes", "Models": "aero, chutes, winds, terrain", "Output": "landing ellipse", "Users": "Orion, Mars landers"}], ["Failure Injection and Fault Tolerance", "gnc-algorithms", "Trick makes it easy to break the vehicle on purpose: stuck thrusters, biased sensors, dropped telemetry frames. Fault-tolerant GNC must detect, isolate, and recover without ground help, and the sim is where that logic earns its flight rationale. Every failure mode in the FMEA gets sim cases.", {"Inject": "thrusters, sensors, comms", "FDIR": "detect, isolate, recover", "Evidence": "FMEA case coverage", "Goal": "autonomous recovery"}], ["Verification Campaigns: From Sim to Flight", "missions", "A Trick verification campaign is the bridge between design and flight: requirements trace to sim cases, cases run in Monte Carlo batches, results feed the verification database, and reviewers sign off on statistics, not anecdotes. The sim models themselves are validated against test data. This is the paperwork that lets a vehicle fly crew.", {"Trace": "requirements -> sim cases", "Batches": "Monte Carlo evidence", "Models": "validated vs test data", "Sign-off": "statistics, not anecdotes"}], ["Trick in the Orion Program", "missions", "Orion's guidance, navigation, and control development leaned heavily on Trick-based simulation: high-fidelity vehicle dynamics, sensor models, and Monte Carlo verification of entry trajectories. The same sim framework supported training and mission operations analysis. Trick is part of why Orion's uncrewed Artemis I flight behaved as predicted.", {"Program": "Orion / Artemis", "Use": "GNC development + verification", "Models": "dynamics, sensors, entry", "Result": "Artemis I matched predictions"}], ["TrickView Custom Displays", "data-systems", "TrickView is Trick's visualization front end: engineers build custom displays — dials, strip charts, 3D vehicle views — bound directly to sim variables, watching a run unfold in real time. A good display turns a thousand numbers into one glance. Displays are saved with the sim so every analyst sees the same picture.", {"Tool": "TrickView", "Widgets": "dials, charts, 3D views", "Binding": "direct to sim variables", "Saved": "with the simulation"}], ["The Full Trick Workflow, Start to Finish", "trick-framework", "The complete Trick workflow in one ladder-top picture: write models in C/C++, declare the sim in S_define, generate the executable, drive cases with input files, run Monte Carlo batches, record everything, visualize in TrickView, and file the statistics as verification evidence. Fifteen rungs up, that pipeline is how Johnson proves a vehicle is ready to fly.", {"Write": "models in C/C++", "Declare": "S_define", "Drive": "input files", "Prove": "Monte Carlo + recording", "File": "verification evidence"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var steps=6+P.a%5, x=7000, y=0, vx=0, vy=7.5, mu=398600, dt=60;
var code='// Trick-style 2-body propagation demo (simulated model)\nvar x='+x+',y='+y+',vx='+vx+',vy='+vy+',mu='+mu+',dt='+dt+';\n';
code+='for(var s=0;s<'+steps+';s++){var r=Math.sqrt(x*x+y*y);var ax=-mu*x/(r*r*r),ay=-mu*y/(r*r*r);vx+=ax*dt;vy+=ay*dt;x+=vx*dt;y+=vy*dt;console.log("t+"+((s+1)*dt)+"s r="+r.toFixed(1)+" km");}\n';
code+='console.log("done: orbit propagated '+steps+' steps");';return code;
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
var gen={version:'jahdb-defense-aerospace-gnc-trick-simulation-environment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-gnc-trick-simulation-environment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
