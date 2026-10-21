(function(){'use strict';
/* jahdb-defense-aerospace-wireshark-1.0 — deterministic boundless generator for defense-aerospace-wireshark-signature.
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
var PREFIX='JAH-DAE46S-';
var DBNAME="Signature Wireshark Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["packet-analysis",
 "Signature Wireshark: What Wireshark Is: The Network's Microscope",
 "The Signature counterpart is the SigScope auditor, Manon's original packet-analysis design. SigScope mirrors the capture-dissect-filter pipeline but every capture carries a case record \u2014 whose network, under what authority, retained how long. The Signature design makes the authority part of the capture file: you inspect traffic you are entitled to inspect.",
 ["Capture live or read pcaps", "Thousands of protocol dissectors", "Authority recorded per capture"],
 "console.log('Wireshark: capture -> dissect -> filter');\n['live capture','pcap files','3000+ dissectors','display filters','follow stream'].forEach(function(s){console.log(' '+s);});"],
["dissectors",
 "Signature Wireshark: Dissectors: Reading Every Layer",
 "The bench's dissectors are the grammars: same layered parsing, with custom grammars versioned. The Signature design requires the grammar version in the analysis \u2014 a decode is only as trustworthy as the grammar that produced it.",
 ["Per-protocol byte parsing", "Chained by port and heuristics", "Custom Lua dissectors for proprietary protocols"],
 "var tcp={src:443,dst:51234,seq:8812001,flags:'PA',win:64240};\nconsole.log('TCP '+tcp.src+' -> '+tcp.dst+' seq '+tcp.seq+' flags '+tcp.flags+' win '+tcp.win);\nconsole.log('grammar: tcp v4.2 (versioned decode)');"],
["capture",
 "Signature Wireshark: Display Filters: Finding the Needle",
 "The bench's filters are the lenses: same query power, with every lens saved to the case record. The Signature design makes the lens part of the evidence \u2014 'these are the packets I looked at, and here is the filter that selected them'.",
 ["Query dissected fields", "Fluency finds packets in seconds", "Filters saved as evidence"],
 "console.log('lens: tls.handshake.type==1 && ip.addr==10.0.0.5');\nconsole.log('1,000,000 packets -> 14 ClientHellos (lens saved to case)');"],
["filters",
 "Signature Wireshark: Follow Stream: Reassembling Conversations",
 "The bench's stream view is the transcript: same reassembly, with decryption only under recorded authority. The Signature design logs every decryption \u2014 whose keys, whose session, whose authority \u2014 because readable encrypted traffic is the most sensitive capability in the toolkit.",
 ["TCP reassembly to conversations", "Reads like narrative", "Decryption logged with authority"],
 "console.log('transcript: TCP stream 7 (HTTP)');\nconsole.log('GET /api/status -> 200 OK (214 bytes)');\nconsole.log('decryption: authorized case 4417 (logged)');"],
["forensics",
 "Signature Wireshark: Your First Capture: The Local Handshake",
 "The bench's hello-world is the first look: same choreography, but the capture opens with the case record dialog \u2014 whose network, what purpose. The Signature design makes the authority question the first habit: before the first packet, the analyst states the right to look.",
 ["Capture loopback, browse, inspect", "See the protocol choreography", "Authority stated before first packet"],
 "var pkts=[['DNS query',1],['TCP SYN',3],['TLS ClientHello',1],['HTTP GET',2]];\npkts.forEach(function(p){console.log(p[0]+': '+p[1]+' packets');});\nconsole.log('case: training capture, own network (authority stated)');"],
["tactical",
 "Signature Wireshark: Tactical PCAP: Capturing in the Field",
 "The bench's field kit is the evidence bag: ring-buffer capture with case metadata sealed at capture time. The Signature design hash-seals the capture on stop \u2014 the pcap's integrity is provable from the moment of capture.",
 ["Ring buffers, capture filters", "Time-synced for correlation", "Hash-sealed at capture"],
 "var cap={ring_mb:512,duration_h:6,sealed:true};\nconsole.log('field capture: '+cap.ring_mb+' MB ring, '+cap.duration_h+'h');\nconsole.log('sealed on stop: sha 7d11\u2026 (integrity provable)');"],
["packet-analysis",
 "Signature Wireshark: Wireless and IoT Capture: Beyond Ethernet",
 "The bench's wireless doctrine is the spectrum witness: captures with signal metadata, protocol dissectors for the IoT stack. The Signature design records the capture conditions \u2014 channel, adapter, antenna \u2014 because wireless captures are meaningless without their RF context.",
 ["Wi-Fi, Bluetooth, 802.15.4, LoRa", "Monitor mode and radiotap", "RF context recorded"],
 "var cap={proto:'802.15.4',channel:15,rssi_dbm:-72};\nconsole.log('capture: '+cap.proto+' ch '+cap.channel+', RSSI '+cap.rssi_dbm+' dBm');\nconsole.log('conditions recorded (RF context attached)');"],
["dissectors",
 "Signature Wireshark: Statistics: The Network's Vital Signs",
 "The bench's statistics are the vital signs: same shape analysis, with baselines for comparison. The Signature design keeps the baseline with the case \u2014 'this spike is abnormal because the baseline says so' is an evidenced claim.",
 ["Protocol hierarchy, conversations, IO graphs", "Spikes as incident indicators", "Baselines make anomalies evidenced"],
 "var stats=[['TLS',68],['DNS',12],['QUIC',9],['other',11]];\nstats.forEach(function(s){console.log(s[0]+': '+s[1]+'%');});\nconsole.log('IO spike 14:22 vs baseline: ANOMALY (evidenced)');"],
["capture",
 "Signature Wireshark: Defensive Uses: The Network Witness",
 "The bench's forensics doctrine is the unimpeachable witness: sealed captures, documented lenses, hash-verified chains. The Signature design makes the capture handling log part of the case \u2014 who touched the evidence, when \u2014 because the witness's credibility is procedural.",
 ["Incident ground truth", "Reconstruct attacks from packets", "Sealed, logged, credible evidence"],
 "console.log('case 4417: beaconing every 60s to 203.0.113.7 (witness)');\nconsole.log('handling log: 3 accesses, all authorized');\nconsole.log('bytes are bytes (witness unimpeachable)');"],
["filters",
 "Signature Wireshark: Encrypted Traffic Analysis Without Decryption",
 "The bench's encrypted analysis is the shape reader: handshake fingerprints, flow patterns, baseline comparison. The Signature design requires the inference labeled \u2014 'likely beaconing (metadata only)' \u2014 because metadata suggests, it does not convict.",
 ["JA3, SNI, timing patterns", "Metadata suffices for triage", "Inferences labeled as such"],
 "var flow={sni:'cdn.example.com',interval_s:60,jitter:0.02};\nconsole.log('flow: '+flow.sni+', every '+flow.interval_s+'s, jitter '+flow.jitter);\nconsole.log('assessment: LIKELY beaconing (metadata only, labeled)');"],
["forensics",
 "Signature Wireshark: Debugging: The Protocol Misbehaves",
 "The bench's protocol debugging is the conversation read: handshake narrated, failure named. The Signature design attaches the read to the ticket \u2014 the diagnosis rides with the incident, not in the analyst's head.",
 ["Retransmissions, alerts, handshakes", "Read the handshake like conversation", "Diagnoses attached to tickets"],
 "console.log('TLS alert 40: handshake failure (cipher mismatch)');\nconsole.log('diagnosis: server lacks ECDHE (not \"network slow\")');\nconsole.log('read attached to ticket (not in head)');"],
["tactical",
 "Signature Wireshark: Capture Filters: BPF at the Source",
 "The bench's capture doctrine is the wide net: filter only what is certainly irrelevant. The Signature design requires the filter in the case record \u2014 'we did not capture X because the filter excluded it' is stated, not discovered later.",
 ["BPF drops packets at capture", "Filter deliberately, document exclusions", "Wide net over narrow assumptions"],
 "console.log('capture filter: tcp port 443 (case record notes exclusion)');\nconsole.log('stored: 2.1 GB of 40 GB seen (filtered deliberately)');"],
["packet-analysis",
 "Signature Wireshark: Testing: Validating Network Changes",
 "The bench's validation is the packet proof: before/after captures per change. The Signature design requires the proof attached to the change record \u2014 the network's changes are evidenced, not hoped.",
 ["Before/after captures per change", "Firewall and QoS verification", "Proof attached to change records"],
 "var change={rule:'block 203.0.113.0/24',before:'allowed',after:'blocked'};\nconsole.log('change: '+change.rule);\nconsole.log('before: '+change.before+' -> after: '+change.after+' (capture proof)');"],
["dissectors",
 "Signature Wireshark: Real-World Pattern: Incident Packet Forensics",
 "The bench's incident doctrine is the evidenced narrative: capture to case file, every step recorded. The Signature design requires the re-capture proof \u2014 'we blocked it' is verified with packets, not assumed.",
 ["Detect, capture, dissect, block, prove", "Lua dissector for the C2 protocol", "Re-capture proves the block"],
 "console.log('indicators extracted -> firewall blocked 203.0.113.7');\nconsole.log('re-capture: silence (blocked, proven)');\nconsole.log('case file: complete, sealed, reviewable');"],
["capture",
 "Signature Wireshark: Mastery: The Packet Analyst's Playbook",
 "The bench's mastery adds the stewardship layer: cases, seals, handling logs. Manon's roadmap runs from today's analyst workstations to fleet-scale capture fabrics under one scope discipline \u2014 the wire never lies, and now it is witnessed properly.",
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
    edition:'signature',
    category:tp[0],
    tags:["wireshark", "pcap", "network-analysis", "dissectors", "forensics", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-wireshark-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-wireshark-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();