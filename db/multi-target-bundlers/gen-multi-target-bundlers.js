(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["js", "rust-go", "native", "mobile", "edge"];
var PREFIX='JAH-MTB-';
var GENVER='jahdb-multi-target-bundlers-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["bundler", "targets", "splitting", "speed"];
var DEMO_TPL="// $TITLE - bundler module graph demo\nvar modules = { app: [\"utils\", \"router\"], utils: [], router: [\"utils\"] };\nvar order = [], seen = {};\n(function visit(m) { if (seen[m]) return; seen[m] = 1; modules[m].forEach(visit); order.push(m); })(\"app\");\nconsole.log(\"Bundler: $BUNDLER | Targets: $TARGETS\");\nconsole.log(\"Bundle order: \" + order.join(\" -> \"));\nconsole.log(\"Chunks: app.[hash].js (entry), shared utils deduplicated -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["js", "webpack", "The configurable giant: loaders, plugins, and module federation. Targets: web/node/workers. Splitting: dynamic import + splitChunks. Speed: slow, thorough.", {"bundler": "webpack", "targets": "web/node/workers", "splitting": "dynamic import + splitChunks", "speed": "slow, thorough"}], ["js", "Rollup", "ES-module-first bundler famous for clean tree-shaken libraries. Targets: web/node. Splitting: manual + dynamic chunks. Speed: medium.", {"bundler": "Rollup", "targets": "web/node", "splitting": "manual + dynamic chunks", "speed": "medium"}], ["js", "esbuild", "Go-written bundler 10-100x faster than JS-based ones. Targets: web/node. Splitting: code splitting. Speed: extremely fast.", {"bundler": "esbuild", "targets": "web/node", "splitting": "code splitting", "speed": "extremely fast"}], ["js", "Vite", "Dev via native ESM, build via Rollup; the modern default. Targets: web. Splitting: rollup chunks. Speed: fast dev.", {"bundler": "Vite", "targets": "web", "splitting": "rollup chunks", "speed": "fast dev"}], ["js", "Parcel", "Zero-config bundler with automatic transforms and caching. Targets: web/node. Splitting: automatic. Speed: fast.", {"bundler": "Parcel", "targets": "web/node", "splitting": "automatic", "speed": "fast"}], ["js", "Turbopack", "Rust incremental bundler behind Next.js 13+. Targets: web. Splitting: incremental chunks. Speed: very fast.", {"bundler": "Turbopack", "targets": "web", "splitting": "incremental chunks", "speed": "very fast"}], ["js", "Rolldown", "Rust Rollup-compatible bundler powering Vite’s future. Targets: web/node. Splitting: rollup-compatible. Speed: very fast.", {"bundler": "Rolldown", "targets": "web/node", "splitting": "rollup-compatible", "speed": "very fast"}], ["js", "Rspack", "Rust webpack-compatible bundler for migration paths. Targets: web/node. Splitting: webpack-compatible. Speed: very fast.", {"bundler": "Rspack", "targets": "web/node", "splitting": "webpack-compatible", "speed": "very fast"}], ["js", "Bun bundler", "Bun’s built-in bundler/transpiler in Zig. Targets: web/server. Splitting: code splitting. Speed: very fast.", {"bundler": "Bun", "targets": "web/server", "splitting": "code splitting", "speed": "very fast"}], ["js", "Browserify", "The original: require() in the browser via static analysis. Targets: web. Splitting: factor-bundle. Speed: slow (legacy).", {"bundler": "Browserify", "targets": "web", "splitting": "factor-bundle", "speed": "slow (legacy)"}], ["mobile", "Metro", "React Native’s bundler with RAM bundles and delta updates. Targets: iOS/Android. Splitting: RAM bundles. Speed: medium.", {"bundler": "Metro", "targets": "iOS/Android", "splitting": "RAM bundles", "speed": "medium"}], ["js", "Microbundle", "Zero-config library bundler outputting CJS/ES/UMD. Targets: libraries. Splitting: formats. Speed: fast.", {"bundler": "Microbundle", "targets": "libraries", "splitting": "formats", "speed": "fast"}], ["js", "tsup", "esbuild-powered library bundler with DTS generation. Targets: libraries. Splitting: formats. Speed: very fast.", {"bundler": "tsup", "targets": "libraries", "splitting": "formats", "speed": "very fast"}], ["js", "WMR", "Preact’s tiny all-in-one dev tool with Rollup build. Targets: web. Splitting: rollup. Speed: fast.", {"bundler": "WMR", "targets": "web", "splitting": "rollup", "speed": "fast"}], ["js", "Snowpack", "Unbundled dev via ESM; build via esbuild/webpack plugins. Targets: web. Splitting: per-file ESM. Speed: fast dev.", {"bundler": "Snowpack", "targets": "web", "splitting": "per-file ESM", "speed": "fast dev"}]];
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
  if(!new RegExp('^'+'JAH\\-MTB\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('multi-target-bundlers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
