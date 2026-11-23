// Demo for the Programmable Materials Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PROMAT-000001", "title": "What Programmable Materials Are", "subject": "programmable materials identity"}, {"id": "JAH-PROMAT-000002", "title": "Shape-Memory Alloys", "subject": "shape-memory alloys"}, {"id": "JAH-PROMAT-000003", "title": "Shape-Memory Polymers", "subject": "shape-memory polymers"}, {"id": "JAH-PROMAT-000004", "title": "Electroactive Polymers", "subject": "electroactive polymers"}, {"id": "JAH-PROMAT-000005", "title": "Magnetorheological Fluids", "subject": "magnetorheological fluids"}, {"id": "JAH-PROMAT-000006", "title": "Phase-Change Materials", "subject": "phase-change materials"}, {"id": "JAH-PROMAT-000007", "title": "Self-Healing Polymers", "subject": "self-healing polymers"}, {"id": "JAH-PROMAT-000008", "title": "Photo-Responsive Materials", "subject": "photo-responsive materials"}, {"id": "JAH-PROMAT-000009", "title": "4D Printing", "subject": "4d printing"}, {"id": "JAH-PROMAT-000010", "title": "Programmable Matter and Claytronics", "subject": "programmable matter and claytronics"}, {"id": "JAH-PROMAT-000011", "title": "Metamaterials with Tunable Properties", "subject": "metamaterials with tunable properties"}, {"id": "JAH-PROMAT-000012", "title": "Stimuli-Responsive Hydrogels", "subject": "stimuli-responsive hydrogels"}, {"id": "JAH-PROMAT-000013", "title": "Piezoelectric Materials", "subject": "piezoelectric materials"}, {"id": "JAH-PROMAT-000014", "title": "Thermoelectric Materials", "subject": "thermoelectric materials"}, {"id": "JAH-PROMAT-000015", "title": "Chromic Materials", "subject": "chromic materials"}, {"id": "JAH-PROMAT-000016", "title": "Programmable Stiffness Materials", "subject": "programmable stiffness materials"}, {"id": "JAH-PROMAT-000017", "title": "Soft Robotics Materials", "subject": "soft robotics materials"}, {"id": "JAH-PROMAT-000018", "title": "Programmable Textiles", "subject": "programmable textiles"}, {"id": "JAH-PROMAT-000019", "title": "Self-Assembling Materials", "subject": "self-assembling materials"}, {"id": "JAH-PROMAT-000020", "title": "Programmable Materials Testing and Standards", "subject": "programmable materials testing"}, {"id": "JAH-PROMAT-000021", "title": "Programmable Materials in Medicine", "subject": "programmable materials in medicine"}, {"id": "JAH-PROMAT-000022", "title": "Programmable Materials in Buildings", "subject": "programmable materials in buildings"}, {"id": "JAH-PROMAT-000023", "title": "Programmable Materials and Sustainability", "subject": "programmable materials and sustainability"}, {"id": "JAH-PROMAT-000024", "title": "The Future of Programmable Materials", "subject": "future of programmable materials"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: programmable-materials');
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
