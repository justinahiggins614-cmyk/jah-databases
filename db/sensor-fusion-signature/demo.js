// Demo for the The Signature Sensor Fusion Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-SENFS-000001", "title": "Signature Design Study: A Fusion Mission Workbench", "subject": "Sensor fusion overview"}, {"id": "JAH-SENFS-000002", "title": "Signature Design Study: A Kalman Filter Bench", "subject": "Kalman filtering"}, {"id": "JAH-SENFS-000003", "title": "Signature Design Study: A Nonlinear Filter Bench", "subject": "Extended and unscented Kalman filters"}, {"id": "JAH-SENFS-000004", "title": "Signature Design Study: A Particle Filter Bench", "subject": "Particle filters"}, {"id": "JAH-SENFS-000005", "title": "Signature Design Study: A Bayesian Fusion Bench", "subject": "Bayesian fusion"}, {"id": "JAH-SENFS-000006", "title": "Signature Design Study: An Evidence Theory Bench", "subject": "Dempster-Shafer evidence theory"}, {"id": "JAH-SENFS-000007", "title": "Signature Design Study: A Calibration Bench", "subject": "Multi-sensor calibration"}, {"id": "JAH-SENFS-000008", "title": "Signature Design Study: A Time Synchronization Bench", "subject": "Time synchronization"}, {"id": "JAH-SENFS-000009", "title": "Signature Design Study: A Data Association Bench", "subject": "Data association and tracking"}, {"id": "JAH-SENFS-000010", "title": "Signature Design Study: A Radar-Lidar Fusion Bench", "subject": "Radar-Lidar fusion"}, {"id": "JAH-SENFS-000011", "title": "Signature Design Study: A Camera-Lidar Fusion Bench", "subject": "Camera-Lidar fusion"}, {"id": "JAH-SENFS-000012", "title": "Signature Design Study: An Inertial Fusion Bench", "subject": "Inertial navigation fusion"}, {"id": "JAH-SENFS-000013", "title": "Signature Design Study: A GNSS-Denied Fusion Bench", "subject": "GNSS-denied fusion"}, {"id": "JAH-SENFS-000014", "title": "Signature Design Study: A Distributed Fusion Bench", "subject": "Distributed sensor fusion"}, {"id": "JAH-SENFS-000015", "title": "Signature Design Study: An Infrastructure Health Fusion Bench", "subject": "Fusion for infrastructure health monitoring"}, {"id": "JAH-SENFS-000016", "title": "Signature Design Study: A Fusion Architecture Bench", "subject": "Fusion architectures"}, {"id": "JAH-SENFS-000017", "title": "Signature Design Study: An Uncertainty Quantification Bench", "subject": "Uncertainty quantification"}, {"id": "JAH-SENFS-000018", "title": "Signature Design Study: A Fusion Testing Bench", "subject": "Fusion testing and ground truth"}, {"id": "JAH-SENFS-000019", "title": "Signature Design Study: A Real-Time Fusion Bench", "subject": "Real-time fusion systems"}, {"id": "JAH-SENFS-000020", "title": "Signature Design Study: An Environmental Fusion Bench", "subject": "Fusion for environmental monitoring"}, {"id": "JAH-SENFS-000021", "title": "Signature Design Study: An Acoustic Fusion Bench", "subject": "Acoustic sensor fusion"}, {"id": "JAH-SENFS-000022", "title": "Signature Design Study: A Thermal Fusion Bench", "subject": "Thermal and infrared fusion"}, {"id": "JAH-SENFS-000023", "title": "Signature Design Study: A Fusion Standards Bench", "subject": "Fusion data standards and interfaces"}, {"id": "JAH-SENFS-000024", "title": "Signature Design Study: A Fusion Reliability Bench", "subject": "Fusion system reliability"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: sensor-fusion-signature');
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
