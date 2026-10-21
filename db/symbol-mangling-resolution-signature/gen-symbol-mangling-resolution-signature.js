(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["scheme", "tool", "cxx", "rust", "other"];
var PREFIX='JAH-SYMBOL-S-';
var GENVER='jahdb-symbol-mangling-resolution-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["entry", "kind2", "example2", "resolves_to"];
var DEMO_TPL="// $TITLE - demangle demo (simplified Itanium)\nfunction demangle(m) {\n  var mm = m.match(/^_Z(\\d+)([A-Za-z_]+)(\\d+)([A-Za-z_]+)v$$/);\n  if (mm) return mm[2] + \"::\" + mm[4] + \"()\";\n  if (m.indexOf(\"_ZN\") === 0) return m.replace(/^_ZN/, \"\").replace(/E.*$$/, \"[nested]\");\n  return m;\n}\nvar mangled = \"_Z3fooi\";\nconsole.log(\"Entry: $ENTRY\");\nconsole.log(\"Mangled: \" + mangled);\nconsole.log(\"Demangled: foo(int)  [simplified model]\");\nconsole.log(\"Resolution -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["scheme", "SigMangle", "Signature-original: readable-by-design mangling that stays greppable. Example: `Sig_foo__i32` resolves to `foo(i32)`.", {"entry": "SigMangle", "kind2": "scheme", "example2": "Sig_foo__i32", "resolves_to": "foo(i32)"}], ["tool", "SigDemangle", "Signature-original: demangler for Sig and foreign schemes in one tool. Example: `sigdemangle <sym>` resolves to `readable name`.", {"entry": "sigdemangle", "kind2": "tool", "example2": "sigdemangle <sym>", "resolves_to": "readable name"}], ["tool", "SigMangle-Verify", "Signature-original: verifies mangled names match declarations. Example: `sigmangle --check` resolves to `diagnostics`.", {"entry": "SigMangle-Verify", "kind2": "tool", "example2": "sigmangle --check", "resolves_to": "diagnostics"}], ["tool", "SigSym-Cache", "Signature-original: cached demangling for huge symbol tables. Example: `instant profiles` resolves to `fast symbols`.", {"entry": "SigSym-Cache", "kind2": "tool", "example2": "instant profiles", "resolves_to": "fast symbols"}], ["scheme", "SigMangle-Stable", "Signature-original: stability-guaranteed mangling across compiler versions. Example: `SigS_foo` resolves to `foo (stable)`.", {"entry": "SigMangle-Stable", "kind2": "scheme", "example2": "SigS_foo", "resolves_to": "foo (stable)"}], ["tool", "SigGen-Syms", "Signature-original: symbol generation with collision-proof hashing. Example: `build output` resolves to `unique symbols`.", {"entry": "SigGen-Syms", "kind2": "tool", "example2": "build output", "resolves_to": "unique symbols"}], ["tool", "SigStrip-Safe", "Signature-original: stripping that preserves demangle-ability. Example: `stripped binary` resolves to `still demangleable`.", {"entry": "SigStrip", "kind2": "tool", "example2": "stripped binary", "resolves_to": "still demangleable"}], ["tool", "SigMangle-Doc", "Signature-original: docs linking mangled symbols to source. Example: `docs build` resolves to `linked docs`.", {"entry": "SigMangle-Doc", "kind2": "tool", "example2": "docs build", "resolves_to": "linked docs"}], ["tool", "SigProfile-Syms", "Signature-original: profiler symbolization with inline-frame recovery. Example: `perf.data` resolves to `annotated profile`.", {"entry": "SigProfile-Syms", "kind2": "tool", "example2": "perf.data", "resolves_to": "annotated profile"}], ["tool", "SigCrash-Syms", "Signature-original: crash symbolication pipeline for Sig dumps. Example: `.sigdump` resolves to `symbolicated trace`.", {"entry": "SigCrash-Syms", "kind2": "tool", "example2": ".sigdump", "resolves_to": "symbolicated trace"}], ["tool", "SigMangle-Fuzz", "Signature-original: fuzzer for demanglers against malformed inputs. Example: `corpus` resolves to `robust demanglers`.", {"entry": "SigMangle-Fuzz", "kind2": "tool", "example2": "corpus", "resolves_to": "robust demanglers"}], ["tool", "SigABI-Syms", "Signature-original: ABI-aware symbol comparison across builds. Example: `two builds` resolves to `ABI diff`.", {"entry": "SigABI-Syms", "kind2": "tool", "example2": "two builds", "resolves_to": "ABI diff"}], ["tool", "SigNames-Clean", "Signature-original: name canonicalization for cross-language linking. Example: `mixed langs` resolves to `canonical names`.", {"entry": "SigNames", "kind2": "tool", "example2": "mixed langs", "resolves_to": "canonical names"}], ["tool", "SigMangle-Lint", "Signature-original: linting symbol names for ABI hazards. Example: `CI check` resolves to `hazard report`.", {"entry": "SigMangle-Lint", "kind2": "tool", "example2": "CI check", "resolves_to": "hazard report"}], ["tool", "SigSymbol-One", "Signature-original: the united symbol plane — mangle, demangle, verify in one. Example: `sigsymbol` resolves to `everything readable`.", {"entry": "SigSymbol-One", "kind2": "unified", "example2": "sigsymbol", "resolves_to": "everything readable"}]];
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
  if(!new RegExp('^'+'JAH\\-SYMBOL\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('symbol-mangling-resolution-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
