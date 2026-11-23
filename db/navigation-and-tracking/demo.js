// Demo for the Navigation and Tracking Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-NAVTR-000001", "title": "Kalman Filtering for Orbit Estimation", "subject": "Kalman filtering"}, {"id": "JAH-NAVTR-000002", "title": "Deep Space Network Two-Way Doppler Tracking", "subject": "Deep Space Network Doppler tracking"}, {"id": "JAH-NAVTR-000003", "title": "Orbit Determination from Ranging Measurements", "subject": "orbit determination from ranging"}, {"id": "JAH-NAVTR-000004", "title": "Star Tracker Attitude Determination", "subject": "star tracker attitude determination"}, {"id": "JAH-NAVTR-000005", "title": "Inertial Navigation and Gyroscope Drift", "subject": "inertial navigation"}, {"id": "JAH-NAVTR-000006", "title": "Global Positioning System Navigation in Low Earth Orbit", "subject": "GPS navigation in low Earth orbit"}, {"id": "JAH-NAVTR-000007", "title": "Two-Line Element Sets and Satellite Tracking", "subject": "two-line element sets"}, {"id": "JAH-NAVTR-000008", "title": "Ground Station Pass Planning and Scheduling", "subject": "ground station pass planning"}, {"id": "JAH-NAVTR-000009", "title": "Atomic Clocks and Deep Space Timekeeping", "subject": "atomic clocks and timekeeping"}, {"id": "JAH-NAVTR-000010", "title": "Delta Differential One-Way Ranging", "subject": "delta differential one-way ranging"}, {"id": "JAH-NAVTR-000011", "title": "Optical Navigation Using Asteroid Landmarks", "subject": "optical navigation with asteroid landmarks"}, {"id": "JAH-NAVTR-000012", "title": "Pulsar-Based Navigation Concepts", "subject": "pulsar-based navigation"}, {"id": "JAH-NAVTR-000013", "title": "Range and Range-Rate Measurement Models", "subject": "range and range-rate models"}, {"id": "JAH-NAVTR-000014", "title": "Tracking Data Compression and the DSN 70-Metre Antenna", "subject": "DSN 70-metre antenna tracking"}, {"id": "JAH-NAVTR-000015", "title": "Navigation for the Voyager Interstellar Trajectory", "subject": "Voyager interstellar navigation"}, {"id": "JAH-NAVTR-000016", "title": "Cassini Navigation at Saturn", "subject": "Cassini navigation at Saturn"}, {"id": "JAH-NAVTR-000017", "title": "James Webb Telescope Station-Keeping Navigation", "subject": "James Webb station-keeping navigation"}, {"id": "JAH-NAVTR-000018", "title": "Lunar Navigation with Earth-Based Tracking", "subject": "lunar navigation with Earth tracking"}, {"id": "JAH-NAVTR-000019", "title": "Mars Relay Tracking and the Mars Network", "subject": "Mars relay tracking"}, {"id": "JAH-NAVTR-000020", "title": "Navigation Covariance Analysis and Error Budgets", "subject": "navigation covariance analysis"}, {"id": "JAH-NAVTR-000021", "title": "Sequential Filtering and the Extended Kalman Filter", "subject": "extended Kalman filter"}, {"id": "JAH-NAVTR-000022", "title": "Batch Least-Squares Orbit Determination", "subject": "batch least-squares orbit determination"}, {"id": "JAH-NAVTR-000023", "title": "Tracking During Solar Conjunction Blackout", "subject": "solar conjunction blackout tracking"}, {"id": "JAH-NAVTR-000024", "title": "Navigation Data Validation and Residual Analysis", "subject": "navigation data validation"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: navigation-and-tracking');
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
