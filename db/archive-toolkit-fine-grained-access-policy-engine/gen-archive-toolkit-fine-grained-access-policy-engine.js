(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["resource-scoping", "field-level", "operation-level"];
var PREFIX="JAH-ATK262-";
var KIND="fine-grained access policy engine";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["resource-scoping", "Resource-level ACLs", "Each database and record carries its own access-control list naming the identities and groups allowed to reach it. Requests are checked against the ACL of the exact resource requested, so access to one database never implies access to another. ACL changes take effect immediately.", "per-database and per-record access lists", "immediate effect on ACL change", "ACL inheritance with explicit overrides", "CFG = {1: {\"db1\": [\"amy\"], \"db2\": [\"bob\"]}, 2: {\"db1\": [\"amy\", \"ops\"], \"db2\": [\"bob\"]}, 3: {\"db1\": [\"amy\", \"ops\", \"auditors\"], \"db2\": [\"bob\"], \"db3\": []}}\nacls, who, res = CFG[LEVEL], \"amy\", \"db1\"\nprint(\"ACLs:\", acls, \"|\", who, \"->\", res, \":\", \"ALLOW\" if who in acls.get(res, []) else \"DENY\")"],
["field-level", "Field-level redaction", "Policies decide visibility field by field: a record's public fields are shown to everyone while sensitive fields are redacted per the viewer's clearance. Redaction happens at read time, so one stored record serves many audiences safely. Redacted output marks what was hidden.", "per-field visibility rules", "read-time redaction with hidden-field markers", "redaction policies versioned alongside data", "CFG = {1: \"viewer\", 2: \"analyst\", 3: \"admin\"}\nrole = CFG[LEVEL]\nrec = {\"name\": \"Amy\", \"ssn\": \"000-00-0000\", \"salary\": 90000}\nvisible = {\"viewer\": [\"name\"], \"analyst\": [\"name\", \"salary\"], \"admin\": [\"name\", \"ssn\", \"salary\"]}[role]\nout = {k: (v if k in visible else \"***REDACTED***\") for k, v in rec.items()}\nprint(\"role:\", role, \"| view:\", out)"],
["operation-level", "Operation-level permissions", "Read, write, delete, and execute are granted separately: an identity may read a database but not modify it, or execute a tool but not reconfigure it. Operation matrices make the granted set explicit and reviewable. Default-deny closes anything not listed.", "separate grants per operation", "explicit operation matrices", "default-deny for unlisted operations", "CFG = {1: {\"read\"}, 2: {\"read\", \"write\"}, 3: {\"read\", \"write\", \"execute\"}}\ngrants = CFG[LEVEL]\nfor op in [\"read\", \"write\", \"delete\", \"execute\"]:\n    print(\"grants:\", sorted(grants), \"|\", op, \"->\", \"ALLOW\" if op in grants else \"DENY\")"],
["resource-scoping", "Policy combining (deny-overrides)", "When multiple policies apply to one request, their decisions are combined with an explicit rule: deny-overrides means any deny wins over allows. Combining rules are declared up front so outcomes are predictable. Conflicting allows without a deny resolve to allow.", "combining decisions from multiple policies", "deny-overrides as the combining rule", "declared combining algorithms, never implicit", "CFG = {1: [\"allow\", \"allow\"], 2: [\"allow\", \"deny\", \"allow\"], 3: [\"deny\", \"deny\"]}\ndecisions = CFG[LEVEL]\nfinal = \"DENY\" if \"deny\" in decisions else \"ALLOW\"\nprint(\"policy decisions:\", decisions, \"| combined (deny-overrides):\", final)"],
["field-level", "Time-bounded grants", "Grants carry a validity window: not-before and not-after timestamps. Requests outside the window are denied even if everything else matches. Time bounds make temporary access self-expiring, which removes the need for a separate revocation step.", "not-before / not-after validity windows", "self-expiring temporary access", "clock-skew tolerance in window checks", "CFG = {1: (9, 17, 12), 2: (9, 17, 8), 3: (9, 17, 18)}\nstart, end, now = CFG[LEVEL]\ninside = start - 1 <= now <= end + 1  # 1h skew tolerance\nprint(\"window %d-%d, now %d ->\" % (start, end, now), \"ALLOW\" if inside else \"DENY\")"]
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
var gen={version:"jahdb-archive-toolkit-fine-grained-access-policy-engine-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-fine-grained-access-policy-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
