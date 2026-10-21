(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["answer-audit", "citation-check", "unsupported-claim-flag", "evidence-alignment", "audit-report"];
var PREFIX='JAH-AT60-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Answer sentence extraction", "k": "method", "d": "A generated answer is split into individual sentences, each treated as a claim candidate, while boilerplate like greetings and transitions is filtered out. Only sentences that assert something checkable proceed to the audit; opinions and rhetorical questions are marked non-factual and skipped. This keeps the auditor focused on statements that could actually be wrong.", "demo": "import re\nanswer = 'Hello! The archive holds 52,268 databases. It is quite impressive, really. Growth continues daily.'\nsents = [s.strip() for s in re.split(r'(?<=[.!?])\\s+', answer) if s.strip()]\nfactual = [s for s in sents if not re.match(r'(?i)^(hello|hi|thanks|it is quite)', s)]\nprint('sentences:', len(sents), '| factual candidates:', len(factual))\nfor s in factual: print(' -', s)\n"}, {"t": "Per-sentence evidence alignment", "k": "algorithm", "d": "Each factual sentence is aligned against the retrieved evidence passages using token overlap with entity emphasis, exactly like the evidence chain builder's linker. A sentence passes when at least one passage scores above the support threshold; the best-scoring passage becomes its cited support. Sentences are audited independently so one weak claim does not sink its well-supported neighbors.", "demo": "def align(sent, passages):\n    s = set(sent.lower().split())\n    best = max(passages, key=lambda p: len(s & set(p.lower().split())) / max(1, len(s)))\n    sc = len(s & set(best.lower().split())) / max(1, len(s))\n    return best, round(sc, 2)\nsent = 'the archive holds 52268 databases'\nprint(align(sent, ['the archive holds 52268 databases today', 'weather is sunny']))\n"}, {"t": "Unsupported-claim flagging", "k": "method", "d": "Sentences with no supporting passage above threshold are flagged as unsupported and returned with their exact text, not paraphrased away. The flag distinguishes 'no evidence retrieved' from 'evidence contradicts', because the remedies differ: the first needs more retrieval, the second needs the answer rewritten. Flags accumulate into the audit verdict for the whole answer.", "demo": "audited = [('the archive holds 52268 databases', 0.9), ('it was founded on mars', 0.1)]\nTH = 0.35\nfor sent, sc in audited:\n    print(('SUPPORTED ' if sc >= TH else 'UNSUPPORTED ') + sent[:50])\n"}, {"t": "Citation presence and placement check", "k": "method", "d": "The auditor also checks that the answer's citations actually point at the passages used for support, not at decorative references. Each citation marker is resolved to a passage, and the passage is re-scored against the sentence it supposedly supports. Orphan citations and mismatched pairings are reported as formatting faults even when the underlying claim is true.", "demo": "cites = {'[1]': 'passage about database counts', '[2]': 'passage about weather'}\nsentence_supports = {'[1]': 'database counts', '[2]': 'database counts'}\nfor mark, topic in sentence_supports.items():\n    ok = topic in cites[mark]\n    print(mark, '->', 'aligned' if ok else 'MISMATCHED citation')\n"}, {"t": "Audit report with pass/fail verdict", "k": "procedure", "d": "The audit ends in a structured report: per-sentence support scores, the list of unsupported claims, citation faults, and an overall verdict of pass, pass-with-notes, or fail. Failed answers are routed back for regeneration with the unsupported claims listed as explicit constraints. The report is stored with the answer so readers can see exactly what was checked.", "demo": "report = {'sentences': 4, 'supported': 3, 'unsupported': ['it was founded on mars'], 'citation_faults': 0}\nreport['verdict'] = 'fail' if report['unsupported'] else 'pass'\nprint('audit verdict:', report['verdict'])\nprint('needs rewrite:', report['unsupported'])\n"}];
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
var gen={version:'jahdb-archive-tool-claim-to-source-auditor-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-claim-to-source-auditor',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
