// Demo for the The Signature Programmable Materials Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PROMATS-000001", "title": "A Shape-Shifting Bridge Joint", "subject": "shape-shifting bridge joint design"}, {"id": "JAH-PROMATS-000002", "title": "A Self-Fitting Splint Study", "subject": "self-fitting splint design"}, {"id": "JAH-PROMATS-000003", "title": "An Electroactive Artificial Muscle", "subject": "electroactive artificial muscle design"}, {"id": "JAH-PROMATS-000004", "title": "A Magnetorheological Shock Absorber", "subject": "magnetorheological shock absorber design"}, {"id": "JAH-PROMATS-000005", "title": "A Phase-Change Cooling Wall", "subject": "phase-change cooling wall design"}, {"id": "JAH-PROMATS-000006", "title": "A Self-Healing Phone Skin", "subject": "self-healing phone skin design"}, {"id": "JAH-PROMATS-000007", "title": "A Sun-Tracking Window Film", "subject": "sun-tracking window film design"}, {"id": "JAH-PROMATS-000008", "title": "A 4D-Printed Folding Chair", "subject": "4d-printed folding chair design"}, {"id": "JAH-PROMATS-000009", "title": "A Claytronics Sandbox", "subject": "claytronics sandbox design"}, {"id": "JAH-PROMATS-000010", "title": "A Tunable Metamaterial Lens", "subject": "tunable metamaterial lens design"}, {"id": "JAH-PROMATS-000011", "title": "A Hydrogel Release Model", "subject": "hydrogel release model design"}, {"id": "JAH-PROMATS-000012", "title": "A Piezoelectric Floor Tile", "subject": "piezoelectric floor tile design"}, {"id": "JAH-PROMATS-000013", "title": "A Thermoelectric Waste-Heat Harvester", "subject": "thermoelectric waste-heat harvester design"}, {"id": "JAH-PROMATS-000014", "title": "A Colour-Changing Facade", "subject": "colour-changing facade design"}, {"id": "JAH-PROMATS-000015", "title": "A Stiffness-Tuning Sports Grip", "subject": "stiffness-tuning sports grip design"}, {"id": "JAH-PROMATS-000016", "title": "A Soft Robotic Gripper", "subject": "soft robotic gripper design"}, {"id": "JAH-PROMATS-000017", "title": "A Programmable Weave Jacket", "subject": "programmable weave jacket design"}, {"id": "JAH-PROMATS-000018", "title": "A Self-Assembling Shelter Kit", "subject": "self-assembling shelter kit design"}, {"id": "JAH-PROMATS-000019", "title": "A Materials Testing Bench", "subject": "materials testing bench design"}, {"id": "JAH-PROMATS-000020", "title": "A Programmable Hospital Bed Surface", "subject": "programmable hospital bed surface design"}, {"id": "JAH-PROMATS-000021", "title": "A Breathing Building Skin", "subject": "breathing building skin design"}, {"id": "JAH-PROMATS-000022", "title": "A Recyclable Programmable Panel", "subject": "recyclable programmable panel design"}, {"id": "JAH-PROMATS-000023", "title": "A Programmable Materials Teaching Kit", "subject": "programmable materials teaching kit design"}, {"id": "JAH-PROMATS-000024", "title": "A Future Programmable Materials Laboratory", "subject": "future programmable materials laboratory design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: programmable-materials-signature');
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
