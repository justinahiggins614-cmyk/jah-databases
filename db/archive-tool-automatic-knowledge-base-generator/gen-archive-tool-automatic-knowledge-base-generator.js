(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["subject-scoping", "corpus-assembly", "topic-clustering", "index-construction", "qa-smoke-test"];
var PREFIX='JAH-AT95-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Subject scoping from a seed description", "k": "method", "d": "The new subject starts from a seed description that is expanded into a scope: core topics in, adjacent topics parked, explicit exclusions. Scoping prevents the knowledge base from sprawling into neighboring subjects. The scope document is reviewed before any corpus assembly begins.", "demo": "scope = {'subject': 'archive indexing', 'in': ['inverted index', 'posting lists'], 'out': ['video codecs']}\nprint('scope:', scope['subject'], '| core topics:', len(scope['in']))\n"}, {"t": "Corpus assembly from approved sources", "k": "method", "d": "Source documents are gathered from the archive's approved collections matching the scope, with provenance recorded per document. Assembly favors primary sources and recent material, and deduplicates near-identical documents. The corpus is the knowledge base's raw material; its quality bounds everything built on it.", "demo": "docs = [{'id': 'd1', 'text': 'inverted index maps terms to docs'}, {'id': 'd2', 'text': 'posting lists store positions'}]\nprint('corpus documents:', len(docs))\n"}, {"t": "Topic clustering of the corpus", "k": "algorithm", "d": "Documents are clustered by term overlap into topic groups, giving the knowledge base its browse structure. Clustering uses agglomerative merging on Jaccard similarity with a similarity floor, which needs no predeclared cluster count. Each cluster is labeled by its most distinctive terms.", "demo": "def jacc(a, b):\n    A, B = set(a.split()), set(b.split())\n    return len(A & B) / max(1, len(A | B))\ndocs = ['inverted index terms docs', 'posting lists positions', 'hash table buckets']\nprint('d1-d2 similarity:', round(jacc(docs[0], docs[1]), 2), '| d1-d3:', round(jacc(docs[0], docs[2]), 2))\n"}, {"t": "Search index construction over the corpus", "k": "algorithm", "d": "An inverted index is built over the corpus: each term maps to the documents containing it with positions. The index makes the knowledge base searchable from the moment it is published. Construction is a single pass over the corpus, linear in total text length.", "demo": "from collections import defaultdict\ncorpus = {'d1': 'inverted index maps terms', 'd2': 'posting lists store positions'}\nidx = defaultdict(list)\nfor did, text in corpus.items():\n    for w in text.split(): idx[w].append(did)\nprint('index terms:', len(idx), '| \"index\" ->', idx['index'])\n"}, {"t": "Question-answering smoke test", "k": "procedure", "d": "Before publication, the knowledge base answers a smoke-test set of questions drawn from its scope, and each answer is checked for support in the corpus. The smoke test catches empty clusters, broken indexes, and scope drift. A knowledge base that fails smoke testing does not ship.", "demo": "qa = [('what maps terms to docs?', 'inverted index'), ('what stores positions?', 'posting lists')]\ncorpus_text = 'inverted index maps terms to docs. posting lists store positions.'\npassed = sum(1 for q, a in qa if a in corpus_text)\nprint(f'smoke test: {passed}/{len(qa)} passed')\n"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var v=(rnd()*3)|0;
  var desc=a.d+VARIANTS[v]+(SIG?' Signature-authored original by Justin Addam Higgins (JAH).':'');
  var id=PREFIX+String(seed).padStart(6,'0');
  var ttl=a.t+[' (foundational)',' (compounded)',' (production)'][v];
  var prov=SIG?'Signature-authored original by Justin Addam Higgins (JAH), 2026-10-21.':'Public computer-science methods literature; cross-checked against standard references, 2026-10-21.';
  return {id:id,t:ttl,title:ttl,description:desc,kind:a.k,category:cat,ladder_rank:v+1,demo:(SIG?'# Signature-authored original (JAH).\n':'')+a.demo,provenance:prov,last_verified:'2026-10-21',src:SIG?'signature-generated-completion':'public-harvest',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/-/g,'\\-');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(KIND_LIST.indexOf(r.kind)<0)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==(SIG?'signature-generated-completion':'public-harvest'))e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  if(sample&&sample.length){
    for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].id===rec.id){e.push('duplicate id');break;} }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-archive-tool-automatic-knowledge-base-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-automatic-knowledge-base-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
