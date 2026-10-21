(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["nvidia", "amd", "google-tpu", "cloud-asic", "startup-chip", "edge-npu", "planning"] */
var CATS=["nvidia", "amd", "google-tpu", "cloud-asic", "startup-chip", "edge-npu", "planning"];
var PREFIX='JAH-AIACC-S-';
var FIELDS=["vendor", "memory", "throughput", "process_power", "form_factor"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["nvidia", "Signature Core-1 Datacenter Card", "Signature-authored concept: a datacenter AI card optimized for the Signature software stack.", "Signature Core-1 is a JAH-designed accelerator concept: a PCIe datacenter card with large on-package memory, native FP8/FP4 tensor units, and a compiler target matching the Signature inference stack. The concept specifies a memory-first architecture (compute sized to feed the memory, not vice versa) for LLM serving. Labeled Signature throughout — a concept design, not shipping hardware.", "Signature Systems (JAH concept)", "192 GB on-package (concept)", "2 PFLOPS BF16 dense (target)", "5nm-class target; 600W", "PCIe (concept)", "python", "Concept spec sheet", "spec = {\"memory_gb\": 192, \"bf16_tflops\": 2000, \"power_w\": 600}\nprint(f\"{spec['bf16_tflops']/spec['power_w']:.1f} TFLOPS/W target\")"],
 ["cloud-asic", "JAH Inference Blade", "Signature-authored concept: a low-power inference blade for dense serving racks.", "JAH Inference Blade is a JAH-designed blade concept: 8 inference-optimized chips per blade with shared memory pooling, targeting maximum tokens-per-watt for chat serving. The concept includes a power-telemetry unit per blade for the Signature power-aware scheduler. Labeled Signature; a concept design.", "Signature Systems (JAH concept)", "512 GB pooled per blade (concept)", "4000 tok/s per blade (target)", "2 kW per blade", "Blade (concept)", "python", "Blade efficiency target", "tps, watts = 4000, 2000\nprint(f\"{tps/watts:.1f} tokens/sec per watt (target)\")"],
 ["nvidia", "Signature Training Tile", "Signature-authored concept: a training tile with on-tile interconnect for tensor parallelism.", "Signature Training Tile is a JAH-designed training accelerator concept: tiles connect via a high-bandwidth on-package fabric so tensor parallelism never leaves the package, with HBM stacks per tile. The concept targets 60%+ MFU out of the box via co-designed collectives. Labeled Signature throughout — a concept design.", "Signature Systems (JAH concept)", "128 GB HBM per tile (concept)", "1.5 PFLOPS BF16 per tile (target)", "800W per tile", "OAM-class tile (concept)", "python", "Tile fabric math", "tiles, bw_tbs = 4, 1.8\nprint(f\"{tiles} tiles x {bw_tbs} TB/s on-package fabric\")"],
 ["startup-chip", "JAH Memory-First Accelerator", "Signature-authored concept: an accelerator where memory capacity, not FLOPs, is the headline spec.", "JAH Memory-First Accelerator is a JAH-designed concept that inverts the usual spec sheet: 1 TB of on-card memory with 'enough' compute to saturate it, aimed at serving 70B-400B models on single cards. The concept trades peak FLOPs for capacity and memory bandwidth. Labeled Signature; a concept design.", "Signature Systems (JAH concept)", "1 TB on-card (concept)", "800 TFLOPS BF16 (balanced)", "500W", "PCIe (concept)", "python", "Memory-first fit", "mem_tb = 1\nprint(f\"400B Q4 = {400*0.5:.0f}GB -> fits in {mem_tb}TB with KV headroom\")"],
 ["startup-chip", "Signature Sparse Compute Unit", "Signature-authored concept: hardware that skips zeros — native 2:4 and unstructured sparsity.", "Signature Sparse Compute Unit is a JAH-designed accelerator concept with native sparse tensor cores: 2:4 structured sparsity at full throughput plus unstructured sparsity support, doubling effective FLOPs on pruned models. The concept pairs with the Signature sparsity-aware training method. Labeled Signature throughout — a concept design.", "Signature Systems (JAH concept)", "96 GB HBM (concept)", "2x effective on 2:4 sparse", "450W", "PCIe (concept)", "python", "Sparse speedup", "dense, sparse_ratio = 1000, 0.5\nprint(f\"effective: {dense/(1-sparse_ratio):.0f} TFLOPS at 50% sparsity\")"],
 ["startup-chip", "JAH Photonic Inference Concept", "Signature-authored concept: photonic matrix multiplication for ultra-low-energy inference.", "JAH Photonic Inference Concept is a JAH-designed research concept: perform matrix multiplications optically (light interference) for near-zero-energy MACs, with electronic control planes. The concept acknowledges the hard problems (precision, programmability) and scopes itself to fixed-model inference appliances. Labeled Signature; a research concept, not a product.", "Signature Systems (JAH concept)", "Model-stationary photonic mesh (concept)", "10x energy efficiency (aspiration)", "100W optical + control", "Appliance (concept)", "python", "Photonic energy sketch", "macs, j_per_mac_elec, j_per_mac_phot = 1e12, 1e-12, 1e-14\nprint(f\"electronic: {macs*j_per_mac_elec:.0f}J vs photonic: {macs*j_per_mac_phot:.2f}J\")"],
 ["startup-chip", "Signature Analog-Digital Hybrid Tile", "Signature-authored concept: analog crossbars for MACs, digital for control and precision.", "Signature Analog-Digital Hybrid Tile is a JAH-designed concept pairing analog in-memory crossbars (dense MACs at extreme efficiency) with a digital control plane that corrects and calibrates. The concept targets edge-datacenter inference where watts matter most. Labeled Signature throughout — a concept design.", "Signature Systems (JAH concept)", "Analog crossbar arrays + digital SRAM", "50 TOPS/W (target)", "75W", "PCIe (concept)", "python", "Hybrid precision plan", "print(\"analog: 95% of MACs | digital: calibration + residuals\")"],
 ["edge-npu", "JAH Edge TPU-Class Chip", "Signature-authored concept: a phone-grade NPU for the Signature Edge Runtime.", "JAH Edge TPU-Class Chip is a JAH-designed mobile NPU concept: 30 TOPS INT8, hardware support for the Signature quantization formats, and a delegate interface for the Signature Edge Runtime. The concept targets on-device LLM inference at 5-10 tokens/sec within phone power budgets. Labeled Signature; a concept design.", "Signature Systems (JAH concept)", "Shared SoC memory", "30 TOPS INT8", "5W", "SoC IP (concept)", "python", "Edge token budget", "tops, tops_per_token = 30, 2\nprint(f\"~{tops/tops_per_token:.0f} tok/s INT8 (rough)\")"]
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
  rec.provenance="Signature Systems (JAH)";
  rec.last_verified='2026-10-20';
  rec.src="signature-generated-completion";
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
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ai-accelerator-hardware-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-accelerator-hardware-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
