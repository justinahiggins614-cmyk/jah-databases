// Demo for the The Signature Advanced Navigation Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-ADNAVS-000001", "title": "Signature Advanced Navigation Overview Design", "subject": "Advanced navigation overview (Signature design-study)"}, {"id": "JAH-ADNAVS-000002", "title": "Signature GNSS Receiver Bench Design", "subject": "Global navigation satellite systems (Signature design-study)"}, {"id": "JAH-ADNAVS-000003", "title": "Signature Inertial Unit Design", "subject": "Inertial navigation systems (Signature design-study)"}, {"id": "JAH-ADNAVS-000004", "title": "Signature Kalman Studio Design", "subject": "Kalman filtering for navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000005", "title": "Signature Terrain Matcher Design", "subject": "Terrain-referenced navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000006", "title": "Signature Celestial Tracker Design", "subject": "Celestial navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000007", "title": "Signature Visual Odometry Rig Design", "subject": "Visual odometry and SLAM (Signature design-study)"}, {"id": "JAH-ADNAVS-000008", "title": "Signature Dead-Reckoning Kit Design", "subject": "Dead reckoning (Signature design-study)"}, {"id": "JAH-ADNAVS-000009", "title": "Signature Augmentation Station Design", "subject": "Differential GNSS and augmentation (Signature design-study)"}, {"id": "JAH-ADNAVS-000010", "title": "Signature Signal-Loss Drill Design", "subject": "Resilient positioning under signal loss (Signature design-study)"}, {"id": "JAH-ADNAVS-000011", "title": "Signature Indoor Beacon Mesh Design", "subject": "Indoor positioning (Signature design-study)"}, {"id": "JAH-ADNAVS-000012", "title": "Signature Maritime Plotter Design", "subject": "Maritime navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000013", "title": "Signature Aviation Aid Bench Design", "subject": "Aviation navigation aids (Signature design-study)"}, {"id": "JAH-ADNAVS-000014", "title": "Signature Survey Kit Design", "subject": "Surveying and geodesy (Signature design-study)"}, {"id": "JAH-ADNAVS-000015", "title": "Signature Clock Ensemble Design", "subject": "Time synchronisation (Signature design-study)"}, {"id": "JAH-ADNAVS-000016", "title": "Signature Datum Converter Design", "subject": "Map datums and coordinate systems (Signature design-study)"}, {"id": "JAH-ADNAVS-000017", "title": "Signature Integrity Monitor Design", "subject": "Navigation integrity monitoring (Signature design-study)"}, {"id": "JAH-ADNAVS-000018", "title": "Signature Civilian Vehicle Navigator Design", "subject": "Autonomous vehicle navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000019", "title": "Signature Pedestrian Guide Design", "subject": "Pedestrian navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000020", "title": "Signature Responder Beacon Design", "subject": "Emergency responder navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000021", "title": "Signature Spoof-Detection Lab Design", "subject": "Navigation security, defensive (Signature design-study)"}, {"id": "JAH-ADNAVS-000022", "title": "Signature Standards Desk Design", "subject": "Standards for civilian navigation (Signature design-study)"}, {"id": "JAH-ADNAVS-000023", "title": "Signature Data Format Converter Design", "subject": "Navigation data formats (Signature design-study)"}, {"id": "JAH-ADNAVS-000024", "title": "Signature Resilience Roadmap Design", "subject": "Future resilient navigation (Signature design-study)"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: advanced-navigation-signature');
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
