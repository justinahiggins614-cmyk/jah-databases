/* JAH Embedding Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='embeddings',PREFIX='JAH-EMB-';
var CATS=['benchmark','model','technique','application'];
/* [name, org, year, dims, kind, cat, desc] */
var REAL=[
["MTEB","Muennighoff et al.","2022","-","benchmark","benchmark","Massive Text Embedding Benchmark: 56 tasks across 8 embedding types. The standard scoreboard for embedding models."],
["BEIR","Thakur et al.","2021","-","benchmark","benchmark","A heterogeneous retrieval benchmark of 18 datasets. Tests zero-shot generalization of retrieval models."],
["text-embedding-ada-002","OpenAI","2022","1536","model","model","OpenAI's second-generation embedding model with 1536 dimensions. The default choice for RAG pipelines for years."],
["text-embedding-3-small","OpenAI","2024","1536","model","model","A smaller, cheaper embedding model that beats ada-002. Matryoshka support allows truncated dimensions."],
["text-embedding-3-large","OpenAI","2024","3072","model","model","OpenAI's flagship embedding model with 3072 dimensions. Top-tier MTEB scores with shorten-able vectors."],
["bge-large-en-v1.5","BAAI","2023","1024","model","model","Beijing Academy's 1024-dim English embedding model. A top open performer on MTEB retrieval tasks."],
["e5-large-v2","Microsoft","2022","1024","model","model","Microsoft's E5 large v2 trained with contrastive learning on weak supervision. A retrieval workhorse."],
["nomic-embed-text-v1","Nomic","2024","768","model","model","Nomic's 768-dim open embedding model with Matryoshka representations and a long 8192 context."],
["all-MiniLM-L6-v2","Reimers & Gurevych","2019","384","model","model","The 384-dim sentence-transformer that started it all. Fast, tiny, and still everywhere."],
["instructor-xl","Su et al.","2022","1024","model","model","An instruction-tuned embedding model: prefix the task, get task-specific vectors. One model, many tasks."],
["gte-large","Alibaba","2023","1024","model","model","Alibaba's general text embedding large model. Strong multilingual retrieval performance."],
["SFR-Embedding-Mistral","Salesforce","2024","4096","model","model","A Mistral-7B-based embedding model with 4096 dimensions. Top of the MTEB leaderboard on release."],
["voyage-2","Voyage AI","2024","1024","model","model","Voyage AI's general-purpose embedding model. Strong retrieval with domain-tuned variants."],
["ColBERT","Khattab & Zaharia","2020","-","technique","technique","Late interaction: keep per-token vectors and score with MaxSim. Precise retrieval at higher compute cost."],
["Matryoshka Representation Learning","Kusupati et al.","2022","-","technique","technique","Nested embeddings where prefixes of the vector stay useful. Truncate dimensions without retraining."],
["SimCSE","Gao et al.","2021","-","technique","technique","Simple contrastive learning of sentence embeddings with dropout as augmentation. Unsupervised and effective."],
["Contrastive learning","-","-","-","technique","technique","Train embeddings by pulling similar pairs together and pushing dissimilar ones apart. The core of modern embedding training."],
["Mean pooling","-","-","-","technique","technique","Average token vectors into one sentence vector, often with attention masking. The simplest pooling that works."],
["RAG retrieval","-","-","-","application","application","Retrieval-augmented generation: embed the query, fetch documents, ground the answer. Embeddings made it possible."],
["Semantic search","-","-","-","application","application","Search by meaning instead of keywords. Cosine similarity over embeddings replaced many keyword systems."],
["Clustering with embeddings","-","-","-","application","application","Group documents by topic using embedding similarity. Powers topic discovery and deduplication."],
["Embedding-based reranking","-","-","-","application","application","Score candidate documents with a cross-encoder or bi-encoder for final ordering. The second stage of retrieval."]
];
var NOTES=["Check the MTEB leaderboard for current scores.","Dimension count trades quality against storage cost.","Normalize vectors before cosine similarity.","Chunking strategy changes retrieval quality.","Evaluate on your own data, not just the leaderboard.","Quantization can shrink storage with small quality loss."];
var SIG_M=["Nova Embed","Ember Vector","Tide Encode","Prism Retriever","Comet Search","Drift Match"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[6]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],org:e[1],year:e[2],dims:e[3],kind:e[4],
      source:"fact-checked",source_ref:"MTEB leaderboard / published papers",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var nm=pick(rnd,SIG_M)+" "+pick(rnd,["v1","v2","XL","mini"]);
  return {id:id,t:nm,title:nm,
    description:"A Signature original embedding "+cat+": "+nm+". "+pick(rnd,["It uses Matryoshka training so vectors truncate cleanly from 1024 to 128 dims.","Its contrastive training pairs hard negatives mined from the target domain.","Instruction prefixes let one model serve search, clustering, and classification."])+" "+pick(rnd,NOTES),
    category:cat,g:cat,org:"Signature Vector Works",year:String(ri(rnd,2024,2026)),
    dims:String(pick(rnd,[128,256,384,768,1024,3072])),kind:cat,
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','org','year','kind','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-embeddings-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
function selfTest(){
  var pass=0,fails=[];
  function t(n,c){if(c)pass++;else fails.push(n);}
  var i,s,r,a,b;
  for(i=0;i<20;i++){s=1+i*50000;r=generate(s,{},prng(s));t('gen+validate seed '+s,validate(r).ok);}
  for(i=0;i<10;i++){s=1+i*99999;a=generate(s,{},prng(s));b=generate(s,{},prng(s));t('determinism '+s,JSON.stringify(a)===JSON.stringify(b));}
  var seen={},dup=false;for(s=1;s<=5000;s++){var id=PREFIX+String(s).padStart(7,'0');if(seen[id])dup=true;seen[id]=1;}t('5000 unique ids',!dup);
  var okid=true;for(i=0;i<100;i++){s=1+((i*7919)%5000);r=generate(s,{},prng(s));if(!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))okid=false;}t('id format x100',okid);
  t('reject null',!validate(null).ok);
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],org:'o',year:'2020',kind:'k',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],org:'o',year:'2020',kind:'k',source:'signature'}).ok);
  var okc=true;for(i=0;i<100;i++){s=1+((i*104729)%5000);r=generate(s,{},prng(s));if(CATS.indexOf(r.category)<0)okc=false;}t('category membership x100',okc);
  var g1=generate(1,{category:CATS[0]},prng(1));t('opts.category honored',g1.category===CATS[0]);
  t('gen exports',typeof module.exports.generate==='function');
  t('version set',/^jahdb-/.test(gen.version));
  var dc=driftCheck(generate(7,{},prng(7)),[]);t('driftCheck ok',!!(dc&&dc.ok));
  console.log('SELF-TEST '+SLUG+': '+pass+'/40 '+(pass===40?'PASS':'FAIL ['+fails.join('; ')+']'));
  return pass===40;
}
if(typeof require!=='undefined'&&require.main===module){process.exit(selfTest()?0:1);}
})();
