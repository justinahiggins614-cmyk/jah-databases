(function(){'use strict';
var PREFIX="JAH-ATK203S-";
var METHODS=[["Document segmentation", "Split documents into overlapping passages (sentences or paragraphs) so no claim is ever cut in half at a boundary."], ["Passage scoring", "Rank passages against the query with BM25 or embedding similarity and keep the score for later auditing."], ["Offset-stable citations", "Record byte or token offsets per passage so citations remain valid even when the document gains new sections."], ["Heading inheritance", "Attach each passage to its section heading path so a retrieved paragraph never loses its structural context."], ["Passage deduplication", "Drop near-duplicate passages from different documents before ranking so the top results are not five copies of one paragraph."], ["Query-focused expansion", "Expand the query with synonyms before scoring passages to catch passages that answer without using the query words."], ["Passage length normalization", "Score passages with length normalization so a 2000-word section does not always outrank a sharp 60-word answer."], ["Answer-span highlighting", "Within the winning passage, highlight the exact span that answers the query for quick human verification."], ["Cross-document passage join", "Link passages from different documents that answer different parts of a multi-part question and present them together."], ["Passage freshness filter", "Down-rank passages from superseded document versions so citations point at current text."], ["Negative passage filtering", "Suppress passages that match the query but contradict it, using contradiction detection on the passage text."], ["Passage clustering", "Group retrieved passages by subtopic so the caller sees one representative per angle instead of a flat list."], ["Citation chains", "When a passage cites another document, follow the chain and return both so the evidence trail is complete."], ["Passage-level access control", "Enforce field-level policy at passage granularity so one restricted paragraph does not block the whole document."], ["Streaming passage delivery", "Stream passages as they score above threshold instead of waiting for the full ranking to complete."]];
var CATS=["passages", "scoring", "citations"];
var DEMO="# Passage-Level Retrieval demo: segment, score with BM25-lite, cite with offsets.\nimport math, re\nDOC=\"\"\"# Solar Sails\nSails catch photons. A large reflective sail can push a probe.\n## Materials\nMylar is cheap but tears. Kapton survives heat better.\n## Propulsion\nPhoton pressure is tiny but constant. Over months it adds up.\"\"\"\ndef passages(doc):\n    out=[]; pos=0\n    for p in re.split(r\"\\n\\n+\",doc):\n        p=p.strip()\n        if p: out.append({\"text\":p,\"start\":doc.index(p,pos)}); pos=doc.index(p,pos)+len(p)\n    return out\ndef score(q,p):\n    qt=q.lower().split(); pt=p[\"text\"].lower()\n    return sum(pt.count(t)*(1.0/(1+pt.count(t))) for t in qt)\nq=\"which material survives heat\"\nranked=sorted(passages(DOC),key=lambda p:-score(q,p))\nfor p in ranked[:2]:\n    print(\"score=%.3f offset=%d text=%r\"%(score(q,p),p[\"start\"],p[\"text\"][:60]))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Passage-Level Retrieval (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. Passage-level retrieval treats long documents as addressable sections and returns only the passages that answer the question, with enough surrounding signal to stay honest. It is the foundation of grounded question answering: instead of handing an AI a whole book and hoping it cites correctly, the system retrieves the exact paragraphs, each stamped with document, section, and offsets. Core machine",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-passage-level-retrieval-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-passage-level-retrieval-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();