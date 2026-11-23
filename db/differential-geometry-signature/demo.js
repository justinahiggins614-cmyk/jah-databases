// Demo for the The Signature Differential Geometry Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-DGEOS-000001", "title": "Signature Design: A Manifold Explorer", "subject": "manifold explorer design"}, {"id": "JAH-DGEOS-000002", "title": "Signature Design: A Metric Laboratory", "subject": "metric laboratory design"}, {"id": "JAH-DGEOS-000003", "title": "Signature Design: A Curvature Visualiser", "subject": "curvature visualiser design"}, {"id": "JAH-DGEOS-000004", "title": "Signature Design: A Geodesic Tracer", "subject": "geodesic tracer design"}, {"id": "JAH-DGEOS-000005", "title": "Signature Design: A Gauss-Bonnet Checker", "subject": "Gauss-Bonnet checker design"}, {"id": "JAH-DGEOS-000006", "title": "Signature Design: A Connection Laboratory", "subject": "connection laboratory design"}, {"id": "JAH-DGEOS-000007", "title": "Signature Design: A Form Calculator", "subject": "form calculator design"}, {"id": "JAH-DGEOS-000008", "title": "Signature Design: A Stokes Workbench", "subject": "Stokes workbench design"}, {"id": "JAH-DGEOS-000009", "title": "Signature Design: A Ricci-Flow Simulator", "subject": "Ricci-flow simulator design"}, {"id": "JAH-DGEOS-000010", "title": "Signature Design: A Lie Group Explorer", "subject": "Lie group explorer design"}, {"id": "JAH-DGEOS-000011", "title": "Signature Design: A Levi-Civita Workbench", "subject": "Levi-Civita workbench design"}, {"id": "JAH-DGEOS-000012", "title": "Signature Design: A Spectral Laboratory", "subject": "spectral laboratory design"}, {"id": "JAH-DGEOS-000013", "title": "Signature Design: A Minimal-Surface Studio", "subject": "minimal-surface studio design"}, {"id": "JAH-DGEOS-000014", "title": "Signature Design: An Index-Theorem Checker", "subject": "index-theorem checker design"}, {"id": "JAH-DGEOS-000015", "title": "Signature Design: A Symplectic Explorer", "subject": "symplectic explorer design"}, {"id": "JAH-DGEOS-000016", "title": "Signature Design: A Finsler Laboratory", "subject": "Finsler laboratory design"}, {"id": "JAH-DGEOS-000017", "title": "Signature Design: A Theorema Egregium Demonstrator", "subject": "Theorema Egregium demonstrator design"}, {"id": "JAH-DGEOS-000018", "title": "Signature Design: A Bundle Builder", "subject": "bundle builder design"}, {"id": "JAH-DGEOS-000019", "title": "Signature Design: A Hopf-Rinow Explorer", "subject": "Hopf-Rinow explorer design"}, {"id": "JAH-DGEOS-000020", "title": "Signature Design: A Submanifold Studio", "subject": "submanifold studio design"}, {"id": "JAH-DGEOS-000021", "title": "Signature Design: A Relativity Geometry Bench", "subject": "relativity geometry bench design"}, {"id": "JAH-DGEOS-000022", "title": "Signature Design: A Chern Laboratory", "subject": "Chern laboratory design"}, {"id": "JAH-DGEOS-000023", "title": "Signature Design: A Morse Explorer", "subject": "Morse explorer design"}, {"id": "JAH-DGEOS-000024", "title": "Signature Design: A Differential Geometry Teaching Laboratory", "subject": "differential geometry teaching laboratory design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: differential-geometry-signature');
  console.log('EDITION: signature');
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
