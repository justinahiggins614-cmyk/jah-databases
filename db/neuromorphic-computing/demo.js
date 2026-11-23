// Demo for the Neuromorphic Computing Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-NEUROM-000001", "title": "Neuromorphic Computing Foundations: Brains as the Blueprint", "subject": "neuromorphic computing foundations"}, {"id": "JAH-NEUROM-000002", "title": "Spiking Neural Networks: Computing with Spikes", "subject": "spiking neural networks"}, {"id": "JAH-NEUROM-000003", "title": "The Leaky Integrate-and-Fire Neuron: The Standard Model", "subject": "the leaky integrate-and-fire neuron"}, {"id": "JAH-NEUROM-000004", "title": "Spike-Timing-Dependent Plasticity: Learning from Timing", "subject": "spike-timing-dependent plasticity"}, {"id": "JAH-NEUROM-000005", "title": "The Memristor as Artificial Synapse: Memory That Learns", "subject": "the memristor as artificial synapse"}, {"id": "JAH-NEUROM-000006", "title": "Crossbar Arrays and In-Memory Computing: Math Where the Data Lives", "subject": "crossbar arrays and in-memory computing"}, {"id": "JAH-NEUROM-000007", "title": "Event-Driven Sensing and the Dynamic Vision Sensor", "subject": "event-driven sensing and the dynamic vision sensor"}, {"id": "JAH-NEUROM-000008", "title": "Intel Loihi: A Research Chip for Spiking Networks", "subject": "Intel Loihi"}, {"id": "JAH-NEUROM-000009", "title": "IBM TrueNorth: A Million Neurons on One Chip", "subject": "IBM TrueNorth"}, {"id": "JAH-NEUROM-000010", "title": "SpiNNaker: A Million Cores Simulating Spikes", "subject": "SpiNNaker"}, {"id": "JAH-NEUROM-000011", "title": "BrainScaleS: Analog Neurons at Biological Speed", "subject": "BrainScaleS"}, {"id": "JAH-NEUROM-000012", "title": "Analog Neuromorphic Circuits: Neurons in Silicon, Directly", "subject": "analog neuromorphic circuits"}, {"id": "JAH-NEUROM-000013", "title": "Digital Neuromorphic Architectures: Spikes in Logic", "subject": "digital neuromorphic architectures"}, {"id": "JAH-NEUROM-000014", "title": "Dendritic Computation: The Branches That Compute", "subject": "dendritic computation"}, {"id": "JAH-NEUROM-000015", "title": "Reservoir Computing: A Rich Pool, A Simple Readout", "subject": "reservoir computing"}, {"id": "JAH-NEUROM-000016", "title": "Homeostatic Plasticity and Stability: Keeping the Network in Range", "subject": "homeostatic plasticity and stability"}, {"id": "JAH-NEUROM-000017", "title": "Neuromorphic Learning Rules: How the Hardware Learns", "subject": "neuromorphic learning rules"}, {"id": "JAH-NEUROM-000018", "title": "Neuromorphic Software Frameworks: Programming the Spiking Machine", "subject": "neuromorphic software frameworks"}, {"id": "JAH-NEUROM-000019", "title": "Neuromorphic Benchmarking: Measuring the Brain-Inspired Machine", "subject": "neuromorphic benchmarking"}, {"id": "JAH-NEUROM-000020", "title": "Energy Efficiency of Brain-Inspired Computing: Watts That Matter", "subject": "energy efficiency of brain-inspired computing"}, {"id": "JAH-NEUROM-000021", "title": "Neuromorphic Olfaction and Chemical Sensing: Smelling with Spikes", "subject": "neuromorphic olfaction and chemical sensing"}, {"id": "JAH-NEUROM-000022", "title": "Neuromorphic Motor Control and Robotics: Moving with Spikes", "subject": "neuromorphic motor control and robotics"}, {"id": "JAH-NEUROM-000023", "title": "Phase-Change Memory Synapses: Glass That Remembers", "subject": "phase-change memory synapses"}, {"id": "JAH-NEUROM-000024", "title": "Hybrid Neuromorphic-Classical Systems: Two Kinds of Computer, One Job", "subject": "hybrid neuromorphic-classical systems"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: neuromorphic-computing');
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
