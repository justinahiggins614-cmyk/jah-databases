// Demo for the Theoretical Computer Science Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Evidence status is stated
// exactly as the sources support it; an open problem is reported
// open. Signature framing is a SIGNATURE DESIGN CLAIM only.
const RECORDS = [{"id": "JAH-THCS-000001", "title": "Turing Machines", "subject": "Turing machines"}, {"id": "JAH-THCS-000002", "title": "The Cook-Levin Theorem", "subject": "the Cook-Levin theorem"}, {"id": "JAH-THCS-000003", "title": "P versus NP: An Open Problem", "subject": "the P versus NP problem"}, {"id": "JAH-THCS-000004", "title": "NP-Completeness", "subject": "NP-completeness"}, {"id": "JAH-THCS-000005", "title": "NP: The Complexity Class", "subject": "the complexity class NP"}, {"id": "JAH-THCS-000006", "title": "The Time Hierarchy Theorem", "subject": "the time hierarchy theorem"}, {"id": "JAH-THCS-000007", "title": "The Space Hierarchy Theorem", "subject": "the space hierarchy theorem"}, {"id": "JAH-THCS-000008", "title": "Savitch's Theorem", "subject": "Savitch's theorem on space"}, {"id": "JAH-THCS-000009", "title": "The PCP Theorem", "subject": "the PCP theorem"}, {"id": "JAH-THCS-000010", "title": "Ladner's Theorem", "subject": "Ladner's theorem on NP-intermediate problems"}, {"id": "JAH-THCS-000011", "title": "Rice's Theorem", "subject": "Rice's theorem on program properties"}, {"id": "JAH-THCS-000012", "title": "Circuit Complexity", "subject": "circuit complexity"}, {"id": "JAH-THCS-000013", "title": "Probabilistic Turing Machines and BPP", "subject": "probabilistic Turing machines and BPP"}, {"id": "JAH-THCS-000014", "title": "Interactive Proofs and IP Equals PSPACE", "subject": "interactive proofs and IP equals PSPACE"}, {"id": "JAH-THCS-000015", "title": "Zero-Knowledge Proofs", "subject": "zero-knowledge proofs"}, {"id": "JAH-THCS-000016", "title": "Shor's Algorithm", "subject": "Shor's algorithm for factoring"}, {"id": "JAH-THCS-000017", "title": "BQP: Bounded-Error Quantum Polynomial Time", "subject": "the complexity class BQP"}, {"id": "JAH-THCS-000018", "title": "Quantum Computing", "subject": "quantum computing"}, {"id": "JAH-THCS-000019", "title": "Communication Complexity", "subject": "communication complexity"}, {"id": "JAH-THCS-000020", "title": "Parameterized Complexity", "subject": "parameterized complexity"}, {"id": "JAH-THCS-000021", "title": "Approximation Algorithms", "subject": "approximation algorithms"}, {"id": "JAH-THCS-000022", "title": "The FLP Impossibility Result", "subject": "the FLP impossibility result for distributed consensus"}, {"id": "JAH-THCS-000023", "title": "One-Way Functions", "subject": "one-way functions"}, {"id": "JAH-THCS-000024", "title": "Derandomization", "subject": "derandomization"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: theoretical-computer-science');
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
