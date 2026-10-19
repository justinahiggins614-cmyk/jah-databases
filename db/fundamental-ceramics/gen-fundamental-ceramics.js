(function(){'use strict';
/* JAH Fundamentals of Ceramics Database generator — jahdb-fundamental-ceramics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CER-";
var FIELDS=["clay and raw materials", "forming methods", "drying and firing", "sintering", "microstructure", "advanced ceramics"];
var TOPICS=[
    {t: "What Ceramics Are", b: "Inorganic, non-metallic solids \u2014 from earthenware pots to silicon carbide armor \u2014 bonded ionically and covalently for hardness and heat resistance."},
    {t: "Clay Mineralogy", b: "Kaolinite, illite, and montmorillonite are layered silicates; water between layers gives clay its plasticity and drying its shrinkage."},
    {t: "Forming: Throwing, Casting, Pressing", b: "Wheel throwing aligns particles, slip casting builds hollow ware in molds, dry pressing makes tiles \u2014 forming sets the green microstructure."},
    {t: "Drying Without Cracking", b: "Water leaves pores last; uneven drying shrinks surfaces faster than interiors, so slow, even drying prevents the classic cracks."},
    {t: "Firing Transformations", b: "Quartz inversion, dehydroxylation, and vitrification happen in sequence as temperature climbs \u2014 each leaves a permanent record in the body."},
    {t: "Glazes: Glass on Clay", b: "Glazes are thin glass coatings matched in thermal expansion to the body; fit too tight causes shivering, too loose causes crazing."},
    {t: "Sintering Science", b: "Below the melting point, surface energy drives atoms to fill pores: particle size, temperature, and time control final density."},
    {t: "Porcelain vs Stoneware vs Earthenware", b: "Firing temperature and vitrification separate them: earthenware stays porous, stoneware vitrifies, porcelain vitrifies to translucency."},
    {t: "Microstructure Rules Properties", b: "Grain size, porosity, and grain-boundary phases determine strength, toughness, and thermal behavior \u2014 processing is destiny."},
    {t: "Brittle Fracture and Weibull", b: "Ceramics fail from the worst flaw, not the average one: Weibull statistics turn scatter into reliable design allowances."},
    {t: "Advanced Structural Ceramics", b: "Alumina, zirconia (transformation-toughened), and silicon nitride serve as bearings, cutting tools, and engine parts where metals fail."},
    {t: "Functional Ceramics", b: "Piezoelectrics, ferrites, varistors, and solid-oxide fuel-cell electrolytes exploit electrical and magnetic properties of ceramics."}
];
var PRINCIPLES=[
    {n: "Sintering densification", e: "pores shrink as atoms diffuse", s: "Firing bonds particles by diffusion, eliminating pores without melting the whole body."},
    {n: "Weibull strength statistics", e: "P = 1 \u2212 exp(\u2212(\u03c3/\u03c3\u2080)^m)", s: "Brittle failure follows weakest-link statistics \u2014 design uses probabilities, not averages."},
    {n: "Thermal shock parameter", e: "R = \u03c3\u00b7(1\u2212\u03bd)/(E\u00b7\u03b1)", s: "Resistance to thermal shock rises with strength and falls with stiffness and expansion."}
];
var USES=["Formulating tile and sanitaryware bodies", "Specifying refractory linings", "Designing ceramic cutting tools", "Making electronic ceramic components"];
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
    id:id, t:tp.t, g:field, name:"Ceramics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Ceramics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-ceramics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-ceramics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-ceramics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
