// Demo for the Topology Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-TOPR-000001", "title": "Topology: Open Sets and Continuity", "subject": "Open sets and continuity"}, {"id": "JAH-TOPR-000002", "title": "Point-Set Topology: Bases and Subbases", "subject": "Bases and subbases"}, {"id": "JAH-TOPR-000003", "title": "Metric Spaces and Completeness", "subject": "Metric spaces and completeness"}, {"id": "JAH-TOPR-000004", "title": "Compactness and the Heine-Borel Theorem", "subject": "Compactness and Heine-Borel"}, {"id": "JAH-TOPR-000005", "title": "Connectedness and Path Connectedness", "subject": "Connectedness"}, {"id": "JAH-TOPR-000006", "title": "Hausdorff Spaces and Separation Axioms", "subject": "Hausdorff and separation"}, {"id": "JAH-TOPR-000007", "title": "Product and Quotient Topologies", "subject": "Product and quotient topologies"}, {"id": "JAH-TOPR-000008", "title": "The Fundamental Group", "subject": "Fundamental group"}, {"id": "JAH-TOPR-000009", "title": "Homotopy and Homotopy Equivalence", "subject": "Homotopy equivalence"}, {"id": "JAH-TOPR-000010", "title": "Homology Theory", "subject": "Homology theory"}, {"id": "JAH-TOPR-000011", "title": "The Euler Characteristic", "subject": "Euler characteristic"}, {"id": "JAH-TOPR-000012", "title": "Manifolds and Atlases", "subject": "Manifolds and atlases"}, {"id": "JAH-TOPR-000013", "title": "Surfaces and the Classification Theorem", "subject": "Surface classification"}, {"id": "JAH-TOPR-000014", "title": "Knot Theory and the Jones Polynomial", "subject": "Knot theory"}, {"id": "JAH-TOPR-000015", "title": "Covering Spaces", "subject": "Covering spaces"}, {"id": "JAH-TOPR-000016", "title": "The Brouwer Fixed Point Theorem", "subject": "Brouwer fixed point theorem"}, {"id": "JAH-TOPR-000017", "title": "The Jordan Curve Theorem", "subject": "Jordan curve theorem"}, {"id": "JAH-TOPR-000018", "title": "Urysohn's Lemma and Metrization", "subject": "Urysohn lemma and metrization"}, {"id": "JAH-TOPR-000019", "title": "Compactifications: One-Point and Stone-Cech", "subject": "Compactifications"}, {"id": "JAH-TOPR-000020", "title": "The Borsuk-Ulam Theorem", "subject": "Borsuk-Ulam theorem"}, {"id": "JAH-TOPR-000021", "title": "Simplicial Complexes and Triangulation", "subject": "Simplicial complexes"}, {"id": "JAH-TOPR-000022", "title": "Topological Groups and Lie Groups", "subject": "Topological and Lie groups"}, {"id": "JAH-TOPR-000023", "title": "The Seifert-van Kampen Theorem", "subject": "Seifert-van Kampen theorem"}, {"id": "JAH-TOPR-000024", "title": "Open Problems in Topology", "subject": "Open problems in topology"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: topology-research');
  console.log('EDITION: public');
  console.log('RECORDS: '+RECORDS.length);
  const words0=RECORDS[0].title.split(/\s+/).filter(w=>w.length>3);
  const q1=(words0[0]||RECORDS[0].title.split(/\s+/)[0]).toLowerCase();
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
