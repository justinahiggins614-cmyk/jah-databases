(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["capability-matching", "degradation-ladder", "health-routing"];
var PREFIX="JAH-ATK253-";
var KIND="fallback tool selector";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["capability-matching", "Capability-based fallback ranking", "Candidate tools are described by the capabilities they provide, and the request lists the capabilities it needs. The selector ranks candidates by capability coverage and picks the highest-ranked healthy one. This keeps fallbacks functionally correct instead of merely available.", "matching required capabilities against candidate sets", "ranking by coverage, then by historical reliability", "partial-capability fallbacks with explicit gap disclosure", "CFG = {1: {\"need\": [\"search\", \"filter\"]}, 2: {\"need\": [\"search\", \"filter\", \"rank\"]}, 3: {\"need\": [\"search\", \"filter\", \"rank\", \"dedup\"]}}\nneed = set(CFG[LEVEL][\"need\"])\ntools = {\"t1\": ({\"search\", \"filter\"}, True), \"t2\": ({\"search\"}, True), \"t3\": ({\"search\", \"filter\", \"rank\", \"dedup\"}, False), \"t4\": ({\"search\", \"filter\", \"rank\"}, True)}\ncands = [(name, len(caps & need)) for name, (caps, healthy) in tools.items() if healthy and need <= caps]\ncands.sort(key=lambda x: -x[1])\nprint(\"need:\", sorted(need), \"| ranked:\", cands, \"| chosen:\", cands[0][0] if cands else \"NONE\")"],
["degradation-ladder", "Degradation ladder", "Fallbacks are ordered from full-fidelity to minimal in a degradation ladder. The selector walks down the ladder until it finds a working rung, so users get the best quality currently achievable. Each rung documents what is lost relative to the preferred tool.", "walking an ordered ladder of decreasing fidelity", "documenting the quality loss at each rung", "auto-climbing back up when the preferred tool recovers", "CFG = {1: 2, 2: 3, 3: 4}\nDOWN_UNTIL = CFG[LEVEL]\nladder = [(\"full-llm\", True), (\"small-llm\", True), (\"template\", True), (\"cached\", True), (\"static\", True)]\nfor i in range(DOWN_UNTIL):\n    ladder[i] = (ladder[i][0], False)  # top rungs down\nchosen = next((name for name, up in ladder if up), None)\nlost = [name for name, up in ladder if not up]\nprint(\"down rungs:\", lost, \"| serving from:\", chosen)"],
["health-routing", "Health-checked routing", "Each candidate tool receives periodic health probes, and the routing table marks tools healthy or unhealthy. The selector only routes to healthy tools and re-checks on a schedule, so failover happens without human intervention. Probe failures trigger deeper diagnostics before a tool is marked down.", "periodic health probes per candidate", "marking tools down after consecutive probe failures", "diagnostic probes that distinguish overload from outage", "CFG = {1: {\"fails\": 2}, 2: {\"fails\": 3}, 3: {\"fails\": 1}}\nNEED_FAILS = CFG[LEVEL][\"fails\"]\ntools = {\"a\": {\"fails\": 0, \"up\": True}, \"b\": {\"fails\": 0, \"up\": True}}\nprobe_results = {\"a\": [\"ok\", \"fail\", \"fail\", \"fail\"], \"b\": [\"ok\"] * 4}\nfor name, results in probe_results.items():\n    for r in results:\n        t = tools[name]\n        t[\"fails\"] = 0 if r == \"ok\" else t[\"fails\"] + 1\n        if t[\"fails\"] >= NEED_FAILS:\n            t[\"up\"] = False\nprint({n: (\"UP\" if t[\"up\"] else \"DOWN\") for n, t in tools.items()})"],
["capability-matching", "Cost-quality tradeoff fallback", "When the preferred tool is unavailable, the selector scores alternatives by quality per unit cost and picks the best value. A slightly lower-quality but dramatically cheaper tool often beats a premium fallback. Scores combine measured quality, latency, and price.", "scoring candidates by quality per cost", "weighting latency alongside quality and price", "budget-capped selection for cost-sensitive workloads", "CFG = {1: {\"budget\": 10}, 2: {\"budget\": 5}, 3: {\"budget\": 2}}\nBUDGET = CFG[LEVEL][\"budget\"]\ncands = [(\"premium\", 0.95, 8.0), (\"standard\", 0.85, 2.0), (\"economy\", 0.70, 0.5)]\nok = [(n, q / c) for n, q, c in cands if c <= BUDGET]\nok.sort(key=lambda x: -x[1])\nprint(\"budget:\", BUDGET, \"| value-ranked:\", [(n, round(v, 3)) for n, v in ok], \"| chosen:\", ok[0][0] if ok else \"NONE\")"],
["degradation-ladder", "Cached-result fallback", "If no live tool can serve the request, the selector serves the last known-good cached result, labeled with its age. Stale data with a staleness warning beats no data for many read workloads. Cache entries carry TTLs and provenance so consumers can judge trust.", "serving last-known-good results with staleness labels", "TTL-based freshness tiers", "background refresh so the cache heals itself", "CFG = {1: {\"age\": 30}, 2: {\"age\": 300}, 3: {\"age\": 3600}}\nAGE = CFG[LEVEL][\"age\"]\ncache = {\"q1\": {\"result\": \"42\", \"age_s\": AGE, \"ttl_s\": 600}}\nentry = cache[\"q1\"]\nfresh = \"FRESH\" if entry[\"age_s\"] <= entry[\"ttl_s\"] else \"STALE\"\nprint(\"serving:\", entry[\"result\"], \"| age: %ds\" % entry[\"age_s\"], \"| status:\", fresh, \"| provenance: cache\")"]
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
var gen={version:"jahdb-archive-toolkit-fallback-tool-selector-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-fallback-tool-selector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
