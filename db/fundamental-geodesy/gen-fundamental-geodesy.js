(function(){'use strict';
/* JAH Fundamentals of Geodesy Database generator — jahdb-fundamental-geodesy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GEO-";
var FIELDS=["Earth's shape", "datums", "gravity field", "satellite geodesy", "height systems", "reference frames"];
var TOPICS=[
    {t: "What Geodesy Measures", b: "Geodesy determines Earth's shape, orientation, and gravity field \u2014 the foundation every map, GPS fix, and construction survey stands on."},
    {t: "The Ellipsoid", b: "An oblate spheroid (flattened ~1/298) models mean sea level mathematically; WGS84's ellipsoid is the world's coordinate anchor."},
    {t: "The Geoid", b: "The true equipotential surface of gravity \u2014 lumpy by \u00b1100 m from mass anomalies \u2014 is what 'sea level' actually means."},
    {t: "Datums: Anchoring Coordinates", b: "A datum ties coordinates to Earth: horizontal datums fix latitude/longitude, vertical datums fix heights \u2014 mismatched datums shift positions meters."},
    {t: "Gravity Measurement", b: "Absolute and relative gravimeters map g to microgal precision, revealing oil, aquifers, and magma by their mass."},
    {t: "Satellite Laser Ranging", b: "Bouncing lasers off retroreflector satellites measures station positions to millimeters \u2014 tracking continental drift directly."},
    {t: "VLBI: Quasars as Anchors", b: "Very-long-baseline interferometry uses distant quasars as fixed points to measure Earth's rotation and plate motion."},
    {t: "How GPS/GNSS Works", b: "Satellites broadcast precise time; receivers trilaterate from signal travel times, solving position plus clock bias from four satellites."},
    {t: "Differential and RTK Positioning", b: "Reference stations cancel atmospheric errors, taking GNSS from meters to centimeters \u2014 the precision behind machine guidance."},
    {t: "Height Systems", b: "Ellipsoid, orthometric, and dynamic heights differ by the geoid: engineers must know which 'elevation' a number means."},
    {t: "Reference Frames in Motion", b: "Plates move centimeters per year, so coordinates need epochs: ITRF tracks stations through time, not just space."},
    {t: "Geodesy in Practice", b: "Bridge alignment, dam monitoring, sea-level tracking, and autonomous navigation all consume geodetic products daily."}
];
var PRINCIPLES=[
    {n: "Reference ellipsoid", e: "WGS84: a = 6378137 m, 1/f = 298.257", s: "A mathematical ellipsoid approximates sea level for coordinates worldwide."},
    {n: "Geoid undulation", e: "h = H + N", s: "Ellipsoid height equals orthometric (sea-level) height plus the geoid separation."},
    {n: "GNSS trilateration", e: "4 satellites \u2192 3-D + clock", s: "Four ranging signals solve for position and receiver clock error simultaneously."}
];
var USES=["Establishing survey control networks", "Enabling precision agriculture guidance", "Monitoring dam and bridge deformation", "Tracking sea-level rise"];
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
    id:id, t:tp.t, g:field, name:"Geodesy"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Geodesy demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-geodesy-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-geodesy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-geodesy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
