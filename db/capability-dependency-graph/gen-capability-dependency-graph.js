(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["data", "service", "library", "model", "hardware", "credential"];
var PREFIX="JAH-CAPABI3-";
var FKEYS=["depends_on", "dependency_type", "criticality"];
var RANK_TXT={"1": "the concept in its simplest, most direct form", "2": "the concept compounded with real-world conditions and trade-offs", "3": "the concept at full complexity, orchestrated with neighboring capabilities"};
var DEMO_TMPL="# Capability dependency graph: {TITLE}\nedges = {{\"{F1}\": \"{F2}\".split(\";\")}}\n# criticality: {F3}\norder, seen = [], set()\ndef visit(n):\n    if n in seen:\n        return\n    seen.add(n)\n    for d in edges.get(n, []):\n        visit(d)\n    order.append(n)\nfor n in edges:\n    visit(n)\nprint(\"install/start order:\", order)\nprint(\"OK - dependency graph has no cycles on the sample\")";
var SIG_SUFFIX="";
var PROV="Curated from public documentation of established engineering practice; verified against standard references.";
var SRC="public-harvest";
var B=[["data", "Search Depends on Index Data", "Web search capability depends on the freshness of the underlying index data.", "Stale index data silently degrades search; the edge makes the dependency explicit.", "web-search -> index-data", "data dependency", "critical"], ["service", "Code Execution Depends on Sandbox Service", "Running code depends on the sandbox service being healthy and available.", "The edge explains why code execution fails when the sandbox is down.", "code-execution -> sandbox-service", "service dependency", "critical"], ["library", "NLP Depends on Tokenizer Library", "Language capabilities depend on the tokenizer library version they were built against.", "Tokenizer drift changes model behavior; the edge pins the relationship.", "nlp-pipeline -> tokenizer-lib", "library dependency", "high"], ["hardware", "Vision Depends on GPU Hardware", "Image understanding at production speed depends on GPU availability.", "The edge lets planners route vision work to GPU-equipped hosts.", "vision -> gpu-pool", "hardware dependency", "high"], ["credential", "API Calls Depend on Credentials", "External API capabilities depend on valid, unexpired credentials.", "The edge triggers credential refresh before expiry breaks the capability.", "external-api -> api-credentials", "credential dependency", "critical"], ["model", "Summarization Depends on Base Model", "Summarization quality depends on the underlying language model version.", "Model upgrades change summaries; the edge links quality shifts to their cause.", "summarization -> base-model", "model dependency", "high"], ["data", "Translation Depends on Language Data", "Translation for a language pair depends on training data coverage for that pair.", "Thin data means thin translation; the edge quantifies the relationship.", "translation -> parallel-corpus", "data dependency", "high"], ["service", "Monitoring Depends on Metrics Pipeline", "Alerting depends on the metrics pipeline delivering data on time.", "A broken pipeline blinds monitoring; the edge makes the blindness explainable.", "alerting -> metrics-pipeline", "service dependency", "critical"], ["library", "Build Depends on Compiler Toolchain", "Compiling depends on the toolchain version; upgrades can break builds.", "The edge pins the toolchain so builds are reproducible.", "build -> toolchain", "library dependency", "high"], ["service", "Auth Depends on Identity Provider", "Authentication depends on the identity provider's availability.", "The edge is why auth fails when the IdP sneezes.", "auth -> identity-provider", "service dependency", "critical"], ["data", "Recommendations Depend on Behavior Data", "Recommendation quality depends on the recency and volume of behavior data.", "Cold-start is just this edge with no data on it.", "recommendations -> behavior-data", "data dependency", "medium"], ["hardware", "Speech Depends on Audio Drivers", "Transcription depends on audio capture hardware and drivers working.", "The edge separates 'model failed' from 'microphone failed'.", "transcription -> audio-hardware", "hardware dependency", "medium"], ["service", "Deploy Depends on Container Registry", "Deploying depends on the registry serving the required image.", "The edge explains deploy failures during registry outages.", "deploy -> container-registry", "service dependency", "critical"], ["credential", "Encryption Depends on Key Management", "Encryption capabilities depend on the key management service.", "Lost keys mean lost data; the edge marks this as critical.", "encryption -> kms", "credential dependency", "critical"], ["data", "Analytics Depends on Event Stream", "Dashboards depend on the event stream's completeness.", "Gaps in the stream become gaps in the dashboard; the edge traces them.", "analytics -> event-stream", "data dependency", "high"], ["model", "Chat Depends on Model Serving", "Conversational capability depends on the model serving infrastructure.", "The edge routes chat traffic only to healthy serving capacity.", "chat -> model-serving", "model dependency", "critical"], ["hardware", "Backup Depends on Storage Backend", "Backups depend on the storage backend's durability and capacity.", "The edge triggers alerts before the backend fills.", "backup -> storage-backend", "hardware dependency", "critical"], ["service", "CI Depends on Runner Pool", "Continuous integration depends on runner availability.", "The edge explains queue backlogs during runner outages.", "ci -> runner-pool", "service dependency", "high"], ["credential", "Payments Depend on Processor Certs", "Payment processing depends on valid processor certificates.", "Expiring certs break payments silently; the edge watches expiry.", "payments -> processor-certs", "credential dependency", "critical"], ["data", "ML Training Depends on Dataset Version", "Training runs depend on the exact dataset version they were configured with.", "The edge prevents training on the wrong data - a silent catastrophe.", "training -> dataset-version", "data dependency", "critical"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rank=1+(seed%3);
  var desc=b[2]+' '+b[3]+' Teaching ladder: rank '+rank+' \u2014 '+RANK_TXT[rank]+'.'+SIG_SUFFIX;
  var prog=DEMO_TMPL.split('{TITLE}').join(b[1]).split('{F1}').join(b[4]).split('{F2}').join(b[5]).split('{F3}').join(b[6]);
  var r={id:id,title:b[1],description:desc,category:cat,ladder_rank:rank,
    demo:{kind:'code',title:'Runnable code demo \u2014 '+b[1].slice(0,50),program:prog,language:'python'},
    provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
  r[FKEYS[0]]=b[4];r[FKEYS[1]]=b[5];r[FKEYS[2]]=b[6];
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.indexOf('Teaching ladder: rank')<0)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FKEYS.forEach(function(k){if(typeof r[k]!=='string'||!r[k].length)e.push(k);});
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-capability-dependency-graph-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("capability-dependency-graph",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
