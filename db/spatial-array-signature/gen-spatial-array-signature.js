(function(){'use strict';
/* JAH The Spatial Array Signature Database generator — jahdb-spatial-array-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPARS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature TileDB Engine",
  "Signature PostGIS Engine",
  "Signature Rasdaman Engine",
  "Signature SciDB Engine",
  "Signature Apache Sedona Engine",
  "Signature GeoMesa Engine",
  "Signature MobilityDB Engine",
  "Signature DuckDB Spatial Engine",
  "Signature Zarr Engine",
  "Signature GeoWave Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: tiled squares, circles of inclusion\n" +
   "CELL = 5\n" +
   "tiles = {}\n" +
   "def tile(pt): return (int(pt[0] // CELL), int(pt[1] // CELL))\n" +
   "for name_, pt in [(\"a\", (1, 2)), (\"b\", (6, 1)), (\"c\", (2, 7))]:\n" +
   "    tiles.setdefault(tile(pt), []).append(name_)\n" +
   "print(\"square tiles:\", tiles)\n" +
   "import math\n" +
   "def circle(center, r, pts):\n" +
   "    return [n for n, p in pts.items() if math.hypot(p[0]-center[0], p[1]-center[1]) <= r]\n" +
   "print(\"circle of inclusion r=5:\", circle((0, 0), 5, {\"a\": (1, 2), \"b\": (6, 1), \"c\": (2, 7)}))\n" +
   "print(\"Space tiled in squares from the Signature-One origin; regions are circles.\")\n" +
   "\n";
  return tpl.split('__TOPIC__').join(safe);
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — electronics diagnostic record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A electronics diagnostic record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-spatial-array-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('spatial-array-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
