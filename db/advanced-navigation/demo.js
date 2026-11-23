// Demo for the Advanced Navigation Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-ADNAV-000001", "title": "Advanced Navigation: Overview and Objective", "subject": "Advanced navigation overview"}, {"id": "JAH-ADNAV-000002", "title": "Global Navigation Satellite Systems", "subject": "Global navigation satellite systems"}, {"id": "JAH-ADNAV-000003", "title": "Inertial Navigation Systems", "subject": "Inertial navigation systems"}, {"id": "JAH-ADNAV-000004", "title": "Kalman Filtering and Sensor Fusion for Navigation", "subject": "Kalman filtering for navigation"}, {"id": "JAH-ADNAV-000005", "title": "Terrain-Referenced Navigation", "subject": "Terrain-referenced navigation"}, {"id": "JAH-ADNAV-000006", "title": "Celestial Navigation, Modernised", "subject": "Celestial navigation"}, {"id": "JAH-ADNAV-000007", "title": "Visual Odometry and Simultaneous Localisation and Mapping", "subject": "Visual odometry and SLAM"}, {"id": "JAH-ADNAV-000008", "title": "Dead Reckoning: The Oldest Method, Kept Honest", "subject": "Dead reckoning"}, {"id": "JAH-ADNAV-000009", "title": "Differential GNSS and Augmentation Systems", "subject": "Differential GNSS and augmentation"}, {"id": "JAH-ADNAV-000010", "title": "Resilient Positioning Under Signal Loss", "subject": "Resilient positioning under signal loss"}, {"id": "JAH-ADNAV-000011", "title": "Indoor Positioning: Finding the Way Inside", "subject": "Indoor positioning"}, {"id": "JAH-ADNAV-000012", "title": "Maritime Navigation: Civilian Ships at Sea", "subject": "Maritime navigation"}, {"id": "JAH-ADNAV-000013", "title": "Aviation Navigation Aids: Civilian Air Navigation", "subject": "Aviation navigation aids"}, {"id": "JAH-ADNAV-000014", "title": "Surveying and Geodesy: Measuring the Earth", "subject": "Surveying and geodesy"}, {"id": "JAH-ADNAV-000015", "title": "Time Synchronisation and Atomic Clocks", "subject": "Time synchronisation"}, {"id": "JAH-ADNAV-000016", "title": "Map Datums and Coordinate Systems", "subject": "Map datums and coordinate systems"}, {"id": "JAH-ADNAV-000017", "title": "Navigation Integrity Monitoring: RAIM and Friends", "subject": "Navigation integrity monitoring"}, {"id": "JAH-ADNAV-000018", "title": "Autonomous Vehicle Navigation: Civilian Research", "subject": "Autonomous vehicle navigation"}, {"id": "JAH-ADNAV-000019", "title": "Pedestrian Navigation: Walking, Indoors and Out", "subject": "Pedestrian navigation"}, {"id": "JAH-ADNAV-000020", "title": "Emergency Responder Navigation", "subject": "Emergency responder navigation"}, {"id": "JAH-ADNAV-000021", "title": "Navigation Security: Defensive Detection of Spoofing", "subject": "Navigation security, defensive"}, {"id": "JAH-ADNAV-000022", "title": "Standards and Certification for Civilian Navigation", "subject": "Standards for civilian navigation"}, {"id": "JAH-ADNAV-000023", "title": "Navigation Data Formats and Interchange", "subject": "Navigation data formats"}, {"id": "JAH-ADNAV-000024", "title": "Future Resilient Navigation: Development Targets", "subject": "Future resilient navigation"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-navigation');
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
