(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK120-";
var KIND="search method";
var TOOLNAME="Composite Search Engine";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Reciprocal rank fusion", "d": "RRF scores each document by summing 1/(k + rank) over the rankings that include it. It needs no score normalization because ranks, not raw scores, are fused. RRF is the default unsupervised fusion: simple, robust, and hard to beat.", "c": "fundamentals", "r": 1, "p": {"QUERY": "Jon Smith", "K": "60", "DOCS": "{'d1': 'John Smith', 'd2': 'Jon Smyth', 'd3': 'Jane Doe'}"}}, {"t": "Score normalization", "d": "Fusing raw scores requires normalization: min-max scaling or z-scores per ranker. Without it, the ranker with the widest score range dominates. Normalization is the unglamorous step that makes fusion work.", "c": "algorithms", "r": 1, "p": {"QUERY": "archive index", "K": "60", "DOCS": "{'d1': 'archive index', 'd2': 'archive catalog', 'd3': 'weather'}"}}, {"t": "Weighted linear combination", "d": "Weighted sums let operators favor trusted rankers: 0.7*keyword + 0.3*phonetic. Weights are tuned on labeled data via grid or coordinate search. Weights encode which signals the application trusts.", "c": "implementation", "r": 1, "p": {"QUERY": "catalog search", "K": "60", "DOCS": "{'d1': 'catalog search tips', 'd2': 'search catalog', 'd3': 'unrelated'}"}}, {"t": "Cascade ranking", "d": "Cascades run a cheap ranker first, then an expensive one only on the top candidates. Keyword retrieval feeds neural reranking on the top 100. Cascades buy quality at bounded cost.", "c": "optimization", "r": 1, "p": {"QUERY": "lighthouse history", "K": "60", "DOCS": "{'d1': 'lighthouse history', 'd2': 'history of lighthouses', 'd3': 'harbor'}"}}, {"t": "Borda count fusion", "d": "Borda assigns points by position (n-1 for first) and sums across rankings. It is a voting-theoretic fusion needing no scores at all. Borda is simple but sensitive to weak rankers' noise.", "c": "evaluation", "r": 1, "p": {"QUERY": "data archive", "K": "60", "DOCS": "{'d1': 'data archive', 'd2': 'archive data', 'd3': 'noise'}"}}, {"t": "CombSUM and CombMNZ", "d": "CombSUM adds normalized scores; CombMNZ multiplies the sum by the number of rankers retrieving the document. MNZ rewards documents found by many methods, a consensus bonus. These classic fusions remain strong baselines.", "c": "fundamentals", "r": 2, "p": {"QUERY": "maps collection", "K": "60", "DOCS": "{'d1': 'maps collection', 'd2': 'collection of maps', 'd3': 'other'}"}}, {"t": "Learning to rank", "d": "Supervised fusion trains a model on (query, document, label) triples with per-ranker scores as features. Gradient-boosted trees over ranker scores dominate benchmarks. Learning to rank turns fusion into a prediction problem.", "c": "algorithms", "r": 2, "p": {"QUERY": "annual report", "K": "60", "DOCS": "{'d1': 'annual report', 'd2': 'yearly report', 'd3': 'notes'}"}}, {"t": "Query-type routing", "d": "Not every query needs every ranker: routers send name queries to phonetic+typo rankers and topic queries to semantic ones. Routing saves compute and reduces noise from irrelevant rankers. Smart routing beats always-on fusion on both speed and quality.", "c": "implementation", "r": 2, "p": {"QUERY": "Catherine", "K": "60", "DOCS": "{'d1': 'Katherine', 'd2': 'Catherine the Great', 'd3': 'other'}"}}, {"t": "Diversified fusion", "d": "Fusion can over-concentrate on one interpretation; diversification re-ranks for aspect coverage. MMR-style penalties demote near-duplicates of already-selected results. Diversity matters most for ambiguous queries.", "c": "optimization", "r": 2, "p": {"QUERY": "apple", "K": "60", "DOCS": "{'d1': 'apple fruit', 'd2': 'apple company', 'd3': 'apple pie'}"}}, {"t": "Federated search merging", "d": "Federated search queries independent collections, each with its own ranker and score scale. Merging needs score calibration or rank-based fusion like RRF. Federation keeps sources autonomous while presenting one list.", "c": "evaluation", "r": 2, "p": {"QUERY": "climate data", "K": "60", "DOCS": "{'d1': 'climate data', 'd2': 'data on climate', 'd3': 'x'}"}}, {"t": "Fallback chains", "d": "When the primary ranker returns too few results, fallbacks relax the query: fewer terms, typo tolerance, broader fields. Each fallback stage widens the net until the result count suffices. Fallbacks guarantee users rarely face an empty page.", "c": "fundamentals", "r": 3, "p": {"QUERY": "zxqv archive", "K": "60", "DOCS": "{'d1': 'archive notes', 'd2': 'old archive', 'd3': 'y'}"}}, {"t": "Evaluating fused systems", "d": "Fusion is judged against each component alone: it must beat the best single ranker to justify its complexity. Ablation removes one ranker at a time to measure marginal value. Honest evaluation keeps fusion lean.", "c": "algorithms", "r": 3, "p": {"QUERY": "test query", "K": "60", "DOCS": "{'d1': 'test query here', 'd2': 'query test', 'd3': 'z'}"}}, {"t": "Real-time fusion budgets", "d": "Production fusion runs under latency budgets: slow rankers get timeouts and partial results still fuse. Deadline-aware fusion degrades gracefully instead of failing. Budgets make fusion deployable.", "c": "implementation", "r": 3, "p": {"QUERY": "fast search", "K": "60", "DOCS": "{'d1': 'fast search tips', 'd2': 'search fast', 'd3': 'w'}"}}, {"t": "Explainable fusion", "d": "Result cards can show which rankers voted for each document and their ranks. 'Ranked #2 by keyword, #5 by semantic' builds trust. Explanation turns fusion from magic into method.", "c": "optimization", "r": 3, "p": {"QUERY": "open data", "K": "60", "DOCS": "{'d1': 'open data portal', 'd2': 'data open', 'd3': 'v'}"}}, {"t": "Tuning fusion weights", "d": "Weights are tuned by coordinate ascent on a validation set, one ranker at a time. Regularization keeps weights from overfitting small judgment sets. Retuning cadence follows data drift.", "c": "evaluation", "r": 3, "p": {"QUERY": "final report", "K": "60", "DOCS": "{'d1': 'final report', 'd2': 'report final', 'd3': 'u'}"}}];
var DEMO="# Composite search: run keyword + phonetic scorers, fuse with reciprocal rank fusion.\ndef kw_score(query, text):\n    qt = set(query.lower().split()); dt = set(text.lower().split())\n    return len(qt & dt) / len(qt) if qt else 0.0\ndef soundex(w):\n    w = w.upper(); m = {\"BFPV\": \"1\", \"CGJKQSXZ\": \"2\", \"DT\": \"3\", \"L\": \"4\", \"MN\": \"5\", \"R\": \"6\"}\n    code = w[0]; prev = \"\"\n    for ch in w[1:]:\n        d = next((v for k, v in m.items() if ch in k), \"\")\n        if d and d != prev: code += d\n        prev = d\n    return code\ndef phon_score(query, text):\n    qc = {soundex(w) for w in query.split()}\n    tc = {soundex(w) for w in text.split()}\n    return len(qc & tc) / len(qc) if qc else 0.0\ndocs = %%DOCS%%\nquery = \"%%QUERY%%\"\nrankings = []\nfor name, fn in [(\"keyword\", kw_score), (\"phonetic\", phon_score)]:\n    ranked = sorted(docs, key=lambda d: fn(query, docs[d]), reverse=True)\n    rankings.append(ranked)\n    print(name, \"ranking:\", ranked)\nrrf = {}\nfor ranked in rankings:\n    for i, d in enumerate(ranked):\n        rrf[d] = rrf.get(d, 0) + 1.0 / (%%K%% + i)\nprint(\"fused (RRF, k=%%K%%):\", sorted(rrf, key=rrf.get, reverse=True))\n";
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
  if(!new RegExp("^JAH\\-ATK120\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-composite-search-engine-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-composite-search-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
