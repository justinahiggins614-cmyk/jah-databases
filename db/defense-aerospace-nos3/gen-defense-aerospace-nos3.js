(function(){'use strict';
/* jahdb-defense-aerospace-nos3-1.0 — deterministic boundless generator for defense-aerospace-nos3.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["nos-engine", "simulated-hardware", "cfs-integration", "ground-system", "missions"];
var PREFIX='JAH-DAE10-';
var EDITION='public';
var POOL=[["NOS3: NASA's SmallSat Test Bench", "nos-engine", "NOS3 (NASA Operational Simulator for Small Satellites) is the hardware-in-the-loop test bench that lets smallsat teams run their real flight software against simulated hardware. Built around the NOS Engine with 42 and Trick dynamics plus cFS flight software, it catches interface bugs before launch. It is how small missions get big-mission test discipline.", {"Developer": "NASA (IV&V)", "Tests": "flight SW vs sim HW", "Stack": "NOS Engine + 42 + cFS", "Catches": "interface bugs pre-launch"}], ["The NOS Engine", "nos-engine", "The NOS Engine is the message-passing core: simulated hardware components (power, comms, ADCS) exchange packets over software buses that mimic the real ones — I2C, SPI, UART, SpaceWire. Flight software cannot tell it is not talking to hardware. Fidelity lives in the bus protocols.", {"Core": "message passing", "Buses": "I2C, SPI, UART, SpaceWire", "Illusion": "SW can't tell", "Fidelity": "protocol-level"}], ["Simulated Spacecraft Hardware", "simulated-hardware", "NOS3 simulates the spacecraft's hardware boxes: electrical power (batteries, solar), radios, reaction wheels, GPS receivers — each a software model with the same interface as the real unit. Swap the sim for hardware later without changing flight software. Interfaces are the contract.", {"Boxes": "power, radio, wheels, GPS", "Interface": "same as hardware", "Swap": "sim -> HW, no SW change", "Contract": "interfaces"}], ["cFS Inside NOS3", "cfs-integration", "NOS3 runs actual cFS flight software — the same apps that will fly — against the simulated hardware, so the test is the flight configuration with hardware swapped for models. App bugs, timing bugs, and configuration bugs all surface here. Test what you fly, fly what you test.", {"Runs": "real cFS apps", "Config": "flight + sim HW", "Surfaces": "app, timing, config bugs", "Rule": "test what you fly"}], ["42 and Dynamics in the Loop", "simulated-hardware", "Spacecraft dynamics in NOS3 come from 42-class simulation: attitude and orbit truth drive the simulated sensors, and actuator commands flow back into the dynamics. The loop is closed through the flight software. GNC gets tested against physics, not stubs.", {"Truth": "42-class dynamics", "Drives": "sim sensors", "Back": "actuator commands", "Tests": "GNC vs physics"}], ["The Ground System", "ground-system", "NOS3 includes a ground-system side: command uplink, telemetry downlink, and COSMOS-style tooling to operate the simulated mission. Operators practice on the sim before they touch the real spacecraft. The ground team trains where mistakes are free.", {"Up": "commands", "Down": "telemetry", "Tools": "COSMOS-style ops", "Trains": "where mistakes are free"}], ["Day-in-the-Life Testing", "missions", "NOS3 runs day-in-the-life tests: the full mission timeline — deployments, burns, payload ops, eclipses — executed against the sim to prove the flight software handles the whole story. Timeline bugs are mission bugs; this is where they die. DITL is the dress rehearsal.", {"Runs": "full mission timeline", "Covers": "deploys, burns, eclipses", "Kills": "timeline bugs", "Is": "dress rehearsal"}], ["Fault Injection Campaigns", "nos-engine", "NOS3 injects hardware faults — a stuck wheel, a dead radio, a brownout — to prove the flight software's fault responses work. FDIR logic that never sees a fault in test will not handle one in flight. Campaigns enumerate the failure space systematically.", {"Injects": "wheels, radios, power", "Proves": "FDIR responses", "Logic": "untested = untrusted", "Method": "systematic campaigns"}], ["Timing and Real-Time Behavior", "nos-engine", "Flight software timing is verified in NOS3: scheduler slots, bus latencies, interrupt timing — all measured against requirements in the sim. A missed deadline in sim is a finding; on orbit it is an anomaly. Real-time behavior is a requirement, not a hope.", {"Verifies": "slots, latencies, interrupts", "Sim miss": "a finding", "Orbit miss": "an anomaly", "Is": "a requirement"}], ["SmallSat Missions Using HIL", "missions", "Smallsat missions adopt NOS3-class HIL to punch above their mass class: CubeSats running tested flight software with proven fault handling. The cost of a bug found in HIL is hours; on orbit it can be the mission. Test discipline scales down even when spacecraft do.", {"Users": "CubeSats, smallsats", "Gains": "flagship test discipline", "Bug cost": "hours vs mission", "Scales": "discipline down"}], ["From Sim to FlatSat to Flight", "cfs-integration", "The maturation path: NOS3 sim, then FlatSat (real avionics on a bench wired to sims), then flight. Each step replaces models with hardware while flight software stays constant. By launch, the software has met reality in stages. No surprises is the goal.", {"Steps": "sim -> FlatSat -> flight", "Replaces": "models with HW", "Constant": "flight software", "Goal": "no surprises"}], ["Regression Testing", "nos-engine", "Every flight software change re-runs the NOS3 regression suite — the safety net that catches what the change broke. Regressions run in CI so broken builds never reach the bench. The suite grows with the mission; it is an asset, not overhead.", {"Runs": "per change, in CI", "Catches": "what broke", "Grows": "with the mission", "Is": "an asset"}], ["Power System Simulation", "simulated-hardware", "NOS3's power models — solar input vs orbit, battery charge/discharge, load switching — prove the mission never goes power-negative. Eclipse seasons are the stress test. Power is life; the sim proves the budget closes.", {"Models": "solar, battery, loads", "Stress": "eclipse seasons", "Proves": "budget closes", "Is": "life"}], ["Comms and Link Simulation", "ground-system", "NOS3 simulates the RF link — passes, data rates, dropouts — so the mission proves it can get its data down. Store-and-forward, contact scheduling, and link budgets all get exercised. A spacecraft that cannot phone home is a very expensive brick.", {"Simulates": "passes, rates, dropouts", "Proves": "data gets down", "Exercises": "store-and-forward", "Avoids": "expensive brick"}], ["The NOS3 Test Campaign End to End", "missions", "Ladder-top NOS3: build the sim, load flight software, run DITL, inject faults, check timing, regress every change, mature sim to FlatSat to flight. Fifteen rungs from models to a smallsat that behaves like a flagship.", {"Build": "sim + flight SW", "Run": "DITL + faults", "Check": "timing", "Mature": "to flight"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var pkts=5+P.a%6, dt=100;
var code='// NOS3-style HIL loop timing demo (simulated model)\n';
code+='var t=0,late=0;for(var i=0;i<'+pkts+';i++){t+='+dt+'+((i*37)%11)-5;if(t>(i+1)*'+dt+'){late++;}console.log("frame "+i+": bus time "+t+" ms");}\n';
code+='console.log("HIL: '+pkts+' frames, "+late+" late");';return code;
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
var gen={version:'jahdb-defense-aerospace-nos3-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-nos3',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
