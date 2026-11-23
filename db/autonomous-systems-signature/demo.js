// Demo for the The Signature Autonomous Systems Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-AUTSYSS-000001", "title": "Signature Design Study: An Autonomy Mission Workbench", "subject": "Autonomous systems overview"}, {"id": "JAH-AUTSYSS-000002", "title": "Signature Design Study: A Perception Workbench", "subject": "Perception and world modeling"}, {"id": "JAH-AUTSYSS-000003", "title": "Signature Design Study: A Path Planning Bench", "subject": "Path planning"}, {"id": "JAH-AUTSYSS-000004", "title": "Signature Design Study: A Motion Control Bench", "subject": "Motion control"}, {"id": "JAH-AUTSYSS-000005", "title": "Signature Design Study: A Localization and Mapping Bench", "subject": "Localization and mapping"}, {"id": "JAH-AUTSYSS-000006", "title": "Signature Design Study: A Decision Bench for Uncertain Worlds", "subject": "Decision making under uncertainty"}, {"id": "JAH-AUTSYSS-000007", "title": "Signature Design Study: A Supervision and Override Bench", "subject": "Human supervision and override"}, {"id": "JAH-AUTSYSS-000008", "title": "Signature Design Study: A Fleet Coordination Bench", "subject": "Fleet coordination"}, {"id": "JAH-AUTSYSS-000009", "title": "Signature Design Study: A Ground Vehicle Test Bench", "subject": "Autonomous ground vehicles"}, {"id": "JAH-AUTSYSS-000010", "title": "Signature Design Study: An Aerial System Test Bench", "subject": "Autonomous aerial systems"}, {"id": "JAH-AUTSYSS-000011", "title": "Signature Design Study: A Maritime System Test Bench", "subject": "Autonomous maritime systems"}, {"id": "JAH-AUTSYSS-000012", "title": "Signature Design Study: An Inspection System Bench", "subject": "Autonomous inspection systems"}, {"id": "JAH-AUTSYSS-000013", "title": "Signature Design Study: A Fault Recovery Bench", "subject": "Fault detection and recovery"}, {"id": "JAH-AUTSYSS-000014", "title": "Signature Design Study: A Digital Twin Bench for Autonomy", "subject": "Simulation and digital twins for autonomy"}, {"id": "JAH-AUTSYSS-000015", "title": "Signature Design Study: An Autonomy Verification Bench", "subject": "Verification and validation of autonomy"}, {"id": "JAH-AUTSYSS-000016", "title": "Signature Design Study: A Sensor Integration Bench", "subject": "Sensor integration for autonomy"}, {"id": "JAH-AUTSYSS-000017", "title": "Signature Design Study: An Energy Management Bench", "subject": "Energy management for autonomous platforms"}, {"id": "JAH-AUTSYSS-000018", "title": "Signature Design Study: A Communications Bench for Autonomy", "subject": "Communications for autonomous systems"}, {"id": "JAH-AUTSYSS-000019", "title": "Signature Design Study: A Safety Governance Bench", "subject": "Safety governance for autonomy"}, {"id": "JAH-AUTSYSS-000020", "title": "Signature Design Study: A Swarm Coordination Bench", "subject": "Swarm coordination"}, {"id": "JAH-AUTSYSS-000021", "title": "Signature Design Study: A Learning Control Bench", "subject": "Learning-based control"}, {"id": "JAH-AUTSYSS-000022", "title": "Signature Design Study: A Robust Control Bench", "subject": "Robust control theory"}, {"id": "JAH-AUTSYSS-000023", "title": "Signature Design Study: A Mission Planning Bench", "subject": "Mission planning"}, {"id": "JAH-AUTSYSS-000024", "title": "Signature Design Study: An Autonomy Test Range Bench", "subject": "Autonomy test ranges and evaluation"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: autonomous-systems-signature');
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
