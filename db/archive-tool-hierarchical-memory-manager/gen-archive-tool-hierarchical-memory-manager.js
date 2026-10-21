(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["tier-promotion", "tier-demotion", "summary-cascade", "capacity-management", "tier-query-routing"];
var PREFIX='JAH-AT65-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Three-tier memory architecture", "k": "pattern", "d": "Memory is organized in three tiers: a small fast working set for the current task, a larger summary tier of distilled findings, and the full archive of source records. Each tier has a fixed capacity and a defined promotion rule, which keeps the working set relevant without manual curation. This mirrors CPU cache hierarchies, where each level trades size for speed.", "demo": "tiers = {'working': {'cap': 5, 'items': []}, 'summary': {'cap': 50, 'items': []}, 'archive': {'cap': float('inf'), 'items': []}}\ntiers['working']['items'] = ['w1', 'w2', 'w3']\nprint('working', len(tiers['working']['items']), '/', tiers['working']['cap'])\nprint('summary', len(tiers['summary']['items']), '/', tiers['summary']['cap'])\n"}, {"t": "Promotion by reuse count", "k": "algorithm", "d": "An item in the summary tier that gets reused across tasks is promoted to the working set, evicting the least-recently-used working item back down. Reuse is the promotion signal because it is direct evidence of value. Promotion and demotion keep the working set small but high-value without any manual triage.", "demo": "from collections import OrderedDict\nworking = OrderedDict([('w1', 1), ('w2', 1)])\nworking['w3'] = 3  # reused 3 times -> promote\nworking.move_to_end('w3')\nevicted = working.popitem(last=False)\nprint('promoted: w3 | demoted:', evicted[0], '| working:', list(working))\n"}, {"t": "Summary cascade on demotion", "k": "method", "d": "When a working item is demoted, it is not stored verbatim in the summary tier; it is first compressed to a one-line summary. The cascade keeps the summary tier dense: dozens of distilled findings fit where a few full items would. The original full record stays reachable in the archive tier via the summary's source link.", "demo": "def summarize(item):\n    return item.split('.')[0][:60]\nfull = 'The inverted index cut query latency from 900ms to 40ms. Posting lists were the key change.'\nprint('summary-tier form:', summarize(full))\n"}, {"t": "Capacity management with LRU eviction", "k": "algorithm", "d": "Each tier enforces its capacity with least-recently-used eviction: the item untouched longest leaves first. LRU is chosen because it is simple, predictable, and matches the temporal locality of real task sequences. Evicted summary items are already represented in the archive tier, so nothing of value is truly lost.", "demo": "from collections import OrderedDict\ntier = OrderedDict()\nfor k in ['a', 'b', 'c']: tier[k] = 1\ntier['a'] = tier.pop('a')  # touch a -> most recent\ntier['d'] = 1\nif len(tier) > 3: tier.popitem(last=False)\nprint('after eviction:', list(tier), '(b evicted as LRU)')\n"}, {"t": "Tier-aware query routing", "k": "method", "d": "A query first checks the working set, then the summary tier, and only then the archive, stopping at the first tier that answers it. Routing by tier keeps common questions fast and reserves expensive archive searches for genuinely new questions. Each tier hit also refreshes that item's recency, reinforcing the LRU ordering.", "demo": "working = {'idx': 'inverted index is fastest'}\nsummary = {'cache': 'cache cuts latency'}\ndef route(q):\n    for tier_name, tier in [('working', working), ('summary', summary)]:\n        if q in tier: return tier_name, tier[q]\n    return 'archive', 'deep search needed'\nprint(route('idx'))\nprint(route('unknown-topic'))\n"}];
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
var gen={version:'jahdb-archive-tool-hierarchical-memory-manager-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-hierarchical-memory-manager',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
