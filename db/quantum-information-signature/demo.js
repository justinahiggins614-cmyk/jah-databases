// Demo for the The Signature Quantum Information Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-QINFS-000001", "title": "Signature Qubit Room", "subject": "signature qubit room"}, {"id": "JAH-QINFS-000002", "title": "Signature Bit Cradle", "subject": "signature bit cradle"}, {"id": "JAH-QINFS-000003", "title": "Signature Superposition Bridge", "subject": "signature superposition bridge"}, {"id": "JAH-QINFS-000004", "title": "Signature Entanglement Loom", "subject": "signature entanglement loom"}, {"id": "JAH-QINFS-000005", "title": "Signature Gate Workshop", "subject": "signature gate workshop"}, {"id": "JAH-QINFS-000006", "title": "Signature Computing Hall", "subject": "signature computing hall"}, {"id": "JAH-QINFS-000007", "title": "Signature Error Shield", "subject": "signature error shield"}, {"id": "JAH-QINFS-000008", "title": "Signature Key Courier", "subject": "signature key courier"}, {"id": "JAH-QINFS-000009", "title": "Signature Quantum Web", "subject": "signature quantum web"}, {"id": "JAH-QINFS-000010", "title": "Signature Sensing Needle", "subject": "signature sensing needle"}, {"id": "JAH-QINFS-000011", "title": "Signature Message Tunnel", "subject": "signature message tunnel"}, {"id": "JAH-QINFS-000012", "title": "Signature Algorithm Library", "subject": "signature algorithm library"}, {"id": "JAH-QINFS-000013", "title": "Signature Noise Blanket", "subject": "signature noise blanket"}, {"id": "JAH-QINFS-000014", "title": "Signature Memory Vault", "subject": "signature memory vault"}, {"id": "JAH-QINFS-000015", "title": "Signature Post-Quantum Lock", "subject": "signature post-quantum lock"}, {"id": "JAH-QINFS-000016", "title": "Signature Standard Ruler", "subject": "signature standard ruler"}, {"id": "JAH-QINFS-000017", "title": "Signature Simulation Mirror", "subject": "signature simulation mirror"}, {"id": "JAH-QINFS-000018", "title": "Signature Cold Circuit Forge", "subject": "signature cold circuit forge"}, {"id": "JAH-QINFS-000019", "title": "Signature Ion Trap Garden", "subject": "signature ion trap garden"}, {"id": "JAH-QINFS-000020", "title": "Signature Light Circuit", "subject": "signature light circuit"}, {"id": "JAH-QINFS-000021", "title": "Signature Security Watchtower", "subject": "signature security watchtower"}, {"id": "JAH-QINFS-000022", "title": "Signature Repeater Relay", "subject": "signature repeater relay"}, {"id": "JAH-QINFS-000023", "title": "Signature Teaching Staircase", "subject": "signature teaching staircase"}, {"id": "JAH-QINFS-000024", "title": "Signature Quantum Seed", "subject": "signature quantum seed"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: quantum-information-signature');
  console.log('EDITION: signature');
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
