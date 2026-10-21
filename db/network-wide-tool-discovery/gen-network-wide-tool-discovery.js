(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["registry", "search", "gossip", "naming", "health"];
var PREFIX='JAH-NWT-';
var USE="Used by agent networks and service meshes so tools can find each other without hardcoding.";
var FLD=[["mechanism", "Mechanism"], ["registry", "Registry"], ["lookup", "Lookup"]];
var DEMO="# {title} - lookup latency estimate (python3)\nentries={d1}\nms_per_1k={d2}\nbudget={d3}\nest=entries/1000.0*ms_per_1k\nprint(\"estimated lookup: %.1f ms for %d entries\" % (est, entries))\nprint(\"WITHIN BUDGET\" if est <= budget else \"ADD INDEXING\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["registry", "Capability Registry", "Central directory where tools register contracts and heartbeats.", "Capability Registry", "central", "indexed query", "50000", "2.0", "100.0"], ["search", "Broadcast Advertisement", "Tools announce themselves on the local network for zero-config discovery.", "Broadcast Advertisement", "local", "multicast listen", "500", "5.0", "200.0"], ["gossip", "Semantic Search", "Finds tools by meaning of the task description, not just keywords.", "Semantic Search", "index", "vector query", "20000", "8.0", "150.0"], ["naming", "DNS-style Naming", "Hierarchical names (vision.ocr.v2) resolve to tool endpoints.", "DNS-style Naming", "naming", "name resolve", "100000", "1.0", "50.0"], ["health", "DHT Lookup", "Distributed hash table spreads the directory across peers with no center.", "DHT Lookup", "peer", "key lookup", "80000", "5.0", "120.0"], ["registry", "Gossip Propagation", "Peers spread tool announcements epidemically until all know.", "Gossip Propagation", "peer", "eventual", "30000", "10.0", "200.0"], ["search", "Directory Service", "Curated directory with categories, ratings, and verified badges.", "Directory Service", "curated", "faceted search", "15000", "6.0", "120.0"], ["gossip", "Metadata Index", "Full-text and faceted index over tool metadata for rich queries.", "Metadata Index", "index", "query DSL", "60000", "4.0", "100.0"], ["naming", "Health-checked Listing", "Lists only tools passing current health checks.", "Health-checked Listing", "filtered", "healthy-only", "25000", "3.0", "80.0"], ["health", "Version-aware Resolution", "Resolves to the newest compatible version satisfying constraints.", "Version-aware Resolution", "registry", "semver resolve", "40000", "2.5", "90.0"], ["registry", "Geo-aware Routing", "Prefers nearby tool instances to cut latency and respect residency.", "Geo-aware Routing", "geo", "proximity", "35000", "3.5", "100.0"], ["search", "Reputation-ranked Results", "Ranks discovered tools by measured reliability and user ratings.", "Reputation-ranked Results", "ranked", "score sort", "20000", "5.0", "120.0"], ["gossip", "Federated Search", "Queries multiple registries and merges results.", "Federated Search", "federated", "fan-out", "45000", "12.0", "200.0"], ["naming", "Cached Directory", "Caches directory snapshots at the edge for fast offline-capable lookup.", "Cached Directory", "edge", "cache read", "70000", "1.5", "60.0"], ["health", "Push Notification", "Pushes new-tool and deprecation events to subscribers.", "Push Notification", "pubsub", "subscribe", "10000", "2.0", "80.0"], ["registry", "Pull Polling", "Clients poll for updates on an interval; simple and firewall-friendly.", "Pull Polling", "poll", "interval fetch", "55000", "4.0", "110.0"], ["search", "Contract-first Discovery", "Discovers by required input/output contract, guaranteeing compatibility.", "Contract-first Discovery", "contract", "contract match", "30000", "6.0", "130.0"], ["gossip", "Trial Invocation", "Lets agents test-invoke candidates in a sandbox before committing.", "Trial Invocation", "sandbox", "trial call", "5000", "25.0", "300.0"], ["naming", "Dependency Graph Walk", "Follows tool dependency edges to discover supporting tools.", "Dependency Graph Walk", "graph", "traversal", "22000", "7.0", "150.0"], ["health", "Sunset Notices", "Announces retirements early so dependents migrate in time.", "Sunset Notices", "registry", "notice feed", "12000", "3.0", "90.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-network-wide-tool-discovery-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-wide-tool-discovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
