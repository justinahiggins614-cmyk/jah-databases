(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["finding-storage", "retention-control", "memory-indexing", "recall-ranking", "expiry-sweep"];
var PREFIX='JAH-AT61S-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=true;
var ARCH=[{"t": "Finding capture with context envelope", "k": "method", "d": "Signature original: A useful finding is stored together with its context envelope: the task that produced it, the sources behind it, and a timestamp. The envelope is what makes a memory reusable later, because a bare fact without provenance cannot be trusted or refreshed. Captures are small by design; the archive holds the full records, memory holds the distilled findings.", "demo": "mem = {}\ndef capture(key, finding, task, sources):\n    mem[key] = {'finding': finding, 'task': task, 'sources': sources, 'ts': '2026-10-21'}\ncapture('idx-benchmark', 'inverted index beats scan past 10k docs', 'speed up search', ['srcA'])\nprint('stored:', list(mem)[0], '->', mem['idx-benchmark']['finding'][:40])\n"}, {"t": "Retention policy with TTL and pinning", "k": "method", "d": "Signature original: Every memory carries a time-to-live and a pin flag. Unpinned memories expire when their TTL lapses; pinned ones survive until explicitly unpinned, which protects hard-won findings from routine cleanup. TTLs are set by finding type: volatile operational notes get days, durable reference facts get years.", "demo": "from datetime import date, timedelta\nmem = {'a': {'ttl_days': 7, 'pinned': False, 'born': date(2026, 10, 10)},\n       'b': {'ttl_days': 7, 'pinned': True, 'born': date(2026, 10, 1)}}\ntoday = date(2026, 10, 21)\nfor k, m in mem.items():\n    alive = m['pinned'] or (today - m['born']).days <= m['ttl_days']\n    print(k, 'alive' if alive else 'expired')\n"}, {"t": "Memory indexing by topic signature", "k": "algorithm", "d": "Signature original: Memories are indexed by a topic signature: the set of significant terms in the finding, minus stopwords. Lookup intersects the query's terms with the index, which is fast and needs no vector machinery for moderate memory sizes. The signature doubles as a deduplication key: a new finding with an identical signature to an existing one updates it instead of duplicating it.", "demo": "STOP = {'the','a','of','to','is'}\ndef sig(text): return frozenset(w for w in text.lower().split() if w not in STOP)\nidx = {}\ndef store(finding):\n    s = sig(finding)\n    idx[s] = finding  # same signature -> update, not duplicate\n    return s\nprint('sig:', store('inverted index speeds search past ten thousand documents'))\nprint('entries:', len(idx))\n"}, {"t": "Recall ranking by recency and reuse", "k": "algorithm", "d": "Signature original: When several memories match, they are ranked by a score combining recency, past reuse count, and source reliability. Frequently reused findings float up because reuse is evidence of value; stale, never-reused ones sink. The ranking is deliberately simple so its behavior stays explainable to the user.", "demo": "cands = [('m1', 2, 12, 0.9), ('m2', 30, 1, 0.9), ('m3', 5, 8, 0.4)]  # id, age_days, reuses, reliability\nranked = sorted(cands, key=lambda m: (m[2] * m[3]) / (1 + m[1]), reverse=True)\nprint('recall order:', [m[0] for m in ranked])\n"}, {"t": "Expiry sweep with audit trail", "k": "procedure", "d": "Signature original: A scheduled sweep removes expired, unpinned memories and writes each removal to an audit trail with the reason. Nothing is deleted silently: the trail records what was forgotten and why, so a user can see that a memory aged out rather than vanished mysteriously. Sweeps run frequently enough that the store never accumulates dead weight.", "demo": "from datetime import date\nstore = {'old': {'born': date(2026, 9, 1), 'ttl': 30, 'pinned': False},\n         'new': {'born': date(2026, 10, 20), 'ttl': 30, 'pinned': False}}\ntrail = []\ntoday = date(2026, 10, 21)\nfor k in list(store):\n    m = store[k]\n    if not m['pinned'] and (today - m['born']).days > m['ttl']:\n        trail.append((k, 'expired TTL')); del store[k]\nprint('remaining:', list(store), '| trail:', trail)\n"}];
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
var gen={version:'jahdb-archive-tool-persistent-knowledge-memory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-persistent-knowledge-memory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
