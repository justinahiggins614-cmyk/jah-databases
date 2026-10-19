(function(){'use strict';
/* JAH Fundamentals of Nanofabrication Database generator — jahdb-fundamental-nanofabrication-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NAN-";
var FIELDS=["cleanrooms", "lithography", "deposition", "etching", "self-assembly", "nanometrology"];
var TOPICS=[
    {t: "Why Nanometers Matter", b: "At 1\u2013100 nm, quantum confinement, surface plasmons, and huge surface-to-volume ratios create properties bulk materials never show."},
    {t: "Cleanrooms", b: "A single dust particle dwarfs a transistor: ISO classes, bunny suits, and ULPA filtration keep killer defects off wafers."},
    {t: "Photolithography", b: "Projecting circuit patterns through masks with deep-UV light is how billions of transistors print per chip \u2014 the industry's core art."},
    {t: "EUV Lithography", b: "13.5-nm extreme-ultraviolet light, all-mirror optics, and tin-droplet plasma sources print today's most advanced chips."},
    {t: "Electron-Beam Lithography", b: "A focused electron beam writes arbitrary patterns without masks \u2014 slow but capable of sub-10-nm research structures."},
    {t: "Thin-Film Deposition", b: "Evaporation, sputtering, CVD, and atomic layer deposition build films atom by atom, each with its own uniformity and conformality signature."},
    {t: "Atomic Layer Deposition", b: "Self-limiting half-reactions grow exactly one atomic layer per cycle \u2014 perfect for ultrathin, pinhole-free barriers."},
    {t: "Wet and Dry Etching", b: "Liquid etchants undercut isotropically; plasma (dry) etching carves vertical walls \u2014 anisotropy is the whole game in device fabrication."},
    {t: "Lift-Off and Damascene", b: "Additive patterning (lift-off) and trench-fill (damascene copper interconnects) are the two philosophies of making metal lines."},
    {t: "Self-Assembly", b: "Block copolymers and DNA origami pattern themselves at molecular scales \u2014 bottom-up fabrication complementing top-down lithography."},
    {t: "Nanometrology", b: "SEM, AFM, and TEM see what optical microscopes cannot; measuring nanometers demands its own instruments and statistics."},
    {t: "From Lab to Fab", b: "Yield, throughput, contamination control, and cost per wafer separate research demos from manufacturing \u2014 scaling is the hardest step."}
];
var PRINCIPLES=[
    {n: "Diffraction limit", e: "CD \u2248 k\u2081\u00b7\u03bb/NA", s: "The smallest printable feature scales with wavelength over numerical aperture."},
    {n: "Deposition rate", e: "rate = flux \u00d7 sticking", s: "Film growth is incoming atom flux times the probability each atom stays."},
    {n: "Etch selectivity", e: "selectivity = rate_target/rate_mask", s: "Useful etching removes the target far faster than the mask."}
];
var USES=["Planning semiconductor process flows", "Specifying thin-film coatings", "Designing nano-patterned surfaces", "Troubleshooting cleanroom yield"];
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
    id:id, t:tp.t, g:field, name:"Nanofabrication"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Nanofabrication demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-nanofabrication-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-nanofabrication-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-nanofabrication",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
