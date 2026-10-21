(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["elf", "macho", "pe", "wasm", "linker"];
var PREFIX='JAH-DSRT-';
var GENVER='jahdb-dynamic-symbol-relocation-tables-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["mechanism", "format", "resolves", "cost"];
var DEMO_TPL="// $TITLE - relocation demo (GOT/PLT model)\nvar GOT = {};\nfunction pltCall(name, impl) {\n  if (!GOT[name]) { GOT[name] = impl; console.log(\"  lazy bind: resolved \" + name); }\n  return GOT[name]();\n}\nfunction puts() { return \"hello from libc\"; }\nconsole.log(\"Mechanism: $MECHANISM | Format: $FORMAT\");\nconsole.log(\"call 1: \" + pltCall(\"puts\", puts));\nconsole.log(\"call 2: \" + pltCall(\"puts\", puts) + \" (cached, no re-resolve)\");\nconsole.log(\"Lazy binding -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["elf", "ELF .dynsym", "The dynamic symbol table listing symbols the loader must resolve. Format: ELF. Resolves exported/imported symbols; cost: hash lookup.", {"mechanism": ".dynsym", "format": "ELF", "resolves": "exported/imported symbols", "cost": "hash lookup"}], ["elf", "ELF .rela relocations", "Relocation entries patching addresses at load or lazily. Format: ELF. Resolves addresses; cost: per-reloc patch.", {"mechanism": ".rela.*", "format": "ELF", "resolves": "addresses", "cost": "per-reloc patch"}], ["elf", "GOT/PLT", "Global Offset Table + Procedure Linkage Table enabling lazy function binding. Format: ELF. Resolves function addresses; cost: first-call bind.", {"mechanism": "GOT/PLT", "format": "ELF", "resolves": "function addresses", "cost": "first-call bind"}], ["macho", "Mach-O dyld stubs", "Apple’s lazy binding stubs with dyld resolving on first call. Format: Mach-O. Resolves lazy symbols; cost: first-call bind.", {"mechanism": "dyld stubs", "format": "Mach-O", "resolves": "lazy symbols", "cost": "first-call bind"}], ["pe", "PE import tables", "Windows’ Import Address Table filled by the loader from DLLs. Format: PE. Resolves DLL imports; cost: load-time.", {"mechanism": "IAT", "format": "PE", "resolves": "DLL imports", "cost": "load-time"}], ["pe", "COFF relocations", "Relocation records in object files patched by the linker. Format: COFF. Resolves object addresses; cost: link-time.", {"mechanism": "COFF reloc", "format": "COFF", "resolves": "object addresses", "cost": "link-time"}], ["wasm", "WASM import section", "WASM modules declare imports; the host satisfies them at instantiation. Format: WASM. Resolves host functions; cost: instantiation.", {"mechanism": "import section", "format": "WASM", "resolves": "host functions", "cost": "instantiation"}], ["linker", "ld.so", "The Linux dynamic linker resolving DT_NEEDED chains and symbols. Format: ELF. Resolves shared libs; cost: startup.", {"mechanism": "ld.so", "format": "ELF", "resolves": "shared libs", "cost": "startup"}], ["linker", "Lazy binding", "LD_BIND_NOW=1 disables laziness; default binds on first call. Format: ELF/Mach-O. Resolves on first use; cost: amortized.", {"mechanism": "lazy binding", "format": "ELF/Mach-O", "resolves": "on first use", "cost": "amortized"}], ["elf", "Symbol versioning", "Version scripts pinning symbol versions so old binaries keep working. Format: ELF GNU. Resolves versioned symbols; cost: lookup.", {"mechanism": "symver", "format": "ELF GNU", "resolves": "versioned symbols", "cost": "lookup"}], ["linker", "Prelink", "prelink pre-assigns load addresses to cut startup relocation work. Format: ELF. Resolves preassigned addrs; cost: precompute.", {"mechanism": "prelink", "format": "ELF", "resolves": "preassigned addrs", "cost": "precompute"}], ["linker", "ASLR effects", "Address randomization forces full relocation every exec — the security tax. Format: all. Resolves randomized bases; cost: full reloc each run.", {"mechanism": "ASLR", "format": "all", "resolves": "randomized bases", "cost": "full reloc each run"}], ["elf", "DT_NEEDED chains", "Dependency tags forming the library load graph the loader walks. Format: ELF. Resolves library graph; cost: graph walk.", {"mechanism": "DT_NEEDED", "format": "ELF", "resolves": "library graph", "cost": "graph walk"}], ["linker", "rpath/runpath", "Embedded library search paths controlling where the loader looks first. Format: ELF. Resolves library paths; cost: path search.", {"mechanism": "rpath", "format": "ELF", "resolves": "library paths", "cost": "path search"}], ["elf", "Copy relocations", "The loader copies data symbols into the executable — a classic footgun. Format: ELF. Resolves data symbols; cost: copy at load.", {"mechanism": "copy reloc", "format": "ELF", "resolves": "data symbols", "cost": "copy at load"}]];
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
  if(!new RegExp('^'+'JAH\\-DSRT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dynamic-symbol-relocation-tables',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
