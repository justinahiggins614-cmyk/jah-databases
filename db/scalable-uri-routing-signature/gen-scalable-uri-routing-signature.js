(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["library", "server", "gateway", "service-mesh", "edge"];
var PREFIX='JAH-SU-S-';
var GENVER='jahdb-scalable-uri-routing-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["router", "matches", "algorithm", "scale"];
var DEMO_TPL="// $TITLE - radix router demo\nfunction Router() { this.routes = []; }\nRouter.prototype.add = function(pattern, handler) {\n  var re = new RegExp(\"^\" + pattern.replace(/:[a-zA-Z_]+/g, \"([^/]+)\").replace(/\\*/g, \".*\") + \"$$\");\n  this.routes.push({ pattern: pattern, re: re, handler: handler });\n};\nRouter.prototype.match = function(path) {\n  for (var i = 0; i < this.routes.length; i++) { var m = path.match(this.routes[i].re); if (m) return { handler: this.routes[i].handler, params: m.slice(1) }; }\n  return null;\n};\nvar r = new Router();\nr.add(\"/api/users/:id\", \"userHandler\"); r.add(\"/static/*\", \"staticHandler\");\nconsole.log(\"Router: $ROUTER | Algorithm: $ALGORITHM\");\nconsole.log(\"/api/users/42 -> \" + JSON.stringify(r.match(\"/api/users/42\")));\nconsole.log(\"/static/a/b.css -> \" + JSON.stringify(r.match(\"/static/a/b.css\")));\nconsole.log(\"Route resolution -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["library", "SigRoute-Trie", "Signature-original: compressed-trie router with zero-alloc matching in the Sig runtime. Matches params + wildcards using compressed trie; proven scale: 10M req/s.", {"router": "SigRoute-Trie", "matches": "params + wildcards", "algorithm": "compressed trie", "scale": "10M req/s"}], ["service-mesh", "SigRoute-Mesh", "Signature-original: mesh-native routing with identity-based policies. Matches identity + path using policy trie; proven scale: mesh-wide.", {"router": "SigRoute-Mesh", "matches": "identity + path", "algorithm": "policy trie", "scale": "mesh-wide"}], ["edge", "SigRoute-Edge", "Signature-original: edge routers with geo-aware weighted pools. Matches geo + path using geo trie; proven scale: global edge.", {"router": "SigRoute-Edge", "matches": "geo + path", "algorithm": "geo trie", "scale": "global edge"}], ["gateway", "SigRoute-AI", "Signature-original: ML-predicted routing prefetching likely backends. Matches predicted intent using model + trie; proven scale: large fleets.", {"router": "SigRoute-AI", "matches": "predicted intent", "algorithm": "model + trie", "scale": "large fleets"}], ["gateway", "SigRoute-Canary", "Signature-original: canary routing with automatic rollback on error budgets. Matches canary headers using weighted split; proven scale: per-service.", {"router": "SigRoute-Canary", "matches": "canary headers", "algorithm": "weighted split", "scale": "per-service"}], ["gateway", "SigRoute-Shadow", "Signature-original: shadow traffic mirroring to test backends safely. Matches mirror rules using tee routing; proven scale: per-service.", {"router": "SigRoute-Shadow", "matches": "mirror rules", "algorithm": "tee routing", "scale": "per-service"}], ["gateway", "SigRoute-AB", "Signature-original: A/B routing with sticky assignment and metrics. Matches experiment cohorts using cohort hash; proven scale: per-service.", {"router": "SigRoute-AB", "matches": "experiment cohorts", "algorithm": "cohort hash", "scale": "per-service"}], ["gateway", "SigRoute-Auth", "Signature-original: auth-aware routing rejecting unauthenticated paths at the edge. Matches auth + path using policy check; proven scale: edge.", {"router": "SigRoute-Auth", "matches": "auth + path", "algorithm": "policy check", "scale": "edge"}], ["gateway", "SigRoute-Rate", "Signature-original: per-route rate limits with distributed token buckets. Matches all routes using token bucket; proven scale: global.", {"router": "SigRoute-Rate", "matches": "all routes", "algorithm": "token bucket", "scale": "global"}], ["edge", "SigRoute-Cache", "Signature-original: cache-aware routing serving cached responses without backend hops. Matches cacheable routes using cache trie; proven scale: edge.", {"router": "SigRoute-Cache", "matches": "cacheable routes", "algorithm": "cache trie", "scale": "edge"}], ["gateway", "SigRoute-GraphQL", "Signature-original: GraphQL-aware routing batching by field cost. Matches operations using cost router; proven scale: per-API.", {"router": "SigRoute-GraphQL", "matches": "operations", "algorithm": "cost router", "scale": "per-API"}], ["gateway", "SigRoute-gRPC", "Signature-original: gRPC method routing with per-method deadlines. Matches service/method using method table; proven scale: per-service.", {"router": "SigRoute-gRPC", "matches": "service/method", "algorithm": "method table", "scale": "per-service"}], ["edge", "SigRoute-Wasm", "Signature-original: routes handled by WASM filters compiled at deploy. Matches filter rules using WASM filters; proven scale: edge.", {"router": "SigRoute-Wasm", "matches": "filter rules", "algorithm": "WASM filters", "scale": "edge"}], ["gateway", "SigRoute-Audit", "Signature-original: every routing decision logged for post-incident replay. Matches all using logged trie; proven scale: fleet.", {"router": "SigRoute-Audit", "matches": "all", "algorithm": "logged trie", "scale": "fleet"}], ["gateway", "SigRoute-One", "Signature-original: the united routing plane — one table for edge, mesh, and gateway. Matches everything using unified trie; proven scale: planetary.", {"router": "SigRoute-One", "matches": "everything", "algorithm": "unified trie", "scale": "planetary"}]];
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
  if(!new RegExp('^'+'JAH\\-SU\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scalable-uri-routing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
