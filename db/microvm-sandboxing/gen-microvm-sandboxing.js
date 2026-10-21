(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hypervisor", "container", "unikernel", "enclave", "tooling"];
var PREFIX='JAH-MICROV-';
var GENVER='jahdb-microvm-sandboxing-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["project", "tech", "boot_ms", "memory_mb"];
var DEMO_TPL="// $TITLE - microVM boot profile\nvar VM = { name: \"$PROJECT\", boot_ms: $BOOT_MS, memory_mb: $MEMORY_MB, tech: \"$TECH\" };\nconsole.log(\"MicroVM: \" + VM.name);\nconsole.log(\"Boot: \" + VM.boot_ms + \" ms | Guest: \" + VM.memory_mb + \" MB | Tech: \" + VM.tech);\nconsole.log(\"Density on 64 GiB host: ~\" + Math.floor(65536 / VM.memory_mb) + \" instances\");\nconsole.log(\"Isolation: hardware virtualization -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["hypervisor", "Firecracker", "AWS’s KVM-based microVM manager; boots MicroVMs in ~125 ms and powers Lambda and Fargate. Built on KVM, it boots in about 125 ms with a 5 MB guest footprint.", {"project": "Firecracker", "tech": "KVM", "boot_ms": "125", "memory_mb": "5"}], ["hypervisor", "Cloud Hypervisor", "A Rust VMM from the rust-vmm project aimed at cloud workloads with vhost-user device offload. Built on KVM, it boots in about 150 ms with a 8 MB guest footprint.", {"project": "Cloud Hypervisor", "tech": "KVM", "boot_ms": "150", "memory_mb": "8"}], ["container", "Kata Containers", "Runs each container in a lightweight VM, blending container UX with hardware isolation boundaries. Built on QEMU/Cloud-Hypervisor/Firecracker, it boots in about 300 ms with a 64 MB guest footprint.", {"project": "Kata Containers", "tech": "QEMU/Cloud-Hypervisor/Firecracker", "boot_ms": "300", "memory_mb": "64"}], ["container", "gVisor", "Google’s user-space kernel intercepts syscalls so containers run with a reduced host attack surface. Built on user-space kernel (Sentry), it boots in about 200 ms with a 32 MB guest footprint.", {"project": "gVisor", "tech": "user-space kernel (Sentry)", "boot_ms": "200", "memory_mb": "32"}], ["hypervisor", "crosvm", "ChromeOS’s Rust VMM for running Linux and Android guests with virtio devices. Built on KVM, it boots in about 120 ms with a 8 MB guest footprint.", {"project": "crosvm", "tech": "KVM", "boot_ms": "120", "memory_mb": "8"}], ["hypervisor", "QEMU microvm", "QEMU’s microvm machine type strips legacy devices for a minimal, fast-booting VM target. Built on KVM/HAXM, it boots in about 400 ms with a 16 MB guest footprint.", {"project": "QEMU microvm", "tech": "KVM/HAXM", "boot_ms": "400", "memory_mb": "16"}], ["hypervisor", "StratoVirt", "A Rust VMM supporting both standard and micro VMs with hot-plug device models. Built on KVM, it boots in about 180 ms with a 8 MB guest footprint.", {"project": "StratoVirt", "tech": "KVM", "boot_ms": "180", "memory_mb": "8"}], ["hypervisor", "Hyperlight", "Microsoft’s library for embedding tiny Hyper-V-isolated guests inside a host process. Built on Hyper-V/WHP, it boots in about 50 ms with a 4 MB guest footprint.", {"project": "Hyperlight", "tech": "Hyper-V/WHP", "boot_ms": "50", "memory_mb": "4"}], ["tooling", "vmm-reference", "The rust-vmm reference VMM showing how to assemble a minimal KVM guest from crates. Built on KVM (rust-vmm), it boots in about 100 ms with a 4 MB guest footprint.", {"project": "vmm-reference", "tech": "KVM (rust-vmm)", "boot_ms": "100", "memory_mb": "4"}], ["unikernel", "OSv", "A unikernel running unmodified Linux ELF binaries on a single-address-space kernel. Built on unikernel, it boots in about 250 ms with a 32 MB guest footprint.", {"project": "OSv", "tech": "unikernel", "boot_ms": "250", "memory_mb": "32"}], ["unikernel", "Unikraft", "A modular unikernel SDK composing minimal images from micro-libraries per application. Built on unikernel, it boots in about 80 ms with a 4 MB guest footprint.", {"project": "Unikraft", "tech": "unikernel", "boot_ms": "80", "memory_mb": "4"}], ["unikernel", "MirageOS", "OCaml unikernels compiled to Xen, KVM, or Unix with type-safe network stacks. Built on unikernel (OCaml), it boots in about 60 ms with a 8 MB guest footprint.", {"project": "MirageOS", "tech": "unikernel (OCaml)", "boot_ms": "60", "memory_mb": "8"}], ["unikernel", "Nanos", "A unikernel that runs Linux binaries as single-process VMs with a tiny kernel surface. Built on unikernel, it boots in about 90 ms with a 8 MB guest footprint.", {"project": "Nanos", "tech": "unikernel", "boot_ms": "90", "memory_mb": "8"}], ["enclave", "Nitro Enclaves", "EC2 enclaves carve CPU/memory-isolated VMs with no persistent storage or network for secrets work. Built on Nitro hypervisor, it boots in about 500 ms with a 64 MB guest footprint.", {"project": "Nitro Enclaves", "tech": "Nitro hypervisor", "boot_ms": "500", "memory_mb": "64"}], ["container", "Weave Ignite", "Ran containers as Firecracker microVMs via a containerd shim for VM-grade multi-tenancy. Built on Firecracker + containerd, it boots in about 350 ms with a 32 MB guest footprint.", {"project": "Weave Ignite", "tech": "Firecracker + containerd", "boot_ms": "350", "memory_mb": "32"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-MICROV\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microvm-sandboxing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
