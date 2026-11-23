// Demo for the Functional Analysis Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-FUNA-000001", "title": "Normed Vector Spaces", "subject": "Normed vector spaces"}, {"id": "JAH-FUNA-000002", "title": "Banach Spaces and Completeness", "subject": "Banach spaces"}, {"id": "JAH-FUNA-000003", "title": "Hilbert Spaces and Inner Products", "subject": "Hilbert spaces"}, {"id": "JAH-FUNA-000004", "title": "The Riesz Representation Theorem for Hilbert Spaces", "subject": "Riesz representation Hilbert"}, {"id": "JAH-FUNA-000005", "title": "Bounded Linear Operators", "subject": "Bounded linear operators"}, {"id": "JAH-FUNA-000006", "title": "The Uniform Boundedness Principle", "subject": "Uniform boundedness principle"}, {"id": "JAH-FUNA-000007", "title": "The Open Mapping Theorem", "subject": "Open mapping theorem"}, {"id": "JAH-FUNA-000008", "title": "The Closed Graph Theorem", "subject": "Closed graph theorem"}, {"id": "JAH-FUNA-000009", "title": "The Hahn-Banach Theorem", "subject": "Hahn-Banach theorem"}, {"id": "JAH-FUNA-000010", "title": "Dual Spaces and Weak Topologies", "subject": "Dual spaces and weak topologies"}, {"id": "JAH-FUNA-000011", "title": "Compact Operators", "subject": "Compact operators"}, {"id": "JAH-FUNA-000012", "title": "The Spectral Theorem for Self-Adjoint Operators", "subject": "Spectral theorem"}, {"id": "JAH-FUNA-000013", "title": "The Fredholm Alternative", "subject": "Fredholm alternative"}, {"id": "JAH-FUNA-000014", "title": "Distributions and Generalized Functions", "subject": "Distributions"}, {"id": "JAH-FUNA-000015", "title": "The Fourier Transform on L2", "subject": "Fourier transform on L2"}, {"id": "JAH-FUNA-000016", "title": "Sobolev Spaces", "subject": "Sobolev spaces"}, {"id": "JAH-FUNA-000017", "title": "The Lax-Milgram Theorem", "subject": "Lax-Milgram theorem"}, {"id": "JAH-FUNA-000018", "title": "Unbounded Operators and Domains", "subject": "Unbounded operators"}, {"id": "JAH-FUNA-000019", "title": "The Hille-Yosida Theorem and Semigroups", "subject": "Hille-Yosida theorem"}, {"id": "JAH-FUNA-000020", "title": "The Krein-Milman Theorem", "subject": "Krein-Milman theorem"}, {"id": "JAH-FUNA-000021", "title": "Fixed Point Theorems in Banach Spaces", "subject": "Fixed point theorems"}, {"id": "JAH-FUNA-000022", "title": "The Gelfand Theory of Banach Algebras", "subject": "Gelfand theory"}, {"id": "JAH-FUNA-000023", "title": "The Stone-Weierstrass Theorem", "subject": "Stone-Weierstrass theorem"}, {"id": "JAH-FUNA-000024", "title": "Open Problems in Functional Analysis", "subject": "Open problems in functional analysis"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: functional-analysis');
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
