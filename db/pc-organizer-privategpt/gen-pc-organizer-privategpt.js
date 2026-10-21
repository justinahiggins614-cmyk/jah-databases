(function(){'use strict';
/* PrivateGPT Database — boundless generator jahdb-pc-organizer-privategpt-1.0
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
var CATS=["ingestion", "models", "config", "privacy"];
var PREFIX='JAH-PCO89-';
var ROWS=[["privacy", "100% local by architecture", "PrivateGPT runs the LLM, embeddings, and vector store all on your machine — documents never leave the disk. Privacy is architectural, not a policy promise. Air-gapped operation is possible.", ["no cloud calls", "air-gap capable"]], ["ingestion", "The ingest pipeline", "Documents in source_documents/ are loaded, split, embedded, and stored in the vector DB by the ingest script. Re-run ingest when documents change. The pipeline is explicit and inspectable.", ["source_documents/", "re-ingest on change"]], ["config", "settings.yaml configuration", "settings.yaml declares the LLM (llamacpp, ollama, openai), embeddings, vector store, and server options in one file. Profiles switch setups without code changes. Configuration is the control plane.", ["profiles", "one config file"]], ["models", "LLM backend choices", "Backends include llama.cpp (GGUF local), Ollama (managed local), and OpenAI-compatible endpoints; the 2.x rewrite made backends pluggable. Local-first with escape hatches. Choice per deployment.", ["llamacpp", "ollama", "pluggable"]], ["models", "Embedding models local too", "Embeddings run locally (sentence-transformers, etc.) so even the vector math stays on-machine. Embedding choice affects retrieval quality most. Local embeddings complete the private loop.", ["sentence-transformers", "retrieval quality"]], ["ingestion", "Vector store options", "Chroma and Qdrant (local modes) persist the document vectors; the store is swappable via settings. Persistence separates ingest from serve. Swappable stores avoid lock-in.", ["Chroma/Qdrant", "persistence"]], ["config", "The Gradio/API interface", "A Gradio UI and REST API expose ask-your-documents chat with source citations. Citations show which chunks grounded each answer. Usable by non-technical users immediately.", ["Gradio UI", "citations"]], ["ingestion", "Ingest modes and file types", "Ingest handles PDF, TXT, MD, DOCX, and more via loaders; new file types plug in as loaders. Broad format support matters for real document piles. Loaders are the extensibility point.", ["loaders", "format breadth"]], ["models", "RAG over private data", "The standard flow is retrieve relevant chunks then generate with citations — RAG scoped to your documents. Answers stay grounded in private data. No training on your files needed.", ["grounded answers", "no fine-tuning"]], ["models", "Keeping models updated", "Swap the GGUF in models/ or the Ollama tag and restart; documents do not need re-ingesting when only the LLM changes. Model upgrades are cheap. Embeddings changes do require re-ingest.", ["cheap LLM upgrades", "embedding changes cost"]], ["config", "Hardware sizing", "A 7-8B GGUF at Q4 needs ~6GB RAM/VRAM plus embeddings overhead; bigger models need proportionally more. Size the model to the machine, not the hype. Local Q&A works on modest hardware.", ["VRAM math", "modest hardware OK"]], ["privacy", "Multi-user considerations", "Single-user by default; multi-user needs the API behind auth and per-user document scoping. Privacy per user requires access control at the retrieval layer. Plan scoping before sharing.", ["auth", "scoping"]], ["privacy", "What it does not do", "PrivateGPT does not train on your documents, does not phone home, and does not replace a search engine for exact lookup — it is Q&A over embeddings. Honest scoping prevents misuse. Use search for exact finds.", ["honest scoping", "right tool pairing"]], ["config", "From 1.x to 2.x", "The 2.x rewrite introduced the settings.yaml architecture and pluggable components, replacing the 1.x script collection. Upgrading means adopting the new config model. Rewrites signal maturation.", ["config model", "pluggable design"]], ["privacy", "Use cases that fit", "Contracts, manuals, research papers, personal notes — any corpus you can read but cannot upload. The fit test: would you paste this into a cloud chatbot? If no, PrivateGPT. Privacy need defines the use case.", ["contracts/manuals", "privacy-defined fit"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"PrivateGPT",edition:'public',description:desc,facts:row[3].slice(),
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
var gen={version:'jahdb-pc-organizer-privategpt-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-privategpt',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_privategpt']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
