(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["elf", "macho", "pe", "wasm", "linker"];
var PREFIX='JAH-DSRT-S-';
var GENVER='jahdb-dynamic-symbol-relocation-tables-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["mechanism", "format", "resolves", "cost"];
var DEMO_TPL="// $TITLE - relocation demo (GOT/PLT model)\nvar GOT = {};\nfunction pltCall(name, impl) {\n  if (!GOT[name]) { GOT[name] = impl; console.log(\"  lazy bind: resolved \" + name); }\n  return GOT[name]();\n}\nfunction puts() { return \"hello from libc\"; }\nconsole.log(\"Mechanism: $MECHANISM | Format: $FORMAT\");\nconsole.log(\"call 1: \" + pltCall(\"puts\", puts));\nconsole.log(\"call 2: \" + pltCall(\"puts\", puts) + \" (cached, no re-resolve)\");\nconsole.log(\"Lazy binding -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["linker", "SigRel-Lazy", "Signature-original: lazy binding with signed symbol manifests. Format: SigELF. Resolves verified symbols; cost: first-call.", {"mechanism": "SigLazy", "format": "SigELF", "resolves": "verified symbols", "cost": "first-call"}], ["linker", "SigRel-Eager", "Signature-original: eager binding mode for latency-critical startup. Format: SigELF. Resolves all at load; cost: startup.", {"mechanism": "SigEager", "format": "SigELF", "resolves": "all at load", "cost": "startup"}], ["linker", "SigRel-Cache", "Signature-original: relocation caches making repeated loads instant. Format: SigELF. Resolves cached addrs; cost: cache hit.", {"mechanism": "SigRelCache", "format": "SigELF", "resolves": "cached addrs", "cost": "cache hit"}], ["linker", "SigRel-Verify", "Signature-original: every resolved symbol checked against the manifest. Format: SigELF. Resolves attested symbols; cost: verify.", {"mechanism": "SigVerify", "format": "SigELF", "resolves": "attested symbols", "cost": "verify"}], ["linker", "SigRel-Mesh", "Signature-original: symbols resolved from mesh peers when local libs miss. Format: SigELF. Resolves mesh symbols; cost: fetch.", {"mechanism": "SigMesh-Rel", "format": "SigELF", "resolves": "mesh symbols", "cost": "fetch"}], ["linker", "SigRel-Sandbox", "Signature-original: capability-scoped symbol namespaces for plugins. Format: SigELF. Resolves scoped symbols; cost: check.", {"mechanism": "SigSandbox", "format": "SigELF", "resolves": "scoped symbols", "cost": "check"}], ["linker", "SigRel-HotSwap", "Signature-original: hot-swappable symbols for live-updated libraries. Format: SigELF. Resolves live symbols; cost: swap.", {"mechanism": "SigHotSwap", "format": "SigELF", "resolves": "live symbols", "cost": "swap"}], ["linker", "SigRel-Delta", "Signature-original: delta relocations shipping only changed addresses. Format: SigELF. Resolves delta addrs; cost: apply.", {"mechanism": "SigDelta-Rel", "format": "SigELF", "resolves": "delta addrs", "cost": "apply"}], ["linker", "SigRel-Static", "Signature-original: static linking mode with full LTO for single binaries. Format: SigELF. Resolves link-time; cost: link.", {"mechanism": "SigStatic", "format": "SigELF", "resolves": "link-time", "cost": "link"}], ["linker", "SigRel-Profile", "Signature-original: profile-guided symbol ordering for cache locality. Format: SigELF. Resolves ordered symbols; cost: layout.", {"mechanism": "SigRel-Profile", "format": "SigELF", "resolves": "ordered symbols", "cost": "layout"}], ["linker", "SigRel-Audit", "Signature-original: relocation audit logs for supply-chain forensics. Format: SigELF. Resolves logged; cost: log.", {"mechanism": "SigAudit", "format": "SigELF", "resolves": "logged", "cost": "log"}], ["linker", "SigRel-Fuzz", "Signature-original: fuzzer for the loader itself against malformed inputs. Format: SigELF. Resolves n/a; cost: test.", {"mechanism": "SigFuzz-LD", "format": "SigELF", "resolves": "n/a", "cost": "test"}], ["linker", "SigRel-Compact", "Signature-original: compact relocation encoding shrinking binaries. Format: SigELF. Resolves addresses; cost: decode.", {"mechanism": "SigCompact", "format": "SigELF", "resolves": "addresses", "cost": "decode"}], ["linker", "SigRel-Parallel", "Signature-original: parallel relocation using all cores at startup. Format: SigELF. Resolves addresses; cost: parallel.", {"mechanism": "SigParallel", "format": "SigELF", "resolves": "addresses", "cost": "parallel"}], ["linker", "SigRel-One", "Signature-original: the united relocation plane — one loader for every Sig format. Format: Sig*. Resolves everything; cost: unified.", {"mechanism": "SigRel-One", "format": "Sig*", "resolves": "everything", "cost": "unified"}]];
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
  if(!new RegExp('^'+'JAH\\-DSRT\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dynamic-symbol-relocation-tables-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
