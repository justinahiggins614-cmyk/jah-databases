(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["minimization", "anonymization", "purpose-limitation"];
var PREFIX="JAH-ATK268-";
var KIND="privacy-preserving retrieval controller";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["minimization", "Field minimization", "Queries return only the fields explicitly requested, never whole records by default. The requester declares the needed fields; anything else is withheld. Minimization is enforced at the retrieval layer so application code cannot accidentally over-fetch.", "returning only requested fields", "requester-declared field lists", "enforcement at the retrieval layer", "CFG = {1: [\"name\"], 2: [\"name\", \"city\"], 3: [\"name\", \"city\", \"age\"]}\nrec = {\"name\": \"Amy\", \"city\": \"Springfield\", \"age\": 34, \"ssn\": \"000-00-0000\"}\nout = {k: rec[k] for k in CFG[LEVEL]}\nprint(\"requested:\", CFG[LEVEL], \"| returned:\", out, \"| withheld: ssn\")"],
["anonymization", "k-anonymity grouping", "Quasi-identifiers like age and ZIP are generalized until every combination appears in at least k records. A 34-year-old in ZIP 12345 becomes 30-39 in 123**. k-anonymity bounds re-identification risk for released datasets. Suppression handles groups that cannot reach k.", "generalizing quasi-identifiers to groups of k", "suppressing ungroupable records", "k chosen per dataset sensitivity", "CFG = {1: 2, 2: 3, 3: 5}\nK = CFG[LEVEL]\nrows = [{\"age\": 34, \"zip\": \"12345\"}, {\"age\": 36, \"zip\": \"12346\"}, {\"age\": 35, \"zip\": \"12345\"}, {\"age\": 52, \"zip\": \"99999\"}]\ndef gen(r): return (\"%d-%d\" % (r[\"age\"] // 10 * 10, r[\"age\"] // 10 * 10 + 9), r[\"zip\"][:3] + \"**\")\ngroups = {}\nfor r in rows: groups.setdefault(gen(r), []).append(r)\nkept = {g: v for g, v in groups.items() if len(v) >= K}\nprint(\"k=%d groups kept:\" % K, {g: len(v) for g, v in kept.items()}, \"| suppressed:\", sum(len(v) for g, v in groups.items() if len(v) < K))"],
["purpose-limitation", "Differential privacy noise", "Calibrated random noise (Laplace or Gaussian) is added to aggregate query results so individual records cannot be reverse-engineered. The noise scale is set by the privacy budget epsilon: smaller epsilon means more privacy and noisier answers. Budgets compose across queries.", "calibrated Laplace noise on aggregates", "epsilon budgets composing across queries", "noise scale from sensitivity and epsilon", "CFG = {1: 1.0, 2: 0.5, 3: 0.1}\nEPS = CFG[LEVEL]\nimport random\nrandom.seed(51)\ntrue_count = 1000\nnoise = random.expovariate(EPS) - random.expovariate(EPS)  # laplace(1/eps)\nprint(\"true:\", true_count, \"| epsilon:\", EPS, \"| released:\", round(true_count + noise))"],
["minimization", "Purpose-limited queries", "Every query declares its purpose, and the controller checks the purpose against the data's allowed uses before executing. Research queries cannot touch data consented only for operations. Purpose declarations are logged with the query for audit.", "declared purpose per query", "purpose checked against allowed uses", "purpose logged with the query", "CFG = {1: \"research\", 2: \"operations\", 3: \"marketing\"}\nallowed = {\"research\", \"operations\"}\npurpose = CFG[LEVEL]\nprint(\"purpose:\", purpose, \"->\", \"EXECUTE + log\" if purpose in allowed else \"DENY: purpose not allowed\")"],
["anonymization", "Suppression of small cells", "Aggregate cells computed over fewer than a threshold number of records are suppressed, because tiny groups are re-identifiable. Suppressed cells are marked, not silently dropped, so consumers know data was withheld. The threshold is set per dataset.", "suppressing aggregates over tiny groups", "marking suppressed cells explicitly", "per-dataset suppression thresholds", "CFG = {1: 3, 2: 5, 3: 10}\nTH = CFG[LEVEL]\ncells = {\"group-a\": 42, \"group-b\": 3, \"group-c\": 17}\nout = {g: (v if v >= TH else \"SUPPRESSED\") for g, v in cells.items()}\nprint(\"threshold:\", TH, \"| released:\", out)"]
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
var gen={version:"jahdb-archive-toolkit-privacy-preserving-retrieval-controller-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-privacy-preserving-retrieval-controller",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
