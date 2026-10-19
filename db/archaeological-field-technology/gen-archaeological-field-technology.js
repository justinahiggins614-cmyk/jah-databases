(function(){'use strict';
/* JAH Archaeological Field Technology Database generator — jahdb-archaeological-field-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AFT-";
var FIELDS=["remote sensing", "geophysics", "dating", "excavation", "digital recording", "analysis"];
var TOPICS=[
    {t: "Aerial Archaeology", b: "Crop marks, soil marks, and shadow marks: the view from above revealing buried landscapes."},
    {t: "LiDAR", b: "Laser pulses stripping forest canopy digitally: the Maya lowlands' cities revealed in a decade."},
    {t: "Satellite Imagery", b: "Multispectral detection of tells, roads, and looting: monitoring heritage from orbit."},
    {t: "Magnetometry", b: "Hearths, kilns, and ditches disturb Earth's field: mapping settlements without turning soil."},
    {t: "Ground-Penetrating Radar", b: "Radar pulses imaging buried walls and voids: the 3-D view before excavation."},
    {t: "Resistivity and EM", b: "Soil moisture contrasts mapping ditches and walls: the complementary geophysics."},
    {t: "Radiocarbon Dating", b: "\u00b9\u2074C decay dating organic material to ~50,000 years: calibration curves (IntCal) correcting atmospheric wiggles."},
    {t: "Dendrochronology", b: "Tree rings dating wood to the year: the gold standard where timbers survive."},
    {t: "OSL and TL Dating", b: "Trapped electrons dating when sediments last saw sunlight or ceramics were fired: beyond radiocarbon's reach."},
    {t: "Excavation Method", b: "Stratigraphy, Harris matrix, single-context recording: the disciplined destruction of the record."},
    {t: "Digital Recording", b: "Photogrammetry, total stations, GIS: the paperless trench producing 3-D archives."},
    {t: "Ethics and Repatriation", b: "Descendant communities, permits, and the SAA principles: the responsibilities framing every project."}
];
var PRINCIPLES=[
    {n: "Non-destructive first", e: "", s: "Survey before you dig: remote sensing and geophysics map sites excavation would destroy."},
    {n: "Context is everything", e: "", s: "An artifact without its provenience is a curiosity: recording position and association is the science."},
    {n: "Multiple methods converge", e: "", s: "No single technique dates or maps alone: independent methods cross-checking is the standard."}
];
var USES=["Planning geophysical surveys", "Dating archaeological finds", "Recording excavations digitally", "Interpreting remote-sensing data"];
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
    id:id, t:tp.t, g:field, name:"Archaeological Field Technology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Archaeological Tech Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-archaeological-field-technology-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-archaeological-field-technology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archaeological-field-technology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
