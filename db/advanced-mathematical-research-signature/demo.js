// Demo for the The Signature Advanced Mathematical Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-AMRS-000001", "title": "Signature Design: A Proof-Checking Workbench", "subject": "proof-checking workbench design"}, {"id": "JAH-AMRS-000002", "title": "Signature Design: A Conjecture Tracker", "subject": "conjecture tracker design"}, {"id": "JAH-AMRS-000003", "title": "Signature Design: A Literature Synthesis Engine", "subject": "literature synthesis engine design"}, {"id": "JAH-AMRS-000004", "title": "Signature Design: A Peer-Review Simulator", "subject": "peer-review simulator design"}, {"id": "JAH-AMRS-000005", "title": "Signature Design: A Hypothesis Generator", "subject": "hypothesis generator design"}, {"id": "JAH-AMRS-000006", "title": "Signature Design: An Experimental Design Bench", "subject": "experimental design bench"}, {"id": "JAH-AMRS-000007", "title": "Signature Design: A Computational Research Bench", "subject": "computational research bench design"}, {"id": "JAH-AMRS-000008", "title": "Signature Design: A Reproducibility Checker", "subject": "reproducibility checker design"}, {"id": "JAH-AMRS-000009", "title": "Signature Design: A Theorem Dependency Graph", "subject": "theorem dependency graph design"}, {"id": "JAH-AMRS-000010", "title": "Signature Design: A Counterexample Searcher", "subject": "counterexample searcher design"}, {"id": "JAH-AMRS-000011", "title": "Signature Design: A Research Expansion Mapper", "subject": "research expansion mapper design"}, {"id": "JAH-AMRS-000012", "title": "Signature Design: A Collaboration Hub for Distributed Proofs", "subject": "collaboration hub design"}, {"id": "JAH-AMRS-000013", "title": "Signature Design: A Citation Graph Analyser", "subject": "citation graph analyser design"}, {"id": "JAH-AMRS-000014", "title": "Signature Design: An Open-Problem Dashboard", "subject": "open-problem dashboard design"}, {"id": "JAH-AMRS-000015", "title": "Signature Design: A Research Notebook with Evidence", "subject": "research notebook design"}, {"id": "JAH-AMRS-000016", "title": "Signature Design: A Verification Pipeline", "subject": "verification pipeline design"}, {"id": "JAH-AMRS-000017", "title": "Signature Design: A Mathematical Reasoning Tutor", "subject": "mathematical reasoning tutor design"}, {"id": "JAH-AMRS-000018", "title": "Signature Design: A Data Curation Tool for Mathematical Records", "subject": "data curation tool design"}, {"id": "JAH-AMRS-000019", "title": "Signature Design: An arXiv Monitor for New Results", "subject": "arxiv monitor design"}, {"id": "JAH-AMRS-000020", "title": "Signature Design: A Conference Proceedings Indexer", "subject": "conference proceedings indexer design"}, {"id": "JAH-AMRS-000021", "title": "Signature Design: A Referee Assignment Aid", "subject": "referee assignment aid design"}, {"id": "JAH-AMRS-000022", "title": "Signature Design: A Result Replication Laboratory", "subject": "result replication laboratory design"}, {"id": "JAH-AMRS-000023", "title": "Signature Design: A Research Ethics Checker", "subject": "research ethics checker design"}, {"id": "JAH-AMRS-000024", "title": "Signature Design: A Theorem Announcement Tracker", "subject": "theorem announcement tracker design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-mathematical-research-signature');
  console.log('EDITION: signature');
  console.log('RECORDS: '+RECORDS.length);
  const words0=RECORDS[0].title.split(/\s+/).filter(w=>w.length>3);
  const q1=(words0[0]||RECORDS[0].title.split(/\s+/)[0]).toLowerCase();
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
