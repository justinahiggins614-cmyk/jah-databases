// Demo for the The Signature Advanced Energy Storage Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-ADESS-000001", "title": "Signature Storage Vault", "subject": "signature storage vault"}, {"id": "JAH-ADESS-000002", "title": "Signature Ion Garden", "subject": "signature ion garden"}, {"id": "JAH-ADESS-000003", "title": "Signature Solid-State Forge", "subject": "signature solid-state forge"}, {"id": "JAH-ADESS-000004", "title": "Signature Flow River", "subject": "signature flow river"}, {"id": "JAH-ADESS-000005", "title": "Signature Sodium Field", "subject": "signature sodium field"}, {"id": "JAH-ADESS-000006", "title": "Signature Grid Reservoir", "subject": "signature grid reservoir"}, {"id": "JAH-ADESS-000007", "title": "Signature Home Cellar", "subject": "signature home cellar"}, {"id": "JAH-ADESS-000008", "title": "Signature Fast Capacitor Tower", "subject": "signature fast capacitor tower"}, {"id": "JAH-ADESS-000009", "title": "Signature Air Cavern", "subject": "signature air cavern"}, {"id": "JAH-ADESS-000010", "title": "Signature Mountain Lake", "subject": "signature mountain lake"}, {"id": "JAH-ADESS-000011", "title": "Signature Heat Bank", "subject": "signature heat bank"}, {"id": "JAH-ADESS-000012", "title": "Signature Hydrogen Well", "subject": "signature hydrogen well"}, {"id": "JAH-ADESS-000013", "title": "Signature Chemistry Workshop", "subject": "signature chemistry workshop"}, {"id": "JAH-ADESS-000014", "title": "Signature Battery Guardian", "subject": "signature battery guardian"}, {"id": "JAH-ADESS-000015", "title": "Signature Safety Blanket", "subject": "signature safety blanket"}, {"id": "JAH-ADESS-000016", "title": "Signature Recycling Loop", "subject": "signature recycling loop"}, {"id": "JAH-ADESS-000017", "title": "Signature Measuring Scale", "subject": "signature measuring scale"}, {"id": "JAH-ADESS-000018", "title": "Signature Sun-and-Wind Storehouse", "subject": "signature sun-and-wind storehouse"}, {"id": "JAH-ADESS-000019", "title": "Signature Vehicle Pack", "subject": "signature vehicle pack"}, {"id": "JAH-ADESS-000020", "title": "Signature Village Microgrid", "subject": "signature village microgrid"}, {"id": "JAH-ADESS-000021", "title": "Signature Long Night Store", "subject": "signature long night store"}, {"id": "JAH-ADESS-000022", "title": "Signature Cost Ledger", "subject": "signature cost ledger"}, {"id": "JAH-ADESS-000023", "title": "Signature Testing Bench", "subject": "signature testing bench"}, {"id": "JAH-ADESS-000024", "title": "Signature Storage Seed", "subject": "signature storage seed"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-energy-storage-signature');
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
