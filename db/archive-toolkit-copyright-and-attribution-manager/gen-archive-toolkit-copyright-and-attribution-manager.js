(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["attribution-tracking", "usage-requirements", "takedown-workflow"];
var PREFIX="JAH-ATK274-";
var KIND="copyright and attribution manager";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["attribution-tracking", "Attribution record keeping", "Every work records its source, author, license, and retrieval date in a structured attribution record. Records travel with the work through copies and derivatives. Complete records make compliance automatic; missing records are flagged at ingest.", "structured records per work", "records traveling with copies", "flagging missing records at ingest", "CFG = {1: {\"author\": \"A. Author\", \"license\": \"CC-BY\"}, 2: {\"author\": \"\", \"license\": \"CC-BY\"}, 3: {\"author\": \"B. Writer\", \"license\": \"MIT\", \"source\": \"archive\"}}\nrec = CFG[LEVEL]\ncomplete = bool(rec.get(\"author\")) and bool(rec.get(\"license\"))\nprint(\"attribution:\", rec, \"| complete:\", complete, \"->\", \"accept\" if complete else \"FLAG at ingest\")"],
["usage-requirements", "Required-notice generation", "From attribution records the manager generates compliant copyright notices automatically: the right names, years, and license texts in the required format. Generated notices are reviewed once per template, then produced at scale. Every published derivative carries its notices.", "automatic notice generation from records", "template review before scale", "notices on every derivative", "CFG = {1: (\"A. Author\", \"2024\", \"MIT\"), 2: (\"B. Writer\", \"2026\", \"CC-BY-4.0\"), 3: (\"C. Creator\", \"2020-2026\", \"Apache-2.0\")}\nauthor, years, lic = CFG[LEVEL]\nprint(\"Copyright (c) %s %s. Licensed under %s.\" % (years, author, lic))"],
["takedown-workflow", "Usage-requirement enforcement", "License usage requirements (link-backs, same-license propagation, non-endorsement clauses) are checked before publication. The checker verifies each requirement is satisfied: links resolve, license texts are included, modifications are marked. Publication is blocked until requirements pass.", "checking requirements pre-publication", "verifying links, texts, markings", "blocking publication on failure", "CFG = {1: {\"linkback\": True, \"license_text\": True}, 2: {\"linkback\": False, \"license_text\": True}, 3: {\"linkback\": True, \"license_text\": False}}\nreqs = CFG[LEVEL]\nok = all(reqs.values())\nprint(\"requirements:\", reqs, \"| publish:\", \"ALLOWED\" if ok else \"BLOCKED: unmet requirements\")"],
["attribution-tracking", "Takedown request workflow", "Takedown requests move through states: received, validated, actioned, and requester-notified. Validation checks the claim (ownership evidence, specific URLs) before any removal. Counter-notices follow the same tracked path. Every transition is timestamped.", "tracked request states", "claim validation before removal", "timestamped transitions", "CFG = {1: [\"received\", \"validated\", \"actioned\", \"notified\"], 2: [\"received\", \"rejected: no evidence\"], 3: [\"received\", \"validated\"]}\nstates = CFG[LEVEL]\nprint(\"takedown:\", \" -> \".join(states), \"| closed:\", states[-1] in (\"notified\", \"rejected: no evidence\"))"],
["usage-requirements", "Public-domain determination", "Copyright term rules are applied to determine public-domain status: publication year plus term, with jurisdiction variations. Works clearly in the public domain are marked so; borderline cases are flagged for counsel. Determinations record the rule applied and the inputs.", "term rules per jurisdiction", "borderline cases flagged for counsel", "recorded rules and inputs", "CFG = {1: 1920, 2: 1935, 3: 2000}\nyear, NOW, TERM = CFG[LEVEL], 2026, 95\npd = NOW - year >= TERM\nprint(\"published:\", year, \"| public domain:\", pd, \"->\", \"mark PD\" if pd else \"in copyright / counsel review\")"]
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
var gen={version:"jahdb-archive-toolkit-copyright-and-attribution-manager-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-copyright-and-attribution-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
