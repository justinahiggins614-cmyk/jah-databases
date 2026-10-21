(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["codemod", "lint-fix", "refactor", "query", "ide"];
var PREFIX='JAH-ASTREW-S-';
var GENVER='jahdb-ast-rewriting-rules-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["engine", "rewrites", "rule_lang", "scale"];
var DEMO_TPL="// $TITLE - AST rewrite demo\nvar AST = { type: \"Call\", name: \"oldApi\", args: [\"x\"] };\nvar rules = [\n  { match: function(n) { return n.type === \"Call\" && n.name === \"oldApi\"; },\n    rewrite: function(n) { return { type: \"Call\", name: \"newApi\", args: n.args.concat([\"opts\"]) }; } }\n];\nfunction applyRules(node) { rules.forEach(function(r) { if (r.match(node)) node = r.rewrite(node); }); return node; }\nconsole.log(\"Engine: $ENGINE | Rewrites: $REWRITES\");\nconsole.log(\"Before: \" + JSON.stringify(AST));\nconsole.log(\"After:  \" + JSON.stringify(applyRules(AST)));\nconsole.log(\"Rewrite applied -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["codemod", "SigRewrite-Core", "Signature-original: rewrite engine with provably semantics-preserving rules. Rewrites Sig AST; rules in SigRule DSL. Scale: Sig fleet.", {"engine": "SigRewrite", "rewrites": "Sig AST", "rule_lang": "SigRule DSL", "scale": "Sig fleet"}], ["codemod", "SigCodemod", "Signature-original: codemods with dry-run diffs and test-gated apply. Rewrites migrations; rules in Sig transform scripts. Scale: monorepos.", {"engine": "SigCodemod", "rewrites": "migrations", "rule_lang": "Sig transform scripts", "scale": "monorepos"}], ["lint-fix", "SigLint-Fix", "Signature-original: every lint has an autofix; CI applies safe ones. Rewrites violations; rules in fix rules. Scale: all Sig code.", {"engine": "SigLint", "rewrites": "violations", "rule_lang": "fix rules", "scale": "all Sig code"}], ["refactor", "SigRefactor", "Signature-original: IDE-grade refactors (rename/extract/move) for Sig langs. Rewrites refactors; rules in refactor ops. Scale: IDEs.", {"engine": "SigRefactor", "rewrites": "refactors", "rule_lang": "refactor ops", "scale": "IDEs"}], ["query", "SigQuery-AST", "Signature-original: AST queries with structural patterns and metavars. Rewrites query (find); rules in pattern DSL. Scale: analysis.", {"engine": "SigQuery", "rewrites": "query (find)", "rule_lang": "pattern DSL", "scale": "analysis"}], ["codemod", "SigMigrate-Auto", "Signature-original: automatic API migration codemods with deprecation maps. Rewrites API upgrades; rules in migration maps. Scale: ecosystem.", {"engine": "SigMigrate-Auto", "rewrites": "API upgrades", "rule_lang": "migration maps", "scale": "ecosystem"}], ["codemod", "SigVerify-Rewrite", "Signature-original: rewrites verified by differential testing before landing. Rewrites verified; rules in verified rules. Scale: critical code.", {"engine": "SigVerify-RW", "rewrites": "verified", "rule_lang": "verified rules", "scale": "critical code"}], ["lint-fix", "SigFormat-Enforce", "Signature-original: formatting as rewrite rules, not a separate tool. Rewrites formatting; rules in format rules. Scale: all code.", {"engine": "SigFormat", "rewrites": "formatting", "rule_lang": "format rules", "scale": "all code"}], ["refactor", "SigDead-Elim", "Signature-original: dead-code elimination as composable rewrite rules. Rewrites dead code; rules in elim rules. Scale: builds.", {"engine": "SigDead-RW", "rewrites": "dead code", "rule_lang": "elim rules", "scale": "builds"}], ["refactor", "SigInline-RW", "Signature-original: inlining decisions expressed as rewrite rules. Rewrites inlining; rules in inline rules. Scale: optimizer.", {"engine": "SigInline-RW", "rewrites": "inlining", "rule_lang": "inline rules", "scale": "optimizer"}], ["codemod", "SigTest-Gen", "Signature-original: test generation rewrites creating tests from code. Rewrites test synthesis; rules in gen rules. Scale: CI.", {"engine": "SigTest-Gen", "rewrites": "test synthesis", "rule_lang": "gen rules", "scale": "CI"}], ["codemod", "SigDoc-Gen", "Signature-original: doc generation as AST rewrites attaching docs. Rewrites docs; rules in doc rules. Scale: docs.", {"engine": "SigDoc-Gen", "rewrites": "docs", "rule_lang": "doc rules", "scale": "docs"}], ["refactor", "SigPerf-RW", "Signature-original: performance rewrites applying known fast patterns. Rewrites perf patterns; rules in perf rules. Scale: hot paths.", {"engine": "SigPerf-RW", "rewrites": "perf patterns", "rule_lang": "perf rules", "scale": "hot paths"}], ["lint-fix", "SigSecure-RW", "Signature-original: security rewrites fixing vulnerable patterns automatically. Rewrites vuln patterns; rules in security rules. Scale: fleet.", {"engine": "SigSecure-RW", "rewrites": "vuln patterns", "rule_lang": "security rules", "scale": "fleet"}], ["codemod", "SigRewrite-One", "Signature-original: the united rewriting plane — one rule language, every language. Rewrites everything; rules in SigRule. Scale: planetary.", {"engine": "SigRewrite-One", "rewrites": "everything", "rule_lang": "SigRule", "scale": "planetary"}]];
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
  if(!new RegExp('^'+'JAH\\-ASTREW\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ast-rewriting-rules-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
