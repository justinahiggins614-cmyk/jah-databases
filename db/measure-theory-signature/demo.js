// Demo for the The Signature Measure Theory Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-MTHYS-000001", "title": "Signature Measure Workbench: Sigma-Algebra Builder", "subject": "Signature sigma-algebra builder"}, {"id": "JAH-MTHYS-000002", "title": "Signature Lebesgue Measure Ruler", "subject": "Signature Lebesgue ruler"}, {"id": "JAH-MTHYS-000003", "title": "Signature Integral Slicer: Lebesgue Integration Lab", "subject": "Signature Lebesgue lab"}, {"id": "JAH-MTHYS-000004", "title": "Signature Measurability Tester", "subject": "Signature measurability tester"}, {"id": "JAH-MTHYS-000005", "title": "Signature Convergence Theater: Monotone, Fatou, Dominated", "subject": "Signature convergence theater"}, {"id": "JAH-MTHYS-000006", "title": "Signature Product Measure Builder", "subject": "Signature product measure builder"}, {"id": "JAH-MTHYS-000007", "title": "Signature Probability Space Studio", "subject": "Signature probability studio"}, {"id": "JAH-MTHYS-000008", "title": "Signature Borel Approximator", "subject": "Signature Borel approximator"}, {"id": "JAH-MTHYS-000009", "title": "Signature Radon Measure Finder", "subject": "Signature Radon finder"}, {"id": "JAH-MTHYS-000010", "title": "Signature Density Finder: Radon-Nikodym Lab", "subject": "Signature density lab"}, {"id": "JAH-MTHYS-000011", "title": "Signature Signed Measure Splitter", "subject": "Signature signed measure splitter"}, {"id": "JAH-MTHYS-000012", "title": "Signature Extension Machine: Caratheodory Builder", "subject": "Signature extension machine"}, {"id": "JAH-MTHYS-000013", "title": "Signature Outer Measure Coverer", "subject": "Signature outer measure coverer"}, {"id": "JAH-MTHYS-000014", "title": "Signature Differentiation Microscope", "subject": "Signature differentiation microscope"}, {"id": "JAH-MTHYS-000015", "title": "Signature Lp Norm Meter", "subject": "Signature Lp meter"}, {"id": "JAH-MTHYS-000016", "title": "Signature Functional-to-Measure Translator", "subject": "Signature functional translator"}, {"id": "JAH-MTHYS-000017", "title": "Signature Ergodic Time-Averager", "subject": "Signature ergodic averager"}, {"id": "JAH-MTHYS-000018", "title": "Signature Fractal Dimension Gauge", "subject": "Signature fractal gauge"}, {"id": "JAH-MTHYS-000019", "title": "Signature Coordinate Changer", "subject": "Signature coordinate changer"}, {"id": "JAH-MTHYS-000020", "title": "Signature Prediction Machine: Conditional Expectation", "subject": "Signature prediction machine"}, {"id": "JAH-MTHYS-000021", "title": "Signature Martingale Tracker", "subject": "Signature martingale tracker"}, {"id": "JAH-MTHYS-000022", "title": "Signature Open Problem Board: Measure Theory", "subject": "Signature measure problem board"}, {"id": "JAH-MTHYS-000023", "title": "Signature Measure Sorter", "subject": "Signature measure sorter"}, {"id": "JAH-MTHYS-000024", "title": "Signature Weak Convergence Viewer", "subject": "Signature weak convergence viewer"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: measure-theory-signature');
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
