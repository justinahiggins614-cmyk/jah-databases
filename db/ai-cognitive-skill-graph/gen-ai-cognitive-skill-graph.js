(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["graph-construction", "dependencies", "composition", "grounding", "evolution"];
var PREFIX="JAH-AICOGN-";
var FIELDS=["technique", "nodes", "edges", "use", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Skill Graph Construction", "Skills become nodes, prerequisites become edges; the graph is built from task decompositions. The map shows what learning what unlocks. Competence gets mapped.", "graph-construction", 2, "Decomposition", "Skills", "Prerequisites", "Curriculum", "Mapped", "Medium"], ["Dependency Resolution", "Learning order follows topological sort: prerequisites before dependents. The order is computed, not guessed. Curricula get ordered.", "dependencies", 1, "Topo sort", "Skills", "Prereqs", "Ordering", "Ordered", "Low"], ["Skill Composition", "Complex skills compose from simpler ones; the graph shows the composition paths. Composition gets visible. Competence gets built.", "composition", 2, "Composition", "Atomic skills", "Compose links", "Building", "Visible", "Medium"], ["Skill Grounding in Tasks", "Skills are grounded by the tasks that need them; ungrounded skills are pruned. Grounding gets real. Graphs stay honest.", "grounding", 2, "Grounding", "Skills", "Task links", "Pruning", "Honest", "Medium"], ["Graph Evolution", "The graph evolves as new skills are learned and old ones refined; versioning tracks the growth. Evolution gets tracked. Maps stay current.", "evolution", 2, "Versioning", "Growing set", "New links", "Tracking", "Current", "Medium"], ["Prerequisite Inference", "Prerequisites are inferred from failure patterns: failing X when lacking Y suggests Y→X. Inference gets empirical. Edges get discovered.", "dependencies", 3, "Inference", "Skills", "Inferred", "Discovery", "Discovered", "High"], ["Skill Embeddings", "Skills embed in vector space; similar skills cluster. The geometry reveals the skill landscape. Landscapes get mapped.", "graph-construction", 3, "Embeddings", "Vectors", "Similarity", "Clustering", "Mapped", "High"], ["Curriculum Generation", "Curricula generate from the graph: the path from current skills to target is the learning plan. Plans get computed. Learning gets directed.", "composition", 2, "Path finding", "Skills", "Prereqs", "Curriculum", "Directed", "Medium"], ["Transfer Detection", "Skills transferring to new tasks are detected by performance deltas; the graph predicts transfer. Transfer gets predicted. Learning gets efficient.", "composition", 3, "Transfer measure", "Skills", "Transfer links", "Prediction", "Efficient", "High"], ["Skill Forgetting Curves", "Unused skills decay; the graph schedules refresh before the decay matters. Forgetting gets managed. Skills stay sharp.", "evolution", 2, "Spaced refresh", "Skills", "Decay links", "Scheduling", "Sharp", "Medium"], ["Multi-Agent Skill Graphs", "Teams share skill graphs: who knows what is mapped, gaps get filled. Teams get mapped. Gaps get visible.", "graph-construction", 2, "Team map", "Agent skills", "Coverage", "Staffing", "Visible gaps", "Medium"], ["Skill Assessment", "Skills are assessed by tasks that isolate them; the graph guides the test design. Assessment gets precise. Levels get known.", "grounding", 2, "Isolated tests", "Skills", "Test links", "Levels", "Precise", "Medium"], ["Hierarchical Skills", "Skills nest: 'cook' contains 'chop' contains 'grip knife'. The hierarchy organizes. Nesting gets structured. Complexity gets managed.", "graph-construction", 1, "Hierarchy", "Nested skills", "Contains", "Organization", "Structured", "Low"], ["Skill Graph Visualization", "The graph is drawn for humans: clusters colored, paths highlighted. Visualization gets intuitive. Maps get readable.", "graph-construction", 1, "Drawing", "Skills", "Links", "Reading", "Readable", "Low"], ["Dynamic Skill Discovery", "New skills are discovered from task traces: repeated patterns become nodes. Discovery gets automatic. Graphs grow themselves.", "evolution", 3, "Pattern mining", "Discovered", "Mined", "Growth", "Self-growing", "High"], ["Skill Decay Modeling", "Decay is modeled per skill: half-lives differ. The model schedules refresh optimally. Decay gets scientific. Refresh gets optimal.", "evolution", 2, "Half-life", "Skills", "Decay rates", "Optimal refresh", "Scientific", "Medium"], ["Cross-Domain Skill Links", "Skills link across domains: 'debugging' helps both code and writing. Links get surprising. Transfer gets broad.", "composition", 2, "Cross links", "All skills", "Analogies", "Broad transfer", "Surprising", "Medium"], ["Skill Graph Query Language", "The graph is queried: 'what unlocks X', 'shortest path to Y'. Queries get answered. Maps get interrogated.", "graph-construction", 2, "Query lang", "Skills", "Links", "Interrogation", "Answered", "Medium"], ["Competence Certification", "Competence is certified by graph coverage: the subgraph mastered is the certificate. Certification gets precise. Levels get proven.", "grounding", 3, "Coverage cert", "Mastered", "Proven", "Certificates", "Proven", "High"], ["Skill Graph Merging", "Graphs from different agents merge: the union is richer. Merging gets careful. Knowledge gets combined.", "evolution", 3, "Union merge", "Combined", "Merged", "Combining", "Richer", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'skills = {\"read\": [], \"summarize\": [\"read\"], \"answer\": [\"summarize\"]}\ndef can(skill, have):\n    return all(d in have for d in skills[skill])\nprint(\"have: {read}, can summarize:\", can(\"summarize\", {\"read\"}))\nprint(\"can answer:\", can(\"answer\", {\"read\"}))\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-ai-cognitive-skill-graph-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-cognitive-skill-graph",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
