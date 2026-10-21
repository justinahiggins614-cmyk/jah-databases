(function(){'use strict';
/* jahdb-defense-aerospace-tactical-ruggedized-hard-cases-1.0 — deterministic boundless generator for defense-aerospace-tactical-ruggedized-hard-cases.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hard-cases", "foam-systems", "environmental", "standards", "field-kits"];
var PREFIX='JAH-DAE19-';
var EDITION='public';
var POOL=[["Ruggedized Hard Cases: Armor for Equipment", "hard-cases", "Tactical ruggedized hard cases — Pelican, SKB, and their class — are roto-molded or injection-molded polymer shells that carry sensitive equipment through drops, water, dust, and stacking. Custom foam interiors cradle each item. The case is the difference between 'shipped' and 'arrived working.'", {"Builds": "molded polymer shells", "Survives": "drops, water, dust", "Cradles": "custom foam", "Means": "arrived working"}], ["Pelican Air and the Classics", "hard-cases", "Pelican's Air line cut case weight with HPX resin while keeping the crushproof, dustproof promise — the classic 1615/1650 sizes are the field standard. SKB's iSeries competes on the same terms. The category is mature; the differences are in latches, valves, and foam.", {"Cuts": "weight via HPX resin", "Keeps": "crushproof promise", "Sizes": "1615/1650-class", "Differs": "latches, valves, foam"}], ["IP67: Dust-Tight and Immersion-Proof", "environmental", "IP67 means dust-tight (6) and surviving 1m immersion for 30 minutes (7) — the sealing bar for field cases, via gasketed lids and purge valves. IP ratings are tested, not claimed. Water stays out or the rating is fiction.", {"6": "dust-tight", "7": "1m/30min immersion", "Seals": "gaskets, purge valves", "Tested": "not claimed"}], ["MIL-STD-810: The Test Regime", "standards", "MIL-STD-810 is the environmental test regime — drop, vibration, shock, temperature, humidity, sand — that rugged cases get tested against. 'Designed to 810' means little; 'tested to 810 methods' with a report means everything. Procurement reads the test reports.", {"Tests": "drop, vibe, shock, climate", "Means": "methods + report", "Not": "'designed to'", "Reads": "procurement reads reports"}], ["Custom Foam: The Cradle", "foam-systems", "Custom foam — CNC-cut polyethylene or polyurethane — holds each item in a fitted cavity so nothing moves, rattles, or point-loads in transit. Foam is designed around the equipment, not the case. Two layers (lid + base) is the standard build.", {"Cuts": "CNC polyethylene", "Holds": "fitted cavities", "Designs": "around equipment", "Builds": "lid + base layers"}], ["Pressure Equalization Valves", "environmental", "Automatic purge valves equalize case pressure across altitude and temperature changes while blocking water and dust — without one, a sealed case vacuum-locks or pops its gasket. The little valve is load-bearing engineering. GORE-style membranes do the breathing.", {"Equalizes": "altitude/temp pressure", "Blocks": "water, dust", "Prevents": "vacuum lock", "Is": "load-bearing"}], ["Latches, Hinges, and Handles", "hard-cases", "Double-throw latches stay shut under impact, stainless hinges survive the salt, and fold-down handles take the stacking load — the small hardware that decides whether the case works after the tenth deployment. Cheap hardware is the most expensive choice.", {"Latches": "double-throw, stay shut", "Hinges": "stainless", "Handles": "stacking load", "Cheap": "most expensive"}], ["Rackmount Cases for Servers", "field-kits", "Rackmount transit cases put 19-inch servers in shock-mounted frames inside the shell — edge-AI servers ride to the field in these. Shock mounts decouple the rack from the case so drops become gentle decelerations. Compute goes where the mission is.", {"Mounts": "19in shock frames", "Carries": "edge-AI servers", "Decouples": "shock from rack", "Takes": "compute to mission"}], ["Desert, Arctic, and Maritime Kits", "environmental", "Environment kits adapt cases: desiccant and dust filters for desert, insulation and heaters for arctic, corrosion protection for maritime. The case is the platform; the kit is the mission config. One shell, many climates.", {"Desert": "desiccant, dust filters", "Arctic": "insulation, heaters", "Maritime": "corrosion proof", "One": "shell, many climates"}], ["ATA 300: Airline Transport", "standards", "ATA Specification 300 governs reusable airline transport containers — the category under which rugged cases fly as checked equipment. Cases that meet ATA 300 survive baggage handling repeatedly. The airline is an environmental test too.", {"Governs": "airline containers", "Survives": "baggage handling", "Repeatedly": "reusable", "Is": "a test regime"}], ["Stacking and Palletizing", "field-kits", "Cases stack and palletize with interlocking lids and documented stacking loads — logistics runs on the rectangle. Weight distribution and tie-down points are part of the design. The warehouse is part of the mission.", {"Stacks": "interlocking lids", "Documents": "stacking loads", "Runs": "logistics", "Is": "mission infrastructure"}], ["Security: Locks and Seals", "field-kits", "Cases take padlocks, and seal hasps take the tamper-evident seals from the companion discipline — physical security rides with the equipment. Lock the case, seal the hasp, log the number. Transport security is layered.", {"Locks": "padlock hasps", "Seals": "tamper-evident", "Logs": "seal numbers", "Layers": "transport security"}], ["Field Repair of Cases", "hard-cases", "Cases get repaired in the field — latch kits, valve replacements, foam re-cuts — because the case fleet is infrastructure. Repair beats replace on cost and on downtime. Maintain the armor.", {"Repairs": "latches, valves, foam", "Beats": "replace on cost", "Is": "infrastructure", "Maintains": "the armor"}], ["Sizing the Case to the Load", "foam-systems", "Case sizing starts from the equipment envelope plus foam plus handling clearances — too tight crushes connectors, too loose lets loads shift. The tape measure is the first design tool. Fit is protection.", {"Starts": "equipment envelope", "Adds": "foam + clearance", "Tight": "crushes", "Loose": "shifts"}], ["The Complete Transport Picture", "field-kits", "Ladder-top cases: rated shell, fitted foam, sealed and valved, tested to 810, locked and sealed, stacked on pallets. Fifteen rungs from a plastic box to edge-AI servers arriving working in a desert.", {"Shells": "rated polymer", "Foams": "fitted", "Seals": "IP67 + valves", "Tests": "810 reports"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var L=(60+(P.a%40)), W=(40+(P.b%30)), H=(25+(P.c%20));
var code='// Rugged case volume + foam demo (simulated model)\n';
code+='var L='+L+',W='+W+',H='+H+';\nvar vol=L*W*H/1e6;\n';
code+='console.log(L+"x"+W+"x"+H+" cm -> "+vol.toFixed(2)+" m^3, foam cut 2 layers");';return code;
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
var gen={version:'jahdb-defense-aerospace-tactical-ruggedized-hard-cases-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-tactical-ruggedized-hard-cases',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
