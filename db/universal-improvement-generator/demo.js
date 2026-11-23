// Demo for the Universal Improvement Generator Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UIG-000001", "title": "Universal Improvement Generator: Improvement Proposals", "subject": "Improvement Proposals"}, {"id": "JAH-UIG-000002", "title": "Universal Improvement Generator: Baseline Measurement", "subject": "Baseline Measurement"}, {"id": "JAH-UIG-000003", "title": "Universal Improvement Generator: Change Design", "subject": "Change Design"}, {"id": "JAH-UIG-000004", "title": "Universal Improvement Generator: Controlled Trials", "subject": "Controlled Trials"}, {"id": "JAH-UIG-000005", "title": "Universal Improvement Generator: Comparison Against Baseline", "subject": "Comparison Against Baseline"}, {"id": "JAH-UIG-000006", "title": "Universal Improvement Generator: Rollback Plans", "subject": "Rollback Plans"}, {"id": "JAH-UIG-000007", "title": "Universal Improvement Generator: Improvement Records", "subject": "Improvement Records"}, {"id": "JAH-UIG-000008", "title": "Universal Improvement Generator: Regression Checks", "subject": "Regression Checks"}, {"id": "JAH-UIG-000009", "title": "Universal Improvement Generator: Performance Tracking", "subject": "Performance Tracking"}, {"id": "JAH-UIG-000010", "title": "Universal Improvement Generator: Cost-Benefit Review", "subject": "Cost-Benefit Review"}, {"id": "JAH-UIG-000011", "title": "Universal Improvement Generator: Stakeholder Review", "subject": "Stakeholder Review"}, {"id": "JAH-UIG-000012", "title": "Universal Improvement Generator: Gradual Rollout", "subject": "Gradual Rollout"}, {"id": "JAH-UIG-000013", "title": "Universal Improvement Generator: The Improvement Backlog", "subject": "The Improvement Backlog"}, {"id": "JAH-UIG-000014", "title": "Universal Improvement Generator: Root-Cause Analysis", "subject": "Root-Cause Analysis"}, {"id": "JAH-UIG-000015", "title": "Universal Improvement Generator: Small-Step Changes", "subject": "Small-Step Changes"}, {"id": "JAH-UIG-000016", "title": "Universal Improvement Generator: Measurement Discipline", "subject": "Measurement Discipline"}, {"id": "JAH-UIG-000017", "title": "Universal Improvement Generator: Improvement Metrics", "subject": "Improvement Metrics"}, {"id": "JAH-UIG-000018", "title": "Universal Improvement Generator: Knowledge Capture", "subject": "Knowledge Capture"}, {"id": "JAH-UIG-000019", "title": "Universal Improvement Generator: Improvement Governance", "subject": "Improvement Governance"}, {"id": "JAH-UIG-000020", "title": "Universal Improvement Generator: Automation of Improvement", "subject": "Automation of Improvement"}, {"id": "JAH-UIG-000021", "title": "Universal Improvement Generator: Cross-System Improvement", "subject": "Cross-System Improvement"}, {"id": "JAH-UIG-000022", "title": "Universal Improvement Generator: Improvement Maturity", "subject": "Improvement Maturity"}, {"id": "JAH-UIG-000023", "title": "Universal Improvement Generator: The Improvement Registry", "subject": "The Improvement Registry"}, {"id": "JAH-UIG-000024", "title": "Universal Improvement Generator: The Improvement Lifecycle", "subject": "The Improvement Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-improvement-generator');
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
