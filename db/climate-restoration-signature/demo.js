// Demo for the The Signature Climate Restoration Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-CLRES-000001", "title": "Signature Design: Climate Library", "subject": "signature climate library"}, {"id": "JAH-CLRES-000002", "title": "Signature Design: Removal Ledger", "subject": "signature removal ledger"}, {"id": "JAH-CLRES-000003", "title": "Signature Design: Air Capture Mill", "subject": "signature air capture mill"}, {"id": "JAH-CLRES-000004", "title": "Signature Design: Basalt Field", "subject": "signature basalt field"}, {"id": "JAH-CLRES-000005", "title": "Signature Design: Alkalinity Harbour", "subject": "signature alkalinity harbour"}, {"id": "JAH-CLRES-000006", "title": "Signature Design: Forest Nursery", "subject": "signature forest nursery"}, {"id": "JAH-CLRES-000007", "title": "Signature Design: Soil Kitchen", "subject": "signature soil kitchen"}, {"id": "JAH-CLRES-000008", "title": "Signature Design: Peat Bog Rewetting Crew", "subject": "signature peat bog rewetting crew"}, {"id": "JAH-CLRES-000009", "title": "Signature Design: Mangrove Coast", "subject": "signature mangrove coast"}, {"id": "JAH-CLRES-000010", "title": "Signature Design: Charcoal Kiln", "subject": "signature charcoal kiln"}, {"id": "JAH-CLRES-000011", "title": "Signature Design: Iron Garden at Sea", "subject": "signature iron garden at sea"}, {"id": "JAH-CLRES-000012", "title": "Signature Design: Sunshade Council", "subject": "signature sunshade council"}, {"id": "JAH-CLRES-000013", "title": "Signature Design: Sky Particle Workshop", "subject": "signature sky particle workshop"}, {"id": "JAH-CLRES-000014", "title": "Signature Design: Cloud Spray Ship", "subject": "signature cloud spray ship"}, {"id": "JAH-CLRES-000015", "title": "Signature Design: Watchtower Network", "subject": "signature watchtower network"}, {"id": "JAH-CLRES-000016", "title": "Signature Design: Counting House", "subject": "signature counting house"}, {"id": "JAH-CLRES-000017", "title": "Signature Design: Living Meadow", "subject": "signature living meadow"}, {"id": "JAH-CLRES-000018", "title": "Signature Design: Adaptation Town", "subject": "signature adaptation town"}, {"id": "JAH-CLRES-000019", "title": "Signature Design: Decision Round Table", "subject": "signature decision round table"}, {"id": "JAH-CLRES-000020", "title": "Signature Design: Model Planetarium", "subject": "signature model planetarium"}, {"id": "JAH-CLRES-000021", "title": "Signature Design: Healing Valley", "subject": "signature healing valley"}, {"id": "JAH-CLRES-000022", "title": "Signature Design: Cool City Garden", "subject": "signature cool city garden"}, {"id": "JAH-CLRES-000023", "title": "Signature Design: River Workshop", "subject": "signature river workshop"}, {"id": "JAH-CLRES-000024", "title": "Signature Design: Restored World Garden", "subject": "signature restored world garden"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: climate-restoration-signature');
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
