(function(){'use strict';
/* JAH Fundamentals of Optics Database generator — jahdb-fundamental-optics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OPT-";
var FIELDS=["geometrical optics", "lenses and mirrors", "wave optics", "interference", "diffraction", "polarization"];
var TOPICS=[
    {t: "Light as Ray and Wave", b: "Geometrical optics treats light as straight-line rays for mirrors and lenses; wave optics is needed for interference, diffraction, and color."},
    {t: "Reflection and Mirrors", b: "The law of reflection (angle in equals angle out) makes plane mirrors form same-size virtual images; curved mirrors focus or spread rays by their geometry."},
    {t: "Refraction and Snell's Law", b: "Light bends entering glass or water because it slows down; the index of refraction n = c/v quantifies the slowdown (about 1.5 for glass)."},
    {t: "Total Internal Reflection", b: "Beyond the critical angle, light cannot leave a dense medium at all \u2014 the principle behind fiber optics and sparkling diamonds."},
    {t: "Lenses and Image Formation", b: "Converging lenses focus parallel rays to a focal point; the thin-lens equation predicts exactly where real or virtual images form."},
    {t: "The Human Eye", b: "The eye is a living camera: cornea and lens focus light on the retina, the iris adjusts aperture, and rods and cones convert photons to neural signals."},
    {t: "Interference of Light", b: "Thomas Young's double slit proved light is a wave: overlapping wavefronts create alternating bright and dark fringes from path differences."},
    {t: "Diffraction and Resolution", b: "Light spreads through small openings, setting the diffraction limit: no lens can resolve details much smaller than the wavelength it uses."},
    {t: "Polarization", b: "Light waves oscillate in planes; polarizing filters pass one plane only \u2014 used in sunglasses, LCD screens, and stress analysis."},
    {t: "Color and Dispersion", b: "A prism spreads white light because refractive index varies with wavelength; the eye builds all color from three cone types (red, green, blue)."},
    {t: "Optical Instruments", b: "Telescopes magnify distant angles, microscopes magnify tiny objects \u2014 both are cascades of objective and eyepiece lenses managing real intermediate images."},
    {t: "Lasers and Coherence", b: "Lasers emit coherent, single-wavelength light via stimulated emission, enabling precise measurement, cutting, and fiber communication."}
];
var PRINCIPLES=[
    {n: "Snell's law", e: "n1 * sin(\u03b81) = n2 * sin(\u03b82)", s: "A ray crossing into a new medium bends by the ratio of refractive indices."},
    {n: "Thin-lens equation", e: "1/f = 1/do + 1/di", s: "Focal length links object and image distances for an ideal thin lens."},
    {n: "Double-slit interference", e: "d * sin(\u03b8) = m * \u03bb", s: "Bright fringes appear where path differences equal whole wavelengths."}
];
var USES=["Designing camera and telescope lenses", "Building fiber-optic communication links", "Correcting vision with glasses and contacts", "Running laser measurement and cutting tools"];
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
    id:id, t:tp.t, g:field, name:"Optics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Optics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-optics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-optics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-optics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
