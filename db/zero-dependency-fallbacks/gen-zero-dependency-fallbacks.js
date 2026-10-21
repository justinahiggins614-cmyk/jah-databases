(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["binary", "library", "shell", "embed", "libc"];
var PREFIX='JAH-ZDF-';
var GENVER='jahdb-zero-dependency-fallbacks-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["name", "deps", "size_kb", "kind2"];
var DEMO_TPL="// $TITLE - zero-dependency audit\nvar T = { name: \"$NAME\", deps: $DEPS, size_kb: \"$SIZE_KB\" };\nconsole.log(\"Tool: \" + T.name + \" (\" + \"$KIND2\" + \")\");\nconsole.log(\"External dependencies: \" + T.deps);\nconsole.log(\"Size: ~\" + T.size_kb + \" KB\");\nconsole.log(T.deps === 0 ? \"VERDICT: zero-dependency fallback READY\" : \"VERDICT: needs vendoring\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["binary", "Go static binaries", "Go links everything statically by default, so a Go binary runs on any same-arch Linux with no runtime. It ships with 0 external dependencies at about 8000 KB.", {"name": "go static binary", "deps": "0", "size_kb": "8000", "kind2": "binary"}], ["binary", "Rust musl static builds", "Targeting x86_64-unknown-linux-musl produces fully static Rust binaries with no glibc dependency. It ships with 0 external dependencies at about 2500 KB.", {"name": "rust musl build", "deps": "0", "size_kb": "2500", "kind2": "binary"}], ["shell", "BusyBox", "One binary replacing 300+ Unix utilities, the standard fallback shell environment in containers. It ships with 0 external dependencies at about 1200 KB.", {"name": "BusyBox", "deps": "0", "size_kb": "1200", "kind2": "shell"}], ["shell", "Toybox", "Android’s BSD-licensed toolbox; a clean-room zero-dependency command set for minimal systems. It ships with 0 external dependencies at about 900 KB.", {"name": "Toybox", "deps": "0", "size_kb": "900", "kind2": "shell"}], ["library", "SQLite amalgamation", "The entire database engine ships as one 250K-line sqlite3.c you compile straight into your app. It ships with 0 external dependencies at about 1500 KB.", {"name": "SQLite amalgamation", "deps": "0", "size_kb": "1500", "kind2": "library"}], ["embed", "Lua 5.4 embed", "Lua’s whole interpreter is ~300 KB of C with no dependencies, the classic embeddable fallback. It ships with 0 external dependencies at about 300 KB.", {"name": "Lua", "deps": "0", "size_kb": "300", "kind2": "embed"}], ["library", "stb single-header libs", "Sean Barrett’s public-domain single-header image, font, and container libraries need only #include. It ships with 0 external dependencies at about 400 KB.", {"name": "stb libraries", "deps": "0", "size_kb": "400", "kind2": "library"}], ["library", "miniz", "A single-file zlib-compatible compressor/decompressor for PNG and zip without linking zlib. It ships with 0 external dependencies at about 120 KB.", {"name": "miniz", "deps": "0", "size_kb": "120", "kind2": "library"}], ["binary", "dropbear SSH", "A tiny SSH server/client replacing OpenSSH where every kilobyte counts, as in routers. It ships with 0 external dependencies at about 350 KB.", {"name": "dropbear", "deps": "0", "size_kb": "350", "kind2": "binary"}], ["binary", "uutils multicall binary", "Rust coreutils as one multicall binary — a memory-safe fallback for GNU coreutils. It ships with 0 external dependencies at about 6000 KB.", {"name": "uutils", "deps": "0", "size_kb": "6000", "kind2": "binary"}], ["embed", "QuickJS", "Fabrice Bellard’s small embeddable JS engine with ES2020 support in a few hundred KB. It ships with 0 external dependencies at about 600 KB.", {"name": "QuickJS", "deps": "0", "size_kb": "600", "kind2": "embed"}], ["libc", "Cosmopolitan Libc", "Actually Portable Executables run on Linux, macOS, Windows, and BSD from one binary. It ships with 0 external dependencies at about 1800 KB.", {"name": "Cosmopolitan APE", "deps": "0", "size_kb": "1800", "kind2": "libc"}], ["binary", "s6 supervision suite", "skarnet’s daemontools-style supervision with static binaries for init-less containers. It ships with 0 external dependencies at about 700 KB.", {"name": "s6", "deps": "0", "size_kb": "700", "kind2": "binary"}], ["binary", "Deno single executable", "Deno compiles scripts to self-contained executables with the runtime and V8 bundled. It ships with 0 external dependencies at about 90000 KB.", {"name": "deno compile", "deps": "0", "size_kb": "90000", "kind2": "binary"}], ["libc", "static-pie builds", "Static PIE binaries get ASLR without a dynamic loader — hardened and dependency-free. It ships with 0 external dependencies at about 2000 KB.", {"name": "static-pie", "deps": "0", "size_kb": "2000", "kind2": "libc"}]];
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
  if(!new RegExp('^'+'JAH\\-ZDF\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('zero-dependency-fallbacks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
