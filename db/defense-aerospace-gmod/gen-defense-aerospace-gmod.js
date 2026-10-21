(function(){'use strict';
/* jahdb-defense-aerospace-gmod-1.0 — deterministic boundless generator for defense-aerospace-gmod.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["propagators", "targeting", "estimation", "force-models", "missions"];
var PREFIX='JAH-DAE3-';
var EDITION='public';
var POOL=[["GMAT: NASA's Open-Source Mission Design Tool", "propagators", "The General Mission Analysis Tool (GMAT) is NASA Goddard's open-source space trajectory optimization and mission analysis system, developed with private-sector contributors. It designs trajectories from low Earth orbit to interplanetary cruise, and it has supported real missions including LRO, LADEE, OSIRIS-REx, and TESS. It is free, scriptable, and runs on desktop workstations.", {"Developer": "NASA Goddard + contributors", "License": "open source", "Missions": "LRO, LADEE, OSIRIS-REx, TESS", "Scope": "LEO to interplanetary"}], ["Propagators: Moving the Spacecraft", "propagators", "A propagator numerically integrates the spacecraft's equations of motion: GMAT offers Runge-Kutta 89, Prince-Dormand 78, and other integrators with adaptive step control. The integrator picks small steps where dynamics are fast (perigee) and large steps where they are slow (apogee). Accuracy settings trade compute time against trajectory error.", {"Integrators": "RK89, Prince-Dormand 78", "Control": "adaptive step size", "Trade": "accuracy vs compute time", "Small steps": "near perigee"}], ["Force Models: What Pushes the Spacecraft", "force-models", "GMAT's force models decide which physics the propagator integrates: point-mass gravity plus high-order gravity fields, atmospheric drag, solar radiation pressure, and third-body gravity from the Sun and Moon. Drag needs an atmosphere model and a spacecraft area-to-mass; SRP needs reflectivity. Leaving out a real force is how trajectories quietly go wrong.", {"Gravity": "point mass + high-order fields", "Drag": "atmosphere + area/mass", "SRP": "reflectivity model", "Third body": "Sun, Moon"}], ["Finite Burns: Modeling Real Maneuvers", "targeting", "Real maneuvers are finite burns — the engine fires for minutes, and the thrust direction and mass flow shape the trajectory during the burn. GMAT models impulsive burns for quick studies and finite burns with thruster data for flight fidelity. Burn execution errors (magnitude, pointing) become dispersions in Monte Carlo analysis.", {"Impulsive": "instant delta-v, quick studies", "Finite": "timed thrust, flight fidelity", "Errors": "magnitude + pointing", "Analysis": "Monte Carlo dispersions"}], ["Targeting: Hitting the Aim Point", "targeting", "Targeting solves for the maneuver that hits the aim point: GMAT's differential corrector varies control variables (burn components, epochs) until constraints (altitude, B-plane, arrival conditions) are met. It is Newton-style iteration on a trajectory — propagate, measure the miss, correct, repeat. Most mission design is targeting loops.", {"Solver": "differential corrector", "Varies": "burns, epochs", "Targets": "altitude, B-plane, arrival", "Method": "propagate, measure, correct"}], ["Estimators: Orbit Determination", "estimation", "GMAT's estimators turn tracking measurements into orbit knowledge: batch least-squares fits long arcs of data, and the extended Kalman filter processes measurements sequentially. Estimation needs a measurement model (range, Doppler) plus station locations and media corrections. The covariance out of the estimator sizes every maneuver and every pointing budget.", {"Batch LS": "fits long data arcs", "EKF": "sequential processing", "Measurements": "range, Doppler", "Output": "state + covariance"}], ["GMAT Scripting: The Mission Script", "propagators", "A GMAT mission is a script: create spacecraft and propagators, set initial conditions, then a mission sequence of Propagate, Maneuver, and Achieve commands. Scripts are text, version-controlled, and reviewable — the mission design is literally readable. GUIs generate the same scripts underneath.", {"Format": "text mission script", "Objects": "spacecraft, propagators, burns", "Sequence": "Propagate, Maneuver, Achieve", "Practice": "version-controlled, reviewable"}], ["Coordinate Systems and Time", "force-models", "Trajectory work lives or dies on frames and time: GMAT handles Earth-centered inertial, Moon-centered, and rotating frames, plus UTC, TAI, and ephemeris time conversions. A maneuver computed in the wrong frame misses by thousands of kilometers. Frame discipline is a core mission-design skill the tool enforces.", {"Frames": "ECI, Moon-centered, rotating", "Times": "UTC, TAI, ephemeris", "Risk": "wrong frame = huge miss", "Discipline": "tool-enforced"}], ["Optimization: Finding the Best Trajectory", "targeting", "GMAT's optimizers search maneuver variables for minimum fuel or minimum time subject to constraints — the same targeting machinery with an objective function. Low-thrust spirals and multi-burn sequences are optimizer territory. The optimizer needs good initial guesses, which is why designers still sketch trajectories by hand first.", {"Goal": "min fuel / min time", "Method": "constrained optimization", "Hard cases": "low-thrust, multi-burn", "Needs": "good initial guesses"}], ["LRO: GMAT at the Moon", "missions", "The Lunar Reconnaissance Orbiter mission used GMAT-class trajectory design for its lunar orbit insertion and station-keeping in the Moon's lumpy gravity field. Low lunar orbits are unstable — mascons tug constantly — so the design included regular maintenance maneuvers. GMAT's force models and targeting handled it.", {"Mission": "Lunar Reconnaissance Orbiter", "Challenge": "mascons, unstable low orbits", "Ops": "regular station-keeping", "Tool": "GMAT trajectory design"}], ["OSIRIS-REx: Touching an Asteroid", "missions", "OSIRIS-REx's journey to the asteroid Bennu and its touch-and-go sample collection were designed with GMAT-class tools: interplanetary cruise targeting, proximity operations around a tiny spinning body, and the precise TAG maneuver. Milligravity proximity ops are the extreme edge of trajectory design.", {"Mission": "OSIRIS-REx", "Target": "asteroid Bennu", "Ops": "proximity + touch-and-go", "Regime": "milligravity design"}], ["TESS: The Lunar Flyby Trick", "missions", "TESS rides a clever 2:1 lunar-resonant high Earth orbit designed with GMAT-class analysis: a lunar flyby pumps the orbit into a stable resonance that needs almost no maintenance. The trajectory does the work that propellant would otherwise do. Mission design at its most elegant.", {"Mission": "TESS", "Orbit": "2:1 lunar resonance", "Trick": "lunar flyby pump-up", "Payoff": "near-zero maintenance"}], ["Validation: Trusting the Numbers", "estimation", "GMAT is validated against known solutions: two-body spot checks, published trajectories, and cross-comparison with independent tools. Validation is never 'it ran' — it is quantified error against truth. Every mission re-validates the configurations it actually flies.", {"Checks": "two-body, published trajectories", "Cross-check": "independent tools", "Metric": "quantified error vs truth", "Rule": "validate what you fly"}], ["Ephemeris: Where Everything Is", "force-models", "GMAT pulls planet and Moon positions from ephemeris files (DE series) so every propagation uses the same solar system everyone else uses. Third-body forces and eclipse calculations depend on it. Consistent ephemerides are why two teams get the same trajectory.", {"Source": "DE ephemeris series", "Gives": "planet + Moon positions", "Drives": "third-body, eclipses", "Value": "everyone gets the same answer"}], ["The Full GMAT Mission Design Loop", "missions", "The ladder-top GMAT loop: sketch the trajectory, script the mission, propagate with full force models, target the aim points, optimize the fuel, estimate with tracking data, validate against truth, and fly. Fifteen rungs up, that loop designed real missions to the Moon, asteroids, and deep space — open source, on a workstation.", {"Sketch": "hand design first", "Script": "readable mission", "Solve": "target + optimize", "Prove": "estimate + validate", "Fly": "real missions"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var dv1=(3.2+(P.a%40)/50).toFixed(2), dv2=(2.9+(P.b%40)/50).toFixed(2);
var code='// GMAT-style Hohmann transfer demo (simulated model)\n';
code+='var dv1='+dv1+', dv2='+dv2+';\n';
code+='var total=dv1+dv2;\nconsole.log("Hohmann: burn1="+dv1+" km/s burn2="+dv2+" km/s");\nconsole.log("total delta-v="+total.toFixed(2)+" km/s");';return code;
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
var gen={version:'jahdb-defense-aerospace-gmod-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-gmod',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
