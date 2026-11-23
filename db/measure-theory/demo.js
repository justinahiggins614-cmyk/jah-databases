// Demo for the Measure Theory Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-MTHY-000001", "title": "Measure Theory: Sigma-Algebras", "subject": "Sigma-algebras"}, {"id": "JAH-MTHY-000002", "title": "Lebesgue Measure on the Real Line", "subject": "Lebesgue measure"}, {"id": "JAH-MTHY-000003", "title": "Lebesgue Integration", "subject": "Lebesgue integration"}, {"id": "JAH-MTHY-000004", "title": "Measurable Functions", "subject": "Measurable functions"}, {"id": "JAH-MTHY-000005", "title": "The Monotone Convergence Theorem", "subject": "Monotone convergence theorem"}, {"id": "JAH-MTHY-000006", "title": "Fatou's Lemma", "subject": "Fatou's lemma"}, {"id": "JAH-MTHY-000007", "title": "Dominated Convergence Theorem", "subject": "Dominated convergence theorem"}, {"id": "JAH-MTHY-000008", "title": "Product Measures and Fubini's Theorem", "subject": "Product measures and Fubini"}, {"id": "JAH-MTHY-000009", "title": "Probability Measures and Probability Spaces", "subject": "Probability measures"}, {"id": "JAH-MTHY-000010", "title": "Borel Measures and Regularity", "subject": "Borel measures and regularity"}, {"id": "JAH-MTHY-000011", "title": "Radon Measures", "subject": "Radon measures"}, {"id": "JAH-MTHY-000012", "title": "The Radon-Nikodym Theorem", "subject": "Radon-Nikodym theorem"}, {"id": "JAH-MTHY-000013", "title": "Signed Measures and Hahn Decomposition", "subject": "Signed measures"}, {"id": "JAH-MTHY-000014", "title": "The Caratheodory Extension Theorem", "subject": "Caratheodory extension theorem"}, {"id": "JAH-MTHY-000015", "title": "Outer Measures", "subject": "Outer measures"}, {"id": "JAH-MTHY-000016", "title": "The Lebesgue Differentiation Theorem", "subject": "Lebesgue differentiation theorem"}, {"id": "JAH-MTHY-000017", "title": "Lp Spaces", "subject": "Lp spaces"}, {"id": "JAH-MTHY-000018", "title": "The Riesz Representation Theorem for Measures", "subject": "Riesz representation"}, {"id": "JAH-MTHY-000019", "title": "Ergodic Theory and Invariant Measures", "subject": "Ergodic theory"}, {"id": "JAH-MTHY-000020", "title": "Hausdorff Measure and Fractal Dimension", "subject": "Hausdorff measure"}, {"id": "JAH-MTHY-000021", "title": "The Change of Variables Formula", "subject": "Change of variables"}, {"id": "JAH-MTHY-000022", "title": "Conditional Expectation", "subject": "Conditional expectation"}, {"id": "JAH-MTHY-000023", "title": "The Martingale Convergence Theorem", "subject": "Martingale convergence"}, {"id": "JAH-MTHY-000024", "title": "Open Problems in Measure Theory", "subject": "Open problems in measure theory"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: measure-theory');
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
