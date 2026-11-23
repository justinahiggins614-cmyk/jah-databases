// Demo for the The Signature Quantum Computing Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-QCOMPS-000001", "title": "Signature Qubit Lattice Array: A Design-Study Qubit Grid", "subject": "the Signature qubit lattice array design"}, {"id": "JAH-QCOMPS-000002", "title": "Signature Entanglement Switchboard: Routing Linked Qubits", "subject": "the Signature entanglement switchboard design"}, {"id": "JAH-QCOMPS-000003", "title": "Signature Surface-Code Tile: One Logical Qubit, Designed", "subject": "the Signature surface-code tile design"}, {"id": "JAH-QCOMPS-000004", "title": "Signature Cryogenic Control Stack: Wiring the Cold Machine", "subject": "the Signature cryogenic control stack design"}, {"id": "JAH-QCOMPS-000005", "title": "Signature Photonic Interconnect: Light Between Modules", "subject": "the Signature photonic interconnect design"}, {"id": "JAH-QCOMPS-000006", "title": "Signature Trapped-Ion Rail: Moving Ions to Compute", "subject": "the Signature trapped-ion rail design"}, {"id": "JAH-QCOMPS-000007", "title": "Signature Superconducting Resonator Bank: Reading Many Qubits", "subject": "the Signature superconducting resonator bank design"}, {"id": "JAH-QCOMPS-000008", "title": "Signature Quantum Error Budget Tool: Counting Every Error", "subject": "the Signature quantum error budget tool design"}, {"id": "JAH-QCOMPS-000009", "title": "Signature Variational Solver Bench: A Workbench for Hybrid Algorithms", "subject": "the Signature variational solver bench design"}, {"id": "JAH-QCOMPS-000010", "title": "Signature Annealing Scheduler: Planning the Slow Change", "subject": "the Signature annealing scheduler design"}, {"id": "JAH-QCOMPS-000011", "title": "Signature QKD Node: A Design-Study Key Exchange Station", "subject": "the Signature QKD node design"}, {"id": "JAH-QCOMPS-000012", "title": "Signature Quantum Repeater Design: Joining Short Links", "subject": "the Signature quantum repeater design"}, {"id": "JAH-QCOMPS-000013", "title": "Signature Quantum Sensor Array: Many Sensors, One Readout", "subject": "the Signature quantum sensor array design"}, {"id": "JAH-QCOMPS-000014", "title": "Signature Quantum Compiler: From Circuit to Pulses", "subject": "the Signature quantum compiler design"}, {"id": "JAH-QCOMPS-000015", "title": "Signature Quantum Benchmark Harness: Testing Every Machine the Same Way", "subject": "the Signature quantum benchmark harness design"}, {"id": "JAH-QCOMPS-000016", "title": "Signature Neutral-Atom Register: Atoms Arranged to Order", "subject": "the Signature neutral-atom register design"}, {"id": "JAH-QCOMPS-000017", "title": "Signature Silicon Spin Cell: One Qubit in Silicon", "subject": "the Signature silicon spin cell design"}, {"id": "JAH-QCOMPS-000018", "title": "Signature Topological Qubit Study: Protection by Shape", "subject": "the Signature topological qubit study design"}, {"id": "JAH-QCOMPS-000019", "title": "Signature Quantum Memory Cell: Holding a Qubit Still", "subject": "the Signature quantum memory cell design"}, {"id": "JAH-QCOMPS-000020", "title": "Signature Hybrid Classical-Quantum Runner: Two Machines, One Job", "subject": "the Signature hybrid classical-quantum runner design"}, {"id": "JAH-QCOMPS-000021", "title": "Signature Quantum Randomness Beacon: Public Random Numbers", "subject": "the Signature quantum randomness beacon design"}, {"id": "JAH-QCOMPS-000022", "title": "Signature Quantum Chemistry Workbench: Molecules on a Quantum Machine", "subject": "the Signature quantum chemistry workbench design"}, {"id": "JAH-QCOMPS-000023", "title": "Signature Quantum Education Simulator: Learning by Running", "subject": "the Signature quantum education simulator design"}, {"id": "JAH-QCOMPS-000024", "title": "Signature Quantum Verification Ledger: Every Claim Checked", "subject": "the Signature quantum verification ledger design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: quantum-computing-signature');
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
