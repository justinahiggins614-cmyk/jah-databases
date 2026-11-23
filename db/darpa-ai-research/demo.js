// Demo for the DARPA AI Research Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DAIR-000001", "title": "DARPA AI Research: Overview and Research Mission", "subject": "Artificial intelligence research overview"}, {"id": "JAH-DAIR-000002", "title": "Machine Learning Architectures: How Learning Systems Are Built", "subject": "Machine learning architectures"}, {"id": "JAH-DAIR-000003", "title": "Deep Neural Networks: Layered Learning from Data", "subject": "Deep neural networks"}, {"id": "JAH-DAIR-000004", "title": "Reinforcement Learning: Learning from Rewards and Penalties", "subject": "Reinforcement learning"}, {"id": "JAH-DAIR-000005", "title": "Natural Language Understanding: Machines Reading Human Language", "subject": "Natural language understanding"}, {"id": "JAH-DAIR-000006", "title": "Computer Vision Research: Machines Seeing the World", "subject": "Computer vision research"}, {"id": "JAH-DAIR-000007", "title": "Knowledge Representation and Reasoning: Machines That Follow Logic", "subject": "Knowledge representation and reasoning"}, {"id": "JAH-DAIR-000008", "title": "Explainable AI: Showing Why a System Decided", "subject": "Explainable artificial intelligence"}, {"id": "JAH-DAIR-000009", "title": "AI Safety and Alignment Research: Keeping Systems Within Their Mandate", "subject": "AI safety and alignment research"}, {"id": "JAH-DAIR-000010", "title": "Federated Learning: Learning Across Many Holders Without Moving Data", "subject": "Federated learning"}, {"id": "JAH-DAIR-000011", "title": "Transfer Learning: Reusing Knowledge from One Task for Another", "subject": "Transfer learning"}, {"id": "JAH-DAIR-000012", "title": "Generative Models: Systems That Produce New Content", "subject": "Generative models"}, {"id": "JAH-DAIR-000013", "title": "AI Planning and Scheduling: Choosing What to Do and When", "subject": "AI planning and scheduling"}, {"id": "JAH-DAIR-000014", "title": "Human-AI Teaming: People and Systems Working Together", "subject": "Human-AI teaming"}, {"id": "JAH-DAIR-000015", "title": "AI Evaluation and Benchmarking: Judging Systems Fairly", "subject": "AI evaluation and benchmarking"}, {"id": "JAH-DAIR-000016", "title": "Neural Architecture Search: Finding Network Designs Automatically", "subject": "Neural architecture search"}, {"id": "JAH-DAIR-000017", "title": "Probabilistic Reasoning: Deciding Under Uncertainty", "subject": "Probabilistic reasoning"}, {"id": "JAH-DAIR-000018", "title": "Causal Inference: Telling Cause from Correlation", "subject": "Causal inference"}, {"id": "JAH-DAIR-000019", "title": "AI Compute Research: The Hardware Behind Learning", "subject": "AI compute research"}, {"id": "JAH-DAIR-000020", "title": "Data Engineering for AI: Building Trustworthy Training Data", "subject": "Data engineering for AI"}, {"id": "JAH-DAIR-000021", "title": "AI Model Verification: Checking What a Model Actually Does", "subject": "AI model verification"}, {"id": "JAH-DAIR-000022", "title": "Continual Learning: Systems That Keep Learning Without Forgetting", "subject": "Continual learning"}, {"id": "JAH-DAIR-000023", "title": "Multimodal AI: Combining Text, Image, Sound, and Sensor Data", "subject": "Multimodal AI"}, {"id": "JAH-DAIR-000024", "title": "Research Program Management for AI: From Questions to Working Systems", "subject": "Research program management for AI"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: darpa-ai-research');
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
