(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK115-";
var KIND="search method";
var TOOLNAME="Geospatial Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Haversine distance", "d": "Haversine computes great-circle distance between latitude/longitude points on a spherical Earth. The formula uses sines of half-differences, remaining numerically stable for nearby points. It is the default distance for 'near me' queries worldwide.", "c": "fundamentals", "r": 1, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "500", "POINTS": "{'NYC': (40.71, -74.0), 'Boston': (42.36, -71.06), 'LA': (34.05, -118.24)}"}}, {"t": "Bounding-box queries", "d": "A bounding box (min/max lat/lon) filters candidates with four cheap comparisons before any distance math. Boxes prune the vast majority of points; exact distance then ranks survivors. Every spatial index uses box filtering as its first pass.", "c": "algorithms", "r": 1, "p": {"QLAT": "41.0", "QLON": "-73.0", "RADIUS": "400", "POINTS": "{'A': (40.7, -74.0), 'B': (42.0, -72.0), 'C': (35.0, -120.0)}"}}, {"t": "R-tree spatial index", "d": "R-trees group nearby points into nested minimum bounding rectangles. Queries descend only branches whose rectangles intersect the search area. R-trees make spatial filtering logarithmic instead of linear.", "c": "implementation", "r": 1, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "300", "POINTS": "{'NYC': (40.71, -74.0), 'Philly': (39.95, -75.16), 'Miami': (25.76, -80.19)}"}}, {"t": "Geohash encoding", "d": "Geohash interleaves lat/lon bits into a base-32 string where shared prefixes mean nearby cells. Prefix length sets precision: longer strings, smaller cells. Geohashes turn 2-D proximity into 1-D prefix queries any database can serve.", "c": "optimization", "r": 1, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "600", "POINTS": "{'NYC': (40.71, -74.0), 'Boston': (42.36, -71.06), 'DC': (38.9, -77.04)}"}}, {"t": "K-nearest neighbors", "d": "KNN queries return the k closest points regardless of distance, answering 'the 5 nearest'. Best-first traversal of the spatial index expands the most promising branches first. KNN needs no radius guess, which users appreciate.", "c": "evaluation", "r": 1, "p": {"QLAT": "40.0", "QLON": "-75.0", "RADIUS": "10000", "POINTS": "{'A': (40.7, -74.0), 'B': (39.9, -75.2), 'C': (41.0, -74.5), 'D': (25.0, -80.0)}"}}, {"t": "Point-in-polygon tests", "d": "Ray casting counts boundary crossings: odd means inside, even means outside. It answers 'which district contains this address' for arbitrary polygons. Polygon tests power every geofencing system.", "c": "fundamentals", "r": 2, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "200", "POINTS": "{'inside': (40.71, -74.0), 'edge': (40.75, -73.99)}"}}, {"t": "Route and corridor search", "d": "Corridor queries find points within distance d of a polyline route. Each route segment becomes a capsule; points test against nearby segments via the spatial index. Corridor search answers 'what is along my drive'.", "c": "algorithms", "r": 2, "p": {"QLAT": "40.5", "QLON": "-74.2", "RADIUS": "150", "POINTS": "{'stop1': (40.71, -74.0), 'stop2': (40.3, -74.5)}"}}, {"t": "Spatial joins", "d": "Spatial joins pair records from two datasets by geometric predicates like WITHIN or INTERSECTS. Plane-sweep and index-nested-loop algorithms keep joins tractable. Joins connect, say, sensor readings to the districts containing them.", "c": "implementation", "r": 2, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "250", "POINTS": "{'s1': (40.71, -74.0), 's2': (40.8, -73.9)}"}}, {"t": "Coordinate reference systems", "d": "Coordinates are meaningless without their CRS; WGS84 (GPS) differs from local projected systems by meters to kilometers. Transforms reproject between systems before comparison. Mixing CRS silently is the classic geospatial bug.", "c": "optimization", "r": 2, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "500", "POINTS": "{'NYC': (40.71, -74.0), 'Albany': (42.65, -73.75)}"}}, {"t": "Reverse geocoding", "d": "Reverse geocoding turns coordinates into place names via point-in-polygon over administrative boundaries. Hierarchical lookup returns street, district, city, country in one pass. It is how apps label a raw GPS fix.", "c": "evaluation", "r": 2, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "100", "POINTS": "{'here': (40.71, -74.0)}"}}, {"t": "Temporal-spatial queries", "d": "Moving objects add time: queries ask 'where was it between 2 and 3pm' or 'which vehicles crossed this zone'. Trajectories index as space-time polylines with 3-D bounding boxes. Spatio-temporal indexes serve fleet and wildlife tracking.", "c": "fundamentals", "r": 3, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "300", "POINTS": "{'v1': (40.71, -74.0), 'v2': (41.0, -73.5)}"}}, {"t": "Density heatmaps", "d": "Heatmaps aggregate point density into grid cells for visualization. Kernel density estimation smooths counts so hotspots emerge. They turn millions of points into one glanceable image.", "c": "algorithms", "r": 3, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "800", "POINTS": "{'a': (40.71, -74.0), 'b': (40.72, -74.01), 'c': (34.0, -118.0)}"}}, {"t": "Geofencing alerts", "d": "Geofences trigger actions on polygon entry/exit, evaluated as streaming point-in-polygon tests. Indexing fences spatially keeps per-event checks cheap at fleet scale. Logistics and safety systems run on geofence events.", "c": "implementation", "r": 3, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "50", "POINTS": "{'truck': (40.71, -74.0)}"}}, {"t": "Map tile pyramids", "d": "Tile pyramids pre-render map zoom levels into 256px squares addressed by z/x/y. Clients fetch only visible tiles, caching aggressively. Pyramids are why web maps pan smoothly over planet-scale data.", "c": "optimization", "r": 3, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "500", "POINTS": "{'NYC': (40.71, -74.0), 'Boston': (42.36, -71.06)}"}}, {"t": "Privacy in location search", "d": "Location queries leak movement; k-anonymity and geo-indistinguishability add calibrated noise. Systems return areas instead of points when precision is not needed. Privacy-preserving geo search is mandatory for personal data.", "c": "evaluation", "r": 3, "p": {"QLAT": "40.7", "QLON": "-74.0", "RADIUS": "500", "POINTS": "{'u1': (40.71, -74.0), 'u2': (40.72, -74.02)}"}}];
var DEMO="# Geospatial search: haversine distance ranks points by true earth-surface distance.\nimport math\npoints = %%POINTS%%\ndef haversine(lat1, lon1, lat2, lon2):\n    R = 6371.0\n    p1, p2 = math.radians(lat1), math.radians(lat2)\n    dp = math.radians(lat2 - lat1); dl = math.radians(lon2 - lon1)\n    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2\n    return 2 * R * math.asin(math.sqrt(a))\nqlat, qlon, radius = %%QLAT%%, %%QLON%%, %%RADIUS%%\nprint(f\"Within {radius} km of ({qlat}, {qlon}):\")\nfor name, (la, lo) in points.items():\n    d = haversine(qlat, qlon, la, lo)\n    if d <= radius:\n        print(f\"  {name}: {d:.1f} km\")\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK115\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-geospatial-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-geospatial-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
