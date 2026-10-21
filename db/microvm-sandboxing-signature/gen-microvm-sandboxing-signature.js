(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hypervisor", "container", "unikernel", "enclave", "tooling"];
var PREFIX='JAH-MICROV-S-';
var GENVER='jahdb-microvm-sandboxing-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["project", "tech", "boot_ms", "memory_mb"];
var DEMO_TPL="// $TITLE - microVM boot profile\nvar VM = { name: \"$PROJECT\", boot_ms: $BOOT_MS, memory_mb: $MEMORY_MB, tech: \"$TECH\" };\nconsole.log(\"MicroVM: \" + VM.name);\nconsole.log(\"Boot: \" + VM.boot_ms + \" ms | Guest: \" + VM.memory_mb + \" MB | Tech: \" + VM.tech);\nconsole.log(\"Density on 64 GiB host: ~\" + Math.floor(65536 / VM.memory_mb) + \" instances\");\nconsole.log(\"Isolation: hardware virtualization -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["hypervisor", "SigCell", "Signature-original: a 3 ms-booting cell hypervisor with per-cell memory coloring against side channels. Built on KVM + SigGuard, it boots in about 3 ms with a 2 MB guest footprint.", {"project": "SigCell", "tech": "KVM + SigGuard", "boot_ms": "3", "memory_mb": "2"}], ["container", "SigPod", "Signature-original: pod sandboxes snapshotting to disk in 40 ms for instant warm restarts. Built on SigCell + overlayfs, it boots in about 45 ms with a 16 MB guest footprint.", {"project": "SigPod", "tech": "SigCell + overlayfs", "boot_ms": "45", "memory_mb": "16"}], ["container", "SigKernel", "Signature-original: a user-space kernel speaking the SigABI with formally checked syscall filters. Built on user-space SigABI, it boots in about 120 ms with a 24 MB guest footprint.", {"project": "SigKernel", "tech": "user-space SigABI", "boot_ms": "120", "memory_mb": "24"}], ["unikernel", "SigUni", "Signature-original: unikernel images synthesized per function with dead code eliminated at build. Built on SigUni SDK, it boots in about 30 ms with a 3 MB guest footprint.", {"project": "SigUni", "tech": "SigUni SDK", "boot_ms": "30", "memory_mb": "3"}], ["enclave", "SigEnclave", "Signature-original: enclaves with remote attestation quotes chained to the Signature ledger. Built on SEV-SNP/TDX, it boots in about 600 ms with a 128 MB guest footprint.", {"project": "SigEnclave", "tech": "SEV-SNP/TDX", "boot_ms": "600", "memory_mb": "128"}], ["hypervisor", "SigMeshVM", "Signature-original: microVMs that join the peer mesh at boot with identity-bound networking. Built on KVM + SigMesh, it boots in about 140 ms with a 8 MB guest footprint.", {"project": "SigMeshVM", "tech": "KVM + SigMesh", "boot_ms": "140", "memory_mb": "8"}], ["tooling", "SigFreeze", "Signature-original: freeze/thaw tooling snapshotting microVM memory to content-addressed blobs. Built on SigCell snapshots, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigFreeze", "tech": "SigCell snapshots", "boot_ms": "0", "memory_mb": "0"}], ["hypervisor", "SigNest", "Signature-original: nested cells running test hypervisors inside production cells safely. Built on nested KVM, it boots in about 200 ms with a 16 MB guest footprint.", {"project": "SigNest", "tech": "nested KVM", "boot_ms": "200", "memory_mb": "16"}], ["tooling", "SigWatch", "Signature-original: a syscall-anomaly watcher killing cells that deviate from learned profiles. Built on eBPF + SigCell, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigWatch", "tech": "eBPF + SigCell", "boot_ms": "0", "memory_mb": "0"}], ["tooling", "SigPack", "Signature-original: image packer producing signed, deduped cell images with SBOM attached. Built on SigCell images, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigPack", "tech": "SigCell images", "boot_ms": "0", "memory_mb": "0"}], ["hypervisor", "SigNet", "Signature-original: per-cell virtual NICs with default-deny egress and mesh-only routing. Built on virtio-net + SigMesh, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigNet", "tech": "virtio-net + SigMesh", "boot_ms": "0", "memory_mb": "0"}], ["hypervisor", "SigTime", "Signature-original: virtualized time sources so cells can be fast-forwarded for testing. Built on KVM clock, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigTime", "tech": "KVM clock", "boot_ms": "0", "memory_mb": "0"}], ["tooling", "SigMigrate", "Signature-original: live migration moving running cells between hosts with sub-second pause. Built on SigCell pre-copy, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigMigrate", "tech": "SigCell pre-copy", "boot_ms": "0", "memory_mb": "0"}], ["tooling", "SigFuzz", "Signature-original: cell-aware fuzzer snapshotting before each input for millisecond resets. Built on SigFreeze + libFuzzer, it boots in about 0 ms with a 0 MB guest footprint.", {"project": "SigFuzz", "tech": "SigFreeze + libFuzzer", "boot_ms": "0", "memory_mb": "0"}], ["hypervisor", "SigOne", "Signature-original: the united master cell runtime combining Cell, Pod, Uni, and Enclave tiers. Built on SigCell family, it boots in about 3 ms with a 2 MB guest footprint.", {"project": "SigOne", "tech": "SigCell family", "boot_ms": "3", "memory_mb": "2"}]];
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
  if(!new RegExp('^'+'JAH\\-MICROV\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microvm-sandboxing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
