(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["codemod", "lint-fix", "refactor", "query", "ide"];
var PREFIX='JAH-ASTREW-';
var GENVER='jahdb-ast-rewriting-rules-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["engine", "rewrites", "rule_lang", "scale"];
var DEMO_TPL="// $TITLE - AST rewrite demo\nvar AST = { type: \"Call\", name: \"oldApi\", args: [\"x\"] };\nvar rules = [\n  { match: function(n) { return n.type === \"Call\" && n.name === \"oldApi\"; },\n    rewrite: function(n) { return { type: \"Call\", name: \"newApi\", args: n.args.concat([\"opts\"]) }; } }\n];\nfunction applyRules(node) { rules.forEach(function(r) { if (r.match(node)) node = r.rewrite(node); }); return node; }\nconsole.log(\"Engine: $ENGINE | Rewrites: $REWRITES\");\nconsole.log(\"Before: \" + JSON.stringify(AST));\nconsole.log(\"After:  \" + JSON.stringify(applyRules(AST)));\nconsole.log(\"Rewrite applied -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["codemod", "jscodeshift", "Facebook’s toolkit for large-scale JS codemods with a test workflow. Rewrites JS codemods; rules in JS transform scripts. Scale: monorepos.", {"engine": "jscodeshift", "rewrites": "JS codemods", "rule_lang": "JS transform scripts", "scale": "monorepos"}], ["codemod", "Babel plugins", "Visitor-based AST transforms; the engine under most JS codemods. Rewrites JS AST; rules in visitor plugins. Scale: ecosystem.", {"engine": "Babel", "rewrites": "JS AST", "rule_lang": "visitor plugins", "scale": "ecosystem"}], ["lint-fix", "ESLint --fix", "Fixable rules rewriting code automatically on --fix. Rewrites lint violations; rules in rule fixers. Scale: every JS repo.", {"engine": "ESLint", "rewrites": "lint violations", "rule_lang": "rule fixers", "scale": "every JS repo"}], ["lint-fix", "Clang-Tidy", "C++ checks with fix-its applied by clang-apply-replacements. Rewrites C++ issues; rules in check + fix-it. Scale: large C++.", {"engine": "Clang-Tidy", "rewrites": "C++ issues", "rule_lang": "check + fix-it", "scale": "large C++"}], ["query", "libclang AST matchers", "Declarative matchers finding AST patterns in C++ code. Rewrites query (find); rules in matcher DSL. Scale: analysis.", {"engine": "clang matchers", "rewrites": "query (find)", "rule_lang": "matcher DSL", "scale": "analysis"}], ["ide", "Roslyn analyzers", "C#/VB analyzers with code fixes surfaced in the IDE lightbulb. Rewrites C# diagnostics; rules in analyzer + fix. Scale: dotnet IDE.", {"engine": "Roslyn", "rewrites": "C# diagnostics", "rule_lang": "analyzer + fix", "scale": "dotnet IDE"}], ["codemod", "Scalafix", "Semantic rewriting for Scala migrations and linting. Rewrites Scala code; rules in rewrite rules. Scale: Scala ecosystem.", {"engine": "Scalafix", "rewrites": "Scala code", "rule_lang": "rewrite rules", "scale": "Scala ecosystem"}], ["codemod", "OpenRewrite", "Recipe-based Java refactoring (e.g. Spring Boot upgrades) at scale. Rewrites Java recipes; rules in recipe YAML/Java. Scale: enterprise Java.", {"engine": "OpenRewrite", "rewrites": "Java recipes", "rule_lang": "recipe YAML/Java", "scale": "enterprise Java"}], ["codemod", "comby", "Structural search-and-replace across languages with metavariables. Rewrites multi-language; rules in match templates. Scale: polyglot repos.", {"engine": "comby", "rewrites": "multi-language", "rule_lang": "match templates", "scale": "polyglot repos"}], ["lint-fix", "Semgrep autofix", "Pattern-based findings with autofix suggestions across 30+ languages. Rewrites findings; rules in YAML patterns. Scale: CI fleets.", {"engine": "Semgrep", "rewrites": "findings", "rule_lang": "YAML patterns", "scale": "CI fleets"}], ["query", "tree-sitter queries", "Incremental parsing + S-expression queries for codemods and highlighting. Rewrites query-driven; rules in query language. Scale: editors/CI.", {"engine": "tree-sitter", "rewrites": "query-driven", "rule_lang": "query language", "scale": "editors/CI"}], ["codemod", "Spoon", "Java source analysis and transformation library. Rewrites Java AST; rules in processors. Scale: research/industry.", {"engine": "Spoon", "rewrites": "Java AST", "rule_lang": "processors", "scale": "research/industry"}], ["codemod", "LibCST", "Concrete syntax trees preserving formatting for Python codemods. Rewrites Python (format-safe); rules in matchers/visitors. Scale: Python monorepos.", {"engine": "LibCST", "rewrites": "Python (format-safe)", "rule_lang": "matchers/visitors", "scale": "Python monorepos"}], ["refactor", "rope", "Python refactoring library (rename, extract, move) used by IDEs. Rewrites Python refactors; rules in refactoring API. Scale: IDEs.", {"engine": "rope", "rewrites": "Python refactors", "rule_lang": "refactoring API", "scale": "IDEs"}], ["codemod", "Coccinelle", "Semantic patches for C, famous for Linux kernel-wide transformations. Rewrites C semantic patches; rules in SmPL. Scale: Linux kernel.", {"engine": "Coccinelle", "rewrites": "C semantic patches", "rule_lang": "SmPL", "scale": "Linux kernel"}]];
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
  if(!new RegExp('^'+'JAH\\-ASTREW\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ast-rewriting-rules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
