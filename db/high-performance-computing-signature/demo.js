// Demo for the The Signature High-Performance Computing Database database (signature edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-HPCS-000001", "title": "Signature High-Performance Computing Overview Design", "subject": "High-performance computing overview (Signature design-study)"}, {"id": "JAH-HPCS-000002", "title": "Signature Supercomputer Node Design", "subject": "Supercomputer architecture (Signature design-study)"}, {"id": "JAH-HPCS-000003", "title": "Signature Parallel Model Design", "subject": "Parallel computing models (Signature design-study)"}, {"id": "JAH-HPCS-000004", "title": "Signature MPI Library Design", "subject": "Message Passing Interface standard (Signature design-study)"}, {"id": "JAH-HPCS-000005", "title": "Signature OpenMP Runtime Design", "subject": "OpenMP shared-memory parallelism (Signature design-study)"}, {"id": "JAH-HPCS-000006", "title": "Signature Graphics Processing Unit Pod Design", "subject": "Graphics processing unit acceleration (Signature design-study)"}, {"id": "JAH-HPCS-000007", "title": "Signature Interconnect Fabric Design", "subject": "Cluster interconnects (Signature design-study)"}, {"id": "JAH-HPCS-000008", "title": "Signature Parallel Storage Tier Design", "subject": "Parallel file systems (Signature design-study)"}, {"id": "JAH-HPCS-000009", "title": "Signature Scheduler Design", "subject": "Job scheduling (Signature design-study)"}, {"id": "JAH-HPCS-000010", "title": "Signature Benchmark Harness Design", "subject": "Performance benchmarking (Signature design-study)"}, {"id": "JAH-HPCS-000011", "title": "Signature Cooling Loop Design", "subject": "Energy efficiency and cooling (Signature design-study)"}, {"id": "JAH-HPCS-000012", "title": "Signature Checkpoint Vault Design", "subject": "Fault tolerance and checkpointing (Signature design-study)"}, {"id": "JAH-HPCS-000013", "title": "Signature Numerical Library Design", "subject": "Numerical libraries (Signature design-study)"}, {"id": "JAH-HPCS-000014", "title": "Signature Fluid Dynamics Bench Design", "subject": "Computational fluid dynamics workloads (Signature design-study)"}, {"id": "JAH-HPCS-000015", "title": "Signature Climate Bench Design", "subject": "Climate modelling workloads (Signature design-study)"}, {"id": "JAH-HPCS-000016", "title": "Signature Molecular Bench Design", "subject": "Molecular dynamics workloads (Signature design-study)"}, {"id": "JAH-HPCS-000017", "title": "Signature AI Training Rig Design", "subject": "Artificial intelligence training at scale (Signature design-study)"}, {"id": "JAH-HPCS-000018", "title": "Signature Data Lake Design", "subject": "Data-intensive computing (Signature design-study)"}, {"id": "JAH-HPCS-000019", "title": "Signature Hybrid Cloud Bridge Design", "subject": "Cloud HPC and hybrid bursting (Signature design-study)"}, {"id": "JAH-HPCS-000020", "title": "Signature Container Runtime Design", "subject": "Containerised HPC (Signature design-study)"}, {"id": "JAH-HPCS-000021", "title": "Signature Profiler Design", "subject": "Performance profiling and tuning (Signature design-study)"}, {"id": "JAH-HPCS-000022", "title": "Signature Reproducibility Kit Design", "subject": "Reproducibility in HPC (Signature design-study)"}, {"id": "JAH-HPCS-000023", "title": "Signature Acceptance Rig Design", "subject": "Procurement and acceptance testing (Signature design-study)"}, {"id": "JAH-HPCS-000024", "title": "Signature Exascale Roadmap Studio Design", "subject": "Exascale directions (Signature design-study)"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: high-performance-computing-signature');
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
