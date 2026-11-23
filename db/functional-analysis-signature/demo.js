// Demo for the The Signature Functional Analysis Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-FUNAS-000001", "title": "Signature Norm Meter", "subject": "Signature norm meter"}, {"id": "JAH-FUNAS-000002", "title": "Signature Completeness Checker", "subject": "Signature completeness checker"}, {"id": "JAH-FUNAS-000003", "title": "Signature Hilbert Geometry Lab", "subject": "Signature Hilbert lab"}, {"id": "JAH-FUNAS-000004", "title": "Signature Riesz Vector Finder", "subject": "Signature Riesz finder"}, {"id": "JAH-FUNAS-000005", "title": "Signature Operator Norm Gauge", "subject": "Signature operator gauge"}, {"id": "JAH-FUNAS-000006", "title": "Signature Uniform Boundedness Demonstrator", "subject": "Signature uniform boundedness demo"}, {"id": "JAH-FUNAS-000007", "title": "Signature Open Map Checker", "subject": "Signature open map checker"}, {"id": "JAH-FUNAS-000008", "title": "Signature Graph Closer", "subject": "Signature graph closer"}, {"id": "JAH-FUNAS-000009", "title": "Signature Extension Engine: Hahn-Banach", "subject": "Signature extension engine"}, {"id": "JAH-FUNAS-000010", "title": "Signature Weak Topology Viewer", "subject": "Signature weak topology viewer"}, {"id": "JAH-FUNAS-000011", "title": "Signature Compact Operator Approximator", "subject": "Signature compact approximator"}, {"id": "JAH-FUNAS-000012", "title": "Signature Spectrum Viewer", "subject": "Signature spectrum viewer"}, {"id": "JAH-FUNAS-000013", "title": "Signature Equation Solver: Fredholm Lab", "subject": "Signature Fredholm lab"}, {"id": "JAH-FUNAS-000014", "title": "Signature Distribution Differentiator", "subject": "Signature distribution differentiator"}, {"id": "JAH-FUNAS-000015", "title": "Signature Fourier Analyzer", "subject": "Signature Fourier analyzer"}, {"id": "JAH-FUNAS-000016", "title": "Signature Sobolev Space Builder", "subject": "Signature Sobolev builder"}, {"id": "JAH-FUNAS-000017", "title": "Signature Variational Solver: Lax-Milgram", "subject": "Signature variational solver"}, {"id": "JAH-FUNAS-000018", "title": "Signature Domain Manager: Unbounded Operators", "subject": "Signature domain manager"}, {"id": "JAH-FUNAS-000019", "title": "Signature Evolution Engine: Semigroup Solver", "subject": "Signature evolution engine"}, {"id": "JAH-FUNAS-000020", "title": "Signature Extreme Point Finder", "subject": "Signature extreme point finder"}, {"id": "JAH-FUNAS-000021", "title": "Signature Iteration Engine: Fixed Points", "subject": "Signature iteration engine"}, {"id": "JAH-FUNAS-000022", "title": "Signature Algebra-to-Function Translator", "subject": "Signature algebra translator"}, {"id": "JAH-FUNAS-000023", "title": "Signature Approximation Engine: Stone-Weierstrass", "subject": "Signature approximation engine"}, {"id": "JAH-FUNAS-000024", "title": "Signature Open Problem Board: Functional Analysis", "subject": "Signature functional problem board"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: functional-analysis-signature');
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
