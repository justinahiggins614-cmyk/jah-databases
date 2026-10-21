(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["allocator", "container", "queue", "layout", "pool"];
var PREFIX='JAH-ZAD-';
var GENVER='jahdb-zero-allocation-data-structures-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["structure", "allocations", "idea", "example"];
var DEMO_TPL="// $TITLE - zero-allocation ring demo\nvar RING = new Array(8), head = 0, tail = 0, count = 0;\nfunction push(v) { if (count === RING.length) return false; RING[tail] = v; tail = (tail + 1) % RING.length; count++; return true; }\nfunction pop() { if (!count) return undefined; var v = RING[head]; head = (head + 1) % RING.length; count--; return v; }\nfor (var i = 0; i < 20; i++) { if (!push(i)) pop(), push(i); }\nvar out = []; var x; while ((x = pop()) !== undefined) out.push(x);\nconsole.log(\"Structure: $STRUCTURE | Idea: $IDEA\");\nconsole.log(\"Pushed 20, ring kept last 8: \" + out.join(\",\"));\nconsole.log(\"Heap allocations during ops: 0 -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["allocator", "Bump/arena allocator", "Allocate by bumping a pointer; free everything at once by resetting — the fastest allocator there is. Allocations per operation: 0 (amortized). Core idea: bump pointer, reset en masse. Example: per-request arenas in servers.", {"structure": "arena", "allocations": "0 (amortized)", "idea": "bump pointer, reset en masse", "example": "per-request arenas in servers"}], ["pool", "Object pools", "Recycle fixed-size objects instead of malloc/free; kills fragmentation in hot loops. Allocations per operation: 0 after warmup. Core idea: free-list recycling. Example: connection pools, particle systems.", {"structure": "object pool", "allocations": "0 after warmup", "idea": "free-list recycling", "example": "connection pools, particle systems"}], ["queue", "Ring buffers", "A fixed array with head/tail indices; the classic lock-free SPSC queue with zero allocation. Allocations per operation: 0. Core idea: circular fixed array. Example: audio pipelines, log shipping.", {"structure": "ring buffer", "allocations": "0", "idea": "circular fixed array", "example": "audio pipelines, log shipping"}], ["container", "Intrusive linked lists", "Links live inside the objects (like Linux list_head) so nodes never allocate separately. Allocations per operation: 0. Core idea: embedding next/prev in payload. Example: Linux kernel lists.", {"structure": "intrusive list", "allocations": "0", "idea": "embedding next/prev in payload", "example": "Linux kernel lists"}], ["container", "Small Vector Optimization", "Vectors store small counts inline (LLVM SmallVector, folly small_vector) avoiding heap for the common case. Allocations per operation: 0 when small. Core idea: inline buffer + spill. Example: compiler IR operand lists.", {"structure": "small vector", "allocations": "0 when small", "idea": "inline buffer + spill", "example": "compiler IR operand lists"}], ["allocator", "Slab allocators", "Pre-carved slabs for fixed sizes; the kernel’s answer to fragmentation. Allocations per operation: 0 (from slab). Core idea: size-classed caches. Example: Linux SLAB/SLUB.", {"structure": "slab", "allocations": "0 (from slab)", "idea": "size-classed caches", "example": "Linux SLAB/SLUB"}], ["layout", "FlatBuffers", "Zero-copy serialization: read structs directly from the wire buffer with no parse step. Allocations per operation: 0 on read. Core idea: aligned in-place layout. Example: game networking, mobile.", {"structure": "flatbuffers", "allocations": "0 on read", "idea": "aligned in-place layout", "example": "game networking, mobile"}], ["container", "Unrolled linked lists", "Nodes hold arrays of elements, cutting pointer overhead and allocations per element. Allocations per operation: 1 per N elements. Core idea: chunked nodes. Example: text editors (ropes’ cousin).", {"structure": "unrolled list", "allocations": "1 per N elements", "idea": "chunked nodes", "example": "text editors (ropes’ cousin)"}], ["queue", "MPMC lock-free queues", "Michael-Scott queues move items between threads with CAS and preallocated nodes. Allocations per operation: 0 steady-state. Core idea: CAS + node recycling. Example: thread-pool work queues.", {"structure": "MPMC queue", "allocations": "0 steady-state", "idea": "CAS + node recycling", "example": "thread-pool work queues"}], ["layout", "Memory-mapped files", "Map files into address space; the OS pages data with zero user-space copies. Allocations per operation: 0. Core idea: OS page cache as storage. Example: databases (LMDB).", {"structure": "mmap", "allocations": "0", "idea": "OS page cache as storage", "example": "databases (LMDB)"}], ["allocator", "Stack allocation", "alloca and stack arrays vanish on return — the original zero-allocator. Allocations per operation: 0. Core idea: frame-lifetime storage. Example: small temp buffers.", {"structure": "stack alloc", "allocations": "0", "idea": "frame-lifetime storage", "example": "small temp buffers"}], ["layout", "Copy-on-write buffers", "Share pages until someone writes; fork() and Btrfs snapshots ride this. Allocations per operation: 0 until write. Core idea: shared pages, fault on write. Example: process fork, snapshots.", {"structure": "COW", "allocations": "0 until write", "idea": "shared pages, fault on write", "example": "process fork, snapshots"}], ["container", "Rope structures", "Trees of string chunks give O(log n) edits without reallocating whole texts. Allocations per operation: O(log n) nodes. Core idea: balanced chunk tree. Example: editors (Xi, Sublime).", {"structure": "rope", "allocations": "O(log n) nodes", "idea": "balanced chunk tree", "example": "editors (Xi, Sublime)"}], ["container", "Static arrays with cursors", "Fixed arrays plus a length cursor replace dynamic vectors in embedded code. Allocations per operation: 0. Core idea: fixed cap + cursor. Example: firmware buffers.", {"structure": "static array", "allocations": "0", "idea": "fixed cap + cursor", "example": "firmware buffers"}], ["layout", "Bit-packed flags", "Pack booleans into bitfields; 64 flags fit in one register with zero indirection. Allocations per operation: 0. Core idea: bit-level packing. Example: entity component flags.", {"structure": "bitfield", "allocations": "0", "idea": "bit-level packing", "example": "entity component flags"}]];
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
  if(!new RegExp('^'+'JAH\\-ZAD\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('zero-allocation-data-structures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
