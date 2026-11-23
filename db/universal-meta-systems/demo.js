// Demo for the Universal Meta-Systems Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UMSY-000001", "title": "Universal Meta-Systems: Meta-System Coordination", "subject": "Meta-System Coordination"}, {"id": "JAH-UMSY-000002", "title": "Universal Meta-Systems: Registry of Systems", "subject": "Registry of Systems"}, {"id": "JAH-UMSY-000003", "title": "Universal Meta-Systems: Capability Discovery", "subject": "Capability Discovery"}, {"id": "JAH-UMSY-000004", "title": "Universal Meta-Systems: Task Decomposition", "subject": "Task Decomposition"}, {"id": "JAH-UMSY-000005", "title": "Universal Meta-Systems: Dependency Graphs", "subject": "Dependency Graphs"}, {"id": "JAH-UMSY-000006", "title": "Universal Meta-Systems: Scheduling Across Systems", "subject": "Scheduling Across Systems"}, {"id": "JAH-UMSY-000007", "title": "Universal Meta-Systems: Shared Memory and Provenance", "subject": "Shared Memory and Provenance"}, {"id": "JAH-UMSY-000008", "title": "Universal Meta-Systems: Conflict Resolution", "subject": "Conflict Resolution"}, {"id": "JAH-UMSY-000009", "title": "Universal Meta-Systems: Health Monitoring", "subject": "Health Monitoring"}, {"id": "JAH-UMSY-000010", "title": "Universal Meta-Systems: Failover Between Systems", "subject": "Failover Between Systems"}, {"id": "JAH-UMSY-000011", "title": "Universal Meta-Systems: Capability Negotiation", "subject": "Capability Negotiation"}, {"id": "JAH-UMSY-000012", "title": "Universal Meta-Systems: Message Passing", "subject": "Message Passing"}, {"id": "JAH-UMSY-000013", "title": "Universal Meta-Systems: Shared Vocabularies", "subject": "Shared Vocabularies"}, {"id": "JAH-UMSY-000014", "title": "Universal Meta-Systems: Version Alignment", "subject": "Version Alignment"}, {"id": "JAH-UMSY-000015", "title": "Universal Meta-Systems: Audit Trails", "subject": "Audit Trails"}, {"id": "JAH-UMSY-000016", "title": "Universal Meta-Systems: Access Control Across Systems", "subject": "Access Control Across Systems"}, {"id": "JAH-UMSY-000017", "title": "Universal Meta-Systems: Resource Quotas", "subject": "Resource Quotas"}, {"id": "JAH-UMSY-000018", "title": "Universal Meta-Systems: System Lifecycle Management", "subject": "System Lifecycle Management"}, {"id": "JAH-UMSY-000019", "title": "Universal Meta-Systems: Cross-System Testing", "subject": "Cross-System Testing"}, {"id": "JAH-UMSY-000020", "title": "Universal Meta-Systems: Rollout Coordination", "subject": "Rollout Coordination"}, {"id": "JAH-UMSY-000021", "title": "Universal Meta-Systems: Retirement of Systems", "subject": "Retirement of Systems"}, {"id": "JAH-UMSY-000022", "title": "Universal Meta-Systems: Meta-System Governance", "subject": "Meta-System Governance"}, {"id": "JAH-UMSY-000023", "title": "Universal Meta-Systems: Learning Across Systems", "subject": "Learning Across Systems"}, {"id": "JAH-UMSY-000024", "title": "Universal Meta-Systems: Meta-System Records", "subject": "Meta-System Records"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-meta-systems');
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
