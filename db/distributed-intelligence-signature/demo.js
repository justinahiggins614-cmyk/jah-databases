// Demo for the The Signature Distributed Intelligence Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DISTIS-000001", "title": "Signature Distributed Intelligence Overview Design", "subject": "Distributed intelligence overview (Signature design-study)"}, {"id": "JAH-DISTIS-000002", "title": "Signature Distributed Fundamentals Design", "subject": "Distributed systems fundamentals (Signature design-study)"}, {"id": "JAH-DISTIS-000003", "title": "Signature Consensus Lab Design", "subject": "Consensus protocols (Signature design-study)"}, {"id": "JAH-DISTIS-000004", "title": "Signature Distributed Database Design", "subject": "Distributed databases (Signature design-study)"}, {"id": "JAH-DISTIS-000005", "title": "Signature Federated Learning Studio Design", "subject": "Federated learning (Signature design-study)"}, {"id": "JAH-DISTIS-000006", "title": "Signature Edge Node Design", "subject": "Edge computing (Signature design-study)"}, {"id": "JAH-DISTIS-000007", "title": "Signature Agent Council Design", "subject": "Multi-agent coordination (Signature design-study)"}, {"id": "JAH-DISTIS-000008", "title": "Signature Message Bus Design", "subject": "Publish-subscribe messaging (Signature design-study)"}, {"id": "JAH-DISTIS-000009", "title": "Signature Ledger Vault Design", "subject": "Distributed ledgers (Signature design-study)"}, {"id": "JAH-DISTIS-000010", "title": "Signature Mesh Gateway Design", "subject": "Service meshes (Signature design-study)"}, {"id": "JAH-DISTIS-000011", "title": "Signature Object Store Design", "subject": "Distributed storage (Signature design-study)"}, {"id": "JAH-DISTIS-000012", "title": "Signature Stream Engine Design", "subject": "Stream processing (Signature design-study)"}, {"id": "JAH-DISTIS-000013", "title": "Signature Trace Observatory Design", "subject": "Distributed tracing (Signature design-study)"}, {"id": "JAH-DISTIS-000014", "title": "Signature Fault-Tolerance Harness Design", "subject": "Byzantine fault tolerance (Signature design-study)"}, {"id": "JAH-DISTIS-000015", "title": "Signature Distributed Scheduler Design", "subject": "Distributed scheduling (Signature design-study)"}, {"id": "JAH-DISTIS-000016", "title": "Signature Delivery Mesh Design", "subject": "Content delivery networks (Signature design-study)"}, {"id": "JAH-DISTIS-000017", "title": "Signature Peer Registry Design", "subject": "Peer-to-peer networks (Signature design-study)"}, {"id": "JAH-DISTIS-000018", "title": "Signature Inference Grid Design", "subject": "Distributed AI inference (Signature design-study)"}, {"id": "JAH-DISTIS-000019", "title": "Signature Knowledge Graph Bridge Design", "subject": "Knowledge graphs across sites (Signature design-study)"}, {"id": "JAH-DISTIS-000020", "title": "Signature Simulation Conductor Design", "subject": "Distributed simulation orchestration (Signature design-study)"}, {"id": "JAH-DISTIS-000021", "title": "Signature Privacy Aggregator Design", "subject": "Privacy-preserving aggregation (Signature design-study)"}, {"id": "JAH-DISTIS-000022", "title": "Signature Test Swarm Design", "subject": "Distributed testing harnesses (Signature design-study)"}, {"id": "JAH-DISTIS-000023", "title": "Signature Reliability Scoreboard Design", "subject": "Reliability engineering (Signature design-study)"}, {"id": "JAH-DISTIS-000024", "title": "Signature Transition Desk Design", "subject": "Technology transition (Signature design-study)"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: distributed-intelligence-signature');
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
