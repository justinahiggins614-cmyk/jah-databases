// Demo for the Flight Avionics Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-FAVI-000001", "title": "Radiation-Tolerant Flight Processors", "subject": "radiation-tolerant flight processors"}, {"id": "JAH-FAVI-000002", "title": "MIL-STD-1553 Data Bus in Spacecraft", "subject": "MIL-STD-1553 data bus"}, {"id": "JAH-FAVI-000003", "title": "ARINC 429 Data Bus Heritage in Flight Systems", "subject": "ARINC 429 data bus"}, {"id": "JAH-FAVI-000004", "title": "SpaceWire High-Speed Avionics Links", "subject": "SpaceWire avionics links"}, {"id": "JAH-FAVI-000005", "title": "CAN Bus in Small Satellite Avionics", "subject": "CAN bus in small satellites"}, {"id": "JAH-FAVI-000006", "title": "Triple Modular Redundancy in Flight Computers", "subject": "triple modular redundancy"}, {"id": "JAH-FAVI-000007", "title": "Fault Detection, Isolation and Recovery in Avionics", "subject": "fault detection isolation recovery"}, {"id": "JAH-FAVI-000008", "title": "Flight Software Architecture and the Core Flight System", "subject": "core flight system software"}, {"id": "JAH-FAVI-000009", "title": "Spacecraft Power Distribution and Avionics Loads", "subject": "spacecraft power distribution"}, {"id": "JAH-FAVI-000010", "title": "Sensor Suites: Gyroscopes, Accelerometers and Magnetometers", "subject": "spacecraft sensor suites"}, {"id": "JAH-FAVI-000011", "title": "Avionics Thermal Design and the Electronics Box", "subject": "avionics thermal design"}, {"id": "JAH-FAVI-000012", "title": "Flight Computer Watchdog Timers and Safe Mode", "subject": "watchdog timers and safe mode"}, {"id": "JAH-FAVI-000013", "title": "Avionics Electromagnetic Compatibility", "subject": "avionics electromagnetic compatibility"}, {"id": "JAH-FAVI-000014", "title": "Onboard Data Handling and Solid-State Recorders", "subject": "onboard data handling"}, {"id": "JAH-FAVI-000015", "title": "Telemetry Formatting and the CCSDS Packet Standard", "subject": "CCSDS telemetry packets"}, {"id": "JAH-FAVI-000016", "title": "Apollo Guidance Computer Legacy in Flight Avionics", "subject": "Apollo computer avionics legacy"}, {"id": "JAH-FAVI-000017", "title": "Flight Avionics for the Space Shuttle Heritage", "subject": "Space Shuttle avionics heritage"}, {"id": "JAH-FAVI-000018", "title": "Single-Event Upset Mitigation in Memory", "subject": "single-event upset mitigation"}, {"id": "JAH-FAVI-000019", "title": "Avionics Timing and Synchronization", "subject": "avionics timing and synchronization"}, {"id": "JAH-FAVI-000020", "title": "Flight Instrumentation and the Data Acquisition Unit", "subject": "flight instrumentation"}, {"id": "JAH-FAVI-000021", "title": "Avionics Built-In Test and Health Monitoring", "subject": "avionics built-in test"}, {"id": "JAH-FAVI-000022", "title": "Redundant Inertial Measurement Units", "subject": "redundant inertial measurement units"}, {"id": "JAH-FAVI-000023", "title": "Avionics for CubeSats and Small Spacecraft", "subject": "CubeSat avionics"}, {"id": "JAH-FAVI-000024", "title": "Flight Avionics Verification and Hardware-in-the-Loop Testing", "subject": "hardware-in-the-loop testing"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: flight-avionics');
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
