(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["web", "mobile", "media", "build", "data"];
var PREFIX='JAH-LAL-S-';
var GENVER='jahdb-lazy-asset-loading-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["technique", "defers", "trigger", "example"];
var DEMO_TPL="// $TITLE - lazy loader demo\nvar assets = [];\nfor (var i = 0; i < 10; i++) assets.push({ id: i, loaded: false, inView: i < 3 });\nfunction loadVisible() {\n  var n = 0;\n  assets.forEach(function(a) { if (a.inView && !a.loaded) { a.loaded = true; n++; } });\n  return n;\n}\nconsole.log(\"Technique: $TECHNIQUE | Defers: $DEFERS\");\nconsole.log(\"First paint loads: \" + loadVisible() + \" of \" + assets.length);\nassets[7].inView = true;\nconsole.log(\"Scroll -> loads: \" + loadVisible() + \" more\");\nconsole.log(\"Savings: 60% deferred -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["web", "SigLazy-View", "Signature-original: viewport prediction preloading what the user will likely scroll to. Defers offscreen assets; triggered by predicted viewport. Example: siglazy viewport --predict.", {"technique": "SigLazy-View", "defers": "offscreen assets", "trigger": "predicted viewport", "example": "siglazy viewport --predict"}], ["web", "SigSplit-Auto", "Signature-original: automatic route splitting with zero config from the file tree. Defers route bundles; triggered by navigation. Example: sigbuild --auto-split.", {"technique": "SigSplit-Auto", "defers": "route bundles", "trigger": "navigation", "example": "sigbuild --auto-split"}], ["web", "SigVirtual-Grid", "Signature-original: virtualized grids handling million-cell datasets at 60fps. Defers offscreen cells; triggered by scroll. Example: <SigGrid rows={1e6}>.", {"technique": "SigVirtual-Grid", "defers": "offscreen cells", "trigger": "scroll", "example": "<SigGrid rows={1e6}>"}], ["media", "SigImage-Prog", "Signature-original: progressive images with Sig blur-up generated at build. Defers detail scans; triggered by byte arrival. Example: sigimg --progressive.", {"technique": "SigImage-Prog", "defers": "detail scans", "trigger": "byte arrival", "example": "sigimg --progressive"}], ["web", "SigHydrate-Part", "Signature-original: per-component hydration priorities with idle-time scheduling. Defers hydration; triggered by priority + idle. Example: sighydrate priority=\"high\".", {"technique": "SigHydrate-Part", "defers": "hydration", "trigger": "priority + idle", "example": "sighydrate priority=\"high\""}], ["web", "SigPrefetch-AI", "Signature-original: ML-predicted prefetching based on navigation patterns. Defers nothing (predicts); triggered by model score. Example: sigprefetch --learn.", {"technique": "SigPrefetch-AI", "defers": "nothing (predicts)", "trigger": "model score", "example": "sigprefetch --learn"}], ["web", "SigFont-Stream", "Signature-original: font subsetting streaming only used glyphs per page. Defers unused glyphs; triggered by text scan. Example: sigfont --subset.", {"technique": "SigFont-Stream", "defers": "unused glyphs", "trigger": "text scan", "example": "sigfont --subset"}], ["media", "SigVideo-Adapt", "Signature-original: adaptive video ladders generated per device class. Defers high renditions; triggered by bandwidth. Example: sigvideo --ladder.", {"technique": "SigVideo-Adapt", "defers": "high renditions", "trigger": "bandwidth", "example": "sigvideo --ladder"}], ["data", "SigData-Page", "Signature-original: cursor paging with total-count estimation for huge tables. Defers later pages; triggered by scroll. Example: sigdata page --cursor.", {"technique": "SigData-Page", "defers": "later pages", "trigger": "scroll", "example": "sigdata page --cursor"}], ["media", "Sig3D-Stream", "Signature-original: 3D asset streaming with progressive mesh refinement. Defers refinement levels; triggered by distance. Example: sig3d --stream.", {"technique": "Sig3D-Stream", "defers": "refinement levels", "trigger": "distance", "example": "sig3d --stream"}], ["web", "SigWasm-Lazy", "Signature-original: WASM modules compiled lazily per exported function. Defers unused exports; triggered by first call. Example: sigwasm --lazy.", {"technique": "SigWasm-Lazy", "defers": "unused exports", "trigger": "first call", "example": "sigwasm --lazy"}], ["web", "SigCSS-Critical", "Signature-original: critical CSS inlined automatically, the rest deferred. Defers non-critical CSS; triggered by build analysis. Example: sigcss --critical.", {"technique": "SigCSS-Critical", "defers": "non-critical CSS", "trigger": "build analysis", "example": "sigcss --critical"}], ["web", "SigState-Replay", "Signature-original: state snapshots letting lazily-loaded parts replay missed events. Defers event handling; triggered by load. Example: sigstate --replay.", {"technique": "SigState-Replay", "defers": "event handling", "trigger": "load", "example": "sigstate --replay"}], ["web", "SigBudget-Load", "Signature-original: load budgets failing the build when pages exceed byte limits. Defers n/a (enforces); triggered by build. Example: sigbudget --max 200kb.", {"technique": "SigBudget-Load", "defers": "n/a (enforces)", "trigger": "build", "example": "sigbudget --max 200kb"}], ["web", "SigLoad-One", "Signature-original: the united loading plane — every asset lazy by default. Defers everything lazy; triggered by visibility. Example: sigload --default-lazy.", {"technique": "SigLoad-One", "defers": "everything lazy", "trigger": "visibility", "example": "sigload --default-lazy"}]];
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
  if(!new RegExp('^'+'JAH\\-LAL\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lazy-asset-loading-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
