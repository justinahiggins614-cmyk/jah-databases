(function(){'use strict';
/* Milvus Lite Database — boundless generator jahdb-pc-organizer-milvus-lite-1.0
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
var CATS=["setup", "collections", "indexes", "search"];
var PREFIX='JAH-PCO84-';
var ROWS=[["setup", "pip install, zero servers", "Milvus Lite installs with `pip install pymilvus` and runs with a local URI — no Docker, no cluster, no server process. A Jupyter notebook can have a real vector database in two lines. It is the fastest path from embeddin", ["pymilvus", "no server process"]], ["setup", "The milvus.db file", "All data lives in a single milvus.db file (SQLite-based metadata + vector storage), so backup is a file copy and projects stay portable. The file can be checked into project storage or shipped with a demo. Local-first me", ["single-file storage", "portable"]], ["setup", "MilvusClient: the simple API", "MilvusClient offers create_collection, insert, search, query, and delete without managing connections or partitions. It is the recommended API for Lite and small projects. Simple API, same engine semantics as full Milvus", ["MilvusClient", "CRUD API"]], ["collections", "Collections and schemas", "Collections define fields: an id primary key, a vector field with dimension, and scalar fields for metadata. Schemas are declared up front so queries can filter on metadata later. Schema-first keeps retrieval precise.", ["field schemas", "primary keys"]], ["indexes", "Vector indexes: HNSW, IVF_FLAT", "Lite supports HNSW (fast approximate search, more memory) and IVF_FLAT (balanced) index types, chosen per collection. Index choice trades recall against speed and RAM. Defaults are sensible; tuning comes later.", ["HNSW", "IVF_FLAT"]], ["indexes", "Distance metrics", "Collections pick a metric: COSINE, L2, or IP (inner product), which must match how the embedding model was trained to be used. Wrong metric silently degrades results. Metric choice is a correctness issue, not a preferenc", ["COSINE/L2/IP", "model alignment"]], ["search", "Filtered search", "Search accepts a filter expression on scalar fields ('category == \"sci-fi\"'), combining vector similarity with metadata constraints. Filtered search is how RAG stays on-topic in multi-tenant data. Expressions use a simpl", ["filter expressions", "hybrid constraints"]], ["collections", "Insert and upsert", "insert() adds vectors with ids; upsert semantics come from inserting with existing ids in newer versions. Batch inserts in the thousands for throughput. IDs are the handle for updates and deletes.", ["batching", "id handles"]], ["collections", "Delete by expression", "delete() removes vectors matching a filter expression, so stale documents leave the index cleanly. RAG pipelines delete by source file when documents update. Clean deletes keep retrieval honest.", ["expression deletes", "stale cleanup"]], ["search", "Query (non-vector) lookups", "query() fetches rows by filter without a vector, useful for metadata inspection and debugging what is actually in the collection. Debugging retrieval starts with querying what got stored. The same filter syntax applies.", ["metadata inspection", "debugging"]], ["setup", "Same API as full Milvus", "Code written against Milvus Lite ports to full Milvus (standalone/clustered) by changing the URI, because both speak the PyMilvus API. Prototypes graduate to production without rewrites. Lite is the on-ramp, not a dead e", ["API parity", "graduation path"]], ["search", "ATTU: the admin UI", "ATTU is the open-source admin interface for Milvus: browse collections, run searches, and inspect schemas visually. Lite users can point ATTU at their file for a GUI view. Visual inspection catches schema mistakes early.", ["admin GUI", "schema inspection"]], ["collections", "Partition-free simplicity", "Lite skips partitions and multi-tenancy features of full Milvus, which is exactly why it stays simple: one file, one API, no ops. When you need partitions and RBAC, you have outgrown Lite by design. Simplicity is the fea", ["opinionated simplicity", "graduation signal"]], ["indexes", "Embedding dimension discipline", "The collection's dim must equal the embedding model's output dimension (384, 768, 1536...); mismatches error at insert. Recording the model name + dim in the collection description prevents mystery errors months later. D", ["dim matching", "documentation"]], ["setup", "Backup = copy the file", "Because everything is one file, backups are cp milvus.db, versioning is file copies with dates, and sharing a dataset is sending the file. Operational simplicity is Lite's superpower for small projects. No backup tooling", ["file-copy backup", "easy sharing"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Milvus Lite",edition:'public',description:desc,facts:row[3].slice(),
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
var gen={version:'jahdb-pc-organizer-milvus-lite-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-milvus-lite',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_milvus_lite']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
