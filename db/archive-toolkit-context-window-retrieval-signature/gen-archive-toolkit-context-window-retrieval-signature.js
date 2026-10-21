(function(){'use strict';
var PREFIX="JAH-ATK204S-";
var METHODS=[["Sentence-window expansion", "Add N sentences before and after each hit so pronouns and references resolve inside the window."], ["Section-scoped windows", "Expand to the enclosing section boundaries rather than a fixed count, keeping the window semantically whole."], ["Token-budget windows", "Grow the window until a token budget is exhausted, balancing fidelity against downstream model costs."], ["Antecedent resolution", "Preferentially include the sentence that introduces a pronoun's antecedent when the passage opens with 'it' or 'they'."], ["Qualifier capture", "Extend the window to include negations and qualifiers ('except', 'however') adjacent to the passage so claims are not overstated."], ["Heading breadcrumb inclusion", "Always prepend the heading path to the window so the passage carries its document position."], ["Overlap merging", "Merge overlapping windows from adjacent hits into one window instead of returning the same text twice."], ["Window quality scoring", "Score candidate windows by information density and trim low-signal sentences from the edges."], ["Citation-stable windows", "Freeze window boundaries at retrieval time and store them with the citation so later edits do not silently shift meaning."], ["Adaptive window sizing", "Size windows by document type: small for reference tables, large for narrative prose where meaning builds slowly."], ["Cross-reference windows", "When a passage cites a figure or table, pull the referenced object into the window automatically."], ["Multi-passage window packing", "Pack several small windows into one response under a shared budget, ordered by relevance."], ["Window diffing over versions", "When the document changes, recompute windows and flag passages whose surrounding context changed meaning."], ["Reader-position windows", "Bias the window toward what the reader has already seen in the session to avoid repeating context."], ["Compression fallback", "If the window still overflows the budget, compress the far edges into a one-line summary while keeping the core verbatim."]];
var CATS=["passages", "context", "fidelity"];
var DEMO="# Context-Window Retrieval demo: sentence windows around hits, overlap-merged.\nimport re\nDOC=(\"Sails catch photons. It is a tiny push. Over months it adds up. \"\n     \"Mylar is cheap. However, mylar tears easily. Kapton survives heat better. \"\n     \"Engineers prefer kapton for long missions.\")\nSENTS=[s.strip() for s in re.split(r\"\\. \",DOC)]\ndef window(hits,radius=1):\n    idx=sorted(set(hits)); merged=[]; start=idx[0]-radius; prev=idx[0]\n    for h in idx[1:]:\n        if h-radius<=prev+radius: prev=h; continue\n        merged.append((max(0,start),prev+radius)); start=h-radius; prev=h\n    merged.append((max(0,start),prev+radius))\n    return [\". \".join(SENTS[a:b+1]) for a,b in merged]\nhits=[i for i,s in enumerate(SENTS) if \"kapton\" in s.lower() or \"mylar\" in s.lower()]\nprint(window(hits))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Context-Window Retrieval (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. Context-window retrieval recognizes that a passage alone can mislead: pronouns lose their antecedents, numbers lose their units, and claims lose their qualifiers outside their neighborhood. The tool wraps each retrieved passage in a controlled window of surrounding text \u2014 sentences before and after, the enclosing section, or a fixed token budget \u2014 so the consumer interprets the evidence the way it",
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
var gen={version:"jahdb-archive-toolkit-context-window-retrieval-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-context-window-retrieval-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();