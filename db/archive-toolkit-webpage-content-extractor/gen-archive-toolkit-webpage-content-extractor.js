(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK148-";
var KIND="extraction method";
var TOOLNAME="Webpage Content Extractor";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Text-density scoring", "d": "Content blocks score by words per link: high text, few links means article body. Density separates articles from nav. Ratios reveal content.", "c": "fundamentals", "r": 1, "p": {"HTML": "<div><a href=x>Home</a> <a href=y>About</a></div><article><p>The quick brown fox jumps over the lazy dog near the river bank at dawn.</p></article>"}}, {"t": "Boilerplate removal", "d": "Headers, footers, and sidebars repeat across pages; shingling finds the repeats. Removing boilerplate dedupes indexes. Repeats are noise.", "c": "algorithms", "r": 1, "p": {"HTML": "<div><p>Copyright 2024 Site Inc all rights reserved</p></div><article><p>Breaking news about the harbor festival this weekend.</p></article>"}}, {"t": "Ad detection", "d": "Ad slots match known patterns (ids, classes, dimensions). Blocking ads cleans extraction. Ads are clutter.", "c": "implementation", "r": 1, "p": {"HTML": "<div id=ad-banner><p>Buy now!</p></div><article><p>Real article text about local elections and voter turnout.</p></article>"}}, {"t": "Main-image selection", "d": "The largest above-the-fold image near the headline is usually the hero. Heuristics pick it reliably. Images illustrate.", "c": "optimization", "r": 1, "p": {"HTML": "<article><p>Story text here about the new bridge opening downtown today.</p></article>"}}, {"t": "Title extraction", "d": "<title> plus the top H1 usually agree; disagreement flags template issues. Titles name pages. Names matter.", "c": "evaluation", "r": 1, "p": {"HTML": "<title>Bridge Opens - Gazette</title><article><p>Downtown celebrated the new bridge opening with fireworks.</p></article>"}}, {"t": "Date extraction", "d": "Publish dates hide in meta tags, time elements, or URL patterns. Dates order content. Time contexts.", "c": "fundamentals", "r": 2, "p": {"HTML": "<article><p>Published report on quarterly earnings released this morning by analysts.</p></article>"}}, {"t": "Author extraction", "d": "Bylines match 'By Name' patterns near the headline, with fallbacks to meta tags and structured data when the visible byline is missing. Extracted authors link articles to people, enabling author pages and credibility signals. Reliable attribution is the basis of provenance for web content.", "c": "algorithms", "r": 2, "p": {"HTML": "<article><p>By Jane Reporter: council votes on the new zoning proposal tonight.</p></article>"}}, {"t": "Comment separation", "d": "Comments live in identifiable containers; extractors exclude them from the article. Separation keeps content clean. Comments are separate.", "c": "implementation", "r": 2, "p": {"HTML": "<article><p>Article body discussing the transit plan expansion across three counties.</p></article><div class=comments><p>Great post!</p></div>"}}, {"t": "Paywall handling", "d": "Extractors respect paywalls: only freely served content is kept. Honesty beats scraping. Rights matter.", "c": "optimization", "r": 2, "p": {"HTML": "<article><p>Free preview paragraph summarizing the investigation into city contracts.</p></article>"}}, {"t": "Language detection", "d": "Per-block language detection handles multilingual pages. Detection routes processing. Languages vary.", "c": "evaluation", "r": 2, "p": {"HTML": "<article><p>The council approved the measure after long debate last night.</p></article>"}}, {"t": "Table preservation", "d": "Content tables are kept as structured data, not flattened text. Structure preserves meaning. Tables inform.", "c": "fundamentals", "r": 3, "p": {"HTML": "<article><table><tr><td>a</td></tr></table><p>Results table shows quarterly growth across all regions.</p></article>"}}, {"t": "Reading-time estimation", "d": "Word counts divided by an average reading speed estimate reading minutes, usually around 200 to 250 words per minute for English prose. Estimates set reader expectations and help interfaces decide between a quick summary and the full text. They are rough but consistently useful.", "c": "algorithms", "r": 3, "p": {"HTML": "<article><p>word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word word </p></article>"}}, {"t": "AMP and reader modes", "d": "Reader modes apply the same extraction for clean reading views. Modes reuse extractors. Clean reading delights.", "c": "implementation", "r": 3, "p": {"HTML": "<article><p>Longform story about mountain rescue teams training through winter storms.</p></article>"}}, {"t": "Evaluating extraction", "d": "Labeled page corpora score extractors on text overlap F1. Benchmarks compare approaches. Measurement improves.", "c": "optimization", "r": 3, "p": {"HTML": "<article><p>Gold standard article text for evaluation purposes here today.</p></article>"}}, {"t": "Streaming extraction", "d": "Streaming parsers extract content during download without building a full DOM, emitting text blocks as tags close. Constant memory usage lets extraction run on huge pages and slow connections alike. Streaming is how large-scale crawlers keep extraction cheap.", "c": "evaluation", "r": 3, "p": {"HTML": "<article><p>Streaming friendly article content delivered in chunks for fast rendering.</p></article>"}}];
var DEMO="# Content extraction: score blocks by text density vs link density (readability-style).\nimport re\nhtml = \"\"\"%%HTML%%\"\"\".replace(\"\\\\n\", \"\\n\")\nblocks = re.findall(r\"<(p|div|article|section)[^>]*>(.*?)</\\1>\", html, re.S | re.I)\ndef clean(s):\n    s = re.sub(r\"<[^>]+>\", \" \", s)\n    return re.sub(r\"\\s+\", \" \", s).strip()\nscored = []\nfor tag, inner in blocks:\n    text = clean(inner)\n    links = len(re.findall(r\"<a\\b\", inner, re.I))\n    words = len(text.split())\n    score = words / (1 + links * 5)\n    scored.append((score, tag, text))\nscored.sort(reverse=True)\nprint(\"blocks ranked (text-density score):\")\nfor score, tag, text in scored:\n    print(f\"  [{score:5.1f}] <{tag}> {text[:60]}\")\nprint(\"\\nMAIN CONTENT:\", scored[0][2][:120] if scored else \"none\")\n";
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
  if(!new RegExp("^JAH\\-ATK148\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-webpage-content-extractor-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-webpage-content-extractor",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
