(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["sql", "nosql", "orm", "online-ddl", "tooling"];
var PREFIX='JAH-AUTOMA4-S-';
var GENVER='jahdb-automated-schema-migrations-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tool", "writes_in", "strategy", "rollback"];
var DEMO_TPL="// $TITLE - migration runner demo\nvar migrations = [\n  { v: 1, up: \"CREATE TABLE users(id INT)\", down: \"DROP TABLE users\" },\n  { v: 2, up: \"ALTER TABLE users ADD COLUMN email TEXT\", down: \"ALTER TABLE users DROP COLUMN email\" }\n];\nvar applied = [];\nconsole.log(\"Tool: $TOOL | Strategy: $STRATEGY\");\nmigrations.forEach(function(m) { applied.push(m.v); console.log(\"  apply v\" + m.v + \": \" + m.up); });\nconsole.log(\"Schema at v\" + applied[applied.length - 1]);\nvar last = migrations.pop();\nconsole.log(\"  rollback v\" + last.v + \": \" + last.down + \" -> $ROLLBACK\");\nconsole.log(\"Migrations applied + rolled back -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["sql", "SigMigrate-Core", "Signature-original: versioned migrations with automatic online-DDL planning. Migrations written in SigSchema DSL; strategy: planned online; rollback: auto reverse.", {"tool": "SigMigrate", "writes_in": "SigSchema DSL", "strategy": "planned online", "rollback": "auto reverse"}], ["online-ddl", "SigMigrate-Zero", "Signature-original: zero-downtime migrations verified against production traffic shadows. Migrations written in SigSchema DSL; strategy: shadow-verified; rollback: instant.", {"tool": "SigMigrate-Zero", "writes_in": "SigSchema DSL", "strategy": "shadow-verified", "rollback": "instant"}], ["tooling", "SigSchema-DSL", "Signature-original: declarative schema language diffing to minimal migration plans. Migrations written in SigSchema DSL; strategy: declarative diff; rollback: inverse plan.", {"tool": "SigSchema", "writes_in": "SigSchema DSL", "strategy": "declarative diff", "rollback": "inverse plan"}], ["sql", "SigMigrate-Data", "Signature-original: data migrations with backfill batching and progress tracking. Migrations written in SigScript; strategy: batched backfill; rollback: compensating writes.", {"tool": "SigMigrate-Data", "writes_in": "SigScript", "strategy": "batched backfill", "rollback": "compensating writes"}], ["online-ddl", "SigMigrate-Branch", "Signature-original: branch-based schema dev with merge-time conflict detection. Migrations written in branches; strategy: branch + merge; rollback: branch drop.", {"tool": "SigMigrate-Branch", "writes_in": "branches", "strategy": "branch + merge", "rollback": "branch drop"}], ["tooling", "SigMigrate-Guard", "Signature-original: migration linting blocking dangerous ops (unbounded backfill). Migrations written in policy; strategy: lint gates; rollback: n/a.", {"tool": "SigGuard", "writes_in": "policy", "strategy": "lint gates", "rollback": "n/a"}], ["sql", "SigMigrate-Multi", "Signature-original: coordinated migrations across sharded databases. Migrations written in SigSchema DSL; strategy: shard-coordinated; rollback: per-shard reverse.", {"tool": "SigMigrate-Multi", "writes_in": "SigSchema DSL", "strategy": "shard-coordinated", "rollback": "per-shard reverse"}], ["tooling", "SigMigrate-Verify", "Signature-original: post-migration verification queries proving data integrity. Migrations written in checks; strategy: verify queries; rollback: alert + auto-reverse.", {"tool": "SigVerify", "writes_in": "checks", "strategy": "verify queries", "rollback": "alert + auto-reverse"}], ["sql", "SigMigrate-Time", "Signature-original: time-travel schemas querying data as of any migration. Migrations written in SigSchema DSL; strategy: versioned views; rollback: time query.", {"tool": "SigTime-Schema", "writes_in": "SigSchema DSL", "strategy": "versioned views", "rollback": "time query"}], ["tooling", "SigMigrate-Audit", "Signature-original: immutable audit of every schema change with approver chains. Migrations written in log; strategy: approved changes; rollback: audit replay.", {"tool": "SigAudit", "writes_in": "log", "strategy": "approved changes", "rollback": "audit replay"}], ["online-ddl", "SigMigrate-Canary", "Signature-original: canary migrations rolling out to 1% of shards first. Migrations written in SigSchema DSL; strategy: canary rollout; rollback: canary revert.", {"tool": "SigCanary-Migrate", "writes_in": "SigSchema DSL", "strategy": "canary rollout", "rollback": "canary revert"}], ["tooling", "SigMigrate-DryRun", "Signature-original: dry-run planning showing exact DDL and lock impact. Migrations written in plan; strategy: plan preview; rollback: n/a.", {"tool": "SigDryRun", "writes_in": "plan", "strategy": "plan preview", "rollback": "n/a"}], ["tooling", "SigMigrate-Seed", "Signature-original: versioned seed data traveling with migrations. Migrations written in SigScript; strategy: seed versions; rollback: seed down.", {"tool": "SigSeed", "writes_in": "SigScript", "strategy": "seed versions", "rollback": "seed down"}], ["tooling", "SigMigrate-Docs", "Signature-original: schema docs regenerated from every migration automatically. Migrations written in auto; strategy: doc generation; rollback: n/a.", {"tool": "SigDocs", "writes_in": "auto", "strategy": "doc generation", "rollback": "n/a"}], ["sql", "SigMigrate-One", "Signature-original: the united migration plane — one DSL for SQL, docs, and streams. Migrations written in SigSchema DSL; strategy: unified; rollback: unified reverse.", {"tool": "SigMigrate-One", "writes_in": "SigSchema DSL", "strategy": "unified", "rollback": "unified reverse"}]];
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
  if(!new RegExp('^'+'JAH\\-AUTOMA4\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-schema-migrations-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
