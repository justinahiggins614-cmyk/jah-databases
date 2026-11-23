// Demo for the Spacecraft Guidance Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SGUI-000001", "title": "Ascent Guidance and the Gravity Turn", "subject": "ascent guidance"}, {"id": "JAH-SGUI-000002", "title": "Powered Descent Guidance for Lunar Landing", "subject": "powered descent guidance"}, {"id": "JAH-SGUI-000003", "title": "Rendezvous Guidance and the Clohessy-Wiltshire Equations", "subject": "rendezvous guidance"}, {"id": "JAH-SGUI-000004", "title": "Docking Guidance and the Final Approach Corridor", "subject": "docking guidance"}, {"id": "JAH-SGUI-000005", "title": "Apollo Guidance Computer and Digital Guidance Heritage", "subject": "Apollo guidance computer heritage"}, {"id": "JAH-SGUI-000006", "title": "Proportional Integral Derivative Control for Spacecraft Attitude", "subject": "PID attitude control"}, {"id": "JAH-SGUI-000007", "title": "Quaternion Attitude Guidance and the Shortest Rotation", "subject": "quaternion attitude guidance"}, {"id": "JAH-SGUI-000008", "title": "Lambert Guidance for Interplanetary Transfer Targeting", "subject": "Lambert transfer targeting"}, {"id": "JAH-SGUI-000009", "title": "Entry Guidance and the Apollo Skip Entry Corridor", "subject": "entry guidance"}, {"id": "JAH-SGUI-000010", "title": "Station-Keeping Guidance for Geostationary Orbit", "subject": "station-keeping guidance"}, {"id": "JAH-SGUI-000011", "title": "Formation Flying Guidance for Satellite Constellations", "subject": "formation flying guidance"}, {"id": "JAH-SGUI-000012", "title": "Low-Thrust Spiral Guidance for Electric Propulsion", "subject": "low-thrust spiral guidance"}, {"id": "JAH-SGUI-000013", "title": "Guidance for Asteroid Proximity Operations", "subject": "asteroid proximity guidance"}, {"id": "JAH-SGUI-000014", "title": "Guidance Fault Detection and Safe-Mode Handover", "subject": "guidance fault detection"}, {"id": "JAH-SGUI-000015", "title": "Terrain-Relative Navigation Guidance for Landing", "subject": "terrain-relative landing guidance"}, {"id": "JAH-SGUI-000016", "title": "Guidance for Aerocapture at Mars", "subject": "Mars aerocapture guidance"}, {"id": "JAH-SGUI-000017", "title": "Solar Sail Steering Guidance", "subject": "solar sail steering guidance"}, {"id": "JAH-SGUI-000018", "title": "Guidance for On-Orbit Servicing Approach", "subject": "on-orbit servicing guidance"}, {"id": "JAH-SGUI-000019", "title": "Guidance for Deploying a Tethered Satellite", "subject": "tether deployment guidance"}, {"id": "JAH-SGUI-000020", "title": "Guidance for Earth Return and Splashdown Targeting", "subject": "Earth return guidance"}, {"id": "JAH-SGUI-000021", "title": "Guidance for Lunar Orbit Insertion Burn Targeting", "subject": "lunar orbit insertion guidance"}, {"id": "JAH-SGUI-000022", "title": "Guidance for Comet Flyby Targeting", "subject": "comet flyby guidance"}, {"id": "JAH-SGUI-000023", "title": "Guidance for Spacecraft Spin Stabilization", "subject": "spin stabilization guidance"}, {"id": "JAH-SGUI-000024", "title": "Guidance for Multi-Burn Orbit Raising", "subject": "multi-burn orbit raising"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: spacecraft-guidance');
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
