// Demo for the The Signature DARPA AI Research Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-DAIRS-000001", "title": "Signature Design Study: An AI Research Workbench", "subject": "Artificial intelligence research overview"}, {"id": "JAH-DAIRS-000002", "title": "Signature Design Study: A Modular Learning Architecture", "subject": "Machine learning architectures"}, {"id": "JAH-DAIRS-000003", "title": "Signature Design Study: A Layered Network Workbench", "subject": "Deep neural networks"}, {"id": "JAH-DAIRS-000004", "title": "Signature Design Study: A Reward-Learning Sandbox", "subject": "Reinforcement learning"}, {"id": "JAH-DAIRS-000005", "title": "Signature Design Study: A Language Understanding Bench", "subject": "Natural language understanding"}, {"id": "JAH-DAIRS-000006", "title": "Signature Design Study: A Vision Research Bench", "subject": "Computer vision research"}, {"id": "JAH-DAIRS-000007", "title": "Signature Design Study: A Reasoning Graph Workbench", "subject": "Knowledge representation and reasoning"}, {"id": "JAH-DAIRS-000008", "title": "Signature Design Study: An Explanation Workbench", "subject": "Explainable artificial intelligence"}, {"id": "JAH-DAIRS-000009", "title": "Signature Design Study: A Safety Review Workbench", "subject": "AI safety and alignment research"}, {"id": "JAH-DAIRS-000010", "title": "Signature Design Study: A Federated Learning Workbench", "subject": "Federated learning"}, {"id": "JAH-DAIRS-000011", "title": "Signature Design Study: A Transfer Learning Bench", "subject": "Transfer learning"}, {"id": "JAH-DAIRS-000012", "title": "Signature Design Study: A Generative Model Workbench", "subject": "Generative models"}, {"id": "JAH-DAIRS-000013", "title": "Signature Design Study: A Planning and Scheduling Bench", "subject": "AI planning and scheduling"}, {"id": "JAH-DAIRS-000014", "title": "Signature Design Study: A Human-AI Teaming Workbench", "subject": "Human-AI teaming"}, {"id": "JAH-DAIRS-000015", "title": "Signature Design Study: An Evaluation Workbench", "subject": "AI evaluation and benchmarking"}, {"id": "JAH-DAIRS-000016", "title": "Signature Design Study: An Architecture Search Bench", "subject": "Neural architecture search"}, {"id": "JAH-DAIRS-000017", "title": "Signature Design Study: A Probabilistic Reasoning Bench", "subject": "Probabilistic reasoning"}, {"id": "JAH-DAIRS-000018", "title": "Signature Design Study: A Causal Inference Bench", "subject": "Causal inference"}, {"id": "JAH-DAIRS-000019", "title": "Signature Design Study: A Compute Research Bench", "subject": "AI compute research"}, {"id": "JAH-DAIRS-000020", "title": "Signature Design Study: A Data Engineering Bench", "subject": "Data engineering for AI"}, {"id": "JAH-DAIRS-000021", "title": "Signature Design Study: A Model Verification Bench", "subject": "AI model verification"}, {"id": "JAH-DAIRS-000022", "title": "Signature Design Study: A Continual Learning Bench", "subject": "Continual learning"}, {"id": "JAH-DAIRS-000023", "title": "Signature Design Study: A Multimodal AI Bench", "subject": "Multimodal AI"}, {"id": "JAH-DAIRS-000024", "title": "Signature Design Study: An AI Program Management Bench", "subject": "Research program management for AI"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: darpa-ai-research-signature');
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
