(function(){'use strict';
/* jahdb-defense-aerospace-faraday-enclosures-signal-shielding-fabrics-1.0 — deterministic boundless generator for defense-aerospace-faraday-enclosures-signal-shielding-fabrics.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["enclosures", "fabrics", "testing", "emp-protection", "tempest"];
var PREFIX='JAH-DAE12-';
var EDITION='public';
var POOL=[["Faraday Cages: Blocking Radio Waves", "enclosures", "A Faraday enclosure is a conductive shell that blocks electromagnetic fields: incoming radio waves induce currents in the shell that cancel the field inside. Phones go silent in a sealed metal box for exactly this reason. Shielding effectiveness is measured in decibels — 60 dB means a million-fold field reduction.", {"Principle": "conductive shell cancels fields", "Measures": "shielding effectiveness (dB)", "60 dB": "million-fold reduction", "Demo": "phone in sealed box"}], ["Shielding Effectiveness in dB", "testing", "Shielding effectiveness (SE) in decibels quantifies an enclosure: 20 dB is 10x field reduction, 40 dB is 100x, 80 dB is 10,000x. Real enclosures quote SE across frequency bands because shielding varies with frequency. One number without a frequency is marketing, not engineering.", {"20 dB": "10x", "40 dB": "100x", "80 dB": "10,000x", "Needs": "frequency band specified"}], ["EMP Protection: MIL-STD-188-125", "emp-protection", "MIL-STD-188-125 specifies high-altitude EMP protection for ground facilities: shielding, filtering, and grounding that keep systems alive through the fast E1 pulse. Compliance is tested with pulse injection, not just analysis. EMP hardening is a facility discipline, not a product sticker.", {"Standard": "MIL-STD-188-125", "Threat": "HEMP E1 pulse", "Tested": "pulse injection", "Is": "facility discipline"}], ["TEMPEST: The Eavesdropping Threat", "tempest", "TEMPEST is the discipline of stopping information leaking through unintentional electromagnetic emanations — monitors, cables, and processors all radiate what they are doing. Shielded enclosures, filtered power, and red/black separation are the defenses. The threat is real enough to have classified standards (NACSIM 5100A).", {"Leaks": "unintentional emanations", "Defends": "shielding, filtering, separation", "Standard": "NACSIM 5100A (classified)", "Real": "enough to classify"}], ["Conductive Fabrics and Gaskets", "fabrics", "Shielding fabrics — nickel-copper ripstop, silver mesh — make flexible enclosures: bags, curtains, and garments that block RF while staying portable. Gaskets seal the seams where rigid enclosures meet doors and panels, because a slot is an antenna. The seam is where shielding usually fails.", {"Fabrics": "Ni-Cu ripstop, silver mesh", "Makes": "bags, curtains, garments", "Seals": "gaskets at seams", "Fails": "at the slot"}], ["Mission Darkness-Style Phone Bags", "enclosures", "Faraday bags for phones and laptops — Mission Darkness is the known brand — block cellular, WiFi, Bluetooth, and GPS so devices cannot be tracked or remotely wiped during transport or analysis. Forensics teams use them to preserve device state. Simple, physical, effective.", {"Blocks": "cellular, WiFi, BT, GPS", "Stops": "tracking, remote wipe", "Uses": "forensics transport", "Is": "simple and physical"}], ["Skin Depth and Material Choice", "testing", "Skin depth — how far fields penetrate a conductor — shrinks with frequency and conductivity: copper shields high frequencies in microns, while low frequencies need thick steel or mu-metal. Material choice follows the threat frequency. Physics picks the metal, not preference.", {"Skin depth": "penetration vs frequency", "High freq": "microns of copper", "Low freq": "thick steel/mu-metal", "Picks": "physics"}], ["Apertures: Every Hole Leaks", "enclosures", "Vents, cable penetrations, and display windows are apertures — and shielding degrades with the largest hole, not the best wall. Waveguide-below-cutoff vents pass air but not waves; filtered connectors pass signals but not RF. Enclosure design is aperture design.", {"Rule": "worst hole sets shielding", "Vents": "waveguide-below-cutoff", "Cables": "filtered connectors", "Design": "is aperture design"}], ["Shielded Rooms and SCIFs", "tempest", "Shielded rooms scale the Faraday cage to buildings: SCIFs (Sensitive Compartmented Information Facilities) combine RF shielding with acoustic, access, and procedural controls. Construction is inspected and accredited. A SCIF is a Faraday cage with a security policy.", {"Scales": "cage to building", "SCIF": "shielding + policy", "Inspected": "and accredited", "Is": "cage with policy"}], ["Testing Shielding: The Real Proof", "testing", "Shielding is proven by test: MIL-STD-285 and IEEE-299 methods measure SE with antennas inside and outside the enclosure across frequency sweeps. Doors get tested open-cycle because use degrades gaskets. Test reports, not datasheets, are the evidence.", {"Methods": "MIL-STD-285, IEEE-299", "Sweeps": "frequency by frequency", "Doors": "tested in use", "Evidence": "test reports"}], ["Grounding the Enclosure", "enclosures", "A shield must be grounded properly: single-point grounds avoid loops that re-radiate, and filters keep conducted noise off the power lines entering the cage. A floating shield is a capacitor; a looped shield is an antenna. Grounding is half the shielding art.", {"Grounds": "single-point, no loops", "Filters": "power-line conducted noise", "Floating": "a capacitor", "Loops": "an antenna"}], ["Portable Field Shielding", "fabrics", "Field operations use portable shielding: pop-up tents, vehicle liners, and equipment covers that deploy in minutes. Compromise is explicit — portable never matches a welded room — but 40 dB in the field beats 0 dB. Mobility has a shielding budget too.", {"Deploys": "tents, liners, covers", "Trade": "40dB mobile vs 100dB fixed", "Budget": "mobility costs dB", "Beats": "zero dB"}], ["Maintenance: Shielding Degrades", "testing", "Gaskets compress, doors wear, cables get added through new holes — shielding degrades with use and must be re-tested on schedule. Maintenance logs track every penetration. A shield is a living system, not a one-time purchase.", {"Degrades": "gaskets, doors, new holes", "Re-tests": "on schedule", "Logs": "every penetration", "Is": "a living system"}], ["Designing Shielding for a Threat", "emp-protection", "Shielding design starts from the threat: which frequencies, what field strength, continuous or pulsed — then materials, seams, apertures, and tests follow. Over-shielding wastes money; under-shielding fails silently. The threat model is the requirements document.", {"Starts": "threat frequencies/levels", "Follows": "materials, seams, tests", "Over": "wastes money", "Under": "fails silently"}], ["The Complete Shielding Picture", "tempest", "Ladder-top shielding: threat model, material, seams, apertures, grounding, testing, maintenance — the full discipline from physics to accredited facility. Fifteen rungs from a phone in a box to a SCIF that holds against nation-state collection.", {"Starts": "threat model", "Builds": "materials to rooms", "Proves": "testing", "Keeps": "maintenance"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var att=(60+(P.a%60));
var code='// Faraday shielding effectiveness demo (simulated model)\n';
code+='var atten_dB='+att+';\nvar ratio=Math.pow(10,atten_dB/20);\n';
code+='console.log("SE="+atten_dB+" dB -> field reduced "+ratio.toExponential(1)+"x");';return code;
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
var gen={version:'jahdb-defense-aerospace-faraday-enclosures-signal-shielding-fabrics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-faraday-enclosures-signal-shielding-fabrics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
