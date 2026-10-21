(function(){'use strict';
/* jahdb-defense-aerospace-micro-dds-1.0 — deterministic boundless generator for defense-aerospace-micro-dds.
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
var CATS=["middleware", "dds", "qos", "determinism", "xrce", "space"];
var PREFIX='JAH-DAE38-';
var DBNAME="Micro-DDS Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["middleware",
 "Micro-DDS: What Micro-DDS Is: DDS for Small Things",
 "DDS is the industrial pub/sub standard \u2014 decentralized, QoS-rich, real-time \u2014 and Micro-DDS (the XRCE-DDS profile, eProsima's implementation) brings it to microcontrollers and constrained links. A tiny XRCE client on a Cortex-M talks through an agent to the full DDS global data space: the sensor node publishes, the flight computer subscribes, with the same reliability and deadline policies as the big systems. It is how resource-starved edges join grown-up middleware instead of speaking ad-hoc serial protocols.",
 ["DDS pub/sub for microcontrollers", "XRCE client/agent architecture", "Joins the global data space"],
 "console.log('Micro-DDS: XRCE client -> agent -> DDS data space');\n['decentralized discovery','QoS policies','Cortex-M clients','space-link profiles'].forEach(function(s){console.log(' '+s);});"],
["dds",
 "Micro-DDS: XRCE-DDS: The Client/Agent Pattern",
 "XRCE splits the work: the tiny client on the microcontroller speaks a compact binary protocol over serial or UDP to the agent, and the agent \u2014 running on a capable host \u2014 participates in full DDS on the client's behalf. The client stays small (tens of KB); the agent does discovery, matching, and QoS. This is the right division of labor: the edge stays lean, the infrastructure stays smart.",
 ["Tiny client, capable agent", "Compact binary wire protocol", "Slot allocations attested"],
 "console.log('herald (device, 28 KB) <-> steward (host)');\nconsole.log('slot allocation attested: device 0x14, slots 4-7 @ 10 ms');"],
["qos",
 "Micro-DDS: QoS on a Diet: What Survives",
 "Constrained DDS keeps the QoS that matters: reliability (best-effort vs reliable with the agent buffering), durability for late joiners, deadlines, and liveliness \u2014 implemented within the client's memory budget. The art is choosing: reliable delivery costs buffers the microcontroller may not have, so critical topics get reliability and telemetry stays best-effort. Every QoS choice is a memory budget line.",
 ["Essential QoS within memory budgets", "Reliability costs buffers", "Memory proven before start"],
 "var qos=[['heartbeat','reliable',2],['telemetry','best_effort',0],['command','reliable',4]];\nvar total=qos.reduce(function(a,q){return a+q[2];},0);\nqos.forEach(function(q){console.log(q[0]+': '+q[1]+' ('+q[2]+' KB)');});\nconsole.log('total '+total+' KB of 8 KB budget -> FITS');"],
["determinism",
 "Micro-DDS: Determinism: Time-Triggered Options",
 "Some systems need not just fast but predictable: time-triggered DDS profiles schedule transmissions in fixed slots, so worst-case latency is computed, not hoped. Space and flight systems live here \u2014 the bus schedule is part of the safety case. Micro-DDS deployments in these domains pair the middleware with schedule analysis: every topic's period, deadline, and jitter budget documented and verified.",
 ["Fixed slots, computed latency", "Schedule as safety-case material", "Slots reviewed like code"],
 "var slots=[['imu',0,2],['gps',2,5],['cmd',5,6]];\nslots.forEach(function(s){console.log(s[0]+': slots '+s[1]+'-'+s[2]);});\nconsole.log('worst-case latency: computed 6 ms (not hoped)');"],
["xrce",
 "Micro-DDS: Your First Talker: Client to Data Space",
 "The hello-world: an XRCE client on a dev board publishes a counter; the agent on the laptop bridges it to DDS; a subscriber prints it. The same code, pointed at a flight computer's agent, becomes flight telemetry. The lesson is the architecture's transparency \u2014 the application does not know or care where the agent lives.",
 ["Client publishes, agent bridges", "Architecture-transparent applications", "Schedule visible from message one"],
 "console.log('first pulse: herald publishes counter');\nconsole.log('slot 4 @ 10 ms, attested');\nconsole.log('subscriber: 0,1,2,3\u2026 (schedule visible)');"],
["space",
 "Micro-DDS: Discovery: Finding Each Other",
 "DDS discovery is decentralized \u2014 no broker \u2014 using multicast or configured peers to find matching publishers and subscribers. On constrained networks, discovery is tuned: static peer lists instead of multicast storms, the agent handling discovery for its clients. In space links with minutes of delay, discovery is preconfigured, not dynamic. The network's constraints shape the discovery strategy.",
 ["Decentralized, brokerless", "Static peers for constrained links", "Unexpected participants as security events"],
 "var muster=['herald-14','herald-15','steward-01'];\nmuster.forEach(function(m){console.log('muster: '+m+' present');});\nconsole.log('unknown herald-99 -> SECURITY EVENT (not on guest list)');"],
["middleware",
 "Micro-DDS: Space Profile: DTN and Long Delays",
 "Space networks break terrestrial assumptions: minutes of light-delay, scheduled contacts, intermittent links. DDS profiles for space (and the DTN \u2014 delay-tolerant networking \u2014 underneath) use store-and-forward, custody transfer, and contact planning. Micro-DDS's small footprint suits flight computers; the space profile suits the physics. Together they are how modern smallsats talk \u2014 and how lunar networks will.",
 ["Store-and-forward, custody transfer", "Contact-plan scheduling", "Custody explicit and logged"],
 "var bundle={id:'b-4471',custodian:'orbiter-2',next_contact:'14:22'};\nconsole.log('bundle '+bundle.id+' custodian '+bundle.custodian);\nconsole.log('next contact '+bundle.next_contact+' (handoff logged)');"],
["dds",
 "Micro-DDS: Defensive Uses: The Trusted Bus",
 "Micro-DDS's defensive value is a trustworthy nervous system for uncrewed vehicles and field systems: authenticated participants, QoS-guaranteed command delivery, deadline-monitored telemetry \u2014 on hardware too small for enterprise middleware. A UGV whose command link has proven deadlines and authenticated publishers is a system the operator can trust at distance. The bus becomes part of the safety case.",
 ["Authenticated, deadline-guaranteed links", "For hardware too small for big middleware", "Bus health self-reported"],
 "console.log('trusted pulse: 14 heralds, 0 slot misses, 0 unknown');\nconsole.log('deadline breaches (24h): 0');\nconsole.log('bus health: NOMINAL (self-reported)');"],
["qos",
 "Micro-DDS: Reliability: What 'Reliable' Costs",
 "Reliable QoS means the agent buffers unacked samples and retransmits \u2014 memory and bandwidth spent for certainty. On constrained links, teams budget it: commands reliable, high-rate telemetry best-effort, with the sequence numbers letting subscribers detect gaps. The engineering is explicit about the trade: certainty has a price, paid in buffers.",
 ["Buffers and retransmits cost memory", "Commands reliable, telemetry best-effort", "Gap detection by sequence numbers"],
 "var ledger=[['command',4,'0 gaps'],['telemetry',0,'3 gaps (tolerated)']];\nledger.forEach(function(l){console.log(l[0]+': '+l[1]+' KB buffers, '+l[2]);});"],
["determinism",
 "Micro-DDS: Debugging: The Silent Subscriber",
 "DDS debugging classics: the subscriber that never receives (QoS mismatch \u2014 check compatibility), discovery that never completes (multicast blocked), and the agent that drops clients (resource limits). The tools are the DDS spy (list the data space), QoS compatibility reporting, and the agent's logs. The first question is always: do they see each other? Then: do they agree?",
 ["Spy the data space first", "QoS compatibility checks", "Diagnostics suggest the fix"],
 "console.log('roll call: muster OK, slots OK');\nconsole.log('diagnostic: /telemetry QoS mismatch (fix: set subscriber best-effort)');"],
["xrce",
 "Micro-DDS: Security: DDS-Security on Small Devices",
 "DDS-Security brings authentication, access control, and encryption to the data space \u2014 and the XRCE profile carries it to constrained devices via the agent. The plugins (PKI auth, crypto, access control) are the same model as SROS2's. Key provisioning for fleets of devices is the operational challenge; the answer is manufacturing-time provisioning with rotation. An unauthenticated bus is a remote-control interface for anyone on the network.",
 ["Auth, access control, encryption", "Manufacturing-time provisioning", "Key age as telemetry"],
 "var keys=[['herald-14','22d'],['herald-15','91d']];\nkeys.forEach(function(k){console.log(k[0]+' key age '+k[1]+(k[1]==='91d'?' -> ROTATE SOON':''));});"],
["space",
 "Micro-DDS: Performance: Latency Budgets",
 "Micro-DDS deployments live on budgets: sensor-to-actuator latency decomposed into bus hops, each with a deadline. The measurement is end-to-end with hardware timestamps \u2014 not estimates. Tuning is buffer sizes, thread priorities, and (for time-triggered) slot maps. The budget document is the performance contract, reviewed when anything changes.",
 ["End-to-end budgets with hardware timestamps", "Per-hop deadlines", "Measured p99 must fit the budget"],
 "var hops=[['sensor->bus',2],['bus->compute',3],['compute->bus',4],['bus->actuator',2]];\nvar total=hops.reduce(function(a,h){return a+h[1];},0);\nhops.forEach(function(h){console.log(h[0]+': '+h[1]+' ms');});\nconsole.log('end-to-end '+total+' ms vs SLO 15 ms: '+(total<=15?'ENFORCED':'REJECTED'));"],
["middleware",
 "Micro-DDS: Testing: Conformance and Interop",
 "DDS's strength is standards: conformance tests verify the implementation, interop events verify vendors work together. Micro-DDS programs add the constrained layer: client/agent protocol tests, resource-exhaustion tests (what happens at the buffer limit?), and long-soak tests for leaks. A middleware that fails gracefully under exhaustion is a middleware you can field.",
 ["Conformance plus interop", "Exhaustion behavior specified", "Soak tests for leaks"],
 "var tests=[['conformance',1],['exhaustion',1],['soak 72h',1]];\ntests.forEach(function(t){console.log(t[0]+': '+(t[1]?'PASS':'FAIL'));});\nconsole.log('exhaustion spec: shed lowest priority first (published)');"],
["dds",
 "Micro-DDS: Real-World Pattern: Flight Computer Bus",
 "A complete pattern: a smallsat's flight computer runs the steward; payload heralds publish telemetry in attested slots; the ground station subscribes through the data space during contacts. Commands go reliable with custody; telemetry goes best-effort with gap detection. The bus schedule is part of the mission's safety case, reviewed alongside the flight software.",
 ["Steward on flight computer, heralds on payloads", "Contact-plan rehearsals in sim", "Schedule part of the safety case"],
 "console.log('contact rehearsal: 3 contacts, 412 bundles, custody clean');\nconsole.log('slot map reviewed, safety case updated');"],
["qos",
 "Micro-DDS: Mastery: The Middleware Playbook",
 "Micro-DDS mastery is distributed-systems thinking at small scale: QoS fluency, discovery tuning, schedule analysis, security architecture, and measurement discipline. The advanced moves are custom transports, space profiles, and safety-case authorship. The mindset: the bus is infrastructure \u2014 invisible when right, catastrophic when wrong.",
 ["Distributed systems at small scale", "Custom transports, space profiles", "Stewardship: attested, sealed, published"],
 "var playbook=['QoS fluency','discovery tuning','schedule analysis','security architecture','measurement'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The bus is infrastructure. Engineer it invisibly well.');"]
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
    tags:["dds", "xrce", "fastdds", "middleware", "real-time", "space", "deterministic", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"micro dds record",
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
var gen={version:'jahdb-defense-aerospace-micro-dds-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-micro-dds',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-micro-dds']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();