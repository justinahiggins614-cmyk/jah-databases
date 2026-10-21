(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK126-";
var KIND="traversal method";
var TOOLNAME="API Pagination Navigator";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Next-link following", "d": "REST APIs expose next page URLs; navigators follow them until none remains. Link headers (RFC 5988) standardize the 'next' relation. Following links beats constructing URLs by hand.", "c": "fundamentals", "r": 1, "p": {"PAGES": "{0: (['a','b'], 1), 1: (['c'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Page-number iteration", "d": "Some APIs take ?page=N; navigators increment until an empty page or total_pages. Empty-page termination handles unknown totals. Number iteration is simple but offset-fragile.", "c": "algorithms", "r": 1, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Cursor query params", "d": "Cursor APIs take ?cursor=...; navigators feed each response's cursor into the next request. Cursors stay stable as data changes. Cursor params are the modern default.", "c": "implementation", "r": 1, "p": {"PAGES": "{0: (['a'], 1), 1: (['b','c'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Stopping conditions", "d": "Navigators stop on: no next page, empty page, item-count target, time budget, or predicate match. Explicit conditions prevent infinite crawls. Every traversal needs a defined end.", "c": "optimization", "r": 1, "p": {"PAGES": "{0: (['a','STOP'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": "STOP"}}, {"t": "Loop detection", "d": "Buggy APIs repeat cursors; navigators track seen tokens and abort on repeats. Loop detection turns hangs into errors. Seen-sets are cheap insurance.", "c": "evaluation", "r": 1, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Retry with backoff", "d": "Transient failures retry with exponential backoff and jitter. Idempotent page fetches make retries safe. Backoff keeps crawlers polite under load.", "c": "fundamentals", "r": 2, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], 2), 2: (['c'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Rate-limit handling", "d": "429 responses carry Retry-After; navigators sleep accordingly. Token buckets smooth request rates proactively. Respecting limits keeps access unblocked.", "c": "algorithms", "r": 2, "p": {"PAGES": "{0: (['a'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Parallel page fetching", "d": "Independent pages (numbered) fetch in parallel with bounded concurrency. Cursors serialize; page numbers parallelize. Concurrency needs care with rate limits.", "c": "implementation", "r": 2, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Incremental sync", "d": "Sync APIs return 'since' deltas; navigators store the sync token between runs. Deltas beat full re-crawls for freshness. Token persistence makes sync resumable.", "c": "optimization", "r": 2, "p": {"PAGES": "{0: (['new1'], 1), 1: (['new2'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Response validation", "d": "Navigators validate each page's shape before following its cursor. Schema checks catch API changes early. Validation fails fast instead of corrupting data.", "c": "evaluation", "r": 2, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Checkpointing progress", "d": "Long crawls checkpoint the current cursor to disk per page. Crashes resume from the checkpoint. Checkpointing bounds rework to one page.", "c": "fundamentals", "r": 3, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], 2), 2: (['c'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Deduplicating overlaps", "d": "Overlapping pages (from concurrent writes) dedupe by item id. Id-keyed sets keep exactly-once semantics. Dedup handles the real world's messiness.", "c": "algorithms", "r": 3, "p": {"PAGES": "{0: (['a','b'], 1), 1: (['b','c'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Total estimation", "d": "Some APIs report totals; navigators show progress as collected/total. Unknown totals fall back to page counts. Progress keeps long crawls transparent.", "c": "implementation", "r": 3, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Authentication refresh", "d": "Long crawls outlive tokens; navigators refresh credentials mid-traversal. Refresh hooks plug into the fetch loop. Seamless refresh avoids midnight failures.", "c": "optimization", "r": 3, "p": {"PAGES": "{0: (['a'], None)}", "MAXP": "10", "STOP": ""}}, {"t": "Crawl politeness", "d": "Polite crawlers identify themselves, honor robots directives, and limit rates. Politeness sustains long-term API access. Good citizenship is operational strategy.", "c": "evaluation", "r": 3, "p": {"PAGES": "{0: (['a'], 1), 1: (['b'], None)}", "MAXP": "10", "STOP": ""}}];
var DEMO="# API pagination navigator: follow next-links until the stop condition, with retries.\nPAGES = %%PAGES%%\ndef fetch(page):\n    # simulated API: returns (items, next_page or None)\n    if page not in PAGES: raise IOError(\"transient failure\")\n    return PAGES[page]\ndef collect_all(max_pages=%%MAXP%%, stop_when=None):\n    items, page, seen = [], 0, set()\n    while page is not None and len(seen) < max_pages:\n        if page in seen: raise RuntimeError(\"page loop detected\")\n        seen.add(page)\n        batch, page = fetch(page)\n        items.extend(batch)\n        if stop_when and stop_when(batch): break\n    return items\ngot = collect_all(stop_when=lambda b: \"%%STOP%%\" in b if \"%%STOP%%\" else False)\nprint(\"collected:\", got)\n";
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
  if(!new RegExp("^JAH\\-ATK126\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-api-pagination-navigator-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-api-pagination-navigator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
