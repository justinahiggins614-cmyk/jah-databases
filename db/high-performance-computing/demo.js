// Demo for the High-Performance Computing Database database (public edition).
// Searches the edition's real 24 records and runs a deterministic
// generator demo (seed 7) over them. Node only, no dependencies.
// PACKAGE-ONLY: nothing here is live. DARPA-grade is never a claim of
// DARPA approval, certification, funding, or endorsement.
const RECORDS = [{"id": "JAH-HPC-000001", "title": "High-Performance Computing: Overview and Objective", "subject": "High-performance computing overview"}, {"id": "JAH-HPC-000002", "title": "Supercomputer Architecture: Nodes, Memory, and Interconnects", "subject": "Supercomputer architecture"}, {"id": "JAH-HPC-000003", "title": "Parallel Computing Models: Shared Memory, Distributed Memory, and Hybrid", "subject": "Parallel computing models"}, {"id": "JAH-HPC-000004", "title": "Message Passing Interface: The MPI Standard for Distributed Programs", "subject": "Message Passing Interface standard"}, {"id": "JAH-HPC-000005", "title": "OpenMP: Shared-Memory Parallelism Inside One Node", "subject": "OpenMP shared-memory parallelism"}, {"id": "JAH-HPC-000006", "title": "Graphics Processing Unit Acceleration for HPC", "subject": "Graphics processing unit acceleration"}, {"id": "JAH-HPC-000007", "title": "Cluster Interconnects: Networks That Join Thousands of Nodes", "subject": "Cluster interconnects"}, {"id": "JAH-HPC-000008", "title": "Parallel File Systems and High-Speed Storage", "subject": "Parallel file systems"}, {"id": "JAH-HPC-000009", "title": "Job Scheduling and Resource Management", "subject": "Job scheduling"}, {"id": "JAH-HPC-000010", "title": "Performance Benchmarking: LINPACK and the TOP500 Method", "subject": "Performance benchmarking"}, {"id": "JAH-HPC-000011", "title": "Energy Efficiency and Cooling for Large Clusters", "subject": "Energy efficiency and cooling"}, {"id": "JAH-HPC-000012", "title": "Fault Tolerance and Checkpointing", "subject": "Fault tolerance and checkpointing"}, {"id": "JAH-HPC-000013", "title": "Numerical Libraries: BLAS, LAPACK, and Friends", "subject": "Numerical libraries"}, {"id": "JAH-HPC-000014", "title": "Computational Fluid Dynamics Workloads", "subject": "Computational fluid dynamics workloads"}, {"id": "JAH-HPC-000015", "title": "Climate Modelling Workloads", "subject": "Climate modelling workloads"}, {"id": "JAH-HPC-000016", "title": "Molecular Dynamics Workloads", "subject": "Molecular dynamics workloads"}, {"id": "JAH-HPC-000017", "title": "Artificial Intelligence Training at Scale", "subject": "Artificial intelligence training at scale"}, {"id": "JAH-HPC-000018", "title": "Data-Intensive Computing and MapReduce", "subject": "Data-intensive computing"}, {"id": "JAH-HPC-000019", "title": "Cloud HPC and Hybrid Bursting", "subject": "Cloud HPC and hybrid bursting"}, {"id": "JAH-HPC-000020", "title": "Containerised HPC: Reproducible Software Environments", "subject": "Containerised HPC"}, {"id": "JAH-HPC-000021", "title": "Performance Profiling and Tuning", "subject": "Performance profiling and tuning"}, {"id": "JAH-HPC-000022", "title": "Reproducibility in HPC: Same Input, Same Answer", "subject": "Reproducibility in HPC"}, {"id": "JAH-HPC-000023", "title": "Procurement and Acceptance Testing for Clusters", "subject": "Procurement and acceptance testing"}, {"id": "JAH-HPC-000024", "title": "Exascale Directions: Development Targets, Not Achievements", "subject": "Exascale directions"}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function search(q){const s=q.toLowerCase();return RECORDS.filter(r=>(r.title+' '+r.subject).toLowerCase().includes(s));}
function titleChecksum(){let h=0;for(const r of RECORDS){for(const ch of r.title){h=(h*31+ch.charCodeAt(0))>>>0;}}return h;}
function main(){
  console.log('DATABASE: high-performance-computing');
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
