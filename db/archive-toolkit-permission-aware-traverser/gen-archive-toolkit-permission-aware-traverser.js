(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK139-";
var KIND="traversal method";
var TOOLNAME="Permission-Aware Traverser";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "ACL evaluation", "d": "Access control lists grant/deny per path and identity; most-specific rule wins. Deterministic precedence avoids ambiguity. Clear rules are auditable rules.", "c": "fundamentals", "r": 1, "p": {"IDENT": "amy", "TREE": "{'pub': {'a.txt': None}, 'priv': {'b.txt': None}}", "ACL": "[['/pub*', '*', ['read']], ['/priv*', 'amy', ['read']], ['/priv*', 'bob', []]]"}}, {"t": "Prune-before-descend", "d": "Traversers check permission before entering each directory, never listing denied branches. Early pruning avoids leaking names. Pruning is both security and speed.", "c": "algorithms", "r": 1, "p": {"IDENT": "bob", "TREE": "{'pub': {'a.txt': None}, 'priv': {'b.txt': None}}", "ACL": "[['/pub*', '*', ['read']], ['/priv*', 'amy', ['read']]]"}}, {"t": "Deny-by-default", "d": "Default-deny means that no matching rule equals no access, so traversers start from zero permission. Fail-closed is the safe posture: mistakes in policy then deny rather than leak. Getting the default right matters more than any individual rule.", "c": "implementation", "r": 1, "p": {"IDENT": "eve", "TREE": "{'docs': {'x.txt': None}}", "ACL": "[['/docs*', 'amy', ['read']]]"}}, {"t": "Group membership", "d": "Groups bundle identities; ACLs reference groups. Membership resolution happens at check time. Groups scale administration.", "c": "optimization", "r": 1, "p": {"IDENT": "amy", "TREE": "{'team': {'f.txt': None}}", "ACL": "[['/team*', 'staff', ['read']]]"}}, {"t": "Inheritance", "d": "Child paths inherit parent permissions unless overridden. Inheritance keeps ACLs compact. Overrides handle exceptions.", "c": "evaluation", "r": 1, "p": {"IDENT": "amy", "TREE": "{'proj': {'sub': {'f.txt': None}}}", "ACL": "[['/proj*', 'amy', ['read']]]"}}, {"t": "Audit of traversals", "d": "Every allowed or denied traversal decision is logged with the identity, path, and rule that decided it. These logs prove compliance during audits and explain exactly what each identity could reach. Accountability needs records, and permission-aware traversal keeps them.", "c": "fundamentals", "r": 2, "p": {"IDENT": "amy", "TREE": "{'a': {'f.txt': None}}", "ACL": "[['/a*', 'amy', ['read']]]"}}, {"t": "Time-bound grants", "d": "Grants carry expiry; traversers re-check per session. Expiry bounds exposure. Time limits contain risk.", "c": "algorithms", "r": 2, "p": {"IDENT": "temp", "TREE": "{'tmp': {'f.txt': None}}", "ACL": "[['/tmp*', 'temp', ['read']]]"}}, {"t": "Attribute-based control", "d": "ABAC evaluates attributes (clearance, department) instead of identity lists. Policies express 'managers can read reports'. ABAC scales where ACLs sprawl.", "c": "implementation", "r": 2, "p": {"IDENT": "mgr1", "TREE": "{'reports': {'q.pdf': None}}", "ACL": "[['/reports*', 'mgr1', ['read']]]"}}, {"t": "Row-level filtering", "d": "Databases filter rows by policy predicates during traversal. Predicates push into the query plan. Filtering keeps semantics correct.", "c": "optimization", "r": 2, "p": {"IDENT": "amy", "TREE": "{'rows': {'r1': None, 'r2': None}}", "ACL": "[['/rows*', 'amy', ['read']]]"}}, {"t": "Consent scoping", "d": "Personal data traverses only with recorded consent scope. Scope checks precede access. Consent is a permission.", "c": "evaluation", "r": 2, "p": {"IDENT": "researcher", "TREE": "{'study': {'anon.csv': None}}", "ACL": "[['/study*', 'researcher', ['read']]]"}}, {"t": "Break-glass access", "d": "Emergency overrides grant temporary access with mandatory review. Overrides log loudly. Break-glass balances safety and availability.", "c": "fundamentals", "r": 3, "p": {"IDENT": "oncall", "TREE": "{'prod': {'db': None}}", "ACL": "[['/prod*', 'oncall', ['read']]]"}}, {"t": "Permission caching", "d": "Decisions cache per (identity, path) with short TTLs. Caching keeps traversal fast. Invalidation follows policy changes.", "c": "algorithms", "r": 3, "p": {"IDENT": "amy", "TREE": "{'c': {'f.txt': None}}", "ACL": "[['/c*', 'amy', ['read']]]"}}, {"t": "Explaining denials", "d": "Denials explain which rule blocked access (to authorized auditors). Explanations aid troubleshooting. Transparency within bounds.", "c": "implementation", "r": 3, "p": {"IDENT": "bob", "TREE": "{'x': {'f.txt': None}}", "ACL": "[['/x*', 'amy', ['read']]]"}}, {"t": "Least-privilege traversal", "d": "Traversers request only needed permissions, never broad ones. Narrow grants limit blast radius. Least privilege is discipline.", "c": "optimization", "r": 3, "p": {"IDENT": "svc", "TREE": "{'inbox': {'m.eml': None}}", "ACL": "[['/inbox*', 'svc', ['read']]]"}}, {"t": "Cross-system identity mapping", "d": "Federated identities map to local principals per system. Mapping keeps permissions meaningful across hops. Identity is the anchor.", "c": "evaluation", "r": 3, "p": {"IDENT": "amy@a", "TREE": "{'s': {'f.txt': None}}", "ACL": "[['/s*', 'amy@a', ['read']]]"}}];
var DEMO="# Permission-aware traversal: prune branches the identity cannot read before descending.\ntree = %%TREE%%\nacl = %%ACL%%\ndef can(identity, path, need=\"read\"):\n    # most-specific matching rule wins\n    best, perm = -1, set()\n    for pattern, who, allows in acl:\n        if who in (identity, \"*\") and (path == pattern or path.startswith(pattern.rstrip(\"*\"))):\n            if len(pattern) > best: best, perm = len(pattern), set(allows)\n    return need in perm\ndef walk(node, path, identity):\n    for name, sub in sorted(node.items()):\n        p = path + \"/\" + name\n        if not can(identity, p):\n            print(f\"  SKIP {p} (denied)\")\n            continue\n        print(f\"  VISIT {p}\")\n        if isinstance(sub, dict): walk(sub, p, identity)\nprint(\"traversal as %%IDENT%%:\")\nwalk(tree, \"\", \"%%IDENT%%\")\n";
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
  if(!new RegExp("^JAH\\-ATK139\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-permission-aware-traverser-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-permission-aware-traverser",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
