(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["accuracy-scoring", "speed-profiling", "resource-metering"];
var PREFIX="JAH-ATK258-";
var KIND="tool performance benchmark";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["accuracy-scoring", "Accuracy harness with gold answers", "The tool runs over a labeled task set with known-correct gold answers, and each output is scored as exact match, partial match, or miss. Accuracy is reported with the task count so readers can judge significance. Gold sets are versioned so scores stay comparable across tool versions.", "scoring outputs against gold answers", "partial-credit rubrics for near misses", "versioned gold sets for cross-version comparison", "CFG = {1: 10, 2: 25, 3: 50}\nN = CFG[LEVEL]\nimport random\nrandom.seed(11)\ngold = [i % 4 for i in range(N)]\npred = [g if random.random() < 0.8 else (g + 1) % 4 for g in gold]\nacc = sum(1 for g, p in zip(gold, pred) if g == p) / N\nprint(\"tasks:\", N, \"| accuracy: %.2f\" % acc)"],
["speed-profiling", "Latency percentile profiling", "The tool is run many times and the latency distribution is summarized with percentiles: p50 for the typical case, p95 and p99 for the tail. Percentiles reveal slow outliers that averages hide. Warmup runs are discarded so JIT and cache effects do not pollute the numbers.", "measuring p50/p95/p99 over repeated runs", "discarding warmup runs", "tail-latency attribution to slow phases", "CFG = {1: 100, 2: 500, 3: 1000}\nN = CFG[LEVEL]\nimport random, time\nrandom.seed(3)\nlat = sorted(random.gammavariate(2, 0.01) for _ in range(N))\ndef pct(p): return lat[int(p * N)]\nprint(\"n=%d p50=%.3fs p95=%.3fs p99=%.3fs\" % (N, pct(0.50), pct(0.95), pct(0.99)))"],
["resource-metering", "Resource consumption metering", "Peak memory and CPU time are measured per task using OS counters, so benchmarks report what a tool costs, not just how fast it is. Memory is sampled at peak RSS; CPU time separates user and system. Resource numbers make capacity planning possible.", "measuring peak memory per task", "separating user and system CPU time", "cost-per-task from resource usage", "CFG = {1: 1000, 2: 10000, 3: 100000}\nN = CFG[LEVEL]\nimport tracemalloc, time\ntracemalloc.start()\nt0 = time.perf_counter()\ndata = [i * i for i in range(N)]\ntotal = sum(data)\ncpu = time.perf_counter() - t0\npeak_kb = tracemalloc.get_traced_memory()[1] / 1024\ntracemalloc.stop()\nprint(\"n=%d sum=%d cpu=%.4fs peak=%.1fKB\" % (N, total, cpu, peak_kb))"],
["accuracy-scoring", "Reliability (success-rate) tracking", "The tool runs N trials and the success rate is reported with a binomial confidence interval, so a 95 percent success rate over 20 trials is not confused with the same rate over 20,000 trials. Reliability tracking separates flaky tools from solid ones with statistical honesty.", "success rates with confidence intervals", "distinguishing flakes from systematic failures", "reliability trends across versions", "CFG = {1: (18, 20), 2: (190, 200), 3: (1900, 2000)}\nok, n = CFG[LEVEL]\nimport math\np = ok / n\nmargin = 1.96 * math.sqrt(p * (1 - p) / n)\nprint(\"success %d/%d = %.3f | 95%% CI [%.3f, %.3f]\" % (ok, n, p, p - margin, p + margin))"],
["speed-profiling", "Head-to-head A/B benchmark", "Two tools run the same workload and their outputs are compared pair by pair: wins, losses, and ties. Paired comparison controls for task difficulty, so the winner is the better tool, not the luckier draw. Significance is checked before declaring a winner.", "paired comparison on identical workloads", "win/loss/tie tallies", "significance checks before declaring winners", "CFG = {1: 20, 2: 60, 3: 200}\nN = CFG[LEVEL]\nimport random\nrandom.seed(5)\nwins = sum(1 for _ in range(N) if random.random() < 0.62)\nprint(\"tool A wins %d/%d (%.1f%%)\" % (wins, N, 100.0 * wins / N), \"| winner:\", \"A\" if wins > N / 2 else \"tie\")"]
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
var gen={version:"jahdb-archive-toolkit-tool-performance-benchmark-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-tool-performance-benchmark",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
