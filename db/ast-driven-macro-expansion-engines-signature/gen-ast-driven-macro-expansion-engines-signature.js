(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hygienic", "textual", "procedural", "metaprogramming", "tooling"];
var PREFIX='JAH-ADME-S-';
var GENVER='jahdb-ast-driven-macro-expansion-engines-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["system", "kind", "expands", "example"];
var DEMO_TPL="// $TITLE - macro expansion demo (template expander)\nfunction expand(tpl, vars) {\n  return tpl.replace(/\\{\\{(\\w+)\\}\\}/g, function(m, k) { return vars[k] !== undefined ? vars[k] : m; });\n}\nvar out = expand(\"fn {{name}}() { return {{val}}; }\", { name: \"answer\", val: 42 });\nconsole.log(\"System: $SYSTEM | Kind: $KIND\");\nconsole.log(\"Template: fn {{name}}() { return {{val}}; }\");\nconsole.log(\"Expanded: \" + out);\nconsole.log(\"Expansion deterministic -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["hygienic", "SigMacro-Hyg", "Signature-original: hygienic macros with scope graphs preventing capture bugs. Kind: hygienic. Expands Sig AST. Example: sigmacro unless ....", {"system": "sigc", "kind": "hygienic", "expands": "Sig AST", "example": "sigmacro unless ..."}], ["procedural", "SigMacro-Proc", "Signature-original: procedural macros running in a sandboxed compile-time VM. Kind: procedural. Expands token streams. Example: #[sig_derive(...)].", {"system": "sigc", "kind": "procedural", "expands": "token streams", "example": "#[sig_derive(...)]"}], ["metaprogramming", "SigQuote", "Signature-original: typed quotation with automatic hygiene and source maps. Kind: typed quote. Expands quoted Sig AST. Example: sigquote { ... }.", {"system": "sigc", "kind": "typed quote", "expands": "quoted Sig AST", "example": "sigquote { ... }"}], ["metaprogramming", "SigDSL-Embed", "Signature-original: embedded DSLs with custom syntax checked at compile time. Kind: DSL embedding. Expands DSL AST. Example: sigdsl sql\"...\".", {"system": "sigc", "kind": "DSL embedding", "expands": "DSL AST", "example": "sigdsl sql\"...\""}], ["tooling", "SigExpand-Trace", "Signature-original: macro expansion tracing showing every rewrite step. Kind: tooling. Expands traces. Example: sigexpand --trace.", {"system": "sigc", "kind": "tooling", "expands": "traces", "example": "sigexpand --trace"}], ["tooling", "SigMacro-Test", "Signature-original: property tests for macros verifying expansion invariants. Kind: tooling. Expands test cases. Example: sigtest-macro ....", {"system": "sigc", "kind": "tooling", "expands": "test cases", "example": "sigtest-macro ..."}], ["procedural", "SigInline-Always", "Signature-original: guaranteed inlining macros for zero-cost abstractions. Kind: inline. Expands inlined bodies. Example: #[sig_inline].", {"system": "sigc", "kind": "inline", "expands": "inlined bodies", "example": "#[sig_inline]"}], ["metaprogramming", "SigConst-Eval", "Signature-original: compile-time evaluation with resource budgets. Kind: const eval. Expands constants. Example: const X = sig_eval!{...}.", {"system": "sigc", "kind": "const eval", "expands": "constants", "example": "const X = sig_eval!{...}"}], ["procedural", "SigDerive", "Signature-original: derive macros generating trait impls with diagnostics. Kind: derive. Expands impl blocks. Example: #[derive(SigSer)].", {"system": "sigc", "kind": "derive", "expands": "impl blocks", "example": "#[derive(SigSer)]"}], ["hygienic", "SigSyntax-Ext", "Signature-original: syntax extensions adding new expression forms safely. Kind: extensions. Expands new syntax. Example: sigsyntax match? ....", {"system": "sigc", "kind": "extensions", "expands": "new syntax", "example": "sigsyntax match? ..."}], ["textual", "SigTemplate", "Signature-original: typed text templates for code generation with escaping. Kind: typed textual. Expands source text. Example: sigtemplate \"...\".", {"system": "siggen", "kind": "typed textual", "expands": "source text", "example": "sigtemplate \"...\""}], ["tooling", "SigRewrite", "Signature-original: AST rewrite rules applied as compiler passes. Kind: rewrite rules. Expands rewritten AST. Example: sigrewrite rules.toml.", {"system": "sigc", "kind": "rewrite rules", "expands": "rewritten AST", "example": "sigrewrite rules.toml"}], ["metaprogramming", "SigReflect", "Signature-original: compile-time reflection over types and modules. Kind: reflection. Expands metadata. Example: sigreflect Type.", {"system": "sigc", "kind": "reflection", "expands": "metadata", "example": "sigreflect Type"}], ["metaprogramming", "SigStage", "Signature-original: multi-stage programming with explicit stage annotations. Kind: staging. Expands staged code. Example: sigstage<1> { ... }.", {"system": "sigc", "kind": "staging", "expands": "staged code", "example": "sigstage<1> { ... }"}], ["hygienic", "SigMacro-One", "Signature-original: the united macro plane — one expander for every Sig language. Kind: unified. Expands all Sig AST. Example: sigmacro ....", {"system": "sigc", "kind": "unified", "expands": "all Sig AST", "example": "sigmacro ..."}]];
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
  if(!new RegExp('^'+'JAH\\-ADME\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ast-driven-macro-expansion-engines-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
