// Demo for the Autonomous Systems Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-AUTSYS-000001", "title": "Autonomous Systems: Overview and Autonomy Mission", "subject": "Autonomous systems overview"}, {"id": "JAH-AUTSYS-000002", "title": "Perception and World Modeling: How Machines Understand Surroundings", "subject": "Perception and world modeling"}, {"id": "JAH-AUTSYS-000003", "title": "Path Planning: Finding a Safe Route Through the World", "subject": "Path planning"}, {"id": "JAH-AUTSYS-000004", "title": "Motion Control: Making a Machine Follow Its Plan", "subject": "Motion control"}, {"id": "JAH-AUTSYS-000005", "title": "Localization and Mapping: Knowing Where You Are", "subject": "Localization and mapping"}, {"id": "JAH-AUTSYS-000006", "title": "Decision Making under Uncertainty: Choosing When Facts Are Incomplete", "subject": "Decision making under uncertainty"}, {"id": "JAH-AUTSYS-000007", "title": "Human Supervision and Override: Keeping People in Charge", "subject": "Human supervision and override"}, {"id": "JAH-AUTSYS-000008", "title": "Fleet Coordination: Many Machines Working as One Team", "subject": "Fleet coordination"}, {"id": "JAH-AUTSYS-000009", "title": "Autonomous Ground Vehicles: Civilian Research and Testing", "subject": "Autonomous ground vehicles"}, {"id": "JAH-AUTSYS-000010", "title": "Autonomous Aerial Systems: Civilian Research and Testing", "subject": "Autonomous aerial systems"}, {"id": "JAH-AUTSYS-000011", "title": "Autonomous Maritime Systems: Civilian Research and Testing", "subject": "Autonomous maritime systems"}, {"id": "JAH-AUTSYS-000012", "title": "Autonomous Inspection Systems: Civilian Infrastructure Inspection", "subject": "Autonomous inspection systems"}, {"id": "JAH-AUTSYS-000013", "title": "Fault Detection and Recovery: Surviving Failures Gracefully", "subject": "Fault detection and recovery"}, {"id": "JAH-AUTSYS-000014", "title": "Simulation and Digital Twins for Autonomy: Testing Before Moving", "subject": "Simulation and digital twins for autonomy"}, {"id": "JAH-AUTSYS-000015", "title": "Verification and Validation of Autonomy: Proving Systems Behave", "subject": "Verification and validation of autonomy"}, {"id": "JAH-AUTSYS-000016", "title": "Sensor Integration for Autonomy: Wiring the Senses Together", "subject": "Sensor integration for autonomy"}, {"id": "JAH-AUTSYS-000017", "title": "Energy Management for Autonomous Platforms: Power as a Constraint", "subject": "Energy management for autonomous platforms"}, {"id": "JAH-AUTSYS-000018", "title": "Communications for Autonomous Systems: Staying Connected and Safe", "subject": "Communications for autonomous systems"}, {"id": "JAH-AUTSYS-000019", "title": "Safety Governance for Autonomy: Rules That Keep Systems Accountable", "subject": "Safety governance for autonomy"}, {"id": "JAH-AUTSYS-000020", "title": "Swarm Coordination: Civilian Research in Distributed Control", "subject": "Swarm coordination"}, {"id": "JAH-AUTSYS-000021", "title": "Learning-Based Control: Controllers That Improve from Experience", "subject": "Learning-based control"}, {"id": "JAH-AUTSYS-000022", "title": "Robust Control Theory: Controllers That Survive the Unexpected", "subject": "Robust control theory"}, {"id": "JAH-AUTSYS-000023", "title": "Mission Planning: Turning Objectives into Executable Missions", "subject": "Mission planning"}, {"id": "JAH-AUTSYS-000024", "title": "Autonomy Test Ranges and Evaluation: Proving Grounds for Machines", "subject": "Autonomy test ranges and evaluation"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: autonomous-systems');
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
