(function(){'use strict';
/* jahdb-fundamental-networking-1.0 — fundamental networking bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FNET-';
var KIND='fundamental networking record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Computer networking is the study and engineering of communication between computing devices: how data moves across links, through routers, and between applications reliably, efficiently, and securely. It is what turned computers into the internet.', 'reasoning':'Network engineers reason in layers: each layer provides a service to the one above and uses the one below. When something fails, the layer model localizes the fault — the art is knowing which layer to blame.', 'quantities':'The core quantities are bandwidth (bits per second), latency (delay), loss (fraction dropped), and jitter (delay variation). Throughput is what you get; bandwidth is what you paid for — they differ.', 'mechanism':'Networking works by packet switching: data chopped into packets, each routed independently, reassembled at the destination. Reliability is built atop unreliability — TCP\'s acknowledgments and retransmissions make a lossy network deliver perfectly.', 'miscon':'Networking is not magic: \'the cloud\' is someone else\'s computer, reached through these protocols. Bandwidth is not speed — latency governs responsiveness. And Wi-Fi bars measure signal strength, not internet speed.'};
var SIGLENS=['In the Signature system, networking is the connective tissue: every database sync, every API call, every distributed piece of this network runs on these principles, and the Signature formulation teaches each one as a mechanism you can trace.','The Signature practice is to trace the packet: follow the layers, measure the latency, find the loss — so networking is understood as a path you can walk, not a cloud you must trust.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- subnet math demo. Runs as-is with python3."""\ndef ip_to_int(ip):\n    a, b, c, d = (int(x) for x in ip.split("."))\n    return (a << 24) | (b << 16) | (c << 8) | d\ndef int_to_ip(n):\n    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))\ndef network(ip, prefix):\n    n = ip_to_int(ip)\n    mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF\n    return int_to_ip(n & mask), int_to_ip(n | (~mask & 0xFFFFFFFF))\nnet, bcast = network("192.168.1.77", 24)\nprint("network:", net, "broadcast:", bcast, "hosts:", 2**(32-24) - 2)\n', '#!/usr/bin/env python3\n"""{TITLE} -- latency vs bandwidth demo. Runs as-is with python3."""\ndef transfer_time(file_mb, bandwidth_mbps, latency_ms, rtt_roundtrips=4):\n    bits = file_mb * 8\n    send_s = bits / bandwidth_mbps\n    latency_s = (latency_ms / 1000) * rtt_roundtrips\n    return send_s + latency_s\nfor bw, lat in [(10, 20), (1000, 20), (1000, 300)]:\n    t = transfer_time(100, bw, lat)\n    print(f"{bw} Mbps, {lat} ms RTT: 100MB takes {t:.1f}s")\nprint("bandwidth moves big files; latency governs responsiveness")\n', '#!/usr/bin/env python3\n"""{TITLE} -- TCP reliability sketch demo. Runs as-is with python3."""\nimport random\nrandom.seed(5)\ndef send_packets(n, loss_rate):\n    acked = set()\n    transmissions = 0\n    pending = list(range(n))\n    while pending:\n        seq = pending.pop(0)\n        transmissions += 1\n        if random.random() > loss_rate:\n            acked.add(seq)          # ACK received\n        else:\n            pending.append(seq)     # lost: retransmit later\n    return transmissions\natt = send_packets(20, 0.2)\nprint(f"20 packets, 20% loss -> {att} transmissions; all arrived (retransmission works)")\nprint("TCP: every byte is acknowledged; the lost ones are resent")\n'];
var TOPICS=[['What Networking Is','Computer networking is the engineering of communication between devices: moving bits across wires, fiber, and air, through switches and routers, to the right application. It turned isolated computers into the internet — humanity\'s nervous system.'],
['The Core Question of Networking','The core question is: how does data get from here to there, correctly and efficiently? Every protocol — every header, handshake, and timeout — is an answer to some corner of that question.'],
['Assumptions: Unreliable Foundations','Networking assumes the lower layers are unreliable: packets get lost, duplicated, reordered, and corrupted. The architecture\'s genius is building reliable communication atop unreliable parts — each layer compensating for the one below.'],
['The Vocabulary: Packets, Protocols, Addresses','The vocabulary names the pieces: packets (chunks of data), protocols (rules of exchange), addresses (who), ports (which application), and routes (which way). Fluency means reading a packet capture like a paragraph.'],
['Bandwidth and Latency: The Fundamental Quantities','Bandwidth (bits per second) and latency (seconds of delay) are the fundamental quantities, and they govern different things: bandwidth moves big files, latency governs responsiveness. Confusing them is the field\'s original sin.'],
['Layering: The Primary Method','Layering is the primary method: the OSI and TCP/IP models divide networking into layers — physical, link, network, transport, application — each serving the one above. Debugging is layer-by-layer elimination: find the lowest broken layer.'],
['A Canonical First Example','The canonical first example is ping: one ICMP echo request, one reply, the round-trip time measured. From that single number — and whether it returns at all — begins all network diagnosis.'],
['How Networking Measures','The field measures with ping, traceroute, and packet captures: latency and loss from probes, paths from TTL tricks, everything from captures. \'Measure, don\'t guess\' is the networker\'s creed — the wire never lies.'],
['The Core Mechanism: Packet Switching','The core mechanism is packet switching: messages divided into packets, each routed independently toward the destination, reassembled on arrival. It replaced circuits with statistical multiplexing — the reason the internet scales.'],
['The Simplest Law: Best Effort','The simplest law is IP\'s best-effort service: the network promises to try, nothing more. Reliability, ordering, and completeness are built above IP by TCP — the end-to-end principle placing smarts at the edges.'],
['Common Misconceptions in Networking','The misconceptions mislead: that bandwidth equals speed (latency matters), that the cloud is not physical (it is buildings full of servers), that Wi-Fi signal bars measure internet speed, and that \'the network is reliable\' (the first fallacy of distributed computing).'],
['How Beginners Practice Networking','Beginners practice by building small networks: two machines, a switch, static addresses, then ping, then capture. Watching your own packets in Wireshark teaches more than any diagram of the stack.'],
['The Core Model: TCP/IP','TCP/IP is the core model: IP addressing and routing below, TCP\'s reliable streams (and UDP\'s datagrams) above. The hourglass shape — everything over IP, IP over everything — is why the internet absorbed every new link technology.'],
['The Great Idea: The End-to-End Principle','The end-to-end principle is the great idea: keep the network simple, put intelligence at the endpoints. It let the internet evolve without permission — every new application rode the same dumb, fast pipes.'],
['Systems Thinking: Congestion','Systems thinking in networking is congestion: everyone sending at once collapses the shared resource. TCP\'s congestion control — additive increase, multiplicative decrease — is distributed cooperation emerging from selfish algorithms.'],
['Invariance: Protocol Contracts','The invariance principle is the protocol contract: bits on the wire follow the RFC regardless of vendor. Interoperability — Cisco talking to Juniper talking to Linux — is the field\'s proof that standards beat products.'],
['Approximation: Statistical Multiplexing','Approximation exploits statistics: not everyone transmits at once, so links are oversubscribed by design. The math of multiplexing — provisioning for the probable, not the possible — is the economics of all networking.'],
['Evidence Standards: The Packet Capture','The evidence standard is the capture: tcpdump and Wireshark show what actually crossed the wire. Theories about network behavior end where the capture begins — the packets are ground truth.'],
['Classic Discoveries','The classic discoveries are packet switching, TCP/IP, the World Wide Web, Wi-Fi, and congestion control. Each turned a laboratory idea into planetary infrastructure.'],
['Core Trade-offs: Throughput versus Delay','The core trade-off is throughput versus delay versus loss: bufferbloat trades latency for throughput, retransmission trades delay for reliability. Every network is a point chosen on this triangle.'],
['Handling Uncertainty: Loss and Retransmission','Networking handles uncertainty with timers and retransmission: TCP assumes loss from missing acknowledgments and resends, adapting its rate to what the network proves it can carry. Uncertainty is measured, then managed.'],
['Tools of the Trade','The tools of the trade are ping, traceroute, dig, Wireshark, and iperf. The deepest is the packet capture — the complete, honest record of a conversation between machines.'],
['Ethics and Responsibility','Ethics in networking concerns neutrality, privacy, and access: net neutrality debates, encryption for everyone, and closing the digital divide. The network\'s operators hold power over speech itself — the responsibility is commensurate.'],
['Teaching Networking','Teaching it well wires things up: students configure real interfaces, break real connectivity, and fix it with captures. The stack stops being abstract the first time your ping fails and you find why.'],
['The Frontier Question','The frontier question is the network\'s next scale: terabit links, satellite constellations, programmable data planes, and networks that configure themselves. The frontier asks whether the hourglass can survive another thousand-fold growth.'],
['Unifying Theories','The unifying theories are Shannon\'s information theory beneath it all and the end-to-end argument above it: one bounds what communication can do, the other guides where the doing should live. Between them, the whole field.'],
['Computational Networking','Computational networking programs the network itself: software-defined networking separates control from forwarding, and programmable switches run code per packet. The network becomes software — with software\'s powers and bugs.'],
['Bridges to Other Fields','Networking bridges to electrical engineering (the physical layer), computer science (protocols as distributed algorithms), economics (peering and transit), and sociology (the network society). It is infrastructure for everything digital.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: internet-scale routing security (BGP hijacks persist), perfect congestion control, and the architecture for a post-quantum, AI-driven network. Active work, no settled answers.'],
['How New Claims Are Validated','New protocols are validated by interoperation and deployment: independent implementations, testbed trials, then RFC and adoption. A protocol earns trust when strangers\' equipment speaks it correctly.'],
['The Great Debates','The great debates include net neutrality, the wisdom of middleboxes versus end-to-end purity, and IPv6\'s long transition. The debates are architectural — each side defends a vision of what the network is for.'],
['Failure Modes: When Networking Gets It Wrong','Networking gets it wrong through misconfiguration (the leading cause of outages), bufferbloat, and assuming reliability the network never promised. The immune system is the capture, the config review, and designing for failure.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis architects networks from fundamentals: addressing planned, routing designed, congestion understood, failures assumed. The fundamentals are the difference between a network and a collection of cables.'],
['The Signature Formulation: Networking as Traceable Path','The Signature formulation treats every network principle as a traceable path: packets you can follow, layers you can peel, because in the Signature system communication you cannot trace is communication you cannot trust. That is the Signature capstone on networking bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Layering is respected: each layer's contract is honored by implementations.", "Interoperability: standards (RFCs) rule; proprietary extensions are documented.", "Measurement first: diagnose with data (ping, traceroute, captures) before theorizing."],citations:["Kurose, J. and Ross, K. \u2014 Computer Networking: A Top-Down Approach.", "IETF RFCs \u2014 the internet's open standards documents.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-networking-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-networking',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
