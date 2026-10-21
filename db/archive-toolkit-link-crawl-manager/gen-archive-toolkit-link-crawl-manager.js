(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK128-";
var KIND="traversal method";
var TOOLNAME="Link-Crawl Manager";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Frontier queue", "d": "The frontier holds discovered-but-unvisited URLs, usually as a priority queue. Prioritization by estimated value focuses the crawl. Frontier design decides crawl quality.", "c": "fundamentals", "r": 1, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/b', 'https://a.example/c'], 'https://a.example/b': ['https://a.example/d'], 'https://a.example/c': [], 'https://a.example/d': []}"}}, {"t": "Allow-list scoping", "d": "Crawls stay within allowed hosts and paths, ignoring everything else. Scoping prevents runaway crawls across the web. Explicit scope is a safety requirement.", "c": "algorithms", "r": 1, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/docs/']", "PAGES": "{'https://a.example/': ['https://a.example/docs/x', 'https://b.example/y'], 'https://a.example/docs/x': []}"}}, {"t": "Duplicate detection", "d": "URL normalization (lowercasing hosts, dropping fragments) dedupes before fetching. Content hashing catches distinct URLs serving identical pages. Dedup keeps crawls from reprocessing the web.", "c": "implementation", "r": 1, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/b', 'https://a.example/b#frag'], 'https://a.example/b': []}"}}, {"t": "Depth limiting", "d": "Max depth bounds how far from seeds the crawl wanders. Shallow crawls stay topical; deep crawls discover more. Depth trades focus against coverage.", "c": "optimization", "r": 1, "p": {"START": "https://a.example/", "DEPTH": "1", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/b'], 'https://a.example/b': ['https://a.example/c']}"}}, {"t": "Politeness delays", "d": "Crawlers space requests per host and honor crawl-delay directives. Politeness sustains access and avoids overloading servers. Good crawlers are invited back.", "c": "evaluation", "r": 1, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/b'], 'https://a.example/b': []}"}}, {"t": "Robots directives", "d": "Crawlers parse robots.txt for allow/disallow rules per user-agent. Compliance is both ethical and legally prudent. Directive-aware crawlers skip forbidden paths automatically.", "c": "fundamentals", "r": 2, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/public/']", "PAGES": "{'https://a.example/': ['https://a.example/public/x'], 'https://a.example/public/x': []}"}}, {"t": "Link extraction", "d": "Extractors pull hrefs from markup, resolving relative URLs against the base. Canonicalization then normalizes each link. Clean extraction feeds the frontier.", "c": "algorithms", "r": 2, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/about'], 'https://a.example/about': []}"}}, {"t": "Crawl budgeting", "d": "Budgets cap pages per host, total pages, and bytes. Budgeted crawls stop gracefully with coverage reports. Budgets make large crawls predictable.", "c": "implementation", "r": 2, "p": {"START": "https://a.example/", "DEPTH": "3", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/1','https://a.example/2'], 'https://a.example/1': [], 'https://a.example/2': []}"}}, {"t": "Revisit scheduling", "d": "Changed pages get recrawled on schedules based on observed change frequency. Adaptive schedules focus on volatile pages. Freshness matters for news and prices.", "c": "optimization", "r": 2, "p": {"START": "https://a.example/", "DEPTH": "1", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/news'], 'https://a.example/news': []}"}}, {"t": "Trap avoidance", "d": "Calendar and session-id URLs generate infinite spaces; pattern detectors blacklist them. Query-parameter budgets cap variations per path. Trap avoidance keeps crawls finite.", "c": "evaluation", "r": 2, "p": {"START": "https://a.example/", "DEPTH": "3", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/cal'], 'https://a.example/cal': []}"}}, {"t": "Sitemap seeding", "d": "XML sitemaps seed crawls with the site's own URL list. Sitemaps reveal pages no link path reaches. Seeding from sitemaps boosts coverage.", "c": "fundamentals", "r": 3, "p": {"START": "https://a.example/sitemap", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/sitemap': ['https://a.example/a','https://a.example/b'], 'https://a.example/a': [], 'https://a.example/b': []}"}}, {"t": "Distributed crawling", "d": "Partitioning by host hash spreads the crawl across workers without overlap. Coordination services dedupe the global frontier. Distribution scales crawls to billions of pages.", "c": "algorithms", "r": 3, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/x'], 'https://a.example/x': []}"}}, {"t": "Crawl diagnostics", "d": "Dashboards track fetch rates, error codes, and politeness waits per host. Diagnostics reveal blocks and misconfigurations fast. Observable crawls are fixable crawls.", "c": "implementation", "r": 3, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/ok'], 'https://a.example/ok': []}"}}, {"t": "Content-type filtering", "d": "Crawlers fetch only wanted content types, skipping binaries when text is the goal. HEAD requests or extension rules filter cheaply. Filtering saves bandwidth and storage.", "c": "optimization", "r": 3, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/page'], 'https://a.example/page': []}"}}, {"t": "Incremental recrawls", "d": "Recrawls fetch only pages whose ETag or Last-Modified changed. Conditional requests make freshness cheap. Incremental crawling sustains living indexes.", "c": "evaluation", "r": 3, "p": {"START": "https://a.example/", "DEPTH": "2", "ALLOWED": "['https://a.example/']", "PAGES": "{'https://a.example/': ['https://a.example/a'], 'https://a.example/a': []}"}}];
var DEMO="# Link crawl: BFS over a link graph with allow-list, depth cap, and visited set.\npages = %%PAGES%%\nallowed = %%ALLOWED%%\ndef crawl(start, max_depth=%%DEPTH%%):\n    seen, queue, order = {start}, [(start, 0)], []\n    while queue:\n        url, depth = queue.pop(0)\n        order.append((url, depth))\n        if depth >= max_depth: continue\n        for link in pages.get(url, []):\n            if link not in seen and any(link.startswith(a) for a in allowed):\n                seen.add(link); queue.append((link, depth + 1))\n    return order\nfor url, depth in crawl(\"%%START%%\"):\n    print(\"  \"*depth + url)\n";
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
  if(!new RegExp("^JAH\\-ATK128\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-link-crawl-manager-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-link-crawl-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
