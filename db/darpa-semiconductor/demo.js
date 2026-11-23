// Demo for the DARPA Semiconductor Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DSEM-000001", "title": "The Transistor and the CMOS Switch: The Unit of Computing", "subject": "the transistor and the CMOS switch"}, {"id": "JAH-DSEM-000002", "title": "Moore's Law and Density Scaling: More Transistors Every Generation", "subject": "Moore's law and density scaling"}, {"id": "JAH-DSEM-000003", "title": "FinFET Transistors: The Fin That Saved Scaling", "subject": "FinFET transistors"}, {"id": "JAH-DSEM-000004", "title": "Gate-All-Around Transistors: The Gate That Wraps Everything", "subject": "gate-all-around transistors"}, {"id": "JAH-DSEM-000005", "title": "Extreme Ultraviolet Lithography: Printing with 13.5 Nanometer Light", "subject": "extreme ultraviolet lithography"}, {"id": "JAH-DSEM-000006", "title": "Deep Ultraviolet Lithography and Multi-Patterning", "subject": "deep ultraviolet lithography and multi-patterning"}, {"id": "JAH-DSEM-000007", "title": "Photolithography and the Mask: The Stencil of Chipmaking", "subject": "photolithography and the mask"}, {"id": "JAH-DSEM-000008", "title": "The Wafer and the Cleanroom: Where Chips Are Born", "subject": "the wafer and the cleanroom"}, {"id": "JAH-DSEM-000009", "title": "Doping and the Junction: Teaching Silicon to Conduct", "subject": "doping and the junction"}, {"id": "JAH-DSEM-000010", "title": "The Fabrication Process Flow: Five Hundred Steps in Order", "subject": "the fabrication process flow"}, {"id": "JAH-DSEM-000011", "title": "Chip Design and Electronic Design Automation", "subject": "chip design and electronic design automation"}, {"id": "JAH-DSEM-000012", "title": "Chiplets and Heterogeneous Integration: Small Chips, One Package", "subject": "chiplets and heterogeneous integration"}, {"id": "JAH-DSEM-000013", "title": "Three-Dimensional Packaging and Through-Silicon Vias", "subject": "three-dimensional packaging and through-silicon vias"}, {"id": "JAH-DSEM-000014", "title": "Memory: DRAM, the Working Memory of Computers", "subject": "memory: DRAM"}, {"id": "JAH-DSEM-000015", "title": "Memory: NAND Flash, the Storage That Remembers", "subject": "memory: NAND flash"}, {"id": "JAH-DSEM-000016", "title": "High-Bandwidth Memory: Stacked Memory for Accelerators", "subject": "high-bandwidth memory"}, {"id": "JAH-DSEM-000017", "title": "Silicon Carbide Power Devices: Power That Runs Hot", "subject": "silicon carbide power devices"}, {"id": "JAH-DSEM-000018", "title": "Gallium Nitride Power Devices: Fast Switching for Small Chargers", "subject": "gallium nitride power devices"}, {"id": "JAH-DSEM-000019", "title": "Interconnects and the Wiring Stack: The Roads of the Chip", "subject": "interconnects and the wiring stack"}, {"id": "JAH-DSEM-000020", "title": "Power Delivery and Thermal Management: Feeding and Cooling the Chip", "subject": "power delivery and thermal management"}, {"id": "JAH-DSEM-000021", "title": "Yield, Defects, and Testing: Finding the Bad Chips", "subject": "yield, defects, and testing"}, {"id": "JAH-DSEM-000022", "title": "RISC-V: The Open Instruction Set Architecture", "subject": "RISC-V open instruction set architecture"}, {"id": "JAH-DSEM-000023", "title": "Analog and Mixed-Signal Circuits: The Bridge to the Real World", "subject": "analog and mixed-signal circuits"}, {"id": "JAH-DSEM-000024", "title": "AI Accelerators and Domain-Specific Chips: Hardware for One Job", "subject": "AI accelerators and domain-specific chips"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: darpa-semiconductor');
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
