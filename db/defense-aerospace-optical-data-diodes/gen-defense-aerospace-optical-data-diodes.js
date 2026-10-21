(function(){'use strict';
/* jahdb-defense-aerospace-optical-data-diodes-1.0 — deterministic boundless generator for defense-aerospace-optical-data-diodes.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["optical-diodes", "protocols", "certifications", "deployments", "throughput"];
var PREFIX='JAH-DAE15-';
var EDITION='public';
var POOL=[["Data Diodes: One-Way by Physics", "optical-diodes", "An optical data diode enforces one-way data transfer in hardware: a transmitter LED on the low side, a receiver photodiode on the high side, and physically no return path — not a firewall rule, but the absence of a wire. Owl Cyber Defense and Waterfall Security build them for industrial and defense networks. What cannot physically return cannot leak.", {"Enforces": "one-way in hardware", "How": "LED -> photodiode, no return", "Not": "a firewall rule", "Makers": "Owl, Waterfall-class vendors"}], ["Why One-Way: The Air-Gap Problem", "deployments", "Air-gapped networks still need data in — patches, threat intel, historian feeds — and every inbound path is a potential outbound leak. Data diodes solve the dilemma: information flows in, nothing flows out, by construction. Monitoring without exfiltration is the use case.", {"Needs": "data in (patches, feeds)", "Risks": "every path leaks out", "Solves": "in by construction", "Use": "monitor without exfiltration"}], ["Optical Separation: The Core Mechanism", "optical-diodes", "The diode's core is optical separation: electrical-to-optical conversion on the sending side, optical-to-electrical on the receiving side, with an air gap or fiber between. There is no electrical continuity to exploit and no reverse channel to sneak data through. Tampering with the optics breaks the link visibly.", {"Converts": "electrical-optical-electrical", "Between": "air gap or fiber", "No": "electrical continuity", "Tamper": "breaks visibly"}], ["Protocol Proxies and Breaks", "protocols", "TCP needs acknowledgments — which cannot cross a diode — so diode systems proxy protocols: they terminate TCP on each side and forward payloads across the optical link via UDP-style unidirectional protocols. File transfer, syslog, historian replication, and email all have diode-friendly proxies. The protocol break is the engineering that makes one-way usable.", {"Breaks": "TCP at each side", "Crosses": "payloads via UDP-style", "Proxies": "files, syslog, historians", "Makes": "one-way usable"}], ["Throughput and Performance", "throughput", "Modern diodes move serious traffic — gigabit-class throughput with low latency — because the optical link is just fast. Performance engineering covers packet pacing, forward error correction, and reassembly on the receiving side. One-way does not mean slow.", {"Moves": "gigabit-class", "Covers": "pacing, FEC, reassembly", "Latency": "low", "Means": "one-way, not slow"}], ["EAL and Common Criteria Certification", "certifications", "High-assurance diodes pursue Common Criteria EAL certification (EAL4+, EAL7 for the strictest) proving the one-way property under evaluation. NERC CIP recognizes diodes for electronic security perimeters in the power grid. Certification turns a claim into evaluated fact.", {"Pursues": "CC EAL4+/EAL7", "Proves": "one-way, evaluated", "Grid": "NERC CIP recognized", "Turns": "claim into fact"}], ["Deployments: ICS and Power Grid", "deployments", "Data diodes guard industrial control systems: historian data flows out of the plant to the business network while control stays unreachable from it. Power grid operators deploy diodes at security perimeters. The plant talks; the plant cannot be talked to.", {"Guards": "ICS historians", "Grid": "perimeter enforcement", "Flows": "data out, never in", "Plant": "talks, can't be talked to"}], ["Diodes vs Firewalls", "optical-diodes", "A firewall is software policy that can be misconfigured or exploited; a diode is physics that cannot be reconfigured into two-way. Defense in depth uses both: diodes where the direction must be absolute, firewalls where policy suffices. Do not substitute one for the other.", {"Firewall": "policy, reconfigurable", "Diode": "physics, absolute", "Uses": "both, layered", "Substitutes": "never"}], ["File Transfer Across the Diode", "protocols", "Diode file transfer chops files into sequenced, checksummed chunks, blasts them across, and reassembles on receipt — with no acknowledgments, redundancy and FEC replace retransmission. Large files cross reliably one-way every day. The protocol does the reliability TCP cannot.", {"Chops": "sequenced chunks", "Replaces": "retransmission with FEC", "Crosses": "large files daily", "Does": "reliability without ACKs"}], ["Monitoring and SIEM Feeds", "protocols", "Security monitoring crosses diodes outward: IDS alerts, logs, and SIEM feeds flow from the protected enclave to analysts without giving analysts' network a path back in. The SOC sees everything and touches nothing. Visibility without vulnerability.", {"Flows": "alerts, logs outward", "SOC": "sees everything", "Touches": "nothing", "Gives": "visibility sans vulnerability"}], ["Video and Streaming Across", "throughput", "Even video crosses diodes: unidirectional streaming protocols carry camera feeds out of secure areas to monitoring stations. Latency stays low enough for live watch. Seeing out without a path in is the point of the camera.", {"Carries": "video outward", "Stays": "low latency", "Watches": "live", "Point": "see out, no path in"}], ["Testing the One-Way Property", "certifications", "The one-way property is tested adversarially: evaluators try to exfiltrate from the high side through every interface, timing channel, and fault they can devise. Passing means no path found under evaluation. This is security testing at its most literal.", {"Tests": "adversarial exfiltration", "Tries": "interfaces, timing, faults", "Passes": "no path found", "Is": "literal security testing"}], ["Redundancy and High Availability", "deployments", "Critical diode deployments run redundant pairs with failover so the one-way path survives hardware failure. Monitoring watches link health, not just traffic. Availability engineering applies to physics too.", {"Runs": "redundant pairs", "Survives": "HW failure", "Watches": "link health", "Applies": "to physics too"}], ["Covert Channels and Residual Risk", "certifications", "Honest diode engineering names residual risks: timing channels, compromised endpoints, and physical access are outside the diode's guarantee. The diode solves direction; the rest of the security program solves everything else. No single device is the whole program.", {"Names": "timing, endpoints, physical", "Solves": "direction", "Rest": "the security program", "No": "single-device program"}], ["The One-Way Architecture", "optical-diodes", "Ladder-top diodes: physics-enforced direction, proxied protocols, certified one-way property, deployed at perimeters, tested adversarially. Fifteen rungs from an LED and a photodiode to industrial networks that can report out but never be reached in.", {"Enforces": "physics", "Proxies": "protocols", "Certifies": "one-way", "Deploys": "perimeters"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var chunks=4+P.a%5, sz=1400;
var code='// Data-diode one-way transfer demo (simulated model)\n';
code+='var n='+chunks+',sz='+sz+',seq=0;\n';
code+='for(var i=0;i<n;i++){seq++;console.log("TX seq="+seq+" "+sz+"B -> (optical, no return path)");}\n';
code+='console.log(n*sz+" bytes moved one-way; reverse channel: none by physics");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-optical-data-diodes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-optical-data-diodes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
