// Demo for the Algebraic Geometry Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-AGEO-000001", "title": "Algebraic Geometry: The Field in Outline", "subject": "algebraic geometry overview"}, {"id": "JAH-AGEO-000002", "title": "Algebraic Curves and the Genus", "subject": "algebraic curves and genus"}, {"id": "JAH-AGEO-000003", "title": "Elliptic Curves and the Mordell-Weil Theorem", "subject": "elliptic curves"}, {"id": "JAH-AGEO-000004", "title": "Algebraic Varieties: Shapes Defined by Equations", "subject": "algebraic varieties"}, {"id": "JAH-AGEO-000005", "title": "Schemes: Grothendieck's Rebuilding of Geometry", "subject": "schemes"}, {"id": "JAH-AGEO-000006", "title": "Sheaves and Cohomology: Local Data, Global Shape", "subject": "sheaves and cohomology"}, {"id": "JAH-AGEO-000007", "title": "The Weil Conjectures in Algebraic Geometry", "subject": "Weil conjectures"}, {"id": "JAH-AGEO-000008", "title": "Moduli Spaces: Spaces Whose Points Are Shapes", "subject": "moduli spaces"}, {"id": "JAH-AGEO-000009", "title": "Intersection Theory and Bezout's Theorem", "subject": "intersection theory"}, {"id": "JAH-AGEO-000010", "title": "Algebraic Surfaces and the Enriques-Kodaira Classification", "subject": "algebraic surfaces"}, {"id": "JAH-AGEO-000011", "title": "The Riemann-Roch Theorem: Counting Functions on a Curve", "subject": "Riemann-Roch theorem"}, {"id": "JAH-AGEO-000012", "title": "Birational Geometry and the Minimal Model Program", "subject": "minimal model program"}, {"id": "JAH-AGEO-000013", "title": "Abelian Varieties: Higher-Dimensional Elliptic Curves", "subject": "abelian varieties"}, {"id": "JAH-AGEO-000014", "title": "Algebraic Groups: Symmetry Described by Equations", "subject": "algebraic groups"}, {"id": "JAH-AGEO-000015", "title": "Toric Varieties: Geometry You Can Draw", "subject": "toric varieties"}, {"id": "JAH-AGEO-000016", "title": "Etale Cohomology and the Etale Fundamental Group", "subject": "etale cohomology"}, {"id": "JAH-AGEO-000017", "title": "Hodge Theory: The Shape of Cohomology", "subject": "Hodge theory"}, {"id": "JAH-AGEO-000018", "title": "Mirror Symmetry: Two Geometries, One Physics", "subject": "mirror symmetry"}, {"id": "JAH-AGEO-000019", "title": "Arithmetic Geometry and Diophantine Equations", "subject": "arithmetic geometry"}, {"id": "JAH-AGEO-000020", "title": "The Resolution of Singularities: Hironaka's Theorem", "subject": "resolution of singularities"}, {"id": "JAH-AGEO-000021", "title": "Algebraic Geometry Codes: Curves That Correct Errors", "subject": "algebraic geometry codes"}, {"id": "JAH-AGEO-000022", "title": "Computational Algebraic Geometry and Grobner Bases", "subject": "computational algebraic geometry"}, {"id": "JAH-AGEO-000023", "title": "The Jacobian Variety and the Abel-Jacobi Map", "subject": "Jacobian variety"}, {"id": "JAH-AGEO-000024", "title": "Grothendieck's Topos and the Etale Topology", "subject": "topos and etale topology"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: algebraic-geometry');
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
