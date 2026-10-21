(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["process", "container", "vm", "language", "tooling"];
var PREFIX='JAH-LSC-';
var GENVER='jahdb-live-state-checkpointing-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "scope", "format", "restore"];
var DEMO_TPL="// $TITLE - checkpoint/restore cycle\nvar CKPT = { tool: \"$TOOL\", scope: \"$SCOPE\", file: \"ckpt-$ID.bin\" };\nvar state = { counter: 41, openFiles: 3 };\nconsole.log(\"Tool: \" + CKPT.tool + \" (\" + CKPT.scope + \")\");\nvar frozen = JSON.stringify(state);\nconsole.log(\"Frozen -> \" + CKPT.file + \" (\" + frozen.length + \" bytes)\");\nstate.counter = 999;\nvar restored = JSON.parse(frozen);\nconsole.log(\"Restored counter=\" + restored.counter + \" openFiles=\" + restored.openFiles + \" -> RESTORE OK\");\nconsole.log(\"Restore cmd: $RESTORE\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["process", "CRIU", "Checkpoint/Restore In Userspace freezes Linux processes including TCP sockets and namespaces. Scope: Linux process tree. Checkpoint format: image files (protobuf). Restore with: criu restore -D ckpt/.", {"tool": "CRIU", "scope": "Linux process tree", "format": "image files (protobuf)", "restore": "criu restore -D ckpt/"}], ["container", "Podman checkpoint", "Podman integrates CRIU so containers checkpoint to disk and restore on any host. Scope: OCI container. Checkpoint format: tarball of CRIU images. Restore with: podman container restore <name>.", {"tool": "podman", "scope": "OCI container", "format": "tarball of CRIU images", "restore": "podman container restore <name>"}], ["container", "Docker checkpoint (experimental)", "Docker’s experimental checkpoint uses CRIU under the hood for container migration. Scope: container. Checkpoint format: CRIU image dir. Restore with: docker start --checkpoint <id>.", {"tool": "docker", "scope": "container", "format": "CRIU image dir", "restore": "docker start --checkpoint <id>"}], ["vm", "QEMU live migration", "QEMU pre-copies RAM while the VM runs, then pauses briefly for the final delta. Scope: full VM. Checkpoint format: migration stream. Restore with: qemu -incoming tcp:0:4444.", {"tool": "QEMU", "scope": "full VM", "format": "migration stream", "restore": "qemu -incoming tcp:0:4444"}], ["vm", "Firecracker snapshots", "Firecracker snapshots microVM memory to files for sub-second resume of serverless functions. Scope: microVM. Checkpoint format: memory + state files. Restore with: PUT /snapshot/load.", {"tool": "Firecracker", "scope": "microVM", "format": "memory + state files", "restore": "PUT /snapshot/load"}], ["container", "gVisor checkpoint", "gVisor’s Sentry can checkpoint the entire sandbox state including goroutine stacks. Scope: sandbox. Checkpoint format: state file. Restore with: runsc checkpoint/restore.", {"tool": "gVisor", "scope": "sandbox", "format": "state file", "restore": "runsc checkpoint/restore"}], ["language", "Erlang hot code loading", "The BEAM swaps module code under running processes with zero downtime — checkpointing by design. Scope: BEAM VM. Checkpoint format: release packages. Restore with: release_handler:install_release/1.", {"tool": "OTP release_handler", "scope": "BEAM VM", "format": "release packages", "restore": "release_handler:install_release/1"}], ["language", "V8 startup snapshots", "mksnapshot serializes the heap after running setup code so Node and Chrome boot faster. Scope: JS heap. Checkpoint format: snapshot blob. Restore with: linked into the binary.", {"tool": "mksnapshot", "scope": "JS heap", "format": "snapshot blob", "restore": "linked into the binary"}], ["container", "CRI-O checkpoint", "CRI-O exposes CRIU checkpoint/restore through the Kubernetes CRI for pod migration. Scope: K8s pod sandbox. Checkpoint format: CRIU images. Restore with: crictl restore.", {"tool": "CRI-O", "scope": "K8s pod sandbox", "format": "CRIU images", "restore": "crictl restore"}], ["container", "LXD snapshots", "LXD snapshots containers and VMs with optional stateful (running-memory) capture. Scope: instance. Checkpoint format: zfs/btrfs snapshot + state. Restore with: lxc restore <inst> <snap>.", {"tool": "LXD", "scope": "instance", "format": "zfs/btrfs snapshot + state", "restore": "lxc restore <inst> <snap>"}], ["vm", "VirtualBox snapshots", "VirtualBox differencing images let desktop VMs branch and roll back live state. Scope: desktop VM. Checkpoint format: VDI differencing chain. Restore with: VBoxManage snapshot restore.", {"tool": "VirtualBox", "scope": "desktop VM", "format": "VDI differencing chain", "restore": "VBoxManage snapshot restore"}], ["vm", "VMware snapshots", "VMware’s .vmsn files capture full VM memory and device state for instant rollback. Scope: VM. Checkpoint format: .vmsn + delta disks. Restore with: revert to snapshot.", {"tool": "VMware", "scope": "VM", "format": ".vmsn + delta disks", "restore": "revert to snapshot"}], ["vm", "KVM live migration", "KVM guests migrate between hosts with dirty-page tracking keeping downtime in milliseconds. Scope: KVM guest. Checkpoint format: migration stream. Restore with: virsh migrate --live.", {"tool": "KVM/QEMU", "scope": "KVM guest", "format": "migration stream", "restore": "virsh migrate --live"}], ["process", "DMTCP", "Distributed MultiThreaded CheckPointing needs no root and handles MPI clusters transparently. Scope: distributed process. Checkpoint format: ckpt files per rank. Restore with: dmtcp_restart ckpt_*.dmtcp.", {"tool": "DMTCP", "scope": "distributed process", "format": "ckpt files per rank", "restore": "dmtcp_restart ckpt_*.dmtcp"}], ["process", "BLCR", "Berkeley Lab Checkpoint/Restart was the classic HPC process checkpointer for batch systems. Scope: HPC process. Checkpoint format: context files. Restore with: cr_restart context.", {"tool": "BLCR", "scope": "HPC process", "format": "context files", "restore": "cr_restart context"}]];
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
  if(!new RegExp('^'+'JAH\\-LSC\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('live-state-checkpointing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
