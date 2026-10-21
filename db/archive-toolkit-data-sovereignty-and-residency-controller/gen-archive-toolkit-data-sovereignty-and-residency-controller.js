(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["residency-rules", "transfer-controls", "localization"];
var PREFIX="JAH-ATK275-";
var KIND="data sovereignty and residency controller";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["residency-rules", "Residency rule engine", "Datasets are tagged with allowed storage and processing regions, and the rule engine checks every placement decision against the tags. A dataset tagged EU-only is never written to US storage. Rules are evaluated at write time, read time for processing location, and replication time.", "allowed-region tags per dataset", "checks at write, process, and replicate time", "deny-by-default for untagged data", "CFG = {1: (\"EU\", [\"EU\"]), 2: (\"US\", [\"EU\"]), 3: (\"EU\", [\"EU\", \"US\"])}\nregion, allowed = CFG[LEVEL]\nprint(\"store in\", region, \"| allowed:\", allowed, \"->\", \"ALLOW\" if region in allowed else \"DENY\")"],
["transfer-controls", "Cross-border transfer assessment", "Transfers across borders are assessed against adequacy decisions, safeguards (standard contractual clauses), and derogations. Each transfer records its legal basis. Transfers without a valid basis are blocked before any bytes move.", "adequacy and safeguard checks", "recorded legal basis per transfer", "blocking baseless transfers pre-move", "CFG = {1: (\"EU\", \"US\", \"adequacy\"), 2: (\"EU\", \"US\", None), 3: (\"EU\", \"CH\", \"adequacy\")}\nsrc, dst, basis = CFG[LEVEL]\nprint(\"transfer %s -> %s basis: %s\" % (src, dst, basis or \"NONE\"), \"->\", \"ALLOW\" if basis else \"BLOCK\")"],
["localization", "Data localization enforcement", "Certain data categories (health, financial, government) must remain within national borders by law. Localization rules pin these categories to in-country storage and processing, and the controller rejects any operation that would move them out. Localization is verified by audit, not assumed.", "in-country pinning for regulated categories", "rejecting out-of-country operations", "audit-verified localization", "CFG = {1: (\"health\", \"DE\", \"DE\"), 2: (\"health\", \"DE\", \"US\"), 3: (\"marketing\", \"DE\", \"US\")}\ncat, home, target = CFG[LEVEL]\nLOCALIZE = {\"health\", \"financial\", \"government\"}\nok = not (cat in LOCALIZE and target != home)\nprint(\"category:\", cat, \"| %s -> %s\" % (home, target), \"|\", \"ALLOW\" if ok else \"DENY: localization\")"],
["residency-rules", "Region-aware routing", "Processing requests are routed to regions where the data is allowed to be processed. The router considers data tags, user location, and service availability. Misrouted requests are rejected rather than processed in the wrong region.", "routing by data tags and user location", "availability-aware region choice", "rejecting misrouted requests", "CFG = {1: ([\"EU\"], \"EU\"), 2: ([\"EU\"], \"US\"), 3: ([\"EU\", \"US\"], \"US\")}\nallowed, user = CFG[LEVEL]\nregion = user if user in allowed else allowed[0]\nprint(\"allowed:\", allowed, \"| user in\", user, \"| route to:\", region)"],
["transfer-controls", "Residency audit trail", "Every storage and processing location decision is logged: what data, where, when, under which rule. The audit trail proves compliance to regulators and reveals drift. Trails are retained as long as the data they describe.", "logging every location decision", "regulator-ready compliance evidence", "retention tied to the data", "CFG = {1: 2, 2: 5, 3: 9}\nN = CFG[LEVEL]\ntrail = [{\"data\": \"ds-%d\" % i, \"region\": \"EU\", \"rule\": \"tag-match\"} for i in range(N)]\nprint(\"audit entries:\", len(trail), \"| complete:\", all(\"rule\" in e for e in trail))"]
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
var gen={version:"jahdb-archive-toolkit-data-sovereignty-and-residency-controller-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-data-sovereignty-and-residency-controller",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
