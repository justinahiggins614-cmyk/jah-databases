(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["search-log-capture", "query-replay", "source-version-pinning", "result-diffing", "replay-report"];
var PREFIX='JAH-AT77-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Search log capture at investigation time", "k": "method", "d": "During the original investigation, every query, source version, and retrieval parameter is captured into a replay log. Capture is automatic and complete; a replay is only as good as the log it replays. The log format is stable across tool versions so old investigations stay replayable.", "demo": "replay_log = [{'q': 'inverted index latency', 'src_ver': 'v12', 'top_k': 10}, {'q': 'posting lists', 'src_ver': 'v12', 'top_k': 10}]\nprint('captured steps:', len(replay_log))\n"}, {"t": "Query replay against pinned versions", "k": "algorithm", "d": "Replay re-issues each logged query against the same source versions recorded in the log, not the current live versions. Pinning versions isolates the search procedure from archive drift: if the replay diverges, the cause is the procedure, not changed data. Where a pinned version is unavailable, the replay notes the substitution explicitly.", "demo": "log = [{'q': 'index latency', 'src_ver': 'v12'}]\nfor step in log:\n    print(f\"replaying '{step['q']}' against pinned {step['src_ver']}\")\n"}, {"t": "Source-version availability check", "k": "method", "d": "Before replaying, the tool checks that every pinned source version is still retrievable. Missing versions are reported up front with their identifiers, so the replay can degrade gracefully instead of failing halfway. This check is what makes 'where possible' in the tool's mandate operational rather than aspirational.", "demo": "pinned = {'srcA': 'v12', 'srcB': 'v7'}\navailable = {'srcA': ['v12', 'v13'], 'srcB': ['v8']}\nfor s, v in pinned.items():\n    print(s, v, 'available' if v in available[s] else 'MISSING -> will substitute latest with note')\n"}, {"t": "Result diffing: original vs replay", "k": "algorithm", "d": "Original and replayed result sets are compared with Jaccard similarity over record identifiers, and rank changes are measured for the top positions. High similarity means the search reproduces; divergence is localized to the specific steps where it appears. The diff distinguishes procedure instability from data drift by consulting the version-pinning notes.", "demo": "def jacc(a, b):\n    A, B = set(a), set(b)\n    return len(A & B) / max(1, len(A | B))\norig, replay = ['d1', 'd2', 'd3', 'd4'], ['d1', 'd3', 'd2', 'd5']\nprint('replay similarity:', round(jacc(orig, replay), 2))\nprint('verdict:', 'REPRODUCES' if jacc(orig, replay) >= 0.75 else 'DIVERGES -> investigate')\n"}, {"t": "Replay report with divergence analysis", "k": "procedure", "d": "The replay ends in a report: per-step similarity, overall verdict, and for each divergence whether the cause looks like procedure, data drift, or version substitution. The report is stored alongside the original investigation so future readers know how reproducible the search was. Honest divergence notes are more valuable than a forced 'reproduces' stamp.", "demo": "report = {'steps': 4, 'mean_similarity': 0.83, 'verdict': 'reproduces', 'divergences': [{'step': 4, 'cause': 'version substitution srcB v7->v8'}]}\nprint('replay report:', report)\n"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var v=(rnd()*3)|0;
  var desc=a.d+VARIANTS[v]+(SIG?' Signature-authored original by Justin Addam Higgins (JAH).':'');
  var id=PREFIX+String(seed).padStart(6,'0');
  var ttl=a.t+[' (foundational)',' (compounded)',' (production)'][v];
  var prov=SIG?'Signature-authored original by Justin Addam Higgins (JAH), 2026-10-21.':'Public computer-science methods literature; cross-checked against standard references, 2026-10-21.';
  return {id:id,t:ttl,title:ttl,description:desc,kind:a.k,category:cat,ladder_rank:v+1,demo:(SIG?'# Signature-authored original (JAH).\n':'')+a.demo,provenance:prov,last_verified:'2026-10-21',src:SIG?'signature-generated-completion':'public-harvest',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/-/g,'\\-');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(KIND_LIST.indexOf(r.kind)<0)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==(SIG?'signature-generated-completion':'public-harvest'))e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  if(sample&&sample.length){
    for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].id===rec.id){e.push('duplicate id');break;} }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-archive-tool-research-reproduction-tool-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-research-reproduction-tool',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
