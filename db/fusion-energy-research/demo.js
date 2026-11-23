// Demo for the Fusion Energy Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-FER-000001", "title": "What Fusion Energy Research Is", "subject": "fusion energy research identity"}, {"id": "JAH-FER-000002", "title": "The Deuterium-Tritium Reaction", "subject": "deuterium-tritium reaction"}, {"id": "JAH-FER-000003", "title": "The Lawson Criterion", "subject": "lawson criterion"}, {"id": "JAH-FER-000004", "title": "Tokamaks", "subject": "tokamaks"}, {"id": "JAH-FER-000005", "title": "Stellarators", "subject": "stellarators"}, {"id": "JAH-FER-000006", "title": "ITER", "subject": "iter"}, {"id": "JAH-FER-000007", "title": "JET", "subject": "jet"}, {"id": "JAH-FER-000008", "title": "Inertial Confinement Fusion", "subject": "inertial confinement fusion"}, {"id": "JAH-FER-000009", "title": "The National Ignition Facility", "subject": "national ignition facility"}, {"id": "JAH-FER-000010", "title": "Magnetic Confinement and Plasma Stability", "subject": "magnetic confinement and plasma stability"}, {"id": "JAH-FER-000011", "title": "Plasma Heating Methods", "subject": "plasma heating methods"}, {"id": "JAH-FER-000012", "title": "Tritium Breeding and Fuel Cycle", "subject": "tritium breeding and fuel cycle"}, {"id": "JAH-FER-000013", "title": "Neutron-Resistant Materials", "subject": "neutron-resistant materials"}, {"id": "JAH-FER-000014", "title": "Superconducting Magnets for Fusion", "subject": "superconducting magnets for fusion"}, {"id": "JAH-FER-000015", "title": "Fusion Diagnostics", "subject": "fusion diagnostics"}, {"id": "JAH-FER-000016", "title": "The Q Factor and Energy Gain", "subject": "q factor and energy gain"}, {"id": "JAH-FER-000017", "title": "Spherical Tokamaks", "subject": "spherical tokamaks"}, {"id": "JAH-FER-000018", "title": "Private Fusion Research", "subject": "private fusion research"}, {"id": "JAH-FER-000019", "title": "Fusion Safety and Regulation", "subject": "fusion safety and regulation"}, {"id": "JAH-FER-000020", "title": "Fusion and the Electricity Grid", "subject": "fusion and electricity grid"}, {"id": "JAH-FER-000021", "title": "Alternative Fusion Fuels", "subject": "alternative fusion fuels"}, {"id": "JAH-FER-000022", "title": "Fusion Simulation and Modelling", "subject": "fusion simulation and modelling"}, {"id": "JAH-FER-000023", "title": "Fusion Workforce and Education", "subject": "fusion workforce and education"}, {"id": "JAH-FER-000024", "title": "The Future of Fusion Research", "subject": "future of fusion research"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: fusion-energy-research');
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
