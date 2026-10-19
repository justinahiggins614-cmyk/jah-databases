(function(){'use strict';
/* JAH Fundamentals of Glass Science Database generator — jahdb-fundamental-glass-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GS-";
var FIELDS=["glass formation", "structure", "thermal properties", "mechanical properties", "optical properties", "manufacturing"];
var TOPICS=[
    {t: "What Makes a Glass", b: "Glass is a supercooled liquid frozen into an amorphous solid: no crystal lattice, no sharp melting point, just rising viscosity."},
    {t: "Network Formers and Modifiers", b: "Silica tetrahedra form the network; soda and lime modifiers break it up to lower melting temperature \u2014 window glass is soda-lime-silica."},
    {t: "The Glass Transition", b: "Tg marks where a melt becomes rigid on laboratory timescales; below Tg the structure is frozen, above it the material can still flow."},
    {t: "Viscosity and Working Range", b: "Glassblowing and forming happen across defined viscosity points (working, softening, annealing) spanning ten orders of magnitude."},
    {t: "Annealing: Removing Stress", b: "Controlled slow cooling through the annealing range relaxes internal stress \u2014 skip it and the glass shatters spontaneously later."},
    {t: "Why Glass Breaks", b: "Theoretical strength is enormous, but microscopic surface flaws concentrate stress: real glass fails at a few tens of megapascals in tension."},
    {t: "Strengthening Glass", b: "Thermal tempering and ion-exchange (chemical strengthening) put surfaces into compression, multiplying practical strength several-fold."},
    {t: "Thermal Shock Resistance", b: "Low-expansion borosilicate (Pyrex-type) survives rapid temperature swings that shatter soda-lime \u2014 expansion coefficient is the key."},
    {t: "Optical Properties", b: "Transparency, refractive index, and dispersion are tuned by composition: flint glass bends light strongly, fused silica passes deep UV."},
    {t: "Colored Glass Chemistry", b: "Transition-metal ions paint glass: cobalt makes blue, gold makes ruby red, iron makes green \u2014 the medieval stained-glass palette."},
    {t: "Float Glass Process", b: "Molten glass floats on liquid tin to make perfectly flat, fire-polished sheets \u2014 the process behind nearly all modern windows."},
    {t: "Specialty Glasses", b: "Gorilla-type cover glass, fiber-optic silica, bioactive bone glass, and metallic glasses each push one property to an extreme."}
];
var PRINCIPLES=[
    {n: "Viscosity-temperature (VFT)", e: "log \u03b7 = A + B/(T \u2212 T\u2080)", s: "Glass has no melting point \u2014 viscosity rises continuously through the working range."},
    {n: "Thermal stress", e: "\u03c3 = E\u00b7\u03b1\u00b7\u0394T/(1\u2212\u03bd)", s: "Stress from temperature gradients scales with stiffness, expansion, and the gradient itself."},
    {n: "Griffith flaw strength", e: "\u03c3 \u221d 1/\u221a(flaw size)", s: "Glass strength is set by surface flaws, not bonds \u2014 pristine fibers reach gigapascals."}
];
var USES=["Specifying window and facade glazing", "Designing phone cover glass", "Building laboratory glassware", "Making optical fiber preforms"];
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
    id:id, t:tp.t, g:field, name:"Glass Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Glass Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-glass-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-glass-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-glass-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
