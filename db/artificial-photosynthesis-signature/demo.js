// Demo for the The Signature Artificial Photosynthesis Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-APHOS-000001", "title": "Signature Sun Leaf", "subject": "signature sun leaf"}, {"id": "JAH-APHOS-000002", "title": "Signature Green Model", "subject": "signature green model"}, {"id": "JAH-APHOS-000003", "title": "Signature Water Splitter", "subject": "signature water splitter"}, {"id": "JAH-APHOS-000004", "title": "Signature Carbon Kitchen", "subject": "signature carbon kitchen"}, {"id": "JAH-APHOS-000005", "title": "Signature Light Catcher", "subject": "signature light catcher"}, {"id": "JAH-APHOS-000006", "title": "Signature Sun Cell", "subject": "signature sun cell"}, {"id": "JAH-APHOS-000007", "title": "Signature Solar Fuel Still", "subject": "signature solar fuel still"}, {"id": "JAH-APHOS-000008", "title": "Signature Oxygen Fountain", "subject": "signature oxygen fountain"}, {"id": "JAH-APHOS-000009", "title": "Signature Fuel Forge", "subject": "signature fuel forge"}, {"id": "JAH-APHOS-000010", "title": "Signature Sun Stone", "subject": "signature sun stone"}, {"id": "JAH-APHOS-000011", "title": "Signature Electron Road", "subject": "signature electron road"}, {"id": "JAH-APHOS-000012", "title": "Signature Leaf Workshop", "subject": "signature leaf workshop"}, {"id": "JAH-APHOS-000013", "title": "Signature Efficiency Lens", "subject": "signature efficiency lens"}, {"id": "JAH-APHOS-000014", "title": "Signature Endurance Clock", "subject": "signature endurance clock"}, {"id": "JAH-APHOS-000015", "title": "Signature Scaling Ladder", "subject": "signature scaling ladder"}, {"id": "JAH-APHOS-000016", "title": "Signature Carbon Net", "subject": "signature carbon net"}, {"id": "JAH-APHOS-000017", "title": "Signature Water Fuel Spring", "subject": "signature water fuel spring"}, {"id": "JAH-APHOS-000018", "title": "Signature Air Fuel Spring", "subject": "signature air fuel spring"}, {"id": "JAH-APHOS-000019", "title": "Signature Proving Bench", "subject": "signature proving bench"}, {"id": "JAH-APHOS-000020", "title": "Signature Material Garden", "subject": "signature material garden"}, {"id": "JAH-APHOS-000021", "title": "Signature Grid Bridge", "subject": "signature grid bridge"}, {"id": "JAH-APHOS-000022", "title": "Signature Safety Screen", "subject": "signature safety screen"}, {"id": "JAH-APHOS-000023", "title": "Signature Future Fuel Map", "subject": "signature future fuel map"}, {"id": "JAH-APHOS-000024", "title": "Signature Photosynthesis Seed", "subject": "signature photosynthesis seed"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: artificial-photosynthesis-signature');
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
