(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["rendering", "navigation", "models", "usability"];
var PREFIX='JAH-MLAZ-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Semantic Zoom", "navigation", "Changes what is shown — not just size — as users zoom: boxes become modules become code. Each level has its own representation; transitions are the design. It matches how architects think.", ["Define level representations", "Transition on zoom", "Keep context across levels"], ["Custom", "Research", "Tools"], ["InfoVis literature", "Semantic zoom"], 2, 0], ["Level-of-Detail Rendering", "rendering", "Renders detail proportional to zoom: far means boxes, near means text. LOD keeps massive diagrams interactive; detail appears exactly when readable. It is how maps work, applied to code.", ["Define LOD thresholds", "Swap representations", "Keep it smooth"], ["Custom", "Game engines", "Maps"], ["LOD literature", "Graphics"], 2, 1], ["C4 Model Navigation", "models", "Navigates architecture through C4's four levels: context, containers, components, code. Each level answers different questions; zooming moves between them. It structures architectural thinking.", ["Model the four levels", "Link levels explicitly", "Navigate top-down"], ["Structurizr", "Custom", "Docs"], ["C4 model (Brown)", "Architecture literature"], 1, 2], ["Diagram Tile Pyramids", "rendering", "Serves huge diagrams as tile pyramids like web maps: pre-rendered at each zoom, fetched on demand. Gigapixel architecture diagrams become browsable; only visible tiles load. It scales infinitely.", ["Render tiles per zoom", "Serve on demand", "Prefetch neighbors"], ["Custom", "Map tech", "Tools"], ["Tile map literature", "Slippy maps"], 3, 1], ["Vector Tile Diagrams", "rendering", "Streams diagrams as vector tiles for crisp zoom at any level. Vectors stay sharp; styling adapts per zoom. It is the modern map stack applied to architecture.", ["Encode as vector tiles", "Style per zoom", "Render client-side"], ["Mapbox", "Custom", "Tools"], ["Vector tiles spec", "Map literature"], 3, 1], ["Progressive Disclosure", "navigation", "Reveals complexity progressively: overview first, details on demand. Users are never overwhelmed; curiosity drives the drill-down. It respects cognitive limits.", ["Show the overview", "Reveal on interaction", "Keep breadcrumbs"], ["UI kits", "Custom", "Docs"], ["HCI literature", "InfoVis"], 1, 0], ["Zoom-to-Code", "navigation", "Zooms from architecture diagrams directly into the source file and line. The diagram and code are one navigable space; there is no context switch. It unifies the abstract and concrete.", ["Link diagram nodes to code", "Zoom into the editor", "Keep the path visible"], ["IDEs", "Custom", "Tools"], ["HCI literature", "IDE research"], 2, 2], ["Minimap Overlays", "navigation", "Shows a minimap overview with the viewport rectangle during deep zooms. Users never get lost; the minimap is the compass. Editors and games proved the pattern.", ["Render the overview", "Show the viewport", "Click to jump"], ["Editors", "Games", "Custom"], ["UI patterns", "HCI"], 1, 0], ["GPU-Accelerated Canvas", "rendering", "Renders diagrams on the GPU for smooth zoom of massive graphs. Canvas and WebGL batch thousands of nodes; the CPU stays free. Performance enables exploration.", ["Batch draw calls", "Use the GPU", "Profile frame times"], ["Canvas", "WebGL", "Custom"], ["Graphics literature", "Web perf"], 3, 1], ["Infinite Canvas", "navigation", "Lays architecture on an infinite canvas with pan and zoom as the navigation. No pages, no hierarchy constraints; space is the organizer. Whiteboard tools made it familiar.", ["Support pan and zoom", "Persist positions", "Search the canvas"], ["Excalidraw", "Miro", "Custom"], ["Canvas literature", "HCI"], 2, 0], ["Layer Culling", "rendering", "Culls off-screen and irrelevant layers during zoom for performance. Only visible content renders; the rest waits. It keeps frame rates high at any scale.", ["Cull off-screen", "Prioritize visible", "Stream the rest"], ["Custom", "Game engines", "Maps"], ["Culling literature", "Graphics"], 2, 1], ["Zoom-Level Prefetching", "rendering", "Prefetches adjacent zoom levels so zooming never waits on the network. The current level plus neighbors stay cached; zoom feels instant. It hides latency with prediction.", ["Cache neighbors", "Predict zoom direction", "Evict wisely"], ["Custom", "Maps", "Tools"], ["Prefetch literature", "Caching"], 2, 1], ["Gesture Zoom Handling", "navigation", "Handles pinch and wheel zoom with the right physics: momentum, bounds, snapping. The feel of zoom decides whether the tool delights or frustrates. Native gestures set expectations.", ["Add momentum", "Bound the zoom", "Snap to levels"], ["Touch devices", "Browsers", "Custom"], ["Gesture literature", "HCI"], 1, 0], ["Zoom State Persistence", "navigation", "Persists zoom position and level across sessions via shareable URLs. A link opens exactly the view the sender saw; collaboration needs it. State is part of the document.", ["Encode view in the URL", "Restore on load", "Share links"], ["Web apps", "Custom", "Tools"], ["Web literature", "UX patterns"], 1, 2], ["Zoom Usability Studies", "usability", "Studies whether zoomable architecture actually helps with task-based evaluations. Navigation time, lostness, and insight versus static diagrams; evidence guides design. It keeps the field honest.", ["Design task studies", "Measure navigation", "Compare against static"], ["Research", "Universities", "Labs"], ["HCI evaluation", "Empirical methods"], 3, 2]];
var DEMOS=["// Demo: {NAME} — semantic zoom levels\nvar levels=['system','subsystem','module','file','function','line'];\nvar z=({SEED}%6);\nconsole.log('technique: {NAME}');console.log('zoom level '+z+': '+levels[z]);\nconsole.log(z<2?'show: boxes and flows':z<4?'show: modules and APIs':'show: source code');", "// Demo: {NAME} — tile pyramid math\nvar base=256,levels=6,tiles=0;\nfor(var z=0;z<levels;z++){tiles+=Math.pow(4,z);}\nconsole.log('technique: {NAME}');console.log('pyramid: '+levels+' levels, '+tiles+' tiles total');\nconsole.log('viewport needs ~'+Math.pow(4,2)+' tiles — prefetch neighbors');", "// Demo: {NAME} — C4 navigation\nvar c4=['context','containers','components','code'];\nvar at=({SEED}%4);\nconsole.log('technique: {NAME}');console.log('C4 level: '+c4[at]);\nconsole.log(at<3?'drill down -> '+c4[at+1]:'deepest level — source code');"];
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
var gen={version:'jahdb-multi-layered-architectural-zooming-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('multi-layered-architectural-zooming',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
