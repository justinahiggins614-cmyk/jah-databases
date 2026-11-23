// Demo for the The Signature Flight Avionics Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-FAVIS-000001", "title": "Signature Low-Power Radiation-Tolerant Processor Study", "subject": "signature low-power radiation-tolerant processor"}, {"id": "JAH-FAVIS-000002", "title": "Signature Time-Triggered 1553 Bus Study", "subject": "signature time-triggered 1553 bus"}, {"id": "JAH-FAVIS-000003", "title": "Signature Dual-Channel ARINC 429 Study", "subject": "signature dual-channel ARINC 429"}, {"id": "JAH-FAVIS-000004", "title": "Signature Fault-Tolerant SpaceWire Network Study", "subject": "signature fault-tolerant SpaceWire network"}, {"id": "JAH-FAVIS-000005", "title": "Signature CAN Bus Guardian Study", "subject": "signature CAN bus guardian"}, {"id": "JAH-FAVIS-000006", "title": "Signature Five-Module Voting Computer Study", "subject": "signature five-module voting computer"}, {"id": "JAH-FAVIS-000007", "title": "Signature Predictive Fault Recovery Study", "subject": "signature predictive fault recovery"}, {"id": "JAH-FAVIS-000008", "title": "Signature Partitioned Flight Software Study", "subject": "signature partitioned flight software"}, {"id": "JAH-FAVIS-000009", "title": "Signature Smart Power Distribution Study", "subject": "signature smart power distribution"}, {"id": "JAH-FAVIS-000010", "title": "Signature Self-Calibrating Sensor Suite Study", "subject": "signature self-calibrating sensor suite"}, {"id": "JAH-FAVIS-000011", "title": "Signature Adaptive Thermal Control Study", "subject": "signature adaptive thermal control"}, {"id": "JAH-FAVIS-000012", "title": "Signature Hierarchical Watchdog Study", "subject": "signature hierarchical watchdog"}, {"id": "JAH-FAVIS-000013", "title": "Signature Filtered Power Bus Study", "subject": "signature filtered power bus"}, {"id": "JAH-FAVIS-000014", "title": "Signature Wear-Levelled Recorder Study", "subject": "signature wear-levelled recorder"}, {"id": "JAH-FAVIS-000015", "title": "Signature Adaptive Telemetry Study", "subject": "signature adaptive telemetry"}, {"id": "JAH-FAVIS-000016", "title": "Signature Modernised Apollo Computer Study", "subject": "signature modernised Apollo computer"}, {"id": "JAH-FAVIS-000017", "title": "Signature Diverse Backup Computer Study", "subject": "signature diverse backup computer"}, {"id": "JAH-FAVIS-000018", "title": "Signature Scrub-Scheduled Memory Study", "subject": "signature scrub-scheduled memory"}, {"id": "JAH-FAVIS-000019", "title": "Signature Precision Time Distribution Study", "subject": "signature precision time distribution"}, {"id": "JAH-FAVIS-000020", "title": "Signature Smart Data Acquisition Study", "subject": "signature smart data acquisition"}, {"id": "JAH-FAVIS-000021", "title": "Signature Coverage-Driven Test Study", "subject": "signature coverage-driven test"}, {"id": "JAH-FAVIS-000022", "title": "Signature Four-Unit Inertial Voting Study", "subject": "signature four-unit inertial voting"}, {"id": "JAH-FAVIS-000023", "title": "Signature Radiation-Hardened CubeSat Avionics Study", "subject": "signature radiation-hardened CubeSat avionics"}, {"id": "JAH-FAVIS-000024", "title": "Signature Model-Based Avionics Verification Study", "subject": "signature model-based avionics verification"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: flight-avionics-signature');
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
