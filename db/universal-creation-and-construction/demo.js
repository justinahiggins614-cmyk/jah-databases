// Demo for the Universal Creation and Construction Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Roadmap and proposed systems are
// development targets, not achieved claims. JAH live retrieval was NOT
// verified. Demo code runs locally for checking only and is NOT a hardened sandbox.
const RECORDS = [{"id": "JAH-UCAC-000001", "title": "Universal Creation and Construction: Requirements-First System Design", "subject": "Requirements-First System Design"}, {"id": "JAH-UCAC-000002", "title": "Universal Creation and Construction: Scope and Boundary Setting", "subject": "Scope and Boundary Setting"}, {"id": "JAH-UCAC-000003", "title": "Universal Creation and Construction: Component Cataloguing", "subject": "Component Cataloguing"}, {"id": "JAH-UCAC-000004", "title": "Universal Creation and Construction: Interface Contracts", "subject": "Interface Contracts"}, {"id": "JAH-UCAC-000005", "title": "Universal Creation and Construction: Data Model Design", "subject": "Data Model Design"}, {"id": "JAH-UCAC-000006", "title": "Universal Creation and Construction: Build Sequencing", "subject": "Build Sequencing"}, {"id": "JAH-UCAC-000007", "title": "Universal Creation and Construction: Prototype Construction", "subject": "Prototype Construction"}, {"id": "JAH-UCAC-000008", "title": "Universal Creation and Construction: Test Harness Design", "subject": "Test Harness Design"}, {"id": "JAH-UCAC-000009", "title": "Universal Creation and Construction: Verification Checklists", "subject": "Verification Checklists"}, {"id": "JAH-UCAC-000010", "title": "Universal Creation and Construction: Documentation as Deliverable", "subject": "Documentation as Deliverable"}, {"id": "JAH-UCAC-000011", "title": "Universal Creation and Construction: Versioning and Change Control", "subject": "Versioning and Change Control"}, {"id": "JAH-UCAC-000012", "title": "Universal Creation and Construction: Reuse Libraries", "subject": "Reuse Libraries"}, {"id": "JAH-UCAC-000013", "title": "Universal Creation and Construction: Template Systems", "subject": "Template Systems"}, {"id": "JAH-UCAC-000014", "title": "Universal Creation and Construction: Construction Workflows", "subject": "Construction Workflows"}, {"id": "JAH-UCAC-000015", "title": "Universal Creation and Construction: Human Review Gates", "subject": "Human Review Gates"}, {"id": "JAH-UCAC-000016", "title": "Universal Creation and Construction: Rollback Planning", "subject": "Rollback Planning"}, {"id": "JAH-UCAC-000017", "title": "Universal Creation and Construction: Resource Budgeting", "subject": "Resource Budgeting"}, {"id": "JAH-UCAC-000018", "title": "Universal Creation and Construction: Dependency Registration", "subject": "Dependency Registration"}, {"id": "JAH-UCAC-000019", "title": "Universal Creation and Construction: Integration Testing", "subject": "Integration Testing"}, {"id": "JAH-UCAC-000020", "title": "Universal Creation and Construction: Acceptance Criteria", "subject": "Acceptance Criteria"}, {"id": "JAH-UCAC-000021", "title": "Universal Creation and Construction: Deployment Checklists", "subject": "Deployment Checklists"}, {"id": "JAH-UCAC-000022", "title": "Universal Creation and Construction: Maintenance Handover", "subject": "Maintenance Handover"}, {"id": "JAH-UCAC-000023", "title": "Universal Creation and Construction: Improvement Loops", "subject": "Improvement Loops"}, {"id": "JAH-UCAC-000024", "title": "Universal Creation and Construction: Creation Records and Provenance", "subject": "Creation Records and Provenance"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: universal-creation-and-construction');
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
