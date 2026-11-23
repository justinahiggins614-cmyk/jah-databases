// Demo for the The Signature Post-Quantum Computing Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PQCMS-000001", "title": "Signature Design: Quantum-Safe Library", "subject": "signature quantum-safe library"}, {"id": "JAH-PQCMS-000002", "title": "Signature Design: Lattice Workshop", "subject": "signature lattice workshop"}, {"id": "JAH-PQCMS-000003", "title": "Signature Design: Code-Based Vault", "subject": "signature code-based vault"}, {"id": "JAH-PQCMS-000004", "title": "Signature Design: Hash Signature Tree", "subject": "signature hash signature tree"}, {"id": "JAH-PQCMS-000005", "title": "Signature Design: Multivariate Atelier", "subject": "signature multivariate atelier"}, {"id": "JAH-PQCMS-000006", "title": "Signature Design: Isogeny Map Room", "subject": "signature isogeny map room"}, {"id": "JAH-PQCMS-000007", "title": "Signature Design: Standards Council Hall", "subject": "signature standards council hall"}, {"id": "JAH-PQCMS-000008", "title": "Signature Design: Key Exchange Post Office", "subject": "signature key exchange post office"}, {"id": "JAH-PQCMS-000009", "title": "Signature Design: Signature Studio", "subject": "signature signature studio"}, {"id": "JAH-PQCMS-000010", "title": "Signature Design: Long-Life Seal Press", "subject": "signature long-life seal press"}, {"id": "JAH-PQCMS-000011", "title": "Signature Design: Photon Key Courier", "subject": "signature photon key courier"}, {"id": "JAH-PQCMS-000012", "title": "Signature Design: Migration Expedition", "subject": "signature migration expedition"}, {"id": "JAH-PQCMS-000013", "title": "Signature Design: Hybrid Bridge", "subject": "signature hybrid bridge"}, {"id": "JAH-PQCMS-000014", "title": "Signature Design: Identity Gatehouse", "subject": "signature identity gatehouse"}, {"id": "JAH-PQCMS-000015", "title": "Signature Design: Chip Forge", "subject": "signature chip forge"}, {"id": "JAH-PQCMS-000016", "title": "Signature Design: Error Correction Loom", "subject": "signature error correction loom"}, {"id": "JAH-PQCMS-000017", "title": "Signature Design: Protocol Switchboard", "subject": "signature protocol switchboard"}, {"id": "JAH-PQCMS-000018", "title": "Signature Design: Agility Workshop", "subject": "signature agility workshop"}, {"id": "JAH-PQCMS-000019", "title": "Signature Design: Randomness Well", "subject": "signature randomness well"}, {"id": "JAH-PQCMS-000020", "title": "Signature Design: Small Device Kit", "subject": "signature small device kit"}, {"id": "JAH-PQCMS-000021", "title": "Signature Design: Threat Map Table", "subject": "signature threat map table"}, {"id": "JAH-PQCMS-000022", "title": "Signature Design: Testing Arena", "subject": "signature testing arena"}, {"id": "JAH-PQCMS-000023", "title": "Signature Design: Horizon Observatory", "subject": "signature horizon observatory"}, {"id": "JAH-PQCMS-000024", "title": "Signature Design: Quantum-Safe City", "subject": "signature quantum-safe city"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: post-quantum-computing-signature');
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
