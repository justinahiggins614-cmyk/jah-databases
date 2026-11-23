// Demo for the Launch Vehicle Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. NASA-level means engineering
// targets modeled on public NASA standards, never NASA certification,
// approval, affiliation, funding, or endorsement. No design here is
// presented as flight-ready. JAH live retrieval was NOT verified.
const RECORDS = [{"id": "JAH-LVEH-000001", "title": "Saturn V Heavy Launch Vehicle", "subject": "Saturn V heavy launch vehicle"}, {"id": "JAH-LVEH-000002", "title": "Space Launch System Block 1", "subject": "Space Launch System Block 1"}, {"id": "JAH-LVEH-000003", "title": "Falcon 9 Reusable Launch Vehicle", "subject": "Falcon 9 reusable launch vehicle"}, {"id": "JAH-LVEH-000004", "title": "Tsiolkovsky Rocket Equation Analysis", "subject": "Tsiolkovsky rocket equation analysis"}, {"id": "JAH-LVEH-000005", "title": "Specific Impulse Performance Analysis", "subject": "Specific impulse performance analysis"}, {"id": "JAH-LVEH-000006", "title": "Multistage Rocket Design", "subject": "Multistage rocket design"}, {"id": "JAH-LVEH-000007", "title": "Launch Vehicle Staging and Separation", "subject": "Launch vehicle staging and separation"}, {"id": "JAH-LVEH-000008", "title": "Launch Vehicle Structural Loads", "subject": "Launch vehicle structural loads"}, {"id": "JAH-LVEH-000009", "title": "Launch Vehicle Guidance and Control", "subject": "Launch vehicle guidance and control"}, {"id": "JAH-LVEH-000010", "title": "Launch Vehicle Propellant Systems", "subject": "Launch vehicle propellant systems"}, {"id": "JAH-LVEH-000011", "title": "Launch Vehicle Engine Cycle Analysis", "subject": "Launch vehicle engine cycle analysis"}, {"id": "JAH-LVEH-000012", "title": "Launch Vehicle Fairing and Payload Adapter", "subject": "Launch vehicle fairing and payload adapter"}, {"id": "JAH-LVEH-000013", "title": "Launch Vehicle Trajectory Design", "subject": "Launch vehicle trajectory design"}, {"id": "JAH-LVEH-000014", "title": "Launch Vehicle Range Safety System", "subject": "Launch vehicle range safety system"}, {"id": "JAH-LVEH-000015", "title": "Launch Vehicle Ground Support Equipment", "subject": "Launch vehicle ground support equipment"}, {"id": "JAH-LVEH-000016", "title": "Launch Vehicle Reusability Design", "subject": "Launch vehicle reusability design"}, {"id": "JAH-LVEH-000017", "title": "Small Launch Vehicle Design", "subject": "Small launch vehicle design"}, {"id": "JAH-LVEH-000018", "title": "Heavy Lift Launch Vehicle Comparison", "subject": "Heavy lift launch vehicle comparison"}, {"id": "JAH-LVEH-000019", "title": "Launch Vehicle Acoustic and Vibration Environment", "subject": "Launch vehicle acoustic and vibration environment"}, {"id": "JAH-LVEH-000020", "title": "Launch Vehicle Mass Fraction Analysis", "subject": "Launch vehicle mass fraction analysis"}, {"id": "JAH-LVEH-000021", "title": "Launch Vehicle Thrust Vector Control", "subject": "Launch vehicle thrust vector control"}, {"id": "JAH-LVEH-000022", "title": "Launch Vehicle Ascent Aerodynamics", "subject": "Launch vehicle ascent aerodynamics"}, {"id": "JAH-LVEH-000023", "title": "Launch Vehicle Orbital Insertion", "subject": "Launch vehicle orbital insertion"}, {"id": "JAH-LVEH-000024", "title": "Launch Vehicle Recovery and Reuse Operations", "subject": "Launch vehicle recovery and reuse operations"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: launch-vehicle');
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
