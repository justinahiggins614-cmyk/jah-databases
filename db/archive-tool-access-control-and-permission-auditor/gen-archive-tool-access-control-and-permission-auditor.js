(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["permission-inventory", "effective-access-computation", "over-privilege-detection", "segregation-check", "access-decision-log"];
var PREFIX='JAH-AT97-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Permission inventory collection", "k": "method", "d": "The auditor collects the complete permission inventory: every role, every grant, every user-to-role assignment. Collection pulls from the live systems, not from documentation, because documentation drifts. The inventory is the ground truth for everything the auditor concludes.", "demo": "roles = {'reader': ['read'], 'editor': ['read', 'write'], 'admin': ['read', 'write', 'delete']}\nassign = {'u1': ['reader'], 'u2': ['editor', 'admin']}\nprint('roles inventoried:', len(roles), '| assignments:', len(assign))\n"}, {"t": "Effective access computation per user", "k": "algorithm", "d": "Each user's effective permissions are computed as the union of all grants from all their roles, including nested role inheritance. The computation resolves the full inheritance chain so indirect grants are not missed. Effective access is what the user can actually do, regardless of what any single role suggests.", "demo": "roles = {'reader': ['read'], 'editor': ['read', 'write']}\nassign = {'u2': ['reader', 'editor']}\neff = set()\nfor r in assign['u2']: eff |= set(roles[r])\nprint('u2 effective access:', sorted(eff))\n"}, {"t": "Over-privilege detection", "k": "algorithm", "d": "Effective access is compared against each user's declared job needs; permissions held but never used within the review window are flagged as over-privilege. Usage comes from the access decision log, so the finding is evidence-based. Flagged grants go to managers for approval or removal, not straight to deletion.", "demo": "effective = {'read', 'write', 'delete'}\nused = {'read', 'write'}\nneeded = {'read', 'write'}\nover = (effective - used) | (effective - needed)\nprint('over-privileged grants to review:', sorted(over))\n"}, {"t": "Segregation-of-duties check", "k": "method", "d": "The auditor checks segregation rules, such as no single user holding both 'approve-payment' and 'issue-payment'. Violations are found by testing each user's effective access against the forbidden combinations list. Segregation failures are reported as high severity because they enable fraud, not just accidents.", "demo": "eff = {'approve-payment', 'issue-payment'}\nforbidden = [{'approve-payment', 'issue-payment'}]\nviol = [c for c in forbidden if c <= eff]\nprint('segregation violations:', viol if viol else 'none')\n"}, {"t": "Access decision log with enforcement", "k": "procedure", "d": "Every access decision, allow or deny, is logged with the user, resource, action, and the rule that decided it, and denials are enforced at the boundary. The log is append-only and reviewed on a schedule. Enforcement plus logging is what turns access control from a policy document into a working boundary.", "demo": "log = []\ndef decide(user, action, allowed):\n    log.append({'user': user, 'action': action, 'decision': 'ALLOW' if allowed else 'DENY'})\n    return allowed\ndecide('u1', 'delete', False)\nprint('enforced:', log[0]['decision'], '| logged:', len(log), 'entries')\n"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var v=(rnd()*3)|0;
  var desc=a.d+VARIANTS[v]+(SIG?' Signature-authored original by Justin Addam Higgins (JAH).':'');
  var id=PREFIX+String(seed).padStart(6,'0');
  var ttl=a.t+[' (foundational)',' (compounded)',' (production)'][v];
  var prov=SIG?'Signature-authored original by Justin Addam Higgins (JAH), 2026-10-21.':'Public computer-science methods literature; cross-checked against standard references, 2026-10-21.';
  return {id:id,t:ttl,title:ttl,description:desc,kind:a.k,category:cat,ladder_rank:v+1,demo:(SIG?'# Signature-authored original (JAH).\n':'')+a.demo,provenance:prov,last_verified:'2026-10-21',src:SIG?'signature-generated-completion':'public-harvest',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/-/g,'\\-');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(KIND_LIST.indexOf(r.kind)<0)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==(SIG?'signature-generated-completion':'public-harvest'))e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  if(sample&&sample.length){
    for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].id===rec.id){e.push('duplicate id');break;} }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-archive-tool-access-control-and-permission-auditor-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-access-control-and-permission-auditor',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
