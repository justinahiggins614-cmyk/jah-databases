// Demo for the Spacecraft Engineering Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SCEN-000001", "title": "Spacecraft Bus Architecture", "subject": "Spacecraft bus architecture"}, {"id": "JAH-SCEN-000002", "title": "Spacecraft Structural Design", "subject": "Spacecraft structural design"}, {"id": "JAH-SCEN-000003", "title": "Spacecraft Thermal Control System", "subject": "Spacecraft thermal control system"}, {"id": "JAH-SCEN-000004", "title": "Spacecraft Power Subsystem", "subject": "Spacecraft power subsystem"}, {"id": "JAH-SCEN-000005", "title": "Spacecraft Attitude Control System", "subject": "Spacecraft attitude control system"}, {"id": "JAH-SCEN-000006", "title": "Reaction Wheel Assembly Design", "subject": "Reaction wheel assembly design"}, {"id": "JAH-SCEN-000007", "title": "Star Tracker Navigation Sensor", "subject": "Star tracker navigation sensor"}, {"id": "JAH-SCEN-000008", "title": "Spacecraft Propulsion Subsystem", "subject": "Spacecraft propulsion subsystem"}, {"id": "JAH-SCEN-000009", "title": "Spacecraft Communications Subsystem", "subject": "Spacecraft communications subsystem"}, {"id": "JAH-SCEN-000010", "title": "Spacecraft Command and Data Handling", "subject": "Spacecraft command and data handling"}, {"id": "JAH-SCEN-000011", "title": "Spacecraft Solar Array Design", "subject": "Spacecraft solar array design"}, {"id": "JAH-SCEN-000012", "title": "Spacecraft Battery Energy Storage", "subject": "Spacecraft battery energy storage"}, {"id": "JAH-SCEN-000013", "title": "Spacecraft Radiation Shielding Design", "subject": "Spacecraft radiation shielding design"}, {"id": "JAH-SCEN-000014", "title": "Spacecraft Harness and Wiring Design", "subject": "Spacecraft harness and wiring design"}, {"id": "JAH-SCEN-000015", "title": "Spacecraft Mechanisms and Deployment", "subject": "Spacecraft mechanisms and deployment"}, {"id": "JAH-SCEN-000016", "title": "Spacecraft Materials Selection", "subject": "Spacecraft materials selection"}, {"id": "JAH-SCEN-000017", "title": "Spacecraft Integration and Test", "subject": "Spacecraft integration and test"}, {"id": "JAH-SCEN-000018", "title": "Spacecraft Fault Protection Design", "subject": "Spacecraft fault protection design"}, {"id": "JAH-SCEN-000019", "title": "Spacecraft Guidance Computer Architecture", "subject": "Spacecraft guidance computer architecture"}, {"id": "JAH-SCEN-000020", "title": "Spacecraft Docking Mechanism Design", "subject": "Spacecraft docking mechanism design"}, {"id": "JAH-SCEN-000021", "title": "Spacecraft Antenna Design", "subject": "Spacecraft antenna design"}, {"id": "JAH-SCEN-000022", "title": "Spacecraft Life Support Integration", "subject": "Spacecraft life support integration"}, {"id": "JAH-SCEN-000023", "title": "Spacecraft Reentry Capsule Structure", "subject": "Spacecraft reentry capsule structure"}, {"id": "JAH-SCEN-000024", "title": "Spacecraft Robotic Arm Design", "subject": "Spacecraft robotic arm design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: spacecraft-engineering');
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
