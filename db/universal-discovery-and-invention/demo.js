// Demo for the Universal Discovery and Invention Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UDI-000001", "title": "Universal Discovery and Invention: Opportunity Scanning", "subject": "Opportunity Scanning"}, {"id": "JAH-UDI-000002", "title": "Universal Discovery and Invention: Problem Framing", "subject": "Problem Framing"}, {"id": "JAH-UDI-000003", "title": "Universal Discovery and Invention: Prior-Knowledge Search", "subject": "Prior-Knowledge Search"}, {"id": "JAH-UDI-000004", "title": "Universal Discovery and Invention: Hypothesis Formation", "subject": "Hypothesis Formation"}, {"id": "JAH-UDI-000005", "title": "Universal Discovery and Invention: Experiment Design", "subject": "Experiment Design"}, {"id": "JAH-UDI-000006", "title": "Universal Discovery and Invention: Prototype Invention", "subject": "Prototype Invention"}, {"id": "JAH-UDI-000007", "title": "Universal Discovery and Invention: Novelty Checking", "subject": "Novelty Checking"}, {"id": "JAH-UDI-000008", "title": "Universal Discovery and Invention: Feasibility Assessment", "subject": "Feasibility Assessment"}, {"id": "JAH-UDI-000009", "title": "Universal Discovery and Invention: Invention Records", "subject": "Invention Records"}, {"id": "JAH-UDI-000010", "title": "Universal Discovery and Invention: Discovery Logs", "subject": "Discovery Logs"}, {"id": "JAH-UDI-000011", "title": "Universal Discovery and Invention: Cross-Domain Transfer", "subject": "Cross-Domain Transfer"}, {"id": "JAH-UDI-000012", "title": "Universal Discovery and Invention: Serendipity Capture", "subject": "Serendipity Capture"}, {"id": "JAH-UDI-000013", "title": "Universal Discovery and Invention: Research Planning", "subject": "Research Planning"}, {"id": "JAH-UDI-000014", "title": "Universal Discovery and Invention: Evidence Collection", "subject": "Evidence Collection"}, {"id": "JAH-UDI-000015", "title": "Universal Discovery and Invention: Peer Review Inside the System", "subject": "Peer Review Inside the System"}, {"id": "JAH-UDI-000016", "title": "Universal Discovery and Invention: Invention Disclosure", "subject": "Invention Disclosure"}, {"id": "JAH-UDI-000017", "title": "Universal Discovery and Invention: Iteration Cycles", "subject": "Iteration Cycles"}, {"id": "JAH-UDI-000018", "title": "Universal Discovery and Invention: Failure Records", "subject": "Failure Records"}, {"id": "JAH-UDI-000019", "title": "Universal Discovery and Invention: Breakthrough Criteria", "subject": "Breakthrough Criteria"}, {"id": "JAH-UDI-000020", "title": "Universal Discovery and Invention: Technology Readiness", "subject": "Technology Readiness"}, {"id": "JAH-UDI-000021", "title": "Universal Discovery and Invention: Invention to Construction Handover", "subject": "Invention to Construction Handover"}, {"id": "JAH-UDI-000022", "title": "Universal Discovery and Invention: Discovery Metrics", "subject": "Discovery Metrics"}, {"id": "JAH-UDI-000023", "title": "Universal Discovery and Invention: The Inventor's Notebook", "subject": "The Inventor's Notebook"}, {"id": "JAH-UDI-000024", "title": "Universal Discovery and Invention: Discovery and Invention Lifecycle", "subject": "Discovery and Invention Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-discovery-and-invention');
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
