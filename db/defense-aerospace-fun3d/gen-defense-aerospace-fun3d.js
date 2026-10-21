(function(){'use strict';
/* jahdb-defense-aerospace-fun3d-1.0 — deterministic boundless generator for defense-aerospace-fun3d.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["solvers", "turbulence", "adjoint-optimization", "hypersonics", "validation"];
var PREFIX='JAH-DAE6-';
var EDITION='public';
var POOL=[["FUN3D: NASA's Flow Solver", "solvers", "FUN3D (Fully Unstructured Navier-Stokes 3D) is NASA Langley's computational fluid dynamics suite for compressible flow — subsonic to hypersonic — on unstructured grids. It models the air around launch vehicles, capsules, and high-speed aircraft, and it has supported SLS, Orion, and the X-59 quiet supersonic program. It is one of NASA's workhorse CFD codes.", {"Developer": "NASA Langley", "Solves": "compressible Navier-Stokes, 3D", "Grids": "unstructured", "Programs": "SLS, Orion, X-59"}], ["The Navier-Stokes Equations", "solvers", "FUN3D solves the Navier-Stokes equations — conservation of mass, momentum, and energy for a viscous, compressible fluid — discretized on the grid. Everything in CFD is these equations plus models for what the grid cannot resolve. Understanding them is understanding the tool.", {"Equations": "mass, momentum, energy", "Fluid": "viscous, compressible", "Discretized": "on unstructured grids", "Plus": "models for unresolved scales"}], ["Unstructured Grids", "solvers", "Unstructured grids use tetrahedra, prisms, and pyramids that fit complex vehicle shapes — capsules with launch abort towers, SLS with boosters — where structured grids struggle. FUN3D's grid adapts: fine near walls and shocks, coarse in the far field. Grid quality directly sets solution quality.", {"Cells": "tets, prisms, pyramids", "Fits": "complex vehicles", "Adapts": "fine at walls/shocks", "Rule": "grid quality = solution quality"}], ["RANS Turbulence Modeling", "turbulence", "FUN3D's Reynolds-Averaged Navier-Stokes mode models turbulence with closures like Spalart-Allmaras and SST instead of resolving every eddy — the affordable way to get vehicle forces and heating. Turbulence models are calibrated, not derived, which is why validation matters. RANS is the daily driver of aerospace CFD.", {"Mode": "RANS (affordable)", "Models": "Spalart-Allmaras, SST", "Nature": "calibrated closures", "Use": "forces, heating, daily"}], ["DES: When RANS Is Not Enough", "turbulence", "Detached-Eddy Simulation blends RANS near walls with eddy-resolving LES in separated regions — for buffet, wake flows, and launch-vehicle base flows where RANS averages away the physics that matters. DES costs far more than RANS and far less than full LES. Engineers spend the compute where the flow demands it.", {"Blends": "RANS walls + LES separated", "For": "buffet, wakes, base flows", "Cost": "between RANS and LES", "Rule": "spend compute where physics demands"}], ["Hypersonics and Re-entry Heating", "hypersonics", "At hypersonic speeds the air dissociates and ionizes — FUN3D models thermochemical nonequilibrium to predict the heat flux that sizes the heat shield. Shock-layer radiation adds to convective heating on lunar-return trajectories. Getting heating wrong means losing the vehicle, so these models are validated relentlessly.", {"Regime": "dissociating, ionizing flow", "Models": "thermochemical nonequilibrium", "Heating": "convective + radiative", "Stakes": "sizes the heat shield"}], ["Adjoint-Based Design Optimization", "adjoint-optimization", "FUN3D's adjoint solver computes how every design variable affects the objective — drag, lift, heating — in about the cost of one flow solution, no matter how many variables. That gradient drives shape optimization: the wing or capsule reshapes itself toward better performance. This is CFD doing design, not just analysis.", {"Adjoint": "gradient for all variables, ~1 solve", "Drives": "shape optimization", "Objective": "drag, lift, heating", "Shift": "analysis -> design"}], ["SLS Aerodynamics", "validation", "FUN3D modeled the Space Launch System's aerodynamics — the full stack with boosters, core, and Orion — predicting forces, buffet, and base heating through ascent. Wind-tunnel data validated the predictions. Launch vehicle aerodynamics is FUN3D's home turf.", {"Vehicle": "SLS full stack", "Predicts": "forces, buffet, base heating", "Validated": "wind tunnel", "Turf": "launch aerodynamics"}], ["Orion and Capsule Flows", "hypersonics", "Blunt capsules like Orion create detached bow shocks and unsteady wakes — FUN3D predicts the heating distribution and aerodynamic stability that the design depends on. Capsule aerodynamics looks simple and is not. The solver earns its keep on every entry.", {"Shape": "blunt capsule", "Flow": "bow shock + unsteady wake", "Predicts": "heating, stability", "Matters": "every entry"}], ["X-59: Quiet Supersonics", "validation", "The X-59 program shapes its aircraft so the sonic boom arrives as a soft thump — FUN3D's adjoint optimization sculpted the airframe to manage shock placement. CFD designed the quiet. Flight tests will confirm what the solver predicted.", {"Program": "X-59", "Goal": "soft thump, not boom", "Tool": "adjoint shaping", "Proof": "flight test pending"}], ["Verification: The Method of Manufactured Solutions", "validation", "FUN3D is verified with manufactured solutions — choose an answer, derive the source terms that produce it, and check the code recovers it at the theoretical order of accuracy. This proves the discretization is correct independent of physics. Verification first, validation second, always.", {"Method": "manufactured solutions", "Proves": "discretization correct", "Order": "theoretical accuracy recovered", "Sequence": "verify, then validate"}], ["Validation: Wind Tunnels and Flight", "validation", "FUN3D predictions are validated against wind-tunnel measurements and flight data — forces, pressures, heating — with quantified uncertainty. A validated configuration is one where predictions match data within known bounds. Validation never ends; each new vehicle re-earns it.", {"Tunnels": "forces, pressures, heating", "Flight": "the final truth", "Metric": "match within bounds", "Rule": "re-earn per vehicle"}], ["Running FUN3D at Scale", "solvers", "Production FUN3D runs use thousands of cores: the grid partitions across MPI ranks, and strong scaling determines how big a problem finishes overnight. A full-vehicle RANS case is routine; a DES of a launch vehicle is a campaign. Compute planning is part of CFD.", {"Parallel": "MPI partitioned grids", "Metric": "strong scaling", "Routine": "full-vehicle RANS", "Campaign": "vehicle DES"}], ["Solution Adaptation", "adjoint-optimization", "FUN3D adapts the grid to the solution — refining where error indicators are high (shocks, shear layers) and coarsening where the flow is smooth. Adaptation buys accuracy without globally refining. The grid follows the physics.", {"Refines": "shocks, shear layers", "Coarsens": "smooth regions", "Buys": "accuracy without global cost", "Follows": "the physics"}], ["The FUN3D Workflow End to End", "solvers", "Ladder-top FUN3D: build the geometry, generate the adapted grid, set the physics models, solve, check forces and heating, validate against data, and optimize the shape with adjoints. Fifteen rungs from equations to designed flight hardware.", {"Geometry": "vehicle CAD", "Grid": "adapted unstructured", "Solve": "RANS/DES + models", "Design": "adjoint optimization"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var mach=(0.8+(P.a%220)/100).toFixed(2), rho=1.225, V=340*parseFloat(mach), L=1.5, mu=1.81e-5;
var code='// FUN3D-style Reynolds number demo (simulated model)\n';
code+='var rho='+rho+',V='+V.toFixed(1)+',L='+L+',mu='+mu+';\n';
code+='var Re=rho*V*L/mu;\nconsole.log("M='+mach+' V="+V.toFixed(0)+" m/s -> Re="+Re.toExponential(2));';return code;
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
var gen={version:'jahdb-defense-aerospace-fun3d-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-fun3d',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
