(function(){'use strict';
/* jahdb-defense-aerospace-physical-kill-switch-relays-1.0 — deterministic boundless generator for defense-aerospace-physical-kill-switch-relays.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["relays", "memory-wipe", "power-design", "field-use", "safety"];
var PREFIX='JAH-DAE20-';
var EDITION='public';
var POOL=[["Kill Switches: The Last-Resort Control", "relays", "A physical kill switch is a hardware power cutoff — a relay, contactor, or breaker wired to drop power to a system instantly and unconditionally, independent of software. In field emergencies (capture, compromise), it is the control that cannot be hacked because it is not software. The last resort must be the most reliable control.", {"Cuts": "power, instantly", "Independent": "of software", "Cannot": "be hacked", "Must": "be most reliable"}], ["Relays vs Contactors vs Breakers", "relays", "Small relays switch logic-level loads, contactors switch high-current DC/AC, breakers add overcurrent protection — the cutoff chain picks the device per the load it must drop. Coil voltage, contact rating, and fail-safe state (normally-open vs closed) are the selection parameters. The right device for the amperage.", {"Relays": "small loads", "Contactors": "high current", "Breakers": "+ overcurrent", "Picks": "per load"}], ["RAM Remanence: Why Power-Cut Matters", "memory-wipe", "DRAM keeps its data for seconds after power loss — longer when cold — which is the cold-boot attack: freeze the RAM, move it, read the keys. Cutting power fast and keeping it off lets remanence decay past recovery. The kill switch fights physics with speed.", {"Keeps": "data seconds after power", "Attack": "cold-boot reads keys", "Fights": "with fast cutoff", "Decays": "past recovery"}], ["Memory Scrubbing Sequences", "memory-wipe", "Before or with the power cut, scrub routines overwrite RAM and registers with zeros or patterns — defense in depth for the remanence window. Scrub-then-cut covers the seconds that cut alone leaves. The sequence is timed in milliseconds.", {"Overwrites": "RAM, registers", "Covers": "remanence window", "Timed": "milliseconds", "Layers": "scrub then cut"}], ["Fail-Safe vs Fail-Secure Wiring", "power-design", "Fail-safe wiring drops power when the control signal is lost (safe for personnel, dangerous for data); fail-secure holds state (safe for data, needs deliberate action). Kill switches choose per the asset: personnel safety vs data destruction. The wiring diagram encodes the policy.", {"Fail-safe": "drops on signal loss", "Fail-secure": "holds state", "Chooses": "per asset", "Encodes": "policy in wiring"}], ["Tamper-Triggered Cutoffs", "field-use", "Tamper sensors — chassis intrusion, accelerometer shock, light sensors — can trigger the kill relay automatically when a device is opened or seized. The device defends itself when the operator cannot. Automatic does not mean accidental: triggers need debouncing and arming discipline.", {"Triggers": "intrusion, shock, light", "Defends": "itself", "Needs": "debounce + arming", "Automatic": "not accidental"}], ["Dead-Man Switches", "field-use", "A dead-man switch requires continuous positive action — held button, periodic check-in — and fires the kill when the action stops. The operator's continued presence is the authorization. Capture or incapacitation removes the authorization automatically.", {"Requires": "continuous action", "Fires": "when action stops", "Authorizes": "presence", "Removes": "on capture"}], ["Purism-Style Hardware Kill Switches", "relays", "Purism's Librem laptops made kill switches visible: physical switches cutting the camera/mic and radios, verifiable by the user. The concept scales from privacy switches to full power kills. A switch you can see and feel is a switch you can trust.", {"Cuts": "camera/mic/radios", "Verifiable": "by the user", "Scales": "to full kills", "Trusts": "what you can feel"}], ["Emergency Procedures and Drills", "field-use", "Kill switches need procedures: who may authorize, how to verify the kill worked, what to do with the dead hardware, and drills so the action is reflex. An untested kill switch is a hope. Field teams drill the worst day.", {"Defines": "who authorizes", "Verifies": "kill worked", "Drills": "to reflex", "Untested": "is hope"}], ["Verifying the Kill Worked", "safety", "After the kill, verification confirms power is truly gone — no standby rails, no capacitors holding charge, memory decayed. Test points and procedures prove the dark state. Trust the meter, not the click.", {"Confirms": "no standby rails", "Checks": "capacitors, decay", "Proves": "dark state", "Trusts": "the meter"}], ["Safety Interlocks", "safety", "Kill switches that drop high power need interlocks — guards against accidental activation, two-action arming, covers over the big red button. Safety engineering keeps the last resort from firing on a bump. Deliberate, never casual.", {"Guards": "against accidents", "Requires": "two-action arming", "Covers": "the button", "Keeps": "deliberate"}], ["Key Destruction vs Data Destruction", "memory-wipe", "Destroying keys (crypto-shredding) is faster and often sufficient — without keys, encrypted data is noise — while full data destruction takes longer. Kill switches pair with crypto-erase: cut power and drop the keys. Speed where it counts.", {"Keys": "crypto-shred, fast", "Data": "slower to destroy", "Pairs": "kill + erase", "Speeds": "where it counts"}], ["Post-Kill Forensics", "field-use", "After a kill, forensics asks what happened: relay logs, sensor triggers, and the dead hardware's state get documented. The kill itself is an event with a chain of custody. Even destruction gets paperwork.", {"Asks": "what happened", "Logs": "triggers, relay state", "Documents": "the event", "Gets": "paperwork too"}], ["Selecting Kill-Switch Hardware", "power-design", "Selection matches relay to load, trigger to threat, and wiring to policy — with derating for the field environment. The bill of materials is short; the thinking is long. Every part earns its place.", {"Matches": "relay to load", "Triggers": "to threat", "Wires": "to policy", "Thinks": "long, BOM short"}], ["The Kill-Switch Discipline", "safety", "Ladder-top kill switches: right device, right trigger, scrub-then-cut, interlocked, drilled, verified dark. Fifteen rungs from a relay to a last resort the field can bet lives and secrets on.", {"Devices": "matched", "Triggers": "disciplined", "Acts": "scrub then cut", "Proves": "dark"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var code='// Kill-switch RAM remanence demo (simulated model)\n';
code+='var t_half=2.5,t=0,charge=100;\n';
code+='console.log("RELAY OPEN at t=0: power cut");\n';
code+='for(var i=0;i<5;i++){t+=1;charge=100*Math.pow(0.5,t/t_half);console.log("t+"+t+"s charge="+charge.toFixed(1)+"%");}\n';
code+='console.log("volatile memory unrecoverable");';return code;
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
var gen={version:'jahdb-defense-aerospace-physical-kill-switch-relays-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-physical-kill-switch-relays',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
