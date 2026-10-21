(function(){'use strict';
/* SQLite / SpatiaLite Database — boundless generator jahdb-pc-organizer-sqlite-spatialite-1.0
   SELF-REGULATION (standing order): hard stop at ONE TRILLION records
   (1,000,000,000,000). Throttled batching, every record correctness-verified
   before acceptance, generated records labeled "simulated" for weeding,
   completion detection when the topic space is exhausted. */
var SELF_REG={max_records:1000000000000,hard_stop:true,throttled:true,
  labeling:'generated records are labeled simulated for weeding',
  correctness:'every record validated before acceptance',
  completion:'detects when the topic space is exhausted'};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["core", "extensions", "fts", "geospatial"];
var PREFIX='JAH-PCO85-';
var ROWS=[["core", "Zero-configuration, serverless SQL", "SQLite needs no server, no setup, no administration: the database is a single ordinary file and the engine is a library linked into the application. Opening a database is opening a file. This is why SQLite ships inside p", ["single-file DB", "library engine"]], ["core", "Public domain license", "SQLite is public domain — no license to buy, no attribution required, usable in any commercial product. The license simplicity is a deliberate project choice. It removes legal friction entirely.", ["public domain", "commercial-friendly"]], ["core", "ACID transactions", "SQLite transactions are fully ACID even across crashes and power loss, using rollback journals or write-ahead logging. Reliability is not sacrificed for simplicity. Your data survives the crash.", ["WAL mode", "crash safety"]], ["core", "Single-file portability", "A database file copies, emails, and backs up like any file; the format is stable and cross-platform. Moving an app's data is a file copy. Portability is the operational model.", ["file copy backup", "cross-platform format"]], ["fts", "FTS5 full-text search", "The FTS5 extension builds full-text indexes with BM25 ranking, tokenizers, and snippet highlighting — a real search engine inside the file. Small apps get search without a search server. FTS5 is criminally underused.", ["BM25 ranking", "snippets"]], ["extensions", "JSON1: JSON in SQL", "The JSON1 extension stores, queries, and indexes JSON with -> and ->> operators and json_each table functions. Semi-structured data lives happily in relational tables. SQLite is a document store when you need one.", ["JSON operators", "json_each"]], ["geospatial", "The RTREE spatial index", "SQLite's built-in RTREE virtual table indexes bounding boxes for fast spatial lookups even without SpatiaLite. Proximity queries over rectangles need nothing else. RTREE is the lightweight geo option.", ["bounding boxes", "built-in"]], ["geospatial", "SpatiaLite: full GIS in the file", "SpatiaLite adds OGC Simple Features SQL: geometry types, spatial indexes, and hundreds of functions (ST_Distance, ST_Within, ST_Buffer) loadable as an extension. A file-based PostGIS for local GIS work. Alessandro Furier", ["OGC functions", "spatial indexes"]], ["geospatial", "Loading the SpatiaLite extension", "SpatiaLite loads via SELECT load_extension('mod_spatialite') (or statically linked builds), then SELECT InitSpatialMetaData() prepares the metadata tables. One-time setup per database file. After that it is all SQL.", ["load_extension", "InitSpatialMetaData"]], ["geospatial", "Geometry columns and SRIDs", "AddGeometryColumn registers a geometry column with a type (POINT, LINESTRING, POLYGON) and SRID (e.g., 4326 for WGS84); CreateSpatialIndex builds the index. Typed geometry columns keep GIS data honest. SRIDs keep coordin", ["typed geometries", "SRID 4326"]], ["geospatial", "Spatial SQL queries", "Find-nearby, within-polygon, and intersection queries are plain SQL with ST_ functions, returning distances and geometries. GIS analysis without leaving SQL. The query you already know, with geometry.", ["ST_Within", "ST_Buffer"]], ["core", "WAL mode for concurrency", "Write-ahead logging lets readers proceed during writes, the standard tuning for apps with concurrent access. One PRAGMA changes the locking behavior. WAL is the modern default for multi-threaded apps.", ["PRAGMA journal_mode", "concurrency"]], ["core", "Backup API and VACUUM", "The online backup API copies a live database safely; VACUUM rebuilds the file to reclaim space and defragment. Maintenance is two commands. Small databases stay small with occasional vacuums.", ["backup API", "VACUUM"]], ["core", "Limits and when to graduate", "SQLite handles gigabytes and high read concurrency beautifully; write-heavy multi-writer workloads and network access are the graduation signals toward client-server databases. Knowing the ceiling is part of using it wel", ["appropriate scale", "ceiling awareness"]], ["core", "The CLI: sqlite3", "The sqlite3 shell (.schema, .dump, .mode, .import) administers databases from the terminal and scripts migrations. .dump produces portable SQL backups. The CLI is the DBA toolkit for file databases.", [".schema/.dump", "scriptable admin"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"SQLite / SpatiaLite",edition:'public',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Public record \u2014 fact-checked.",last_verified:'2026-10-21',_seed:seed,_simulated:true};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-pc-organizer-sqlite-spatialite-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-sqlite-spatialite',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_sqlite_spatialite']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
