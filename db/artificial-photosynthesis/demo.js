// Demo for the Artificial Photosynthesis Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-APHO-000001", "title": "What Artificial Photosynthesis Is", "subject": "artificial photosynthesis identity"}, {"id": "JAH-APHO-000002", "title": "Natural Photosynthesis as the Model", "subject": "natural photosynthesis as the model"}, {"id": "JAH-APHO-000003", "title": "Water Splitting for Hydrogen", "subject": "water splitting for hydrogen"}, {"id": "JAH-APHO-000004", "title": "Carbon Dioxide Reduction to Fuels", "subject": "carbon dioxide reduction to fuels"}, {"id": "JAH-APHO-000005", "title": "Photocatalysts and Light Absorbers", "subject": "photocatalysts and light absorbers"}, {"id": "JAH-APHO-000006", "title": "Photoelectrochemical Cells", "subject": "photoelectrochemical cells"}, {"id": "JAH-APHO-000007", "title": "Solar Fuels", "subject": "solar fuels"}, {"id": "JAH-APHO-000008", "title": "Catalysts for Oxygen Production", "subject": "catalysts for oxygen production"}, {"id": "JAH-APHO-000009", "title": "Catalysts for Fuel Production", "subject": "catalysts for fuel production"}, {"id": "JAH-APHO-000010", "title": "Semiconductors for Sunlight Capture", "subject": "semiconductors for sunlight capture"}, {"id": "JAH-APHO-000011", "title": "Electron Flow and Charge Separation", "subject": "electron flow and charge separation"}, {"id": "JAH-APHO-000012", "title": "Artificial Leaves", "subject": "artificial leaves"}, {"id": "JAH-APHO-000013", "title": "Measuring Efficiency: Solar to Fuel", "subject": "measuring efficiency solar to fuel"}, {"id": "JAH-APHO-000014", "title": "Stability and Lifetime of Devices", "subject": "stability and lifetime of devices"}, {"id": "JAH-APHO-000015", "title": "Scaling Laboratory Devices", "subject": "scaling laboratory devices"}, {"id": "JAH-APHO-000016", "title": "Artificial Photosynthesis and Carbon Capture", "subject": "artificial photosynthesis and carbon capture"}, {"id": "JAH-APHO-000017", "title": "Fuels from Sunlight and Water", "subject": "fuels from sunlight and water"}, {"id": "JAH-APHO-000018", "title": "Fuels from Sunlight and Carbon Dioxide", "subject": "fuels from sunlight and carbon dioxide"}, {"id": "JAH-APHO-000019", "title": "Testing and Validation of Devices", "subject": "testing and validation of devices"}, {"id": "JAH-APHO-000020", "title": "Materials for Artificial Photosynthesis", "subject": "materials for artificial photosynthesis"}, {"id": "JAH-APHO-000021", "title": "Artificial Photosynthesis and Energy Grids", "subject": "artificial photosynthesis and energy grids"}, {"id": "JAH-APHO-000022", "title": "Safety and Environmental Review", "subject": "safety and environmental review"}, {"id": "JAH-APHO-000023", "title": "The Future of Solar Fuels", "subject": "the future of solar fuels"}, {"id": "JAH-APHO-000024", "title": "The Artificial Photosynthesis Record Itself", "subject": "artificial photosynthesis record itself"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: artificial-photosynthesis');
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
