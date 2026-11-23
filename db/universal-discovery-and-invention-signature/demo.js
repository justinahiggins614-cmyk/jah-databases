// Demo for the The Signature Universal Discovery and Invention Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UDIS-000001", "title": "Signature Opportunity Scanning: Universal Discovery and Invention", "subject": "Opportunity Scanning"}, {"id": "JAH-UDIS-000002", "title": "Signature Problem Framing: Universal Discovery and Invention", "subject": "Problem Framing"}, {"id": "JAH-UDIS-000003", "title": "Signature Prior-Knowledge Search: Universal Discovery and Invention", "subject": "Prior-Knowledge Search"}, {"id": "JAH-UDIS-000004", "title": "Signature Hypothesis Formation: Universal Discovery and Invention", "subject": "Hypothesis Formation"}, {"id": "JAH-UDIS-000005", "title": "Signature Experiment Design: Universal Discovery and Invention", "subject": "Experiment Design"}, {"id": "JAH-UDIS-000006", "title": "Signature Prototype Invention: Universal Discovery and Invention", "subject": "Prototype Invention"}, {"id": "JAH-UDIS-000007", "title": "Signature Novelty Checking: Universal Discovery and Invention", "subject": "Novelty Checking"}, {"id": "JAH-UDIS-000008", "title": "Signature Feasibility Assessment: Universal Discovery and Invention", "subject": "Feasibility Assessment"}, {"id": "JAH-UDIS-000009", "title": "Signature Invention Records: Universal Discovery and Invention", "subject": "Invention Records"}, {"id": "JAH-UDIS-000010", "title": "Signature Discovery Logs: Universal Discovery and Invention", "subject": "Discovery Logs"}, {"id": "JAH-UDIS-000011", "title": "Signature Cross-Domain Transfer: Universal Discovery and Invention", "subject": "Cross-Domain Transfer"}, {"id": "JAH-UDIS-000012", "title": "Signature Serendipity Capture: Universal Discovery and Invention", "subject": "Serendipity Capture"}, {"id": "JAH-UDIS-000013", "title": "Signature Research Planning: Universal Discovery and Invention", "subject": "Research Planning"}, {"id": "JAH-UDIS-000014", "title": "Signature Evidence Collection: Universal Discovery and Invention", "subject": "Evidence Collection"}, {"id": "JAH-UDIS-000015", "title": "Signature Peer Review Inside the System: Universal Discovery and Invention", "subject": "Peer Review Inside the System"}, {"id": "JAH-UDIS-000016", "title": "Signature Invention Disclosure: Universal Discovery and Invention", "subject": "Invention Disclosure"}, {"id": "JAH-UDIS-000017", "title": "Signature Iteration Cycles: Universal Discovery and Invention", "subject": "Iteration Cycles"}, {"id": "JAH-UDIS-000018", "title": "Signature Failure Records: Universal Discovery and Invention", "subject": "Failure Records"}, {"id": "JAH-UDIS-000019", "title": "Signature Breakthrough Criteria: Universal Discovery and Invention", "subject": "Breakthrough Criteria"}, {"id": "JAH-UDIS-000020", "title": "Signature Technology Readiness: Universal Discovery and Invention", "subject": "Technology Readiness"}, {"id": "JAH-UDIS-000021", "title": "Signature Invention to Construction Handover: Universal Discovery and Invention", "subject": "Invention to Construction Handover"}, {"id": "JAH-UDIS-000022", "title": "Signature Discovery Metrics: Universal Discovery and Invention", "subject": "Discovery Metrics"}, {"id": "JAH-UDIS-000023", "title": "Signature The Inventor's Notebook: Universal Discovery and Invention", "subject": "The Inventor's Notebook"}, {"id": "JAH-UDIS-000024", "title": "Signature Discovery and Invention Lifecycle: Universal Discovery and Invention", "subject": "Discovery and Invention Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-discovery-and-invention-signature');
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
