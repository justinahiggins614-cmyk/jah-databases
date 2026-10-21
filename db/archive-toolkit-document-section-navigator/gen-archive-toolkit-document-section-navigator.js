(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK123-";
var KIND="traversal method";
var TOOLNAME="Document Section Navigator";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Heading-tree parsing", "d": "Headings nest by level: H2 sections contain H3 subsections, forming a document tree. Parsers maintain a stack, popping until the parent level fits each new heading. The tree is what 'jump to section' navigates.", "c": "fundamentals", "r": 1, "p": {"TARGET": "Methods", "DOC": "# Report\\nIntro text\\n## Methods\\nWe measured twice.\\n## Results\\nIt worked."}}, {"t": "Table-of-contents generation", "d": "Walking the heading tree emits a nested TOC with anchor links. Depth limits keep TOCs readable on deep documents. Generated TOCs stay in sync with the document automatically.", "c": "algorithms", "r": 1, "p": {"TARGET": "Results", "DOC": "# Guide\\n## Install\\nSteps here.\\n## Usage\\nUse it well."}}, {"t": "Section addressing", "d": "Sections get stable addresses: heading slugs, numbered paths (2.3.1), or page numbers. Addresses survive re-rendering when derived from content, not position. Stable addresses enable deep linking.", "c": "implementation", "r": 1, "p": {"TARGET": "Install", "DOC": "# Manual\\n## Install\\nRun setup.\\n## Config\\nEdit file."}}, {"t": "Page-number mapping", "d": "Print-oriented documents map sections to page numbers via layout passes. Two-pass rendering resolves forward references like 'see page 12'. Page maps bridge digital navigation and print citation.", "c": "optimization", "r": 1, "p": {"TARGET": "Config", "DOC": "# Manual\\n## Install\\nRun setup.\\n## Config\\nEdit file."}}, {"t": "Skipping levels gracefully", "d": "Real documents skip heading levels; parsers attach H4 under the nearest H2 without complaint. Graceful handling keeps navigation working on messy real-world files. Strict parsers break on the documents users actually have.", "c": "evaluation", "r": 1, "p": {"TARGET": "Deep", "DOC": "# Doc\\n#### Deep\\nBuried content."}}, {"t": "Section-aware search", "d": "Search scopes to a section subtree, answering 'find X in the Methods'. Scoping intersects the heading path with term matches. Section scope raises precision on long documents.", "c": "fundamentals", "r": 2, "p": {"TARGET": "Methods", "DOC": "# Paper\\n## Methods\\nWe used surveys.\\n## Appendix\\nSurvey form."}}, {"t": "Extracting section bodies", "d": "Body extraction collects all content under a heading until the next same-or-higher heading. It powers 'give me just section 3' summarization inputs. Clean extraction needs the heading tree, not regex.", "c": "algorithms", "r": 2, "p": {"TARGET": "Results", "DOC": "# Study\\n## Methods\\nDid things.\\n## Results\\nFound things.\\nMore findings."}}, {"t": "Cross-references", "d": "'See Section 4' links resolve through the heading index to target anchors. Resolvers handle renumbered sections by matching titles fuzzily. Working cross-references make long documents navigable.", "c": "implementation", "r": 2, "p": {"TARGET": "Usage", "DOC": "# Guide\\n## Install\\nSee Usage.\\n## Usage\\nRun it."}}, {"t": "Chunking for retrieval", "d": "RAG pipelines chunk documents at section boundaries instead of fixed sizes. Section chunks preserve topical coherence for embedding. Better chunks mean better retrieval.", "c": "optimization", "r": 2, "p": {"TARGET": "Intro", "DOC": "# Book\\n## Intro\\nWelcome.\\n## Chapter 1\\nBegin."}}, {"t": "Collapsible outlines", "d": "UIs render the heading tree as collapsible nodes, expanding on demand. Lazy expansion keeps thousand-section documents responsive. Outlines are the primary navigation for long reads.", "c": "evaluation", "r": 2, "p": {"TARGET": "Chapter 1", "DOC": "# Book\\n## Intro\\nHi.\\n## Chapter 1\\nGo."}}, {"t": "Numbered section paths", "d": "Numbering (1, 1.2, 1.2.3) gives each section a hierarchical address. Numbers derive from tree position, updating as structure changes. Numbered paths suit formal documents.", "c": "fundamentals", "r": 3, "p": {"TARGET": "Details", "DOC": "# Spec\\n## Overview\\nHigh level.\\n### Details\\nLow level."}}, {"t": "Landmark navigation", "d": "Landmarks (abstract, references, appendix) get special handling as known section roles. Role detection uses title patterns per document type. Landmarks speed scholarly navigation.", "c": "algorithms", "r": 3, "p": {"TARGET": "Abstract", "DOC": "# Paper\\n## Abstract\\nWe show X.\\n## References\\n[1] Y."}}, {"t": "Multi-document section merge", "d": "Merging reports aligns same-titled sections across documents. Alignment enables side-by-side comparison of methods sections. Merged views serve literature reviews.", "c": "implementation", "r": 3, "p": {"TARGET": "Methods", "DOC": "# A\\n## Methods\\nSurvey.\\n# B\\n## Methods\\nInterviews."}}, {"t": "Accessibility of navigation", "d": "Screen readers use heading levels for document navigation; proper hierarchy is an accessibility requirement. Skipped or fake headings (bold text) break navigation. Semantic headings serve every reader.", "c": "optimization", "r": 3, "p": {"TARGET": "Usage", "DOC": "# Help\\n## Install\\nStep 1.\\n## Usage\\nStep 2."}}, {"t": "Navigation state persistence", "d": "Reading positions (section + scroll offset) persist across sessions. Restoring state returns readers to their exact spot. Persistence respects that long documents are read over days.", "c": "evaluation", "r": 3, "p": {"TARGET": "Install", "DOC": "# Long Manual\\n## Install\\nDo this.\\n## Usage\\nThen that."}}];
var DEMO="# Section navigation: parse markdown-style headings into a tree, jump to a section.\ndoc = \"\"\"%%DOC%%\"\"\".replace(\"\\\\n\", \"\\n\")\ndef parse(lines):\n    root = {\"title\": \"ROOT\", \"level\": 0, \"children\": [], \"body\": []}\n    stack = [root]\n    for line in lines:\n        if line.startswith(\"#\"):\n            level = len(line) - len(line.lstrip(\"#\"))\n            node = {\"title\": line.strip(\"# \").strip(), \"level\": level, \"children\": [], \"body\": []}\n            while stack[-1][\"level\"] >= level: stack.pop()\n            stack[-1][\"children\"].append(node); stack.append(node)\n        else:\n            stack[-1][\"body\"].append(line)\n    return root\ndef find(node, title):\n    if node[\"title\"].lower() == title.lower(): return node\n    for c in node[\"children\"]:\n        r = find(c, title)\n        if r: return r\n    return None\ndef outline(node, depth=0):\n    for c in node[\"children\"]:\n        print(\"  \"*depth + \"- \" + c[\"title\"]); outline(c, depth+1)\nroot = parse(doc.splitlines())\nprint(\"Outline:\"); outline(root)\ntarget = \"%%TARGET%%\"\nnode = find(root, target)\nprint(f\"\\nJump to '{target}':\")\nprint(\"\\n\".join(node[\"body\"]).strip() if node else \"not found\")\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK123\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-document-section-navigator-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-document-section-navigator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
