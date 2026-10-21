(function(){'use strict';
var PREFIX="JAH-ATK237-";
var METHODS=[["Schema diffing", "Compute a precise field-level diff between schema versions: added, removed, renamed, retyped."], ["Compatibility classification", "Classify each change as backward-compatible, forward-compatible, or breaking."], ["Expand-contract planning", "Plan in phases: add new fields, dual-write, migrate readers, then remove old fields."], ["Data backfill planning", "Size and schedule backfills for new required fields over historical records."], ["Type-change risk analysis", "Flag narrowing conversions (float->int, longer->shorter strings) with data-loss estimates."], ["Rename detection", "Detect renames vs drop+add by matching field semantics, preventing silent data orphaning."], ["Consumer impact analysis", "Map every schema field to its consuming applications and flag who breaks."], ["Rollback planning", "Ensure every migration step has a tested reverse step before the first forward step runs."], ["Canary migrations", "Migrate a small collection first and verify before the fleet follows."], ["Migration dry runs", "Simulate the full plan against a copy and report what would change."], ["Constraint validation", "Re-validate uniqueness, not-null, and foreign-key constraints under the new schema."], ["Versioned schema registry", "Keep every schema version with its migration history as a permanent record."], ["Downtime estimation", "Estimate read/write impact per phase so maintenance windows are sized honestly."], ["Post-migration verification", "Re-run data quality checks after cutover and compare record counts and samples."], ["Communication plans", "Generate per-consumer notices describing exactly what changes for them and when."]];
var CATS=["migration", "schemas", "planning"];
var DEMO="# Schema Migration Planner demo: diff -> classify -> expand/contract plan.\nOLD={\"id\":\"int\",\"name\":\"str\",\"age\":\"int\"}\nNEW={\"id\":\"int\",\"full_name\":\"str\",\"age\":\"str\",\"email\":\"str\"}\ndef diff(old,new):\n    plan=[]\n    for f in new:\n        if f not in old: plan.append((\"add\",f,\"backward-compatible\"))\n    for f in old:\n        if f not in new: plan.append((\"remove?\",f,\"check rename first\"))\n    for f in set(old)&set(new):\n        if old[f]!=new[f]: plan.append((\"retype %s %s->%s\"%(f,old[f],new[f]),f,\"breaking?\"))\n    return plan\nfor step in diff(OLD,NEW): print(step)\nprint(\"plan: 1.expand(add full_name,email) 2.dual-write 3.backfill 4.contract(remove name)\")\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Schema Migration Planner";
  return {id:id,t:title,title:title,description:"The schema migration planner takes the fear out of changing database structure: it diffs old and new schemas, identifies every compatibility risk \u2014 renamed fields, narrowed types, dropped columns \u2014 and produces an ordered, reversible migration plan. Applications keep running through expand/contract phases, and every step has a verification and a rollback. Schema changes become routine engineering ",
    kind:"maintenance tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-schema-migration-planner-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-schema-migration-planner",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();