(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK109-";
var KIND="search method";
var TOOLNAME="Image Similarity Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Color histogram descriptors", "d": "A color histogram counts pixels per quantized color bin, giving a compact global signature of an image. Histograms ignore layout, so two different beach photos match while a beach and a forest do not. They are cheap to compute and surprisingly effective for coarse similarity.", "c": "fundamentals", "r": 1, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Edge and texture features", "d": "Texture descriptors like local binary patterns encode how brightness varies in small neighborhoods. They capture surface qualities (smooth, rough, striped) that color alone misses. Texture plus color together separate images that either feature alone confuses.", "c": "algorithms", "r": 1, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [5,5,1,1], 'img2': [5,4,2,1], 'img3': [1,1,5,5], 'img4': [4,5,1,2]}"}}, {"t": "SIFT keypoint matching", "d": "SIFT finds scale-invariant keypoints and describes each with a gradient-orientation histogram. Two images match when enough keypoint descriptors pair up under a ratio test against the second-best match. Keypoint methods survive cropping, rotation, and partial occlusion.", "c": "implementation", "r": 1, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [9,1,1,2], 'img2': [8,2,1,2], 'img3': [1,8,2,1], 'img4': [2,1,9,1]}"}}, {"t": "Bag of visual words", "d": "Visual words quantize local descriptors into a vocabulary, and each image becomes a histogram over that vocabulary. TF-IDF weighting downplays common visual words, mirroring text retrieval exactly. The model turns image search into the same inverted-index machinery as keyword search.", "c": "optimization", "r": 1, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [6,0,3,1], 'img2': [5,1,3,1], 'img3': [0,6,1,3], 'img4': [1,0,6,3]}"}}, {"t": "Deep embedding vectors", "d": "Convolutional networks trained on classification produce embedding vectors where similar images sit close together. Cosine or Euclidean distance in embedding space replaces hand-crafted descriptors. Embeddings capture semantic similarity ('two dogs') beyond pixel similarity.", "c": "evaluation", "r": 1, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [0.9,0.1,0.2], 'img2': [0.85,0.15,0.25], 'img3': [0.1,0.9,0.2], 'img4': [0.2,0.1,0.9]}"}}, {"t": "Cosine similarity ranking", "d": "Cosine similarity measures the angle between feature vectors, ignoring their magnitude. This makes it robust to brightness scaling, where Euclidean distance would overreact. Ranking by cosine is the default for normalized embedding vectors.", "c": "fundamentals", "r": 2, "p": {"QUERY": "img2", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Spatial pyramid matching", "d": "Spatial pyramids split the image into increasingly fine grids and pool features per cell, then concatenate. Coarse levels capture global layout while fine levels capture local detail. Pyramids restore the spatial information that pure histograms throw away.", "c": "algorithms", "r": 2, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [4,4,2,2], 'img2': [4,3,2,3], 'img3': [2,2,4,4], 'img4': [3,4,3,2]}"}}, {"t": "Perceptual hashing", "d": "Perceptual hashes shrink an image to a short bit string (e.g. 64 bits) where similar images differ in few bits. Hamming distance between hashes gives near-duplicate detection in constant time per comparison. Hashes are tiny enough to index billions of images.", "c": "implementation", "r": 2, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [10,0,0,0], 'img2': [9,1,0,0], 'img3': [0,0,10,0], 'img4': [0,10,0,0]}"}}, {"t": "Region-based queries", "d": "Users can query with a cropped region instead of a whole image; the system matches region descriptors. This finds objects within larger scenes rather than requiring globally similar images. Region queries turn similarity search into visual object lookup.", "c": "optimization", "r": 2, "p": {"QUERY": "img3", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Sketch-based retrieval", "d": "Sketches are matched by edge-orientation descriptors that ignore color and texture entirely. The query pipeline extracts contours from the sketch and compares against image edge maps. Sketch search bridges the gap between what users can draw and what cameras capture.", "c": "evaluation", "r": 2, "p": {"QUERY": "img4", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Relevance feedback", "d": "Users mark results relevant or not, and the query vector shifts toward relevant examples and away from rejected ones. Rocchio-style updates in feature space refine the search without new keywords. Two or three feedback rounds typically transform mediocre results.", "c": "fundamentals", "r": 3, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Approximate nearest neighbors", "d": "Exact nearest-neighbor search is too slow at scale; ANN indexes (HNSW, IVF) trade a little recall for orders of magnitude in speed. Graph-based HNSW navigates from entry points down through layers to the neighborhood. ANN is what makes billion-image similarity search interactive.", "c": "algorithms", "r": 3, "p": {"QUERY": "img2", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}, {"t": "Multi-feature fusion", "d": "No single descriptor wins everywhere, so systems fuse color, texture, and deep features with learned weights. Late fusion merges ranked lists; early fusion concatenates vectors before indexing. Fusion consistently beats the best single feature on benchmark suites.", "c": "implementation", "r": 3, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [6,6,2,2], 'img2': [6,5,2,3], 'img3': [2,2,6,6], 'img4': [5,6,3,2]}"}}, {"t": "Duplicate clustering", "d": "Near-duplicate detection clusters images whose pairwise distance falls below a tight threshold. Union-find over thresholded pairs groups resized, recompressed, and slightly edited copies. Clustering dedupes crawled collections that would otherwise drown in copies.", "c": "optimization", "r": 3, "p": {"QUERY": "img1", "TOPK": "3", "IMAGES": "{'img1': [10,1,1,1], 'img2': [10,1,1,2], 'img3': [1,10,1,1], 'img4': [1,1,10,1]}"}}, {"t": "Evaluation with precision at k", "d": "Image retrieval is scored by precision@k and mean average precision over labeled query sets. Ground truth marks which corpus images count as similar to each query. Standard benchmarks keep descriptor comparisons honest across papers and products.", "c": "evaluation", "r": 3, "p": {"QUERY": "img3", "TOPK": "3", "IMAGES": "{'img1': [8,2,1,1], 'img2': [7,3,1,1], 'img3': [1,1,8,2], 'img4': [2,1,1,8]}"}}];
var DEMO="# Image similarity: cosine similarity over feature vectors (color/texture descriptors).\nimport math\nimages = %%IMAGES%%\ndef cosine(a, b):\n    dot = sum(x*y for x, y in zip(a, b))\n    na = math.sqrt(sum(x*x for x in a)); nb = math.sqrt(sum(x*x for x in b))\n    return dot / (na * nb) if na and nb else 0.0\nquery = \"%%QUERY%%\"\nqv = images[query]\nranked = sorted(((cosine(qv, v), name) for name, v in images.items() if name != query), reverse=True)\nprint(\"Query image:\", query)\nfor score, name in ranked[:%%TOPK%%]:\n    print(f\"  {name}: similarity {score:.3f}\")\n";
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
  if(!new RegExp("^JAH\\-ATK109\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-image-similarity-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-image-similarity-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
