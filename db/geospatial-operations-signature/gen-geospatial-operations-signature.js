(function(){'use strict';
/* JAH The Geospatial Operations Signature Database generator — jahdb-geospatial-operations-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GEOPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Coordinate Is (Signature Edition) - Foundations",
  "Geographic Versus Projected Coordinates (Signature Edition) - Foundations",
  "Distance on a Curved Earth (Signature Edition) - Foundations",
  "Coordinate Precision and Significant Digits (Signature Edition) - Foundations",
  "Map Projections and What They Preserve (Signature Edition) - Foundations",
  "Datums: Why Coordinates Move (Signature Edition) - Foundations",
  "Coordinate Reference Systems and the EPSG Registry (Signature Edition) - Foundations",
  "Vector Boundaries: Points, Lines, and Polygons (Signature Edition) - Foundations",
  "Terrain Basics: Elevation, Slope, and Aspect (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Proximity Queries: Near, Within, and K-Nearest (Signature Edition) - Compounded",
  "Spatial Joins: Points in Polygons at Scale (Signature Edition) - Compounded",
  "Geohashing: Location as a String (Signature Edition) - Compounded",
  "Spatial Indexes: Quadtrees and R-Trees (Signature Edition) - Compounded",
  "Hexagonal Grids and the H3 Index (Signature Edition) - Compounded",
  "Routing Algorithms: Dijkstra on Road Networks (Signature Edition) - Compounded",
  "Fast Routing: A-Star and Contraction Hierarchies (Signature Edition) - Compounded",
  "Map-Matching: Snapping GPS Tracks to Roads (Signature Edition) - Compounded",
  "GPS Error Budgets (Signature Edition) - Compounded",
  "Coordinate Transformations in Practice (Signature Edition) - Compounded",
  "Raster Operations: Map Algebra and Zonal Statistics (Signature Edition) - Compounded",
  "Isochrones and Service Areas (Signature Edition) - Compounded",
  "Geofencing: Enter, Dwell, and Exit (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Location Uncertainty: Error Ellipses and Confidence Regions (Signature Edition) - Advanced",
  "Kalman Filtering for Moving Positions (Signature Edition) - Advanced",
  "Spatial Query Patterns at Scale (Signature Edition) - Advanced",
  "Terrain Analysis: Viewsheds and Watersheds (Signature Edition) - Advanced",
  "Constrained Network Routing: Turns and Transfers (Signature Edition) - Advanced",
  "Projection Math: Forward, Inverse, and Scale Factor (Signature Edition) - Advanced",
  "Trajectory Analysis: Stays, Segments, and Similarity (Signature Edition) - Advanced",
  "Propagating Uncertainty Through Spatial Operations (Signature Edition) - Advanced",
  "Time-Dependent Coordinates: ITRF and Plate Motion (Signature Edition) - Advanced",
  "Spatial Data Quality and Fitness for Use (Signature Edition) - Advanced",
  "Real-Time Geospatial Pipelines (Signature Edition) - Advanced",
  "The Geospatial Operations Playbook (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Geospatial Operations Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — geospatial operations record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A geospatial operations record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"geospatial-operations-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-geospatial-operations-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('geospatial-operations-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
