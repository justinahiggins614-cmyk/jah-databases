(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["gpu-cluster", "interconnect", "cloud-gpu", "planning", "networking", "storage"] */
var CATS=["gpu-cluster", "interconnect", "cloud-gpu", "planning", "networking", "storage"];
var PREFIX='JAH-TRNC-';
var FIELDS=["resource_type", "capacity", "interconnect", "cost_notes"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["gpu-cluster", "NVIDIA DGX H100", "The 8xH100 reference training node: 640 GB HBM3, NVLink fabric, ~32 PFLOPS FP8.", "The DGX H100 packs eight H100 SXM GPUs (80 GB HBM3 each) with NVLink/NVSwitch giving 900 GB/s GPU-to-GPU bandwidth, plus dual CPUs and 2 TB system memory. It delivers about 32 petaFLOPS of FP8 tensor compute per node and is the building block of H100 clusters (DGX SuperPOD scales to thousands). For planners, one DGX H100 is the unit of capacity: training math is usually quoted in 'DGX-days' or 'H100-hours'.", "training node", "8x H100; ~32 PFLOPS FP8; 640 GB HBM3", "NVLink 4.0 / NVSwitch (900 GB/s)", "~$300K+ per system; cloud ~$8/GPU-hr on demand", "python", "DGX-H100 capacity math", "gpus, fp8_per_gpu = 8, 4e15  # ~4 PFLOPS FP8 dense per H100\nprint(f\"node FP8: {gpus*fp8_per_gpu/1e15:.0f} PFLOPS\")\nprint(f\"HBM3: {8*80} GB; NVLink: 900 GB/s all-to-all\")"],
 ["gpu-cluster", "NVIDIA DGX H200", "DGX H100's successor node: 8xH200 with 141 GB HBM3e each — 1.1 TB of GPU memory per node.", "The DGX H200 keeps the 8-GPU DGX form factor but upgrades each GPU to 141 GB of HBM3e (1.1 TB per node) with 4.8 TB/s memory bandwidth per GPU. The extra memory directly extends maximum model size and context length per node before tensor parallelism must span nodes. Compute is similar-class to H100; the win is memory capacity for long-context and large-model training.", "training node", "8x H200; 1.1 TB HBM3e per node", "NVLink 4.0 / NVSwitch", "Premium over H100; cloud ~$10+/GPU-hr", "python", "H200 vs H100 memory", "for name, mem in [(\"H100\", 80), (\"H200\", 141)]:\n    print(f\"{name}: {8*mem} GB/node; 70B fp16 needs {140/(8*mem):.1%} of node\")"],
 ["interconnect", "NVLink / NVSwitch", "NVIDIA's GPU-to-GPU fabric: 900 GB/s per GPU on H100 systems — the fast lane inside the node.", "NVLink connects GPUs directly at 900 GB/s bidirectional per H100 (4th gen), and NVSwitch fabrics let all 8 GPUs in a node talk all-to-all at full speed. This is what makes tensor parallelism practical: sharded layers exchange activations every step without touching the slower network. Between nodes, traffic moves to InfiniBand or Ethernet — the NVLink domain ends at the node boundary, which is why parallelism strategies are designed around it.", "interconnect", "900 GB/s per GPU (NVLink 4.0); 7.2 TB/s bisection per node", "On-package/board fabric (intra-node)", "Included in DGX/node price; NVL72 extends domain to rack", "python", "All-reduce time on NVLink", "size_gb, bw_gbs = 80, 900  # one H100's gradients\n# ring all-reduce ~ 2*(n-1)/n * size / bw\nt = 2 * 7/8 * size_gb / bw_gbs\nprint(f\"80GB all-reduce over NVLink: {t*1000:.0f} ms\")"],
 ["interconnect", "InfiniBand NDR", "400 Gb/s per port fabric for inter-node training traffic — the standard for large GPU clusters.", "InfiniBand NDR runs 400 Gb/s per port (with 800 Gb/s XDR arriving), with RDMA and adaptive routing that keep all-reduce collectives fast across thousands of GPUs. NCCL is tuned for it, and 'rail-optimized' topologies give each GPU a dedicated rail to its peers. For clusters above ~64 GPUs, InfiniBand (or high-end RoCE Ethernet) is effectively mandatory — training throughput collapses on oversubscribed networks.", "interconnect", "400 Gb/s per port (NDR); 800 Gb/s (XDR)", "Inter-node fabric", "~$1-2K per port incl. cables/switches amortized", "python", "Inter-node all-reduce estimate", "size_gb, bw_gbs, gpus = 80, 50, 256  # 400Gb/s = 50 GB/s\nt = 2 * (gpus-1)/gpus * size_gb / bw_gbs\nprint(f\"80GB all-reduce, 256 GPUs, NDR: {t:.1f} s\")"],
 ["cloud-gpu", "AWS EC2 P5 Instances", "AWS's 8xH100 cloud instances with EFA networking — on-demand H100s without buying hardware.", "EC2 P5 instances provide 8 H100 GPUs, 3.2 Tb/s EFA (Elastic Fabric Adapter) networking, and up to 3200 Gbps aggregate network bandwidth per instance. P5en adds newer networking; P6 (B200) is the next step. Pricing is on-demand (~$100+/hr per instance), reserved, or spot — spot P5 can be 60-70% cheaper but preemptible. HyperPod adds Slurm-managed cluster orchestration for multi-hundred-GPU runs.", "cloud GPU", "8x H100 per instance; scales to 1000s via HyperPod", "EFA (3.2 Tb/s per instance)", "~$98/hr on-demand per p5.48xlarge; spot much cheaper", "shell", "Launch a P5 spot fleet (AWS CLI)", "aws ec2 request-spot-instances \\\n  --instance-type p5.48xlarge \\\n  --spot-price \"30.00\" \\\n  --launch-specification '{\"ImageId\":\"ami-0abc\",\"KeyName\":\"train-key\"}'"],
 ["cloud-gpu", "Google Cloud A3 Instances", "GCP's 8xH100 VMs with GPUDirect-TCPX — Google's on-ramp to H100 training.", "GCE A3 VMs offer 8 H100 80GB GPUs with NVIDIA GPUDirect-TCPX networking for efficient multi-node collectives, plus local NVMe. A3 Mega doubles the network bandwidth for large runs. Google pairs them with GKE for Kubernetes-native training or managed Vertex AI Training. Committed-use discounts cut ~40% off on-demand for steady workloads.", "cloud GPU", "8x H100 per VM; A3 Mega for large runs", "GPUDirect-TCPX", "On-demand ~$100/hr; committed-use ~-40%", "python", "Committed-use savings", "ondemand, hours = 100, 24*30\nfor disc, name in [(0, \"on-demand\"), (0.4, \"1-yr commit\"), (0.6, \"3-yr commit\")]:\n    print(f\"{name:12s}: ${ondemand*(1-disc)*hours:,.0f}/mo\")"],
 ["cloud-gpu", "Azure ND H100 v5", "Azure's 8xH100 VMs on InfiniBand NDR — Microsoft's flagship training SKU.", "Azure ND H100 v5 VMs pack 8 H100s with 400 Gb/s InfiniBand NDR per GPU via 8 ConnectX-7 NICs — one of the strongest per-GPU network ratios in the cloud. They underpin Azure's OpenAI supercomputing partnership and are available in NDv5 clusters for large runs. Azure ML provides the managed training layer; low-priority/spot VMs offer deep discounts for fault-tolerant workloads.", "cloud GPU", "8x H100; 400 Gb/s IB per GPU", "InfiniBand NDR (8x CX-7)", "On-demand high; spot/low-priority much cheaper", "python", "Per-GPU network ratio", "print(\"NDv5: 400 Gb/s per GPU =\", 400/8, \"Gb/s per H100 vs\")\nprint(\"typical: 200-400 Gb/s shared per node\")"],
 ["cloud-gpu", "Lambda Labs GPU Cloud", "Developer-friendly H100/A100 cloud with simple pricing — popular with startups and researchers.", "Lambda Labs offers on-demand and reserved H100, H200, A100, and GH200 instances with straightforward hourly pricing and no hyperscaler complexity. Their 1-click clusters provide multi-node setups with InfiniBand-class networking. Pricing has historically undercut the big three clouds, making Lambda a favorite for fine-tuning and mid-size training runs.", "cloud GPU", "H100/H200/A100/GH200; 1-click clusters", "InfiniBand-class inter-node", "H100 ~$2.5-4/GPU-hr on demand (varies)", "shell", "SSH to a Lambda instance", "ssh ubuntu@<instance-ip>\nnvidia-smi  # verify 8x H100\n# then: torchrun --nproc_per_node=8 train.py"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,title:b[1],t:b[1],g:cat,c:1,summary:b[2],details:b[3]};
  for(var i=0;i<FIELDS.length;i++){rec[FIELDS[i]]=b[4+i];}
  var di=4+FIELDS.length;
  rec.ladder_rank=1+(seed%3);
  rec.demo={language:b[di],title:b[di+1],program:b[di+2]};
  rec.provenance="JAH Databases generator (archive-style records)";
  rec.last_verified='2026-10-20';
  rec.src="public-harvest";
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||!r.summary.length)e.push('summary');
  if(typeof r.details!=='string'||!r.details.length)e.push('details');
  if(CATS.indexOf(r.g)<0)e.push('g');
  for(var i=0;i<FIELDS.length;i++){
    var v=r[FIELDS[i]];
    if(v===undefined||v===null||(typeof v==='string'&&!v.length))e.push('field:'+FIELDS[i]);
  }
  if(!(r.ladder_rank===1||r.ladder_rank===2||r.ladder_rank===3))e.push('ladder_rank');
  var d=r.demo;
  if(!d||typeof d.language!=='string'||!d.language.length||typeof d.title!=='string'||!d.title.length||typeof d.program!=='string'||!d.program.length)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-20')e.push('last_verified');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ai-training-compute-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-training-compute',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
