(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["ffi", "bindings", "runtime", "jvm", "scripting"];
var PREFIX='JAH-PLF-';
var GENVER='jahdb-polyglot-linking-frameworks-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["framework", "bridges", "mechanism", "overhead"];
var DEMO_TPL="// $TITLE - FFI boundary demo (simulated)\nvar nativeLib = { add: function(a, b) { return a + b; } }; // \"C\" side\nfunction ffiCall(fn) {\n  return function() {\n    var args = Array.prototype.slice.call(arguments);\n    var t0 = Date.now();\n    var r = fn.apply(null, args);\n    return { result: r, boundary_us: (Date.now() - t0) * 1000 };\n  };\n}\nvar add = ffiCall(nativeLib.add);\nvar out = add(20, 22);\nconsole.log(\"Framework: $FRAMEWORK | Bridges: $BRIDGES\");\nconsole.log(\"add(20,22) across boundary = \" + out.result);\nconsole.log(\"Boundary crossed -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["jvm", "JNI", "Java Native Interface: the verbose but universal Java-to-C bridge. Bridges Java <-> C/C++ via JNIEnv calls; call overhead: moderate.", {"framework": "JNI", "bridges": "Java <-> C/C++", "mechanism": "JNIEnv calls", "overhead": "moderate"}], ["jvm", "JNA", "Java Native Access calls C libraries without writing any JNI glue. Bridges Java <-> C via libffi dynamic; call overhead: higher (dynamic).", {"framework": "JNA", "bridges": "Java <-> C", "mechanism": "libffi dynamic", "overhead": "higher (dynamic)"}], ["runtime", "P/Invoke", ".NET’s DllImport calling native exports with marshaling attributes. Bridges .NET <-> C via DllImport marshaling; call overhead: low-moderate.", {"framework": "P/Invoke", "bridges": ".NET <-> C", "mechanism": "DllImport marshaling", "overhead": "low-moderate"}], ["ffi", "libffi", "The Foreign Function Interface library behind Python ctypes, Ruby fiddle, and JNA. Bridges any <-> C via dynamic call frames; call overhead: moderate.", {"framework": "libffi", "bridges": "any <-> C", "mechanism": "dynamic call frames", "overhead": "moderate"}], ["scripting", "Cython", "Write C-speed extensions in Python-like syntax compiled to C. Bridges Python <-> C via compiled extensions; call overhead: near zero.", {"framework": "Cython", "bridges": "Python <-> C", "mechanism": "compiled extensions", "overhead": "near zero"}], ["scripting", "PyO3", "Rust bindings for Python with ergonomic macros and GIL handling. Bridges Python <-> Rust via extension modules; call overhead: low.", {"framework": "PyO3", "bridges": "Python <-> Rust", "mechanism": "extension modules", "overhead": "low"}], ["scripting", "pybind11", "Header-only C++11 bindings for Python with elegant type casters. Bridges Python <-> C++ via extension modules; call overhead: low.", {"framework": "pybind11", "bridges": "Python <-> C++", "mechanism": "extension modules", "overhead": "low"}], ["bindings", "SWIG", "Wraps C/C++ for dozens of languages from interface files. Bridges C/C++ -> many via generated wrappers; call overhead: low.", {"framework": "SWIG", "bridges": "C/C++ -> many", "mechanism": "generated wrappers", "overhead": "low"}], ["runtime", "wasm-bindgen", "Rust<->JavaScript bindings for WASM with wasm-pack publishing. Bridges Rust <-> JS (WASM) via generated shims; call overhead: low.", {"framework": "wasm-bindgen", "bridges": "Rust <-> JS (WASM)", "mechanism": "generated shims", "overhead": "low"}], ["runtime", "N-API", "Node’s ABI-stable C API for native addons surviving V8 upgrades. Bridges Node <-> C/C++ via stable ABI; call overhead: low.", {"framework": "N-API", "bridges": "Node <-> C/C++", "mechanism": "stable ABI", "overhead": "low"}], ["runtime", "GraalVM Polyglot", "Run JS, Python, Ruby, R on the JVM sharing objects with near-zero cost. Bridges JVM langs <-> each other via Truffle interop; call overhead: near zero.", {"framework": "GraalVM", "bridges": "JVM langs <-> each other", "mechanism": "Truffle interop", "overhead": "near zero"}], ["bindings", "cbindgen/bindgen", "Generate C headers from Rust and Rust bindings from C automatically. Bridges Rust <-> C via generated bindings; call overhead: zero.", {"framework": "bindgen", "bridges": "Rust <-> C", "mechanism": "generated bindings", "overhead": "zero"}], ["runtime", "COM interop", "Windows’ Component Object Model bridging languages via vtables. Bridges many <-> many (Windows) via vtable interfaces; call overhead: low.", {"framework": "COM", "bridges": "many <-> many (Windows)", "mechanism": "vtable interfaces", "overhead": "low"}], ["runtime", "D-Bus", "IPC message bus bridging processes and languages on Linux desktops. Bridges any <-> any (IPC) via message bus; call overhead: IPC-level.", {"framework": "D-Bus", "bridges": "any <-> any (IPC)", "mechanism": "message bus", "overhead": "IPC-level"}], ["scripting", "JEP (Java embedded Python)", "Embed CPython inside Java with shared interpreters. Bridges Java <-> Python via embedded interpreter; call overhead: low.", {"framework": "JEP", "bridges": "Java <-> Python", "mechanism": "embedded interpreter", "overhead": "low"}]];
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
  if(!new RegExp('^'+'JAH\\-PLF\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('polyglot-linking-frameworks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
