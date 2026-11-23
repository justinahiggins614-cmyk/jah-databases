// Demo for the Distributed Intelligence Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DISTI-000001", "title": "Distributed Intelligence: Overview and Objective", "subject": "Distributed intelligence overview"}, {"id": "JAH-DISTI-000002", "title": "Distributed Systems Fundamentals: Processes, Messages, and Time", "subject": "Distributed systems fundamentals"}, {"id": "JAH-DISTI-000003", "title": "Consensus: Raft and Paxos for Agreement Across Machines", "subject": "Consensus protocols"}, {"id": "JAH-DISTI-000004", "title": "Distributed Databases and Replication", "subject": "Distributed databases"}, {"id": "JAH-DISTI-000005", "title": "Federated Learning: Training Together Without Sharing Raw Data", "subject": "Federated learning"}, {"id": "JAH-DISTI-000006", "title": "Edge Computing: Intelligence Close to the Data", "subject": "Edge computing"}, {"id": "JAH-DISTI-000007", "title": "Multi-Agent Coordination: Agents That Work Together", "subject": "Multi-agent coordination"}, {"id": "JAH-DISTI-000008", "title": "Publish-Subscribe Messaging for Distributed Systems", "subject": "Publish-subscribe messaging"}, {"id": "JAH-DISTI-000009", "title": "Distributed Ledgers for Civilian Record-Keeping", "subject": "Distributed ledgers"}, {"id": "JAH-DISTI-000010", "title": "Service Meshes: Managing Service-to-Service Communication", "subject": "Service meshes"}, {"id": "JAH-DISTI-000011", "title": "Distributed Storage: Object and Block Stores", "subject": "Distributed storage"}, {"id": "JAH-DISTI-000012", "title": "Stream Processing: Computing on Flowing Data", "subject": "Stream processing"}, {"id": "JAH-DISTI-000013", "title": "Distributed Tracing and Observability", "subject": "Distributed tracing"}, {"id": "JAH-DISTI-000014", "title": "Byzantine Fault Tolerance: Defensive Resilience Against Bad Actors", "subject": "Byzantine fault tolerance"}, {"id": "JAH-DISTI-000015", "title": "Distributed Scheduling: Placing Work Across Many Machines", "subject": "Distributed scheduling"}, {"id": "JAH-DISTI-000016", "title": "Content Delivery Networks: Moving Data Close to Readers", "subject": "Content delivery networks"}, {"id": "JAH-DISTI-000017", "title": "Peer-to-Peer Networks for Civilian Sharing", "subject": "Peer-to-peer networks"}, {"id": "JAH-DISTI-000018", "title": "Distributed AI Inference: Answering Together", "subject": "Distributed AI inference"}, {"id": "JAH-DISTI-000019", "title": "Knowledge Graphs Across Sites", "subject": "Knowledge graphs across sites"}, {"id": "JAH-DISTI-000020", "title": "Distributed Simulation Orchestration", "subject": "Distributed simulation orchestration"}, {"id": "JAH-DISTI-000021", "title": "Privacy-Preserving Aggregation", "subject": "Privacy-preserving aggregation"}, {"id": "JAH-DISTI-000022", "title": "Distributed Testing Harnesses", "subject": "Distributed testing harnesses"}, {"id": "JAH-DISTI-000023", "title": "Reliability Engineering for Distributed Systems", "subject": "Reliability engineering"}, {"id": "JAH-DISTI-000024", "title": "Technology Transition for Distributed Systems", "subject": "Technology transition"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: distributed-intelligence');
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
