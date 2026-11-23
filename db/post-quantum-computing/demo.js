// Demo for the Post-Quantum Computing Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PQCM-000001", "title": "What Post-Quantum Computing Is", "subject": "post-quantum computing identity"}, {"id": "JAH-PQCM-000002", "title": "Shor's Algorithm and the Quantum Threat", "subject": "shor's algorithm and the quantum threat"}, {"id": "JAH-PQCM-000003", "title": "Lattice-Based Cryptography", "subject": "lattice-based cryptography"}, {"id": "JAH-PQCM-000004", "title": "Code-Based Cryptography", "subject": "code-based cryptography"}, {"id": "JAH-PQCM-000005", "title": "Hash-Based Signatures", "subject": "hash-based signatures"}, {"id": "JAH-PQCM-000006", "title": "Multivariate Cryptography", "subject": "multivariate cryptography"}, {"id": "JAH-PQCM-000007", "title": "Isogeny-Based Cryptography", "subject": "isogeny-based cryptography"}, {"id": "JAH-PQCM-000008", "title": "The NIST Standardization Process", "subject": "NIST standardization process"}, {"id": "JAH-PQCM-000009", "title": "ML-KEM Key Encapsulation", "subject": "ML-KEM key encapsulation"}, {"id": "JAH-PQCM-000010", "title": "ML-DSA Digital Signatures", "subject": "ML-DSA digital signatures"}, {"id": "JAH-PQCM-000011", "title": "SLH-DSA Hash-Based Signatures", "subject": "SLH-DSA hash-based signatures"}, {"id": "JAH-PQCM-000012", "title": "Quantum Key Distribution", "subject": "quantum key distribution"}, {"id": "JAH-PQCM-000013", "title": "Post-Quantum Migration Planning", "subject": "post-quantum migration planning"}, {"id": "JAH-PQCM-000014", "title": "Hybrid Classical-Quantum Cryptography", "subject": "hybrid classical-quantum cryptography"}, {"id": "JAH-PQCM-000015", "title": "Quantum-Resistant Authentication", "subject": "quantum-resistant authentication"}, {"id": "JAH-PQCM-000016", "title": "Post-Quantum Secure Hardware", "subject": "post-quantum secure hardware"}, {"id": "JAH-PQCM-000017", "title": "Quantum Error Correction and Fault Tolerance", "subject": "quantum error correction and fault tolerance"}, {"id": "JAH-PQCM-000018", "title": "Post-Quantum Cryptography in Protocols", "subject": "post-quantum cryptography in protocols"}, {"id": "JAH-PQCM-000019", "title": "Cryptographic Agility", "subject": "cryptographic agility"}, {"id": "JAH-PQCM-000020", "title": "Quantum-Safe Random Number Generation", "subject": "quantum-safe random number generation"}, {"id": "JAH-PQCM-000021", "title": "Post-Quantum Cryptography for Constrained Devices", "subject": "post-quantum cryptography for constrained devices"}, {"id": "JAH-PQCM-000022", "title": "Threat Modeling for the Quantum Transition", "subject": "threat modeling for the quantum transition"}, {"id": "JAH-PQCM-000023", "title": "Verification and Testing of Post-Quantum Implementations", "subject": "verification and testing of post-quantum implementations"}, {"id": "JAH-PQCM-000024", "title": "Future Expansion: Post-Quantum Research Horizons", "subject": "post-quantum research horizons"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: post-quantum-computing');
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
