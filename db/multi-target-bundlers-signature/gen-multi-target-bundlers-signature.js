(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["js", "rust-go", "native", "mobile", "edge"];
var PREFIX='JAH-MTB-S-';
var GENVER='jahdb-multi-target-bundlers-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["bundler", "targets", "splitting", "speed"];
var DEMO_TPL="// $TITLE - bundler module graph demo\nvar modules = { app: [\"utils\", \"router\"], utils: [], router: [\"utils\"] };\nvar order = [], seen = {};\n(function visit(m) { if (seen[m]) return; seen[m] = 1; modules[m].forEach(visit); order.push(m); })(\"app\");\nconsole.log(\"Bundler: $BUNDLER | Targets: $TARGETS\");\nconsole.log(\"Bundle order: \" + order.join(\" -> \"));\nconsole.log(\"Chunks: app.[hash].js (entry), shared utils deduplicated -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["js", "SigBundle-JS", "Signature-original: JS bundler with whole-program analysis and Sig tree-shaking. Targets: web/node/edge. Splitting: auto chunks. Speed: very fast.", {"bundler": "SigBundle-JS", "targets": "web/node/edge", "splitting": "auto chunks", "speed": "very fast"}], ["native", "SigBundle-Native", "Signature-original: native bundler linking multi-target artifacts. Targets: all Sig targets. Splitting: per-target. Speed: fast.", {"bundler": "SigBundle-Native", "targets": "all Sig targets", "splitting": "per-target", "speed": "fast"}], ["js", "SigBundle-Wasm", "Signature-original: WASM bundler composing modules with interface checks. Targets: wasm. Splitting: module graph. Speed: fast.", {"bundler": "SigBundle-Wasm", "targets": "wasm", "splitting": "module graph", "speed": "fast"}], ["mobile", "SigBundle-Mobile", "Signature-original: mobile bundler with asset slicing per device. Targets: iOS/Android. Splitting: device slices. Speed: fast.", {"bundler": "SigBundle-Mobile", "targets": "iOS/Android", "splitting": "device slices", "speed": "fast"}], ["edge", "SigBundle-Edge", "Signature-original: edge bundler with byte budgets enforced per route. Targets: edge. Splitting: route chunks. Speed: very fast.", {"bundler": "SigBundle-Edge", "targets": "edge", "splitting": "route chunks", "speed": "very fast"}], ["js", "SigBundle-Cache", "Signature-original: content-addressed bundles with immutable caching. Targets: web. Splitting: CAS chunks. Speed: instant rebuilds.", {"bundler": "SigBundle-Cache", "targets": "web", "splitting": "CAS chunks", "speed": "instant rebuilds"}], ["js", "SigBundle-Delta", "Signature-original: delta bundles shipping only changed modules. Targets: web. Splitting: delta chunks. Speed: fast updates.", {"bundler": "SigBundle-Delta", "targets": "web", "splitting": "delta chunks", "speed": "fast updates"}], ["js", "SigBundle-Verify", "Signature-original: verified bundles with SBOM and signatures. Targets: all. Splitting: signed chunks. Speed: fast.", {"bundler": "SigBundle-Verify", "targets": "all", "splitting": "signed chunks", "speed": "fast"}], ["js", "SigBundle-Poly", "Signature-original: polyglot bundler mixing JS, WASM, and native. Targets: mixed. Splitting: per-runtime. Speed: fast.", {"bundler": "SigBundle-Poly", "targets": "mixed", "splitting": "per-runtime", "speed": "fast"}], ["js", "SigBundle-Audit", "Signature-original: bundle auditing with duplicate and bloat detection. Targets: web. Splitting: analysis. Speed: analysis.", {"bundler": "SigBundle-Audit", "targets": "web", "splitting": "analysis", "speed": "analysis"}], ["js", "SigBundle-Lazy", "Signature-original: lazy-by-default bundling with prefetch hints. Targets: web. Splitting: lazy chunks. Speed: fast.", {"bundler": "SigBundle-Lazy", "targets": "web", "splitting": "lazy chunks", "speed": "fast"}], ["js", "SigBundle-I18n", "Signature-original: locale-split bundles loading only the user’s language. Targets: web. Splitting: locale chunks. Speed: fast.", {"bundler": "SigBundle-I18n", "targets": "web", "splitting": "locale chunks", "speed": "fast"}], ["js", "SigBundle-Theme", "Signature-original: theme-split assets for white-label apps. Targets: web. Splitting: theme chunks. Speed: fast.", {"bundler": "SigBundle-Theme", "targets": "web", "splitting": "theme chunks", "speed": "fast"}], ["edge", "SigBundle-Worker", "Signature-original: worker bundler targeting isolates with size limits. Targets: isolates. Splitting: isolate chunks. Speed: very fast.", {"bundler": "SigBundle-Worker", "targets": "isolates", "splitting": "isolate chunks", "speed": "very fast"}], ["js", "SigBundle-One", "Signature-original: the united bundler — one config, every target. Targets: everything. Splitting: unified. Speed: very fast.", {"bundler": "SigBundle-One", "targets": "everything", "splitting": "unified", "speed": "very fast"}]];
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
  if(!new RegExp('^'+'JAH\\-MTB\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('multi-target-bundlers-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
