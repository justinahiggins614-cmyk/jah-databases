(function(){'use strict';
/* JAH Fundamentals of Photonics Database generator — jahdb-fundamental-photonics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PHO-";
var FIELDS=["waveguides", "lasers", "modulators", "photodetectors", "fiber optics", "photonic integration"];
var TOPICS=[
    {t: "Photonics Defined", b: "Photonics is electronics with photons: generating, guiding, modulating, and detecting light to carry information and energy."},
    {t: "Waveguides", b: "High-index cores trap light by total internal reflection; single-mode guides carry one clean spatial mode for communications."},
    {t: "Laser Physics", b: "Population inversion plus a resonant cavity turns spontaneous emission into coherent stimulated avalanches \u2014 threshold, modes, and linewidth follow."},
    {t: "Semiconductor Lasers", b: "Diode lasers (VCSELs, DFBs) are the workhorses: tiny, efficient, directly modulatable \u2014 they light the internet's fiber."},
    {t: "LEDs vs Lasers", b: "LEDs emit incoherent spontaneous light cheaply; lasers add coherence for distance, speed, and focus \u2014 different physics, different jobs."},
    {t: "Modulators", b: "Electro-optic and electro-absorption modulators impress data onto light at tens of gigabaud without touching the laser itself."},
    {t: "Photodetectors", b: "PIN diodes and avalanche photodiodes convert photons to current; bandwidth, responsivity, and noise set receiver sensitivity."},
    {t: "Optical Fiber", b: "Silica fiber loses under 0.2 dB/km at 1550 nm \u2014 the transparency window that makes transoceanic light-speed links possible."},
    {t: "Wavelength-Division Multiplexing", b: "Dozens of colors share one fiber, each an independent channel: WDM multiplied fiber capacity a thousandfold."},
    {t: "Optical Amplifiers", b: "Erbium-doped fiber amplifiers boost all wavelengths at once, removing the need for electronic regeneration every 80 km."},
    {t: "Photonic Integrated Circuits", b: "Waveguides, modulators, and detectors on one chip (silicon photonics) promise optical interconnects inside data centers and computers."},
    {t: "Nonlinear and Quantum Photonics", b: "Intense light changes its own medium (switching, frequency conversion); single photons enable quantum-secure communication."}
];
var PRINCIPLES=[
    {n: "Total internal reflection", e: "\u03b8 > \u03b8c = asin(n2/n1)", s: "Light striking the core-cladding boundary beyond the critical angle is perfectly guided."},
    {n: "Laser threshold", e: "gain = loss", s: "Lasing begins exactly when stimulated-emission gain overcomes all cavity losses."},
    {n: "Responsivity", e: "R = \u03b7\u00b7q/(h\u03bd)", s: "A photodetector's amps-per-watt follows from quantum efficiency and photon energy."}
];
var USES=["Designing fiber-optic links", "Specifying laser diode sources", "Building WDM transport networks", "Integrating silicon-photonic transceivers"];
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
    id:id, t:tp.t, g:field, name:"Photonics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Photonics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-photonics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-photonics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-photonics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
