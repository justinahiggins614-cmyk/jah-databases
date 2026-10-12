(function(){'use strict';
/* Universal Physics Simulation Database generator — jahdb-universal-physics-sim-1.0.
   Property of Justin Addam Higgins (JAH).
   Recreates accurate universe simulations from the physics archive:
   atoms, compounds, quarks, and formulas databases ground every sim.
   Seed 1 is ALWAYS the Baseline Universe (ours) — real physics, Type 1 factual.
   Seeds 2+ are variant universes branching from baseline — Type 2 speculative,
   every speculative string labeled. Deterministic: same seed = same universe. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-UPS-';
/* ---------------- baseline physics (Type 1: real, measured values) ---------------- */
var BASELINE={
 universe:'Baseline Universe (Ours)',
 is_baseline:true,
 physics_parameters:{
  speed_of_light_m_s:'299792458 (exact, defined)',
  gravitational_constant:'6.67430e-11 m^3 kg^-1 s^-2',
  planck_constant_J_s:'6.62607015e-34 (exact, defined)',
  elementary_charge_C:'1.602176634e-19 (exact, defined)',
  boltzmann_constant_J_K:'1.380649e-23 (exact, defined)',
  fine_structure_constant:'1/137.036 (measured)',
  proton_mass_kg:'1.67262192369e-27',
  electron_mass_kg:'9.1093837015e-31',
  age_billion_years:'13.8',
  spatial_dimensions:'3',
  time_dimensions:'1',
  cosmological_constant:'positive, small (accelerating expansion)',
  matter_antimatter:'matter dominates (asymmetry unexplained)'
 },
 archive_refs:['atom-mixes-environment','compounds-universal','quarks-subatomic','scientific-formulas']
};
/* ---------------- variant axes (Type 2: speculative branches) ---------------- */
var AXES=[
 {key:'gravity',name:'Gravitational strength',up:'Gravity is stronger: stars burn fast and die young, black holes form from smaller masses, planetary orbits tighten.',
  down:'Gravity is weaker: matter stays diffuse, stars take far longer to ignite, galaxies are loose and dim.'},
 {key:'em',name:'Electromagnetic strength',up:'EM force is stronger: chemistry is tighter, atoms are smaller, stellar fusion runs hotter.',
  down:'EM force is weaker: atoms are large and fragile, chemistry is sluggish, solids barely hold together.'},
 {key:'strong',name:'Strong nuclear force',up:'Strong force is stronger: more stable heavy nuclei exist, fusion ignites at lower temperatures.',
  down:'Strong force is weaker: only hydrogen is stable — no carbon, no chemistry, no life as we know it.'},
 {key:'lightspeed',name:'Speed of light',up:'Light is faster: causality loosens, relativity effects shrink, the observable universe is vastly larger.',
  down:'Light is slower: relativistic effects appear at walking pace, distant stars are unreachable in principle.'},
 {key:'cosmo',name:'Cosmological constant',up:'Expansion accelerates harder: galaxies isolate early, the sky goes dark sooner.',
  down:'Expansion is slower or reverses: a Big Crunch becomes possible, the universe may recollapse.'},
 {key:'dimensions',name:'Spatial dimensions',up:'More than 3 spatial dimensions: gravity dilutes faster, stable orbits are rare, chemistry is alien.',
  down:'Fewer than 3 spatial dimensions: no stable atoms as we know them, a flattened physics.'},
 {key:'weak',name:'Weak nuclear force',up:'Weak force is stronger: radioactive decay is rapid, heavy elements are fleeting.',
  down:'Weak force is weaker: stars cannot fuse past helium efficiently, supernovae are rare.'},
 {key:'matter',name:'Matter-antimatter balance',up:'Perfect symmetry: total annihilation — a universe of pure radiation, no matter at all.',
  down:'Even stronger asymmetry: denser matter, faster structure formation.'}
];
var VARIANT_NAMES=['Ashen Expanse','Tight Orbit','Slow Ember','Bright Lattice','Deep Drift','Iron Bloom','Quiet Crunch','Glass Vacuum','Heavy Dawn','Thin Fire'];
function buildBaseline(){
 return {
  universe:BASELINE.universe,
  is_baseline:true,
  physics_parameters:BASELINE.physics_parameters,
  archive_refs:BASELINE.archive_refs,
  simulation:{
   method:'Parameters drawn from the physics archive: atomic reactions (atom-mixes-environment), compound phenomena (compounds-universal), subatomic processes (quarks-subatomic), governing equations (scientific-formulas).',
   evolution:['t=0: Big Bang — hot dense state, all forces unified','t=1e-43 s: Planck epoch ends, gravity separates','t=1e-36 s: inflation expands space enormously','t=1e-6 s: quarks confine into protons and neutrons','t=3 min: Big Bang nucleosynthesis — hydrogen, helium, trace lithium','t=380,000 yr: recombination — atoms form, light travels free (CMB)','t=200 Myr: first stars ignite, forging heavier elements','t=9.2 Gyr: solar system forms from enriched gas','t=13.8 Gyr: present day'],
   key_events:['Big Bang nucleosynthesis sets H/He ratio','First stars forge carbon and beyond','Supernovae seed interstellar medium','Solar system condenses 4.6 Gyr ago']
  },
  branch_point:null,
  known_findings:'This record describes our own universe with measured physical constants (Type 1 factual). The speed of light, Planck constant, elementary charge and Boltzmann constant are exact by SI definition; G, the fine-structure constant and particle masses are measured values.',
  speculative_findings:null,
  type:'baseline universe',
  src:'fact'
 };
}
function buildVariant(s,seed){
 var nAxes=ri(s,1,3);
 var axes=[],used={};
 for(var i=0;i<nAxes;i++){var a;do{a=pick(AXES,s);}while(used[a.key]);used[a.key]=1;axes.push(a);}
 var dirs=axes.map(function(a){return s()<0.5?'up':'down';});
 var branch=axes.map(function(a,i){return a.name+' shifted '+(dirs[i]==='up'?'higher':'lower');}).join('; ');
 var consequences=axes.map(function(a,i){return (dirs[i]==='up'?a.up:a.down)+' [SPECULATIVE]';});
 var vname=pick(VARIANT_NAMES,s)+' '+(seed);
 var params={};
 axes.forEach(function(a,i){params[a.key]=dirs[i]==='up'?'increased vs baseline [SPECULATIVE]':'decreased vs baseline [SPECULATIVE]';});
 params.note='All other parameters match the Baseline Universe. [SPECULATIVE]';
 return {
  universe:'Variant Universe '+vname,
  is_baseline:false,
  physics_parameters:params,
  archive_refs:BASELINE.archive_refs,
  simulation:{
   method:'Branches from the Baseline Universe record using the same physics-archive grounding; altered parameters are extrapolated. [SPECULATIVE]',
   evolution:['t=0: variant Big Bang with altered parameters [SPECULATIVE]','Early universe follows the altered physics [SPECULATIVE]','Structure formation diverges from baseline [SPECULATIVE]'],
   key_events:consequences
  },
  branch_point:'Diverges from the Baseline Universe at: '+branch+'. [SPECULATIVE]',
  known_findings:'The baseline physics this variant branches from is measured and factual (Type 1).',
  speculative_findings:'Everything about this variant universe — its parameters, evolution and consequences — is speculative extrapolation (Type 2). Labeled throughout. [SPECULATIVE]',
  type:'variant universe',
  src:'signature'
 };
}
/* ---------------- main ---------------- */
function generate(seed,opts){
 opts=opts||{};
 var s=prng(seed);
 var id=PREFIX+String(seed).padStart(6,'0');
 var b=(seed===1)?buildBaseline():buildVariant(s,seed);
 var title=b.is_baseline?'Baseline Universe (Ours) — full physics simulation record':'Universe Sim '+b.universe;
 var desc=b.is_baseline?
  'The baseline record: our own universe recreated from the physics archive — real constants, real history from the Big Bang to today. Every other simulation branches from this one.':
  'A variant universe branching from the baseline at: '+b.branch_point+' Speculative throughout and labeled.';
 return {id:id,title:title,description:desc,universe:b.universe,is_baseline:b.is_baseline,
  physics_parameters:b.physics_parameters,archive_refs:b.archive_refs,simulation:b.simulation,
  branch_point:b.branch_point,known_findings:b.known_findings,speculative_findings:b.speculative_findings,
  type:b.type,src:b.src,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-UPS-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(typeof r.universe!=='string'||!r.universe.length)e.push('universe');
 if(typeof r.is_baseline!=='boolean')e.push('is_baseline');
 if(!r.physics_parameters||typeof r.physics_parameters!=='object')e.push('physics_parameters');
 if(!r.simulation||typeof r.simulation!=='object')e.push('simulation');
 if(r.is_baseline!==true&&typeof r.branch_point!=='string')e.push('branch_point');
 if(typeof r.known_findings!=='string'||!r.known_findings.length)e.push('known_findings');
 if(r.src!=='fact'&&r.src!=='signature')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.universe===record.universe&&r.id!==record.id;});
 return dups.length?{ok:false,errors:['duplicate universe in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-universal-physics-sim-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-physics-sim',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
