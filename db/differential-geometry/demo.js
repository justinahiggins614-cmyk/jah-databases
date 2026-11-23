// Demo for the Differential Geometry Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-DGEO-000001", "title": "Differential Geometry: The Field in Outline", "subject": "differential geometry overview"}, {"id": "JAH-DGEO-000002", "title": "Manifolds: Spaces That Look Flat Up Close", "subject": "manifolds"}, {"id": "JAH-DGEO-000003", "title": "Riemannian Manifolds and the Metric", "subject": "Riemannian manifolds"}, {"id": "JAH-DGEO-000004", "title": "Curvature: Gaussian, Sectional, and Ricci", "subject": "curvature"}, {"id": "JAH-DGEO-000005", "title": "Geodesics: The Straightest Possible Paths", "subject": "geodesics"}, {"id": "JAH-DGEO-000006", "title": "The Gauss-Bonnet Theorem: Bending and Topology Together", "subject": "Gauss-Bonnet theorem"}, {"id": "JAH-DGEO-000007", "title": "Connections and Parallel Transport", "subject": "connections and parallel transport"}, {"id": "JAH-DGEO-000008", "title": "Differential Forms and the Exterior Derivative", "subject": "differential forms"}, {"id": "JAH-DGEO-000009", "title": "Stokes' Theorem: The Fundamental Theorem of Calculus on Manifolds", "subject": "Stokes' theorem"}, {"id": "JAH-DGEO-000010", "title": "The Ricci Flow and the Poincare Conjecture", "subject": "Ricci flow"}, {"id": "JAH-DGEO-000011", "title": "Lie Groups and Lie Algebras", "subject": "Lie groups"}, {"id": "JAH-DGEO-000012", "title": "The Levi-Civita Connection", "subject": "Levi-Civita connection"}, {"id": "JAH-DGEO-000013", "title": "The Laplace-Beltrami Operator", "subject": "Laplace-Beltrami operator"}, {"id": "JAH-DGEO-000014", "title": "Minimal Surfaces: Soap Films and Mathematics", "subject": "minimal surfaces"}, {"id": "JAH-DGEO-000015", "title": "The Atiyah-Singer Index Theorem", "subject": "Atiyah-Singer index theorem"}, {"id": "JAH-DGEO-000016", "title": "Symplectic Geometry: The Geometry of Phase Space", "subject": "symplectic geometry"}, {"id": "JAH-DGEO-000017", "title": "Finsler Geometry: Geometry Without a Quadratic Metric", "subject": "Finsler geometry"}, {"id": "JAH-DGEO-000018", "title": "The Theorema Egregium: Gauss's Remarkable Theorem", "subject": "Theorema Egregium"}, {"id": "JAH-DGEO-000019", "title": "Vector Bundles and Fibre Bundles", "subject": "vector bundles and fibre bundles"}, {"id": "JAH-DGEO-000020", "title": "The Hopf-Rinow Theorem: Completeness and Geodesics", "subject": "Hopf-Rinow theorem"}, {"id": "JAH-DGEO-000021", "title": "Submanifolds and the Second Fundamental Form", "subject": "submanifolds"}, {"id": "JAH-DGEO-000022", "title": "Differential Geometry in General Relativity", "subject": "differential geometry in general relativity"}, {"id": "JAH-DGEO-000023", "title": "The Chern-Gauss-Bonnet Theorem", "subject": "Chern-Gauss-Bonnet theorem"}, {"id": "JAH-DGEO-000024", "title": "Morse Theory: The Shape of a Manifold from a Function", "subject": "Morse theory"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: differential-geometry');
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
