(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cdn", "client", "server", "dns", "degraded"];
var PREFIX='JAH-ISF-';
var GENVER='jahdb-instant-static-fallbacks-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["pattern", "triggers", "serves", "example"];
var DEMO_TPL="// $TITLE - fallback chain demo\nvar chain = [\n  { name: \"live backend\", ok: false },\n  { name: \"$PATTERN\", ok: true }\n];\nvar served = null;\nfor (var i = 0; i < chain.length; i++) { if (chain[i].ok) { served = chain[i].name; break; } }\nconsole.log(\"Pattern: $PATTERN | Serves: $SERVES\");\nconsole.log(\"Backend down -> fallback engaged: \" + served);\nconsole.log(served ? \"RESULT: user still gets a page -> PASS\" : \"RESULT: outage\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cdn", "CDN stale-while-revalidate", "Serve the stale cached copy instantly while the CDN revalidates in the background. Triggers when origin slow or erroring; serves stale cached page. Example: Cache-Control: max-age=60, stale-while-revalidate=300.", {"pattern": "stale-while-revalidate", "triggers": "origin slow or erroring", "serves": "stale cached page", "example": "Cache-Control: max-age=60, stale-while-revalidate=300"}], ["client", "Service worker offline page", "A service worker serving a cached app shell and offline page when the network fails. Triggers when network failure; serves cached shell + offline page. Example: workbox precaching + catch handler.", {"pattern": "offline-first SW", "triggers": "network failure", "serves": "cached shell + offline page", "example": "workbox precaching + catch handler"}], ["server", "nginx try_files cascade", "try_files walks a list of files and falls back to a static page or named location. Triggers when missing file/route; serves fallback file. Example: try_files $uri $uri/ /fallback.html;.", {"pattern": "try_files", "triggers": "missing file/route", "serves": "fallback file", "example": "try_files $uri $uri/ /fallback.html;"}], ["server", "Pre-rendered error pages", "Static 50x pages served by the edge so error pages never depend on the app server. Triggers when 5xx from origin; serves branded static page. Example: error_page 500 502 /50x.html;.", {"pattern": "static error pages", "triggers": "5xx from origin", "serves": "branded static page", "example": "error_page 500 502 /50x.html;"}], ["dns", "DNS failover", "Route 53 health checks flip DNS to a standby region when the primary fails checks. Triggers when health-check failure; serves standby region. Example: Route 53 failover routing policy.", {"pattern": "DNS failover", "triggers": "health-check failure", "serves": "standby region", "example": "Route 53 failover routing policy"}], ["degraded", "Read-only degraded mode", "Disable writes but keep reads serving from replicas during an incident. Triggers when primary DB down; serves read traffic. Example: feature flag: writes_enabled=false.", {"pattern": "read-only mode", "triggers": "primary DB down", "serves": "read traffic", "example": "feature flag: writes_enabled=false"}], ["cdn", "Last-known-good API cache", "The edge serves the last successful API response with a warning header when origin dies. Triggers when origin 5xx/timeout; serves last good JSON. Example: stale-if-error=86400.", {"pattern": "stale API cache", "triggers": "origin 5xx/timeout", "serves": "last good JSON", "example": "stale-if-error=86400"}], ["server", "Static mirror", "A periodic rsync mirror of the site that the load balancer promotes when the app tier fails. Triggers when app tier down; serves mirrored static site. Example: rsync -a --delete origin::www /mirror.", {"pattern": "static mirror", "triggers": "app tier down", "serves": "mirrored static site", "example": "rsync -a --delete origin::www /mirror"}], ["server", "Maintenance page with Retry-After", "A 503 plus Retry-After tells clients and crawlers to come back instead of hammering. Triggers when planned downtime; serves 503 + Retry-After. Example: return 503; add_header Retry-After 3600;.", {"pattern": "maintenance page", "triggers": "planned downtime", "serves": "503 + Retry-After", "example": "return 503; add_header Retry-After 3600;"}], ["client", "PWA app shell", "The shell (header/nav) loads from cache instantly; only content waits on network. Triggers when slow network; serves instant shell. Example: cache.addAll([\"/\",\"/shell.html\"]).", {"pattern": "app shell", "triggers": "slow network", "serves": "instant shell", "example": "cache.addAll([\"/\",\"/shell.html\"])"}], ["degraded", "Feature-flag kill switch", "Flags disable the broken feature in seconds without a deploy. Triggers when feature incident; serves reduced functionality. Example: flags.new_checkout=false.", {"pattern": "kill switch", "triggers": "feature incident", "serves": "reduced functionality", "example": "flags.new_checkout=false"}], ["client", "Image onerror placeholder", "onerror swaps broken images for a local placeholder so layouts never collapse. Triggers when image 404; serves placeholder. Example: <img onerror=\"this.src='/img/ph.png'\">.", {"pattern": "image fallback", "triggers": "image 404", "serves": "placeholder", "example": "<img onerror=\"this.src='/img/ph.png'\">"}], ["cdn", "API snapshot fallback", "Edge workers serve yesterday’s snapshot of an API feed when the generator stalls. Triggers when feed generator stalled; serves snapshot JSON. Example: KV-stored daily snapshot.", {"pattern": "snapshot fallback", "triggers": "feed generator stalled", "serves": "snapshot JSON", "example": "KV-stored daily snapshot"}], ["degraded", "Outbox queue for writes", "Writes queue locally (outbox pattern) and sync when the backend recovers. Triggers when backend unreachable; serves queued writes. Example: SQLite outbox + sync worker.", {"pattern": "outbox queue", "triggers": "backend unreachable", "serves": "queued writes", "example": "SQLite outbox + sync worker"}], ["server", "Pre-built static export", "A nightly static export of the whole site stands ready behind the dynamic one. Triggers when dynamic tier failure; serves full static site. Example: next export && sync to edge.", {"pattern": "static export", "triggers": "dynamic tier failure", "serves": "full static site", "example": "next export && sync to edge"}]];
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
  if(!new RegExp('^'+'JAH\\-ISF\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('instant-static-fallbacks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
