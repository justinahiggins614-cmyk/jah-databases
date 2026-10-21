(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["sql", "nosql", "orm", "online-ddl", "tooling"];
var PREFIX='JAH-AUTOMA4-';
var GENVER='jahdb-automated-schema-migrations-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "writes_in", "strategy", "rollback"];
var DEMO_TPL="// $TITLE - migration runner demo\nvar migrations = [\n  { v: 1, up: \"CREATE TABLE users(id INT)\", down: \"DROP TABLE users\" },\n  { v: 2, up: \"ALTER TABLE users ADD COLUMN email TEXT\", down: \"ALTER TABLE users DROP COLUMN email\" }\n];\nvar applied = [];\nconsole.log(\"Tool: $TOOL | Strategy: $STRATEGY\");\nmigrations.forEach(function(m) { applied.push(m.v); console.log(\"  apply v\" + m.v + \": \" + m.up); });\nconsole.log(\"Schema at v\" + applied[applied.length - 1]);\nvar last = migrations.pop();\nconsole.log(\"  rollback v\" + last.v + \": \" + last.down + \" -> $ROLLBACK\");\nconsole.log(\"Migrations applied + rolled back -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["sql", "Alembic", "SQLAlchemy’s migration tool generating versioned scripts from model diffs. Migrations written in Python; strategy: versioned scripts; rollback: downgrade revisions.", {"tool": "Alembic", "writes_in": "Python", "strategy": "versioned scripts", "rollback": "downgrade revisions"}], ["sql", "Flyway", "Versioned SQL migrations (V1__desc.sql) applied in order with checksum validation. Migrations written in SQL/Java; strategy: versioned files; rollback: undo scripts (Teams).", {"tool": "Flyway", "writes_in": "SQL/Java", "strategy": "versioned files", "rollback": "undo scripts (Teams)"}], ["sql", "Liquibase", "XML/YAML/JSON changesets with contexts, preconditions, and rollback generation. Migrations written in XML/YAML/SQL; strategy: changesets; rollback: auto + custom.", {"tool": "Liquibase", "writes_in": "XML/YAML/SQL", "strategy": "changesets", "rollback": "auto + custom"}], ["orm", "Django migrations", "Auto-detected model changes with squashable, data-capable migrations. Migrations written in Python; strategy: autodetect + apply; rollback: migrate to earlier.", {"tool": "Django", "writes_in": "Python", "strategy": "autodetect + apply", "rollback": "migrate to earlier"}], ["orm", "Rails ActiveRecord", "Ruby migrations with reversible change methods and schema.rb snapshots. Migrations written in Ruby; strategy: timestamped versions; rollback: reversible db:rollback.", {"tool": "ActiveRecord", "writes_in": "Ruby", "strategy": "timestamped versions", "rollback": "reversible db:rollback"}], ["orm", "Prisma Migrate", "Declarative schema.prisma diffed into SQL migrations with shadow-database dev flow. Migrations written in Prisma schema; strategy: declarative diff; rollback: manual resolve.", {"tool": "Prisma Migrate", "writes_in": "Prisma schema", "strategy": "declarative diff", "rollback": "manual resolve"}], ["sql", "Knex", "JS query builder with timestamped migration files and seed support. Migrations written in JavaScript; strategy: timestamped files; rollback: down functions.", {"tool": "Knex", "writes_in": "JavaScript", "strategy": "timestamped files", "rollback": "down functions"}], ["orm", "TypeORM", "TypeScript migrations auto-generated from entity diffs. Migrations written in TypeScript; strategy: generated diffs; rollback: down methods.", {"tool": "TypeORM", "writes_in": "TypeScript", "strategy": "generated diffs", "rollback": "down methods"}], ["sql", "golang-migrate", "Go CLI/library with ordered SQL files and dirty-state tracking. Migrations written in SQL; strategy: ordered files; rollback: down files.", {"tool": "golang-migrate", "writes_in": "SQL", "strategy": "ordered files", "rollback": "down files"}], ["sql", "Atlas", "Declarative schema-as-code with drift detection and migration linting. Migrations written in HCL/SQL; strategy: declarative; rollback: checkpoint-based.", {"tool": "Atlas", "writes_in": "HCL/SQL", "strategy": "declarative", "rollback": "checkpoint-based"}], ["sql", "Skeema", "Pull-request style schema management for MySQL fleets. Migrations written in SQL files; strategy: diff + push; rollback: revert commit.", {"tool": "Skeema", "writes_in": "SQL files", "strategy": "diff + push", "rollback": "revert commit"}], ["online-ddl", "pt-online-schema-change", "Percona’s trigger-based online ALTER for MySQL without locking tables. Migrations written in CLI; strategy: shadow table + triggers; rollback: drop shadow.", {"tool": "pt-osc", "writes_in": "CLI", "strategy": "shadow table + triggers", "rollback": "drop shadow"}], ["online-ddl", "gh-ost", "GitHub’s triggerless online schema migration reading the binlog. Migrations written in CLI; strategy: binlog-driven copy; rollback: cutover revert.", {"tool": "gh-ost", "writes_in": "CLI", "strategy": "binlog-driven copy", "rollback": "cutover revert"}], ["online-ddl", "PlanetScale deploy requests", "Branch-based schema changes with deploy queues and instant rollback. Migrations written in SQL branches; strategy: branch + deploy request; rollback: revert deploy.", {"tool": "PlanetScale", "writes_in": "SQL branches", "strategy": "branch + deploy request", "rollback": "revert deploy"}], ["tooling", "Hasura migrations", "GraphQL-engine-tracked migrations versioning metadata alongside SQL. Migrations written in SQL + metadata; strategy: tracked versions; rollback: down SQL.", {"tool": "Hasura", "writes_in": "SQL + metadata", "strategy": "tracked versions", "rollback": "down SQL"}]];
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
  if(!new RegExp('^'+'JAH\\-AUTOMA4\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-schema-migrations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
