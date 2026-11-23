// Demo for the The Signature Fusion Energy Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-FERS-000001", "title": "A Tabletop Fusion Model", "subject": "tabletop fusion model design"}, {"id": "JAH-FERS-000002", "title": "A D-T Fuel Capsule Design", "subject": "d-t fuel capsule design"}, {"id": "JAH-FERS-000003", "title": "A Lawson Criterion Slide Rule", "subject": "lawson criterion slide rule design"}, {"id": "JAH-FERS-000004", "title": "A Tokamak Control Room Study", "subject": "tokamak control room design"}, {"id": "JAH-FERS-000005", "title": "A Stellarator Coil Workshop", "subject": "stellarator coil workshop design"}, {"id": "JAH-FERS-000006", "title": "An ITER-Scale Q = 10 Demonstrator", "subject": "iter-scale q10 demonstrator design"}, {"id": "JAH-FERS-000007", "title": "A JET-Style D-T Campaign Plan", "subject": "jet-style d-t campaign plan design"}, {"id": "JAH-FERS-000008", "title": "A Laser Pellet Squeeze Simulator", "subject": "laser pellet squeeze simulator design"}, {"id": "JAH-FERS-000009", "title": "A NIF-Style Ignition Exhibit", "subject": "nif-style ignition exhibit design"}, {"id": "JAH-FERS-000010", "title": "A Plasma Stability Feedback Rig", "subject": "plasma stability feedback rig design"}, {"id": "JAH-FERS-000011", "title": "A Three-Heater Plasma Oven", "subject": "three-heater plasma oven design"}, {"id": "JAH-FERS-000012", "title": "A Tritium Breeding Blanket Model", "subject": "tritium breeding blanket model design"}, {"id": "JAH-FERS-000013", "title": "A Neutron Damage Test Garden", "subject": "neutron damage test garden design"}, {"id": "JAH-FERS-000014", "title": "A Superconducting Magnet Winding Hall", "subject": "superconducting magnet winding hall design"}, {"id": "JAH-FERS-000015", "title": "A Fusion Diagnostics Observatory", "subject": "fusion diagnostics observatory design"}, {"id": "JAH-FERS-000016", "title": "A Q-Factor Calculator Exhibit", "subject": "q-factor calculator exhibit design"}, {"id": "JAH-FERS-000017", "title": "A Compact Spherical Tokamak Study", "subject": "compact spherical tokamak study design"}, {"id": "JAH-FERS-000018", "title": "A Private Fusion Pitch Review", "subject": "private fusion pitch review design"}, {"id": "JAH-FERS-000019", "title": "A Fusion Safety Case Template", "subject": "fusion safety case template design"}, {"id": "JAH-FERS-000020", "title": "A Fusion Grid Planning Board", "subject": "fusion grid planning board design"}, {"id": "JAH-FERS-000021", "title": "An Alternative Fuel Test Matrix", "subject": "alternative fuel test matrix design"}, {"id": "JAH-FERS-000022", "title": "A Fusion Simulation Workbench", "subject": "fusion simulation workbench design"}, {"id": "JAH-FERS-000023", "title": "A Fusion Summer School Plan", "subject": "fusion summer school plan design"}, {"id": "JAH-FERS-000024", "title": "A Future Fusion Research Campus", "subject": "future fusion research campus design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: fusion-energy-research-signature');
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
