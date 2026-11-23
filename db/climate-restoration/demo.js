// Demo for the Climate Restoration Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-CLRE-000001", "title": "What Climate Restoration Research Is", "subject": "climate restoration research identity"}, {"id": "JAH-CLRE-000002", "title": "Carbon Dioxide Removal Overview", "subject": "carbon dioxide removal overview"}, {"id": "JAH-CLRE-000003", "title": "Direct Air Capture", "subject": "direct air capture"}, {"id": "JAH-CLRE-000004", "title": "Enhanced Rock Weathering", "subject": "enhanced rock weathering"}, {"id": "JAH-CLRE-000005", "title": "Ocean Alkalinity Enhancement", "subject": "ocean alkalinity enhancement"}, {"id": "JAH-CLRE-000006", "title": "Reforestation and Afforestation", "subject": "reforestation and afforestation"}, {"id": "JAH-CLRE-000007", "title": "Soil Carbon Restoration", "subject": "soil carbon restoration"}, {"id": "JAH-CLRE-000008", "title": "Wetland and Peatland Restoration", "subject": "wetland and peatland restoration"}, {"id": "JAH-CLRE-000009", "title": "Blue Carbon Ecosystems", "subject": "blue carbon ecosystems"}, {"id": "JAH-CLRE-000010", "title": "Biochar Research", "subject": "biochar research"}, {"id": "JAH-CLRE-000011", "title": "Ocean Iron Fertilization Research", "subject": "ocean iron fertilization research"}, {"id": "JAH-CLRE-000012", "title": "Solar Radiation Management Research", "subject": "solar radiation management research"}, {"id": "JAH-CLRE-000013", "title": "Stratospheric Aerosol Injection Research", "subject": "stratospheric aerosol injection research"}, {"id": "JAH-CLRE-000014", "title": "Marine Cloud Brightening Research", "subject": "marine cloud brightening research"}, {"id": "JAH-CLRE-000015", "title": "Climate Monitoring and Measurement", "subject": "climate monitoring and measurement"}, {"id": "JAH-CLRE-000016", "title": "Carbon Accounting and Verification", "subject": "carbon accounting and verification"}, {"id": "JAH-CLRE-000017", "title": "Ecosystem Restoration and Biodiversity", "subject": "ecosystem restoration and biodiversity"}, {"id": "JAH-CLRE-000018", "title": "Climate Adaptation Research", "subject": "climate adaptation research"}, {"id": "JAH-CLRE-000019", "title": "Governance of Climate Intervention Research", "subject": "governance of climate intervention research"}, {"id": "JAH-CLRE-000020", "title": "Climate Models and Simulation", "subject": "climate models and simulation"}, {"id": "JAH-CLRE-000021", "title": "Restoration of Degraded Lands", "subject": "restoration of degraded lands"}, {"id": "JAH-CLRE-000022", "title": "Urban Climate Restoration Research", "subject": "urban climate restoration research"}, {"id": "JAH-CLRE-000023", "title": "Freshwater System Restoration", "subject": "freshwater system restoration"}, {"id": "JAH-CLRE-000024", "title": "Future Expansion: Climate Research Horizons", "subject": "climate research horizons"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: climate-restoration');
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
