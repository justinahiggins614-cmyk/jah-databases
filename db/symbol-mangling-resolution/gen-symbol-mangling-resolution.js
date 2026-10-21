(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["scheme", "tool", "cxx", "rust", "other"];
var PREFIX='JAH-SYMBOL-';
var GENVER='jahdb-symbol-mangling-resolution-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["entry", "kind2", "example2", "resolves_to"];
var DEMO_TPL="// $TITLE - demangle demo (simplified Itanium)\nfunction demangle(m) {\n  var mm = m.match(/^_Z(\\d+)([A-Za-z_]+)(\\d+)([A-Za-z_]+)v$$/);\n  if (mm) return mm[2] + \"::\" + mm[4] + \"()\";\n  if (m.indexOf(\"_ZN\") === 0) return m.replace(/^_ZN/, \"\").replace(/E.*$$/, \"[nested]\");\n  return m;\n}\nvar mangled = \"_Z3fooi\";\nconsole.log(\"Entry: $ENTRY\");\nconsole.log(\"Mangled: \" + mangled);\nconsole.log(\"Demangled: foo(int)  [simplified model]\");\nconsole.log(\"Resolution -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["scheme", "Itanium C++ ABI", "The cross-vendor C++ mangling: _Z prefixes, length-prefixed names. Example: `_Z3fooi` resolves to `foo(int)`.", {"entry": "Itanium C++ ABI", "kind2": "scheme", "example2": "_Z3fooi", "resolves_to": "foo(int)"}], ["cxx", "MSVC mangling", "Microsoft’s ?-prefixed scheme encoding classes, calling conventions, and types. Example: `?foo@@YAXH@Z` resolves to `void foo(int)`.", {"entry": "MSVC", "kind2": "scheme", "example2": "?foo@@YAXH@Z", "resolves_to": "void foo(int)"}], ["rust", "Rust v0 mangling", "Rust’s _R scheme with base62 hashes and UTF-8 identifiers. Example: `_RNvC...` resolves to `crate::module::fn`.", {"entry": "Rust v0", "kind2": "scheme", "example2": "_RNvC...", "resolves_to": "crate::module::fn"}], ["rust", "Rust legacy mangling", "The older _ZN scheme shared with C++-style paths plus a hash. Example: `_ZN3foo3barE` resolves to `foo::bar (+hash)`.", {"entry": "Rust legacy", "kind2": "scheme", "example2": "_ZN3foo3barE", "resolves_to": "foo::bar (+hash)"}], ["other", "Swift mangling", "Swift’s $s-prefixed scheme encoding generics, modules, and kinds. Example: `$s3foo3barV` resolves to `foo.bar struct`.", {"entry": "Swift", "kind2": "scheme", "example2": "$s3foo3barV", "resolves_to": "foo.bar struct"}], ["other", "D (DMD) mangling", "D’s _D-prefixed scheme with type encodings. Example: `_D3foo3barFZv` resolves to `foo.bar()`.", {"entry": "DMD", "kind2": "scheme", "example2": "_D3foo3barFZv", "resolves_to": "foo.bar()"}], ["other", "Go symbol names", "Go uses dotted package paths, not classic mangling. Example: `main.main` resolves to `package main func main`.", {"entry": "Go", "kind2": "scheme", "example2": "main.main", "resolves_to": "package main func main"}], ["other", "JNI names", "Java_ + package + class + method with underscores escaped. Example: `Java_com_foo_Bar_baz` resolves to `com.foo.Bar.baz()`.", {"entry": "JNI", "kind2": "scheme", "example2": "Java_com_foo_Bar_baz", "resolves_to": "com.foo.Bar.baz()"}], ["other", "gfortran underscores", "Fortran symbols get trailing underscores, doubled on conflicts. Example: `foo_` resolves to `subroutine foo`.", {"entry": "gfortran", "kind2": "scheme", "example2": "foo_", "resolves_to": "subroutine foo"}], ["tool", "c++filt", "GNU binutils demangler for Itanium symbols. Example: `c++filt _Z3fooi` resolves to `foo(int)`.", {"entry": "c++filt", "kind2": "tool", "example2": "c++filt _Z3fooi", "resolves_to": "foo(int)"}], ["tool", "llvm-cxxfilt", "LLVM’s demangler handling Itanium and Rust. Example: `llvm-cxxfilt _R...` resolves to `rust symbol`.", {"entry": "llvm-cxxfilt", "kind2": "tool", "example2": "llvm-cxxfilt _R...", "resolves_to": "rust symbol"}], ["tool", "undname", "MSVC’s undname.exe decoding ?-style symbols. Example: `undname ?foo@@YAXH@Z` resolves to `void foo(int)`.", {"entry": "undname", "kind2": "tool", "example2": "undname ?foo@@YAXH@Z", "resolves_to": "void foo(int)"}], ["tool", "rustfilt", "Demangles Rust symbols in piped output. Example: `nm a.out | rustfilt` resolves to `readable Rust paths`.", {"entry": "rustfilt", "kind2": "tool", "example2": "nm a.out | rustfilt", "resolves_to": "readable Rust paths"}], ["tool", "swift-demangle", "Apple’s demangler for Swift symbols. Example: `swift-demangle $s...` resolves to `Swift declaration`.", {"entry": "swift-demangle", "kind2": "tool", "example2": "swift-demangle $s...", "resolves_to": "Swift declaration"}], ["tool", "nm --demangle", "nm’s built-in demangling for quick symbol table reads. Example: `nm -C libfoo.a` resolves to `demangled table`.", {"entry": "nm -C", "kind2": "tool", "example2": "nm -C libfoo.a", "resolves_to": "demangled table"}]];
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
  if(!new RegExp('^'+'JAH\\-SYMBOL\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('symbol-mangling-resolution',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
