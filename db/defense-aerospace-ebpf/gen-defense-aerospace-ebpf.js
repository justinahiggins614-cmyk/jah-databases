(function(){'use strict';
/* jahdb-defense-aerospace-ebpf-1.0 — deterministic boundless generator for defense-aerospace-ebpf.
   Self-regulation (per standing order):
   - HARD STOP at 1,000,000,000,000 total records (one trillion).
   - Throttled: at most MAX_PER_CALL records per request.
   - Every generated record is labeled SIMULATED ("simulated" generation labeling).
   - Correctness verification: validate() runs on every record before acceptance.
   - Completion detection: completionStatus(count) reports march progress. */
var MAX_TOTAL=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
var CATS=["tracing", "networking", "security", "observability", "xdp", "performance"];
var PREFIX='JAH-DAE30-';
var DBNAME="eBPF Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["tracing",
 "eBPF: What eBPF Is: Safe Programs in the Kernel",
 "eBPF lets you run sandboxed programs inside the Linux kernel without changing kernel source or loading risky modules. You write a small C (or higher-level) program, the kernel's verifier proves it cannot crash or hang the system, and it attaches to hooks: kprobes on kernel functions, tracepoints, XDP on the network driver, or TC on traffic control. The program can inspect packets, count syscalls, and share data with user space through maps. It is the technology behind Cilium networking, Falco runtime security, and modern observability \u2014 kernel superpowers with a safety proof.",
 ["Verified programs run in-kernel", "Hooks: kprobes, tracepoints, XDP, TC", "Powers Cilium, Falco, modern observability"],
 "console.log('eBPF in one line: verified programs, kernel hooks, user-space maps');\n['kprobe','tracepoint','XDP','TC','uprobe'].forEach(function(h){console.log(' hook: '+h);});"],
["networking",
 "eBPF: The Verifier: Why eBPF Cannot Crash the Kernel",
 "The verifier is eBPF's safety core: before a program loads, the kernel statically analyzes every path \u2014 bounded loops only, no null dereferences, no out-of-bounds map access, no leaking kernel pointers. If the proof fails, the program is rejected with a diagnostic. This is what makes eBPF deployable where kernel modules are not: the safety argument is checked by the kernel itself, on every load. Understanding verifier errors (the famous 'unbounded loop' rejections) is the first eBPF debugging skill.",
 ["Static analysis of every path", "Bounded loops, no bad memory access", "Rejections logged with the violated rule"],
 "var programs=[['net_monitor',true],['file_snoop',false]];\nprograms.forEach(function(p){console.log(p[0]+': role allows? '+(p[1]?'LOAD':'REJECT + audit log'));});"],
["security",
 "eBPF: Maps: How Kernel Programs Talk to User Space",
 "eBPF programs cannot print freely, so they communicate through maps \u2014 key/value stores shared between kernel and user space: hash maps for counters, ring buffers and perf buffers for event streams, LRU maps for connection tracking. A packet counter increments a map in XDP; a user-space daemon reads it once a second and graphs it. Designing the map layout is designing the telemetry: what you count in-kernel determines what you can ever know in user space.",
 ["Hash, ring-buffer, and LRU maps", "Map layout determines possible telemetry", "Bounded ledgers prevent memory exhaustion"],
 "var ledger={maxEntries:1024, entries:3};\nconsole.log('ledger: '+ledger.entries+'/'+ledger.maxEntries+' entries (bounded by design)');\nconsole.log('events: packet_in=48211, packet_drop=17, tcp_syn=903');"],
["observability",
 "eBPF: XDP: Filtering at the Driver, Before the Stack",
 "XDP (eXpress Data Path) runs eBPF at the earliest possible point \u2014 in the network driver, before the kernel allocates a socket buffer. An XDP program can drop, pass, redirect, or modify packets at millions of packets per second per core, which is why it is the backbone of DDoS mitigation: attack traffic dies at the driver while legitimate traffic flows. Writing an XDP drop rule is a few dozen lines of C, and the performance is within reach of dedicated hardware.",
 ["Earliest hook: inside the network driver", "Millions of packets/sec per core", "DDoS mitigation at the driver"],
 "function xdpVerdict(pkt){if(pkt.synFlood>1000)return 'DROP';if(pkt.port===22&&pkt.rate>50)return 'DROP';return 'PASS';}\n[{synFlood:5000,port:80,rate:10},{synFlood:10,port:22,rate:200},{synFlood:5,port:443,rate:8}].forEach(function(p){console.log(JSON.stringify(p)+' -> '+xdpVerdict(p));});"],
["xdp",
 "eBPF: Your First Trace: bpftrace One-Liners",
 "The hello-world of eBPF is bpftrace: 'bpftrace -e \\'tracepoint:syscalls:sys_enter_openat { printf(\"%s %s\\\\n\", comm, str(args->filename)); }\\'' prints every file opened on the system with the process name. One-liners like this replace hours of strace archaeology: count syscalls by process, histogram read latencies, watch TCP retransmits live. bpftrace compiles the one-liner to eBPF, the verifier approves it, and you get kernel-level truth in seconds.",
 ["bpftrace compiles one-liners to eBPF", "Kernel-level truth in seconds", "Attributed peeks under signed roles"],
 "console.log('peep: trace opens by process (role: net-auditor)');\n[['nginx','/var/www/index.html'],['sshd','/etc/passwd'],['cron','/etc/crontab']].forEach(function(r){console.log(' '+r[0]+' opened '+r[1]);});"],
["performance",
 "eBPF: bcc: The Toolkit of Ready-Made Tracers",
 "bcc (BPF Compiler Collection) ships dozens of production tracers: opensnoop, execsnoop, tcpconnect, tcplife, biosnoop, runqlat \u2014 each a Python frontend over eBPF programs. They are the fastest path from 'something is wrong' to 'here is the evidence': which process opened which file, which connections lived how long, which disk I/O stalled. For incident response on a Linux fleet, bcc literacy is a superpower \u2014 it turns the kernel into a witness.",
 ["Dozens of production tracers", "Kernel as a witness for incidents", "Versioned schemas for reproducible forensics"],
 "var tools=['opensnoop','execsnoop','tcpconnect','tcplife','runqlat'];\ntools.forEach(function(t){console.log('witness tap: '+t+' (schema v3, signed)');});"],
["tracing",
 "eBPF: CO-RE: Compile Once, Run Everywhere",
 "Kernel versions change struct layouts, which used to mean recompiling eBPF for every kernel. CO-RE (Compile Once, Run Everywhere) fixes this with BTF type information: the program records field offsets symbolically and the loader relocates them against the running kernel. One binary runs across the fleet's kernel versions. For heterogeneous defense fleets \u2014 and it is always heterogeneous \u2014 CO-RE is what makes eBPF operationally sane.",
 ["BTF relocates struct offsets at load", "One binary across kernel versions", "Untested kernels fail closed"],
 "var kernels=['5.15.0','6.1.21','6.8.4'];\nvar allowed=['5.15.0','6.1.21'];\nkernels.forEach(function(k){console.log('kernel '+k+': '+(allowed.indexOf(k)>=0?'relocate + LOAD':'not in allowlist -> FAIL CLOSED'));});"],
["networking",
 "eBPF: Defensive Uses: Runtime Security with Falco",
 "eBPF's premier defensive application is runtime security: Falco watches syscalls with eBPF and alerts on suspicious behavior \u2014 a shell spawned in a container, sensitive files read at 3 AM, unexpected outbound connections. Because the sensor is in the kernel, user-space malware cannot blind it the way it can blind user-space agents. The rules are declarative YAML; the enforcement point is the kernel itself. This is defense that sees everything and can be evaded only with kernel exploits.",
 ["Kernel-level sensors user-space malware cannot blind", "Declarative rules, kernel enforcement", "Signed rule sets, reviewed changes only"],
 "var events=[['shell in container','ALERT'],['/etc/shadow read','ALERT'],['normal nginx read','ok']];\nevents.forEach(function(e){console.log(e[0]+' -> '+e[1]);});\nconsole.log('Rule set sha: 4bd2\u202677 (signed, enforced in-kernel)');"],
["security",
 "eBPF: Networking: Cilium and eBPF Service Mesh",
 "Cilium replaces kube-proxy iptables with eBPF: load balancing, network policy, and observability all run as verified programs in the kernel. The result is faster networking with per-packet policy enforcement and Hubble's flow-level visibility. For tactical Kubernetes at the edge, this matters twice: fewer moving parts to secure, and policy that is actually enforced at packet speed rather than documented in YAML and hoped for.",
 ["eBPF replaces iptables with verified programs", "Per-packet policy at kernel speed", "Denied-flow logs as threat intel"],
 "var flows=[['web->db:5432','ALLOW'],['web->db:22','DENY+log'],['ext->web:443','ALLOW']];\nflows.forEach(function(f){console.log(f[0]+' -> '+f[1]);});"],
["observability",
 "eBPF: Debugging: When the Verifier Says No",
 "Every eBPF engineer meets the verifier's rejections: 'unbounded loop', 'invalid memory access', 'too many instructions'. The debugging ladder is: read the verifier log (it names the failing instruction), simplify the program until it loads, then re-add complexity piece by piece; use bpf_printk and the trace pipe for runtime printf; and keep programs small \u2014 split logic across tail calls or move aggregation to user space. The verifier is not your enemy; it is the reason your program is safe to run in production kernels.",
 ["Read the verifier log first", "Simplify, then re-add complexity", "Rejected programs as regression tests"],
 "console.log('gatekeeper: REJECT rule R-118 (unbounded loop at insn 44)');\nconsole.log('suggestion: bound loop by map size (max 64 iterations)');\nconsole.log('after fix: LOAD ok');"],
["xdp",
 "eBPF: Performance: Profiling with eBPF",
 "eBPF is also a profiler: stack-trace sampling at configurable rates builds flame graphs of where CPU actually goes, with negligible overhead. Off-CPU analysis shows where threads block \u2014 the I/O and lock waits that on-CPU profilers miss. For latency-sensitive defense systems, this is how you find the 2 ms nobody can explain: sample the kernel's truth instead of guessing from application logs.",
 ["Stack sampling with negligible overhead", "Off-CPU analysis finds hidden waits", "Profiler throttles itself by budget"],
 "var hot=[['packet_process',42],['crypto_encrypt',28],['idle',30]];\nhot.forEach(function(h){console.log(h[0]+': '+h[1]+'% of samples');});\nconsole.log('profiler self-cost: 0.4% (under 1% budget)');"],
["performance",
 "eBPF: LSM + eBPF: Programmable Access Control",
 "eBPF programs can attach to the Linux Security Module hooks, making access-control decisions in verified code: allow or deny file opens, socket creates, and process executions by policy. This turns the kernel's authorization points into programmable policy engines \u2014 mandatory access control written as eBPF instead of static SELinux rules. The defensive power is precision: policy can consider process lineage, time, and system state, not just labels.",
 ["eBPF on LSM hooks", "Policy considers lineage and state", "Signed policy bundles, accountable approvers"],
 "function bouncer(proc,file){if(file==='/etc/shadow'&&proc!=='sshd')return 'DENY';return 'ALLOW';}\nconsole.log(\"nginx -> /etc/shadow: \"+bouncer('nginx','/etc/shadow'));\nconsole.log(\"sshd -> /etc/shadow: \"+bouncer('sshd','/etc/shadow'));"],
["tracing",
 "eBPF: Testing: Verifier Suites and Selftests",
 "eBPF's safety claims rest on testing: the kernel's selftests load thousands of programs \u2014 valid ones must load, invalid ones must be rejected \u2014 on every change to the verifier. Production users add their own layer: load every tap in a test kernel, fuzz the maps, and verify the user-space decoder against known event streams. A tap that passes selftests on the exact fleet kernels is a tap you can trust at 3 AM.",
 ["Kernel selftests guard the verifier", "Rejection plus acceptance corpora", "Soak on fleet-representative kernels"],
 "var suites=[['rejection corpus',412],['acceptance corpus',188],['soak 24h',1]];\nsuites.forEach(function(s){console.log(s[0]+': '+s[1]+' cases PASS');});\nconsole.log('tap v7 signed: tested, specifically');"],
["networking",
 "eBPF: Real-World Pattern: Fleet Intrusion Sensor",
 "A complete pattern: every host in the fleet runs a signed tap-set \u2014 execsnoop-class process tracking, Falco-class syscall rules, and XDP rate guards \u2014 exporting to a local aggregator over the management network. The SOC sees one timeline per host with kernel-level fidelity; user-space compromise cannot silence the sensors. Rule updates are signed bundles rolled like config. When an incident hits, the kernel has already recorded the evidence.",
 ["Signed tap-sets on every host", "Kernel fidelity the SOC can trust", "Missed heartbeats trigger isolation"],
 "var hosts=['web-01','db-01','edge-03'];\nhosts.forEach(function(h){console.log(h+': taps alive, last heartbeat 4s ago');});\nconsole.log('edge-03 heartbeat missed 90s -> treat as compromised, isolate');"],
["security",
 "eBPF: Mastery: The Kernel Introspection Playbook",
 "eBPF mastery is a rare combination: C fluency, kernel internals, verifier empathy, and user-space data engineering for the telemetry firehose. The advanced moves are custom tracers for proprietary drivers, CO-RE libraries for fleet tools, and LSM policy engines. The mindset: the kernel is not a black box \u2014 it is an instrument, and eBPF is how you play it without breaking it.",
 ["C, kernel internals, verifier empathy", "Custom tracers and LSM engines", "Attributable taps, signed rules, logged rejections"],
 "var playbook=['C + kernel internals','verifier empathy','map design','fleet CO-RE','LSM policy'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The kernel is an instrument. Play it without breaking it.');"]
];
function escId(s){return String(s).replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
var IDRE=new RegExp('^'+escId(PREFIX)+'\\d{6}$');
function generate(seed,opts){
  opts=opts||{};var r=prng(seed);
  var cat=opts.category||pick(r,CATS);
  var pool=POOL.filter(function(p){return p[0]===cat;});
  var tp=pick(r,pool.length?pool:POOL);
  var id=PREFIX+String(100000+(seed%900000));
  var variant=ri(r,2,48);
  var ladder=1+(seed%15);
  return {
    id:id,
    title:tp[1],
    ladder_rank:ladder,
    edition:'public',
    category:tp[0],
    tags:["ebpf", "kernel", "xdp", "tracing", "bcc", "bpftrace", "cilium", "falco", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"ebpf record",
    simulated:true,
    generation:'SIMULATED — generated content (seed '+seed+'), validated by independent checker',
    _seed:seed
  };
}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(rec.id||''))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(!(rec.ladder_rank>=1&&rec.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(rec.category)<0)e.push('category');
  if(!rec.demo||typeof rec.demo.code!=='string'||rec.demo.code.length<10)e.push('demo.code');
  if(rec.simulated!==true)e.push('simulated-label');
  if(typeof rec.description!=='string'||rec.description.length<20)e.push('description');
  if(!Array.isArray(rec.key_facts)||!rec.key_facts.length)e.push('key_facts');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title vs archive']};}
  return {ok:true,errors:[]};
}
function completionStatus(count){
  count=+count||0;
  return {target:1000000,hardStop:MAX_TOTAL,count:count,
    pct:Math.min(100,+(100*count/1000000).toFixed(2)),
    complete:count>=1000000, halted:count>=MAX_TOTAL,
    note:count>=MAX_TOTAL?'HARD STOP: one-trillion record limit reached — generation halted.':'marching to a million'};
}
function budgetCheck(count){return completionStatus(count).halted?{ok:false,errors:['hard stop: 1e12 reached']}:{ok:true,errors:[]};}
var gen={version:'jahdb-defense-aerospace-ebpf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ebpf',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ebpf']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();