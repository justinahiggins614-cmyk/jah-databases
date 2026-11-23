// Demo for the Orbital Mechanics Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-OMECH-000001", "title": "Kepler's Laws of Planetary Motion", "subject": "Kepler's laws of planetary motion"}, {"id": "JAH-OMECH-000002", "title": "Circular Orbits and Orbital Speed", "subject": "circular orbits and orbital speed"}, {"id": "JAH-OMECH-000003", "title": "Elliptic Orbits and Orbital Period", "subject": "elliptic orbits and orbital period"}, {"id": "JAH-OMECH-000004", "title": "Hohmann Transfer Orbit from Low Earth Orbit to Geostationary Orbit", "subject": "the Hohmann transfer orbit"}, {"id": "JAH-OMECH-000005", "title": "Bi-Elliptic Transfer and the Three-Burn Path", "subject": "the bi-elliptic transfer"}, {"id": "JAH-OMECH-000006", "title": "The Vis-Viva Equation and Orbital Energy", "subject": "the vis-viva equation"}, {"id": "JAH-OMECH-000007", "title": "Specific Orbital Energy of Earth Orbits", "subject": "specific orbital energy"}, {"id": "JAH-OMECH-000008", "title": "The Six Classical Orbital Elements", "subject": "the six classical orbital elements"}, {"id": "JAH-OMECH-000009", "title": "Orbital Inclination Change Manoeuvres", "subject": "orbital inclination change manoeuvres"}, {"id": "JAH-OMECH-000010", "title": "Geostationary Orbit and the Clarke Belt", "subject": "geostationary orbit"}, {"id": "JAH-OMECH-000011", "title": "Geostationary Transfer Orbit Operations", "subject": "geostationary transfer orbit operations"}, {"id": "JAH-OMECH-000012", "title": "Sun-Synchronous Orbit and Earth Observation", "subject": "sun-synchronous orbit"}, {"id": "JAH-OMECH-000013", "title": "Molniya Orbit and High-Latitude Coverage", "subject": "the Molniya orbit"}, {"id": "JAH-OMECH-000014", "title": "Hyperbolic Trajectories and Escape Velocity", "subject": "hyperbolic trajectories and escape velocity"}, {"id": "JAH-OMECH-000015", "title": "Orbital Rendezvous and Phasing", "subject": "orbital rendezvous and phasing"}, {"id": "JAH-OMECH-000016", "title": "Orbital Manoeuvres: Prograde, Retrograde, and Radial", "subject": "orbital manoeuvres"}, {"id": "JAH-OMECH-000017", "title": "Two-Line Element Sets and Satellite Tracking", "subject": "two-line element sets and satellite tracking"}, {"id": "JAH-OMECH-000018", "title": "Ground Tracks and Coverage Patterns", "subject": "ground tracks and coverage patterns"}, {"id": "JAH-OMECH-000019", "title": "Orbital Decay and Atmospheric Drag", "subject": "orbital decay and atmospheric drag"}, {"id": "JAH-OMECH-000020", "title": "Delta-V Budgets for Earth, Moon, and Mars Missions", "subject": "delta-v budgets for Earth, Moon, and Mars missions"}, {"id": "JAH-OMECH-000021", "title": "Gravity Assist and the Patched Conic Approximation", "subject": "gravity assist and the patched conic approximation"}, {"id": "JAH-OMECH-000022", "title": "Orbital Period and Mean Motion", "subject": "orbital period and mean motion"}, {"id": "JAH-OMECH-000023", "title": "Apsis: Perigee, Apogee, Perihelion, and Aphelion", "subject": "apsis points of orbits"}, {"id": "JAH-OMECH-000024", "title": "True Anomaly, Eccentric Anomaly, and Mean Anomaly", "subject": "true, eccentric, and mean anomaly"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: orbital-mechanics');
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
