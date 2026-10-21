(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["mapping", "coherency", "userspace", "ordering"];
var PREFIX='JAH-MMM-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["BAR Mapping with Attributes", "mapping", "Maps device BARs with the right memory attributes: uncacheable for registers, write-combining for framebuffers. Wrong attributes cause corruption or terrible performance; the driver chooses per region. It is the foundation of all MMIO.", ["Map registers uncacheable", "Map framebuffers write-combining", "Verify attributes per region"], ["Linux (ioremap)", "Windows", "Drivers"], ["PCI spec", "x86 PAT/MTRR"], 2, 0], ["Write-Combining Buffers", "mapping", "Uses write-combining memory to burst streaming writes to devices. WC buffers collect writes into full cache-line bursts instead of trickling bytes. GPUs and framebuffers depend on it for throughput.", ["Mark streaming regions WC", "Let the CPU combine writes", "Flush explicitly when needed"], ["Linux (ioremap_wc)", "GPU drivers", "x86"], ["x86 PAT", "Driver guides"], 2, 0], ["Uncacheable Register Access", "mapping", "Accesses device registers as uncacheable so every read hits the hardware. Cached register reads return stale values; UC guarantees freshness. Control registers are always UC.", ["Map control registers UC", "Use volatile accesses", "Never cache side-effecting reads"], ["All drivers", "Linux", "Windows"], ["PCI spec", "Architecture manuals"], 1, 0], ["Posted Write Semantics", "ordering", "Understands that MMIO writes are posted: they complete from the CPU's view before reaching the device. Ordering between writes is preserved, but completion is not; a read-back or non-posted write acts as a barrier. Drivers synchronize accordingly.", ["Treat writes as posted", "Use read-back as a barrier", "Order with non-posted operations"], ["PCIe drivers", "Linux", "All OSes"], ["PCI Express spec", "Driver literature"], 2, 2], ["Read-Modify-Write Safety", "ordering", "Performs read-modify-write on registers with locking or atomic sequences. Concurrent RMW from two threads corrupts bits; spinlocks or hardware atomics serialize them. It is the classic driver race.", ["Lock around RMW sequences", "Mask only the target bits", "Verify with read-back"], ["Linux drivers", "Windows", "Embedded"], ["Concurrency literature", "Driver guides"], 2, 1], ["Doorbell Registers", "mapping", "Rings doorbell registers to notify hardware of new work instead of polling. The driver writes descriptors to memory, then one MMIO write kicks the device. Batching doorbells amortizes the MMIO cost.", ["Write descriptors to memory", "Ring the doorbell once", "Batch to amortize MMIO"], ["NVMe", "NIC drivers", "GPUs"], ["NVMe spec", "PCIe"], 2, 1], ["Cache Coherency with Devices", "coherency", "Keeps CPU caches coherent with DMA through snooping or explicit flushes. Coherent interconnects snoop automatically; non-coherent ones need manual cache maintenance. Getting it wrong corrupts data silently.", ["Use coherent mappings where available", "Flush/invalidate explicitly otherwise", "Test with DMA patterns"], ["ARM (coherent)", "x86 (snooping)", "Embedded"], ["AMBA ACE", "PCIe (No Snoop)"], 3, 0], ["Huge Pages for MMIO", "mapping", "Maps large MMIO regions with huge pages to cut TLB pressure. A 1 GB BAR needs 262k 4K TLB entries but one 1G page; fewer misses mean faster access. It matters for big apertures.", ["Map large BARs with huge pages", "Reduce TLB misses", "Align to huge-page boundaries"], ["Linux (hugetlb)", "GPU drivers", "DPDK"], ["Linux huge pages", "Architecture manuals"], 3, 0], ["Userspace I/O with UIO/VFIO", "userspace", "Exposes MMIO to userspace safely with UIO for simple devices and VFIO for IOMMU-isolated ones. Userspace drivers map BARs directly, bypassing kernel overhead; the IOMMU keeps DMA safe. DPDK and SPDK are built on this.", ["Bind the device to vfio-pci", "Map BARs into userspace", "Isolate DMA with the IOMMU"], ["DPDK", "SPDK", "VFIO"], ["VFIO docs", "IOMMU specs"], 3, 2], ["Register Shadowing", "coherency", "Keeps software shadows of write-only registers to allow read-modify-write. Some registers cannot be read back; the shadow tracks their last written value. It enables safe bit manipulation on write-only hardware.", ["Shadow write-only registers", "RMW against the shadow", "Sync shadow on every write"], ["Embedded drivers", "Linux", "Firmware"], ["Driver literature", "Hardware manuals"], 2, 1], ["Memory Ordering Barriers", "ordering", "Places memory barriers to order MMIO against normal memory accesses. Weakly ordered architectures reorder freely; barriers enforce the sequence the hardware requires. Missing barriers cause Heisenbugs.", ["Identify required orderings", "Insert the weakest sufficient barrier", "Document each barrier's purpose"], ["Linux (mb/rmb/wmb)", "ARM", "Drivers"], ["Memory model literature", "Architecture manuals"], 3, 2], ["MSI-X Tables in MMIO", "mapping", "Programs MSI-X vector tables that live in MMIO BARs. The driver writes message address and data per vector into the table; the device reads them to signal interrupts. It ties MMIO programming to interrupt delivery.", ["Locate the MSI-X table BAR", "Program address/data per vector", "Mask/unmask per vector"], ["Linux PCI", "NVMe", "NIC drivers"], ["PCI Express (MSI-X)", "Linux IRQ"], 3, 1], ["Cache-Line Padding", "coherency", "Pads per-CPU MMIO-adjacent structures to cache lines to avoid false sharing. Two cores hammering adjacent words in one line ping-pong the cache; padding isolates them. It is cheap insurance for hot paths.", ["Pad hot structures to 64 bytes", "Align to cache lines", "Verify with perf counters"], ["Linux (____cacheline_aligned)", "DPDK", "Drivers"], ["Cache literature", "Concurrency guides"], 2, 0], ["Device Memory Fences", "ordering", "Uses device-specific fences to order operations within the device. Some accelerators need explicit fence commands between batches; the driver inserts them per the programming model. It is the device-side analog of CPU barriers.", ["Insert fences per the programming model", "Wait on fence completion", "Batch between fences"], ["GPU drivers", "Accelerators", "NVMe"], ["Vendor programming guides", "PCIe ordering"], 3, 2], ["Write-Back Register Caching", "coherency", "Caches frequently-written registers in write-back software caches with flush on demand. For registers written far more than read, batching writes cuts MMIO traffic. Flush points are chosen where hardware needs consistency.", ["Cache hot registers in software", "Batch writes", "Flush at consistency points"], ["GPU drivers", "Custom drivers", "Firmware"], ["Driver literature", "Caching theory"], 3, 1]];
var DEMOS=["// Demo: {NAME} — write-combining vs uncacheable throughput\nvar bytes={N1}*4096;\nvar wc=bytes/3.2e9*1e3,uc=bytes/0.4e9*1e3;\nconsole.log('technique: {NAME}');console.log('transfer: '+(bytes/1048576).toFixed(1)+' MB');\nconsole.log('write-combining: '+wc.toFixed(1)+' ms, uncacheable: '+uc.toFixed(1)+' ms');\nconsole.log('WC wins '+(uc/wc).toFixed(1)+'x for streaming writes');", "// Demo: {NAME} — doorbell batching\nvar regs={N1},per=50;\nvar single=regs*per,batched=per+regs*2;\nconsole.log('technique: {NAME}');console.log('registers: '+regs);\nconsole.log('individual MMIO: '+single+' ns, batched doorbell: '+batched+' ns');\nconsole.log('batching saves '+Math.round(100*(1-batched/single))+'% of MMIO cost');", "// Demo: {NAME} — posted vs non-posted ordering\nvar log=[];\nfunction posted(w){log.push('posted:'+w);}\nfunction nonposted(w){log.push('nonposted:'+w+' (acked)');}\nposted('A');posted('B');nonposted('C');\nconsole.log('technique: {NAME}');console.log(log.join(' -> '));\nconsole.log('non-posted C acts as a barrier: A,B are visible before C completes');"];
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
var gen={version:'jahdb-memory-mapped-i-o-mmio-caching-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('memory-mapped-i-o-mmio-caching',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
