// Demo for the Quantum Information Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-QINF-000001", "title": "What Quantum Information Is", "subject": "quantum information identity"}, {"id": "JAH-QINF-000002", "title": "The Quantum Bit", "subject": "the quantum bit"}, {"id": "JAH-QINF-000003", "title": "Superposition and Measurement", "subject": "superposition and measurement"}, {"id": "JAH-QINF-000004", "title": "Entanglement", "subject": "entanglement"}, {"id": "JAH-QINF-000005", "title": "Quantum Gates and Circuits", "subject": "quantum gates and circuits"}, {"id": "JAH-QINF-000006", "title": "Quantum Computing", "subject": "quantum computing"}, {"id": "JAH-QINF-000007", "title": "Quantum Error Correction", "subject": "quantum error correction"}, {"id": "JAH-QINF-000008", "title": "Quantum Key Distribution", "subject": "quantum key distribution"}, {"id": "JAH-QINF-000009", "title": "Quantum Networks", "subject": "quantum networks"}, {"id": "JAH-QINF-000010", "title": "Quantum Sensing", "subject": "quantum sensing"}, {"id": "JAH-QINF-000011", "title": "Quantum Communication", "subject": "quantum communication"}, {"id": "JAH-QINF-000012", "title": "Quantum Algorithms", "subject": "quantum algorithms"}, {"id": "JAH-QINF-000013", "title": "Decoherence and Noise", "subject": "decoherence and noise"}, {"id": "JAH-QINF-000014", "title": "Quantum Memory", "subject": "quantum memory"}, {"id": "JAH-QINF-000015", "title": "Post-Quantum Cryptography", "subject": "post-quantum cryptography"}, {"id": "JAH-QINF-000016", "title": "Quantum Standards and Testing", "subject": "quantum standards and testing"}, {"id": "JAH-QINF-000017", "title": "Quantum Simulation", "subject": "quantum simulation"}, {"id": "JAH-QINF-000018", "title": "Quantum Hardware: Superconducting Circuits", "subject": "quantum hardware superconducting circuits"}, {"id": "JAH-QINF-000019", "title": "Quantum Hardware: Trapped Ions", "subject": "quantum hardware trapped ions"}, {"id": "JAH-QINF-000020", "title": "Quantum Hardware: Light-Based Systems", "subject": "quantum hardware light-based systems"}, {"id": "JAH-QINF-000021", "title": "Quantum Information and Security", "subject": "quantum information and security"}, {"id": "JAH-QINF-000022", "title": "Quantum Repeaters and Long Distances", "subject": "quantum repeaters and long distances"}, {"id": "JAH-QINF-000023", "title": "Teaching Quantum Information", "subject": "teaching quantum information"}, {"id": "JAH-QINF-000024", "title": "The Quantum Information Record Itself", "subject": "quantum information record itself"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: quantum-information');
  console.log('EDITION: public');
  console.log('RECORDS: '+RECORDS.length);
  const q1=RECORDS[0].title.split(/\s+/).find(w=>w.length>3).toLowerCase();
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
