// Demo for the Space Mission Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SPMI-000001", "title": "Apollo 11 Lunar Landing Mission", "subject": "Apollo 11 lunar landing mission"}, {"id": "JAH-SPMI-000002", "title": "Hohmann Transfer Orbit Mission Design", "subject": "Hohmann transfer orbit mission design"}, {"id": "JAH-SPMI-000003", "title": "Artemis I Uncrewed Lunar Test Flight", "subject": "Artemis I uncrewed lunar test flight"}, {"id": "JAH-SPMI-000004", "title": "International Space Station Assembly and Operations", "subject": "International Space Station assembly and operations"}, {"id": "JAH-SPMI-000005", "title": "Voyager 1 Interstellar Mission", "subject": "Voyager 1 interstellar mission"}, {"id": "JAH-SPMI-000006", "title": "Mars Science Laboratory Curiosity Landing", "subject": "Mars Science Laboratory Curiosity landing"}, {"id": "JAH-SPMI-000007", "title": "James Webb Space Telescope Deployment", "subject": "James Webb Space Telescope deployment"}, {"id": "JAH-SPMI-000008", "title": "Cassini-Huygens Saturn Mission", "subject": "Cassini-Huygens Saturn mission"}, {"id": "JAH-SPMI-000009", "title": "Parker Solar Probe Solar Encounter", "subject": "Parker Solar Probe solar encounter"}, {"id": "JAH-SPMI-000010", "title": "Perseverance Mars Rover Mission", "subject": "Perseverance Mars rover mission"}, {"id": "JAH-SPMI-000011", "title": "Lunar Gateway Station Concept", "subject": "Lunar Gateway station concept"}, {"id": "JAH-SPMI-000012", "title": "Lagrange Point Halo Orbit Mission", "subject": "Lagrange point halo orbit mission"}, {"id": "JAH-SPMI-000013", "title": "Deep Space Network Tracking Architecture", "subject": "Deep Space Network tracking architecture"}, {"id": "JAH-SPMI-000014", "title": "Lunar Surface Exploration Mission", "subject": "Lunar surface exploration mission"}, {"id": "JAH-SPMI-000015", "title": "Mars Sample Return Mission Architecture", "subject": "Mars sample return mission architecture"}, {"id": "JAH-SPMI-000016", "title": "Asteroid Rendezvous Mission Design", "subject": "Asteroid rendezvous mission design"}, {"id": "JAH-SPMI-000017", "title": "Earth Orbit Constellation Mission", "subject": "Earth orbit constellation mission"}, {"id": "JAH-SPMI-000018", "title": "Venus Flyby Mission Design", "subject": "Venus flyby mission design"}, {"id": "JAH-SPMI-000019", "title": "Jupiter System Exploration Mission", "subject": "Jupiter system exploration mission"}, {"id": "JAH-SPMI-000020", "title": "Comet Rendezvous Mission Design", "subject": "Comet rendezvous mission design"}, {"id": "JAH-SPMI-000021", "title": "Lunar Polar Exploration Mission", "subject": "Lunar polar exploration mission"}, {"id": "JAH-SPMI-000022", "title": "Mars Transit Mission Architecture", "subject": "Mars transit mission architecture"}, {"id": "JAH-SPMI-000023", "title": "Interstellar Probe Mission Concept", "subject": "Interstellar probe mission concept"}, {"id": "JAH-SPMI-000024", "title": "Space Station Resupply Mission Operations", "subject": "Space station resupply mission operations"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: space-mission');
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
