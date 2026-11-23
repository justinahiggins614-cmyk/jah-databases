// Demo for the Photonic Computing Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. Horizons are PLANNING WINDOWS,
// never predictions. Public records are documented evidence; Signature
// records are design-study, never authentic public record.
const RECORDS = [{"id": "JAH-PHTC-000001", "title": "What Photonic Computing Is", "subject": "photonic computing identity"}, {"id": "JAH-PHTC-000002", "title": "Light as a Computing Medium", "subject": "light as a computing medium"}, {"id": "JAH-PHTC-000003", "title": "Silicon Photonics", "subject": "silicon photonics"}, {"id": "JAH-PHTC-000004", "title": "Photonic Integrated Circuits", "subject": "photonic integrated circuits"}, {"id": "JAH-PHTC-000005", "title": "Optical Neural Networks", "subject": "optical neural networks"}, {"id": "JAH-PHTC-000006", "title": "Mach-Zehnder Interferometers in Computing", "subject": "mach-zehnder interferometers in computing"}, {"id": "JAH-PHTC-000007", "title": "Microring Resonators", "subject": "microring resonators"}, {"id": "JAH-PHTC-000008", "title": "Wavelength-Division Multiplexing for Computing", "subject": "wavelength-division multiplexing for computing"}, {"id": "JAH-PHTC-000009", "title": "Optical Memory and Storage", "subject": "optical memory and storage"}, {"id": "JAH-PHTC-000010", "title": "Photonic Quantum Computing Interfaces", "subject": "photonic quantum computing interfaces"}, {"id": "JAH-PHTC-000011", "title": "Optical Interconnects in Data Centers", "subject": "optical interconnects in data centers"}, {"id": "JAH-PHTC-000012", "title": "Nonlinear Optics for Computation", "subject": "nonlinear optics for computation"}, {"id": "JAH-PHTC-000013", "title": "Photonic Tensor Cores", "subject": "photonic tensor cores"}, {"id": "JAH-PHTC-000014", "title": "Coherent Optical Computing", "subject": "coherent optical computing"}, {"id": "JAH-PHTC-000015", "title": "Photonic Sensors as Computing Inputs", "subject": "photonic sensors as computing inputs"}, {"id": "JAH-PHTC-000016", "title": "Energy Efficiency of Light-Based Computing", "subject": "energy efficiency of light-based computing"}, {"id": "JAH-PHTC-000017", "title": "Fabrication of Photonic Chips", "subject": "fabrication of photonic chips"}, {"id": "JAH-PHTC-000018", "title": "Testing and Validation of Photonic Processors", "subject": "testing and validation of photonic processors"}, {"id": "JAH-PHTC-000019", "title": "Photonic Computing Software and Compilers", "subject": "photonic computing software and compilers"}, {"id": "JAH-PHTC-000020", "title": "Optical Logic Gates", "subject": "optical logic gates"}, {"id": "JAH-PHTC-000021", "title": "Photonic Reservoir Computing", "subject": "photonic reservoir computing"}, {"id": "JAH-PHTC-000022", "title": "Hybrid Electronic-Photonic Systems", "subject": "hybrid electronic-photonic systems"}, {"id": "JAH-PHTC-000023", "title": "Photonic Computing for AI Acceleration", "subject": "photonic computing for AI acceleration"}, {"id": "JAH-PHTC-000024", "title": "Future Expansion: Photonic Research Horizons", "subject": "photonic research horizons"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: photonic-computing');
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
