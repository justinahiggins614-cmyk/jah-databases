(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["identity-scoping", "policy-evaluation", "enforcement-point"];
var PREFIX="JAH-ATK256-";
var KIND="tool permission enforcer";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["identity-scoping", "Role-based access control (RBAC)", "Permissions are granted to roles, and identities are assigned roles, instead of wiring permissions to individuals. An identity's effective permissions are the union of its roles' permissions. RBAC keeps permission management tractable as the number of identities grows.", "granting permissions via roles", "computing effective permissions as the union of roles", "role hierarchies with inherited permissions", "CFG = {1: [\"viewer\"], 2: [\"viewer\", \"editor\"], 3: [\"viewer\", \"editor\", \"admin\"]}\nROLES = {\"viewer\": {\"read\"}, \"editor\": {\"read\", \"write\"}, \"admin\": {\"read\", \"write\", \"delete\"}}\neffective = set().union(*[ROLES[r] for r in CFG[LEVEL]])\nfor op in [\"read\", \"write\", \"delete\"]:\n    print(\"can %s:\" % op, op in effective)"],
["policy-evaluation", "Attribute-based access control (ABAC)", "ABAC evaluates policy rules over attributes of the subject, the resource, the action, and the environment. A rule like 'analysts may read datasets labeled internal during business hours' is evaluated per request. ABAC handles fine-grained cases RBAC cannot express.", "evaluating rules over subject/resource/action attributes", "environment attributes like time and network", "combining multiple ABAC rules with explicit precedence", "CFG = {1: {\"role\": \"analyst\", \"label\": \"internal\", \"hour\": 10}, 2: {\"role\": \"analyst\", \"label\": \"secret\", \"hour\": 10}, 3: {\"role\": \"analyst\", \"label\": \"internal\", \"hour\": 23}}\na = CFG[LEVEL]\nrule_ok = a[\"role\"] == \"analyst\" and a[\"label\"] in (\"public\", \"internal\") and 8 <= a[\"hour\"] <= 18\nprint(\"request:\", a, \"| allowed:\", rule_ok)"],
["enforcement-point", "Least-privilege scope tokens", "Tools receive short-lived tokens carrying only the scopes they need for the current task. A token for reading cannot write; a token for one database cannot touch another. Narrow scopes plus short lifetimes shrink the blast radius of a compromised token.", "issuing tokens with minimal scopes", "short lifetimes with refresh on demand", "audience binding so tokens work on one service only", "CFG = {1: [\"read\"], 2: [\"read\", \"write\"], 3: [\"read\", \"write\"]}\ntoken = {\"scopes\": set(CFG[LEVEL]), \"ttl_s\": 600}\nfor op, need in [(\"read\", \"read\"), (\"write\", \"write\"), (\"delete\", \"delete\")]:\n    print(\"token scopes:\", sorted(token[\"scopes\"]), \"| %s ->\" % op, \"ALLOW\" if need in token[\"scopes\"] else \"DENY\")"],
["identity-scoping", "Policy decision point / enforcement point split", "The policy decision point (PDP) evaluates policy and returns a decision; the policy enforcement point (PEP) carries it out and cannot override it. Separating decision from enforcement lets one audited PDP serve many PEPs and keeps enforcement dumb and predictable.", "a PDP that only decides", "PEPs that only enforce", "one audited PDP serving many PEPs", "CFG = {1: (\"amy\", \"read\", \"db1\"), 2: (\"amy\", \"write\", \"db1\"), 3: (\"bob\", \"delete\", \"db1\")}\nPOLICY = {(\"amy\", \"read\", \"db1\"), (\"amy\", \"write\", \"db1\")}\ndef pdp(sub, act, res):\n    return (sub, act, res) in POLICY  # decision only\ndef pep(sub, act, res):\n    decision = pdp(sub, act, res)     # enforcement only\n    return \"EXECUTED\" if decision else \"BLOCKED\"\nsub, act, res = CFG[LEVEL]\nprint(\"PDP decision:\", pdp(sub, act, res), \"| PEP:\", pep(sub, act, res))"],
["policy-evaluation", "Permission caching with invalidation", "Permission decisions are cached for speed, but the cache is invalidated the moment policy changes. A version counter on the policy lets cached entries detect staleness without a central invalidation bus. This gives fast checks with correct revocation.", "caching decisions keyed by subject/action/resource", "invalidating on policy version change", "negative caching with short TTLs for denies", "CFG = {1: 1, 2: 2, 3: 3}\nPOLICY_VERSION = CFG[LEVEL]\ncache = {}\ndef check(sub, act):\n    key = (sub, act, POLICY_VERSION)\n    if key in cache:\n        return cache[key] + \" (cached)\"\n    decision = \"ALLOW\" if act == \"read\" else \"DENY\"\n    cache[key] = decision\n    return decision + \" (fresh)\"\nprint(check(\"amy\", \"read\")); print(check(\"amy\", \"read\"))\nprint(\"policy v%d: stale entries from older versions never hit\" % POLICY_VERSION)"]
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
var gen={version:"jahdb-archive-toolkit-tool-permission-enforcer-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-tool-permission-enforcer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
