(function(){'use strict';
/* JAH Fundamentals of Composite Materials Database generator — jahdb-fundamental-composite-materials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CM-";
var FIELDS=["fibers and matrices", "micromechanics", "laminate theory", "manufacturing", "joining", "damage and repair"];
var TOPICS=[
    {t: "What Makes a Composite", b: "Stiff strong fibers in a binding matrix: the fiber carries load, the matrix holds shape and transfers stress between fibers."},
    {t: "Fiber Types", b: "Glass is cheap and tough, carbon is stiff and light, aramid absorbs impact, basalt and natural fibers fill niches \u2014 each with a strength/cost signature."},
    {t: "Matrix Choices", b: "Epoxies dominate aerospace, polyesters and vinyl esters serve marine and construction, PEEK and thermoplastics enable welding and recycling."},
    {t: "The Fiber-Matrix Interface", b: "Load transfers across the interface by shear: sizing chemistry on the fiber makes or breaks composite performance."},
    {t: "Rule of Mixtures", b: "Along the fibers, stiffness and strength average by volume fraction; across them, the soft matrix dominates \u2014 extreme anisotropy by design."},
    {t: "Laminate Stacking", b: "Plies at 0\u00b0, \u00b145\u00b0, 90\u00b0 build quasi-isotropic panels; stacking sequence controls bending-twisting coupling and must stay symmetric and balanced."},
    {t: "Classical Laminate Theory", b: "The ABD matrix predicts every laminate's stiffness from its ply properties \u2014 the working calculation of composite design."},
    {t: "Failure Modes", b: "Fiber breakage, matrix cracking, delamination, and buckling compete; compression-after-impact strength often sizes real structures."},
    {t: "Manufacturing Routes", b: "Hand layup, filament winding, pultrusion, RTM, and autoclave prepreg each trade cost, quality, and shape complexity differently."},
    {t: "Joining Composites", b: "Bonded joints spread load gracefully; bolted joints need careful bearing/bypass analysis \u2014 drilling cuts the very fibers that carry load."},
    {t: "Damage Tolerance", b: "Barely visible impact damage hides delaminations that slash compression strength; ultrasonic inspection finds what eyes cannot."},
    {t: "Repair Methods", b: "Bolted patches restore load paths quickly, bonded scarf repairs restore aerodynamics \u2014 repair design is its own discipline."}
];
var PRINCIPLES=[
    {n: "Rule of mixtures", e: "E_c = V_f\u00b7E_f + V_m\u00b7E_m", s: "Longitudinal stiffness is the volume-weighted average of fiber and matrix stiffness."},
    {n: "Classical laminate theory", e: "[N;M] = [A B;B D][\u03b5;\u03ba]", s: "Laminate forces and moments link to strains and curvatures through the ABD matrix."},
    {n: "Tsai-Wu failure", e: "F_i\u00b7\u03c3_i + F_ij\u00b7\u03c3_i\u00b7\u03c3_j < 1", s: "A quadratic interaction criterion predicting first-ply failure under combined stress."}
];
var USES=["Laying up aircraft wing skins", "Specifying wind-turbine blades", "Designing composite pressure vessels", "Repairing impact-damaged panels"];
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
    id:id, t:tp.t, g:field, name:"Composite Materials"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Composite Materials demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-composite-materials-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-composite-materials-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-composite-materials",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
