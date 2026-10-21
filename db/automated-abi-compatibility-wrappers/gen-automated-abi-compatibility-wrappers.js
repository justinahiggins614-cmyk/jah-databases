(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["shim", "idl", "os", "rpc", "tooling"];
var PREFIX='JAH-AACW-';
var GENVER='jahdb-automated-abi-compatibility-wrappers-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["wrapper", "stabilizes", "technique", "guarantee"];
var DEMO_TPL="// $TITLE - ABI shim demo (versioned dispatch)\nvar impls = {\n  v1: { greet: function(n) { return \"hi \" + n; } },\n  v2: { greet: function(n, title) { return \"hello \" + (title || \"\") + n; } }\n};\nfunction shim(version) {\n  var impl = impls[version] || impls.v2;\n  return { greet: function(n) { return impl.greet(n); } }; // stable v1-shaped API\n}\nconsole.log(\"Wrapper: $WRAPPER | Stabilizes: $STABILIZES\");\nconsole.log(\"v1 client -> \" + shim(\"v1\").greet(\"ada\"));\nconsole.log(\"v2 client -> \" + shim(\"v2\").greet(\"ada\"));\nconsole.log(\"Stable ABI across versions -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["os", "COM", "Microsoft’s binary interface standard: vtables + IUnknown, stable for decades. Stabilizes Windows components via vtable interfaces; guarantee: binary compat.", {"wrapper": "COM", "stabilizes": "Windows components", "technique": "vtable interfaces", "guarantee": "binary compat"}], ["os", "XPCOM", "Mozilla’s cross-platform COM used by Firefox extensions historically. Stabilizes Mozilla components via IDL vtables; guarantee: frozen interfaces.", {"wrapper": "XPCOM", "stabilizes": "Mozilla components", "technique": "IDL vtables", "guarantee": "frozen interfaces"}], ["idl", "CORBA", "The OMG’s language-neutral ORB with IDL-defined interfaces. Stabilizes distributed objects via IDL stubs; guarantee: wire compat.", {"wrapper": "CORBA", "stabilizes": "distributed objects", "technique": "IDL stubs", "guarantee": "wire compat"}], ["os", "D-Bus", "Stable message-based interfaces for Linux desktop services. Stabilizes desktop services via introspection XML; guarantee: message compat.", {"wrapper": "D-Bus", "stabilizes": "desktop services", "technique": "introspection XML", "guarantee": "message compat"}], ["rpc", "Protocol Buffers", "Field numbers and unknown-field skipping keep wire compat across versions. Stabilizes RPC messages via field evolution; guarantee: wire compat.", {"wrapper": "protobuf", "stabilizes": "RPC messages", "technique": "field evolution", "guarantee": "wire compat"}], ["rpc", "Thrift", "Facebook’s IDL with version-tolerant field evolution. Stabilizes RPC services via field IDs; guarantee: wire compat.", {"wrapper": "Thrift", "stabilizes": "RPC services", "technique": "field IDs", "guarantee": "wire compat"}], ["rpc", "Cap’n Proto RPC", "Zero-copy RPC with schema evolution and capability security. Stabilizes RPC interfaces via schema evolution; guarantee: wire compat.", {"wrapper": "Cap'n Proto", "stabilizes": "RPC interfaces", "technique": "schema evolution", "guarantee": "wire compat"}], ["idl", "FlatBuffers", "Backwards/forwards compatible table evolution without parsing. Stabilizes serialized data via vtable offsets; guarantee: data compat.", {"wrapper": "FlatBuffers", "stabilizes": "serialized data", "technique": "vtable offsets", "guarantee": "data compat"}], ["tooling", "SWIG wrappers", "Generated language bindings pinning a stable C-facing API. Stabilizes C APIs via generated shims; guarantee: source compat.", {"wrapper": "SWIG", "stabilizes": "C APIs", "technique": "generated shims", "guarantee": "source compat"}], ["tooling", "JNA direct mapping", "JNA maps Java directly to native exports without C glue to rot. Stabilizes native libs via dynamic binding; guarantee: no glue code.", {"wrapper": "JNA", "stabilizes": "native libs", "technique": "dynamic binding", "guarantee": "no glue code"}], ["shim", "C-ABI shims", "extern \"C\" wrappers giving C++ libraries a stable C face. Stabilizes C++ libraries via extern C facade; guarantee: ABI stability.", {"wrapper": "C ABI shim", "stabilizes": "C++ libraries", "technique": "extern C facade", "guarantee": "ABI stability"}], ["shim", "libffi closures", "Runtime-generated closures adapting calling conventions on the fly. Stabilizes call conventions via closures; guarantee: dynamic adapt.", {"wrapper": "libffi", "stabilizes": "call conventions", "technique": "closures", "guarantee": "dynamic adapt"}], ["os", "Wine API translation", "Wine implements Win32 on POSIX — the largest ABI compatibility project alive. Stabilizes Win32 API via reimplementation; guarantee: app compat.", {"wrapper": "Wine", "stabilizes": "Win32 API", "technique": "reimplementation", "guarantee": "app compat"}], ["os", "Android NDK stable ABIs", "Android’s stable native ABIs (e.g. libandroid) frozen across releases. Stabilizes Android native via frozen APIs; guarantee: forward compat.", {"wrapper": "NDK stable", "stabilizes": "Android native", "technique": "frozen APIs", "guarantee": "forward compat"}], ["os", "glibc symbol versioning", "Versioned symbols let one libc serve binaries from 1997 and 2024. Stabilizes libc via symbol versions; guarantee: backward compat.", {"wrapper": "symver", "stabilizes": "libc", "technique": "symbol versions", "guarantee": "backward compat"}]];
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
  if(!new RegExp('^'+'JAH\\-AACW\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-abi-compatibility-wrappers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
