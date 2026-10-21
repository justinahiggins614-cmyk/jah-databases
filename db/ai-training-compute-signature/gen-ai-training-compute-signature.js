(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["gpu-cluster", "interconnect", "cloud-gpu", "planning", "networking", "storage"] */
var CATS=["gpu-cluster", "interconnect", "cloud-gpu", "planning", "networking", "storage"];
var PREFIX='JAH-TRNC-S-';
var FIELDS=["resource_type", "capacity", "interconnect", "cost_notes"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["planning", "Signature FLOPs Budget Planner", "Signature-authored planner: from model size and tokens to GPU-hours, dollars, and schedule.", "The Signature FLOPs Budget Planner is a JAH-designed planning worksheet (and calculator): input parameters, tokens, hardware, and MFU assumption, and it outputs total FLOPs, GPU-hours, calendar days at a given fleet size, and cost under on-demand, reserved, and spot pricing. Every estimate carries an uncertainty band. Labeled Signature throughout.", "planning tool", "Any model scale", "n/a", "Built-in pricing scenarios", "python", "Signature budget planner", "def plan(params, tokens, peak_tflops=989, mfu=0.45, price=3.0):\n    flops = 6*params*tokens\n    hrs = flops/(peak_tflops*1e12*mfu)/3600\n    return {\"FLOPs\": f\"{flops:.2e}\", \"gpu_hours\": f\"{hrs:,.0f}\",\n            \"cost\": f\"${hrs*price:,.0f}\"}\nprint(plan(7e9, 2e12))"],
 ["gpu-cluster", "JAH Cluster Sizer", "Signature-authored method: size node count, parallelism, and network from model and deadline.", "JAH Cluster Sizer is a JAH-designed sizing method: given model parameters, tokens, and a deadline, it computes the minimum fleet, recommends tensor/pipeline/data parallel splits that respect NVLink domains, and sizes the fabric (rails per GPU). Outputs include a single-node validation step before scaling. Labeled Signature; an original JAH procedure.", "sizing method", "Any scale", "NVLink-domain-aware splits", "Avoids over-provisioned fabrics", "python", "Parallelism split recommender", "params = 70e9\ntp = 8 if params > 30e9 else 4   # fill NVLink domain first\nprint(f\"70B: TP={tp} within node, then pipeline/data parallel across nodes\")"],
 ["interconnect", "Signature Interconnect Chooser", "Signature-authored decision framework: InfiniBand vs RoCE vs EFA for your scale and budget.", "The Signature Interconnect Chooser is a JAH-designed decision framework scoring fabrics on collective performance, cost per port, operational complexity, and vendor lock-in, weighted by cluster size. Under 64 GPUs it usually recommends cloud-managed fabrics; above 512 it scores dedicated IB/RoCE. Labeled Signature throughout.", "decision framework", "Any cluster size", "Compares IB/RoCE/EFA", "Includes 3-year fabric TCO", "python", "Fabric scoring", "scores = {\"InfiniBand\": {\"perf\": 9, \"cost\": 5},\n            \"RoCE\": {\"perf\": 7, \"cost\": 8}, \"EFA\": {\"perf\": 8, \"cost\": 6}}\nfor k, v in scores.items():\n    print(k, \"value:\", v[\"perf\"] + v[\"cost\"])"],
 ["planning", "JAH Spot Bid Optimizer", "Signature-authored strategy: bid across regions and instance types for cheapest reliable spot.", "JAH Spot Bid Optimizer is a JAH-designed spot strategy: diversify across regions, zones, and GPU types; set max prices per type; checkpoint every 15 minutes; and auto-failover to on-demand only for the final training phase. A ledger tracks effective $/GPU-hour including preemption losses. Labeled Signature; an original JAH procedure.", "pricing strategy", "Any scale", "Same as chosen instances", "Targets 70%+ savings vs on-demand", "python", "Effective spot cost with preemptions", "rate, preempt_per_day, restart_min = 2.0, 2, 10\nwaste = preempt_per_day * restart_min / 60 / 24\neff = rate * (1 + waste)\nprint(f\"effective: ${eff:.2f}/hr (waste {waste:.1%})\")"],
 ["planning", "Signature Power Envelope Planner", "Signature-authored facility plan: from GPU count to megawatts, cooling, and utility contracts.", "The Signature Power Envelope Planner is a JAH-designed worksheet: GPU count to kW (with PUE), cooling technology choice (air vs direct-liquid), utility feed sizing, and a power-purchase checklist. It flags the common trap — GPUs arriving before the power does. Labeled Signature throughout.", "facility planning", "Any cluster size", "n/a", "Flags power-first procurement", "python", "Power envelope", "gpus, w_per_gpu, pue = 2048, 700, 1.35\nmw = gpus * w_per_gpu * pue / 1e6\nprint(f\"{gpus} GPUs -> {mw:.1f} MW; cooling: {'liquid' if mw > 5 else 'air'}\")"],
 ["storage", "JAH Checkpoint Cadence Calculator", "Signature-authored method: optimal checkpoint interval from failure rate and checkpoint cost.", "JAH Checkpoint Cadence Calculator is a JAH-designed formula tool: given per-GPU MTBF, fleet size, and checkpoint write time, it computes the Young/Daly optimal interval minimizing expected lost work. Outputs include storage sizing for the retention window. Labeled Signature; an original JAH procedure.", "reliability method", "Any fleet size", "n/a", "Minimizes expected lost GPU-hours", "python", "Young/Daly optimal interval", "import math\nmtbf_h, ckpt_min = 50, 5  # fleet MTBF hours, checkpoint minutes\nopt_min = math.sqrt(2 * ckpt_min * mtbf_h * 60)\nprint(f\"optimal checkpoint every ~{opt_min:.0f} min\")"],
 ["planning", "Signature MFU Tracker", "Signature-authored dashboard spec: track MFU per run and attribute every point of loss.", "The Signature MFU Tracker is a JAH-designed monitoring spec: log achieved vs peak FLOPs per step, attribute gaps to dataloader/compute/communication buckets, and alert when MFU drops 5 points below the run's baseline. The design turns MFU from a vanity metric into a debugging tool. Labeled Signature throughout.", "monitoring spec", "Any run", "n/a", "Finds wasted GPU-hours automatically", "python", "MFU attribution", "gaps = {\"dataloader\": 0.06, \"communication\": 0.04, \"kernels\": 0.03}\nprint(\"MFU lost:\", sum(gaps.values()), \"-> fix:\", max(gaps, key=gaps.get))"],
 ["planning", "JAH Scaling Law Fitter", "Signature-authored method: fit your own scaling curves from small runs before committing.", "JAH Scaling Law Fitter is a JAH-designed procedure: run a ladder of small models (10M to 1B), fit loss-vs-compute power laws, and extrapolate to pick the compute-optimal size for your budget — your own Chinchilla, calibrated to your data. Includes confidence bands so extrapolation risk is explicit. Labeled Signature; an original JAH procedure.", "planning method", "Any budget", "n/a", "Small runs de-risk big bets", "python", "Power-law fit sketch", "import math\nruns = [(1e18, 3.2), (1e19, 2.9), (1e20, 2.65)]  # (flops, loss)\nxs = [math.log10(f) for f, _ in runs]; ys = [l for _, l in runs]\nn = len(runs)\nslope = (n*sum(a*b for a, b in zip(xs, ys)) - sum(xs)*sum(ys)) /         (n*sum(a*a for a in xs) - sum(xs)**2)\nprint(\"loss slope per decade:\", round(slope, 3))"]
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
var gen={version:'jahdb-ai-training-compute-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-training-compute-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
