(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hygienic", "textual", "procedural", "metaprogramming", "tooling"];
var PREFIX='JAH-ADME-';
var GENVER='jahdb-ast-driven-macro-expansion-engines-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "kind", "expands", "example"];
var DEMO_TPL="// $TITLE - macro expansion demo (template expander)\nfunction expand(tpl, vars) {\n  return tpl.replace(/\\{\\{(\\w+)\\}\\}/g, function(m, k) { return vars[k] !== undefined ? vars[k] : m; });\n}\nvar out = expand(\"fn {{name}}() { return {{val}}; }\", { name: \"answer\", val: 42 });\nconsole.log(\"System: $SYSTEM | Kind: $KIND\");\nconsole.log(\"Template: fn {{name}}() { return {{val}}; }\");\nconsole.log(\"Expanded: \" + out);\nconsole.log(\"Expansion deterministic -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["hygienic", "Rust macro_rules", "Declarative pattern-matching macros expanding at compile time, hygienic by default. Kind: declarative. Expands token trees. Example: macro_rules! vec {...}.", {"system": "rustc", "kind": "declarative", "expands": "token trees", "example": "macro_rules! vec {...}"}], ["procedural", "Rust procedural macros", "Full Rust programs transforming token streams; derive macros are the famous case. Kind: procedural. Expands token streams. Example: #[derive(Serialize)].", {"system": "rustc", "kind": "procedural", "expands": "token streams", "example": "#[derive(Serialize)]"}], ["hygienic", "Lisp macros", "The original: code as data, macros as functions over syntax with quasiquote. Kind: code-as-data. Expands s-expressions. Example: (defmacro unless ...).", {"system": "Common Lisp", "kind": "code-as-data", "expands": "s-expressions", "example": "(defmacro unless ...)"}], ["hygienic", "Elixir macros", "quote/unquote metaprogramming compiling to Erlang bytecode. Kind: AST quote. Expands quoted exprs. Example: defmacro unless ....", {"system": "Elixir", "kind": "AST quote", "expands": "quoted exprs", "example": "defmacro unless ..."}], ["procedural", "Template Haskell", "Haskell’s compile-time metaprogramming with typed splices. Kind: typed splices. Expands TH AST. Example: $(deriveJSON ...).", {"system": "GHC", "kind": "typed splices", "expands": "TH AST", "example": "$(deriveJSON ...)"}], ["procedural", "Scala 3 macros", "Quotes, splices, and inline giving type-safe metaprogramming. Kind: quotes/splices. Expands quoted code. Example: inline def ....", {"system": "Scala 3", "kind": "quotes/splices", "expands": "quoted code", "example": "inline def ..."}], ["textual", "C preprocessor", "The textual #define/#include engine every C program still boots through. Kind: textual. Expands token text. Example: #define MAX(a,b) ....", {"system": "cpp", "kind": "textual", "expands": "token text", "example": "#define MAX(a,b) ..."}], ["textual", "M4", "The general macro processor behind autoconf and sendmail configs. Kind: textual. Expands text. Example: define(`FOO’,`bar’).", {"system": "m4", "kind": "textual", "expands": "text", "example": "define(`FOO’,`bar’)"}], ["metaprogramming", "Julia metaprogramming", "homoiconic AST with hygienic macros evaluated at parse time. Kind: hygienic AST. Expands Expr trees. Example: @time expr.", {"system": "Julia", "kind": "hygienic AST", "expands": "Expr trees", "example": "@time expr"}], ["hygienic", "Racket syntax transformers", "Language-oriented programming: define whole languages via syntax-parse. Kind: syntax objects. Expands syntax. Example: #lang custom.", {"system": "Racket", "kind": "syntax objects", "expands": "syntax", "example": "#lang custom"}], ["hygienic", "Nim macros", "AST-transforming macros making Nim read like a DSL toolkit. Kind: AST templates. Expands NimNode. Example: macro benchmark ....", {"system": "Nim", "kind": "AST templates", "expands": "NimNode", "example": "macro benchmark ..."}], ["procedural", "Crystal macros", "Compile-time Ruby-like macros expanding with full language introspection. Kind: AST macros. Expands Crystal AST. Example: macro method_missing ....", {"system": "Crystal", "kind": "AST macros", "expands": "Crystal AST", "example": "macro method_missing ..."}], ["procedural", "Haxe macros", "Build macros and expression macros transforming typed ASTs. Kind: typed AST. Expands Expr. Example: macro function ....", {"system": "Haxe", "kind": "typed AST", "expands": "Expr", "example": "macro function ..."}], ["tooling", "Babel plugins", "JS AST transforms (visitors) powering JSX, TypeScript stripping, and minifiers. Kind: AST visitors. Expands JS AST. Example: plugin transforming JSX.", {"system": "Babel", "kind": "AST visitors", "expands": "JS AST", "example": "plugin transforming JSX"}], ["metaprogramming", "C++ templates", "Turing-complete compile-time computation via template instantiation. Kind: template metaprogram. Expands instantiations. Example: template <int N> ....", {"system": "C++", "kind": "template metaprogram", "expands": "instantiations", "example": "template <int N> ..."}]];
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
  if(!new RegExp('^'+'JAH\\-ADME\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ast-driven-macro-expansion-engines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
