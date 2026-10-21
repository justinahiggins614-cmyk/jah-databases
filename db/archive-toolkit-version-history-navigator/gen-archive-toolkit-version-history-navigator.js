(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK134-";
var KIND="traversal method";
var TOOLNAME="Version History Navigator";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Linear version chains", "d": "Versions form a chain v1 -> v2 -> v3 with parent pointers. Chain walking answers 'what changed when'. Linear history suits documents.", "c": "fundamentals", "r": 1, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'amy', 'msg': 'init', 'text': 'line1'}, {'n': 2, 'date': '2024-01-02', 'author': 'bob', 'msg': 'fix', 'text': 'line1\\nline2'}]"}}, {"t": "Branching histories", "d": "Branches fork for parallel work; merges rejoin them. DAG history needs topological navigation. Branches enable collaboration.", "c": "algorithms", "r": 1, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'base', 'text': 'x'}, {'n': 2, 'date': '2024-01-02', 'author': 'b', 'msg': 'branch', 'text': 'x\\ny'}]"}}, {"t": "Diff computation", "d": "Diffs align old and new text (Myers algorithm) into add/remove hunks. Hunks make changes reviewable. Diff is the lens on history.", "c": "implementation", "r": 1, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'v1', 'text': 'alpha'}, {'n': 2, 'date': '2024-01-03', 'author': 'a', 'msg': 'v2', 'text': 'alpha\\nbeta'}]"}}, {"t": "Blame annotation", "d": "Blame attributes each line to its last-modifying version. Annotation answers 'who changed this'. Blame is accountability.", "c": "optimization", "r": 1, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'amy', 'msg': 'init', 'text': 'keep'}, {'n': 2, 'date': '2024-02-01', 'author': 'bob', 'msg': 'edit', 'text': 'keep\\nnew'}]"}}, {"t": "Time-travel queries", "d": "'Show me the record as of March' checks out the latest version before a timestamp. Temporal navigation reconstructs past states. Time travel audits history.", "c": "evaluation", "r": 1, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'jan', 'text': 'old'}, {'n': 2, 'date': '2024-06-01', 'author': 'a', 'msg': 'jun', 'text': 'new'}]"}}, {"t": "Version comparison", "d": "Side-by-side views align two arbitrary versions. Comparison works across branches too. Arbitrary diffs support review.", "c": "fundamentals", "r": 2, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'one', 'text': 'A'}, {'n': 3, 'date': '2024-03-01', 'author': 'a', 'msg': 'three', 'text': 'A\\nC'}]"}}, {"t": "Revert operations", "d": "Revert creates a new version restoring old content; history stays append-only. Reverts are safe because nothing is rewritten. Append-only history is trustworthy.", "c": "algorithms", "r": 2, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'good', 'text': 'fine'}, {'n': 2, 'date': '2024-01-02', 'author': 'b', 'msg': 'bad', 'text': 'broken'}]"}}, {"t": "Tagging releases", "d": "Tags name versions (v2.0) for stable reference. Tags move navigation from numbers to meaning. Named versions are citable.", "c": "implementation", "r": 2, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'release', 'text': 'stable'}, {'n': 2, 'date': '2024-02-01', 'author': 'a', 'msg': 'dev', 'text': 'stable\\nwip'}]"}}, {"t": "Merge-base finding", "d": "The merge base is the newest common ancestor of two versions. Diffs against the base show each side's changes. Base-finding enables three-way merge.", "c": "optimization", "r": 2, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'base', 'text': 'root'}, {'n': 2, 'date': '2024-01-05', 'author': 'b', 'msg': 'side', 'text': 'root\\nleaf'}]"}}, {"t": "Cherry-picking", "d": "Cherry-pick replays one version's changes onto another line. Selective replay shares fixes across branches. Picking is surgical history reuse.", "c": "evaluation", "r": 2, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'base', 'text': 'x'}, {'n': 2, 'date': '2024-01-02', 'author': 'a', 'msg': 'fix', 'text': 'x\\nfixed'}]"}}, {"t": "History search", "d": "'When did this line change' searches diffs across versions (pickaxe search). Content-history search finds the introduction of any text. Searchable history is debuggable history.", "c": "fundamentals", "r": 3, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'init', 'text': 'start'}, {'n': 2, 'date': '2024-04-01', 'author': 'a', 'msg': 'add', 'text': 'start\\nneedle'}]"}}, {"t": "Shallow history", "d": "Shallow clones fetch recent versions only, deepening on demand. Shallowness speeds initial access. Depth trades completeness for speed.", "c": "algorithms", "r": 3, "p": {"A": "0", "B": "0", "VERSIONS": "[{'n': 5, 'date': '2024-05-01', 'author': 'a', 'msg': 'recent', 'text': 'now'}]"}}, {"t": "Signed versions", "d": "Signatures attest authorship per version. Verification builds a trust chain. Signed history resists tampering.", "c": "implementation", "r": 3, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'amy', 'msg': 'signed', 'text': 'trusted'}, {'n': 2, 'date': '2024-01-02', 'author': 'amy', 'msg': 'signed2', 'text': 'trusted\\nmore'}]"}}, {"t": "Retention policies", "d": "Old versions age out per policy, keeping history bounded. Policies balance audit needs against storage. Retention is governance.", "c": "optimization", "r": 3, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 10, 'date': '2024-10-01', 'author': 'a', 'msg': 'keep', 'text': 'latest'}, {'n': 11, 'date': '2024-11-01', 'author': 'a', 'msg': 'keep2', 'text': 'latest\\nmore'}]"}}, {"t": "History visualization", "d": "DAG renderers draw branches, merges, and tags. Visualization makes complex histories legible. Graphs beat log lists.", "c": "evaluation", "r": 3, "p": {"A": "0", "B": "1", "VERSIONS": "[{'n': 1, 'date': '2024-01-01', 'author': 'a', 'msg': 'root', 'text': 'r'}, {'n': 2, 'date': '2024-01-02', 'author': 'b', 'msg': 'leaf', 'text': 'r\\nl'}]"}}];
var DEMO="# Version history: walk a version chain, diff adjacent versions, blame a line.\nversions = %%VERSIONS%%\ndef show(v):\n    print(f\"--- v{v['n']} ({v['date']}) by {v['author']}: {v['msg']}\")\nchain = sorted(versions, key=lambda v: v[\"n\"])\nfor v in chain: show(v)\na, b = chain[%%A%%], chain[%%B%%]\nla, lb = a[\"text\"].splitlines(), b[\"text\"].splitlines()\nprint(f\"\\ndiff v{a['n']} -> v{b['n']}:\")\nfor line in lb:\n    if line not in la: print(\"  +\", line)\nfor line in la:\n    if line not in lb: print(\"  -\", line)\n";
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
  if(!new RegExp("^JAH\\-ATK134\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-version-history-navigator-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-version-history-navigator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
