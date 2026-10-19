(function(){'use strict';
/* JAH Fundamentals of Color Science Database generator — jahdb-fundamental-color-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CS-";
var FIELDS=["light and vision", "color matching", "color spaces", "color measurement", "color reproduction", "color appearance"];
var TOPICS=[
    {t: "Light and the Eye", b: "Color begins with spectra: objects reflect some wavelengths and absorb others, and the eye's three cone types sample the result."},
    {t: "Trichromatic Vision", b: "Red, green, and blue cones overlap in sensitivity; the brain compares their signals to construct every hue we perceive."},
    {t: "Color Matching Experiments", b: "Matching any test color with three primaries yields color-matching functions \u2014 the experimental foundation of all colorimetry."},
    {t: "The CIE 1931 System", b: "The XYZ color space maps every human-visible color to coordinates, with the famous horseshoe chromaticity diagram as its 2-D projection."},
    {t: "RGB and Device Color", b: "Screens emit RGB mixtures; cameras capture them \u2014 but device RGB is meaningless without a profile tying it to XYZ."},
    {t: "CMYK and Printing", b: "Printers subtract with cyan, magenta, yellow (plus black): inks absorb wavelengths, the inverse physics of emissive displays."},
    {t: "CIELAB and Perceptual Uniformity", b: "Lab space warps coordinates so equal distances mean equal perceived differences \u2014 essential for quality control."},
    {t: "Delta-E: Measuring Difference", b: "\u0394E numbers quantify 'how different do these colors look' \u2014 under ~1.0 is imperceptible, over 3 is obvious to most viewers."},
    {t: "White Points and Adaptation", b: "The eye adapts to the illuminant (D65 daylight vs tungsten); white balance is cameras imitating that adaptation."},
    {t: "Gamut: What Can Be Shown", b: "Every device reproduces only a gamut subset of visible color; wide-gamut displays and printers expand it at real cost."},
    {t: "Color Appearance Phenomena", b: "Simultaneous contrast, afterimages, and chromatic adaptation prove color is a brain construction, not a property of light alone."},
    {t: "Color Management Workflow", b: "Profiles, rendering intents, and calibration chain devices together so a photo looks the same from camera to screen to print."}
];
var PRINCIPLES=[
    {n: "Trichromacy", e: "any color = r\u00b7R + g\u00b7G + b\u00b7B", s: "Three primaries match any visible color for the standard observer \u2014 the basis of all screens."},
    {n: "CIE XYZ (1931)", e: "X,Y,Z from color-matching functions", s: "The master color space: every visible color is a coordinate triple."},
    {n: "Delta-E", e: "\u0394E*ab = \u221a((\u0394L*)\u00b2+(\u0394a*)\u00b2+(\u0394b*)\u00b2)", s: "Perceptual color difference as Euclidean distance in CIELAB."}
];
var USES=["Calibrating monitors and printers", "Matching brand colors in manufacturing", "Grading film and photography", "Designing accessible color palettes"];
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
    id:id, t:tp.t, g:field, name:"Color Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Color Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-color-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-color-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-color-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
