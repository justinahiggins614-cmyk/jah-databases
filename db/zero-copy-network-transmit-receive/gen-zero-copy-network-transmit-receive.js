(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["kernel", "userspace", "rdma", "buffers"];
var PREFIX='JAH-ZCN-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["sendfile() Transfers", "kernel", "Transfers files to sockets with sendfile, avoiding userspace copies entirely. Data moves from page cache to the NIC via DMA; the application never touches the bytes. Static file servers live on it.", ["Open the file once", "Call sendfile to the socket", "Let DMA move the bytes"], ["Linux", "NGINX", "File servers"], ["Linux man pages", "POSIX"], 1, 1], ["splice() Pipelines", "kernel", "Moves data between file descriptors with splice through kernel pipes, zero-copy. Proxies shuffle bytes from socket to socket without userspace involvement. It is the generic zero-copy plumbing.", ["Splice socket to pipe", "Splice pipe to socket", "Stay in the kernel"], ["Linux", "Proxies", "HAProxy"], ["Linux man pages", "Kernel docs"], 2, 1], ["MSG_ZEROCOPY Sockets", "kernel", "Transmits with MSG_ZEROCOPY so the kernel DMaes from userspace buffers. Completion notifications tell the app when buffers are safe to reuse. It brings zero-copy transmit to normal sockets.", ["Pin userspace buffers", "Send with MSG_ZEROCOPY", "Reclaim on completion"], ["Linux 4.14+", "Custom apps", "Benchmarks"], ["Kernel docs", "LWN articles"], 3, 0], ["DMA-BUF Sharing", "userspace", "Shares DMA buffers between devices with DMA-BUF file descriptors. A camera buffer goes straight to the GPU or NIC without copies; exporters and importers coordinate via fences. It is the Linux zero-copy currency.", ["Export buffers as DMA-BUF", "Import into the consumer", "Synchronize with fences"], ["Linux", "GPUs", "V4L2"], ["DMA-BUF docs", "Kernel"], 3, 2], ["Page Flipping", "kernel", "Flips pages between the network stack and application instead of copying. The receiver's pages become the application's pages; only metadata moves. It is the oldest zero-copy trick, still effective.", ["Receive into swappable pages", "Flip pages to the app", "Recycle the pool"], ["Research stacks", "BSD", "Custom"], ["Networking literature", "OS texts"], 3, 0], ["PACKET_MMAP Rings", "userspace", "Maps kernel packet rings into userspace for zero-copy capture and transmit. The app reads packets straight from the shared ring; no recvmsg copies. Tcpdump-class tools use it.", ["Map the TX/RX rings", "Poll the ring status", "Recycle frames"], ["Linux", "tcpdump", "Sniffers"], ["Linux docs", "Packet socket"], 2, 2], ["RDMA Verbs", "rdma", "Transfers memory to memory with RDMA verbs, bypassing the remote CPU entirely. One-sided reads and writes move data at line rate with microsecond latency. HPC and NVMe-oF depend on it.", ["Register memory regions", "Post work requests", "Poll completions"], ["InfiniBand", "RoCE", "iWARP"], ["IBTA specs", "RDMA literature"], 3, 2], ["io_uring Networking", "kernel", "Drives sockets with io_uring submission and completion rings, batching syscalls to near zero. Registered buffers enable true zero-copy; one syscall submits hundreds of operations. It is the modern Linux fast path.", ["Register buffers", "Batch submissions", "Reap completions"], ["Linux 5.1+", "Custom servers", "Databases"], ["io_uring docs", "LWN"], 3, 1], ["Buffer Pool Recycling", "buffers", "Recycles fixed-size buffers through pools so the fast path never allocates. Allocation is the hidden copy-cost; pools make it disappear. Sizing the pool is the tuning knob.", ["Preallocate buffer pools", "Recycle on completion", "Size for peak load"], ["DPDK", "Netty", "Custom"], ["Memory management", "Perf literature"], 2, 2], ["Header/Data Split", "buffers", "Splits headers from payloads so headers go to the CPU and payloads DMA to their destination. The NIC separates them on receive; software processes tiny headers while bulk data never moves. SmartNICs do this in hardware.", ["Configure header split", "Process headers on CPU", "DMA payloads direct"], ["SmartNICs", "DPDK", "Drivers"], ["NIC docs", "Offload literature"], 3, 2], ["Checksum Offload", "kernel", "Offloads checksum computation to the NIC so the CPU never touches payload bytes. Touching bytes to checksum them is a hidden copy; offload removes it. Every modern NIC does it.", ["Enable TX/RX checksum offload", "Verify with bad packets", "Trust but verify"], ["All NICs", "Linux", "Drivers"], ["NIC specs", "TCP/IP"], 1, 2], ["Hugepage Packet Buffers", "buffers", "Backs packet buffers with huge pages to cut TLB misses on the fast path. At millions of packets per second, TLB misses are measurable; huge pages remove them. DPDK made it standard.", ["Allocate buffers on huge pages", "Pin for DMA", "Measure TLB misses"], ["DPDK", "Custom", "Linux"], ["Huge page docs", "DPDK guides"], 2, 2], ["NUMA-Pinned Buffers", "buffers", "Pins packet buffers and threads to the same NUMA node as the NIC. Cross-node DMA and access add latency; locality keeps the fast path fast. L3 forwarding benchmarks demand it.", ["Pin threads to the NIC's node", "Allocate buffers locally", "Verify with counters"], ["DPDK", "Tuned", "Benchmarks"], ["NUMA docs", "DPDK guides"], 2, 2], ["Buffer Refcounting", "buffers", "Shares buffers between pipeline stages with reference counts instead of copying. Cloning a packet bumps a count; the last user frees it. It is zero-copy composition for packet pipelines.", ["Refcount shared buffers", "Clone by bumping counts", "Free on last release"], ["DPDK (mbuf)", "Sk_buff", "Custom"], ["Memory management", "Networking literature"], 3, 2], ["Zero-Copy Fallbacks", "kernel", "Falls back to copies gracefully when zero-copy conditions are not met. Small messages, unaligned buffers, and old kernels all need the copy path; the fast path checks and diverts. Correctness first, speed second.", ["Check zero-copy preconditions", "Divert to the copy path", "Keep both paths tested"], ["Libraries", "Kernel", "Apps"], ["Robustness literature", "API docs"], 2, 1]];
var DEMOS=["// Demo: {NAME} — copy cost at 10 Gbps\nvar gbps=10,bytesPerSec=gbps*1e9/8;\nvar copyCost=bytesPerSec*20/3e9;\nconsole.log('technique: {NAME}');console.log('throughput: '+gbps+' Gbps = '+(bytesPerSec/1e6).toFixed(0)+' MB/s');\nconsole.log('one copy costs: '+copyCost.toFixed(1)+' CPU cores');\nconsole.log('zero-copy saves those cores for application work');", "// Demo: {NAME} — sendfile vs read+write syscalls\nvar chunks={N1};\nconsole.log('technique: {NAME}');console.log('read+write: '+(chunks*2)+' syscalls + '+chunks+' copies');\nconsole.log('sendfile: 1 syscall, 0 copies (page cache -> socket)');\nconsole.log('syscalls cut by '+Math.round(100*(1-1/(chunks*2)))+'%');", "// Demo: {NAME} — buffer pool recycling\nvar pool=64,used=0,peak=0;\nfor(var i=0;i<{N1}*10;i++){if(((i*13+{SEED})%2)===0&&used<pool){used++;}else if(used>0){used--;}\npeak=Math.max(peak,used);}\nconsole.log('technique: {NAME}');console.log('pool: '+pool+', peak in use: '+peak);\nconsole.log(peak<pool?'no allocation in the fast path — buffers recycled':'pool exhausted — grow it');"];
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
var gen={version:'jahdb-zero-copy-network-transmit-receive-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('zero-copy-network-transmit-receive',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
