// Demo for the Rocket Propulsion Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-RPRO-000001", "title": "The Tsiolkovsky Rocket Equation and Mass Ratio", "subject": "the Tsiolkovsky rocket equation"}, {"id": "JAH-RPRO-000002", "title": "Specific Impulse and Exhaust Velocity Across Engine Types", "subject": "specific impulse across engine types"}, {"id": "JAH-RPRO-000003", "title": "Liquid-Propellant Rocket Engines and the RS-25", "subject": "liquid-propellant rocket engines"}, {"id": "JAH-RPRO-000004", "title": "Solid-Fuel Rocket Motors and the Space Shuttle Booster", "subject": "solid-fuel rocket motors"}, {"id": "JAH-RPRO-000005", "title": "Hybrid-Propellant Rockets and SpaceShipOne", "subject": "hybrid-propellant rockets"}, {"id": "JAH-RPRO-000006", "title": "De Laval Nozzles and Exhaust Expansion", "subject": "de Laval nozzles and exhaust expansion"}, {"id": "JAH-RPRO-000007", "title": "Combustion Chambers and Injector Design", "subject": "combustion chambers and injectors"}, {"id": "JAH-RPRO-000008", "title": "Turbopumps and High-Pressure Propellant Feed", "subject": "turbopumps and propellant feed"}, {"id": "JAH-RPRO-000009", "title": "Regenerative Cooling of Rocket Engines", "subject": "regenerative cooling of rocket engines"}, {"id": "JAH-RPRO-000010", "title": "The RS-25 Space Shuttle Main Engine", "subject": "the RS-25 Space Shuttle main engine"}, {"id": "JAH-RPRO-000011", "title": "The RL10 Upper-Stage Engine and Expander Cycle", "subject": "the RL10 upper-stage engine"}, {"id": "JAH-RPRO-000012", "title": "The Merlin Engine Family and Falcon 9 Clustering", "subject": "the Merlin engine family"}, {"id": "JAH-RPRO-000013", "title": "The Raptor Full-Flow Staged Combustion Engine", "subject": "the Raptor full-flow staged combustion engine"}, {"id": "JAH-RPRO-000014", "title": "Ion Thrusters and the NEXT Engine", "subject": "ion thrusters and the NEXT engine"}, {"id": "JAH-RPRO-000015", "title": "Hall-Effect Thrusters and the SPT-100", "subject": "Hall-effect thrusters"}, {"id": "JAH-RPRO-000016", "title": "Pulsed Plasma Thrusters for Small Spacecraft", "subject": "pulsed plasma thrusters"}, {"id": "JAH-RPRO-000017", "title": "Nuclear Thermal Propulsion and the NERVA Program", "subject": "nuclear thermal propulsion"}, {"id": "JAH-RPRO-000018", "title": "Solar Sails and Light Pressure Propulsion", "subject": "solar sails and light pressure propulsion"}, {"id": "JAH-RPRO-000019", "title": "Rocket Propellants: Cryogenic, Hypergolic, and Solid", "subject": "rocket propellants"}, {"id": "JAH-RPRO-000020", "title": "Propellant Tanks and Pressurization", "subject": "propellant tanks and pressurization"}, {"id": "JAH-RPRO-000021", "title": "Thrust Vector Control and Engine Gimbaling", "subject": "thrust vector control and engine gimbaling"}, {"id": "JAH-RPRO-000022", "title": "Engine Clustering, Staging, and the Saturn V First Stage", "subject": "engine clustering and staging"}, {"id": "JAH-RPRO-000023", "title": "Propulsion Test Stands and Hot-Fire Testing", "subject": "propulsion test stands and hot-fire testing"}, {"id": "JAH-RPRO-000024", "title": "Propulsion System Safety and Failure Modes", "subject": "propulsion system safety and failure modes"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: rocket-propulsion');
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
