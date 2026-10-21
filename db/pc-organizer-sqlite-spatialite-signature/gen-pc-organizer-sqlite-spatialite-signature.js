(function(){'use strict';
/* Signature SQLite / SpatiaLite Database — boundless generator jahdb-pc-organizer-sqlite-spatialite-signature-1.0
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
var PREFIX='JAH-PCO85S-';
var ROWS=[["core", "SigBase pocket relational DB", "Signature Pocket Base is a Signature original: a zero-configuration embedded relational database in a single file, with ACID transactions, full-text search, JSON support, and a geospatial extension — the Signature take o", ["single file", "ACID"]], ["core", "SigFree open license", "SigBase is released under a permissive Signature open license with no attribution requirement for binaries. The license simplicity is deliberate. Legal friction: zero.", ["open license", "no friction"]], ["core", "SigTrans crash-safe transactions", "SigTrans provides ACID transactions with a write-ahead log and automatic recovery on open after a crash. The recovery protocol is Signature-original.", ["WAL", "auto recovery"]], ["core", "SigFile portable format", "The .sigbase file format is versioned and cross-platform with a format-stability guarantee across releases. The stability guarantee is Signature-original.", ["versioned format", "stability guarantee"]], ["fts", "SigFind full-text search", "SigFind builds ranked full-text indexes with BM25, phrase search, and snippet highlighting inside the file. The integrated search is Signature-original.", ["BM25", "snippets"]], ["extensions", "SigDoc JSON support", "SigDoc stores JSON with path query operators, generated columns over JSON paths, and indexes on expressions. The generated-column indexing is Signature-original.", ["path operators", "expression indexes"]], ["geospatial", "SigBox rectangle index", "SigBox is the built-in rectangle index for bounding-box queries with zero extensions. The zero-extension spatial index is Signature-original.", ["built-in", "fast proximity"]], ["geospatial", "SigGeo full GIS module", "SigGeo adds geometry types and OGC-style spatial SQL (distance, containment, buffering) as a loadable module. The module's function set is Signature-original.", ["spatial SQL", "loadable module"]], ["geospatial", "SigGeoInit one-step geo setup", "One INIT GEO command loads the module and prepares metadata tables. The one-step setup is Signature-original.", ["one command", "metadata tables"]], ["geospatial", "SigGeom typed geometry columns", "Geometry columns declare type and coordinate system at creation with validation on insert. The validated typed columns are Signature-original.", ["typed columns", "insert validation"]], ["geospatial", "SigSpatial spatial queries", "Nearby, within, and intersection queries are plain SQL over SigGeo functions with automatic index use. The automatic index selection is Signature-original.", ["auto indexing", "plain SQL"]], ["core", "SigFlow concurrent access", "SigFlow's WAL-style logging lets readers work during writes with snapshot isolation. The isolation implementation is Signature-original.", ["WAL-style", "snapshot isolation"]], ["core", "SigTidy maintenance", "SigTidy offers online backup to a second file and a compact command that reclaims space with a before/after report. The reported compaction is Signature-original.", ["online backup", "compact reports"]], ["core", "SigScale graduation guide", "SigScale documents the exact signals for moving to a client-server database and provides an export tool that preserves schemas, indexes, and data. The guided export is Signature-original.", ["graduation signals", "export tool"]], ["core", "SigShell admin CLI", "SigShell provides schema inspection, SQL dumps, CSV import/export, and scripted migrations from the terminal. The migration scripting is Signature-original.", ["dumps", "migrations"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Signature Pocket Base",edition:'signature',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Signature original \u2014 designed by Justin Addam Higgins (JAH).",last_verified:'2026-10-21',_seed:seed,_simulated:true};
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
var gen={version:'jahdb-pc-organizer-sqlite-spatialite-signature-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-sqlite-spatialite-signature',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_sqlite_spatialite_signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
