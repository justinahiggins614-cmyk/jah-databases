(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["linux", "windows", "macos", "mobile", "wasm", "embedded"];
var PREFIX='JAH-CCT-';
var GENVER='jahdb-cross-compilation-targets-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["triple", "toolchain", "os", "arch", "use"];
var DEMO_TPL="// $TITLE - target triple parser\nvar triple = \"$TRIPLE\";\nvar parts = triple.split(\"-\");\nconsole.log(\"Triple: \" + triple);\nconsole.log(\"Arch: \" + parts[0]);\nconsole.log(\"Vendor: \" + (parts[1] || \"?\"));\nconsole.log(\"OS/ABI: \" + parts.slice(2).join(\"-\"));\nconsole.log(\"Toolchain: $TOOLCHAIN | Use: $USE\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["linux", "x86_64 Linux GNU", "The default 64-bit Linux server target; glibc ABI, the baseline everything else compares to. Toolchain: rustc/gcc/clang; OS: Linux; architecture: x86_64. Typical use: servers, containers.", {"triple": "x86_64-unknown-linux-gnu", "toolchain": "rustc/gcc/clang", "os": "Linux", "arch": "x86_64", "use": "servers, containers"}], ["windows", "x86_64 Windows MSVC", "Windows builds with the Microsoft ABI; links against MSVCRT via the MSVC toolchain. Toolchain: rustc/msvc; OS: Windows; architecture: x86_64. Typical use: Windows desktop apps.", {"triple": "x86_64-pc-windows-msvc", "toolchain": "rustc/msvc", "os": "Windows", "arch": "x86_64", "use": "Windows desktop apps"}], ["macos", "Apple Silicon macOS", "The aarch64 macOS target; universal binaries pair it with x86_64-apple-darwin. Toolchain: rustc/clang; OS: macOS; architecture: aarch64. Typical use: M1/M2/M3 Mac apps.", {"triple": "aarch64-apple-darwin", "toolchain": "rustc/clang", "os": "macOS", "arch": "aarch64", "use": "M1/M2/M3 Mac apps"}], ["linux", "ARM64 Linux", "aarch64 servers (Graviton, Ampere) and Raspberry Pi 64-bit builds. Toolchain: rustc/gcc; OS: Linux; architecture: aarch64. Typical use: ARM servers, Pi.", {"triple": "aarch64-unknown-linux-gnu", "toolchain": "rustc/gcc", "os": "Linux", "arch": "aarch64", "use": "ARM servers, Pi"}], ["wasm", "WASI preview 1", "The original WASI target for sandboxed server-side WASM with file and clock access. Toolchain: rustc/clang; OS: WASI; architecture: wasm32. Typical use: portable WASM modules.", {"triple": "wasm32-wasi", "toolchain": "rustc/clang", "os": "WASI", "arch": "wasm32", "use": "portable WASM modules"}], ["macos", "Intel macOS", "The legacy Intel Mac target, still shipped in universal binaries for older hardware. Toolchain: rustc/clang; OS: macOS; architecture: x86_64. Typical use: Intel Mac apps.", {"triple": "x86_64-apple-darwin", "toolchain": "rustc/clang", "os": "macOS", "arch": "x86_64", "use": "Intel Mac apps"}], ["linux", "RISC-V 64 Linux", "The open-ISA 64-bit target gaining real silicon from StarFive and SiFive boards. Toolchain: rustc/gcc; OS: Linux; architecture: riscv64. Typical use: RISC-V boards.", {"triple": "riscv64gc-unknown-linux-gnu", "toolchain": "rustc/gcc", "os": "Linux", "arch": "riscv64", "use": "RISC-V boards"}], ["embedded", "ARMv7 hard-float Linux", "32-bit ARM with hardware float; the classic Raspberry Pi OS target. Toolchain: rustc/gcc; OS: Linux; architecture: armv7. Typical use: 32-bit ARM boards.", {"triple": "armv7-unknown-linux-gnueabihf", "toolchain": "rustc/gcc", "os": "Linux", "arch": "armv7", "use": "32-bit ARM boards"}], ["mobile", "Android ARM64", "Bionic libc Android target; the NDK exposes it for native libraries. Toolchain: rustc/ndk-clang; OS: Android; architecture: aarch64. Typical use: Android native code.", {"triple": "aarch64-linux-android", "toolchain": "rustc/ndk-clang", "os": "Android", "arch": "aarch64", "use": "Android native code"}], ["linux", "x86_64 musl static", "Fully static Linux binaries via musl — the Alpine/container minimal target. Toolchain: rustc/musl-gcc; OS: Linux; architecture: x86_64. Typical use: static containers.", {"triple": "x86_64-unknown-linux-musl", "toolchain": "rustc/musl-gcc", "os": "Linux", "arch": "x86_64", "use": "static containers"}], ["windows", "32-bit Windows MSVC", "i686 Windows for legacy 32-bit desktop deployments. Toolchain: rustc/msvc; OS: Windows; architecture: i686. Typical use: legacy Windows apps.", {"triple": "i686-pc-windows-msvc", "toolchain": "rustc/msvc", "os": "Windows", "arch": "i686", "use": "legacy Windows apps"}], ["linux", "POWER8+ little-endian", "IBM Power servers running Linux; big in HPC and enterprise Linux distros. Toolchain: gcc; OS: Linux; architecture: powerpc64le. Typical use: IBM Power servers.", {"triple": "powerpc64le-unknown-linux-gnu", "toolchain": "gcc", "os": "Linux", "arch": "powerpc64le", "use": "IBM Power servers"}], ["linux", "IBM Z mainframe", "s390x big-endian mainframe Linux — the banking and airline target. Toolchain: gcc; OS: Linux; architecture: s390x. Typical use: mainframes.", {"triple": "s390x-unknown-linux-gnu", "toolchain": "gcc", "os": "Linux", "arch": "s390x", "use": "mainframes"}], ["wasm", "bare wasm32", "WASM with no OS interface at all; the host must provide every import. Toolchain: rustc; OS: none; architecture: wasm32. Typical use: browser WASM, plugins.", {"triple": "wasm32-unknown-unknown", "toolchain": "rustc", "os": "none", "arch": "wasm32", "use": "browser WASM, plugins"}], ["linux", "LoongArch 64", "China’s LoongArch ISA target, now tier-2 in Rust and GCC. Toolchain: gcc/rustc; OS: Linux; architecture: loongarch64. Typical use: Loongson systems.", {"triple": "loongarch64-unknown-linux-gnu", "toolchain": "gcc/rustc", "os": "Linux", "arch": "loongarch64", "use": "Loongson systems"}]];
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
  if(!new RegExp('^'+'JAH\\-CCT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cross-compilation-targets',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
