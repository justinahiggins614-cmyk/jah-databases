// Demo for the The Signature Navigation and Tracking Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-NAVTRS-000001", "title": "Signature Adaptive Kalman Filter Study", "subject": "signature adaptive Kalman filter"}, {"id": "JAH-NAVTRS-000002", "title": "Signature Three-Station Doppler Tracking Study", "subject": "signature three-station Doppler tracking"}, {"id": "JAH-NAVTRS-000003", "title": "Signature Robust Orbit Determination Study", "subject": "signature robust orbit determination"}, {"id": "JAH-NAVTRS-000004", "title": "Signature Multi-Star Attitude Determination Study", "subject": "signature multi-star attitude determination"}, {"id": "JAH-NAVTRS-000005", "title": "Signature Aided Inertial Navigation Study", "subject": "signature aided inertial navigation"}, {"id": "JAH-NAVTRS-000006", "title": "Signature High-Orbit GPS Navigation Study", "subject": "signature high-orbit GPS navigation"}, {"id": "JAH-NAVTRS-000007", "title": "Signature Compressed Element Set Study", "subject": "signature compressed element set"}, {"id": "JAH-NAVTRS-000008", "title": "Signature Autonomous Pass Scheduling Study", "subject": "signature autonomous pass scheduling"}, {"id": "JAH-NAVTRS-000009", "title": "Signature Chip-Scale Atomic Clock Study", "subject": "signature chip-scale atomic clock"}, {"id": "JAH-NAVTRS-000010", "title": "Signature Two-Station Delta-DOR Study", "subject": "signature two-station delta-DOR"}, {"id": "JAH-NAVTRS-000011", "title": "Signature Landmark Navigation Study", "subject": "signature landmark navigation"}, {"id": "JAH-NAVTRS-000012", "title": "Signature Pulsar Navigation Demonstrator Study", "subject": "signature pulsar navigation demonstrator"}, {"id": "JAH-NAVTRS-000013", "title": "Signature Measurement Model Calibration Study", "subject": "signature measurement model calibration"}, {"id": "JAH-NAVTRS-000014", "title": "Signature Small-Antenna Tracking Study", "subject": "signature small-antenna tracking"}, {"id": "JAH-NAVTRS-000015", "title": "Signature Long-Arc Navigation Study", "subject": "signature long-arc navigation"}, {"id": "JAH-NAVTRS-000016", "title": "Signature Tour Navigation Study", "subject": "signature tour navigation"}, {"id": "JAH-NAVTRS-000017", "title": "Signature Halo Orbit Navigation Study", "subject": "signature halo orbit navigation"}, {"id": "JAH-NAVTRS-000018", "title": "Signature Lunar Gravity Navigation Study", "subject": "signature lunar gravity navigation"}, {"id": "JAH-NAVTRS-000019", "title": "Signature Mars Surface Positioning Study", "subject": "signature Mars surface positioning"}, {"id": "JAH-NAVTRS-000020", "title": "Signature Navigation Error Budget Study", "subject": "signature navigation error budget"}, {"id": "JAH-NAVTRS-000021", "title": "Signature Unscented Kalman Filter Study", "subject": "signature unscented Kalman filter"}, {"id": "JAH-NAVTRS-000022", "title": "Signature Sequential Batch Hybrid Study", "subject": "signature sequential batch hybrid"}, {"id": "JAH-NAVTRS-000023", "title": "Signature Conjunction Recovery Study", "subject": "signature conjunction recovery"}, {"id": "JAH-NAVTRS-000024", "title": "Signature Residual Monitoring Study", "subject": "signature residual monitoring"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: navigation-and-tracking-signature');
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
