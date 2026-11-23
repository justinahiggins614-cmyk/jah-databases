// Demo for the Sensor Fusion Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-SENF-000001", "title": "Sensor Fusion: Overview and Fusion Mission", "subject": "Sensor fusion overview"}, {"id": "JAH-SENF-000002", "title": "Kalman Filtering: The Classic Recursive Estimator", "subject": "Kalman filtering"}, {"id": "JAH-SENF-000003", "title": "Extended and Unscented Kalman Filters: Filtering Nonlinear Motion", "subject": "Extended and unscented Kalman filters"}, {"id": "JAH-SENF-000004", "title": "Particle Filters: Tracking with Many Guesses at Once", "subject": "Particle filters"}, {"id": "JAH-SENF-000005", "title": "Bayesian Fusion: Combining Evidence by the Rules of Probability", "subject": "Bayesian fusion"}, {"id": "JAH-SENF-000006", "title": "Dempster-Shafer Evidence Theory: Fusing Uncertain and Conflicting Reports", "subject": "Dempster-Shafer evidence theory"}, {"id": "JAH-SENF-000007", "title": "Multi-Sensor Calibration: Making Sensors Agree on Reality", "subject": "Multi-sensor calibration"}, {"id": "JAH-SENF-000008", "title": "Time Synchronization: Giving Every Sensor the Same Clock", "subject": "Time synchronization"}, {"id": "JAH-SENF-000009", "title": "Data Association and Tracking: Knowing Which Measurement Belongs to Whom", "subject": "Data association and tracking"}, {"id": "JAH-SENF-000010", "title": "Radar-Lidar Fusion: Combining Radio and Laser Ranging", "subject": "Radar-Lidar fusion"}, {"id": "JAH-SENF-000011", "title": "Camera-Lidar Fusion: Combining Images with Depth", "subject": "Camera-Lidar fusion"}, {"id": "JAH-SENF-000012", "title": "Inertial Navigation Fusion: Dead Reckoning Corrected by Fixes", "subject": "Inertial navigation fusion"}, {"id": "JAH-SENF-000013", "title": "GNSS-Denied Fusion: Navigating Without Satellite Signals", "subject": "GNSS-denied fusion"}, {"id": "JAH-SENF-000014", "title": "Distributed Sensor Fusion: Fusing Across a Network", "subject": "Distributed sensor fusion"}, {"id": "JAH-SENF-000015", "title": "Fusion for Infrastructure Health Monitoring: Listening to Structures", "subject": "Fusion for infrastructure health monitoring"}, {"id": "JAH-SENF-000016", "title": "Fusion Architectures: Centralized, Distributed, and Hybrid Designs", "subject": "Fusion architectures"}, {"id": "JAH-SENF-000017", "title": "Uncertainty Quantification: Saying How Sure a Fused Estimate Is", "subject": "Uncertainty quantification"}, {"id": "JAH-SENF-000018", "title": "Fusion Testing and Ground Truth: How Fused Systems Are Judged", "subject": "Fusion testing and ground truth"}, {"id": "JAH-SENF-000019", "title": "Real-Time Fusion Systems: Fusing Fast Enough to Act", "subject": "Real-time fusion systems"}, {"id": "JAH-SENF-000020", "title": "Fusion for Environmental Monitoring: Reading Land, Water, and Air", "subject": "Fusion for environmental monitoring"}, {"id": "JAH-SENF-000021", "title": "Acoustic Sensor Fusion: Combining Sound from Many Ears", "subject": "Acoustic sensor fusion"}, {"id": "JAH-SENF-000022", "title": "Thermal and Infrared Fusion: Combining Heat Images with Depth", "subject": "Thermal and infrared fusion"}, {"id": "JAH-SENF-000023", "title": "Fusion Data Standards and Interfaces: Making Fused Data Exchangeable", "subject": "Fusion data standards and interfaces"}, {"id": "JAH-SENF-000024", "title": "Fusion System Reliability: Keeping Fused Systems Honest Over Time", "subject": "Fusion system reliability"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: sensor-fusion');
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
