// Demo for the The Signature Neuromorphic Computing Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-NEUROMS-000001", "title": "Signature Spiking Neuron Cell: One Neuron, Designed", "subject": "the Signature spiking neuron cell design"}, {"id": "JAH-NEUROMS-000002", "title": "Signature Memristor Crossbar: A Grid That Multiplies", "subject": "the Signature memristor crossbar design"}, {"id": "JAH-NEUROMS-000003", "title": "Signature Event Camera Front End: Seeing Only Change", "subject": "the Signature event camera front end design"}, {"id": "JAH-NEUROMS-000004", "title": "Signature Plasticity Engine: Learning on the Chip", "subject": "the Signature plasticity engine design"}, {"id": "JAH-NEUROMS-000005", "title": "Signature Dendrite Array: Branches That Compute", "subject": "the Signature dendrite array design"}, {"id": "JAH-NEUROMS-000006", "title": "Signature Reservoir Core: A Fixed Pool, A Trained Readout", "subject": "the Signature reservoir core design"}, {"id": "JAH-NEUROMS-000007", "title": "Signature Olfactory Chip: Smelling with a Sensor Array", "subject": "the Signature olfactory chip design"}, {"id": "JAH-NEUROMS-000008", "title": "Signature Motor Control Loop: Spikes That Move a Robot", "subject": "the Signature motor control loop design"}, {"id": "JAH-NEUROMS-000009", "title": "Signature Homeostasis Controller: Keeping Rates in Range", "subject": "the Signature homeostasis controller design"}, {"id": "JAH-NEUROMS-000010", "title": "Signature Analog Neuron Tile: A Thousand Neurons in Analog", "subject": "the Signature analog neuron tile design"}, {"id": "JAH-NEUROMS-000011", "title": "Signature Digital Spike Router: Moving Spikes Between Cores", "subject": "the Signature digital spike router design"}, {"id": "JAH-NEUROMS-000012", "title": "Signature Learning Rule Bench: Comparing Five Ways to Learn", "subject": "the Signature learning rule bench design"}, {"id": "JAH-NEUROMS-000013", "title": "Signature Energy Meter: Measuring Every Picojoule", "subject": "the Signature energy meter design"}, {"id": "JAH-NEUROMS-000014", "title": "Signature Benchmark Harness: Testing Every Neuromorphic Machine the Same Way", "subject": "the Signature benchmark harness design"}, {"id": "JAH-NEUROMS-000015", "title": "Signature Hybrid Runner: Spikes and Software, One Job", "subject": "the Signature hybrid runner design"}, {"id": "JAH-NEUROMS-000016", "title": "Signature Phase-Change Synapse: Glass That Learns", "subject": "the Signature phase-change synapse design"}, {"id": "JAH-NEUROMS-000017", "title": "Signature Ferroelectric Synapse: Polarization That Remembers", "subject": "the Signature ferroelectric synapse design"}, {"id": "JAH-NEUROMS-000018", "title": "Signature Vision Pipeline: From Events to Understanding", "subject": "the Signature vision pipeline design"}, {"id": "JAH-NEUROMS-000019", "title": "Signature Audio Spike Front End: Hearing in Spikes", "subject": "the Signature audio spike front end design"}, {"id": "JAH-NEUROMS-000020", "title": "Signature Tactile Skin Array: Touch in Spikes", "subject": "the Signature tactile skin array design"}, {"id": "JAH-NEUROMS-000021", "title": "Signature Memory Consolidation Vault: Keeping What Was Learned", "subject": "the Signature memory consolidation vault design"}, {"id": "JAH-NEUROMS-000022", "title": "Signature Attention Gate: Choosing What to Process", "subject": "the Signature attention gate design"}, {"id": "JAH-NEUROMS-000023", "title": "Signature Sleep Replay Simulator: Learning While Idle", "subject": "the Signature sleep replay simulator design"}, {"id": "JAH-NEUROMS-000024", "title": "Signature Neuromorphic Verification Ledger: Every Claim Checked", "subject": "the Signature neuromorphic verification ledger design"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: neuromorphic-computing-signature');
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
