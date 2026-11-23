// Demo for the The Signature Universal Safety and Verification Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-USVS-000001", "title": "Signature Safety Requirements: Universal Safety and Verification", "subject": "Safety Requirements"}, {"id": "JAH-USVS-000002", "title": "Signature Hazard Identification: Universal Safety and Verification", "subject": "Hazard Identification"}, {"id": "JAH-USVS-000003", "title": "Signature Risk Assessment: Universal Safety and Verification", "subject": "Risk Assessment"}, {"id": "JAH-USVS-000004", "title": "Signature Verification Plans: Universal Safety and Verification", "subject": "Verification Plans"}, {"id": "JAH-USVS-000005", "title": "Signature Test Evidence: Universal Safety and Verification", "subject": "Test Evidence"}, {"id": "JAH-USVS-000006", "title": "Signature Independent Checking: Universal Safety and Verification", "subject": "Independent Checking"}, {"id": "JAH-USVS-000007", "title": "Signature Failure-Mode Records: Universal Safety and Verification", "subject": "Failure-Mode Records"}, {"id": "JAH-USVS-000008", "title": "Signature Safety Cases: Universal Safety and Verification", "subject": "Safety Cases"}, {"id": "JAH-USVS-000009", "title": "Signature Rollback and Safe States: Universal Safety and Verification", "subject": "Rollback and Safe States"}, {"id": "JAH-USVS-000010", "title": "Signature Access and Authorization: Universal Safety and Verification", "subject": "Access and Authorization"}, {"id": "JAH-USVS-000011", "title": "Signature Data Integrity Checks: Universal Safety and Verification", "subject": "Data Integrity Checks"}, {"id": "JAH-USVS-000012", "title": "Signature Provenance Verification: Universal Safety and Verification", "subject": "Provenance Verification"}, {"id": "JAH-USVS-000013", "title": "Signature Reproducibility Checks: Universal Safety and Verification", "subject": "Reproducibility Checks"}, {"id": "JAH-USVS-000014", "title": "Signature Performance Bounds: Universal Safety and Verification", "subject": "Performance Bounds"}, {"id": "JAH-USVS-000015", "title": "Signature Security Review: Universal Safety and Verification", "subject": "Security Review"}, {"id": "JAH-USVS-000016", "title": "Signature Human Oversight Gates: Universal Safety and Verification", "subject": "Human Oversight Gates"}, {"id": "JAH-USVS-000017", "title": "Signature Incident Records: Universal Safety and Verification", "subject": "Incident Records"}, {"id": "JAH-USVS-000018", "title": "Signature Corrective Actions: Universal Safety and Verification", "subject": "Corrective Actions"}, {"id": "JAH-USVS-000019", "title": "Signature Compliance Mapping: Universal Safety and Verification", "subject": "Compliance Mapping"}, {"id": "JAH-USVS-000020", "title": "Signature Verification Reports: Universal Safety and Verification", "subject": "Verification Reports"}, {"id": "JAH-USVS-000021", "title": "Signature Safety Maturity: Universal Safety and Verification", "subject": "Safety Maturity"}, {"id": "JAH-USVS-000022", "title": "Signature Cross-System Verification: Universal Safety and Verification", "subject": "Cross-System Verification"}, {"id": "JAH-USVS-000023", "title": "Signature The Verification Registry: Universal Safety and Verification", "subject": "The Verification Registry"}, {"id": "JAH-USVS-000024", "title": "Signature Safety and Verification Lifecycle: Universal Safety and Verification", "subject": "Safety and Verification Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-safety-and-verification-signature');
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
