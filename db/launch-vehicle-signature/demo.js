// Demo for the The Signature Launch Vehicle Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-LVEHS-000001", "title": "Signature Two-Stage Orbital Rocket", "subject": "Signature two-stage orbital rocket"}, {"id": "JAH-LVEHS-000002", "title": "Signature Heavy Lift Concept Vehicle", "subject": "Signature heavy lift concept vehicle"}, {"id": "JAH-LVEHS-000003", "title": "Signature Reusable First Stage Design", "subject": "Signature reusable first stage design"}, {"id": "JAH-LVEHS-000004", "title": "Signature Methane Engine Concept", "subject": "Signature methane engine concept"}, {"id": "JAH-LVEHS-000005", "title": "Signature Small Satellite Launcher", "subject": "Signature small satellite launcher"}, {"id": "JAH-LVEHS-000006", "title": "Signature Air-Launch Carrier Concept", "subject": "Signature air-launch carrier concept"}, {"id": "JAH-LVEHS-000007", "title": "Signature Lunar Lander Ascent Stage", "subject": "Signature lunar lander ascent stage"}, {"id": "JAH-LVEHS-000008", "title": "Signature Propellant Depot Transfer Vehicle", "subject": "Signature propellant depot transfer vehicle"}, {"id": "JAH-LVEHS-000009", "title": "Signature Reusable Booster Recovery System", "subject": "Signature reusable booster recovery system"}, {"id": "JAH-LVEHS-000010", "title": "Signature Expandable Nozzle Concept", "subject": "Signature expandable nozzle concept"}, {"id": "JAH-LVEHS-000011", "title": "Signature Composite Tank Structure", "subject": "Signature composite tank structure"}, {"id": "JAH-LVEHS-000012", "title": "Signature Launch Mount and Hold-Down System", "subject": "Signature launch mount and hold-down system"}, {"id": "JAH-LVEHS-000013", "title": "Signature Upper Stage Restart Design", "subject": "Signature upper stage restart design"}, {"id": "JAH-LVEHS-000014", "title": "Signature Payload Fairing Separation System", "subject": "Signature payload fairing separation system"}, {"id": "JAH-LVEHS-000015", "title": "Signature Thrust Vector Actuator Design", "subject": "Signature thrust vector actuator design"}, {"id": "JAH-LVEHS-000016", "title": "Signature Launch Vehicle Avionics Bay", "subject": "Signature launch vehicle avionics bay"}, {"id": "JAH-LVEHS-000017", "title": "Signature Cryogenic Loading System", "subject": "Signature cryogenic loading system"}, {"id": "JAH-LVEHS-000018", "title": "Signature Orbital Tug Concept", "subject": "Signature orbital tug concept"}, {"id": "JAH-LVEHS-000019", "title": "Signature Suborbital Test Vehicle", "subject": "Signature suborbital test vehicle"}, {"id": "JAH-LVEHS-000020", "title": "Signature Clustered Engine Mount", "subject": "Signature clustered engine mount"}, {"id": "JAH-LVEHS-000021", "title": "Signature Grid Fin Control System", "subject": "Signature grid fin control system"}, {"id": "JAH-LVEHS-000022", "title": "Signature Launch Abort System Concept", "subject": "Signature launch abort system concept"}, {"id": "JAH-LVEHS-000023", "title": "Signature Sea-Launch Platform Concept", "subject": "Signature sea-launch platform concept"}, {"id": "JAH-LVEHS-000024", "title": "Signature Reusable Upper Stage Design", "subject": "Signature reusable upper stage design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: launch-vehicle-signature');
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
