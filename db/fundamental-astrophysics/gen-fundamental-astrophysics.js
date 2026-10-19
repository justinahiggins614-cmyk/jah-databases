(function(){'use strict';
/* JAH Fundamentals of Astrophysics Database generator — jahdb-fundamental-astrophysics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AST-";
var FIELDS=["stars", "stellar evolution", "galaxies", "black holes", "cosmology basics", "observational methods"];
var TOPICS=[
    {t: "What Astrophysics Does", b: "Applying physics \u2014 gravity, thermodynamics, nuclear, quantum \u2014 to everything beyond Earth, tested by light alone."},
    {t: "Star Formation", b: "Molecular clouds collapse when gravity beats pressure (Jeans criterion); protostars ignite when cores reach 10 million K."},
    {t: "The Main Sequence", b: "Hydrogen-burning stars obey the mass-luminosity relation (L \u221d M^3.5): mass is destiny on the H-R diagram."},
    {t: "Stellar Death: White Dwarfs", b: "Electron degeneracy pressure halts collapse below 1.4 solar masses (Chandrasekhar limit): Earth-sized stellar embers."},
    {t: "Neutron Stars and Pulsars", b: "Supernova cores crushed to nuclear density, spinning with lighthouse beams: the most precise clocks in nature."},
    {t: "Stellar-Mass Black Holes", b: "Above ~3 solar masses nothing stops collapse: event horizons hide singularities, accretion disks blaze in X-rays."},
    {t: "Galaxies", b: "Spirals, ellipticals, irregulars: island universes of billions of stars, organized by mergers and dark-matter halos."},
    {t: "Supermassive Black Holes", b: "Millions to billions of solar masses anchor galaxy centers (Sgr A*, M87*): imaged as shadows by the Event Horizon Telescope."},
    {t: "Active Galactic Nuclei", b: "Accreting supermassive black holes outshine galaxies: quasars are the most luminous persistent objects known."},
    {t: "Dark Matter", b: "Galaxy rotation curves and lensing demand ~5\u00d7 more mass than visible: the universe's dominant matter is unknown."},
    {t: "The Cosmic Distance Ladder", b: "Parallax \u2192 Cepheids \u2192 supernovae: overlapping rungs climb from nearby stars to the Hubble flow."},
    {t: "Multi-Messenger Astronomy", b: "Light plus gravitational waves plus neutrinos plus cosmic rays: four senses on the universe since 2015\u20132017."}
];
var PRINCIPLES=[
    {n: "Stefan-Boltzmann", e: "L = 4\u03c0R\u00b2\u03c3T\u2074", s: "A star's luminosity follows from its radius and surface temperature."},
    {n: "Hydrostatic equilibrium", e: "dP/dr = \u2212\u03c1GM/r\u00b2", s: "Stars balance gravity against pressure gradient \u2014 the equation of stellar structure."},
    {n: "Eddington luminosity", e: "L_Edd = 4\u03c0GMm_pc/\u03c3_T", s: "Radiation pressure caps how bright an object of mass M can shine."}
];
var USES=["Classifying stars and galaxies", "Planning telescope observations", "Modeling stellar populations", "Interpreting gravitational-wave events"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Astrophysics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Astrophysics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-astrophysics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-astrophysics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-astrophysics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
