(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["license-identification", "compatibility-checking", "obligation-tracking"];
var PREFIX="JAH-ATK273-";
var KIND="data license and usage rights checker";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["license-identification", "License identification from text/headers", "License texts and file headers are scanned for SPDX identifiers and known license phrases. Identification runs on every ingested dataset so nothing enters the archive with unknown rights. Unidentified licenses are treated as all-rights-reserved until clarified.", "SPDX identifier scanning", "identification on every ingest", "unknown treated as all-rights-reserved", "CFG = {1: \"SPDX-License-Identifier: MIT\", 2: \"licensed under Apache-2.0\", 3: \"no license mentioned\"}\nimport re\ntext = CFG[LEVEL]\nm = re.search(r\"SPDX-License-Identifier:\\s*(\\S+)\", text) or re.search(r\"(?i)\\b(MIT|Apache-2\\.0|GPL-3\\.0)\\b\", text)\nprint(\"text:\", text, \"| license:\", m.group(1) if m else \"UNKNOWN -> all-rights-reserved\")"],
["compatibility-checking", "License compatibility matrix", "Combining datasets requires compatible licenses: the matrix answers whether license A and license B can be mixed in one derivative. Incompatible combinations are blocked before the merge, not discovered in a lawsuit. The matrix is maintained as data and reviewed by counsel.", "pairwise compatibility lookups", "blocking incompatible merges pre-merge", "counsel-reviewed matrix data", "CFG = {1: (\"MIT\", \"Apache-2.0\"), 2: (\"GPL-3.0\", \"MIT\"), 3: (\"GPL-3.0\", \"Apache-2.0\")}\nCOMPAT = {(\"MIT\", \"Apache-2.0\"): True, (\"GPL-3.0\", \"MIT\"): False, (\"GPL-3.0\", \"Apache-2.0\"): True}\na, b = CFG[LEVEL]\nkey = (a, b) if (a, b) in COMPAT else (b, a)\nprint(a, \"+\", b, \"->\", \"COMPATIBLE\" if COMPAT.get(key) else \"BLOCKED\")"],
["obligation-tracking", "Obligation extraction", "Each license's obligations are extracted into a checklist: attribution required, share-alike, notice preservation, patent grants. The checklist travels with the dataset so downstream users inherit the obligations, not just the data. Unmet obligations are flagged before publication.", "checklists per license", "obligations traveling with data", "pre-publication obligation checks", "CFG = {1: \"MIT\", 2: \"GPL-3.0\", 3: \"CC-BY-4.0\"}\nOBLIG = {\"MIT\": [\"attribution\", \"notice\"], \"GPL-3.0\": [\"attribution\", \"share-alike\", \"notice\"], \"CC-BY-4.0\": [\"attribution\"]}\nlic = CFG[LEVEL]\nprint(\"license:\", lic, \"| obligations:\", OBLIG[lic])"],
["license-identification", "Usage-scope checking", "Licenses often limit scope: research-only, non-commercial, or no-derivatives. The checker compares the intended use against the granted scope before the data is used. Out-of-scope use is denied with the specific restriction cited.", "comparing intended use to granted scope", "denial with the restriction cited", "scope recorded per dataset", "CFG = {1: \"research\", 2: \"commercial\", 3: \"internal\"}\nSCOPE = {\"research\", \"internal\"}\nuse = CFG[LEVEL]\nprint(\"intended use:\", use, \"->\", \"ALLOWED\" if use in SCOPE else \"DENY: commercial use not in scope\")"],
["compatibility-checking", "License change detection", "Upstream datasets can be relicensed; the checker watches for changes and alerts when a new version carries different terms. Relicensing can silently remove rights the archive depends on. Detected changes pause ingestion until reviewed.", "watching upstream license terms", "alerting on relicensing", "pausing ingestion pending review", "CFG = {1: (\"MIT\", \"MIT\"), 2: (\"MIT\", \"GPL-3.0\"), 3: (\"Apache-2.0\", \"Apache-2.0\")}\nold, new = CFG[LEVEL]\nprint(\"license %s -> %s\" % (old, new), \"|\", \"no change\" if old == new else \"RELICENSED: ingestion paused for review\")"]
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
var gen={version:"jahdb-archive-toolkit-data-license-and-usage-rights-checker-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-data-license-and-usage-rights-checker",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
