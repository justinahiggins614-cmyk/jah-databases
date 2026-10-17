(function(){'use strict';
/* JAH The Geospatial Operations Database generator — jahdb-geospatial-operations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GEOP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Coordinate Is - Foundations",
  "Geographic Versus Projected Coordinates - Foundations",
  "Distance on a Curved Earth - Foundations",
  "Coordinate Precision and Significant Digits - Foundations",
  "Map Projections and What They Preserve - Foundations",
  "Datums: Why Coordinates Move - Foundations",
  "Coordinate Reference Systems and the EPSG Registry - Foundations",
  "Vector Boundaries: Points, Lines, and Polygons - Foundations",
  "Terrain Basics: Elevation, Slope, and Aspect - Foundations"
 ],
 "Compounded": [
  "Proximity Queries: Near, Within, and K-Nearest - Compounded",
  "Spatial Joins: Points in Polygons at Scale - Compounded",
  "Geohashing: Location as a String - Compounded",
  "Spatial Indexes: Quadtrees and R-Trees - Compounded",
  "Hexagonal Grids and the H3 Index - Compounded",
  "Routing Algorithms: Dijkstra on Road Networks - Compounded",
  "Fast Routing: A-Star and Contraction Hierarchies - Compounded",
  "Map-Matching: Snapping GPS Tracks to Roads - Compounded",
  "GPS Error Budgets - Compounded",
  "Coordinate Transformations in Practice - Compounded",
  "Raster Operations: Map Algebra and Zonal Statistics - Compounded",
  "Isochrones and Service Areas - Compounded",
  "Geofencing: Enter, Dwell, and Exit - Compounded"
 ],
 "Advanced": [
  "Location Uncertainty: Error Ellipses and Confidence Regions - Advanced",
  "Kalman Filtering for Moving Positions - Advanced",
  "Spatial Query Patterns at Scale - Advanced",
  "Terrain Analysis: Viewsheds and Watersheds - Advanced",
  "Constrained Network Routing: Turns and Transfers - Advanced",
  "Projection Math: Forward, Inverse, and Scale Factor - Advanced",
  "Trajectory Analysis: Stays, Segments, and Similarity - Advanced",
  "Propagating Uncertainty Through Spatial Operations - Advanced",
  "Time-Dependent Coordinates: ITRF and Plate Motion - Advanced",
  "Spatial Data Quality and Fitness for Use - Advanced",
  "Real-Time Geospatial Pipelines - Advanced",
  "The Geospatial Operations Playbook - Advanced"
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
var gen={version:'jahdb-geospatial-operations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('geospatial-operations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
