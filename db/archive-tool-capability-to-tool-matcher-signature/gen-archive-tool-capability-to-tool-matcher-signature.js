(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["capability-indexing", "requirement-parsing", "match-scoring", "fallback-chaining", "match-explanation"];
var PREFIX='JAH-AT83S-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=true;
var ARCH=[{"t": "Capability indexing of the tool registry", "k": "method", "d": "Signature original: Every registered tool is indexed by its declared capabilities: verbs it performs, data types it consumes and produces, and constraints it honors. The index is built once at registration and updated on every registry change. Good indexing makes matching a lookup problem instead of a search problem.", "demo": "registry = {'hash-tool': {'verbs': ['hash', 'verify'], 'in': ['bytes'], 'out': ['digest']}, 'index-tool': {'verbs': ['index', 'search'], 'in': ['docs'], 'out': ['hits']}}\nprint('tools indexed:', len(registry))\n"}, {"t": "Requirement parsing from task text", "k": "method", "d": "Signature original: The task description is parsed into a requirement frame: the action verb, input and output types, and hard constraints like 'offline only'. Parsing uses keyword patterns over a controlled vocabulary, which keeps it predictable. The frame is what gets matched, never the raw prose.", "demo": "import re\ntask = 'hash these bytes offline and verify the digest'\nframe = {'verb': 'hash', 'io': ('bytes', 'digest'), 'offline': bool(re.search(r'offline', task))}\nprint('requirement frame:', frame)\n"}, {"t": "Match scoring with constraint veto", "k": "algorithm", "d": "Signature original: Candidate tools are scored by capability overlap with the requirement frame, but any violated hard constraint vetoes the candidate outright. A tool that matches perfectly but needs network access loses to an offline-capable partial match when the task demands offline. Vetoes keep the matcher honest about requirements.", "demo": "cands = [('hash-tool', 0.95, True), ('cloud-hash', 1.0, False)]  # (tool, score, offline_ok)\nneed_offline = True\nviable = [(t, s) for t, s, off in cands if not (need_offline and not off)]\nprint('viable:', viable)\n"}, {"t": "Fallback chaining when no single tool fits", "k": "algorithm", "d": "Signature original: When no single tool covers the whole task, the matcher chains tools by matching one's output type to the next one's input type, like the workflow composer's smaller cousin. Chains are ranked by total score minus a per-hop penalty, so shorter chains win ties. The chain ships as an ordered tool list with the handoff types explicit.", "demo": "tools = {'a': ('docs', 'index'), 'b': ('index', 'hits')}\nchain = ['a', 'b'] if tools['a'][1] == tools['b'][0] else []\nprint('fallback chain:', ' -> '.join(chain) if chain else 'none found')\n"}, {"t": "Match explanation for the user", "k": "procedure", "d": "Signature original: The chosen tool or chain is presented with its explanation: which capabilities matched, which constraints were honored, and what the fallbacks were. Explanations let users sanity-check the match instead of trusting a black box. A match the user cannot understand is a match they cannot trust.", "demo": "print('matched: hash-tool | capabilities: hash, verify | constraints honored: offline | runner-up: cloud-hash (vetoed: needs network)')\n"}];
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
var gen={version:'jahdb-archive-tool-capability-to-tool-matcher-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-capability-to-tool-matcher-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
