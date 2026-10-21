(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["conclusion-linking", "source-backtrace", "link-integrity", "provenance-display", "orphan-detection"];
var PREFIX='JAH-AT69S-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=true;
var ARCH=[{"t": "Conclusion-to-source link records", "k": "method", "d": "Signature original: Every conclusion stored in memory carries links to the source records it came from, with the record identifier and the derivation timestamp. The links are written at derivation time, when the sources are known, rather than reconstructed later from fuzzy matching. This makes backtracing exact instead of approximate.", "demo": "conclusion = {'text': 'inverted index is fastest past 10k docs', 'sources': ['JAH-AT92-000003', 'JAH-AT93-000001'], 'derived': '2026-10-21'}\nprint('conclusion links to', len(conclusion['sources']), 'source records')\n"}, {"t": "Backtrace query for any conclusion", "k": "algorithm", "d": "Signature original: Given a conclusion identifier, the linker returns the full chain of source records in one lookup, following links transitively through intermediate conclusions. Backtrace depth is capped to prevent runaway walks on cyclic links, with cycles reported explicitly. The result is the complete evidentiary ancestry of the memory.", "demo": "links = {'c1': ['s1', 'c0'], 'c0': ['s0']}\ndef backtrace(cid, depth=0):\n    if depth > 5: return ['...cycle cap']\n    out = []\n    for s in links.get(cid, []):\n        out.append(s)\n        out += backtrace(s, depth + 1)\n    return out\nprint('ancestry of c1:', backtrace('c1'))\n"}, {"t": "Link integrity verification", "k": "method", "d": "Signature original: Links are verified on read: each linked source record must still exist and its content hash must match the hash recorded at link time. A broken or altered link is reported, not silently followed, so conclusions never rest on sources that have vanished or changed underneath them. Verification failures trigger the invalidation tool downstream.", "demo": "import hashlib\nsrc = {'s1': 'inverted index data'}\nlink = {'sid': 's1', 'hash': hashlib.sha256(src['s1'].encode()).hexdigest()}\nok = link['sid'] in src and hashlib.sha256(src[link['sid']].encode()).hexdigest() == link['hash']\nprint('link integrity:', 'OK' if ok else 'BROKEN -> invalidate')\n"}, {"t": "Orphan conclusion detection", "k": "method", "d": "Signature original: A sweep finds conclusions whose every source link is broken or whose source records were deleted: these are orphans. Orphans are flagged for re-derivation or removal, because a conclusion with no surviving evidence is indistinguishable from a guess. The sweep runs on the same schedule as integrity verification.", "demo": "conclusions = {'c1': ['s1'], 'c2': ['s9']}\nalive_sources = {'s1'}\norphans = [c for c, ss in conclusions.items() if not any(s in alive_sources for s in ss)]\nprint('orphan conclusions needing re-derivation:', orphans)\n"}, {"t": "Provenance display for users", "k": "pattern", "d": "Signature original: When a memory is shown to a user, its provenance renders as a compact trail: conclusion, then each source with its title and derivation date. The display is read-only and generated from the link records, never hand-written, so what the user sees always matches what the linker verified. Transparency here is what earns trust in remembered conclusions.", "demo": "trail = [('conclusion', 'inverted index fastest'), ('source', 'JAH-AT92-000003'), ('source', 'JAH-AT93-000001')]\nprint(' <- '.join(f'{k}:{v[:28]}' for k, v in trail))\n"}];
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
var gen={version:'jahdb-archive-tool-memory-provenance-linker-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-memory-provenance-linker-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
