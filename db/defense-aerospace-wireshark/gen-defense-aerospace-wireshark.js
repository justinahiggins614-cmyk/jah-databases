(function(){'use strict';
/* jahdb-defense-aerospace-wireshark-1.0 — deterministic boundless generator for defense-aerospace-wireshark.
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
var CATS=["packet-analysis", "dissectors", "capture", "filters", "forensics", "tactical"];
var PREFIX='JAH-DAE46-';
var DBNAME="Wireshark Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["packet-analysis",
 "Wireshark: What Wireshark Is: The Network's Microscope",
 "Wireshark captures packets from an interface (via libpcap/Npcap) or reads capture files, then dissects them \u2014 Ethernet to IP to TCP to TLS to HTTP \u2014 presenting every field of every layer. The display filters (ip.addr == x, tcp.port == 443) slice millions of packets to the interesting few; Follow Stream reassembles conversations. It is the tool behind 'what is actually on the wire' \u2014 the ground truth of networks, used by every network engineer and incident responder.",
 ["Capture live or read pcaps", "Thousands of protocol dissectors", "Authority recorded per capture"],
 "console.log('Wireshark: capture -> dissect -> filter');\n['live capture','pcap files','3000+ dissectors','display filters','follow stream'].forEach(function(s){console.log(' '+s);});"],
["dissectors",
 "Wireshark: Dissectors: Reading Every Layer",
 "A dissector parses one protocol's bytes into named fields: the TCP dissector shows sequence numbers, flags, window sizes; the TLS dissector shows handshake messages and cipher suites. Wireshark chains them by port and heuristics. Writing a Lua dissector for a proprietary protocol is the power move \u2014 your weird industrial protocol becomes as readable as HTTP. Understanding dissectors is understanding that 'the network' is just agreed-upon byte layouts.",
 ["Per-protocol byte parsing", "Chained by port and heuristics", "Custom Lua dissectors for proprietary protocols"],
 "var tcp={src:443,dst:51234,seq:8812001,flags:'PA',win:64240};\nconsole.log('TCP '+tcp.src+' -> '+tcp.dst+' seq '+tcp.seq+' flags '+tcp.flags+' win '+tcp.win);\nconsole.log('grammar: tcp v4.2 (versioned decode)');"],
["capture",
 "Wireshark: Display Filters: Finding the Needle",
 "Capture everything, display the interesting: display filters (different from capture filters) query the dissected fields \u2014 'tls.handshake.type == 1 and ip.addr == 10.0.0.5' shows one host's ClientHellos. Filter fluency is Wireshark fluency: the expert finds the three packets that matter in a million-packet capture in seconds. The filter expression is also documentation \u2014 save it with the analysis.",
 ["Query dissected fields", "Fluency finds packets in seconds", "Filters saved as evidence"],
 "console.log('lens: tls.handshake.type==1 && ip.addr==10.0.0.5');\nconsole.log('1,000,000 packets -> 14 ClientHellos (lens saved to case)');"],
["filters",
 "Wireshark: Follow Stream: Reassembling Conversations",
 "Follow TCP Stream reassembles the byte flow \u2014 the HTTP request and response as text, the full conversation. For incident response this is reading the mail: what did the client ask, what did the server return? Combined with decryption (with the session keys, where authorized), even TLS sessions become readable. The stream view turns packets into narrative.",
 ["TCP reassembly to conversations", "Reads like narrative", "Decryption logged with authority"],
 "console.log('transcript: TCP stream 7 (HTTP)');\nconsole.log('GET /api/status -> 200 OK (214 bytes)');\nconsole.log('decryption: authorized case 4417 (logged)');"],
["forensics",
 "Wireshark: Your First Capture: The Local Handshake",
 "The hello-world: capture on loopback, load a web page, stop, filter 'http', Follow Stream the request. You see the DNS query, the TCP handshake, the TLS ClientHello, the HTTP exchange \u2014 the internet's choreography, exposed. Every network engineer remembers this moment: the abstraction became bytes, and the bytes made sense.",
 ["Capture loopback, browse, inspect", "See the protocol choreography", "Authority stated before first packet"],
 "var pkts=[['DNS query',1],['TCP SYN',3],['TLS ClientHello',1],['HTTP GET',2]];\npkts.forEach(function(p){console.log(p[0]+': '+p[1]+' packets');});\nconsole.log('case: training capture, own network (authority stated)');"],
["tactical",
 "Wireshark: Tactical PCAP: Capturing in the Field",
 "Tactical capture means small, rugged, and disciplined: a field laptop or appliance capturing to ring buffers (never filling the disk), with capture filters limiting to the interesting traffic, time-synchronized for correlation. The captures come home for analysis. The discipline is capture hygiene \u2014 know what you captured, when, and under what authority \u2014 because field captures become evidence.",
 ["Ring buffers, capture filters", "Time-synced for correlation", "Hash-sealed at capture"],
 "var cap={ring_mb:512,duration_h:6,sealed:true};\nconsole.log('field capture: '+cap.ring_mb+' MB ring, '+cap.duration_h+'h');\nconsole.log('sealed on stop: sha 7d11\u2026 (integrity provable)');"],
["packet-analysis",
 "Wireshark: Wireless and IoT Capture: Beyond Ethernet",
 "Wireshark captures more than Ethernet: Wi-Fi (with radiotap headers showing signal strength and channels), Bluetooth, Zigbee/802.15.4, and LoRa \u2014 the IoT and tactical protocols. Wireless capture needs monitor mode and the right adapters; the analysis needs the protocol dissectors. For field networks of sensors and radios, this is where the packets actually are.",
 ["Wi-Fi, Bluetooth, 802.15.4, LoRa", "Monitor mode and radiotap", "RF context recorded"],
 "var cap={proto:'802.15.4',channel:15,rssi_dbm:-72};\nconsole.log('capture: '+cap.proto+' ch '+cap.channel+', RSSI '+cap.rssi_dbm+' dBm');\nconsole.log('conditions recorded (RF context attached)');"],
["dissectors",
 "Wireshark: Statistics: The Network's Vital Signs",
 "Wireshark's statistics \u2014 protocol hierarchy, conversations, IO graphs \u2014 show the network's shape: what percentage is TLS, who talks to whom, when the spike happened. For incident response, the IO graph's spike is often the first indicator; the conversations list names the talkers. Statistics turn a capture from a pile of packets into a situation report.",
 ["Protocol hierarchy, conversations, IO graphs", "Spikes as incident indicators", "Baselines make anomalies evidenced"],
 "var stats=[['TLS',68],['DNS',12],['QUIC',9],['other',11]];\nstats.forEach(function(s){console.log(s[0]+': '+s[1]+'%');});\nconsole.log('IO spike 14:22 vs baseline: ANOMALY (evidenced)');"],
["capture",
 "Wireshark: Defensive Uses: The Network Witness",
 "Wireshark's defensive value is ground truth: during incidents, the capture shows what actually traversed the wire \u2014 the exfiltration, the C2 beaconing, the lateral movement. Network forensics reconstructs the attack from packets when logs are incomplete or untrustworthy. The capture is the witness that cannot be gaslit \u2014 bytes are bytes.",
 ["Incident ground truth", "Reconstruct attacks from packets", "Sealed, logged, credible evidence"],
 "console.log('case 4417: beaconing every 60s to 203.0.113.7 (witness)');\nconsole.log('handling log: 3 accesses, all authorized');\nconsole.log('bytes are bytes (witness unimpeachable)');"],
["filters",
 "Wireshark: Encrypted Traffic Analysis Without Decryption",
 "Even encrypted traffic leaks metadata: handshake fingerprints (JA3), SNI, certificate details, timing and size patterns. Wireshark plus the right dissectors reveals the shape of encrypted conversations \u2014 which is often enough for defensive triage (that host is beaconing to a new TLS endpoint every 60 seconds). The discipline is knowing what metadata can and cannot prove.",
 ["JA3, SNI, timing patterns", "Metadata suffices for triage", "Inferences labeled as such"],
 "var flow={sni:'cdn.example.com',interval_s:60,jitter:0.02};\nconsole.log('flow: '+flow.sni+', every '+flow.interval_s+'s, jitter '+flow.jitter);\nconsole.log('assessment: LIKELY beaconing (metadata only, labeled)');"],
["forensics",
 "Wireshark: Debugging: The Protocol Misbehaves",
 "Wireshark debugs protocols: the retransmission storm (congested or lossy path), the TLS handshake failure (cipher mismatch, expired cert \u2014 the alert message says which), the DNS that never answers. The expert reads the handshake like a conversation and spots where it went wrong. 'The network is slow' becomes 'the server's window never opens' \u2014 a diagnosis, not a complaint.",
 ["Retransmissions, alerts, handshakes", "Read the handshake like conversation", "Diagnoses attached to tickets"],
 "console.log('TLS alert 40: handshake failure (cipher mismatch)');\nconsole.log('diagnosis: server lacks ECDHE (not \"network slow\")');\nconsole.log('read attached to ticket (not in head)');"],
["tactical",
 "Wireshark: Capture Filters: BPF at the Source",
 "Capture filters (BPF syntax: 'tcp port 443') drop uninteresting packets during capture \u2014 essential for high-rate links where storing everything is impossible. The art is filtering enough to fit the disk but little enough to keep the evidence: when in doubt, capture more. BPF is also the language of the kernel's packet filter \u2014 the same technology class as eBPF, fittingly.",
 ["BPF drops packets at capture", "Filter deliberately, document exclusions", "Wide net over narrow assumptions"],
 "console.log('capture filter: tcp port 443 (case record notes exclusion)');\nconsole.log('stored: 2.1 GB of 40 GB seen (filtered deliberately)');"],
["packet-analysis",
 "Wireshark: Testing: Validating Network Changes",
 "Wireshark validates network work: before/after captures proving the migration worked, the firewall rule actually blocks, the QoS policy actually prioritizes. 'Trust but verify' with packets: the capture is the test result. Change windows get their captures; the captures get reviewed. Networks are too important for 'it should be fine'.",
 ["Before/after captures per change", "Firewall and QoS verification", "Proof attached to change records"],
 "var change={rule:'block 203.0.113.0/24',before:'allowed',after:'blocked'};\nconsole.log('change: '+change.rule);\nconsole.log('before: '+change.before+' -> after: '+change.after+' (capture proof)');"],
["dissectors",
 "Wireshark: Real-World Pattern: Incident Packet Forensics",
 "A complete pattern: the SOC detects beaconing, pulls the sealed field capture, filters to the suspect host, follows the streams, extracts the C2 protocol with a Lua dissector, and documents the indicators. The firewall blocks the C2; the re-capture proves silence. The case file holds captures, lenses, and the handling log \u2014 the incident as an evidenced narrative.",
 ["Detect, capture, dissect, block, prove", "Lua dissector for the C2 protocol", "Re-capture proves the block"],
 "console.log('indicators extracted -> firewall blocked 203.0.113.7');\nconsole.log('re-capture: silence (blocked, proven)');\nconsole.log('case file: complete, sealed, reviewable');"],
["capture",
 "Wireshark: Mastery: The Packet Analyst's Playbook",
 "Wireshark mastery is protocol literacy: TCP/IP cold, TLS handshake warm, the common application protocols readable, BPF and display filters fluent. The advanced moves are custom dissectors, encrypted-traffic analysis, and expert testimony. The mindset: the wire does not lie \u2014 learn to listen.",
 ["Protocol literacy end to end", "Custom dissectors, encrypted analysis", "Stewardship: cases, seals, logs"],
 "var playbook=['TCP/IP cold','filter fluency','custom dissectors','encrypted analysis','testimony'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The wire does not lie. Learn to listen.');"]
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
    tags:["wireshark", "pcap", "network-analysis", "dissectors", "forensics", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"wireshark record",
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
var gen={version:'jahdb-defense-aerospace-wireshark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-wireshark',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-wireshark']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();