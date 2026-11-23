// Demo for the The Signature Astrodynamics Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-ASTRODS-000001", "title": "Earth-Moon L1 Gateway Station Design Study", "subject": "an Earth-Moon L1 gateway station"}, {"id": "JAH-ASTRODS-000002", "title": "Earth-Moon L2 Halo Station Design Study", "subject": "an Earth-Moon L2 halo station"}, {"id": "JAH-ASTRODS-000003", "title": "Sun-Earth L1 Observatory Design Study", "subject": "a Sun-Earth L1 observatory"}, {"id": "JAH-ASTRODS-000004", "title": "Sun-Earth L2 Observatory Design Study", "subject": "a Sun-Earth L2 observatory"}, {"id": "JAH-ASTRODS-000005", "title": "Weak Stability Boundary Lunar Cargo Design Study", "subject": "a weak stability boundary lunar cargo route"}, {"id": "JAH-ASTRODS-000006", "title": "Ballistic Capture Mars Arrival Design Study", "subject": "a ballistic capture Mars arrival"}, {"id": "JAH-ASTRODS-000007", "title": "Interplanetary Transport Network Route Design Study", "subject": "an interplanetary transport network route design"}, {"id": "JAH-ASTRODS-000008", "title": "Multi-Flyby Tour Design Study", "subject": "a multi-flyby tour"}, {"id": "JAH-ASTRODS-000009", "title": "Solar Sail Lagrange Point Design Study", "subject": "a solar sail at a Lagrange point"}, {"id": "JAH-ASTRODS-000010", "title": "Electric Propulsion Spiral Design Study", "subject": "an electric propulsion spiral"}, {"id": "JAH-ASTRODS-000011", "title": "Cislunar Navigation Design Study", "subject": "cislunar navigation"}, {"id": "JAH-ASTRODS-000012", "title": "Deep-Space Navigation Design Study", "subject": "deep-space navigation"}, {"id": "JAH-ASTRODS-000013", "title": "Autonomous Station-Keeping Design Study", "subject": "autonomous station-keeping"}, {"id": "JAH-ASTRODS-000014", "title": "Formation Flying at Lagrange Points Design Study", "subject": "formation flying at Lagrange points"}, {"id": "JAH-ASTRODS-000015", "title": "Lunar Polar Orbit Design Study", "subject": "a lunar polar orbit"}, {"id": "JAH-ASTRODS-000016", "title": "Mars Phobos Rendezvous Design Study", "subject": "a Mars Phobos rendezvous"}, {"id": "JAH-ASTRODS-000017", "title": "Asteroid Belt Tour Design Study", "subject": "an asteroid belt tour"}, {"id": "JAH-ASTRODS-000018", "title": "Comet Sample Return Design Study", "subject": "a comet sample return"}, {"id": "JAH-ASTRODS-000019", "title": "Outer Planet Flyby Design Study", "subject": "an outer planet flyby"}, {"id": "JAH-ASTRODS-000020", "title": "Solar Polar Orbit Design Study", "subject": "a solar polar orbit"}, {"id": "JAH-ASTRODS-000021", "title": "Earth Escape Design Study", "subject": "an Earth escape"}, {"id": "JAH-ASTRODS-000022", "title": "Lunar Return Design Study", "subject": "a lunar return"}, {"id": "JAH-ASTRODS-000023", "title": "Deep-Space Maneuver Design Study", "subject": "a deep-space maneuver"}, {"id": "JAH-ASTRODS-000024", "title": "Astrodynamics Digital Twin Design Study", "subject": "an astrodynamics digital twin"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: astrodynamics-signature');
  console.log('EDITION: signature');
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
