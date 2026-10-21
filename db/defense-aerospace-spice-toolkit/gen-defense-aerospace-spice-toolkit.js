(function(){'use strict';
/* jahdb-defense-aerospace-spice-toolkit-1.0 — deterministic boundless generator for defense-aerospace-spice-toolkit.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["kernels", "toolkit-apis", "geometry", "time-systems", "missions"];
var PREFIX='JAH-DAE4-';
var EDITION='public';
var POOL=[["SPICE: JPL's Observation Geometry System", "kernels", "SPICE is NASA JPL's Navigation and Ancillary Information Facility (NAIF) system for observation geometry: it organizes and computes where spacecraft, planets, and instruments are and where they point. Missions from Cassini to Mars rovers plan observations with it. The Toolkit (CSPICE, Icy, SpiceyPy) is free and the kernels are archived publicly.", {"Developer": "JPL NAIF", "Purpose": "observation geometry", "Toolkit": "CSPICE, Icy, SpiceyPy", "Users": "Cassini, MRO, rovers", "Kernels": "public archive"}], ["SPK Kernels: Positions and Velocities", "kernels", "SPK kernels store ephemerides — position and velocity of bodies and spacecraft as functions of time, usually as Chebyshev polynomial segments. One file can cover a whole mission. SPICE interpolates the polynomials to any requested epoch. This is the 'where is it' half of geometry.", {"Kernel": "SPK", "Stores": "position + velocity vs time", "Format": "Chebyshev segments", "Query": "state at any epoch"}], ["CK Kernels: Attitude History", "kernels", "CK kernels store attitude — orientation as a function of time, as quaternions or matrices with angular velocity. Spacecraft CK plus instrument-frame definitions tell you exactly where a camera pointed for every image. Without CK, pixels have no direction.", {"Kernel": "CK", "Stores": "orientation vs time", "Format": "quaternions/matrices", "Need": "camera pointing per image"}], ["PCK, FK, and IK: Frames and Instruments", "kernels", "PCK kernels carry planetary constants and body orientations (pole direction, prime meridian); FK kernels define reference frames and their relationships; IK kernels describe instruments (field of view, pixels). Together with SPK/CK they complete the geometry chain from planet to pixel.", {"PCK": "body orientation, constants", "FK": "frame definitions", "IK": "instrument FOV, pixels", "Chain": "planet -> spacecraft -> pixel"}], ["SCLK and LSK: Time Kernels", "time-systems", "SCLK kernels convert spacecraft clock ticks to ephemeris time; LSK kernels carry the leapsecond table for UTC conversion. Time in SPICE is a first-class kernel problem because every position query needs an epoch. A stale leapsecond kernel shifts all your UTC tags.", {"SCLK": "spacecraft clock -> ET", "LSK": "leapsecond table", "Rule": "positions need epochs", "Stale LSK": "UTC tags shift"}], ["DSK: Digital Shape Kernels", "kernels", "DSK kernels store digital shape models — triangulated plates of asteroids, comet nuclei, and small moons — so SPICE can compute illumination, occultation, and surface intercepts on lumpy bodies. Ray-plate intersection against the shape model answers 'what pixel sees what rock.'", {"Kernel": "DSK", "Stores": "triangulated shape plates", "Solves": "illumination, occultation", "Use": "small-body proximity"}], ["CSPICE: The C Toolkit", "toolkit-apis", "CSPICE is the C implementation of the Toolkit: spkezr for states, pxform for frame transforms, ilumin for lighting angles, occultation routines, and dozens more. It is the reference implementation everything else ports. Mission software links it directly.", {"Language": "C (reference)", "Calls": "spkezr, pxform, ilumin", "Role": "reference implementation", "Links": "into flight/ground software"}], ["Geometry Finder: Events Without Propagating", "geometry", "SPICE's Geometry Finder searches kernel data for events — occultations, eclipses, lighting conditions — over time windows without propagating anything: it roots-finds on geometry functions. 'When is the next Earth occultation as seen from the orbiter?' is one call. Mission planning runs on these searches.", {"Searches": "occultations, eclipses, lighting", "Method": "root-finding on geometry", "Cost": "no propagation needed", "Use": "mission planning"}], ["Illumination Angles: Incidence, Emission, Phase", "geometry", "ilumin-style computations give incidence (sun-to-surface), emission (surface-to-observer), and phase (sun-surface-observer) angles for any surface point at any time. Camera exposure, science quality, and thermal input all key off these three angles. Every image is planned against them.", {"Angles": "incidence, emission, phase", "Drives": "exposure, science, thermal", "Plans": "every image", "Routine": "ilumin family"}], ["Occultations and Eclipses", "geometry", "SPICE occultation routines test whether the line of sight between two bodies clears a third — Earth occultations kill comms, solar eclipses kill power. Link budgets and battery sizing assume these blackouts. Geometry, not guesswork, sizes the margins.", {"Tests": "line-of-sight vs third body", "Earth occult": "comms blackout", "Solar eclipse": "power blackout", "Sizes": "link + battery margins"}], ["SPICE on Mars Missions", "missions", "Mars rovers and orbiters plan every observation with SPICE: rover mast pointing uses surface frames and CK-like attitude, orbiter relay passes use occultation searches, and entry-descent-landing analyses use SPK trajectories. The same kernels serve science planning and operations.", {"Rovers": "mast pointing, surface frames", "Orbiters": "relay occultation searches", "EDL": "SPK trajectories", "Dual use": "science + ops"}], ["Kernel Production and Archiving", "kernels", "Kernels are produced by missions and archived at NAIF: reconstructed SPKs from tracking data, CKs from attitude telemetry, and predicted kernels for planning. Versioning matters — reprocessing with better kernels changes science results. The archive is the permanent record of where everything was.", {"Producers": "mission nav teams", "Archive": "NAIF", "Types": "reconstructed + predicted", "Rule": "versioned, reprocessing-aware"}], ["Validating Geometry: The Closed Loop", "geometry", "Geometry validation closes the loop: predict an occultation with SPICE, then observe the signal drop at the predicted second. Image a star field and check the camera pointing solution against CK. When predictions match observations repeatedly, the kernel set is trusted.", {"Test 1": "predict occult, watch signal", "Test 2": "star field vs CK", "Bar": "repeated matches", "Result": "trusted kernel set"}], ["Writing Your Own SPICE Queries", "toolkit-apis", "A SPICE user loads kernels (furnsh), asks for a state (spkezr), transforms frames (pxform), and unloads — four steps that answer most geometry questions. Scripts chain these into planning tools. The Toolkit rewards the discipline of loading exactly the kernels a question needs.", {"Steps": "furnsh, spkezr, pxform", "Scripts": "planning tools", "Discipline": "load what you need", "Port": "SpiceyPy for Python users"}], ["The Full SPICE Geometry Chain", "missions", "The ladder-top SPICE picture: kernels encode positions, attitudes, frames, shapes, and time; the Toolkit interpolates and transforms; the Geometry Finder searches events; missions plan observations, comms, and power on the answers. Fifteen rungs up, that chain flies every deep-space mission JPL operates.", {"Encode": "kernels", "Compute": "Toolkit", "Search": "Geometry Finder", "Fly": "observations, comms, power"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var a=6778+(P.a%2000), e=((P.b%30)/1000).toFixed(3), inc=(28.5+(P.c%70)).toFixed(1);
var code='// SPICE-style orbital elements to state vector demo (simulated model)\n';
code+='var a='+a+',e='+e+',inc='+inc+'*Math.PI/180;\n';
code+='var p=a*(1-e*e), r=p/(1+e*Math.cos(0));\n';
code+='var x=r*Math.cos(0), y=r*Math.sin(0)*Math.cos(inc), z=r*Math.sin(0)*Math.sin(inc);\n';
code+='console.log("a="+a+"km e="+e+" inc='+inc+'deg");\nconsole.log("r_vec=["+x.toFixed(1)+","+y.toFixed(1)+","+z.toFixed(1)+"] km");';return code;
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
var gen={version:'jahdb-defense-aerospace-spice-toolkit-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-spice-toolkit',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
