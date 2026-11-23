// Demo for the The Signature DARPA Semiconductor Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DSEMS-000001", "title": "Signature FinFET Cell Library: A Design-Study Transistor Set", "subject": "the Signature FinFET cell library design"}, {"id": "JAH-DSEMS-000002", "title": "Signature Gate-All-Around Test Structure: Measuring the New Transistor", "subject": "the Signature gate-all-around test structure design"}, {"id": "JAH-DSEMS-000003", "title": "Signature EUV Mask Inspection Bench: Checking the Stencil", "subject": "the Signature EUV mask inspection bench design"}, {"id": "JAH-DSEMS-000004", "title": "Signature Chiplet Interposer: The Floor Between Chiplets", "subject": "the Signature chiplet interposer design"}, {"id": "JAH-DSEMS-000005", "title": "Signature Three-Dimensional Stack: Four Dies, One Package", "subject": "the Signature three-dimensional stack design"}, {"id": "JAH-DSEMS-000006", "title": "Signature Silicon Carbide Inverter: Power for an Electric Vehicle", "subject": "the Signature silicon carbide inverter design"}, {"id": "JAH-DSEMS-000007", "title": "Signature Gallium Nitride Charger: Small Power for a Laptop", "subject": "the Signature gallium nitride charger design"}, {"id": "JAH-DSEMS-000008", "title": "Signature High-Bandwidth Memory Cube: Stacked Memory, Designed", "subject": "the Signature high-bandwidth memory cube design"}, {"id": "JAH-DSEMS-000009", "title": "Signature RISC-V Core: An Open Processor, Designed", "subject": "the Signature RISC-V core design"}, {"id": "JAH-DSEMS-000010", "title": "Signature Analog Front End: Listening to the Real World", "subject": "the Signature analog front end design"}, {"id": "JAH-DSEMS-000011", "title": "Signature AI Accelerator Tile: One Tile of Matrix Arithmetic", "subject": "the Signature AI accelerator tile design"}, {"id": "JAH-DSEMS-000012", "title": "Signature Wafer Map Analyzer: Reading the Yield Map", "subject": "the Signature wafer map analyzer design"}, {"id": "JAH-DSEMS-000013", "title": "Signature Yield Learning Loop: Improving the Process, One Wafer at a Time", "subject": "the Signature yield learning loop design"}, {"id": "JAH-DSEMS-000014", "title": "Signature Thermal Spreader: Moving Heat Off the Die", "subject": "the Signature thermal spreader design"}, {"id": "JAH-DSEMS-000015", "title": "Signature Power Delivery Network: Feeding Every Transistor", "subject": "the Signature power delivery network design"}, {"id": "JAH-DSEMS-000016", "title": "Signature Interconnect Planner: Drawing the Wires Before They Exist", "subject": "the Signature interconnect planner design"}, {"id": "JAH-DSEMS-000017", "title": "Signature Cleanroom Monitor: Watching the Air the Chips Breathe", "subject": "the Signature cleanroom monitor design"}, {"id": "JAH-DSEMS-000018", "title": "Signature Doping Profile Simulator: Predicting the Junction", "subject": "the Signature doping profile simulator design"}, {"id": "JAH-DSEMS-000019", "title": "Signature Test Pattern Generator: Catching Faults Before Shipping", "subject": "the Signature test pattern generator design"}, {"id": "JAH-DSEMS-000020", "title": "Signature Packaging Lab: The Last Step Before the Customer", "subject": "the Signature packaging lab design"}, {"id": "JAH-DSEMS-000021", "title": "Signature Photonic-Electronic Bridge: Light Meets the Chip", "subject": "the Signature photonic-electronic bridge design"}, {"id": "JAH-DSEMS-000022", "title": "Signature Cryogenic Control Chip: Electronics That Work in the Cold", "subject": "the Signature cryogenic control chip design"}, {"id": "JAH-DSEMS-000023", "title": "Signature Radiation-Hardened Cell: A Transistor That Survives Space", "subject": "the Signature radiation-hardened cell design"}, {"id": "JAH-DSEMS-000024", "title": "Signature Chip Security Root: Trust Anchored in Silicon", "subject": "the Signature chip security root design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: darpa-semiconductor-signature');
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
