// Demo for the The Signature Artificial Life Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-ALIFES-000001", "title": "A Digital Tide-Pool Organism", "subject": "digital tide-pool organism design"}, {"id": "JAH-ALIFES-000002", "title": "A Self-Replicating Garden Program", "subject": "self-replicating garden design"}, {"id": "JAH-ALIFES-000003", "title": "A Tierra-Style Evolution Chamber", "subject": "tierra-style evolution chamber design"}, {"id": "JAH-ALIFES-000004", "title": "An Avida-Style Fitness Landscape", "subject": "avida-style fitness landscape design"}, {"id": "JAH-ALIFES-000005", "title": "A Game-of-Life City Simulator", "subject": "game-of-life city design"}, {"id": "JAH-ALIFES-000006", "title": "A Cellular Automaton Weather World", "subject": "cellular automaton weather design"}, {"id": "JAH-ALIFES-000007", "title": "A Self-Repairing Code Colony", "subject": "self-repairing code colony design"}, {"id": "JAH-ALIFES-000008", "title": "An Artificial Chemistry Kitchen", "subject": "artificial chemistry kitchen design"}, {"id": "JAH-ALIFES-000009", "title": "A Protocell Design Bench", "subject": "protocell design bench"}, {"id": "JAH-ALIFES-000010", "title": "A Xenobot-Style Living Machine Study", "subject": "xenobot-style living machine design"}, {"id": "JAH-ALIFES-000011", "title": "A Minimal Genome Drafting Board", "subject": "minimal genome drafting board design"}, {"id": "JAH-ALIFES-000012", "title": "An Open-Ended Evolution Observatory", "subject": "open-ended evolution observatory design"}, {"id": "JAH-ALIFES-000013", "title": "An Evolutionary Algorithm Workshop", "subject": "evolutionary algorithm workshop design"}, {"id": "JAH-ALIFES-000014", "title": "A Digital Reef Ecosystem", "subject": "digital reef ecosystem design"}, {"id": "JAH-ALIFES-000015", "title": "A Swarm Choreography Studio", "subject": "swarm choreography studio design"}, {"id": "JAH-ALIFES-000016", "title": "A Life-Like Robot Behaviour Kit", "subject": "life-like robot behaviour kit design"}, {"id": "JAH-ALIFES-000017", "title": "A Complex Systems Sand Table", "subject": "complex systems sand table design"}, {"id": "JAH-ALIFES-000018", "title": "A Complexity Measuring Instrument", "subject": "complexity measuring instrument design"}, {"id": "JAH-ALIFES-000019", "title": "An Origin-of-Life Test Tube Study", "subject": "origin-of-life test tube design"}, {"id": "JAH-ALIFES-000020", "title": "A Synthetic Cell Modelling Desk", "subject": "synthetic cell modelling desk design"}, {"id": "JAH-ALIFES-000021", "title": "An Artificial Life Software Library", "subject": "artificial life software library design"}, {"id": "JAH-ALIFES-000022", "title": "A Biosafety Screening Workbench", "subject": "biosafety screening workbench design"}, {"id": "JAH-ALIFES-000023", "title": "An Artificial Life Teaching Garden", "subject": "artificial life teaching garden design"}, {"id": "JAH-ALIFES-000024", "title": "A Future Artificial Life Research Station", "subject": "future artificial life research station design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: artificial-life-signature');
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
