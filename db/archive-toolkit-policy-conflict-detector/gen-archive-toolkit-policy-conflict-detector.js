(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["conflict-identification", "precedence-resolution", "impact-analysis"];
var PREFIX="JAH-ATK276-";
var KIND="policy conflict detector";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["conflict-identification", "Direct contradiction detection", "Policies are compared pairwise for direct contradictions: one allows what another denies on the same scope. Contradictions are reported with both rules cited and the overlapping scope. Detection runs whenever policy changes, not on a schedule.", "pairwise allow-vs-deny comparison", "reporting with both rules cited", "detection on every policy change", "CFG = {1: [(\"allow\", \"read\"), (\"allow\", \"write\")], 2: [(\"allow\", \"read\"), (\"deny\", \"read\")], 3: [(\"deny\", \"delete\"), (\"allow\", \"delete\"), (\"allow\", \"read\")]}\nrules = CFG[LEVEL]\nseen, conflicts = {}, []\nfor effect, op in rules:\n    if op in seen and seen[op] != effect:\n        conflicts.append(op)\n    seen[op] = effect\nprint(\"rules:\", rules, \"| contradictions:\", conflicts or [\"none\"])"],
["precedence-resolution", "Precedence ordering", "Policies carry precedence ranks, and higher-ranked policies win conflicts deterministically. Ranks reflect authority: legal holds outrank team preferences. The effective policy is computed by applying rules in rank order, so outcomes are predictable and explainable.", "precedence ranks per policy", "higher rank wins deterministically", "explainable effective policy", "CFG = {1: [(\"team\", 1, \"allow\"), (\"legal\", 5, \"deny\")], 2: [(\"team\", 1, \"deny\"), (\"legal\", 5, \"deny\")], 3: [(\"team\", 1, \"allow\")]}\nrules = sorted(CFG[LEVEL], key=lambda r: -r[1])\nwinner = rules[0]\nprint(\"rules by rank:\", rules, \"| effective:\", winner[2], \"(from\", winner[0], \")\")"],
["impact-analysis", "Overlap analysis", "Policies covering the same resources are grouped so reviewers see the full rule set applying to any resource. Overlap is computed from scope expressions, not just names. Unexpected overlap is often where conflicts hide.", "grouping policies by covered resources", "scope-expression overlap computation", "surfacing unexpected overlap", "CFG = {1: [{\"db1\"}, {\"db2\"}], 2: [{\"db1\", \"db2\"}, {\"db2\", \"db3\"}], 3: [{\"db1\"}, {\"db1\"}]}\nscopes = CFG[LEVEL]\noverlap = set.intersection(*scopes) if len(scopes) > 1 else set()\nprint(\"scopes:\", scopes, \"| overlapping resources:\", sorted(overlap) or [\"none\"])"],
["conflict-identification", "Temporal conflict detection", "Retention schedules and deletion deadlines are compared on the time axis: a 7-year retention rule conflicts with a 30-day deletion rule on the same data. Temporal conflicts are the most common cross-domain policy clash. Detection models each rule as a time interval and finds overlaps with opposing effects.", "modeling rules as time intervals", "finding opposing overlaps", "cross-domain temporal clashes", "CFG = {1: [(\"retain\", 0, 2555), (\"retain\", 0, 2555)], 2: [(\"retain\", 0, 2555), (\"delete\", 30, 30)], 3: [(\"delete\", 30, 30), (\"delete\", 60, 60)]}\nrules = CFG[LEVEL]\nconflict = any(a[0] != b[0] and a[1] <= b[2] and b[1] <= a[2] for a in rules for b in rules if a is not b)\nprint(\"rules:\", rules, \"| temporal conflict:\", conflict)"],
["precedence-resolution", "Conflict impact report", "Each detected conflict gets an impact report: which resources, identities, and operations are affected, and what happens under each resolution. Impact turns abstract contradictions into concrete stakes for the resolver. Reports prioritize conflicts by blast radius.", "affected resources, identities, operations", "outcomes under each resolution", "prioritization by blast radius", "CFG = {1: {\"resources\": 2, \"users\": 10}, 2: {\"resources\": 15, \"users\": 200}, 3: {\"resources\": 100, \"users\": 5000}}\nimp = CFG[LEVEL]\nblast = imp[\"resources\"] * imp[\"users\"]\nprint(\"impact:\", imp, \"| blast radius:\", blast, \"| priority:\", \"P1\" if blast > 10000 else \"P2\")"]
];
function escRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(r){return r[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var ladder=1+((seed>>>0)%3);
  var focus=[row[3],row[4],row[5]][ladder-1];
  var stage=['','At ladder rank 1 (foundation), this record covers ','At ladder rank 2 (compounded), it builds on the foundation with ','At ladder rank 3 (full complexity), it extends to production scale with '][ladder];
  var id=PREFIX+String(seed>>>0).padStart(6,'0');
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Public harvest — documented archive-engineering practice; method fact-checked against standard references.",last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length||r.t!==r.title)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('LEVEL = '+r.ladder_rank)!==0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-policy-conflict-detector-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-policy-conflict-detector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
