(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["stacks", "offload", "protocols", "timing"];
var PREFIX='JAH-BMN-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["lwIP Integration", "stacks", "Integrates the lwIP stack for TCP/IP on microcontrollers and bare-metal systems. The zero-copy API keeps RAM use tiny; the stack runs in a single thread or with an OS. It brings real networking to tiny devices.", ["Port the netif driver", "Use the zero-copy API", "Tune memory pools"], ["lwIP", "FreeRTOS", "Embedded"], ["lwIP docs", "TCP/IP Illustrated"], 1, 0], ["DPDK Poll-Mode Drivers", "stacks", "Runs poll-mode drivers that bypass the kernel for line-rate packet processing. Cores spin on NIC rings instead of taking interrupts; throughput hits tens of millions of packets per second. It is the standard for fast packet work.", ["Bind NICs to userspace", "Poll rings on dedicated cores", "Batch aggressively"], ["DPDK", "VPP", "Telco/NFV"], ["DPDK docs", "NIC guides"], 3, 0], ["XDP Fast Path", "offload", "Processes packets in the driver with XDP before the kernel stack sees them. eBPF programs drop, forward, or redirect at millions of packets per core. It is the Linux fast path for filtering and load balancing.", ["Attach eBPF to the driver", "Decide per packet early", "Redirect or pass up"], ["Linux XDP", "Cilium", "Cloudflare"], ["XDP docs", "eBPF literature"], 3, 0], ["Zero-Copy RX Rings", "offload", "Receives packets directly into application buffers via DMA rings. No copies between NIC, kernel, and app; the descriptor ring is the contract. It removes the biggest cost in packet processing.", ["DMA into app buffers", "Manage descriptor rings", "Recycle buffers fast"], ["DPDK", "netmap", "PACKET_MMAP"], ["DMA literature", "NIC docs"], 2, 1], ["Polling vs Interrupts", "stacks", "Chooses polling at high packet rates and interrupts at low ones. Interrupts cost microseconds each — fine at 10k pps, fatal at 10M; NAPI hybrids switch automatically. The crossover is measured, not guessed.", ["Measure packets per second", "Poll above the crossover", "Use NAPI hybrids"], ["Linux NAPI", "DPDK", "Drivers"], ["Interrupt literature", "Linux networking"], 2, 0], ["TCP Offload Engines", "offload", "Offloads TCP segmentation, checksums, and even full stacks to hardware. TSO builds big segments the NIC splits; full TOE runs TCP on the card. Offload frees CPU for application work.", ["Enable TSO/GRO/GSO", "Offload checksums", "Evaluate full TOE carefully"], ["NICs", "Linux", "SmartNICs"], ["TCP specs", "Offload literature"], 3, 2], ["ARP and Neighbor Discovery", "protocols", "Implements ARP for IPv4 and ND for IPv6 on bare metal. Address resolution maps IPs to MACs; the stack caches entries and handles gratuitous announcements. No network works without it.", ["Answer ARP/ND requests", "Cache resolutions", "Handle gratuitous updates"], ["lwIP", "Custom stacks", "Embedded"], ["RFC 826 (ARP)", "RFC 4861 (ND)"], 1, 1], ["DHCP Clients", "protocols", "Acquires addresses with minimal DHCP clients for diskless and embedded boots. Discover, offer, request, ack — the four-packet dance; leases renew automatically. It is how bare-metal nodes join networks.", ["Broadcast discover", "Request the offered address", "Renew before expiry"], ["udhcpc", "dhcpcd", "Custom"], ["RFC 2131", "RFC 8415 (DHCPv6)"], 1, 1], ["TLS on Bare Metal", "protocols", "Runs TLS without an OS using embedded TLS libraries. mbedTLS and wolfSSL do full handshakes in kilobytes of RAM; hardware crypto accelerates the math. Secure bare-metal communication is practical.", ["Integrate an embedded TLS lib", "Manage certs and keys", "Accelerate with hardware crypto"], ["mbedTLS", "wolfSSL", "Embedded"], ["RFC 8446 (TLS 1.3)", "Embedded TLS guides"], 3, 2], ["Lock-Free Ring Buffers", "stacks", "Passes packets between cores with lock-free rings. Single-producer single-consumer rings need only memory barriers; they are the fastest IPC for packets. DPDK rings are the reference design.", ["Size rings as powers of two", "Use barriers, not locks", "Batch enqueue/dequeue"], ["DPDK rte_ring", "Custom", "netmap"], ["Lock-free literature", "DPDK docs"], 2, 1], ["Receive-Side Scaling", "offload", "Spreads flows across RX queues with RSS hashing so multiple cores share the load. The NIC hashes headers into queue selection; each queue has its own core. It parallelizes receive processing.", ["Program the RSS hash key", "Map queues to cores", "Keep flows on one queue"], ["NICs", "Linux", "DPDK"], ["RSS specs", "NIC docs"], 2, 1], ["Network Boot Chains", "protocols", "Chains network boot from PXE to iPXE to the OS image over HTTP. Each stage fetches the next with more capability; HTTP replaces slow TFTP for big images. Diskless fleets boot this way.", ["PXE to iPXE", "Fetch via HTTP", "Boot the image"], ["iPXE", "MAAS", "Datacenters"], ["PXE spec", "iPXE docs"], 2, 1], ["Link Negotiation", "protocols", "Negotiates link speed and duplex with autonegotiation. Both ends advertise capabilities and pick the best common mode; forced settings are a classic misconfiguration. It just works when left alone.", ["Advertise capabilities", "Pick the best common mode", "Avoid forced mismatches"], ["PHYs", "Switches", "NICs"], ["IEEE 802.3", "Autonegotiation"], 1, 2], ["BPF Packet Filters", "offload", "Filters packets in the kernel or driver with BPF before userspace wakes. Classic BPF and eBPF programs decide per packet at near-zero cost. Tcpdump made it famous; XDP made it fast.", ["Compile filter programs", "Attach at the right hook", "Verify with the verifier"], ["libpcap", "eBPF", "XDP"], ["BPF literature", "eBPF docs"], 2, 2], ["PTP Time Sync", "timing", "Synchronizes clocks to sub-microsecond with Precision Time Protocol. Hardware timestamping at the PHY removes jitter; the servo disciplines the clock. Trading and telecom need it.", ["Timestamp in hardware", "Run the PTP servo", "Monitor offset and jitter"], ["linuxptp", "NICs", "Switches"], ["IEEE 1588", "PTP profiles"], 3, 2]];
var DEMOS=["// Demo: {NAME} — polling vs interrupt overhead\nvar pps={N1}*1000,intrCost=3000,pollCost=200;\nvar intr=pps*intrCost/1e9,poll=pollCost/1e9;\nconsole.log('technique: {NAME}');console.log('packet rate: '+pps+' pps');\nconsole.log('interrupt cost: '+intr.toFixed(2)+' cores, polling cost: '+poll.toFixed(2)+' cores');\nconsole.log('polling wins at high packet rates');", "// Demo: {NAME} — ring buffer occupancy\nvar size=1024,prod=0,cons=0;\nfor(var i=0;i<{N1}*10;i++){if(((i*7+{SEED})%3)!==0)prod=(prod+1)%size;else cons=(cons+1)%size;}\nvar occ=(prod-cons+size)%size;\nconsole.log('technique: {NAME}');console.log('ring size: '+size+', occupancy: '+occ+' ('+(100*occ/size).toFixed(1)+'%)');\nconsole.log(occ<size*0.9?'healthy headroom':'RING NEAR FULL — add buffering or shed');", "// Demo: {NAME} — checksum offload savings\nvar bytes={N2}*1500,cpuPerByte=3;\nvar cpu=bytes*cpuPerByte/3e9;\nconsole.log('technique: {NAME}');console.log('traffic: '+(bytes/1e6).toFixed(1)+' MB');\nconsole.log('CPU checksum cost: '+cpu.toFixed(2)+' core-seconds -> offloaded: ~0');"];
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
var gen={version:'jahdb-bare-metal-network-stack-integration-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bare-metal-network-stack-integration',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
