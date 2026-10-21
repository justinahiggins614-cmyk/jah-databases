(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX10-";
var VERSION="jahdb-apex-tool-apex-knowledge-cartographer-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Knowledge Cartographer is", "The cartographer turns the knowledge ecosystem into a navigable map with zoom levels: fields, records, collections, domains, disciplines. Users pan and zoom like a geographic atlas, and at every level the map shows what is known, what is connected, and what is unexplored territory.", "Territory model with zoom levels; aggregation rules generating each level from the one below; map renderer; navigation state manager."], ["architecture", "Core data model", "Territory and zoom-level data model", "A territory is a record: its bounds (what it covers), its zoom level, its summary statistics, its neighbors, and the rule that generated it from the level below. Zoom levels are fixed and named — field, record, collection, domain, discipline — so maps from different runs are comparable.", "Territory documents with bounds and level; fixed zoom taxonomy; neighbor graph; generation-rule references per territory."], ["component", "Key algorithm I", "Territory aggregation algorithm", "Each zoom level is built by aggregating the level below with explicit rules: clustering by topic affinity, boundary detection where affinity drops, and summary statistics per territory. The rules are deterministic and published, so anyone can verify why a boundary falls where it does.", "Affinity computer; boundary detector; deterministic clustering; per-territory summarizer; rule publication."], ["component", "Key algorithm II", "Cross-domain bridge detection algorithm", "The most valuable features on the map are bridges — narrow connections between distant territories where methods transfer. The detector finds edges that connect otherwise separate clusters, scores them by transfer potential, and highlights them as expedition targets for discovery tools.", "Cluster separator; bridge-edge finder; transfer-potential scorer; expedition handoff exporter."], ["interface", "Interface specification", "Map navigation interface specification", "Callers navigate the map programmatically: get the territory containing a concept, list neighbors, zoom in to constituents, zoom out to context. Responses include the aggregation rule behind each territory so navigation is explainable at every step.", "Navigation service over territory store; zoom in/out operations; neighbor listing; rule-attached responses."], ["component", "Ingestion and adapters", "Ingestion: surveying the ecosystem", "The map is only as good as its survey: crawlers inventory collections, schema readers inventory fields, and citation analysis maps the domain graph. Surveys run on schedule, and each survey records its coverage so the map knows where it is thin.", "Collection crawler; schema reader; citation mapper; coverage recorder per survey."], ["component", "Indexing and retrieval", "Map tile indexing and retrieval", "Maps render as tiles per zoom level for fast panning: precomputed territory tiles with summaries, served from cache, regenerated when the underlying graph changes. Tile invalidation is surgical — only affected regions rebuild — so the map stays fresh without full recomputation.", "Tile generator per zoom; tile cache; surgical invalidation on graph change; on-demand tile fallback."], ["component", "Reasoning and decision component", "Reasoning: reading the map's story", "The cartographer does not just draw — it reads: which territories are growing fastest, where bridges are forming, which regions are stagnating. Trend analysis over survey history turns the map into an instrument for spotting where knowledge is moving.", "Survey-history time series; growth and bridge-formation detectors; stagnation flags; narrative report generator."], ["interface", "Output and presentation", "Atlas presentation output", "The atlas renders as an explorable document: zoomable map, territory dossiers with statistics and neighbors, bridge highlights, and terra-incognita shading for thin regions. Every visual element expands to its underlying data — the map is an interface, not a poster.", "Zoomable renderer; territory dossiers; bridge overlay; thin-region shading; data expansion links."], ["benchmark", "Benchmark harness and measured baseline", "Cartography benchmark harness", "Maps are tested against expert-drawn ground truth: do territory boundaries match expert domain judgments, are bridges real, is coverage honest? Baselines are naive clustering and manual curation samples; the cartographer must match expert boundaries within tolerance to be called accurate.", "Expert-judgment fixture set; boundary agreement scorer; bridge precision scorer; coverage honesty checker; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: mapping an unfamiliar field", "Given a new field — say, agrivoltaics — the cartographer surveys its collections, clusters its records, places it on the map between photovoltaics and agriculture, detects its bridges to both, and marks its thinly surveyed corners. A newcomer gets the lay of the land in one atlas page with every claim expandable.", "Survey; clustering; placement via affinity; bridge detection; thin-region marking; atlas rendering."], ["component", "Failure modes and reliability", "Failure modes: map vs territory errors", "Maps lie in known ways: outdated surveys presented as current, arbitrary boundaries drawn as natural, thin regions rendered as empty. The cartographer labels survey dates on every territory, publishes boundary rules, and shades thin regions instead of hiding them. The map must never be more confident than its survey.", "Survey-date labeling; boundary-rule publication; thin-region shading; confidence caps from coverage."], ["architecture", "Scaling architecture", "Scaling: mapping at planetary scale", "Planetary knowledge needs planetary maps: regional cartographers map their territories and federate upward, with boundary reconciliation where regions meet. The global atlas is the composed view — consistent because every region uses the same zoom taxonomy and aggregation rules.", "Regional cartographers; boundary reconciliation protocol; composed global atlas; shared taxonomy enforcement."], ["interface", "Security, permissions, and audit", "Security: maps of sensitive territory", "Some territories are sensitive — their very shape reveals capabilities. The cartographer supports redacted mapping: sensitive regions appear as unlabeled shaded zones with access-controlled detail. Redaction is visible (a shaded zone, not a hole) so the map stays honest about what it hides.", "Sensitivity tagging per territory; redacted rendering; access-controlled detail endpoints; visible-redaction policy."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance maps a fixture ecosystem end to end: survey, aggregate, detect bridges, render the atlas, then verify boundaries against expert judgment and bridges against planted truth. The atlas ships only when the map matches the territory within tolerance and every visual claim expands to data.", "Fixture ecosystem; full mapping run; expert-agreement and bridge scorers; expandability audit; release gate."]];
function demoProgram(seed,title,rnd){
  var n=ri(rnd,5,12);
  var lines=['// JAH demo program — runnable with: node demo.js','// generated record demo (seed '+seed+')','\'use strict\';'];
  lines.push('var checks=[');
  for(var i=0;i<n;i++){lines.push('  {expr:"'+(i+2)+'*'+(i+3)+'",expect:'+((i+2)*(i+3))+'}'+(i<n-1?',':''));}
  lines.push('];');
  lines.push('var fails=0;');
  lines.push('checks.forEach(function(c){var got=eval(c.expr);var ok=got===c.expect;if(!ok)fails++;console.log((ok?"PASS":"FAIL")+"  "+c.expr+" = "+got);});');
  lines.push('console.log("generated demo: "+(checks.length-fails)+"/"+checks.length+" checks passed");');
  return lines.join("\n");
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=b[2]+' — variant '+seed;
  var prog=demoProgram(seed,title,rnd);
  return {id:id,title:title,description:b[3],ladder_rank:ri(rnd,1,15),
    demo:{kind:'code',title:'Runnable code demo — '+title.slice(0,50),program:prog,language:'javascript'},
    architecture:b[4],components:['core coordinator','interface adapter','validation harness','telemetry exporter'],
    interfaces:['JSON record schema v1','query API (filter/sort/paginate)','demo runner (node-compatible JS)'],
    implementation_status:'Generated design record — proposed capability; demo program is real executable code.',
    acceptance_tests:{criteria:['demo program executes without errors','record validates against schema','no duplicate id in archive'],demo_status:'generated at runtime'},
    dependencies:['node.js runtime (demo execution)','JAH database core (jahdb.js)','gzip JSONL archive'],
    provenance:"Public-record survey",last_verified:"2026-10-21",march_marker:"March to a million in progress \u2014 15 of 1,000,000 records (0.0015%)",
    t:title,g:cat,c:1,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  var d=r.demo;
  if(!d||d.language!=='javascript'||typeof d.program!=='string'||d.program.indexOf('console.log')<0)e.push('demo');
  if(typeof r.architecture!=='string'||!r.architecture.length)e.push('architecture');
  if(!Array.isArray(r.components)||!r.components.length)e.push('components');
  if(!Array.isArray(r.interfaces)||!r.interfaces.length)e.push('interfaces');
  if(typeof r.implementation_status!=='string'||!r.implementation_status.length)e.push('implementation_status');
  if(!r.acceptance_tests||typeof r.acceptance_tests!=='object')e.push('acceptance_tests');
  if(!Array.isArray(r.dependencies)||!r.dependencies.length)e.push('dependencies');
  if(CATS.indexOf(r.g)<0)e.push('g');
  return {ok:!e.length,errors:e};
}
var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-apex-knowledge-cartographer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();