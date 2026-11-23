// Demo for the The Signature Algebraic Geometry Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-AGEOS-000001", "title": "Signature Design: A Variety Explorer", "subject": "variety explorer design"}, {"id": "JAH-AGEOS-000002", "title": "Signature Design: A Curve Plotter for Algebraic Curves", "subject": "curve plotter design"}, {"id": "JAH-AGEOS-000003", "title": "Signature Design: A Scheme Visualiser", "subject": "scheme visualiser design"}, {"id": "JAH-AGEOS-000004", "title": "Signature Design: A Sheaf Laboratory", "subject": "sheaf laboratory design"}, {"id": "JAH-AGEOS-000005", "title": "Signature Design: A Cohomology Calculator", "subject": "cohomology calculator design"}, {"id": "JAH-AGEOS-000006", "title": "Signature Design: A Moduli Navigator", "subject": "moduli navigator design"}, {"id": "JAH-AGEOS-000007", "title": "Signature Design: An Intersection Workbench", "subject": "intersection workbench design"}, {"id": "JAH-AGEOS-000008", "title": "Signature Design: A Surface Classifier", "subject": "surface classifier design"}, {"id": "JAH-AGEOS-000009", "title": "Signature Design: A Riemann-Roch Checker", "subject": "Riemann-Roch checker design"}, {"id": "JAH-AGEOS-000010", "title": "Signature Design: A Minimal-Model Simulator", "subject": "minimal-model simulator design"}, {"id": "JAH-AGEOS-000011", "title": "Signature Design: An Abelian Variety Studio", "subject": "abelian variety studio design"}, {"id": "JAH-AGEOS-000012", "title": "Signature Design: An Algebraic Group Explorer", "subject": "algebraic group explorer design"}, {"id": "JAH-AGEOS-000013", "title": "Signature Design: A Toric Builder", "subject": "toric builder design"}, {"id": "JAH-AGEOS-000014", "title": "Signature Design: An Etale Explorer", "subject": "etale explorer design"}, {"id": "JAH-AGEOS-000015", "title": "Signature Design: A Hodge Laboratory", "subject": "Hodge laboratory design"}, {"id": "JAH-AGEOS-000016", "title": "Signature Design: A Mirror-Symmetry Mapper", "subject": "mirror-symmetry mapper design"}, {"id": "JAH-AGEOS-000017", "title": "Signature Design: A Diophantine Solver Bench", "subject": "Diophantine solver bench design"}, {"id": "JAH-AGEOS-000018", "title": "Signature Design: A Topos Studio", "subject": "topos studio design"}, {"id": "JAH-AGEOS-000019", "title": "Signature Design: A Singularity Resolver", "subject": "singularity resolver design"}, {"id": "JAH-AGEOS-000020", "title": "Signature Design: An Algebraic Geometry Code Builder", "subject": "algebraic geometry code builder design"}, {"id": "JAH-AGEOS-000021", "title": "Signature Design: A Grobner Engine", "subject": "Grobner engine design"}, {"id": "JAH-AGEOS-000022", "title": "Signature Design: A Jacobian Mapper", "subject": "Jacobian mapper design"}, {"id": "JAH-AGEOS-000023", "title": "Signature Design: A Design-Study Theorem Prover for Algebraic Geometry", "subject": "design-study theorem prover design"}, {"id": "JAH-AGEOS-000024", "title": "Signature Design: An Algebraic Geometry Teaching Laboratory", "subject": "algebraic geometry teaching laboratory design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: algebraic-geometry-signature');
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
