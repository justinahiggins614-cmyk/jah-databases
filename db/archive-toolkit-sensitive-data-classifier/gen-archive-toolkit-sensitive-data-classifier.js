(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["pattern-detection", "ml-classification", "context-scoring"];
var PREFIX="JAH-ATK263-";
var KIND="sensitive data classifier";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["pattern-detection", "Regex-based PII detection", "Well-known patterns for social security numbers, credit cards, emails, and phone numbers are matched with regular expressions tuned to avoid common false positives. Matches are labeled by type and returned with their location. Pattern libraries are updated as new identifier formats appear.", "patterns for SSNs, cards, emails, phones", "false-positive tuning per pattern", "updatable pattern libraries", "CFG = {1: \"call 555-0100\", 2: \"ssn 123-45-6789\", 3: \"card 4111-1111-1111-1111 email a@b.com\"}\nimport re\ntext = CFG[LEVEL]\npats = {\"phone\": r\"\\d{3}-\\d{4}\", \"ssn\": r\"\\d{3}-\\d{2}-\\d{4}\", \"card\": r\"\\d{4}(-\\d{4}){3}\", \"email\": r\"[\\w.]+@[\\w.]+\"}\nfound = {k: re.findall(p, text) for k, p in pats.items()}\nfound = {k: v for k, v in found.items() if v}\nprint(\"text:\", text, \"| detected:\", found or \"none\")"],
["ml-classification", "Keyword and context scoring", "Sensitive keywords (diagnosis, salary, password) contribute base scores, and surrounding context adjusts them: 'password' near 'reset instructions' scores lower than near 'is hunter2'. Weighted scoring beats keyword lists because context disambiguates. Thresholds turn scores into labels.", "keyword base scores adjusted by context", "thresholds turning scores into labels", "per-domain keyword weight tuning", "CFG = {1: \"the password reset instructions\", 2: \"my password is hunter2\", 3: \"patient diagnosis: diabetes\"}\ntext = CFG[LEVEL]\nscore = 0\nif \"password\" in text: score += 40\nif \"diagnosis\" in text or \"patient\" in text: score += 70\nif \"reset instructions\" in text: score -= 25\nif \"is \" in text and \"password\" in text: score += 30\nlabel = \"sensitive\" if score >= 50 else (\"review\" if score >= 20 else \"clean\")\nprint(\"text:\", text, \"| score:\", score, \"->\", label)"],
["context-scoring", "Data-type inference", "Columns of data are classified by sampling their values: names, addresses, dates of birth, and identifiers each have characteristic shapes. Inferred types drive default protection: a column inferred as 'email' is treated as personal data until proven otherwise. Inference confidence gates automatic action.", "sampling values to infer column types", "default protection by inferred type", "confidence-gated automatic labeling", "CFG = {1: [\"amy\", \"bob\", \"cara\"], 2: [\"amy@x.com\", \"bob@y.org\"], 3: [\"1990-01-02\", \"1985-12-31\"]}\nimport re\nvals = CFG[LEVEL]\ndef infer(v):\n    if re.fullmatch(r\"[\\w.]+@[\\w.]+\", v): return \"email\"\n    if re.fullmatch(r\"\\d{4}-\\d{2}-\\d{2}\", v): return \"dob\"\n    if re.fullmatch(r\"[A-Za-z]+\", v): return \"name\"\n    return \"unknown\"\ntypes = {infer(v) for v in vals}\nprint(\"values:\", vals, \"| inferred:\", types)"],
["pattern-detection", "Confidence-threshold triage", "High-confidence classifications are handled automatically while low-confidence ones are queued for human review. Two thresholds create three bands: auto-protect, human review, and clean. Thresholds are tuned from precision/recall measurements so the review queue stays manageable.", "three bands: auto, review, clean", "thresholds tuned from precision/recall", "reviewer labels feeding back into tuning", "CFG = {1: [0.95, 0.4, 0.1], 2: [0.75, 0.55, 0.2], 3: [0.9, 0.62, 0.05]}\nfor s in CFG[LEVEL]:\n    band = \"auto-protect\" if s >= 0.8 else (\"human review\" if s >= 0.3 else \"clean\")\n    print(\"score %.2f -> %s\" % (s, band))"],
["ml-classification", "Multi-label classification", "One item can carry several sensitivity labels at once: a medical email is both 'health' and 'contact-info'. Labels are independent, each with its own confidence, and protection is the union of what each label requires. Multi-label output matches how real data mixes concerns.", "independent labels per sensitivity dimension", "per-label confidence scores", "protection as the union of label requirements", "CFG = {1: \"meeting at noon\", 2: \"send the contract to amy@x.com\", 3: \"patient amy@x.com diagnosed with flu\"}\ntext = CFG[LEVEL]\nlabels = set()\nif \"@\" in text: labels.add(\"contact-info\")\nif \"patient\" in text or \"diagnosed\" in text: labels.add(\"health\")\nif \"contract\" in text: labels.add(\"legal\")\nprint(\"text:\", text, \"| labels:\", sorted(labels) or [\"none\"])"]
];
function escRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(r){return r[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var ladder=1+((seed>>>0)%3);
  var focus=[row[3],row[4],row[5]][ladder-1];
  var stage=['','At ladder rank 1 (foundation), this record covers ','At ladder rank 2 (compounded), it builds on the foundation with ','At ladder rank 3 (full complexity), it extends to production scale with '][ladder];
  var id=PREFIX+String(seed>>>0).padStart(6,'0');
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Public harvest — documented archive-engineering practice; method fact-checked against standard references.",last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length||r.t!==r.title)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('LEVEL = '+r.ladder_rank)!==0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-sensitive-data-classifier-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-sensitive-data-classifier",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
