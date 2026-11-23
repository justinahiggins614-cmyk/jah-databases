// Demo for the The Signature Orbital Mechanics Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-OMECHS-000001", "title": "Signature Low-Energy Lunar Transfer Design", "subject": "the Signature low-energy lunar transfer design"}, {"id": "JAH-OMECHS-000002", "title": "Signature Cislunar Gateway Orbit Design", "subject": "the Signature cislunar Gateway orbit design"}, {"id": "JAH-OMECHS-000003", "title": "Signature Frozen Orbit Design for Lunar Mapping", "subject": "the Signature frozen orbit design for lunar mapping"}, {"id": "JAH-OMECHS-000004", "title": "Signature Constellation Phasing Design", "subject": "the Signature constellation phasing design"}, {"id": "JAH-OMECHS-000005", "title": "Signature Debris-Avoidance Manoeuvre Plan", "subject": "the Signature debris-avoidance manoeuvre plan"}, {"id": "JAH-OMECHS-000006", "title": "Signature Earth-Moon Transfer Window Design", "subject": "the Signature Earth-Moon transfer window design"}, {"id": "JAH-OMECHS-000007", "title": "Signature Mars Transfer Window Design", "subject": "the Signature Mars transfer window design"}, {"id": "JAH-OMECHS-000008", "title": "Signature Venus Flyby Trajectory Design", "subject": "the Signature Venus flyby trajectory design"}, {"id": "JAH-OMECHS-000009", "title": "Signature Asteroid Rendezvous Design", "subject": "the Signature asteroid rendezvous design"}, {"id": "JAH-OMECHS-000010", "title": "Signature Comet Intercept Design", "subject": "the Signature comet intercept design"}, {"id": "JAH-OMECHS-000011", "title": "Signature Polar Orbit Earth Survey Design", "subject": "the Signature polar orbit Earth survey design"}, {"id": "JAH-OMECHS-000012", "title": "Signature Repeating Ground Track Design", "subject": "the Signature repeating ground track design"}, {"id": "JAH-OMECHS-000013", "title": "Signature Formation Flying Design", "subject": "the Signature formation flying design"}, {"id": "JAH-OMECHS-000014", "title": "Signature On-Orbit Servicing Rendezvous Design", "subject": "the Signature on-orbit servicing rendezvous design"}, {"id": "JAH-OMECHS-000015", "title": "Signature End-of-Life Disposal Orbit Design", "subject": "the Signature end-of-life disposal orbit design"}, {"id": "JAH-OMECHS-000016", "title": "Signature Multi-Burn Transfer Design", "subject": "the Signature multi-burn transfer design"}, {"id": "JAH-OMECHS-000017", "title": "Signature Inclination Change Optimization Design", "subject": "the Signature inclination change optimization design"}, {"id": "JAH-OMECHS-000018", "title": "Signature Aerobraking Design Study", "subject": "the Signature aerobraking design study"}, {"id": "JAH-OMECHS-000019", "title": "Signature Solar Sail Orbit Raising Design", "subject": "the Signature solar sail orbit raising design"}, {"id": "JAH-OMECHS-000020", "title": "Signature Tether Orbit Design Study", "subject": "the Signature tether orbit design study"}, {"id": "JAH-OMECHS-000021", "title": "Signature Interplanetary Cruise Design", "subject": "the Signature interplanetary cruise design"}, {"id": "JAH-OMECHS-000022", "title": "Signature Orbit Determination Design", "subject": "the Signature orbit determination design"}, {"id": "JAH-OMECHS-000023", "title": "Signature Collision Avoidance Design", "subject": "the Signature collision avoidance design"}, {"id": "JAH-OMECHS-000024", "title": "Signature Station-Keeping Budget Design", "subject": "the Signature station-keeping budget design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: orbital-mechanics-signature');
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
