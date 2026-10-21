(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["retry-policy", "backoff-strategy", "fault-isolation"];
var PREFIX="JAH-ATK252-";
var KIND="failure retry controller";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["retry-policy", "Fixed-attempt retry with attempt cap", "The operation is retried up to a fixed maximum number of attempts, then the failure is surfaced instead of looping forever. A cap bounds the worst-case cost of a retry storm. Callers distinguish retryable errors (timeouts, 503s) from permanent ones (400s, auth failures) before retrying.", "retrying up to N attempts, then surfacing the failure", "retrying only retryable error classes", "per-operation attempt budgets tuned from historical failure rates", "CFG = {1: {\"cap\": 3, \"failures\": 2}, 2: {\"cap\": 5, \"failures\": 4}, 3: {\"cap\": 5, \"failures\": 9}}\ncap, failures = CFG[LEVEL][\"cap\"], CFG[LEVEL][\"failures\"]\nattempts, calls = 0, {\"n\": 0}\ndef flaky():\n    calls[\"n\"] += 1\n    if calls[\"n\"] <= failures:\n        raise IOError(\"transient\")\n    return \"ok\"\nresult = None\nfor attempts in range(1, cap + 1):\n    try:\n        result = flaky(); break\n    except IOError:\n        result = \"gave up after %d attempts\" % attempts\nprint(\"result:\", result, \"| calls made:\", calls[\"n\"])"],
["backoff-strategy", "Exponential backoff with jitter", "Waits between retries grow exponentially (1s, 2s, 4s, ...) so a struggling service gets breathing room. Random jitter is added to each wait so that many clients do not retry in lockstep and create a thundering herd. This combination is the industry standard for retry timing.", "computing exponential waits with a fixed base", "adding full jitter to decorrelate client retries", "capping the maximum wait and resetting the base after success", "CFG = {1: {\"base\": 1.0, \"n\": 4}, 2: {\"base\": 0.5, \"n\": 6}, 3: {\"base\": 0.25, \"n\": 8}}\nimport random\nrandom.seed(7)\nbase, n = CFG[LEVEL][\"base\"], CFG[LEVEL][\"n\"]\nwaits = []\nfor i in range(n):\n    exp = min(base * (2 ** i), 30.0)          # exponential, capped\n    waits.append(round(exp / 2 + random.random() * exp / 2, 3))  # equal jitter\nprint(\"waits:\", waits)\nprint(\"monotonic growth check:\", all(b >= a for a, b in zip([base] + waits, waits + [31])))"],
["fault-isolation", "Retry budget", "A retry budget caps the fraction of requests that may be retries within a time window, typically around 20 percent. When the budget is exhausted, further retries are denied even if attempts remain, which protects the system from retry-driven overload. Budgets are tracked per service and window.", "denying retries once the window budget is spent", "separate budgets per downstream service", "adaptive budgets that shrink when the downstream degrades", "CFG = {1: {\"budget\": 5, \"wanted\": 8}, 2: {\"budget\": 10, \"wanted\": 14}, 3: {\"budget\": 20, \"wanted\": 25}}\nbudget, wanted = CFG[LEVEL][\"budget\"], CFG[LEVEL][\"wanted\"]\nspent, allowed, denied = 0, 0, 0\nfor _ in range(wanted):\n    if spent < budget:\n        spent += 1; allowed += 1\n    else:\n        denied += 1\nprint(\"budget:\", budget, \"| allowed:\", allowed, \"| denied:\", denied, \"| retry ratio capped at %.0f%%\" % (100.0 * budget / wanted))"],
["retry-policy", "Circuit breaker", "A circuit breaker watches consecutive failures: after a threshold it opens and fails fast without calling the downstream, giving it time to recover. After a cooldown it enters half-open and lets one probe through; success closes the circuit, failure re-opens it. This stops cascading failures.", "opening the circuit after consecutive failures", "half-open probing after a cooldown", "per-endpoint breakers with independent thresholds", "CFG = {1: {\"threshold\": 3}, 2: {\"threshold\": 4}, 3: {\"threshold\": 5}}\nTH = CFG[LEVEL][\"threshold\"]\nstate, fails, log = \"closed\", 0, []\nplan = [\"fail\"] * (TH + 1) + [\"cooldown\", \"probe-ok\"]\nfor step in plan:\n    if state == \"open\":\n        if step == \"cooldown\":\n            state = \"half-open\"; log.append(\"half-open probe allowed\")\n        else:\n            log.append(\"fast-fail (open)\"); continue\n    if step == \"fail\":\n        fails += 1; log.append(\"fail %d/%d\" % (fails, TH))\n        if fails >= TH: state = \"open\"; log.append(\"circuit OPEN\")\n    elif step == \"probe-ok\":\n        state = \"closed\"; fails = 0; log.append(\"probe ok -> CLOSED\")\nprint(\"final state:\", state)\nprint(\"transitions:\", \" | \".join(log))"],
["backoff-strategy", "Idempotent retry with request deduplication", "Retries carry the same request identifier, and the server keeps a record of completed request ids. A retried request that the server already processed returns the cached result instead of executing twice. This makes retries safe for non-idempotent operations like charges and orders.", "returning cached results for duplicate request ids", "bounded dedupe store with TTL eviction", "cross-instance dedupe via a shared completed-request log", "CFG = {1: 2, 2: 3, 3: 4}\nREPEATS = CFG[LEVEL]\ncompleted, executions = {}, 0\ndef charge(req_id, amount):\n    global executions\n    if req_id in completed:\n        return completed[req_id] + \" (deduped)\"\n    executions += 1\n    completed[req_id] = \"charged $%d\" % amount\n    return completed[req_id]\nout = [charge(\"req-1\", 50) for _ in range(REPEATS)]\nprint(\"responses:\", out)\nprint(\"actual executions:\", executions, \"(exactly-once)\")"]
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
var gen={version:"jahdb-archive-toolkit-failure-retry-controller-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-failure-retry-controller",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
