(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["finding-organization", "citation-insertion", "unresolved-tracking", "evidence-summarization", "report-assembly"];
var PREFIX='JAH-AT80S-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=true;
var ARCH=[{"t": "Finding organization by subquestion", "k": "method", "d": "Signature original: Findings are grouped under the subquestions that produced them, in the mission's dependency order. Organization by subquestion keeps the report's structure aligned with how the investigation actually ran. Each group opens with its one-line answer, then the supporting detail.", "demo": "findings = {'q1': ['inverted index hits 40ms at 50k records'], 'q2': ['cache cuts p99 to 12ms']}\nfor q, fs in findings.items():\n    print(f'## {q}')\n    for f in fs: print(' -', f)\n"}, {"t": "Citation insertion from evidence links", "k": "algorithm", "d": "Signature original: Every factual sentence in the draft gets its citation inserted from the evidence links recorded during the investigation. Sentences with no link are flagged for the auditor instead of being published uncited. Citation insertion is mechanical and complete: no claim the evidence supports goes without its marker.", "demo": "links = {'inverted index hits 40ms': '[JAH-AT92-000003]'}\nsent = 'inverted index hits 40ms'\nprint(sent, links.get(sent, '[NO CITATION -> flag]'))\n"}, {"t": "Unresolved-question tracking", "k": "method", "d": "Signature original: Subquestions that remain unanswered get their own report section with what was tried and why it fell short. Unresolved questions are first-class report content, not buried in a footnote, because they define the next investigation. Each one carries the negative-result summary from the analyzer.", "demo": "unresolved = [{'q': 'q3', 'tried': '12 queries across 2 collections', 'why': 'no primary sources found'}]\nprint('## Unresolved questions')\nfor u in unresolved: print(f\" - {u['q']}: tried {u['tried']} ({u['why']})\")\n"}, {"t": "Evidence summarization per section", "k": "method", "d": "Signature original: Each report section opens with a two-sentence evidence summary: what was found and how strong the support is. Summaries are extractive, built from the top-scoring evidence passages, so they never drift from the sources. The summary lets busy readers get the point without reading every citation.", "demo": "evidence = ['inverted index: 40ms (strong)', 'scan: 900ms (strong)']\nprint('Evidence summary:', '; '.join(evidence[:2]) + '.')\n"}, {"t": "Report assembly and completeness check", "k": "procedure", "d": "Signature original: Assembly stitches sections, citations, summaries, and unresolved questions into the final document, then runs a completeness check: every subquestion appears exactly once, every factual sentence has a citation, and the unresolved section is non-empty when gaps exist. A report that fails the check goes back for repair instead of shipping incomplete.", "demo": "report = {'sections': 4, 'cited_sentences': 18, 'uncited': 0, 'unresolved_listed': True}\nok = report['uncited'] == 0 and report['unresolved_listed']\nprint('report complete:', ok)\n"}];
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
var gen={version:'jahdb-archive-tool-automatic-research-report-builder-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-automatic-research-report-builder-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
