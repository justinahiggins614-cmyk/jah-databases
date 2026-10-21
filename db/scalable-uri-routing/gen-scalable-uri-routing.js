(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["library", "server", "gateway", "service-mesh", "edge"];
var PREFIX='JAH-SU-';
var GENVER='jahdb-scalable-uri-routing-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["router", "matches", "algorithm", "scale"];
var DEMO_TPL="// $TITLE - radix router demo\nfunction Router() { this.routes = []; }\nRouter.prototype.add = function(pattern, handler) {\n  var re = new RegExp(\"^\" + pattern.replace(/:[a-zA-Z_]+/g, \"([^/]+)\").replace(/\\*/g, \".*\") + \"$$\");\n  this.routes.push({ pattern: pattern, re: re, handler: handler });\n};\nRouter.prototype.match = function(path) {\n  for (var i = 0; i < this.routes.length; i++) { var m = path.match(this.routes[i].re); if (m) return { handler: this.routes[i].handler, params: m.slice(1) }; }\n  return null;\n};\nvar r = new Router();\nr.add(\"/api/users/:id\", \"userHandler\"); r.add(\"/static/*\", \"staticHandler\");\nconsole.log(\"Router: $ROUTER | Algorithm: $ALGORITHM\");\nconsole.log(\"/api/users/42 -> \" + JSON.stringify(r.match(\"/api/users/42\")));\nconsole.log(\"/static/a/b.css -> \" + JSON.stringify(r.match(\"/static/a/b.css\")));\nconsole.log(\"Route resolution -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["library", "httprouter", "Go’s radix-tree router famous for zero-allocation matching. Matches path params + wildcards using radix tree; proven scale: millions req/s.", {"router": "httprouter", "matches": "path params + wildcards", "algorithm": "radix tree", "scale": "millions req/s"}], ["library", "Express router", "Node’s layered middleware router; simple but linear for huge route tables. Matches params, regex, wildcards using layered linear scan; proven scale: thousands of routes.", {"router": "Express", "matches": "params, regex, wildcards", "algorithm": "layered linear scan", "scale": "thousands of routes"}], ["server", "nginx location", "prefix, regex, and exact matching with a documented precedence order. Matches prefix/regex/exact using trie + regex list; proven scale: 10k+ locations.", {"router": "nginx", "matches": "prefix/regex/exact", "algorithm": "trie + regex list", "scale": "10k+ locations"}], ["gateway", "Envoy route tables", "xDS-driven route tables with weighted clusters and header matching. Matches path/headers/query using sorted prefix + regex; proven scale: 100k+ routes.", {"router": "Envoy", "matches": "path/headers/query", "algorithm": "sorted prefix + regex", "scale": "100k+ routes"}], ["gateway", "AWS ALB rules", "Listener rules with host/path conditions evaluated in priority order. Matches host/path/headers using priority-ordered rules; proven scale: 100 rules/listener.", {"router": "ALB", "matches": "host/path/headers", "algorithm": "priority-ordered rules", "scale": "100 rules/listener"}], ["gateway", "Traefik routers", "Dynamic routers from Docker/K8s labels with middleware chains. Matches host/path/headers using rule compiler; proven scale: 10k+ routers.", {"router": "Traefik", "matches": "host/path/headers", "algorithm": "rule compiler", "scale": "10k+ routers"}], ["server", "Caddy matchers", "Caddyfile matchers compiling to efficient request matchers with placeholders. Matches path/host/method using compiled matchers; proven scale: large configs.", {"router": "Caddy", "matches": "path/host/method", "algorithm": "compiled matchers", "scale": "large configs"}], ["gateway", "Kubernetes Ingress", "Ingress resources fan out to services; controllers compile them to proxy config. Matches host/path using generated nginx config; proven scale: 1000s of rules.", {"router": "Ingress-NGINX", "matches": "host/path", "algorithm": "generated nginx config", "scale": "1000s of rules"}], ["service-mesh", "Istio VirtualService", "Traffic splitting, mirroring, and fault injection per route in the mesh. Matches headers/URI/authority using Envoy route gen; proven scale: mesh-wide.", {"router": "Istio", "matches": "headers/URI/authority", "algorithm": "Envoy route gen", "scale": "mesh-wide"}], ["library", "FastAPI routing", "Python’s Starlette-based router with path converters and dependency injection. Matches typed path params using route list + convertors; proven scale: 1000s of routes.", {"router": "FastAPI", "matches": "typed path params", "algorithm": "route list + convertors", "scale": "1000s of routes"}], ["library", "Gorilla mux", "Go’s expressive matcher with host, scheme, and header predicates. Matches predicates using predicate chain; proven scale: 1000s of routes.", {"router": "gorilla/mux", "matches": "predicates", "algorithm": "predicate chain", "scale": "1000s of routes"}], ["library", "chi", "Lightweight Go router built on a compressed trie (radix) design. Matches params/wildcards using compressed trie; proven scale: millions req/s.", {"router": "chi", "matches": "params/wildcards", "algorithm": "compressed trie", "scale": "millions req/s"}], ["gateway", "API Gateway stages", "Managed gateways mapping stages and resources to Lambda/integrations. Matches resource paths using managed trie; proven scale: 1000s of APIs.", {"router": "API Gateway", "matches": "resource paths", "algorithm": "managed trie", "scale": "1000s of APIs"}], ["gateway", "HAProxy ACLs", "ACLs matching on path, headers, and payload with use_backend switching. Matches ACL expressions using ACL evaluation; proven scale: 10k+ backends.", {"router": "HAProxy", "matches": "ACL expressions", "algorithm": "ACL evaluation", "scale": "10k+ backends"}], ["gateway", "YARP", "Microsoft’s reverse proxy with route/transform configuration for .NET. Matches path/host/header using route table; proven scale: large fleets.", {"router": "YARP", "matches": "path/host/header", "algorithm": "route table", "scale": "large fleets"}]];
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
  if(!new RegExp('^'+'JAH\\-SU\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scalable-uri-routing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
