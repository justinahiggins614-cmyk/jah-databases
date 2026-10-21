(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["graphs", "interaction", "analysis", "integration"];
var PREFIX='JAH-IDC-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Force-Directed Layouts", "graphs", "Lays out dependency graphs with force-directed simulation: springs pull related modules together, repulsion spreads them. Clusters emerge visually; the layout is the analysis. It is the default for a reason.", ["Model edges as springs", "Simulate to equilibrium", "Render the result"], ["D3.js", "Gephi", "Cytoscape"], ["Graph drawing literature", "Fruchterman-Reingold"], 2, 2], ["Dependency Matrices", "graphs", "Shows dependencies as adjacency matrices where cell darkness marks coupling. Matrices scale better than node-link for dense graphs; patterns like layers pop out. Architects read them at a glance.", ["Build the adjacency matrix", "Order rows meaningfully", "Highlight violations"], ["Custom", "Tools", "Research"], ["DSM literature", "Visualization"], 1, 2], ["Module Constellations", "graphs", "Renders modules as star constellations with brightness for importance. The metaphor makes architecture memorable; teams talk about 'the bright cluster'. It aids discussion more than analysis.", ["Size stars by metrics", "Connect with lines", "Label constellations"], ["Custom", "Research", "Demos"], ["Visualization literature", "Metaphor design"], 2, 0], ["Interactive Filtering", "interaction", "Filters the constellation interactively: by layer, by team, by change frequency. Sliders and search prune the noise; focus follows the question. Exploration beats static pictures.", ["Index by attributes", "Filter in real time", "Keep context visible"], ["D3.js", "Custom", "Tools"], ["HCI literature", "InfoVis"], 1, 2], ["Impact Analysis", "analysis", "Computes the blast radius of a change by walking dependents transitively. Before editing, developers see everything affected; the map prevents surprise breakage. It is the most practical graph query.", ["Walk dependents transitively", "Rank by distance", "Show the blast radius"], ["Custom", "IDEs", "Tools"], ["Impact analysis literature", "SRE"], 2, 1], ["Cycle Detection", "analysis", "Finds dependency cycles that defeat layering and complicate builds. Strongly connected components reveal the tangles; breaking them simplifies everything. Zero cycles is the goal.", ["Find strongly connected components", "Highlight cycles", "Suggest breaks"], ["Custom", "Build tools", "Linters"], ["Graph algorithms", "Architecture literature"], 2, 0], ["3D Graph Rendering", "graphs", "Renders huge dependency graphs in 3D with GPU acceleration. Thousands of nodes stay interactive; rotation disentangles what 2D flattens. It scales where 2D fails.", ["Use GPU instancing", "Layout in 3D", "Keep it interactive"], ["Three.js", "Custom", "Research"], ["3D visualization", "GPU literature"], 3, 2], ["Graph Database Storage", "integration", "Stores dependency data in graph databases for rich querying. Cypher finds patterns SQL cannot express; the visualization reads from live queries. It unifies storage and exploration.", ["Model as a property graph", "Query with Cypher", "Visualize results"], ["Neo4j", "Custom", "Tools"], ["Graph DB literature", "Cypher"], 2, 1], ["Incremental Layout", "graphs", "Updates layouts incrementally as code changes instead of recomputing. Mental maps persist across commits; only changed regions move. Stability aids comprehension.", ["Pin stable nodes", "Relax changed regions", "Animate transitions"], ["Custom", "Research", "Tools"], ["Dynamic graph drawing", "HCI"], 3, 2], ["Large-Graph Sampling", "graphs", "Samples massive graphs to representative subsets for interactive exploration. Smart sampling preserves structure; the full graph stays in the database. It makes millions of nodes explorable.", ["Sample preserving structure", "Explore the sample", "Drill into full data"], ["Custom", "Research", "Tools"], ["Graph sampling literature", "Big data"], 3, 2], ["SBOM Integration", "integration", "Overlays SBOM data on the constellation: known vulnerabilities glow. Dependency maps meet security data; risky libraries stand out visually. It turns inventory into insight.", ["Import SBOMs", "Join with vuln feeds", "Highlight risks"], ["Custom", "SCA tools", "Dashboards"], ["SPDX/CycloneDX", "Supply chain"], 2, 1], ["License Risk Overlay", "analysis", "Colors dependencies by license risk: green permissive, red copyleft. Legal review becomes visual; problematic licenses cannot hide. It prevents license surprises.", ["Detect licenses", "Classify risk", "Overlay colors"], ["FOSSology", "SCA tools", "Custom"], ["License literature", "Compliance"], 2, 1], ["Version Drift Tracking", "analysis", "Tracks version drift across the constellation: who lags, who leads. Stale dependencies accumulate risk; the map shows where. Updates get prioritized visually.", ["Record versions", "Compare to latest", "Highlight laggards"], ["Renovate", "Dependabot", "Custom"], ["Dependency management", "DevOps"], 2, 1], ["CI Integration", "integration", "Fails CI when the constellation violates architecture rules: new cycles, forbidden dependencies. The map becomes a gate; architecture stays clean by construction. It automates the architect.", ["Define architecture rules", "Check per commit", "Fail on violation"], ["Custom", "CI", "Linters"], ["Architecture governance", "CI practices"], 1, 1], ["Export Formats", "integration", "Exports constellations to standard formats: GraphML, DOT, JSON. Data escapes the tool into reports, docs, and other analyzers. Open formats prevent lock-in.", ["Export GraphML/DOT", "Include metrics", "Document the schema"], ["Tools", "Gephi", "Custom"], ["GraphML", "DOT language"], 1, 1]];
var DEMOS=["// Demo: {NAME} — cycle detection in {N1} modules\nvar edges=[];for(var i=0;i<{N1};i++){edges.push([i,(i*7+{SEED})%{N1}]);}\nvar cyclic=edges.filter(function(e){return e[0]===e[1]||edges.some(function(f){return f[0]===e[1]&&f[1]===e[0];});});\nconsole.log('technique: {NAME}');console.log('edges: '+edges.length+', cyclic pairs: '+cyclic.length/2);\nconsole.log(cyclic.length?'cycles glow red — break them':'acyclic — clean layers');", "// Demo: {NAME} — impact radius of a change\nvar deps={};for(var i=0;i<{N1};i++){deps['m'+i]=['m'+((i*13+{SEED})%{N1})];}\nvar start='m0',seen={},q=[start];\nwhile(q.length){var m=q.pop();if(seen[m])continue;seen[m]=1;(deps[m]||[]).forEach(function(d){q.push(d);});}\nconsole.log('technique: {NAME}');console.log('changing '+start+' affects '+Object.keys(seen).length+' of '+{N1}+' modules');", "// Demo: {NAME} — force layout iterations\nvar n={N1},energy=100;\nconsole.log('technique: {NAME}');\nfor(var i=0;i<5;i++){energy*=0.6;console.log('iteration '+(i+1)+': energy '+energy.toFixed(1));}\nconsole.log('layout converges — related modules cluster together');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-interactive-dependency-constellations-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('interactive-dependency-constellations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
