// Demo for the Advanced Energy Storage Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-ADES-000001", "title": "What Advanced Energy Storage Is", "subject": "advanced energy storage identity"}, {"id": "JAH-ADES-000002", "title": "Lithium-Ion Batteries at Scale", "subject": "lithium-ion batteries at scale"}, {"id": "JAH-ADES-000003", "title": "Solid-State Batteries", "subject": "solid-state batteries"}, {"id": "JAH-ADES-000004", "title": "Flow Batteries for Long Storage", "subject": "flow batteries for long storage"}, {"id": "JAH-ADES-000005", "title": "Sodium-Ion Batteries", "subject": "sodium-ion batteries"}, {"id": "JAH-ADES-000006", "title": "Grid Energy Storage", "subject": "grid energy storage"}, {"id": "JAH-ADES-000007", "title": "Home Battery Systems", "subject": "home battery systems"}, {"id": "JAH-ADES-000008", "title": "Supercapacitors and Fast Storage", "subject": "supercapacitors and fast storage"}, {"id": "JAH-ADES-000009", "title": "Compressed Air Energy Storage", "subject": "compressed air energy storage"}, {"id": "JAH-ADES-000010", "title": "Pumped Hydro Storage", "subject": "pumped hydro storage"}, {"id": "JAH-ADES-000011", "title": "Thermal Energy Storage", "subject": "thermal energy storage"}, {"id": "JAH-ADES-000012", "title": "Hydrogen as Stored Energy", "subject": "hydrogen as stored energy"}, {"id": "JAH-ADES-000013", "title": "Battery Chemistry and Materials", "subject": "battery chemistry and materials"}, {"id": "JAH-ADES-000014", "title": "Battery Management Systems", "subject": "battery management systems"}, {"id": "JAH-ADES-000015", "title": "Battery Safety and Thermal Control", "subject": "battery safety and thermal control"}, {"id": "JAH-ADES-000016", "title": "Battery Recycling and Second Life", "subject": "battery recycling and second life"}, {"id": "JAH-ADES-000017", "title": "Measuring Storage: Capacity and Efficiency", "subject": "measuring storage capacity and efficiency"}, {"id": "JAH-ADES-000018", "title": "Storage for Solar and Wind Power", "subject": "storage for solar and wind power"}, {"id": "JAH-ADES-000019", "title": "Storage for Electric Vehicles", "subject": "storage for electric vehicles"}, {"id": "JAH-ADES-000020", "title": "Microgrids and Local Storage", "subject": "microgrids and local storage"}, {"id": "JAH-ADES-000021", "title": "Long-Duration Storage", "subject": "long-duration storage"}, {"id": "JAH-ADES-000022", "title": "Storage Costs and Lifetime", "subject": "storage costs and lifetime"}, {"id": "JAH-ADES-000023", "title": "Storage Standards and Testing", "subject": "storage standards and testing"}, {"id": "JAH-ADES-000024", "title": "The Advanced Energy Storage Record Itself", "subject": "advanced energy storage record itself"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-energy-storage');
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
