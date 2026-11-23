// Demo for the JAH Boundless Creation Generator Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-JBCG-000001", "title": "JAH Boundless Creation Generator: New Family Proposals", "subject": "New Family Proposals"}, {"id": "JAH-JBCG-000002", "title": "JAH Boundless Creation Generator: Family Feasibility", "subject": "Family Feasibility"}, {"id": "JAH-JBCG-000003", "title": "JAH Boundless Creation Generator: Family Specifications", "subject": "Family Specifications"}, {"id": "JAH-JBCG-000004", "title": "JAH Boundless Creation Generator: Family Databases", "subject": "Family Databases"}, {"id": "JAH-JBCG-000005", "title": "JAH Boundless Creation Generator: Family Websites", "subject": "Family Websites"}, {"id": "JAH-JBCG-000006", "title": "JAH Boundless Creation Generator: Family Generators", "subject": "Family Generators"}, {"id": "JAH-JBCG-000007", "title": "JAH Boundless Creation Generator: Family AIs", "subject": "Family AIs"}, {"id": "JAH-JBCG-000008", "title": "JAH Boundless Creation Generator: Family Integration", "subject": "Family Integration"}, {"id": "JAH-JBCG-000009", "title": "JAH Boundless Creation Generator: Family Testing", "subject": "Family Testing"}, {"id": "JAH-JBCG-000010", "title": "JAH Boundless Creation Generator: Family Launch", "subject": "Family Launch"}, {"id": "JAH-JBCG-000011", "title": "JAH Boundless Creation Generator: Family Growth", "subject": "Family Growth"}, {"id": "JAH-JBCG-000012", "title": "JAH Boundless Creation Generator: Family Records", "subject": "Family Records"}, {"id": "JAH-JBCG-000013", "title": "JAH Boundless Creation Generator: Family Retirement", "subject": "Family Retirement"}, {"id": "JAH-JBCG-000014", "title": "JAH Boundless Creation Generator: Cross-Family Links", "subject": "Cross-Family Links"}, {"id": "JAH-JBCG-000015", "title": "JAH Boundless Creation Generator: Family Templates", "subject": "Family Templates"}, {"id": "JAH-JBCG-000016", "title": "JAH Boundless Creation Generator: Family Governance", "subject": "Family Governance"}, {"id": "JAH-JBCG-000017", "title": "JAH Boundless Creation Generator: Family Metrics", "subject": "Family Metrics"}, {"id": "JAH-JBCG-000018", "title": "JAH Boundless Creation Generator: Family Documentation", "subject": "Family Documentation"}, {"id": "JAH-JBCG-000019", "title": "JAH Boundless Creation Generator: Family Accessibility", "subject": "Family Accessibility"}, {"id": "JAH-JBCG-000020", "title": "JAH Boundless Creation Generator: Family Security", "subject": "Family Security"}, {"id": "JAH-JBCG-000021", "title": "JAH Boundless Creation Generator: Family Expansion Beyond 700", "subject": "Family Expansion Beyond 700"}, {"id": "JAH-JBCG-000022", "title": "JAH Boundless Creation Generator: Boundless Catalog Rules", "subject": "Boundless Catalog Rules"}, {"id": "JAH-JBCG-000023", "title": "JAH Boundless Creation Generator: The Creation Registry", "subject": "The Creation Registry"}, {"id": "JAH-JBCG-000024", "title": "JAH Boundless Creation Generator: The Boundless Creation Lifecycle", "subject": "The Boundless Creation Lifecycle"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: jah-boundless-creation-generator');
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
