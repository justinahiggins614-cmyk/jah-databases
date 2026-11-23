// Demo for the Universal Safety and Verification Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-USV-000001", "title": "Universal Safety and Verification: Safety Requirements", "subject": "Safety Requirements"}, {"id": "JAH-USV-000002", "title": "Universal Safety and Verification: Hazard Identification", "subject": "Hazard Identification"}, {"id": "JAH-USV-000003", "title": "Universal Safety and Verification: Risk Assessment", "subject": "Risk Assessment"}, {"id": "JAH-USV-000004", "title": "Universal Safety and Verification: Verification Plans", "subject": "Verification Plans"}, {"id": "JAH-USV-000005", "title": "Universal Safety and Verification: Test Evidence", "subject": "Test Evidence"}, {"id": "JAH-USV-000006", "title": "Universal Safety and Verification: Independent Checking", "subject": "Independent Checking"}, {"id": "JAH-USV-000007", "title": "Universal Safety and Verification: Failure-Mode Records", "subject": "Failure-Mode Records"}, {"id": "JAH-USV-000008", "title": "Universal Safety and Verification: Safety Cases", "subject": "Safety Cases"}, {"id": "JAH-USV-000009", "title": "Universal Safety and Verification: Rollback and Safe States", "subject": "Rollback and Safe States"}, {"id": "JAH-USV-000010", "title": "Universal Safety and Verification: Access and Authorization", "subject": "Access and Authorization"}, {"id": "JAH-USV-000011", "title": "Universal Safety and Verification: Data Integrity Checks", "subject": "Data Integrity Checks"}, {"id": "JAH-USV-000012", "title": "Universal Safety and Verification: Provenance Verification", "subject": "Provenance Verification"}, {"id": "JAH-USV-000013", "title": "Universal Safety and Verification: Reproducibility Checks", "subject": "Reproducibility Checks"}, {"id": "JAH-USV-000014", "title": "Universal Safety and Verification: Performance Bounds", "subject": "Performance Bounds"}, {"id": "JAH-USV-000015", "title": "Universal Safety and Verification: Security Review", "subject": "Security Review"}, {"id": "JAH-USV-000016", "title": "Universal Safety and Verification: Human Oversight Gates", "subject": "Human Oversight Gates"}, {"id": "JAH-USV-000017", "title": "Universal Safety and Verification: Incident Records", "subject": "Incident Records"}, {"id": "JAH-USV-000018", "title": "Universal Safety and Verification: Corrective Actions", "subject": "Corrective Actions"}, {"id": "JAH-USV-000019", "title": "Universal Safety and Verification: Compliance Mapping", "subject": "Compliance Mapping"}, {"id": "JAH-USV-000020", "title": "Universal Safety and Verification: Verification Reports", "subject": "Verification Reports"}, {"id": "JAH-USV-000021", "title": "Universal Safety and Verification: Safety Maturity", "subject": "Safety Maturity"}, {"id": "JAH-USV-000022", "title": "Universal Safety and Verification: Cross-System Verification", "subject": "Cross-System Verification"}, {"id": "JAH-USV-000023", "title": "Universal Safety and Verification: The Verification Registry", "subject": "The Verification Registry"}, {"id": "JAH-USV-000024", "title": "Universal Safety and Verification: Safety and Verification Lifecycle", "subject": "Safety and Verification Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-safety-and-verification');
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
