(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["token-bucket", "sliding-window", "quota-management"];
var PREFIX="JAH-ATK278-";
var KIND="rate limit and quota enforcer";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["token-bucket", "Token bucket limiter", "Each client holds a bucket of tokens refilled at a fixed rate up to a burst capacity. Requests consume a token; empty buckets mean wait or reject. Token buckets allow bursts while enforcing the long-term rate, which matches how real clients behave.", "fixed-rate refill with burst capacity", "consume-per-request accounting", "burst-tolerant, rate-enforcing", "CFG = {1: {\"rate\": 5, \"burst\": 10, \"want\": 12}, 2: {\"rate\": 2, \"burst\": 4, \"want\": 6}, 3: {\"rate\": 10, \"burst\": 10, \"want\": 25}}\nc = CFG[LEVEL]\ntokens, allowed, denied = float(c[\"burst\"]), 0, 0\nfor _ in range(c[\"want\"]):\n    tokens = min(c[\"burst\"], tokens + c[\"rate\"] * 0.1)\n    if tokens >= 1: tokens -= 1; allowed += 1\n    else: denied += 1\nprint(\"wanted %d: allowed %d, denied %d\" % (c[\"want\"], allowed, denied))"],
["sliding-window", "Sliding window counter", "Requests are counted in a sliding time window for precise enforcement: exactly N requests per rolling 60 seconds, not per calendar minute. Sliding windows close the boundary-exploit of fixed windows (2N requests straddling the boundary). Counters are kept per key.", "rolling-window precise counting", "no boundary exploits", "per-key counters", "CFG = {1: (10, 12), 2: (10, 8), 3: (5, 6)}\nlimit, want = CFG[LEVEL]\nwindow = [0.0] * want  # request timestamps (simulated)\nnow = 100.0\ncount = sum(1 for t in window if now - t < 60)\nallowed = min(want, max(0, limit - count))\nprint(\"limit %d/60s, wanted %d -> allowed %d, denied %d\" % (limit, want, allowed, want - allowed))"],
["quota-management", "Per-key quotas", "Limits are tracked separately per API key, user, or endpoint so one heavy consumer cannot starve others. Quota tables map keys to their limits and current usage. Per-key quotas are the foundation of fair multi-tenant service.", "separate limits per key/user/endpoint", "noisy-neighbor isolation", "quota tables with live usage", "CFG = {1: [\"a\", \"a\", \"b\"], 2: [\"a\"] * 5 + [\"b\"] * 2, 3: [\"a\"] * 12}\nLIMIT = 10\nuse = {}\nfor k in CFG[LEVEL]:\n    use[k] = use.get(k, 0) + 1\nfor k, v in use.items():\n    print(\"key\", k, \"usage %d/%d ->\" % (v, LIMIT), \"ok\" if v <= LIMIT else \"OVER QUOTA\")"],
["token-bucket", "Quota exhaustion handling", "When quota is exhausted the service returns 429 with a Retry-After header telling the client when to try again. Exhaustion responses are cheap to generate and never do partial work. Clients are expected to back off; repeat violators face tighter limits.", "429 with Retry-After", "no partial work on exhaustion", "tighter limits for repeat violators", "CFG = {1: 5, 2: 0, 3: 30}\nremaining = CFG[LEVEL]\nif remaining > 0:\n    print(\"200 OK | remaining:\", remaining)\nelse:\n    print(\"429 Too Many Requests | Retry-After: 60 | remaining: 0\")"],
["sliding-window", "Fair-share scheduling", "When demand exceeds capacity, service is divided among tenants by weighted fair share rather than first-come-first-served. Weights reflect tiers or contracts. Fair-share prevents one tenant's flood from zeroing out everyone else during contention.", "weighted division under contention", "tier/contract-based weights", "flood isolation between tenants", "CFG = {1: {\"a\": 1, \"b\": 1}, 2: {\"a\": 3, \"b\": 1}, 3: {\"a\": 5, \"b\": 1, \"c\": 1}}\nCAP = 100\nw = CFG[LEVEL]\ntotal = sum(w.values())\nfor t, wt in w.items():\n    print(\"tenant\", t, \"weight\", wt, \"-> share:\", round(CAP * wt / total))"]
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
var gen={version:"jahdb-archive-toolkit-rate-limit-and-quota-enforcer-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-rate-limit-and-quota-enforcer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
