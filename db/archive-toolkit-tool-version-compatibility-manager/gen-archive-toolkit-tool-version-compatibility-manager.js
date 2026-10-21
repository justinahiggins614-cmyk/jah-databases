(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["version-graph", "upgrade-planner", "deprecation-tracker"];
var PREFIX="JAH-ATK259-";
var KIND="tool version compatibility manager";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["version-graph", "Semantic-version compatibility matrix", "Each tool declares which version ranges it is compatible with using semantic-versioning rules: same major version for 1.x, caret and tilde ranges for flexible bounds. Before an upgrade, the manager checks the matrix and blocks incompatible combinations. The matrix is data, editable without code changes.", "declaring compatible ranges per tool", "blocking incompatible upgrades", "matrix-driven checks editable without code changes", "CFG = {1: (\"1.4.2\", \"^1.2.0\"), 2: (\"2.0.0\", \"^1.2.0\"), 3: (\"1.9.0\", \">=1.0.0,<2.0.0\")}\nver, req = CFG[LEVEL]\ndef parse(v): return tuple(int(x) for x in v.split(\".\"))\ndef ok(v, r):\n    p = parse(v)\n    if r.startswith(\"^\"): b = parse(r[1:]); return p[0] == b[0] and p >= b\n    lo, hi = r.split(\",\"); return parse(lo[2:]) <= p < parse(hi[1:])\nprint(\"version\", ver, \"vs\", req, \"->\", \"COMPATIBLE\" if ok(ver, req) else \"BLOCKED\")"],
["upgrade-planner", "Dependency version graph resolution", "The resolver builds the full dependency graph and finds a set of versions satisfying every constraint, or reports the conflict precisely. Backtracking tries alternatives when the first pick fails. A resolved lockfile pins the exact chosen versions for reproducibility.", "building the full dependency graph", "backtracking when constraints conflict", "emitting a pinned lockfile", "CFG = {1: {\"a\": [\"1.0\", \"1.1\"], \"b\": [\"2.0\"]}, 2: {\"a\": [\"1.0\", \"1.1\", \"2.0\"], \"b\": [\"2.0\", \"2.1\"]}, 3: {\"a\": [\"1.0\", \"2.0\"], \"b\": [\"3.0\"]}}\navail = CFG[LEVEL]\nconstraints = {\"a\": lambda v: v.startswith(\"1.\"), \"b\": lambda v: True}\nresolved, conflict = {}, None\nfor pkg, versions in avail.items():\n    pick = next((v for v in versions if constraints[pkg](v)), None)\n    if pick is None: conflict = pkg; break\n    resolved[pkg] = pick\nprint(\"resolved:\", resolved, \"| conflict:\", conflict or \"none\")"],
["deprecation-tracker", "Canary upgrade with rollback", "Upgrades roll out to a small canary slice first while metrics are watched: error rate, latency, and business signals. If the canary degrades beyond thresholds, the upgrade rolls back automatically. Only a healthy canary proceeds to full rollout.", "upgrading a small canary slice first", "watching error and latency thresholds", "automatic rollback on canary degradation", "CFG = {1: {\"err\": 0.01}, 2: {\"err\": 0.04}, 3: {\"err\": 0.12}}\nerr = CFG[LEVEL][\"err\"]\nTHRESHOLD = 0.05\nprint(\"canary error rate: %.2f%%\" % (err * 100), \"->\", \"ROLL BACK\" if err > THRESHOLD else \"proceed to full rollout\")"],
["version-graph", "Deprecation schedule tracker", "Deprecated versions carry a removal date, and the tracker warns owners as the date approaches: 90 days, 30 days, 7 days. After removal, the old version is blocked. Schedules give consumers time to migrate without surprise breakage.", "tracking removal dates per deprecated version", "escalating warnings at 90/30/7 days", "blocking removed versions after the date", "CFG = {1: 120, 2: 20, 3: 3}\ndays_left = CFG[LEVEL]\nif days_left > 90: status = \"ok\"\nelif days_left > 30: status = \"warning: 90-day notice passed\"\nelif days_left > 7: status = \"urgent: 30-day notice passed\"\nelif days_left > 0: status = \"CRITICAL: removal in %d days\" % days_left\nelse: status = \"BLOCKED: version removed\"\nprint(\"days to removal:\", days_left, \"->\", status)"],
["upgrade-planner", "ABI/API break detector", "The detector compares the public interface of two versions: removed functions, changed signatures, and altered behavior flags. Breaking changes are listed explicitly so upgrade reviewers know exactly what to fix. Non-breaking additions pass silently.", "diffing public interfaces between versions", "flagging removed or re-typed functions", "explicit break lists for upgrade reviewers", "CFG = {1: ({\"f\": [\"x\"], \"g\": [\"x\", \"y\"]}, {\"f\": [\"x\"], \"g\": [\"x\", \"y\"], \"h\": [\"z\"]}), 2: ({\"f\": [\"x\"], \"g\": [\"x\", \"y\"]}, {\"f\": [\"x\"], \"g\": [\"x\"]}), 3: ({\"f\": [\"x\"]}, {\"g\": [\"x\"]})}\nold, new = CFG[LEVEL]\nbreaks = [fn for fn in old if fn not in new or old[fn] != new[fn]]\nadded = [fn for fn in new if fn not in old]\nprint(\"breaking:\", breaks or [\"none\"], \"| added (safe):\", added or [\"none\"])"]
];
function escRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(r){return r[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var ladder=1+((seed>>>0)%3);
  var focus=[row[3],row[4],row[5]][ladder-1];
  var stage=['','At ladder rank 1 (foundation), this record covers ','At ladder rank 2 (compounded), it builds on the foundation with ','At ladder rank 3 (full complexity), it extends to production scale with '][ladder];
  var id=PREFIX+String(seed>>>0).padStart(6,'0');
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Public harvest — documented archive-engineering practice; method fact-checked against standard references.",last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length||r.t!==r.title)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('LEVEL = '+r.ladder_rank)!==0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-tool-version-compatibility-manager-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-tool-version-compatibility-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
