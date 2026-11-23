// Demo for the Advanced Mathematical Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-AMR-000001", "title": "The Riemann Hypothesis: The Greatest Open Problem in Mathematics", "subject": "Riemann hypothesis"}, {"id": "JAH-AMR-000002", "title": "Fermat's Last Theorem: Proved by Andrew Wiles", "subject": "Fermat's Last Theorem"}, {"id": "JAH-AMR-000003", "title": "The Poincare Conjecture: The Shape of Three-Dimensional Space", "subject": "Poincare conjecture"}, {"id": "JAH-AMR-000004", "title": "The Four Colour Theorem: The First Major Computer-Assisted Proof", "subject": "Four color theorem"}, {"id": "JAH-AMR-000005", "title": "The Classification of Finite Simple Groups: Thirty Thousand Pages", "subject": "classification of finite simple groups"}, {"id": "JAH-AMR-000006", "title": "The Langlands Program: A Grand Unification of Mathematics", "subject": "Langlands program"}, {"id": "JAH-AMR-000007", "title": "Hilbert's Problems: Twenty-Three Questions That Shaped a Century", "subject": "Hilbert's problems"}, {"id": "JAH-AMR-000008", "title": "The Millennium Prize Problems: Seven Problems, One Solved", "subject": "Millennium Prize Problems"}, {"id": "JAH-AMR-000009", "title": "The Birch and Swinnerton-Dyer Conjecture: Rational Points on Elliptic Curves", "subject": "Birch and Swinnerton-Dyer conjecture"}, {"id": "JAH-AMR-000010", "title": "The Hodge Conjecture: Which Shapes Come from Algebra", "subject": "Hodge conjecture"}, {"id": "JAH-AMR-000011", "title": "Navier-Stokes Existence and Smoothness: Do the Equations Break Down", "subject": "Navier-Stokes existence and smoothness"}, {"id": "JAH-AMR-000012", "title": "P versus NP: The Central Question of Computer Science", "subject": "P versus NP problem"}, {"id": "JAH-AMR-000013", "title": "Mathematical Proof: What Counts as a Proof", "subject": "mathematical proof"}, {"id": "JAH-AMR-000014", "title": "The abc Conjecture: A Deep Claim About Addition and Multiplication", "subject": "abc conjecture"}, {"id": "JAH-AMR-000015", "title": "The Twin Prime Conjecture: Primes in Pairs", "subject": "twin prime conjecture"}, {"id": "JAH-AMR-000016", "title": "Goldbach's Conjecture: Every Even Number Is a Sum of Two Primes", "subject": "Goldbach's conjecture"}, {"id": "JAH-AMR-000017", "title": "The Collatz Conjecture: The Simplest Unsolved Problem", "subject": "Collatz conjecture"}, {"id": "JAH-AMR-000018", "title": "The Continuum Hypothesis: Independence from the Axioms", "subject": "continuum hypothesis"}, {"id": "JAH-AMR-000019", "title": "Godel's Incompleteness Theorems: The Limits of Formal Systems", "subject": "Godel's incompleteness theorems"}, {"id": "JAH-AMR-000020", "title": "The Weil Conjectures: Counting Points, Finding Patterns", "subject": "Weil conjectures"}, {"id": "JAH-AMR-000021", "title": "The Mordell Conjecture: Faltings's Theorem on Rational Points", "subject": "Mordell conjecture (Faltings's theorem)"}, {"id": "JAH-AMR-000022", "title": "The Kepler Conjecture: The Densest Way to Stack Spheres", "subject": "Kepler conjecture"}, {"id": "JAH-AMR-000023", "title": "Research Recognition: The Abel Prize and the Fields Medal", "subject": "Abel Prize and Fields Medal"}, {"id": "JAH-AMR-000024", "title": "Reproducibility in Mathematical Research: Checking the Checkers", "subject": "reproducibility in mathematical research"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-mathematical-research');
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
