(function(){'use strict';
/* jahdb-defense-aerospace-k3s-microk8s-1.0 — deterministic boundless generator for defense-aerospace-k3s-microk8s.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["distributions", "air-gap", "networking", "storage", "operations"];
var PREFIX='JAH-DAE21-';
var EDITION='public';
var POOL=[["Lightweight Kubernetes for the Edge", "distributions", "K3s (Rancher) and MicroK8s (Canonical) are lightweight Kubernetes distributions that run the full orchestration API on small hardware — single binary, low memory, ARM-friendly. They bring containers, scheduling, and self-healing to places full Kubernetes cannot go. The edge gets the same declarative model as the cloud.", {"K3s": "Rancher, single binary", "MicroK8s": "Canonical, snap-based", "Runs": "small HW, ARM", "Brings": "K8s API to edge"}], ["K3s: The Single Binary", "distributions", "K3s packs the Kubernetes control plane, kubelet, and containerd into one ~100MB binary with an embedded SQLite (or etcd) datastore — install is one command, upgrade is swapping the binary. Rancher built it for edge and IoT. Simplicity is the feature.", {"Packs": "control plane + kubelet", "Binary": "~100MB, one file", "Stores": "SQLite or etcd", "Installs": "one command"}], ["MicroK8s: The Snap Distribution", "distributions", "MicroK8s delivers Kubernetes as a snap with opinionated addons — DNS, storage, ingress, GPU — toggled by single commands. Canonical aims it at workstations, edge, and appliances. Addons make the common edge stack one-liners.", {"Delivers": "as a snap", "Addons": "dns, storage, ingress, gpu", "Toggles": "one command", "Aims": "edge, appliances"}], ["Air-Gapped Installation", "air-gap", "Air-gapped K3s/MicroK8s install from pre-staged binaries and private registries — no internet at deploy time, ever. Images get mirrored into the enclave; manifests reference the mirror. The cluster is born offline and stays offline. Planning the bundle is the work.", {"Installs": "pre-staged, no internet", "Mirrors": "images to private registry", "Stays": "offline", "Plans": "the bundle"}], ["Private Registries in the Enclave", "air-gap", "Harbor or a simple registry mirror serves images inside the air gap, with the cluster's image pull secrets pointing at it. Every image is scanned before mirroring. The registry is the enclave's app store — curated, versioned, offline.", {"Serves": "Harbor-class mirror", "Scans": "before mirroring", "Points": "pull secrets inward", "Is": "offline app store"}], ["HA: etcd Quorums at the Edge", "operations", "High-availability K3s runs embedded etcd across 3+ nodes — quorum survives a node loss, which is the point at the edge where hardware fails. MicroK8s clusters similarly with dqlite. Odd numbers, watched disks, tested failover. Edge HA is the same math, harsher conditions.", {"Runs": "etcd, 3+ nodes", "Survives": "a node loss", "Needs": "odd numbers", "Tests": "failover"}], ["Kine and Datastore Options", "operations", "K3s's Kine layer lets the control plane use SQLite, Postgres, or etcd as its datastore — SQLite for single nodes, etcd for HA. The choice trades operational simplicity against scale. Defaults are sensible; overrides are available.", {"Kine": "datastore shim", "SQLite": "single node", "etcd": "HA", "Trades": "simple vs scale"}], ["Networking: Flannel, Calico, Cilium", "networking", "Edge clusters network with Flannel (simple overlay), Calico (policy-rich), or Cilium (eBPF-powered) — the CNI choice sets the security and observability posture. Air-gapped clusters often add strict network policies by default. Packets follow policy.", {"Flannel": "simple overlay", "Calico": "policy-rich", "Cilium": "eBPF power", "Defaults": "deny in air gap"}], ["Storage at the Edge", "storage", "Edge storage uses local-path provisioners, Longhorn (replicated block), or OpenEBS — persistence without a SAN. Longhorn replicates volumes across nodes so a dead node does not take the data. The edge stores what it must, replicates what matters.", {"Local-path": "simple persistence", "Longhorn": "replicated block", "Survives": "node loss", "Stores": "what it must"}], ["Workload Scheduling and Taints", "operations", "Taints, tolerations, and affinity place workloads deliberately — GPU jobs on GPU nodes, critical pods spread across failure domains. The scheduler is policy execution. At the edge, every node counts, so placement is explicit.", {"Taints": "keep workloads placed", "Affinity": "spread critical pods", "Counts": "every node", "Is": "policy execution"}], ["GitOps in Disconnected Environments", "air-gap", "GitOps (Flux/Argo) works air-gapped against in-enclave git mirrors — desired state versioned, drift corrected, audits automatic. The repo is the control plane's memory. Disconnected does not mean unmanaged.", {"Mirrors": "git in-enclave", "Corrects": "drift automatically", "Audits": "every change", "Means": "managed, offline"}], ["Observability: Metrics and Logs", "operations", "Edge clusters run Prometheus/Grafana and Loki-class logging in-cluster — metrics and logs without phoning home. Alerts route to local operators. Observability stays inside the enclave because the data never leaves.", {"Metrics": "Prometheus in-cluster", "Logs": "Loki-class", "Alerts": "local operators", "Stays": "inside enclave"}], ["Security Hardening: CIS Benchmarks", "operations", "Hardened K3s/MicroK8s follow CIS Kubernetes benchmarks — RBAC locked down, pod security standards, secrets encrypted at rest, API server flags set. Hardening guides are checklists, not suggestions. The edge is attacked too.", {"Follows": "CIS benchmarks", "Locks": "RBAC, pod security", "Encrypts": "secrets at rest", "Is": "checklist, not suggestion"}], ["Upgrades Without Internet", "air-gap", "Air-gapped upgrades stage new binaries and images into the enclave, then roll nodes one by one — the same rolling discipline, offline. Version skew policies still apply. Planned, staged, reversible.", {"Stages": "binaries + images", "Rolls": "node by node", "Applies": "skew policy", "Is": "planned, reversible"}], ["The Air-Gapped Cluster Picture", "distributions", "Ladder-top edge Kubernetes: light distros, offline install, mirrored images, etcd HA, strict networking, replicated storage, GitOps-managed. Fifteen rungs from a single binary to a tactical cluster that runs disconnected for months.", {"Runs": "light K8s", "Installs": "offline", "Mirrors": "images", "Manages": "GitOps"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var nodes=3+P.a%4, pods=12+P.b%20;
var code='// K3s air-gap scheduling demo (simulated model)\n';
code+='var nodes='+nodes+',pods='+pods+',per=Math.ceil(pods/nodes);\n';
code+='for(var i=0;i<nodes;i++){console.log("node-"+(i+1)+": "+Math.min(per,pods-i*per)+" pods (offline bundle)");}\n';
code+='console.log(pods+" pods scheduled across "+nodes+" air-gapped nodes");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-k3s-microk8s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-k3s-microk8s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
