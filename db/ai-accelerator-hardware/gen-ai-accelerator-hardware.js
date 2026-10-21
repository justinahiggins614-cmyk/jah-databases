(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["nvidia", "amd", "google-tpu", "cloud-asic", "startup-chip", "edge-npu"] */
var CATS=["nvidia", "amd", "google-tpu", "cloud-asic", "startup-chip", "edge-npu"];
var PREFIX='JAH-AIACC-';
var FIELDS=["vendor", "memory", "throughput", "process_power", "form_factor"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["nvidia", "NVIDIA H100 SXM", "The datacenter workhorse: 80 GB HBM3, ~989 TFLOPS BF16 dense, 4th-gen Tensor Cores.", "The H100 SXM (Hopper) delivers about 989 TFLOPS of BF16 dense compute (nearly 2 PFLOPS with FP8), 80 GB of HBM3 at 3 TB/s, and 900 GB/s NVLink. It trained most frontier models of 2023-2025 and remains the reference GPU for training economics. The PCIe variant trades some bandwidth for server compatibility. Fourth-gen Tensor Cores add the Transformer Engine with automatic FP8 mixed precision.", "NVIDIA", "80 GB HBM3; 3 TB/s", "~989 TFLOPS BF16 dense; ~2 PFLOPS FP8", "4nm; 700W SXM", "SXM5 / PCIe", "python", "H100 training throughput", "tflops, mfu = 989, 0.45\nprint(f\"effective: {tflops*mfu:.0f} TFLOPS/GPU\")\nprint(f\"8-GPU node: {8*tflops*mfu/1000:.1f} PFLOPS effective\")"],
 ["nvidia", "NVIDIA H200", "H100-class compute with 141 GB HBM3e — the memory-capacity upgrade for long context.", "The H200 keeps Hopper compute but upgrades memory to 141 GB of HBM3e at 4.8 TB/s — 76% more capacity and 43% more bandwidth than H100. For inference, that means longer contexts and bigger batches per GPU; for training, larger models per node. It slots into existing HGX H100 systems, making it a drop-in upgrade path.", "NVIDIA", "141 GB HBM3e; 4.8 TB/s", "~989 TFLOPS BF16 dense", "4nm; ~700W", "SXM / HGX board", "python", "H200 context capacity", "mem_gb, per_token_kb = 141, 1.0  # ~1MB/token for 70B-ish KV\nprint(f\"max KV tokens: {mem_gb*1e6/per_token_kb/1e6:.1f}M tokens (rough)\")"],
 ["nvidia", "NVIDIA B200", "Blackwell flagship: 192 GB HBM3e, ~2.2 PFLOPS BF16 dense, 5th-gen Tensor Cores with FP4.", "The B200 (Blackwell) roughly doubles H100 training throughput: ~2.2 PFLOPS BF16 dense, 192 GB HBM3e at 8 TB/s, and new FP4 precision for inference. Two B200 dies are co-packaged per GPU. It anchors the GB200 NVL72 rack systems and DGX B200 nodes — the platform for 2025-era frontier training.", "NVIDIA", "192 GB HBM3e; 8 TB/s", "~2.2 PFLOPS BF16 dense; ~4.5 PFLOPS FP4", "4nm-class; ~1000W", "SXM / NVL72 rack", "python", "B200 vs H100", "for name, tflops in [(\"H100\", 989), (\"B200\", 2250)]:\n    print(f\"{name}: {tflops} TFLOPS BF16\")"],
 ["nvidia", "NVIDIA GB200 NVL72", "A full rack as one GPU: 72 B200s with NVLink-domain memory pooling — 130 TB/s fabric.", "The GB200 NVL72 connects 72 Blackwell GPUs (36 Grace CPU + 72 GPU 'superchips') in a single NVLink domain with 130 TB/s aggregate bandwidth, presenting as one giant accelerator with ~13.5 TB of pooled HBM3e. It enables trillion-parameter MoE inference in one rack and 30x faster real-time inference claims versus H100 systems on certain workloads. This is rack-scale computing: the unit is the rack, not the card.", "NVIDIA", "~13.5 TB pooled HBM3e", "~1.4 exaFLOPS FP4 (rack)", "~120 kW per rack (liquid-cooled)", "Full liquid-cooled rack", "python", "NVL72 pooled memory", "gpus, mem = 72, 192\nprint(f\"pooled: {gpus*mem/1024:.1f} TB HBM3e in one NVLink domain\")"],
 ["nvidia", "NVIDIA A100", "The previous-gen workhorse: 40/80 GB HBM2e, still everywhere in research and inference.", "The A100 (Ampere) delivers 312 TFLOPS BF16 dense with 40 or 80 GB HBM2e at 2 TB/s. Though superseded by Hopper, A100s remain the most common research GPU — cheaper on spot markets, ample for fine-tuning and inference of 7-70B models. The 80GB variant with NVLink still trains serious models; it is the value tier of datacenter AI.", "NVIDIA", "40/80 GB HBM2e; 2 TB/s", "312 TFLOPS BF16 dense", "7nm; 400W SXM", "SXM4 / PCIe", "python", "A100 value check", "for mem in [40, 80]:\n    fit = \"7B-13B\" if mem == 40 else \"up to 70B (quantized)\"\n    print(f\"A100 {mem}GB: fine-tune {fit}\")"],
 ["nvidia", "NVIDIA L40S", "The universal datacenter GPU: Ada Lovelace power for inference, graphics, and fine-tuning.", "The L40S packs 48 GB GDDR6 and strong FP8/FP16 throughput in a passively cooled PCIe card that fits standard servers — no SXM baseboard needed. It targets inference, fine-tuning, and graphics/AI mixed workloads, delivering near-H100 inference performance per dollar in many deployments. The easy drop-in form factor made it the default inference GPU for enterprises.", "NVIDIA", "48 GB GDDR6", "~733 TFLOPS FP8; 362 TFLOPS FP16", "5nm; 350W", "PCIe (passive)", "python", "L40S inference fit", "mem = 48\nprint(f\"fits 70B Q4 ({70*0.5:.0f}GB) + KV cache comfortably\")"],
 ["amd", "AMD Instinct MI300X", "AMD's H100 challenger: 192 GB HBM3 per GPU — the memory king of its generation.", "The MI300X offers 192 GB of HBM3 (5.3 TB/s) per GPU — 2.4x the H100's memory — with ~1.3 PFLOPS BF16 dense. Its headline advantage: run 70B+ models on fewer GPUs. Software (ROCm) has matured substantially, with vLLM and PyTorch support now solid. Deployed at scale by Microsoft, Meta, and Oracle clouds, it is the first credible datacenter alternative to NVIDIA for LLM serving.", "AMD", "192 GB HBM3; 5.3 TB/s", "~1.3 PFLOPS BF16 dense", "5/6nm; 750W", "OAM / PCIe", "python", "MI300X memory advantage", "print(f\"MI300X {192}GB vs H100 {80}GB = {192/80:.1f}x memory per GPU\")"],
 ["amd", "AMD Instinct MI325X", "MI300X refresh with 256 GB HBM3e — AMD's answer to H200.", "The MI325X bumps memory to 256 GB HBM3e at 6 TB/s with the same CDNA 3 compute, targeting H200-class inference workloads. Same platform compatibility as MI300X for easy upgrades. AMD's roadmap continues to MI350 (CDNA 4) with FP4/FP6 support.", "AMD", "256 GB HBM3e; 6 TB/s", "~1.3 PFLOPS BF16 dense", "5/6nm; ~1000W", "OAM", "python", "MI325X vs H200 memory", "print(f\"MI325X 256GB vs H200 141GB = {256/141:.1f}x\")"]
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
var gen={version:'jahdb-ai-accelerator-hardware-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-accelerator-hardware',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
