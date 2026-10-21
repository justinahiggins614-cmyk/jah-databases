(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK114-";
var KIND="search method";
var TOOLNAME="Mathematical Expression Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Expression tree canonicalization", "d": "Expressions parse into trees; canonicalization rewrites them into a normal form where equivalent expressions share one representation. Commutative operators sort their operands, variables rename to VAR, constants to NUM. Canonical forms turn structural matching into string equality.", "c": "fundamentals", "r": 1, "p": {"QUERY": "b + a", "CORPUS": "{'e1': 'a + b', 'e2': 'a * b', 'e3': 'x + y + z'}"}}, {"t": "Operator tree versus layout tree", "d": "Layout trees capture how an expression looks (fractions, superscripts); operator trees capture what it means. Search by meaning uses operator trees; search by appearance uses layout trees. Choosing the wrong tree is why some formula searches miss obvious equivalents.", "c": "algorithms", "r": 1, "p": {"QUERY": "a+b", "CORPUS": "{'e1': 'b+a', 'e2': 'a-b'}"}}, {"t": "MathML encoding", "d": "Content MathML encodes operator trees in XML; Presentation MathML encodes layout. Archives store one or both, and search normalizes from either. Standard encodings let tools share formula corpora.", "c": "implementation", "r": 1, "p": {"QUERY": "x^2", "CORPUS": "{'e1': 'x**2', 'e2': 'x**3'}"}}, {"t": "LaTeX formula parsing", "d": "Most published math arrives as LaTeX; parsers convert it to operator trees despite LaTeX's layout orientation. Ambiguities like juxtaposition (multiplication or function application) need heuristic resolution. Robust LaTeX parsing unlocks the entire scientific literature for formula search.", "c": "optimization", "r": 1, "p": {"QUERY": "\\frac{a}{b}", "CORPUS": "{'e1': 'a/b', 'e2': 'a*b'}"}}, {"t": "Subexpression search", "d": "Queries often target subexpressions: find papers using 'x^2 + y^2' anywhere in a larger formula. Indexing all subtrees of each expression makes subexpression queries a lookup. Subtree indexes are the formula analogue of n-gram indexes.", "c": "evaluation", "r": 1, "p": {"QUERY": "x + y", "CORPUS": "{'e1': '(x + y) * z', 'e2': 'x * y'}"}}, {"t": "Unification-based matching", "d": "Unification matches patterns with variables against concrete expressions, binding variables consistently. The query 'a + ?x' unifies with 'b + c^2' binding ?x to 'c^2'. Unification gives formula search the power of logic programming.", "c": "fundamentals", "r": 2, "p": {"QUERY": "a + b", "CORPUS": "{'e1': 'p + q', 'e2': 'p - q'}"}}, {"t": "Similarity over exact match", "d": "Exact structural match is brittle; similarity scores count shared subtrees or aligned nodes. Tree edit distance generalizes string edit distance to expression trees. Similarity ranking finds 'close' formulas when nothing matches exactly.", "c": "algorithms", "r": 2, "p": {"QUERY": "a + b + c", "CORPUS": "{'e1': 'a + b', 'e2': 'x + y + z'}"}}, {"t": "Symbol disambiguation", "d": "The same symbol means different things per field: 'e' is Euler's number, charge, or eccentricity. Context (surrounding text, subject classification) selects the interpretation. Disambiguation keeps physics formulas out of pure-math result sets.", "c": "implementation", "r": 2, "p": {"QUERY": "e", "CORPUS": "{'e1': 'e', 'e2': 'x'}"}}, {"t": "Dimensional analysis", "d": "Physical formulas carry units; dimensional checking rejects matches with incompatible dimensions. A search for energy formulas can require ML^2T^-2 dimensionality. Units turn formula search from syntactic to physically meaningful.", "c": "optimization", "r": 2, "p": {"QUERY": "m * v", "CORPUS": "{'e1': 'm*v', 'e2': 'm+v'}"}}, {"t": "Formula embeddings", "d": "Neural models embed expressions into vectors where algebraic equivalents cluster. Embedding search complements symbolic methods on paraphrased or rearranged formulas. Hybrid symbolic-neural pipelines currently lead benchmarks.", "c": "evaluation", "r": 2, "p": {"QUERY": "a*b", "CORPUS": "{'e1': 'b*a', 'e2': 'a+b'}"}}, {"t": "Handwritten formula recognition", "d": "Offline recognition converts photographed or penned math into operator trees. Segmentation splits strokes into symbols; structural analysis rebuilds the tree. Recognized formulas then enter the same search indexes as born-digital ones.", "c": "fundamentals", "r": 3, "p": {"QUERY": "x_1", "CORPUS": "{'e1': 'x_1', 'e2': 'x_2'}"}}, {"t": "Equation numbering and references", "d": "Papers cite equations by number ('by (3)'); resolvers link citations to the actual formula. Reference graphs connect derivations across papers. Citation-aware search follows the math, not just the text.", "c": "algorithms", "r": 3, "p": {"QUERY": "a^2 + b^2", "CORPUS": "{'e1': 'a**2 + b**2', 'e2': 'c**2'}"}}, {"t": "Computer algebra normalization", "d": "CAS systems expand, factor, and simplify to canonical forms stronger than syntactic normalization. 'sin^2+cos^2' normalizes to 1 under trigonometric rules. CAS-backed search finds mathematically equal but textually distant formulas.", "c": "implementation", "r": 3, "p": {"QUERY": "2*x", "CORPUS": "{'e1': 'x + x', 'e2': 'x * 3'}"}}, {"t": "Query languages for math", "d": "Formula query languages mix structure patterns with text keywords and constraints. Users sketch the shape of the wanted equation and constrain symbols. Purpose-built query languages beat keyword search for math-heavy archives.", "c": "optimization", "r": 3, "p": {"QUERY": "a - b", "CORPUS": "{'e1': 'a - b', 'e2': 'b - a'}"}}, {"t": "Benchmarking formula retrieval", "d": "Benchmarks like NTCIR Math tasks score systems on known formula queries over arXiv corpora. Metrics adapt information-retrieval measures to partial structural relevance. Shared benchmarks drive the field forward.", "c": "evaluation", "r": 3, "p": {"QUERY": "x + 1", "CORPUS": "{'e1': 'x + 1', 'e2': 'x + 2'}"}}];
var DEMO="# Math expression search: normalize expression trees (commutativity, renaming),\n# then compare canonical forms.\nimport ast, re\ndef canon(node):\n    if isinstance(node, ast.BinOp):\n        l, r = canon(node.left), canon(node.right)\n        op = type(node.op).__name__\n        if op in (\"Add\", \"Mult\"):\n            return \"(\" + op + \" \" + \" \".join(sorted([l, r])) + \")\"\n        if op == \"Sub\": return \"(Add \" + l + \" (Neg \" + r + \"))\"\n        return \"(\" + op + \" \" + l + \" \" + r + \")\"\n    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):\n        return \"(Neg \" + canon(node.operand) + \")\"\n    if isinstance(node, ast.Name): return \"VAR\"\n    if isinstance(node, ast.Constant): return \"NUM\"\n    return \"?\"\ndef normalize(expr):\n    # tiny LaTeX bridge: \frac{a}{b} -> (a)/(b)\n    if expr.startswith(\"\\\\frac{\"):\n        inner = expr[6:]\n        a, b = inner[:-1].split(\"}{\")\n        expr = \"(\" + a + \")/(\" + b + \")\"\n    return canon(ast.parse(expr, mode=\"eval\").body)\ncorpus = %%CORPUS%%\nquery = r\"%%QUERY%%\"\nqc = normalize(query)\nprint(\"query canonical form:\", qc)\nfor name, expr in corpus.items():\n    ec = normalize(expr)\n    print((\"MATCH \" if ec == qc else \"      \") + f\"{name}: {expr} -> {ec}\")\n";
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
  if(!new RegExp("^JAH\\-ATK114\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-mathematical-expression-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-mathematical-expression-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
