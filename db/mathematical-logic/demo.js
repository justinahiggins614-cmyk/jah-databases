// Demo for the Mathematical Logic Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-MLOG-000001", "title": "Godel's First Incompleteness Theorem", "subject": "Godel's first incompleteness theorem"}, {"id": "JAH-MLOG-000002", "title": "Godel's Second Incompleteness Theorem", "subject": "Godel's second incompleteness theorem"}, {"id": "JAH-MLOG-000003", "title": "Godel's Completeness Theorem", "subject": "Godel's completeness theorem for first-order logic"}, {"id": "JAH-MLOG-000004", "title": "The Compactness Theorem", "subject": "the compactness theorem of first-order logic"}, {"id": "JAH-MLOG-000005", "title": "The Lowenheim-Skolem Theorem", "subject": "the Lowenheim-Skolem theorem"}, {"id": "JAH-MLOG-000006", "title": "The Halting Problem Is Undecidable", "subject": "the undecidability of the halting problem"}, {"id": "JAH-MLOG-000007", "title": "Tarski's Undefinability Theorem", "subject": "Tarski's undefinability theorem for truth"}, {"id": "JAH-MLOG-000008", "title": "The Church-Turing Thesis", "subject": "the Church-Turing thesis"}, {"id": "JAH-MLOG-000009", "title": "Zermelo-Fraenkel Set Theory (ZFC)", "subject": "Zermelo-Fraenkel set theory with choice"}, {"id": "JAH-MLOG-000010", "title": "The Continuum Hypothesis Is Independent of ZFC", "subject": "the independence of the continuum hypothesis"}, {"id": "JAH-MLOG-000011", "title": "Forcing: Cohen's Method for Building Models", "subject": "forcing in set theory"}, {"id": "JAH-MLOG-000012", "title": "The Axiom of Choice Is Independent of ZF", "subject": "the independence of the axiom of choice"}, {"id": "JAH-MLOG-000013", "title": "Lob's Theorem", "subject": "Lob's theorem on provability"}, {"id": "JAH-MLOG-000014", "title": "Gentzen's Consistency Proof for Arithmetic", "subject": "Gentzen's consistency proof for arithmetic"}, {"id": "JAH-MLOG-000015", "title": "First-Order Logic", "subject": "first-order logic"}, {"id": "JAH-MLOG-000016", "title": "Second-Order Logic", "subject": "second-order logic"}, {"id": "JAH-MLOG-000017", "title": "The Lambda Calculus", "subject": "the lambda calculus"}, {"id": "JAH-MLOG-000018", "title": "Type Theory", "subject": "type theory"}, {"id": "JAH-MLOG-000019", "title": "Modal Logic and S5", "subject": "modal logic and the system S5"}, {"id": "JAH-MLOG-000020", "title": "Intuitionistic Logic", "subject": "intuitionistic logic"}, {"id": "JAH-MLOG-000021", "title": "Decidability of Presburger Arithmetic", "subject": "the decidability of Presburger arithmetic"}, {"id": "JAH-MLOG-000022", "title": "Nonstandard Analysis", "subject": "nonstandard analysis"}, {"id": "JAH-MLOG-000023", "title": "Model Theory", "subject": "model theory"}, {"id": "JAH-MLOG-000024", "title": "Proof Theory", "subject": "proof theory"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: mathematical-logic');
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
