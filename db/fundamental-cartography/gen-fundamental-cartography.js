(function(){'use strict';
/* JAH Fundamentals of Cartography Database generator — jahdb-fundamental-cartography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CAR-";
var FIELDS=["map projections", "symbology", "generalization", "thematic maps", "GIS", "map design"];
var TOPICS=[
    {t: "What Maps Do", b: "Maps are selective, symbolic abstractions of space: they answer where, what, and how much \u2014 never neutral, always designed."},
    {t: "Scale and Generalization", b: "Large scale shows detail, small scale shows patterns; generalization (selection, simplification, exaggeration) bridges them honestly."},
    {t: "Projections: Flattening Earth", b: "No projection preserves everything: Mercator keeps direction (navigation), equal-area keeps size (thematic), compromise keeps looks."},
    {t: "Coordinate Systems", b: "Latitude/longitude, UTM, and state plane systems locate points; datums (WGS84, NAD83) anchor coordinates to Earth's actual shape."},
    {t: "Bertin's Visual Variables", b: "Position, size, value, texture, color, orientation, shape: the grammar for turning data into map symbols that read correctly."},
    {t: "Choropleth Maps", b: "Shaded areas show rates \u2014 but class breaks (quantile, natural breaks, equal interval) reshape the story the same data tells."},
    {t: "Proportional Symbols and Dot Density", b: "Sized circles show totals, dots show distributions: match the symbol to the data's measurement level."},
    {t: "Color in Maps", b: "Sequential schemes for ordered data, diverging for two-ended, qualitative for categories \u2014 ColorBrewer codified the craft."},
    {t: "Typography on Maps", b: "Type placement (labels follow features, hierarchy by size) is half of map legibility \u2014 the most underrated cartographic skill."},
    {t: "GIS: Maps as Databases", b: "Geographic information systems store geometry plus attributes, enabling spatial analysis no paper map could do."},
    {t: "Web Maps and Tiles", b: "Slippy-map pyramids (zoom levels, vector tiles) deliver planetary data to phones \u2014 cartography at internet scale."},
    {t: "Map Ethics and Truth", b: "Projections, classifications, and omissions persuade: cartographers disclose choices because maps make arguments."}
];
var PRINCIPLES=[
    {n: "Projection trade-off", e: "no flat map preserves all", s: "Area, shape, distance, direction \u2014 every projection sacrifices at least one; choose by purpose."},
    {n: "Visual variables (Bertin)", e: "position, size, value, texture, color, orientation, shape", s: "Seven visual channels encode data; position is strongest, color hue weakest for quantities."},
    {n: "Generalization operators", e: "select, simplify, smooth, displace", s: "Smaller scales demand omitting, merging, and exaggerating \u2014 principled simplification."}
];
var USES=["Designing thematic data maps", "Choosing map projections", "Building web map applications", "Teaching spatial literacy"];
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
    id:id, t:tp.t, g:field, name:"Cartography"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Cartography demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-cartography-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-cartography-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-cartography",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
