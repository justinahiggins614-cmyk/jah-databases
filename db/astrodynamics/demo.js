// Demo for the Astrodynamics Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-ASTROD-000001", "title": "The Three-Body Problem and the Restricted Three-Body Problem", "subject": "the three-body problem"}, {"id": "JAH-ASTROD-000002", "title": "Lagrange Points L1 to L5", "subject": "Lagrange points L1 to L5"}, {"id": "JAH-ASTROD-000003", "title": "Halo Orbits Around Lagrange Points", "subject": "halo orbits around Lagrange points"}, {"id": "JAH-ASTROD-000004", "title": "Lissajous Orbits and the SOHO Mission", "subject": "Lissajous orbits"}, {"id": "JAH-ASTROD-000005", "title": "Hill Sphere and Sphere of Influence", "subject": "Hill sphere and sphere of influence"}, {"id": "JAH-ASTROD-000006", "title": "The N-Body Problem and Numerical Integration", "subject": "the N-body problem and numerical integration"}, {"id": "JAH-ASTROD-000007", "title": "Perturbation Theory in Astrodynamics", "subject": "perturbation theory in astrodynamics"}, {"id": "JAH-ASTROD-000008", "title": "Solar Radiation Pressure Perturbations", "subject": "solar radiation pressure perturbations"}, {"id": "JAH-ASTROD-000009", "title": "Atmospheric Drag Perturbations", "subject": "atmospheric drag perturbations"}, {"id": "JAH-ASTROD-000010", "title": "The J2 Oblateness Perturbation", "subject": "the J2 oblateness perturbation"}, {"id": "JAH-ASTROD-000011", "title": "Weak Stability Boundary Transfers", "subject": "weak stability boundary transfers"}, {"id": "JAH-ASTROD-000012", "title": "Ballistic Capture at the Moon and Mars", "subject": "ballistic capture at the Moon and Mars"}, {"id": "JAH-ASTROD-000013", "title": "The Interplanetary Transport Network", "subject": "the interplanetary transport network"}, {"id": "JAH-ASTROD-000014", "title": "The Patched Conic Approximation", "subject": "the patched conic approximation"}, {"id": "JAH-ASTROD-000015", "title": "Gravity Assist Mechanics", "subject": "gravity assist mechanics"}, {"id": "JAH-ASTROD-000016", "title": "Low-Energy Transfers and the Interplanetary Superhighway", "subject": "low-energy transfers"}, {"id": "JAH-ASTROD-000017", "title": "Station-Keeping at Lagrange Points", "subject": "station-keeping at Lagrange points"}, {"id": "JAH-ASTROD-000018", "title": "Orbital Node Regression and Precession", "subject": "orbital node regression and precession"}, {"id": "JAH-ASTROD-000019", "title": "Argument of Periapsis and Orbital Orientation", "subject": "argument of periapsis and orbital orientation"}, {"id": "JAH-ASTROD-000020", "title": "Escape Velocity and Hyperbolic Excess Velocity", "subject": "escape velocity and hyperbolic excess velocity"}, {"id": "JAH-ASTROD-000021", "title": "Geosynchronous Orbit Dynamics", "subject": "geosynchronous orbit dynamics"}, {"id": "JAH-ASTROD-000022", "title": "Orbital Speed and Energy Across Orbit Types", "subject": "orbital speed and energy across orbit types"}, {"id": "JAH-ASTROD-000023", "title": "Ground Track Geometry and Repeating Orbits", "subject": "ground track geometry and repeating orbits"}, {"id": "JAH-ASTROD-000024", "title": "Orbit Determination from Observations", "subject": "orbit determination from observations"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: astrodynamics');
  console.log('EDITION: public');
  console.log('RECORDS: '+RECORDS.length);
  const q1=RECORDS[0].title.split(/\s+/).find(w=>w.length>3).toLowerCase();
  const hits=search(q1);
  console.log('SEARCH "'+q1+'": '+hits.length+' hit(s)');
  for(const h of hits.slice(0,5)){console.log('  - '+h.id+' :: '+h.title);}
  const all=search('');
  console.log('SEARCH "" (all): '+all.length+' record(s)');
  const rng=mulberry32(7);
  const words=[...new Set(RECORDS.flatMap(r=>r.title.split(/[^A-Za-z]+/).filter(w=>w.length>3)))];
  console.log('GENERATOR DEMO (seed 7, 5 samples):');
  for(let i=0;i<5;i++){const a=words[Math.floor(rng()*words.length)];const b=words[Math.floor(rng()*words.length)];console.log('  GEN-'+(i+1)+': '+a+' '+b);}
  const totalTitleChars=RECORDS.reduce((n,r)=>n+r.title.length,0);
  console.log('TOTAL TITLE CHARS: '+totalTitleChars);
  console.log('TITLE CHECKSUM: '+titleChecksum());
  console.log('DEMO OK');
}
main();
