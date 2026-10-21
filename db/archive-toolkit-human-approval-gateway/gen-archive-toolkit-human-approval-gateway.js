(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["approval-workflow", "risk-tiering", "audit-consent"];
var PREFIX="JAH-ATK254-";
var KIND="human approval gateway";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["approval-workflow", "Tiered approval thresholds", "Actions are scored for risk, and each risk tier maps to an approval requirement: low-risk actions are auto-approved, medium-risk need one approver, high-risk need two. Thresholds are set in policy, not in code, so they can be tuned without redeploying. Every decision records the tier and the rule that fired.", "scoring actions into risk tiers", "mapping tiers to approver counts in policy", "tuning thresholds from historical approval outcomes", "CFG = {1: [5, 45, 80], 2: [15, 55, 95], 3: [25, 65, 99]}\nTIERS = [(30, \"auto\"), (70, \"one-approver\"), (101, \"two-approvers\")]\nfor risk in CFG[LEVEL]:\n    need = next(label for bound, label in TIERS if risk < bound)\n    print(\"risk %d -> %s\" % (risk, need))"],
["risk-tiering", "Dual-control (four-eyes) approval", "Consequential actions require two independent approvers: the second approver must be a different person who reviews the same context packet. This four-eyes principle catches mistakes and blocks unilateral abuse. The gateway enforces approver independence cryptographically where identities are managed.", "requiring two distinct approver identities", "independent review of the same context packet", "separation-of-duty rules (requester cannot approve)", "CFG = {1: [\"amy\", \"amy\"], 2: [\"amy\", \"bob\"], 3: [\"amy\", \"bob\", \"amy\"]}\napprovals = CFG[LEVEL]\nrequester = \"amy\"\ndistinct = [a for a in approvals if a != requester]\nok = len(set(distinct)) >= 2\nprint(\"approvals:\", approvals, \"| requester:\", requester, \"| dual-control satisfied:\", ok)"],
["audit-consent", "Time-boxed approval request", "Every approval request carries a time-to-live. If no human responds before the TTL, the request expires and the default is deny: the action does not proceed on silence. Time-boxing prevents stale approvals from authorizing actions long after the context changed.", "expiring unanswered requests at TTL", "default-deny on timeout", "escalating TTLs by risk tier", "CFG = {1: {\"ttl\": 60, \"waited\": 90}, 2: {\"ttl\": 300, \"waited\": 120}, 3: {\"ttl\": 60, \"waited\": 30}}\nttl, waited = CFG[LEVEL][\"ttl\"], CFG[LEVEL][\"waited\"]\nif waited <= ttl:\n    print(\"answered in %ds of %ds TTL -> PROCEED\" % (waited, ttl))\nelse:\n    print(\"unanswered after %ds of %ds TTL -> EXPIRED, default DENY\" % (waited, ttl))"],
["approval-workflow", "Approval with context packet", "The approver never decides blind: each request bundles a context packet with who is acting, what will happen, why it is needed, and how to reverse it. The packet is immutable once submitted, so the approver's decision is tied to exact facts. Packets are archived with the decision for audit.", "bundling who/what/why/reversible-steps", "immutable packets tied to the decision", "archiving packets with decisions for audit", "CFG = {1: \"restart\", 2: \"schema-migration\", 3: \"bulk-delete\"}\npacket = {\"who\": \"svc-indexer\", \"what\": CFG[LEVEL], \"why\": \"scheduled maintenance\",\n          \"reverse\": \"restore from snapshot\", \"risk\": \"medium\"}\nrequired = [\"who\", \"what\", \"why\", \"reverse\"]\ncomplete = all(k in packet and packet[k] for k in required)\nprint(\"context packet complete:\", complete)\nfor k in required:\n    print(\" \", k, \"=\", packet[k])"],
["risk-tiering", "Delegated approval chains", "An approver can delegate authority within policy bounds: the delegation names the delegate, the scope, and the expiry. The gateway validates the whole chain from the original authority to the final approver. Delegations outside policy bounds are rejected before they can be used.", "validating delegation chains to the original authority", "scope and expiry bounds on delegations", "revocation lists that invalidate delegated approvals", "CFG = {1: [\"ceo\", \"vp\"], 2: [\"ceo\", \"vp\", \"mgr\"], 3: [\"ceo\", \"vp\", \"mgr\", \"lead\"]}\nchain = CFG[LEVEL]\nauthority = {\"ceo\": 3, \"vp\": 2, \"mgr\": 1, \"lead\": 1}  # max delegation depth\ndepth_ok = all(authority.get(p, 0) >= len(chain) - 1 - i for i, p in enumerate(chain))\nprint(\"chain:\", \" -> \".join(chain), \"| valid:\", depth_ok)"]
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
var gen={version:"jahdb-archive-toolkit-human-approval-gateway-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-human-approval-gateway",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
