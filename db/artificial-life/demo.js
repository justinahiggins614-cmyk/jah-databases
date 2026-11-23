// Demo for the Artificial Life Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-ALIFE-000001", "title": "What Artificial Life Is", "subject": "artificial life identity"}, {"id": "JAH-ALIFE-000002", "title": "Digital Organisms", "subject": "digital organisms"}, {"id": "JAH-ALIFE-000003", "title": "Tierra and Early Digital Evolution", "subject": "tierra digital evolution"}, {"id": "JAH-ALIFE-000004", "title": "Avida and Digital Evolution Research", "subject": "avida digital evolution"}, {"id": "JAH-ALIFE-000005", "title": "Conway's Game of Life", "subject": "game of life"}, {"id": "JAH-ALIFE-000006", "title": "Cellular Automata", "subject": "cellular automata"}, {"id": "JAH-ALIFE-000007", "title": "Self-Replication in Software", "subject": "self-replication in software"}, {"id": "JAH-ALIFE-000008", "title": "Artificial Chemistries", "subject": "artificial chemistries"}, {"id": "JAH-ALIFE-000009", "title": "Protocells and Minimal Cells", "subject": "protocells and minimal cells"}, {"id": "JAH-ALIFE-000010", "title": "Xenobots and Living Robots", "subject": "xenobots and living robots"}, {"id": "JAH-ALIFE-000011", "title": "Minimal Genomes", "subject": "minimal genomes"}, {"id": "JAH-ALIFE-000012", "title": "Open-Ended Evolution", "subject": "open-ended evolution"}, {"id": "JAH-ALIFE-000013", "title": "Evolutionary Algorithms", "subject": "evolutionary algorithms"}, {"id": "JAH-ALIFE-000014", "title": "Artificial Ecosystems", "subject": "artificial ecosystems"}, {"id": "JAH-ALIFE-000015", "title": "Swarm Behaviour and Artificial Life", "subject": "swarm behaviour"}, {"id": "JAH-ALIFE-000016", "title": "Artificial Life in Robotics", "subject": "artificial life in robotics"}, {"id": "JAH-ALIFE-000017", "title": "Artificial Life and Complex Systems", "subject": "artificial life and complex systems"}, {"id": "JAH-ALIFE-000018", "title": "Measuring Complexity in Artificial Life", "subject": "measuring complexity"}, {"id": "JAH-ALIFE-000019", "title": "Artificial Life and the Origin of Life", "subject": "artificial life and origin of life"}, {"id": "JAH-ALIFE-000020", "title": "Synthetic Cells as Research Models", "subject": "synthetic cells as research models"}, {"id": "JAH-ALIFE-000021", "title": "Artificial Life Software Platforms", "subject": "artificial life software platforms"}, {"id": "JAH-ALIFE-000022", "title": "Artificial Life and Biosafety", "subject": "artificial life and biosafety"}, {"id": "JAH-ALIFE-000023", "title": "Artificial Life Education and Outreach", "subject": "artificial life education"}, {"id": "JAH-ALIFE-000024", "title": "The Future of Artificial Life Research", "subject": "future of artificial life"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: artificial-life');
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
