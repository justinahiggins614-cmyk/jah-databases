// Demo for the The Signature Spacecraft Engineering Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-SCENS-000001", "title": "Signature Modular Spacecraft Bus", "subject": "Signature modular spacecraft bus"}, {"id": "JAH-SCENS-000002", "title": "Signature Deployable Truss Structure", "subject": "Signature deployable truss structure"}, {"id": "JAH-SCENS-000003", "title": "Signature Radiator Thermal System", "subject": "Signature radiator thermal system"}, {"id": "JAH-SCENS-000004", "title": "Signature High-Power Solar Array", "subject": "Signature high-power solar array"}, {"id": "JAH-SCENS-000005", "title": "Signature Precision Pointing Platform", "subject": "Signature precision pointing platform"}, {"id": "JAH-SCENS-000006", "title": "Signature Control Moment Gyroscope Assembly", "subject": "Signature control moment gyroscope assembly"}, {"id": "JAH-SCENS-000007", "title": "Signature Deep Space Antenna", "subject": "Signature deep space antenna"}, {"id": "JAH-SCENS-000008", "title": "Signature Electric Propulsion Module", "subject": "Signature electric propulsion module"}, {"id": "JAH-SCENS-000009", "title": "Signature Autonomous Fault Manager", "subject": "Signature autonomous fault manager"}, {"id": "JAH-SCENS-000010", "title": "Signature Inflatable Habitat Module", "subject": "Signature inflatable habitat module"}, {"id": "JAH-SCENS-000011", "title": "Signature Regolith Shielding Panel", "subject": "Signature regolith shielding panel"}, {"id": "JAH-SCENS-000012", "title": "Signature Cryogenic Tank Structure", "subject": "Signature cryogenic tank structure"}, {"id": "JAH-SCENS-000013", "title": "Signature Laser Communication Terminal", "subject": "Signature laser communication terminal"}, {"id": "JAH-SCENS-000014", "title": "Signature Radiation-Tolerant Computer", "subject": "Signature radiation-tolerant computer"}, {"id": "JAH-SCENS-000015", "title": "Signature Docking and Berthing System", "subject": "Signature docking and berthing system"}, {"id": "JAH-SCENS-000016", "title": "Signature Sample Handling Mechanism", "subject": "Signature sample handling mechanism"}, {"id": "JAH-SCENS-000017", "title": "Signature Deployable Solar Sail", "subject": "Signature deployable solar sail"}, {"id": "JAH-SCENS-000018", "title": "Signature Aerocapture Heat Shield", "subject": "Signature aerocapture heat shield"}, {"id": "JAH-SCENS-000019", "title": "Signature Lunar Lander Leg Assembly", "subject": "Signature lunar lander leg assembly"}, {"id": "JAH-SCENS-000020", "title": "Signature Rover Chassis Design", "subject": "Signature rover chassis design"}, {"id": "JAH-SCENS-000021", "title": "Signature In-Situ Resource Plant Structure", "subject": "Signature in-situ resource plant structure"}, {"id": "JAH-SCENS-000022", "title": "Signature Crew Transfer Vehicle", "subject": "Signature crew transfer vehicle"}, {"id": "JAH-SCENS-000023", "title": "Signature Orbital Assembly Jig", "subject": "Signature orbital assembly jig"}, {"id": "JAH-SCENS-000024", "title": "Signature Long-Duration Storage Module", "subject": "Signature long-duration storage module"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: spacecraft-engineering-signature');
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
