(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['processes','memory','filesystems','cpu-arch','virtualization'];
var PREFIX='JAH-OSA-';

var T=[
{cat:'processes',topic:'fork and exec',t:'fork() and exec() — process birth',
 d:'Unix creates processes in two steps: fork() clones the caller, then exec() replaces the child\'s image with a new program. The split lets the parent wire up redirection and environment between the two calls.',
 mech:'fork() duplicates the address space with copy-on-write pages; both processes resume after the fork call, distinguished by its return value (0 in the child, the child PID in the parent). exec() then loads a new binary over the child.',
 ex:[['strace -f -e trace=process sh -c "echo hi"','Shows the clone/fork plus execve sequence a shell performs for every command.'],['ps -o pid,ppid,cmd','PPID column reveals the process tree fork() built.']],
 got:'Forgetting to reap children creates zombies — the parent must wait() or ignore SIGCHLD.',
 perf:'fork() is cheap thanks to copy-on-write; vfork()/posix_spawn() exist for constrained environments.'},
{cat:'processes',topic:'zombie processes',t:'Zombies — the unreaped dead',
 d:'A zombie is a dead process whose parent hasn\'t called wait() yet: only its exit status remains. Zombies hold no memory but clutter the process table; init (PID 1) reaps orphans automatically.',
 mech:'On exit, the kernel keeps a minimal task struct until the parent collects the status. If the parent dies first, the zombie is reparented to init, which reaps it.',
 ex:[['ps aux | awk \'$8 ~ /^Z/\'','Lists zombie processes by their Z state flag.'],['(sleep 0.1 & exec sleep 5)','Demo: brief zombies appear if the parent naps instead of waiting.']],
 got:'A program that forks workers in a loop without reaping will eventually hit the process limit.',
 perf:'Double-fork (fork, setsid, fork) daemonizes and lets init adopt — the classic daemon pattern.'},
{cat:'processes',topic:'signals',t:'Signals — async process messaging',
 d:'Signals are software interrupts: SIGTERM asks nicely, SIGKILL never asks, SIGCHLD reports child status. Processes can catch most signals but never SIGKILL or SIGSTOP.',
 mech:'The kernel delivers a signal by interrupting the target\'s execution and running its handler (or the default action). Signal masks let threads block delivery temporarily.',
 ex:[['kill -l','Lists all signal names and numbers on the system.'],['kill -TERM <pid>','Polite shutdown request; the process may clean up first.']],
 got:'kill -9 skips cleanup handlers — data loss and orphaned locks are common aftermath.',
 perf:'Signals are cheap but lossy: standard signals don\'t queue, so rapid repeats collapse into one.'},
{cat:'processes',topic:'threads vs processes',t:'Threads vs processes — sharing choices',
 d:'Processes isolate memory; threads share it. Threads are cheaper to create and switch, but shared memory means shared bugs — races, deadlocks, and Heisenbugs.',
 mech:'Threads of one process share the address space, file descriptors, and signal handlers, but each has its own stack and registers. Context switches skip the MMU/TLB flush that process switches need.',
 ex:[['ps -eLf | head','The -L flag lists individual threads (LWP column).'],['cat /proc/<pid>/status | grep Threads','Thread count of a running process.']],
 got:'Sharing without synchronization is a race; over-synchronizing serializes everything you parallelized.',
 perf:'Thread pools amortize creation cost; match pool size to cores for CPU work, larger for I/O wait.'},
{cat:'processes',topic:'nice and priority',t:'Nice values — scheduling politeness',
 d:'Nice values (-20 to +19) bias the scheduler: negative is pushy (needs privilege), positive is polite. The CFS scheduler translates niceness into CPU share weight.',
 mech:'CFS tracks virtual runtime; a nicer task\'s vruntime advances faster, so it gets picked less often. The weight table maps nice 0 to 1024 and scales geometrically.',
 ex:[['nice -n 10 ./batch_job','Runs a batch job politely below interactive work.'],['renice -n -5 -p <pid>','Boosts a running process (root only for negative).']],
 got:'Nice only matters under contention — on an idle machine everything runs at full speed.',
 perf:'For latency-critical work, prefer real-time policies (SCHED_FIFO) or cpusets over extreme nice values.'},
{cat:'memory',topic:'virtual memory',t:'Virtual memory — every process\'s private world',
 d:'Each process sees a private address space; the MMU translates virtual addresses to physical RAM via page tables. Isolation and the illusion of vast memory come free with the translation.',
 mech:'The CPU\'s MMU walks multi-level page tables on each access (cached in the TLB). Unmapped access raises a page fault — handled by mapping, swapping in, or killing the offender (segfault).',
 ex:[['cat /proc/<pid>/maps','Shows one process\'s virtual memory layout: heap, stacks, libraries.'],['getconf PAGESIZE','Page size on this machine — almost always 4096.']],
 got:'Virtual size (VSZ) is not physical use (RSS) — don\'t panic at big VSZ numbers.',
 perf:'Huge pages (2MB/1GB) cut TLB pressure for big heaps and databases.'},
{cat:'memory',topic:'paging and swapping',t:'Paging and swapping — RAM overflow handling',
 d:'When RAM fills, the kernel pages cold frames out to swap. Paging keeps the system alive under pressure but at disk latency — thrashing (constant paging) means you need more RAM, not more swap.',
 mech:'The page-reclaim algorithm (LRU approximations like CLOCK) picks victim frames; dirty pages are written back first. Swap slots live on disk partitions or files.',
 ex:[['free -h','Shows RAM vs swap usage at a glance.'],['vmstat 1','The si/so columns reveal live paging activity.']],
 got:'Swap on SSDs is survivable; swap on spinning disks under load is a standstill.',
 perf:'swappiness tunes the file-cache vs anonymous-page tradeoff; databases often lower it.'},
{cat:'memory',topic:'stack vs heap',t:'Stack vs heap — two allocators',
 d:'The stack holds call frames: automatic, LIFO, fast, small. The heap holds dynamic allocations: flexible, manual or GC-managed, slower. Stack overflow recurses too deep; heap leaks forget to free.',
 mech:'Each thread gets a stack that grows on call and shrinks on return. malloc() carves heap chunks from brk/mmap regions; free() returns them to the allocator (not always to the OS).',
 ex:[['ulimit -s','Stack size limit per thread (usually 8MB on Linux).'],['cat /proc/<pid>/maps | grep -E "stack|heap"','See both regions in a live process.']],
 got:'Returning a pointer to a stack variable is instant undefined behavior.',
 perf:'Arena allocators beat general malloc for short-lived bulk allocations.'},
{cat:'memory',topic:'memory-mapped files',t:'mmap — files as memory',
 d:'mmap() maps a file into the address space: reads become memory accesses, writes flush back. Shared mappings give zero-copy IPC; it is also how executables and shared libraries load.',
 mech:'The kernel populates pages on demand via page faults from the file\'s page cache. MAP_SHARED writes propagate to the file; MAP_PRIVATE gives copy-on-write snapshots.',
 ex:[['python3 -c "import mmap; m=mmap.mmap(-1, 4096); m.write(b\'hi\'); print(m[:2])"','Anonymous mmap as a byte buffer.'],['grep -c mmap /proc/<pid>/maps','Count of mapped regions in a process.']],
 got:'SIGBUS if the file shrinks under a mapping — size files before mapping them.',
 perf:'mmap I/O skips user/kernel copies; for sequential bulk reads, read() can still win.'},
{cat:'memory',topic:'copy on write',t:'Copy-on-write — lazy duplication',
 d:'Copy-on-write shares pages read-only until someone writes, then copies just that page. It makes fork() cheap and saves memory across processes running the same binaries.',
 mech:'Page-table entries are marked read-only and shared; a write triggers a fault, the kernel copies the page, marks it writable, and resumes. Reference counts track sharers.',
 ex:[['pmap -x <pid> | head','Shared vs private dirty pages per mapping.'],['cat /proc/meminfo | grep -i cow','COW fault counters (sometimes exposed).']],
 got:'Fork-heavy workloads with big heaps still pay when the child writes a lot — COW only defers the cost.',
 perf:'KSM (kernel same-page merging) extends COW to identical pages across VMs.'},
{cat:'filesystems',topic:'inodes',t:'Inodes — files without names',
 d:'An inode stores a file\'s metadata and block pointers; directory entries map names to inode numbers. Names are just labels — the inode is the file.',
 mech:'Each inode holds mode, owner, timestamps, and direct/indirect block pointers. df -i shows inode exhaustion, a distinct failure from disk-full.',
 ex:[['ls -i file','Shows the file\'s inode number.'],['df -i','Inode usage per filesystem — watch for 100% IUse%.']],
 got:'Deleting a name (unlink) only frees the inode when the last link and open handle go away.',
 perf:'Millions of tiny files exhaust inodes long before bytes — monitor both.'},
{cat:'filesystems',topic:'hard vs soft links',t:'Hard links vs symlinks',
 d:'Hard links are extra names for the same inode (same filesystem only); symlinks are tiny files holding a path (can dangle, can cross filesystems). ln makes hard links, ln -s makes symlinks.',
 mech:'A hard link bumps the inode\'s link count; the data survives until count and open handles reach zero. A symlink stores a path string that the kernel re-resolves on each access.',
 ex:[['ln a b && ls -i a b','Same inode number: one file, two names.'],['ln -s a c && ls -l c','Arrow notation shows the symlink target.']],
 got:'Editing a hard-linked file edits all its names — surprising when unexpected.',
 perf:'Symlink chains add path-resolution overhead; hard links cost nothing extra at access.'},
{cat:'filesystems',topic:'permissions',t:'Unix permissions — rwx bits',
 d:'Nine bits (owner/group/other × read/write/execute) plus setuid/setgid/sticky. Directories need x to traverse and w to create entries — r alone only lists names.',
 mech:'The kernel checks the applicable class on each open(); setuid runs the binary as its owner (careful!), the sticky bit on /tmp stops users deleting others\' files.',
 ex:[['chmod 640 secret','Owner read/write, group read, others nothing.'],['ls -l /tmp | head -1','The t flag: /tmp\'s sticky bit in action.']],
 got:'chmod -R 777 "fixes" access by destroying security — find the actual missing bit instead.',
 perf:'ACLs (setfacl) extend the nine bits for fine-grained sharing without group gymnastics.'},
{cat:'filesystems',topic:'journaling',t:'Journaling — crash consistency',
 d:'A journal records intended changes before applying them; after a crash, replay completes or rolls back partial work. That is why modern filesystems rarely need full fsck after power loss.',
 mech:'Write-ahead: journal the metadata (or data, in full journaling), commit, then checkpoint to the filesystem. Recovery replays the journal tail.',
 ex:[['dumpe2fs -h /dev/sda1 | grep -i journal','Journal parameters on an ext4 filesystem.'],['mount | grep -o "(.*)"','The (rw,relatime) options reveal journaling-adjacent settings.']],
 got:'Journaling protects metadata by default; file data needs data=journal mode (slower) for full protection.',
 perf:'Ordered mode (ext4 default) balances safety and speed for most workloads.'},
{cat:'filesystems',topic:'filesystem comparison',t:'ext4 vs XFS vs Btrfs vs ZFS',
 d:'ext4: the dependable default. XFS: high-throughput, huge files. Btrfs/ZFS: checksumming, snapshots, copy-on-write — self-healing storage at the cost of complexity and RAM.',
 mech:'Checksumming filesystems hash every block and verify on read, catching silent corruption. COW snapshots share unchanged blocks, making backups instant and cheap.',
 ex:[['df -T','Filesystem type per mount — know what you run.'],['zpool status','ZFS pool health at a glance (where ZFS is used).']],
 got:'Picking ZFS for a tiny VM wastes RAM; picking ext4 where you need snapshots wastes weekends.',
 perf:'Match the filesystem to the workload: databases love XFS/ext4; backup targets love ZFS/Btrfs.'},
{cat:'cpu-arch',topic:'x86-64 registers',t:'x86-64 registers — the CPU\'s desk',
 d:'x86-64 gives 16 general-purpose 64-bit registers (rax..r15), plus rip, rsp, rflags. Calling conventions pass the first arguments in registers (rdi, rsi, rdx...) — the fastest storage in the machine.',
 mech:'Instructions operate register-to-register in a cycle; spills go to the stack when the compiler runs out. Wider vector registers (xmm/ymm/zmm) handle SIMD.',
 ex:[['gcc -S -o - prog.c | head -30','See register allocation in real compiler output.'],['cat /proc/cpuinfo | grep -m1 "model name"','The CPU you are actually running on.']],
 got:'32-bit writes to eax zero the upper half of rax — a classic subtlety in assembly.',
 perf:'Keeping hot data in registers is the compiler\'s job; help it with small, tight loops.'},
{cat:'cpu-arch',topic:'cache hierarchy',t:'L1/L2/L3 caches — the memory pyramid',
 d:'Registers (1 cycle) → L1 (~4) → L2 (~12) → L3 (~40) → RAM (~200+) → SSD. Each level is bigger and slower; locality (using nearby data soon) is what makes the pyramid work.',
 mech:'Caches store 64-byte lines; a miss fetches the whole line. MESI keeps cores\' copies coherent. Prefetchers guess sequential/strided access patterns.',
 ex:[['lscpu','Cache sizes per level on this machine.'],['valgrind --tool=cachegrind ./prog','Measure real cache miss rates.']],
 got:'False sharing: two threads writing different variables on one cache line ping-pong it between cores.',
 perf:'Structure-of-arrays and blocking/tiling are cache-friendly transforms for hot loops.'},
{cat:'cpu-arch',topic:'pipelining',t:'Pipelining — assembly-line execution',
 d:'Modern CPUs overlap instruction stages (fetch, decode, execute...) like an assembly line, retiring multiple instructions per cycle. Hazards (data, control, structural) stall the line; branch prediction and out-of-order execution hide them.',
 mech:'Superscalar cores issue several micro-ops per cycle to multiple execution units. The reorder buffer retires them in program order, preserving correctness.',
 ex:[['perf stat -e cycles,instructions ./prog','IPC (instructions per cycle) reveals pipeline efficiency.'],['perf stat -e branch-misses ./prog','Mispredict counts show where the pipeline flushes.']],
 got:'A mispredicted branch flushes ~15-20 cycles of work — unpredictable branches are expensive.',
 perf:'Predictable branches, loop unrolling, and branchless tricks keep the pipeline fed.'},
{cat:'cpu-arch',topic:'endianness',t:'Endianness — byte order',
 d:'Little-endian (x86, ARM by default) stores the least significant byte first; big-endian (network order) stores the most significant first. Network protocols use big-endian — htons()/ntohs() convert.',
 mech:'The CPU\'s load/store unit orders bytes within multi-byte values per its endianness; mismatched peers must convert at the boundary.',
 ex:[['python3 -c "import sys; print(sys.byteorder)"','This machine\'s byte order.'],['xxd -l 4 -e /bin/ls | head -1','Hex dump in different endianness views.']],
 got:'Casting byte buffers to integers across architectures silently scrambles values.',
 perf:'Endianness rarely affects speed; it affects correctness at every protocol boundary.'},
{cat:'cpu-arch',topic:'risc vs cisc',t:'RISC vs CISC — philosophy, then convergence',
 d:'RISC: many simple fixed-size instructions, load/store architecture (ARM, RISC-V). CISC: fewer, complex instructions, memory operands (x86). Modern x86 decodes CISC into RISC-like micro-ops — the philosophies converged inside the chip.',
 mech:'RISC simplifies pipelining and decoding; CISC densifies code. Both now use out-of-order superscalar cores with micro-op caches.',
 ex:[['gcc -march=native -S -o - p.c | wc -l','Instruction count hints at ISA density.'],['cat /proc/cpuinfo | grep -m1 flags | tr " " "\\n" | grep -E "^(avx|sse|neon)" | head','SIMD extensions actually present.']],
 got:'ISA debates ignore the real differentiators: process node, microarchitecture, and power budget.',
 perf:'ARM\'s efficiency wins in phones; x86\'s throughput wins on desktops — workload and power envelope decide.'},
{cat:'virtualization',topic:'hypervisor types',t:'Type 1 vs Type 2 hypervisors',
 d:'Type 1 (bare-metal: KVM, Hyper-V, ESXi) runs directly on hardware; Type 2 (hosted: VirtualBox, VMware Workstation) runs atop an OS. Type 1 wins on performance and isolation; Type 2 wins on convenience.',
 mech:'Hardware extensions (Intel VT-x, AMD-V) let guests run privileged instructions safely via VM exits to the hypervisor. Paravirtualized drivers cut I/O overhead.',
 ex:[['ls /dev/kvm','KVM device present means hardware virtualization is available.'],['systemd-detect-virt','Detects if you are inside a VM and which kind.']],
 got:'Nested virtualization works but costs performance — test, don\'t assume.',
 perf:'For I/O-heavy guests, virtio drivers matter more than the hypervisor brand.'},
{cat:'virtualization',topic:'containers vs vms',t:'Containers vs VMs — isolation weight',
 d:'VMs virtualize hardware (own kernel each, heavy, strong isolation). Containers share the host kernel with namespace/cgroup isolation (light, fast, weaker blast radius). Different tools for different trust levels.',
 mech:'Namespaces (pid, net, mnt, uts, ipc, user) give each container its own view; cgroups cap CPU/memory/IO. No hardware emulation means near-native speed.',
 ex:[['ls /proc/self/ns','Your current namespaces — compare inside vs outside a container.'],['cat /proc/self/cgroup','Cgroup membership of this process.']],
 got:'A container escape is a host compromise — don\'t run mutually untrusted tenants in plain containers.',
 perf:'Containers start in milliseconds and pack densely; VMs boot in seconds with full isolation.'},
{cat:'virtualization',topic:'namespaces',t:'Linux namespaces — the container primitive',
 d:'Namespaces partition global resources so processes see private instances: PIDs, network stacks, mount points, hostnames, IPC, and user IDs. Seven namespaces compose a container.',
 mech:'clone() with CLONE_NEW* flags creates the namespaces; unshare() moves a process into new ones. User namespaces map container root to an unprivileged host UID.',
 ex:[['lsns','Lists all namespaces on the system and their owners.'],['unshare -n ip link','A shell with its own (empty) network namespace.']],
 got:'Just CLONE_NEWPID without the other namespaces is not a container — it is a process with a funny PID.',
 perf:'Namespaces are nearly free; the cost of containers is in image layers and orchestration, not the primitive.'},
{cat:'virtualization',topic:'cgroups',t:'cgroups — resource budgets',
 d:'Control groups cap and account CPU, memory, and I/O per process group. They are how containers get resource limits and how systemd manages services.',
 mech:'cgroup v2 unifies the hierarchy: cpu.max throttles, memory.max triggers reclaim/OOM-kill within the group, io.max shapes disk bandwidth. The OOM killer respects group boundaries.',
 ex:[['cat /proc/self/cgroup','Your cgroup path (v2 shows "0::/…").'],['systemd-cgtop','Live resource usage per cgroup.']],
 got:'Memory limits without swap accounting let processes dodge the cap via swap.',
 perf:'Right-size limits from measured p99 usage, not guesses — too tight causes throttling/OOMs.'}
];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?T.filter(function(x){return x.cat===opts.category;}):T;
  if(!pool.length)pool=T;
  var t=pick(pool,rnd);
  var exs=shuffle(t.ex,rnd).slice(0,2).map(function(x){return {example:x[0],explanation:x[1]};});
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:t.t,category:t.cat,topic:t.topic,
    description:t.d+' This record is Signature-generated original content: a compact systems reference entry written for this archive.',
    mechanics:t.mech,examples:exs,n_examples:exs.length,gotchas:t.got,performance_notes:t.perf,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-OSA-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.topic!=='string'||!r.topic.length)e.push('topic');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(typeof r.mechanics!=='string'||r.mechanics.length<80)e.push('mechanics');
  if(!Array.isArray(r.examples)||r.examples.length<2||r.examples.length>4)e.push('examples');
  else r.examples.forEach(function(x){if(!x||typeof x.example!=='string'||!x.example.length||typeof x.explanation!=='string'||!x.explanation.length)e.push('example');});
  /* REAL invariant: n_examples must equal the actual examples array length. */
  if(r.n_examples!==r.examples.length)e.push('n_examples');
  if(typeof r.gotchas!=='string'||!r.gotchas.length)e.push('gotchas');
  if(typeof r.performance_notes!=='string'||r.performance_notes.length<60)e.push('performance_notes');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-os-arch-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('os-arch',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
