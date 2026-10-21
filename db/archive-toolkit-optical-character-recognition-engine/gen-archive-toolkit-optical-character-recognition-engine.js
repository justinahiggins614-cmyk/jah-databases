(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK141-";
var KIND="extraction method";
var TOOLNAME="Optical Character Recognition Engine";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Template matching", "d": "Template matching slides character prototypes over the image, scoring pixel agreement. It works on clean, fixed fonts with known layouts. Templates are the simplest real OCR.", "c": "fundamentals", "r": 1, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Binarization", "d": "Binarization thresholds grayscale scans into black/white, separating ink from paper. Adaptive thresholds handle uneven lighting. Clean binaries make or break recognition.", "c": "algorithms", "r": 1, "p": {"TEXT": "1", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..']}"}}, {"t": "Segmentation", "d": "Segmentation splits lines into words and words into characters. Connected-component analysis finds character blobs. Good segmentation precedes good recognition.", "c": "implementation", "r": 1, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Feature-based classifiers", "d": "Classifiers use stroke features (loops, endpoints) instead of raw pixels. Features tolerate font variation. Features generalize.", "c": "optimization", "r": 1, "p": {"TEXT": "2", "TMPL": "{'2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Neural OCR", "d": "CNN-RNN models read whole text lines without character segmentation. Sequence models handle cursive and degraded print. Neural OCR leads accuracy today.", "c": "evaluation", "r": 1, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Language models in OCR", "d": "Language models rescore candidate readings by linguistic plausibility. 'teh' becomes 'the' via context. Language knowledge fixes visual ambiguity.", "c": "fundamentals", "r": 2, "p": {"TEXT": "1", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..']}"}}, {"t": "Layout analysis", "d": "Layout analysis finds columns, headings, and tables before text order is decided. Reading order derives from geometry. Structure precedes text.", "c": "algorithms", "r": 2, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Handwriting recognition", "d": "Handwriting models train on writer-varied samples with sequence loss. Cursive needs context no template can give. Handwriting remains the hard case.", "c": "implementation", "r": 2, "p": {"TEXT": "2", "TMPL": "{'2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Multi-script OCR", "d": "Script identification routes each line to the right recognizer. Mixed-script pages need per-line routing. Diversity needs detection.", "c": "optimization", "r": 2, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Confidence scoring", "d": "Per-character confidences flag uncertain readings for review. Low-confidence words route to humans. Confidence enables triage.", "c": "evaluation", "r": 2, "p": {"TEXT": "1", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..']}"}}, {"t": "Dewarping pages", "d": "Dewarping flattens curved book-page geometry before recognition. Text-line straightening restores baselines. Geometry correction rescues bindings.", "c": "fundamentals", "r": 3, "p": {"TEXT": "2", "TMPL": "{'2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Table OCR", "d": "Table OCR detects cell grids then recognizes per cell. Structure plus text gives real tables. Cells need coordinates.", "c": "algorithms", "r": 3, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Batch digitization", "d": "Pipelines scan, OCR, and index in bulk with quality sampling. Throughput needs parallelism. Scale needs automation.", "c": "implementation", "r": 3, "p": {"TEXT": "1", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..']}"}}, {"t": "Evaluating OCR", "d": "Character and word error rates score recognizers on labeled pages. Benchmarks separate marketing from merit. Measurement drives progress.", "c": "optimization", "r": 3, "p": {"TEXT": "12", "TMPL": "{'1': ['..#..', '..#..', '..#..', '..#..', '..#..'], '2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}, {"t": "Searchable PDFs", "d": "OCR text layers hide behind page images in PDFs. Layered PDFs are searchable and selectable. Layers preserve appearance plus text.", "c": "evaluation", "r": 3, "p": {"TEXT": "2", "TMPL": "{'2': ['.###.', '....#', '.###.', '#....', '.###.']}"}}];
var DEMO="# OCR by template matching: 3x5 pixel digit templates matched against an input row.\ntemplates = %%TMPL%%\ndef render(line):\n    # line: string of chars present in templates -> pixel rows\n    rows = [\"\"] * 5\n    for ch in line:\n        t = templates[ch]\n        for i in range(5): rows[i] += t[i] + \" \"\n    return rows\ndef recognize(rows):\n    out = \"\"\n    nchars = len(rows[0]) // 6\n    for c in range(nchars):\n        block = [r[c*6:c*6+5] for r in rows]\n        best, bs = \"?\", -1\n        for ch, t in templates.items():\n            score = sum(a == b for ra, rb in zip(block, t) for a, b in zip(ra, rb))\n            if score > bs: best, bs = ch, score\n        out += best\n    return out\nrows = render(\"%%TEXT%%\")\nprint(\"\\n\".join(rows))\nprint(\"recognized:\", recognize(rows))\n";
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
  if(!new RegExp("^JAH\\-ATK141\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-optical-character-recognition-engine-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-optical-character-recognition-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
