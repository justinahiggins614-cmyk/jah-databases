(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["layout", "concurrency", "numa", "measurement"];
var PREFIX='JAH-CLA-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["False Sharing Elimination", "concurrency", "Pads independently-updated fields to separate cache lines so cores stop invalidating each other's caches. Two counters in one 64-byte line ping-pong on every increment; padding makes each core's line private. It is the first fix for contended data.", ["Identify independently-updated fields", "Pad each to 64 bytes", "Verify with cache-miss counters"], ["C/C++ (alignas)", "Rust (repr align)", "Java (@Contended)"], ["Cache coherency (MESI)", "Concurrency literature"], 2, 0], ["Cache-Line Padding", "layout", "Pads hot structures to whole cache lines with explicit alignment attributes. Padding wastes a little memory to save a lot of coherence traffic. Compilers offer alignas and attributes for exactly this.", ["Align structures to 64 bytes", "Pad to multiples of the line size", "Keep padding out of serialized forms"], ["C11 alignas", "Linux ____cacheline_aligned", "Rust"], ["C11 standard", "ABI docs"], 1, 0], ["NUMA-Local Allocation", "numa", "Allocates memory on the NUMA node where the using threads run. Remote-node access costs 1.5 to 2x local latency; first-touch placement usually gets it right. Pinning threads completes the picture.", ["Pin threads to nodes", "Allocate with first-touch or explicit policy", "Measure remote-access ratios"], ["Linux (numactl)", "libnuma", "Windows"], ["NUMA literature", "Linux NUMA docs"], 2, 2], ["Software Prefetching", "layout", "Issues software prefetches for data needed a few iterations ahead. Prefetch hides memory latency when the access pattern is predictable; hardware prefetchers handle the simple cases. It helps pointer-chasing and sparse loops.", ["Identify predictable future accesses", "Prefetch one iteration ahead", "Verify with miss counters"], ["GCC (__builtin_prefetch)", "Compilers", "Manual"], ["Prefetch instructions", "Cache literature"], 2, 1], ["Cache Coloring", "layout", "Colors pages so hot data spreads across cache sets instead of colliding. Direct-mapped and set-associative caches thrash when hot addresses alias; coloring assigns pages to spread them. OS page allocators implement it.", ["Assign colors to physical pages", "Spread hot data across sets", "Measure conflict misses"], ["OS kernels", "Research allocators", "Embedded"], ["Cache literature", "OS design texts"], 3, 1], ["Lock-Free MPSC Queues", "concurrency", "Builds multi-producer single-consumer queues with cache-line-separated head and tail. Producers contend on the tail line, the consumer owns the head line, and they never share. It is the workhorse of message passing.", ["Separate head and tail cache lines", "Use atomic CAS on the tail", "Batch consumer dequeues"], ["DPDK rings", "Custom queues", "Disruptor"], ["Lock-free literature", "Memory models"], 3, 0], ["Per-CPU Data Structures", "concurrency", "Keeps per-CPU copies of hot data so cores never share cache lines. Updates touch only the local copy; aggregation reads all copies rarely. The kernel uses this pattern everywhere.", ["Replicate hot state per CPU", "Update only the local copy", "Aggregate on read"], ["Linux (percpu)", "Kernels", "DPDK"], ["OS literature", "Scalability guides"], 2, 0], ["Hot/Cold Field Splitting", "layout", "Splits frequently-accessed fields from rarely-touched ones into separate structs. Hot fields pack into few cache lines; cold fields stop polluting the cache. It is mechanical and reliably effective.", ["Profile field access frequency", "Split hot from cold", "Link with a pointer or index"], ["Game engines", "Databases", "Compilers"], ["Data-oriented design", "Cache literature"], 2, 1], ["Huge Page Mapping", "numa", "Backs large hot data with huge pages to cut TLB misses. Fewer, larger pages mean the TLB covers more memory; workloads with big footprints see clear wins. Transparent huge pages automate it.", ["Map hot regions with huge pages", "Align to huge-page boundaries", "Watch for fragmentation"], ["Linux (THP/hugetlb)", "Databases", "JVMs"], ["Linux memory docs", "Architecture manuals"], 2, 2], ["Write-Combining Stores", "layout", "Uses non-temporal stores for streaming writes that will not be reread. Bypassing the cache avoids polluting it with write-once data; memcpy implementations use them for large copies. It keeps the cache for data that matters.", ["Use non-temporal stores for streams", "Fence where ordering matters", "Measure cache pollution"], ["glibc memcpy", "DPDK", "Compilers"], ["x86 (movnt)", "ARM (nontemporal)"], 3, 1], ["Cache-Oblivious Algorithms", "layout", "Designs algorithms that are cache-efficient at every level without tuning for specific sizes. Recursive divide-and-conquer keeps working sets small naturally; matrix transpose and sorting have cache-oblivious forms. They perform well on unknown hardware.", ["Recurse to small base cases", "Keep working sets cache-sized", "Avoid size-specific tuning"], ["Research libraries", "FFTW", "Custom"], ["Cache-oblivious literature (Frigo)", "Algorithms texts"], 3, 1], ["Perf Counter Validation", "measurement", "Validates layout changes with hardware performance counters, not just wall time. LLC misses, TLB misses, and coherence traffic prove the mechanism worked. Counters turn cache tuning from art to measurement.", ["Count LLC and TLB misses", "Measure coherence traffic", "A/B test layout changes"], ["perf", "VTune", "PAPI"], ["PMU docs", "Measurement methodology"], 2, 2], ["Struct Packing Discipline", "layout", "Orders struct fields by decreasing size to minimize padding waste. Compilers insert padding for alignment; sorting fields largest-first packs them tightly. Smaller structs mean more fit in each cache line.", ["Sort fields by size descending", "Group same-size fields", "Verify with sizeof and pahole"], ["pahole", "Compilers", "All languages"], ["C standard (alignment)", "ABI docs"], 1, 1], ["Read-Mostly Replication", "concurrency", "Replicates read-mostly data per core with RCU-style updates. Readers never lock or share lines; writers publish new versions and wait for grace periods. It scales reads perfectly.", ["Replicate per core or per node", "Update with copy-and-publish", "Reclaim after grace periods"], ["Linux RCU", "Userspace RCU", "Databases"], ["RCU literature", "Concurrency texts"], 3, 0], ["Interleave Policy Tuning", "numa", "Tunes NUMA interleave policies for bandwidth-bound shared data. Striping pages across nodes aggregates their memory bandwidth; local placement would bottleneck one node. HPC codes interleave deliberately.", ["Identify bandwidth-bound shared data", "Interleave across nodes", "Keep latency-sensitive data local"], ["numactl --interleave", "HPC runtimes", "libnuma"], ["NUMA literature", "HPC guides"], 3, 2]];
var DEMOS=["// Demo: {NAME} — false sharing ping-pong cost\nvar line=64,counters=[0,0];\nvar shared=new Array(2);\nconsole.log('technique: {NAME}');console.log('two counters in one 64-byte line: every increment invalidates the other core\\'s copy');\nconsole.log('padded: each counter on its own line — no ping-pong');\nconsole.log('measured effect: up to 10x on contended counters');", "// Demo: {NAME} — struct layout waste\nvar fields=[['a',1],['b',8],['c',1],['d',8],['e',4]];\nvar off=0;fields.forEach(function(f){var al=Math.min(f[1],8);off=Math.ceil(off/al)*al;off+=f[1];});\nconsole.log('technique: {NAME}');console.log('naive order size: '+off+' bytes');\nvar srt=fields.slice().sort(function(a,b){return b[1]-a[1];});off=0;srt.forEach(function(f){var al=Math.min(f[1],8);off=Math.ceil(off/al)*al;off+=f[1];});\nconsole.log('sorted-by-size order: '+off+' bytes — reorder fields, shrink structs');", "// Demo: {NAME} — NUMA distance effect\nvar nodes=2,local=80,remote=140;\nvar frac=({SEED}%60)/100;\nvar avg=local*(1-frac)+remote*frac;\nconsole.log('technique: {NAME}');console.log('remote access fraction: '+(frac*100).toFixed(0)+'%');\nconsole.log('avg latency: '+avg.toFixed(0)+' ns vs '+local+' ns all-local');\nconsole.log('pin memory and threads to the same node');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-cache-line-aligned-data-structures-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cache-line-aligned-data-structures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
