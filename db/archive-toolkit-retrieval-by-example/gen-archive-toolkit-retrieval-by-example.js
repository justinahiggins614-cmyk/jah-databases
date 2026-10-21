(function(){'use strict';
var PREFIX="JAH-ATK208-";
var METHODS=[["Example embedding", "Encode the example into the same vector space as the archive and run nearest-neighbor search."], ["Feature decomposition", "Break the example into features (topic, structure, style, metadata) and let the caller weight each facet."], ["More-like-this query", "Translate the example into a weighted term query so classic inverted indexes can serve example search."], ["Negative examples", "Accept counter-examples ('like this, not like that') and subtract their vectors to sharpen the neighborhood."], ["Facet-constrained similarity", "Restrict matches to the example's facet (same language, same era) while ranking by overall similarity."], ["Diverse neighborhood sampling", "Return the neighborhood's clusters, not just the top-K nearest, so the caller sees the example's whole family."], ["Example explanation", "Show which features drove each match so the caller learns what 'similar' meant here."], ["Iterative refinement", "Let the caller mark results as good or bad and re-run with the feedback folded into the query vector."], ["Cross-modal examples", "Accept an image as the example for text search (or vice versa) via joint embedding spaces."], ["Partial example matching", "Match on a fragment \u2014 one chapter, one figure \u2014 instead of requiring whole-record similarity."], ["Similarity thresholding", "Cut off results below a calibrated similarity floor rather than returning weak matches to fill K."], ["Example versioning", "Pin the example's version so saved 'more like this' searches reproduce as the archive grows."], ["Batch example search", "Accept several examples and return the union neighborhood with per-example attribution."], ["Cold-start defaults", "When no example exists yet, synthesize a prototype from the caller's description to bootstrap the search."], ["Similarity audit", "Log example, weights, and threshold with results so similarity judgments can be reviewed."]];
var CATS=["similarity", "embeddings", "search"];
var DEMO="# Retrieval-by-Example demo: bag-of-words cosine neighborhood of an example.\nimport math\ndef bow(t):\n    d={}\n    for w in t.lower().split(): d[w]=d.get(w,0)+1\n    return d\ndef cos(a,b):\n    keys=set(a)|set(b)\n    dot=sum(a.get(k,0)*b.get(k,0) for k in keys)\n    na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))\n    return dot/(na*nb) if na and nb else 0.0\nEXAMPLE=\"solar sail propulsion using photon pressure for deep space probes\"\nCANDS=[\"photon pressure drives reflective sails on interstellar probes\",\n       \"sourdough bread baking techniques for beginners\",\n       \"deep space probe navigation with ion thrusters and sails\",\n       \"history of maritime sailing ships\"]\neb=bow(EXAMPLE)\nfor c in sorted(CANDS,key=lambda c:-cos(eb,bow(c))):\n    print(\"%.3f %s\"%(cos(eb,bow(c)),c))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Retrieval-by-Example";
  return {id:id,t:title,title:title,description:"Retrieval-by-example inverts the query box: instead of describing what you want in words, you hand the system one good example and it finds more like it. A researcher with one perfect paper, an engineer with one working configuration, a curator with one ideal record \u2014 each gets a neighborhood of kindred items. Under the hood it is similarity search over embeddings or structured features, with the ",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-retrieval-by-example-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-retrieval-by-example",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();