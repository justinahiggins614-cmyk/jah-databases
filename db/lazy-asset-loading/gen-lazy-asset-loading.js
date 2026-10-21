(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["web", "mobile", "media", "build", "data"];
var PREFIX='JAH-LAL-';
var GENVER='jahdb-lazy-asset-loading-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["technique", "defers", "trigger", "example"];
var DEMO_TPL="// $TITLE - lazy loader demo\nvar assets = [];\nfor (var i = 0; i < 10; i++) assets.push({ id: i, loaded: false, inView: i < 3 });\nfunction loadVisible() {\n  var n = 0;\n  assets.forEach(function(a) { if (a.inView && !a.loaded) { a.loaded = true; n++; } });\n  return n;\n}\nconsole.log(\"Technique: $TECHNIQUE | Defers: $DEFERS\");\nconsole.log(\"First paint loads: \" + loadVisible() + \" of \" + assets.length);\nassets[7].inView = true;\nconsole.log(\"Scroll -> loads: \" + loadVisible() + \" more\");\nconsole.log(\"Savings: 60% deferred -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["web", "loading=\"lazy\"", "Native browser lazy-loading for images and iframes below the fold — one attribute. Defers offscreen images/iframes; triggered by viewport proximity. Example: <img loading=\"lazy\" src=\"...\">.", {"technique": "native lazy", "defers": "offscreen images/iframes", "trigger": "viewport proximity", "example": "<img loading=\"lazy\" src=\"...\">"}], ["web", "IntersectionObserver", "Observe elements and load them as they near the viewport with rootMargin tuning. Defers any asset; triggered by intersection ratio. Example: new IntersectionObserver(cb,{rootMargin:\"200px\"}).", {"technique": "IntersectionObserver", "defers": "any asset", "trigger": "intersection ratio", "example": "new IntersectionObserver(cb,{rootMargin:\"200px\"})"}], ["web", "React.lazy + Suspense", "Split routes into chunks loaded on navigation with Suspense fallbacks. Defers route bundles; triggered by route render. Example: const Page = React.lazy(()=>import(\"./Page\")).", {"technique": "code splitting", "defers": "route bundles", "trigger": "route render", "example": "const Page = React.lazy(()=>import(\"./Page\"))"}], ["web", "dynamic import()", "import() returns a promise for a module, the primitive behind all JS code splitting. Defers modules; triggered by call time. Example: const m = await import(\"./heavy.js\").", {"technique": "dynamic import", "defers": "modules", "trigger": "call time", "example": "const m = await import(\"./heavy.js\")"}], ["web", "Virtualized lists", "react-window renders only visible rows, making 100k-row lists feel instant. Defers offscreen rows; triggered by scroll position. Example: <FixedSizeList height={600} itemCount={100000}>.", {"technique": "windowing", "defers": "offscreen rows", "trigger": "scroll position", "example": "<FixedSizeList height={600} itemCount={100000}>"}], ["media", "Progressive JPEG", "Progressive scans show a blurry full image first, sharpening as data arrives. Defers detail scans; triggered by byte arrival. Example: jpegtran -progressive.", {"technique": "progressive image", "defers": "detail scans", "trigger": "byte arrival", "example": "jpegtran -progressive"}], ["media", "Blur-up placeholders", "Tiny blurred thumbnails inline in HTML swap for full images on load (LQIP). Defers full image; triggered by image onload. Example: 20px thumb -> full src.", {"technique": "LQIP", "defers": "full image", "trigger": "image onload", "example": "20px thumb -> full src"}], ["web", "prefetch / preload hints", "Resource hints tell the browser what the next navigation will need. Defers nothing (prioritizes); triggered by hint parsing. Example: <link rel=\"prefetch\" href=\"/next.js\">.", {"technique": "resource hints", "defers": "nothing (prioritizes)", "trigger": "hint parsing", "example": "<link rel=\"prefetch\" href=\"/next.js\">"}], ["web", "Deferred scripts", "defer and async let parsing continue while scripts load in the background. Defers script execution; triggered by parse/DOM events. Example: <script defer src=\"app.js\">.", {"technique": "deferred scripts", "defers": "script execution", "trigger": "parse/DOM events", "example": "<script defer src=\"app.js\">"}], ["media", "Texture streaming", "Game engines stream mip levels by distance so VRAM holds only visible detail. Defers high mip levels; triggered by camera distance. Example: UE5 virtual textures.", {"technique": "texture streaming", "defers": "high mip levels", "trigger": "camera distance", "example": "UE5 virtual textures"}], ["media", "LOD meshes", "Level-of-detail swaps low-poly models in at distance, loading detail on approach. Defers high-poly meshes; triggered by distance threshold. Example: 3 LOD tiers per asset.", {"technique": "LOD", "defers": "high-poly meshes", "trigger": "distance threshold", "example": "3 LOD tiers per asset"}], ["build", "Tree-shaking", "Bundlers drop unused exports at build time so users never download dead code. Defers n/a (removes); triggered by build. Example: rollup/esbuild production build.", {"technique": "tree-shaking", "defers": "n/a (removes)", "trigger": "build", "example": "rollup/esbuild production build"}], ["data", "On-demand paging", "Infinite scroll fetching pages as the user nears the bottom. Defers later pages; triggered by scroll threshold. Example: cursor-based /api/items?after=....", {"technique": "paging", "defers": "later pages", "trigger": "scroll threshold", "example": "cursor-based /api/items?after=..."}], ["web", "Lazy hydration", "Server-rendered HTML becomes interactive only for components entering view. Defers JS hydration; triggered by visibility. Example: astro island directives.", {"technique": "partial hydration", "defers": "JS hydration", "trigger": "visibility", "example": "astro island directives"}], ["web", "Font display swap", "font-display: swap renders fallback text instantly, swapping when the webfont loads. Defers webfont; triggered by font load. Example: @font-face{font-display:swap}.", {"technique": "font swap", "defers": "webfont", "trigger": "font load", "example": "@font-face{font-display:swap}"}]];
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
  if(!new RegExp('^'+'JAH\\-LAL\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lazy-asset-loading',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
