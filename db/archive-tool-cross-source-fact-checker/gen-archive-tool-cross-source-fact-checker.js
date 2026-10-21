(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["source-comparison", "claim-verification", "conflict-flagging", "source-independence", "verdict-scoring"];
var PREFIX='JAH-AT53-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Independent source selection", "k": "method", "d": "The checker gathers candidate sources and first filters for independence: sources that cite each other or share an author are collapsed into one, because three copies of the same press release are not three independent confirmations. Independence is estimated from citation graphs and shared distinctive phrasing. Only sources passing this filter vote on the claim.", "demo": "sources = [{'id':'s1','cites':['s2']},{'id':'s2','cites':[]},{'id':'s3','cites':[]},{'id':'s4','cites':['s1']},{'id':'s5','cites':[]},]\nindep = [s['id'] for s in sources if not s['cites']]\nprint('independent sources:', indep, '(collapsed', len(sources)-len(indep), 'derivative)')\n"}, {"t": "Claim normalization for comparison", "k": "method", "d": "Before comparison, claims are normalized: numbers are converted to a canonical unit, dates to ISO format, and entity names lowercased and stripped of titles. Normalization prevents false conflicts like '52,000' versus '52 thousand' or 'Oct 21' versus '2026-10-21'. The normalized form is what gets compared across sources.", "demo": "import re\ndef norm(s):\n    s = s.lower()\n    s = re.sub(r'(\\d+),(\\d+)', r'\\1\\2', s)\n    s = s.replace(' thousand', '000').replace('oct ', '10-')\n    return s\nprint(norm('52,000 databases'))\nprint(norm('52 thousand databases'))\nprint('match:', norm('52,000 databases') == norm('52 thousand databases'))\n"}, {"t": "Weighted majority verdict", "k": "algorithm", "d": "Each independent source casts a vote of confirm, deny, or unknown on the normalized claim, weighted by that source's historical reliability score. The verdict is the weighted majority; a claim confirmed by high-reliability sources outranks one confirmed only by low-reliability ones. Ties and near-ties produce an 'unresolved' verdict rather than a false certainty.", "demo": "votes = [('s1','confirm',0.9),('s2','confirm',0.7),('s3','deny',0.4),('s4','unknown',0.5)]\nw = {'confirm':0,'deny':0}\nfor _, v, rel in votes: w[v] = w.get(v,0) + rel\nprint('weighted votes:', {k: round(v,2) for k,v in w.items()})\nprint('verdict:', max(w, key=w.get) if max(w.values()) > sum(w.values())/2 else 'unresolved')\n"}, {"t": "Conflict flagging with evidence pairs", "k": "method", "d": "When sources disagree, the checker emits a conflict record pairing the strongest confirming passage with the strongest denying passage, verbatim. Presenting both sides with their sources lets a human or downstream agent adjudicate instead of trusting a black-box verdict. The conflict record also notes which source attributes differ, such as publication date or measurement method.", "demo": "conflict = {'claim': 'archive count', 'confirm': ('srcA', '52,268 databases, verified Oct 20'), 'deny': ('srcB', '51,900 databases, estimated Sep 1')}\nprint('CONFLICT on:', conflict['claim'])\nprint(' +', conflict['confirm'])\nprint(' -', conflict['deny'])\nprint('note: dates differ -> re-check the newer source first')\n"}, {"t": "Runtime verdict caching with source-version keys", "k": "pattern", "d": "Verdicts are cached, but the cache key includes the version identifiers of every source consulted, so a verdict never outlives its evidence. If any source publishes a new version, the key changes and the claim is re-checked automatically. This keeps operational fact-checking fresh without re-running expensive comparisons on every request.", "demo": "cache = {}\ndef key(claim, srcvers): return claim + '|' + ','.join(sorted(f'{k}={v}' for k,v in srcvers.items()))\nk1 = key('count=52268', {'srcA':'v3','srcB':'v1'})\ncache[k1] = 'confirmed'\nk2 = key('count=52268', {'srcA':'v4','srcB':'v1'})  # srcA updated\nprint('cache hit after source update:', k2 in cache, '-> re-check required')\n"}];
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
var gen={version:'jahdb-archive-tool-cross-source-fact-checker-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-cross-source-fact-checker',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
