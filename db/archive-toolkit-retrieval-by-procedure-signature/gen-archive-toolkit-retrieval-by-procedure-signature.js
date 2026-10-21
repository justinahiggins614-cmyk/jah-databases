(function(){'use strict';
var PREFIX="JAH-ATK211S-";
var METHODS=[["Capability indexing", "Index procedures by (verb, input types, output types) triples so 'convert X to Y' queries match structurally."], ["Precondition checking", "Verify the caller's context satisfies each procedure's preconditions before ranking it as applicable."], ["Effect modeling", "Record each procedure's effects so planners can chain procedures whose effects satisfy the next one's preconditions."], ["Procedure ranking", "Rank candidate procedures by success rate, cost, and fit to the caller's tools and skill level."], ["Step extraction", "Pull numbered steps out of prose instructions into an executable checklist with per-step verification."], ["Tool requirement mapping", "List every tool, permission, and credential a procedure needs so callers know the true cost of following it."], ["Variant selection", "When several procedures achieve the goal, present variants (fast, safe, cheap) instead of picking silently."], ["Safety annotation", "Tag procedures with risk levels and required safeguards, refusing to recommend high-risk variants casually."], ["Procedure composition", "Chain atomic procedures into end-to-end workflows, checking that outputs plug into the next inputs."], ["Versioned procedures", "Keep every procedure versioned so a workflow that worked last year can be replayed exactly."], ["Failure-mode documentation", "Attach known failure modes and recoveries to each procedure so callers are not surprised mid-run."], ["Interactive procedure guidance", "Turn a retrieved procedure into a guided session that tracks which step the caller is on."], ["Procedure provenance", "Record who authored and who validated each procedure, with test evidence where it exists."], ["Domain scoping", "Scope procedure search to the caller's domain so a chemistry protocol never answers a software question."], ["Outcome verification hooks", "Pair each procedure with a check the caller can run to confirm the operation actually succeeded."]];
var CATS=["procedures", "capabilities", "workflows"];
var DEMO="# Retrieval-by-Procedure demo: capability-triple matching with preconditions.\nPROCS=[{\"name\":\"migrate-sqlite-postgres\",\"verbs\":[\"migrate\",\"convert\"],\"inputs\":[\"sqlite\"],\"outputs\":[\"postgres\"],\"pre\":[\"disk>1GB\"],\"risk\":\"medium\"},\n       {\"name\":\"backup-sqlite\",\"verbs\":[\"backup\",\"copy\"],\"inputs\":[\"sqlite\"],\"outputs\":[\"backup\"],\"pre\":[],\"risk\":\"low\"},\n       {\"name\":\"tune-postgres\",\"verbs\":[\"tune\",\"optimize\"],\"inputs\":[\"postgres\"],\"outputs\":[\"postgres\"],\"pre\":[\"dba\"],\"risk\":\"low\"}]\nCTX={\"disk>1GB\":True,\"dba\":False}\ndef find(verb,have,want):\n    out=[]\n    for p in PROCS:\n        if verb in p[\"verbs\"] and have in p[\"inputs\"] and want in p[\"outputs\"]:\n            ok=all(CTX.get(c,False) for c in p[\"pre\"])\n            out.append((p[\"name\"],ok,p[\"risk\"],[c for c in p[\"pre\"] if not CTX.get(c,False)]))\n    return out\nprint(find(\"migrate\",\"sqlite\",\"postgres\"))\nprint(find(\"tune\",\"postgres\",\"postgres\"))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Retrieval-by-Procedure (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. Retrieval-by-procedure searches for know-how rather than facts: given a goal phrased as an operation ('calibrate this sensor', 'migrate this schema'), it returns instructions, workflows, scripts, and programs known to complete it. The index is over capabilities \u2014 verbs, inputs, outputs, preconditions \u2014 not just keywords. Matching blends semantic understanding of the requested operation with hard c",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
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
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-retrieval-by-procedure-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-retrieval-by-procedure-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();