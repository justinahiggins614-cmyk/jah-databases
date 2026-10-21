(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["tracing", "metrics", "ebpf", "logging", "profiling-live"];
var PREFIX="JAH-RUNTIM-";
var FIELDS=["technique", "target", "method", "signal", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Distributed Tracing (OpenTelemetry)", "Requests carry trace IDs across services; spans assemble into full request timelines. The trace shows the whole journey. Journeys get visible.", "tracing", 2, "OTel tracing", "Requests", "Span assembly", "Full timeline", "Visible journeys", "Medium"], ["RED Metrics (Rate/Errors/Duration)", "Services expose rate, errors, and duration; the three numbers summarize health. RED is the service dashboard. Health gets three numbers.", "metrics", 1, "RED", "Services", "Three metrics", "Health summary", "Three numbers", "Low"], ["USE Metrics (Util/Sat/Errors)", "Resources expose utilization, saturation, and errors; USE finds the bottlenecked resource. The method is systematic. Bottlenecks get found.", "metrics", 1, "USE", "Resources", "Three checks", "Bottleneck", "Systematic", "Low"], ["eBPF Observability", "eBPF programs observe the kernel safely: syscalls, network, scheduling, all without stopping anything. The superpower is safe kernel vision. Systems get transparent.", "ebpf", 3, "eBPF", "Kernel", "Safe programs", "Kernel events", "Transparent", "High"], ["Structured Logging", "Logs as JSON with trace IDs and fields; machines parse them, humans read them. Structure gets queryable. Logs get useful.", "logging", 1, "JSON logs", "Events", "Structured emit", "Queryable logs", "Useful", "Low"], ["Log Aggregation (ELK/Loki)", "Logs centralize for search across the fleet; the aggregation makes distributed debugging possible. Fleets get searchable. Needles get found.", "logging", 2, "Aggregation", "Fleet logs", "Central search", "Found needle", "Searchable", "Medium"], ["Continuous Profiling in Prod", "Always-on profilers sample production; the profiles reveal real hotspots. Production gets profiled. Reality gets measured.", "profiling-live", 2, "Always-on", "Production", "Sampling", "Real hotspots", "Measured reality", "Medium"], ["Service Mesh Telemetry", "Meshes (Istio) emit telemetry per request automatically; the mesh observes everything. Observation gets free. Services get watched.", "tracing", 2, "Mesh telemetry", "Service mesh", "Auto emit", "Per-request data", "Free observation", "Medium"], ["Alerting on SLOs", "Alerts fire on SLO burn rate, not on raw metrics; the alert means user impact. Alerts get meaningful. Pages get deserved.", "metrics", 2, "Burn alert", "SLOs", "Error budget", "Burn rate", "Meaningful", "Medium"], ["Cardinality Management", "Metric label cardinality is bounded; unbounded labels explode storage. Management gets disciplined. Storage gets saved.", "metrics", 2, "Bound labels", "Metrics", "Cardinality caps", "Bounded storage", "Saved storage", "Medium"], ["Trace Sampling Strategies", "Head/tail sampling balances cost and completeness; tail sampling keeps the interesting traces. Strategies get smart. Costs get bounded.", "tracing", 2, "Tail sample", "Traces", "Smart keep", "Interesting kept", "Bounded cost", "Medium"], ["eBPF Network Observability", "eBPF sees every packet with low overhead: retransmits, drops, latency per flow. Networks get transparent. Packets get watched.", "ebpf", 3, "Packet watch", "Network", "eBPF hooks", "Per-flow data", "Transparent", "High"], ["Runtime Security Observability", "eBPF watches for anomalous syscalls: the security gets behavioral. Anomalies get caught. Intrusions get seen.", "ebpf", 3, "Syscall watch", "Security", "Behavioral", "Anomaly", "Seen intrusions", "High"], ["Profiling Flame Graphs Live", "Live flame graphs update from production profiles; the hot code is always visible. Flames get live. Hotspots get watched.", "profiling-live", 1, "Live flames", "Production", "Streaming", "Visible hot", "Watched", "Low"], ["Correlation: Logs+Metrics+Traces", "The three pillars correlate by trace ID and time; together they tell the full story. Pillars get joined. Stories get complete.", "tracing", 2, "Correlate", "Pillars", "ID + time join", "Full story", "Complete", "Medium"], ["Observability Cost Control", "Telemetry volume is budgeted; sampling and aggregation keep costs sane. Costs get managed. Bills get bounded.", "metrics", 1, "Budgeting", "Telemetry", "Volume caps", "Bounded bill", "Managed", "Low"], ["Blackbox vs Whitebox", "Blackbox probes the outside, whitebox instruments the inside; both are needed. Perspectives get combined. Coverage gets complete.", "logging", 1, "Both", "Systems", "Probe + instrument", "Combined view", "Complete", "Low"], ["Chaos + Observability", "Chaos experiments need observability to verify the hypothesis; the two practices pair. Pairs get powerful. Hypotheses get checked.", "tracing", 2, "Pairing", "Experiments", "Observe chaos", "Checked hypothesis", "Powerful pair", "Medium"], ["On-Call Runbook Links", "Alerts link to runbooks; the link turns pages into procedures. Pages get actionable. On-call gets humane.", "logging", 1, "Runbook links", "Alerts", "Linked docs", "Actionable page", "Humane", "Low"], ["Postmortem Data Collection", "Incidents collect the telemetry automatically; the postmortem gets evidence. Collection gets automatic. Blame gets replaced by learning.", "logging", 2, "Auto collect", "Incidents", "Evidence bundle", "Learning", "Automatic", "Medium"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'spans = [(\"web\", 120), (\"db\", 80), (\"cache\", 5)]\ntotal = sum(d for _, d in spans)\nfor name, d in spans:\n    print(\"%-6s %dms (%d%%)\" % (name, d, 100 * d / total))\nprint(\"slowest span:\", max(spans, key=lambda x: x[1])[0])\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-runtime-observability-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("runtime-observability",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
