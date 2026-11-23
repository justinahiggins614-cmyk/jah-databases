// Demo for the Universal Ecosystem Generator Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UEG-000001", "title": "Universal Ecosystem Generator: Ecosystem Mapping", "subject": "Ecosystem Mapping"}, {"id": "JAH-UEG-000002", "title": "Universal Ecosystem Generator: Resource Families", "subject": "Resource Families"}, {"id": "JAH-UEG-000003", "title": "Universal Ecosystem Generator: Connector Design", "subject": "Connector Design"}, {"id": "JAH-UEG-000004", "title": "Universal Ecosystem Generator: The Dependency Registry", "subject": "The Dependency Registry"}, {"id": "JAH-UEG-000005", "title": "Universal Ecosystem Generator: Ecosystem Bootstrapping", "subject": "Ecosystem Bootstrapping"}, {"id": "JAH-UEG-000006", "title": "Universal Ecosystem Generator: Network Growth Rules", "subject": "Network Growth Rules"}, {"id": "JAH-UEG-000007", "title": "Universal Ecosystem Generator: Cross-Database Links", "subject": "Cross-Database Links"}, {"id": "JAH-UEG-000008", "title": "Universal Ecosystem Generator: Shared AI Services", "subject": "Shared AI Services"}, {"id": "JAH-UEG-000009", "title": "Universal Ecosystem Generator: Ecosystem Health", "subject": "Ecosystem Health"}, {"id": "JAH-UEG-000010", "title": "Universal Ecosystem Generator: Adding a New Family", "subject": "Adding a New Family"}, {"id": "JAH-UEG-000011", "title": "Universal Ecosystem Generator: Retiring a Family", "subject": "Retiring a Family"}, {"id": "JAH-UEG-000012", "title": "Universal Ecosystem Generator: Ecosystem Versioning", "subject": "Ecosystem Versioning"}, {"id": "JAH-UEG-000013", "title": "Universal Ecosystem Generator: Ecosystem Testing", "subject": "Ecosystem Testing"}, {"id": "JAH-UEG-000014", "title": "Universal Ecosystem Generator: Ecosystem Documentation", "subject": "Ecosystem Documentation"}, {"id": "JAH-UEG-000015", "title": "Universal Ecosystem Generator: Ecosystem Governance", "subject": "Ecosystem Governance"}, {"id": "JAH-UEG-000016", "title": "Universal Ecosystem Generator: Ecosystem Metrics", "subject": "Ecosystem Metrics"}, {"id": "JAH-UEG-000017", "title": "Universal Ecosystem Generator: Ecosystem Templates", "subject": "Ecosystem Templates"}, {"id": "JAH-UEG-000018", "title": "Universal Ecosystem Generator: Ecosystem Security", "subject": "Ecosystem Security"}, {"id": "JAH-UEG-000019", "title": "Universal Ecosystem Generator: Ecosystem Accessibility", "subject": "Ecosystem Accessibility"}, {"id": "JAH-UEG-000020", "title": "Universal Ecosystem Generator: Ecosystem Expansion Plans", "subject": "Ecosystem Expansion Plans"}, {"id": "JAH-UEG-000021", "title": "Universal Ecosystem Generator: Ecosystem Failure Recovery", "subject": "Ecosystem Failure Recovery"}, {"id": "JAH-UEG-000022", "title": "Universal Ecosystem Generator: Ecosystem Records", "subject": "Ecosystem Records"}, {"id": "JAH-UEG-000023", "title": "Universal Ecosystem Generator: Ecosystem Maturity", "subject": "Ecosystem Maturity"}, {"id": "JAH-UEG-000024", "title": "Universal Ecosystem Generator: The Ecosystem Lifecycle", "subject": "The Ecosystem Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-ecosystem-generator');
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
