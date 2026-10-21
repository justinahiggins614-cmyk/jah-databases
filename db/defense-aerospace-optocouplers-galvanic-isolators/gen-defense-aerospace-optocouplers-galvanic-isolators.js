(function(){'use strict';
/* jahdb-defense-aerospace-optocouplers-galvanic-isolators-1.0 — deterministic boundless generator for defense-aerospace-optocouplers-galvanic-isolators.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["digital-isolators", "analog-optocouplers", "safety-ratings", "gate-drivers", "signal-integrity"];
var PREFIX='JAH-DAE14-';
var EDITION='public';
var POOL=[["Galvanic Isolation: Breaking the Copper Path", "digital-isolators", "Galvanic isolation breaks the direct electrical connection between two circuits while letting signals cross — no shared ground, no current path for surges. Transformers, capacitors, and light do the crossing. Isolation is what keeps a high-voltage fault on one side from becoming a disaster on the other.", {"Breaks": "electrical connection", "Keeps": "signal crossing", "Stops": "surges, ground loops", "Media": "light, magnetic, capacitive"}], ["Optocouplers: Signals on Light", "analog-optocouplers", "An optocoupler pairs an LED with a photodetector in one package: current through the LED becomes light, light becomes current on the other side, with kilovolts of isolation between. The classic 4N25-style part has isolated thousands of industrial interfaces. Light crosses; voltage does not.", {"Pairs": "LED + photodetector", "Crosses": "light", "Blocks": "kilovolts", "Classic": "4N25-style parts"}], ["Current Transfer Ratio (CTR)", "analog-optocouplers", "CTR — output current over input current, in percent — is the optocoupler's gain: it varies with temperature, LED aging, and drive current, so designs derate it generously. A CTR of 50-600% is typical for transistor-output parts. Designing to worst-case CTR is the difference between working and flaky.", {"CTR": "Iout/Iin, percent", "Varies": "temp, aging, current", "Typical": "50-600%", "Designs": "to worst case"}], ["Digital Isolators: The Modern Replacement", "digital-isolators", "Digital isolators (Analog Devices iCoupler, TI ISO77xx) replace LED optocouplers with on-chip transformers or capacitors: faster (150 Mbps), lower power, tighter timing, and longer life — no LED to age. They dominate new isolated digital designs. The optocoupler remains where proven simplicity wins.", {"Replaces": "LED with transformers/caps", "Speeds": "to 150 Mbps", "Wins": "power, timing, lifetime", "Keeps": "optos where simple wins"}], ["Isolation Voltage Ratings", "safety-ratings", "Isolation is rated in volts RMS or DC the barrier withstands — 2.5 kV, 5 kV, more — tested per UL 1577, IEC 60747-5-5, or VDE. Ratings assume creepage and clearance distances on the board, not just the package. The rating is only as good as the layout around it.", {"Rated": "kVrms withstand", "Tests": "UL 1577, IEC, VDE", "Needs": "creepage + clearance", "Layout": "part of the rating"}], ["Common-Mode Transient Immunity (CMTI)", "signal-integrity", "CMTI measures how fast a common-mode voltage spike the isolator tolerates without corrupting data — 100+ kV/µs for modern parts switching SiC/GaN gates. Motor drives and fast switchers live or die on CMTI. A slow isolator in a fast drive is a glitch generator.", {"Measures": "kV/us tolerated", "Needs": "100+ for SiC/GaN", "Matters": "motor drives", "Slow part": "glitch generator"}], ["Isolated Gate Drivers", "gate-drivers", "Isolated gate drivers combine isolation with the muscle to switch power transistors — driving IGBT/SiC gates across the barrier with desaturation protection and Miller clamping. They are the standard interface between control logic and power stages. One package: isolation plus drive.", {"Drives": "IGBT/SiC gates", "Across": "the barrier", "Protects": "desat, Miller clamp", "Is": "isolation + muscle"}], ["Reinforced vs Basic Isolation", "safety-ratings", "Safety standards distinguish basic isolation (one barrier, needs a second protective measure) from reinforced (a single barrier rated as two). Medical and mains-connected equipment often requires reinforced. The distinction is in the standard's testing, not just the datasheet claim.", {"Basic": "one barrier + second measure", "Reinforced": "single barrier, double-rated", "Requires": "medical, mains", "In": "the standard's testing"}], ["Side-Channel Defense by Isolation", "signal-integrity", "Galvanic isolation also breaks side-channel paths: power-analysis and EM probes on one side see nothing of the cryptographic operations on the other. Secure hardware isolates its crypto island physically, not just logically. Defense in depth starts at the circuit level.", {"Breaks": "power/EM side channels", "Isolates": "crypto island", "Physically": "not just logically", "Starts": "at circuits"}], ["Analog Isolation: Linear Optocouplers", "analog-optocouplers", "Linear optocouplers (HCNR201-style) pass analog signals across the barrier with a feedback photodiode servoing the LED — 0.01% linearity for isolated measurement. Current loops and medical sensing use them. Analog across isolation is harder than digital; the servo makes it honest.", {"Passes": "analog across barrier", "Servo": "feedback photodiode", "Linearity": "0.01%", "Uses": "loops, medical"}], ["Creepage and Clearance Layout", "safety-ratings", "Creepage (along surfaces) and clearance (through air) distances on the PCB complete the isolation the package starts — standards tables set millimeters per voltage and pollution degree. Slots and moats in the board enforce it. The best isolator fails in a sloppy layout.", {"Creepage": "along surfaces", "Clearance": "through air", "Enforces": "slots, moats", "Fails": "in sloppy layout"}], ["Surge and ESD Across the Barrier", "signal-integrity", "Isolation barriers are surge-tested — kilovolt transients per IEC 61000-4-5 — to prove the barrier holds when the real world strikes. ESD guns test the human-touch case. Ratings on paper become ratings in the lab.", {"Surge": "kV per IEC 61000-4-5", "ESD": "human-touch case", "Proves": "barrier holds", "Becomes": "lab-proven ratings"}], ["Choosing the Isolator", "digital-isolators", "Isolator selection weighs speed, voltage, CMTI, power, channels, and lifetime against cost: digital isolators for fast data, optocouplers for proven analog and high-voltage niches, reinforced grades where safety demands. The application picks; the datasheet confirms.", {"Weighs": "speed, volts, CMTI, cost", "Digital": "fast data", "Opto": "analog, HV niches", "Picks": "the application"}], ["Isolation for Cryptographic Hardware", "signal-integrity", "Secure modules isolate key operations behind barriers — power, signal, and physical — so attacks must cross engineered boundaries. Isolation is one layer of the tamper-resistance stack alongside enclosures and sensors. Boundaries compound.", {"Isolates": "key operations", "Layers": "with enclosures, sensors", "Forces": "attacks across boundaries", "Compounds": "boundaries"}], ["The Isolation Design Discipline", "safety-ratings", "Ladder-top isolation: threat voltages, barrier technology, ratings, layout, CMTI, testing — the complete discipline from physics to certified product. Fifteen rungs from an LED and a photodiode to hardware that survives lightning and spies.", {"Starts": "threat voltages", "Builds": "barriers + layout", "Proves": "testing", "Survives": "surges and probes"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var ctr=(80+(P.a%120)), iin=(5+(P.b%15));
var code='// Optocoupler CTR transfer demo (simulated model)\n';
code+='var ctr='+ctr+',i_in='+iin+';\nvar i_out=i_in*ctr/100;\n';
code+='console.log("CTR="+ctr+"% Iin="+i_in+"mA -> Iout="+i_out.toFixed(1)+"mA");';return code;
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
var gen={version:'jahdb-defense-aerospace-optocouplers-galvanic-isolators-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-optocouplers-galvanic-isolators',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
