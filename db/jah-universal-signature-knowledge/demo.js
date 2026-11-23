// Demo for the JAH Universal Signature Knowledge Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-JUSK-000001", "title": "JAH Universal Signature Knowledge: Signature Identity", "subject": "Signature Identity"}, {"id": "JAH-JUSK-000002", "title": "JAH Universal Signature Knowledge: Canonical Record Rules", "subject": "Canonical Record Rules"}, {"id": "JAH-JUSK-000003", "title": "JAH Universal Signature Knowledge: JAH Architecture Overview", "subject": "JAH Architecture Overview"}, {"id": "JAH-JUSK-000004", "title": "JAH Universal Signature Knowledge: Naming and Identifiers", "subject": "Naming and Identifiers"}, {"id": "JAH-JUSK-000005", "title": "JAH Universal Signature Knowledge: Provenance Rules", "subject": "Provenance Rules"}, {"id": "JAH-JUSK-000006", "title": "JAH Universal Signature Knowledge: Signature Stamps", "subject": "Signature Stamps"}, {"id": "JAH-JUSK-000007", "title": "JAH Universal Signature Knowledge: The Master AI Directive", "subject": "The Master AI Directive"}, {"id": "JAH-JUSK-000008", "title": "JAH Universal Signature Knowledge: Network Navigation", "subject": "Network Navigation"}, {"id": "JAH-JUSK-000009", "title": "JAH Universal Signature Knowledge: Database Standards", "subject": "Database Standards"}, {"id": "JAH-JUSK-000010", "title": "JAH Universal Signature Knowledge: Record Completeness Rules", "subject": "Record Completeness Rules"}, {"id": "JAH-JUSK-000011", "title": "JAH Universal Signature Knowledge: The Teaching Ladder", "subject": "The Teaching Ladder"}, {"id": "JAH-JUSK-000012", "title": "JAH Universal Signature Knowledge: Mirror Rules", "subject": "Mirror Rules"}, {"id": "JAH-JUSK-000013", "title": "JAH Universal Signature Knowledge: Signature Editions", "subject": "Signature Editions"}, {"id": "JAH-JUSK-000014", "title": "JAH Universal Signature Knowledge: Public Editions", "subject": "Public Editions"}, {"id": "JAH-JUSK-000015", "title": "JAH Universal Signature Knowledge: Lineage and Attribution", "subject": "Lineage and Attribution"}, {"id": "JAH-JUSK-000016", "title": "JAH Universal Signature Knowledge: The JCC Code System", "subject": "The JCC Code System"}, {"id": "JAH-JUSK-000017", "title": "JAH Universal Signature Knowledge: March-to-a-Million Markers", "subject": "March-to-a-Million Markers"}, {"id": "JAH-JUSK-000018", "title": "JAH Universal Signature Knowledge: AI Per Database", "subject": "AI Per Database"}, {"id": "JAH-JUSK-000019", "title": "JAH Universal Signature Knowledge: Generator Standards", "subject": "Generator Standards"}, {"id": "JAH-JUSK-000020", "title": "JAH Universal Signature Knowledge: Verification Rules", "subject": "Verification Rules"}, {"id": "JAH-JUSK-000021", "title": "JAH Universal Signature Knowledge: Accessibility Rules", "subject": "Accessibility Rules"}, {"id": "JAH-JUSK-000022", "title": "JAH Universal Signature Knowledge: Free-Forever Rules", "subject": "Free-Forever Rules"}, {"id": "JAH-JUSK-000023", "title": "JAH Universal Signature Knowledge: Governance Records", "subject": "Governance Records"}, {"id": "JAH-JUSK-000024", "title": "JAH Universal Signature Knowledge: The Signature Knowledge Map", "subject": "The Signature Knowledge Map"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: jah-universal-signature-knowledge');
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
