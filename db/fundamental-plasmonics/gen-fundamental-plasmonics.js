(function(){'use strict';
/* JAH Fundamentals of Plasmonics Database generator — jahdb-fundamental-plasmonics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLA-";
var FIELDS=["surface plasmons", "localized plasmons", "nanoantennas", "sensing", "metasurfaces", "active plasmonics"];
var TOPICS=[
    {t: "What a Plasmon Is", b: "A plasmon is a collective sloshing of a metal's free electrons \u2014 a charge-density wave that couples strongly to light."},
    {t: "Surface Plasmon Polaritons", b: "At a metal-dielectric interface, light and electron waves marry into a surface-bound hybrid that hugs the boundary."},
    {t: "Localized Surface Plasmons", b: "Metal nanoparticles resonate like tiny antennas, scattering vivid colors \u2014 the physics of medieval stained glass, now engineered."},
    {t: "Why Gold and Silver", b: "Noble metals have the right electron density and low loss in the visible; aluminum extends plasmonics into the ultraviolet."},
    {t: "Nanoantennas", b: "Shaped metal particles focus light into nanometer hotspots, enhancing fluorescence and Raman signals by orders of magnitude."},
    {t: "SERS Sensing", b: "Surface-enhanced Raman scattering turns single molecules detectable: plasmonic hotspots amplify molecular fingerprints a billion-fold."},
    {t: "Plasmonic Biosensors", b: "Binding events shift the plasmon resonance wavelength \u2014 label-free, real-time detection of proteins, DNA, and pathogens."},
    {t: "Metasurfaces", b: "Arrays of nanoantennas impose abrupt phase jumps, making flat lenses, holograms, and beam steerers thinner than a wavelength."},
    {t: "Losses: The Central Challenge", b: "Metals absorb: plasmonic devices fight ohmic loss with gain media, hybrid designs, or alternative materials like nitrides."},
    {t: "Active and Tunable Plasmonics", b: "Carrier injection, phase-change materials, and liquid crystals tune resonances on the fly for switches and displays."},
    {t: "Plasmon-Enhanced Photovoltaics", b: "Nanoparticles trap light in thin solar cells, squeezing more absorption from less semiconductor."},
    {t: "From Lab to Product", b: "Reproducible nanofabrication, stable surface chemistry, and cost decide which plasmonic sensors reach the market."}
];
var PRINCIPLES=[
    {n: "Plasma frequency", e: "\u03c9p = \u221a(ne\u00b2/(m\u00b7\u03b5\u2080))", s: "A metal's free-electron density sets the frequency where it turns reflective."},
    {n: "Resonance condition", e: "Re[\u03b5_metal] = \u22122\u00b7\u03b5_medium", s: "A nanoparticle resonates when its permittivity is twice-negative the surroundings'."},
    {n: "Field enhancement", e: "|E|\u00b2/|E\u2080|\u00b2 up to 10\u00b3\u201310\u2074", s: "Plasmonic hotspots concentrate light intensity thousands-fold for sensing."}
];
var USES=["Designing label-free biosensors", "Building SERS diagnostic chips", "Engineering flat metalenses", "Enhancing thin-film solar cells"];
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
    id:id, t:tp.t, g:field, name:"Plasmonics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Plasmonics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-plasmonics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-plasmonics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-plasmonics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
