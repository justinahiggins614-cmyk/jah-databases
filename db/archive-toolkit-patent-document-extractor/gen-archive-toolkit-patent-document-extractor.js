(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK150-";
var KIND="extraction method";
var TOOLNAME="Patent Document Extractor";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Claim parsing", "d": "Claims are numbered sentences defining legal scope; parsers split and number them. Claims are the patent's heart. Scope is everything.", "c": "fundamentals", "r": 1, "p": {"PATENT": "Claims\\n1. A widget comprising A and B.\\n2. The widget of claim 1, further comprising C.\\nInventors\\nAmy Lee\\nClassifications\\nG06F 17/30", "SNIP": "50"}}, {"t": "Independent vs dependent", "d": "Independent claims stand alone; dependent claims reference and narrow another. The distinction shapes scope analysis. Hierarchy matters.", "c": "algorithms", "r": 1, "p": {"PATENT": "Claims\\n1. A device with X.\\n2. The device of claim 1 with Y.\\n3. A method of making X.", "SNIP": "50"}}, {"t": "Preamble extraction", "d": "Preambles ('A widget comprising') set context before limitations. Parsing separates preamble from body. Context frames.", "c": "implementation", "r": 1, "p": {"PATENT": "Claims\\n1. A widget comprising gears.\\nInventors\\nBob", "SNIP": "50"}}, {"t": "Classification codes", "d": "IPC/CPC codes classify the invention's technical field. Codes enable prior-art search. Classes organize.", "c": "optimization", "r": 1, "p": {"PATENT": "Classifications\\nG06F 17/30\\nH04L 9/00\\nClaims\\n1. A system.", "SNIP": "50"}}, {"t": "Inventor extraction", "d": "Inventor names and addresses parse from the patent front page, where they appear in standardized inventor fields. Extracted inventors link patents to people across filings, enabling inventor-centric search and collaboration graphs. Accurate inventor data underpins prior-art and assignment analysis.", "c": "evaluation", "r": 1, "p": {"PATENT": "Inventors\\nAmy Lee\\nBob Ray\\nClaims\\n1. A thing.", "SNIP": "50"}}, {"t": "Citation extraction", "d": "Cited patents and papers parse into prior-art lists that map the technical landscape around an invention. Extractors split reference sections into individual citations with numbers, dates, and classifications. Citation graphs reveal which earlier work constrains a patent's scope.", "c": "fundamentals", "r": 2, "p": {"PATENT": "Citations\\nUS1234567\\nClaims\\n1. Novel widget.", "SNIP": "50"}}, {"t": "Description sections", "d": "Background, summary, and detailed description segment the specification. Sections support different analyses. Structure aids.", "c": "algorithms", "r": 2, "p": {"PATENT": "Claims\\n1. A widget.\\nDescription\\nWidgets are useful.", "SNIP": "50"}}, {"t": "Figure references", "d": "'FIG. 1' mentions in the description link claim language to the patent's drawings, grounding abstract limitations in concrete visuals. Extractors map every figure reference to its drawing sheet so readers can follow along. Linked figures make dense specifications navigable.", "c": "implementation", "r": 2, "p": {"PATENT": "Claims\\n1. The widget of FIG. 1.\\nInventors\\nAl", "SNIP": "50"}}, {"t": "Priority claims", "d": "Priority data links continuations to parent filings. Chains establish effective dates. Dates decide.", "c": "optimization", "r": 2, "p": {"PATENT": "Claims\\n1. A widget.\\nPriority\\nUS 60/000,001", "SNIP": "50"}}, {"t": "Legal status", "d": "Status (pending, granted, expired) extracts from registers. Status determines enforceability. Status matters.", "c": "evaluation", "r": 2, "p": {"PATENT": "Claims\\n1. A widget.\\nStatus\\nGranted", "SNIP": "50"}}, {"t": "Claim charting", "d": "Charts map claim limitations to accused products. Charting structures infringement analysis. Maps argue.", "c": "fundamentals", "r": 3, "p": {"PATENT": "Claims\\n1. A widget with A.\\n2. The widget of claim 1 with B.", "SNIP": "50"}}, {"t": "Family grouping", "d": "Families group filings sharing priority across countries. Grouping shows global coverage. Families spread.", "c": "algorithms", "r": 3, "p": {"PATENT": "Claims\\n1. A widget.\\nFamily\\nUS, EP, JP", "SNIP": "50"}}, {"t": "OCR of scanned patents", "d": "Old patents exist only as scanned images, so OCR must convert them to text before any extraction can run. Pipelines tuned for patent typography handle column layouts, figure labels, and chemical formulas better than generic OCR. Digitizing the backfile brings a century of prior art into searchable form.", "c": "implementation", "r": 3, "p": {"PATENT": "Claims\\n1. An old widget.", "SNIP": "50"}}, {"t": "Bulk-format parsing", "d": "Patent offices publish bulk XML and JSON dumps, and parsers must stream through millions of documents without loading them whole. Streaming readers emit one patent record at a time for downstream extraction. Bulk parsing is how patent analytics keeps up with weekly publication.", "c": "optimization", "r": 3, "p": {"PATENT": "Claims\\n1. A widget.\\n2. Another.", "SNIP": "50"}}, {"t": "Evaluation on labeled patents", "d": "Labeled patent sets with hand-checked claims, inventors, and classifications score extraction quality field by field. Benchmarks separate reliable extractors from optimistic demos and guide tuning. Measured quality is what makes extraction trustworthy for legal work.", "c": "evaluation", "r": 3, "p": {"PATENT": "Claims\\n1. A widget.\\nInventors\\nZed", "SNIP": "50"}}];
var DEMO="# Patent extraction: parse claims (independent vs dependent), classifications, inventors.\ntext = \"\"\"%%PATENT%%\"\"\".replace(\"\\\\n\", \"\\n\")\nimport re\nclaims, inventors, classes = [], [], []\nsec = None\nfor line in text.splitlines():\n    s = line.strip()\n    if s.lower().startswith(\"claims\"): sec = \"claims\"; continue\n    if s.lower().startswith(\"inventors\"): sec = \"inv\"; continue\n    if s.lower().startswith(\"classifications\"): sec = \"cls\"; continue\n    m = re.match(r\"^(\\d+)\\.\\s*(.*)\", s)\n    if sec == \"claims\" and m:\n        n, body = int(m.group(1)), m.group(2)\n        dep = re.search(r\"claim (\\d+)\", body, re.I)\n        claims.append({\"n\": n, \"independent\": not dep, \"depends_on\": int(dep.group(1)) if dep else None, \"text\": body[:%%SNIP%%]})\n    elif sec == \"inv\" and s: inventors.append(s)\n    elif sec == \"cls\" and s: classes.append(s)\nprint(f\"claims: {len(claims)} ({sum(1 for c in claims if c['independent'])} independent)\")\nfor c in claims:\n    print(f\"  claim {c['n']}: independent={c['independent']} depends_on={c['depends_on']} :: {c['text']}\")\nprint(\"inventors:\", inventors)\nprint(\"classifications:\", classes)\n";
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
  if(!new RegExp("^JAH\\-ATK150\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-patent-document-extractor-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-patent-document-extractor",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
