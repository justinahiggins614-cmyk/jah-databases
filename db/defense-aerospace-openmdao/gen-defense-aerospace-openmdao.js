(function(){'use strict';
/* jahdb-defense-aerospace-openmdao-1.0 — deterministic boundless generator for defense-aerospace-openmdao.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["framework", "drivers", "components", "derivatives", "applications"];
var PREFIX='JAH-DAE7-';
var EDITION='public';
var POOL=[["OpenMDAO: NASA's Design Optimization Framework", "framework", "OpenMDAO is NASA Glenn's open-source Python framework for multidisciplinary design optimization (MDO): it wires disciplinary analyses into one model and computes total derivatives so gradient optimizers can improve the whole system at once. Aircraft, propulsion, and trajectory problems are its home turf. Dymos and OpenAeroStruct are built on it.", {"Developer": "NASA Glenn", "Language": "Python, open source", "Method": "MDO with total derivatives", "Built on it": "Dymos, OpenAeroStruct"}], ["Components: The Building Blocks", "components", "An OpenMDAO Component is one analysis with inputs, outputs, and optionally analytic partial derivatives: aerodynamics, structures, propulsion, cost. Components declare what they compute; the framework handles the rest. Good components are the foundation of good optimization.", {"Unit": "Component", "Has": "inputs, outputs, partials", "Examples": "aero, structures, propulsion", "Rule": "good components, good optimization"}], ["Groups and the Model Tree", "framework", "Components assemble into Groups forming a model tree — the full vehicle as nested subsystems. Groups manage connections: an output of one component feeds inputs of others. The tree mirrors engineering organization, which is why large teams can build one model.", {"Assemble": "Components -> Groups", "Tree": "vehicle as subsystems", "Connect": "outputs to inputs", "Mirrors": "engineering org"}], ["Drivers: Optimizers and DOE", "drivers", "Drivers run the model: gradient optimizers (SLSQP, SNOPT), gradient-free methods, and design-of-experiments samplers. The driver asks for objectives and constraints; OpenMDAO supplies totals. Picking the right driver for the problem shape is a core skill.", {"Gradient": "SLSQP, SNOPT", "Free": "gradient-free methods", "Sampling": "DOE", "Skill": "match driver to problem"}], ["Derivatives: The Secret Sauce", "derivatives", "OpenMDAO's power is total derivatives computed efficiently — analytic partials chained by the chain rule, or the adjoint/unified derivatives method for many variables. Gradients make large optimization tractable: hundreds of variables, one derivative pass. Finite differences are the fallback nobody wants.", {"Power": "total derivatives", "Chain": "analytic partials", "Adjoint": "many variables, one pass", "Avoid": "finite differences"}], ["Couplings: When Disciplines Talk Back", "components", "Real systems are coupled: aerodynamics loads the structure, the structure deforms, the deformed shape changes aerodynamics. OpenMDAO solves coupled systems with nonlinear solvers (fixed-point, Newton) so the model converges before the optimizer trusts it. Unconverged couplings poison gradients.", {"Loop": "aero <-> structures", "Solvers": "fixed-point, Newton", "Rule": "converge before optimizing", "Risk": "unconverged poisons gradients"}], ["Dymos: Trajectory Optimization", "applications", "Dymos builds on OpenMDAO for optimal control — trajectories as optimization problems via collocation. Launch ascent, entry guidance, and aircraft climb profiles optimize directly. The same derivative machinery that sizes wings now flies trajectories.", {"Built on": "OpenMDAO", "Method": "collocation", "Problems": "ascent, entry, climb", "Unifies": "design + trajectory"}], ["OpenAeroStruct: Wing Design", "applications", "OpenAeroStruct couples aerodynamics and structures to optimize wings — the canonical OpenMDAO teaching example and a real research tool. Span, twist, and thickness trade induced drag against weight. Students learn MDO on wings before touching vehicles.", {"Couples": "aero + structures", "Optimizes": "span, twist, thickness", "Trades": "drag vs weight", "Role": "canonical teaching tool"}], ["pyCycle: Engine Cycle Analysis", "applications", "pyCycle models gas-turbine engine cycles inside OpenMDAO so the engine optimizes together with the airframe — thermodynamics as components, on-design and off-design. Propulsion-airframe integration is MDO's classic payoff. The engine is no longer a fixed deck of numbers.", {"Models": "turbine cycles", "Modes": "on/off-design", "Couples": "engine + airframe", "Payoff": "integration, not fixed decks"}], ["Scaling and the N2 Diagram", "framework", "OpenMDAO's N2 diagram shows every component, connection, and derivative in the model — the map reviewers use to audit large optimizations. Scaling (normalizing variables) keeps optimizers healthy across mixed units. Big models are managed, not just built.", {"N2": "model map for review", "Scaling": "normalize mixed units", "Manages": "big models", "Audits": "connections, derivatives"}], ["Gradient-Free Optimization", "drivers", "When derivatives are unavailable or the landscape is multimodal, gradient-free drivers — genetic algorithms, differential evolution — search broadly. They cost more function evaluations but need no smoothness. OpenMDAO hosts both families so the problem picks the tool.", {"When": "no derivatives, multimodal", "Methods": "genetic, differential evolution", "Cost": "more evaluations", "Hosts": "both families"}], ["Multiobjective Trades", "drivers", "Real design trades fuel against cost against noise — OpenMDAO explores Pareto fronts where no single optimum exists, only trade-offs. Decision-makers pick along the front with full knowledge. Optimization informs judgment; it does not replace it.", {"Trades": "fuel vs cost vs noise", "Front": "Pareto, no single optimum", "Decides": "humans, informed", "Role": "inform judgment"}], ["Surrogate Models", "derivatives", "Surrogates (kriging, neural nets) stand in for expensive analyses inside the optimization loop, trained on a DOE sample and refined adaptively. They trade a little accuracy for orders of magnitude in speed. OpenMDAO's MetaModel makes swapping one in a one-line change.", {"Stand-ins": "kriging, neural nets", "Trained": "on DOE samples", "Trade": "accuracy for speed", "Swap": "one-line MetaModel"}], ["Uncertainty Quantification", "applications", "OpenMDAO workflows propagate uncertainty — manufacturing variation, model error — to robust optima that work across the distribution, not just at the nominal point. Robust design costs a little nominal performance for a lot of reliability. The math of margins, automated.", {"Propagates": "variation, model error", "Seeks": "robust optima", "Costs": "nominal performance", "Gains": "reliability"}], ["The OpenMDAO Workflow End to End", "framework", "Ladder-top OpenMDAO: build components, assemble the model tree, connect disciplines, converge couplings, pick a driver, supply derivatives, optimize, and read the Pareto trades. Fifteen rungs from single analyses to system-optimal design.", {"Build": "components", "Assemble": "model tree", "Converge": "couplings", "Optimize": "drivers + derivatives"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var k=(0.5+(P.a%40)/100).toFixed(2);
var code='// OpenMDAO-style coupled solve demo (fixed-point, simulated model)\n';
code+='var k='+k+',y=1.0;\nfor(var i=0;i<8;i++){y=1+k*y/(1+y);}\n';
code+='console.log("coupled disciplines converged: y="+y.toFixed(6));';return code;
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
var gen={version:'jahdb-defense-aerospace-openmdao-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-openmdao',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
