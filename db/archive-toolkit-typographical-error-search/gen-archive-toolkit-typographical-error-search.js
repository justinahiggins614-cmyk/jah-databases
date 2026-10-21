(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK106-";
var KIND="search method";
var TOOLNAME="Typographical Error Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Levenshtein edit distance", "d": "Levenshtein distance counts the minimum insertions, deletions, and substitutions turning one string into another. The classic dynamic program fills an (m+1)x(n+1) table where each cell takes the minimum of its three neighbors plus a substitution cost. Distance 1 or 2 captures the vast majority of human typos, which is why it anchors typo-tolerant search.", "c": "fundamentals", "r": 1, "p": {"QUERY": "archvie", "WORDS": "['archive','archival','archives','index']", "MAXD": "2"}}, {"t": "Damerau-Levenshtein with transpositions", "d": "Adjacent transpositions ('teh' for 'the') are the most common typo, so Damerau-Levenshtein counts a swap as one edit. The extended recurrence tracks the last row each character appeared in, adding the transposition option. With transpositions, 'recieve' sits at distance 1 from 'receive' instead of 2.", "c": "algorithms", "r": 1, "p": {"QUERY": "teh", "WORDS": "['the','ten','tech','tea']", "MAXD": "1"}}, {"t": "Keyboard-adjacency weighting", "d": "Not all substitutions are equal: 'q' for 'w' is a near-miss on QWERTY while 'q' for 'p' is not. Weighted edit distance scales substitution cost by physical key distance. Keyboard-aware costs rank the plausible typo above the coincidence.", "c": "implementation", "r": 1, "p": {"QUERY": "archove", "WORDS": "['archive','archon','above']", "MAXD": "2"}}, {"t": "N-gram similarity", "d": "Character n-grams (usually trigrams) turn strings into sets; similarity is the overlap of those sets. 'archive' and 'archvie' share most trigrams despite the transposition, giving high Jaccard similarity. N-gram indexes also enable fast candidate generation before exact distance checks.", "c": "optimization", "r": 1, "p": {"QUERY": "catalgo", "WORDS": "['catalog','catalogue','cattle']", "MAXD": "2"}}, {"t": "SymSpell deletion index", "d": "SymSpell precomputes every string within k deletions of each vocabulary term and indexes those deletes. A query's own deletes then hit the index directly, finding candidates without scanning the vocabulary. Lookup is effectively constant time, which is why SymSpell powers real-time correction.", "c": "evaluation", "r": 1, "p": {"QUERY": "speling", "WORDS": "['spelling','spieling','spewing']", "MAXD": "2"}}, {"t": "BK-tree nearest neighbors", "d": "A BK-tree organizes the vocabulary by edit distance from chosen pivots, pruning whole subtrees during search. Querying walks only branches whose pivot distance falls within [d-k, d+k] of the query. BK-trees answer nearest-neighbor typo queries in sublinear time on large lexicons.", "c": "fundamentals", "r": 2, "p": {"QUERY": "indxe", "WORDS": "['index','indexed','indexes','indie']", "MAXD": "2"}}, {"t": "Levenshtein automata", "d": "A Levenshtein automaton for a query and budget k accepts exactly the strings within distance k. Walking it alongside a trie finds all vocabulary matches in time proportional to matches, not vocabulary size. Automata-based fuzzy search is how databases implement efficient 'LIKE with typos'.", "c": "algorithms", "r": 2, "p": {"QUERY": "qurey", "WORDS": "['query','queer','quarry']", "MAXD": "1"}}, {"t": "Noisy-channel spelling correction", "d": "The noisy-channel model picks the correction c maximizing P(c) * P(query|c): language prior times error likelihood. P(c) comes from word frequencies; P(query|c) from confusion matrices of real typo corpora. This ranks 'the' above 'teh'-neighbors correctly because 'the' is far more probable.", "c": "implementation", "r": 2, "p": {"QUERY": "acress", "WORDS": "['across','acres','actress']", "MAXD": "2"}}, {"t": "Context-aware correction", "d": "Isolated correction fails on real-word errors like 'their' for 'there'; context models score whole-sentence replacements. N-gram or neural language models pick the candidate that makes the sentence most probable. Context lifts correction from spellchecking to true error recovery.", "c": "optimization", "r": 2, "p": {"QUERY": "peace of", "WORDS": "['peace of','piece of','pace of']", "MAXD": "2"}}, {"t": "OCR error patterns", "d": "OCR confuses visually similar glyphs: 'rn' for 'm', '0' for 'O', '1' for 'l'. Correction models trained on OCR confusion pairs outperform generic edit distance on scanned text. Digitization pipelines pair OCR with a post-correction pass using these patterns.", "c": "evaluation", "r": 2, "p": {"QUERY": "arnhive", "WORDS": "['archive','arrive','arch']", "MAXD": "2"}}, {"t": "Phonetic typo blending", "d": "Some typos are phonetic ('fone' for 'phone'); blending edit distance with phonetic codes catches both. Candidates must be near in spelling or share a phonetic code, then rank by combined score. The blend covers the two distinct ways humans misspell: fingers and ears.", "c": "fundamentals", "r": 3, "p": {"QUERY": "fone", "WORDS": "['phone','fone','fine','fun']", "MAXD": "2"}}, {"t": "Query-log driven suggestions", "d": "Search logs reveal which corrections users actually accept, a stronger signal than any distance metric. 'Did you mean' systems learn P(correction|typo) directly from click-through on suggestions. Log-driven ranking adapts to the vocabulary and error habits of each specific archive.", "c": "algorithms", "r": 3, "p": {"QUERY": "libary", "WORDS": "['library','libel','liability']", "MAXD": "2"}}, {"t": "Typo-tolerant indexing", "d": "Instead of correcting the query, some systems index character n-grams so typos still overlap enough to match. Trigram indexes retrieve candidates sharing enough trigrams, then verify with exact distance. Index-side tolerance needs no query rewriting and handles out-of-vocabulary terms.", "c": "implementation", "r": 3, "p": {"QUERY": "documnet", "WORDS": "['document','documents','documentary']", "MAXD": "2"}}, {"t": "Setting the distance budget", "d": "Budget k=1 is nearly always safe; k=2 helps short queries but risks false friends on long vocabularies. Adaptive budgets scale with query length, often floor(len/4), keeping precision stable. Tuning k on labeled typo pairs beats any fixed rule.", "c": "optimization", "r": 3, "p": {"QUERY": "recieve", "WORDS": "['receive','relieve','recipe']", "MAXD": "2"}}, {"t": "Evaluating correction quality", "d": "Correction is scored by top-1 accuracy: how often the true intended term ranks first. Test sets inject synthetic typos with realistic error models into clean queries. Separate metrics for non-word versus real-word errors keep the evaluation honest.", "c": "evaluation", "r": 3, "p": {"QUERY": "seperate", "WORDS": "['separate','desperate','spear']", "MAXD": "2"}}];
var DEMO="# Typo-tolerant search: Levenshtein distance suggests corrections within a budget.\ndef levenshtein(a, b):\n    prev = list(range(len(b) + 1))\n    for i, ca in enumerate(a, 1):\n        cur = [i]\n        for j, cb in enumerate(b, 1):\n            cur.append(min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + (ca != cb)))\n        prev = cur\n    return prev[-1]\nwords = %%WORDS%%\nquery = \"%%QUERY%%\"\nbudget = %%MAXD%%\ncands = sorted(((levenshtein(query, w), w) for w in words if levenshtein(query, w) <= budget))\nprint(f\"Query {query!r}, max distance {budget}:\")\nfor d, w in cands:\n    print(f\"  {w!r} (distance {d})\")\nif not cands: print(\"  no candidates within budget\")\n";
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
  if(!new RegExp("^JAH\\-ATK106\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-typographical-error-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-typographical-error-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
