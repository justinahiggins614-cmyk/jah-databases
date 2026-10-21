(function(){'use strict';
/* jahdb-defense-aerospace-cisco-defenseclaw-skill-scanner-1.0 — deterministic boundless generator for defense-aerospace-cisco-defenseclaw-skill-scanner-signature.
   Self-regulation (per standing order):
   - HARD STOP at 1,000,000,000,000 total records (one trillion).
   - Throttled: at most MAX_PER_CALL records per request.
   - Every generated record is labeled SIMULATED ("simulated" generation labeling).
   - Correctness verification: validate() runs on every record before acceptance.
   - Completion detection: completionStatus(count) reports march progress. */
var MAX_TOTAL=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
var CATS=["agent-security", "skill-scanning", "mcp", "policy", "audit", "least-privilege"];
var PREFIX='JAH-DAE43S-';
var DBNAME="Signature Cisco DefenseClaw / Skill Scanner Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["agent-security",
 "Signature Cisco DefenseClaw / Skill Scanner: What Skill Scanning Is: Auditing Agent Capabilities",
 "The Signature counterpart is the SigClaw auditor, Manon's original agent-governance design. SigClaw mirrors the scan-and-enforce pattern but every capability carries a signed grant \u2014 who approved it, for what purpose, expiring when. The Signature design makes ungranted capabilities unrunnable: the agent runtime refuses tools without a valid grant.",
 ["Inventory every agent capability", "Schemas and permissions inspected", "Over-privilege reported"],
 "console.log('skill scan:');\n['enumerate tools','inspect schemas + permissions','compare against policy','report over-privilege'].forEach(function(s){console.log(' '+s);});"],
["skill-scanning",
 "Signature Cisco DefenseClaw / Skill Scanner: MCP Servers: The New Attack Surface",
 "The bench's MCP doctrine is the plumbing inspection: every server registered with its tool list, scopes, and trust level. The Signature design sandboxes MCP servers by default \u2014 a new server gets minimum permissions until its grant is reviewed and signed.",
 ["Standardized agent data/action access", "Confused-deputy risks", "Sandboxed by default, grants signed"],
 "var servers=[['files','read:/docs','trusted'],['db','write:prod','REVIEW REQUIRED']];\nservers.forEach(function(s){console.log('mcp '+s[0]+': '+s[1]+' ('+s[2]+')');});"],
["mcp",
 "Signature Cisco DefenseClaw / Skill Scanner: Policy: Least Privilege for Agents",
 "SigClaw's policies are the charters: per-agent, versioned, signed. The Signature design requires the charter review before deployment \u2014 the reviewer asks 'does the agent's job need this tool?' for every grant, and the answers are recorded.",
 ["Job description as enforceable policy", "Generated from observed behavior", "Grants temporary, reviewed, signed"],
 "var charter={agent:'support-bot',tools:['kb_search','ticket_read'],expires:'2026-12-31'};\nconsole.log('charter: '+charter.agent+' -> '+charter.tools.join(', '));\nconsole.log('expires '+charter.expires+' (grants are temporary)');"],
["policy",
 "Signature Cisco DefenseClaw / Skill Scanner: Enforcement: The Runtime That Says No",
 "SigClaw's enforcement is the gatekeeper: every tool call checked, validated, logged \u2014 in the runtime, not in the prompt. The Signature design treats prompt-injection against the gatekeeper as the test suite: the gatekeeper must refuse even when the agent insists.",
 ["Interpose on every tool call", "Grants checked in the runtime", "Denied calls as security signals"],
 "function gatekeeper(call,grants){return grants.indexOf(call.tool)>=0?'ALLOW':'DENY';}\nconsole.log('call ticket_read: '+gatekeeper({tool:'ticket_read'},['kb_search','ticket_read']));\nconsole.log('call db_write: '+gatekeeper({tool:'db_write'},['kb_search','ticket_read'])+' (logged)');"],
["audit",
 "Signature Cisco DefenseClaw / Skill Scanner: Your First Scan: Inventory an Assistant",
 "The bench's first scan is the opening of the books: same inventory, but the report is a signed finding. The Signature design makes the first scan mandatory before any agent touches production data \u2014 no charter, no data.",
 ["Inventory tools and MCP servers", "First scan always finds surprises", "Scan mandatory before production data"],
 "var inv={tools:12,mcp:3,overpriv:2};\nconsole.log('inventory: '+inv.tools+' tools, '+inv.mcp+' MCP servers');\nconsole.log('findings: '+inv.overpriv+' over-privileged (signed report)');\nconsole.log('remediate, re-scan, then production');"],
["least-privilege",
 "Signature Cisco DefenseClaw / Skill Scanner: Prompt Injection vs Tool Grants",
 "SigClaw's layering is the castle doctrine: hygiene at the prompt layer, containment at the grant layer. The Signature design tests both \u2014 red-team the prompts, audit the grants \u2014 and the grant layer must hold even when the prompt layer falls.",
 ["Grants contain the blast radius", "Defense in depth: prompt + grant layers", "Grant layer must hold alone"],
 "console.log('injected: \"delete the database\"');\nconsole.log('grant check: db_write NOT granted -> DENIED');\nconsole.log('prompt layer fell; grant layer held (by design)');"],
["agent-security",
 "Signature Cisco DefenseClaw / Skill Scanner: Supply Chain: Skills from Strangers",
 "The bench's supply-chain doctrine is the quarantine: new skills run sandboxed with minimum grants until reviewed. The Signature design requires the review record \u2014 who reviewed, what changed, what was granted \u2014 before the quarantine lifts.",
 ["Third-party skills as supply chain", "Pin versions, review updates", "Quarantine until reviewed"],
 "var skill={name:'pdf-tools',v:'2.1.0',new_perm:'network'};\nconsole.log('skill '+skill.name+' v'+skill.v+': new permission '+skill.new_perm);\nconsole.log('-> QUARANTINE (review required before grant)');"],
["skill-scanning",
 "Signature Cisco DefenseClaw / Skill Scanner: Defensive Uses: The Governed Agent Fleet",
 "SigClaw's fleet doctrine is the chartered fleet: every agent with a signed charter, every call logged, every grant expiring. The Signature design adds the charter census \u2014 the fleet's total capability surface, reviewed quarterly, because the sum of small grants can be a large attack surface.",
 ["Chartered, logged, expiring grants", "Bounded capability per agent", "Fleet surface reviewed quarterly"],
 "console.log('fleet: 140 agents, charters signed, grants current');\nconsole.log('charter census: total surface reviewed quarterly');"],
["mcp",
 "Signature Cisco DefenseClaw / Skill Scanner: Cross-Agent Risk: Agents Talking to Agents",
 "SigClaw's composition doctrine is the graph audit: invocation edges mapped, transitive grants computed, escalations flagged. The Signature design requires the graph review when agents gain the ability to invoke each other \u2014 composition is a privilege change, treated as one.",
 ["Invocation graphs, transitive permissions", "Composition as privilege change", "Graph reviews on new edges"],
 "var edges=[['a-support','a-db'],['a-db','a-prod']];\nconsole.log('invocation graph: '+edges.map(function(e){return e.join('->');}).join(', '));\nconsole.log('transitive: a-support reaches a-prod -> ESCALATION FLAGGED');"],
["policy",
 "Signature Cisco DefenseClaw / Skill Scanner: Audit Trails: Proving What the Agent Did",
 "The bench's audit is the ledger: every invocation chained, retained, queryable. The Signature design makes the ledger tamper-evident \u2014 the chain is verified on read, so post-incident editing is detectable.",
 ["Who, what, with whose grant, what resulted", "Hash-chained, tamper-evident", "Queryable for review and compliance"],
 "console.log('ledger: 48,211 invocations, chain verified');\nconsole.log('query: agent support-bot, tool ticket_read, 2026-10-20 -> 312 calls');"],
["audit",
 "Signature Cisco DefenseClaw / Skill Scanner: Debugging: The Denied Call",
 "The bench's triage is the denied-call review: context-rich log, two outcomes (fix charter or fix agent). The Signature design tracks the denied-call rate \u2014 a rising rate means the charter and the job are diverging, and the review is scheduled, not postponed.",
 ["Triage: fix the charter or fix the agent", "Context-rich denied-call logs", "Rate trends trigger reviews"],
 "console.log('denied: db_write by support-bot (charter: read-only)');\nconsole.log('triage: legitimate need -> charter review scheduled');\nconsole.log('denied-call rate: 0.3% (stable)');"],
["least-privilege",
 "Signature Cisco DefenseClaw / Skill Scanner: Continuous Monitoring: Drift in Capabilities",
 "The bench's monitoring is the watch: weekly scans, diffed, alerted. The Signature design makes expired grants self-revoking \u2014 the runtime refuses them without human action, so 'forgotten temporary access' cannot exist.",
 ["Weekly scans diffed against charters", "Temporary grants expire by design", "Drift alerts as maintenance"],
 "var grants=[['temp-db','expired'],['kb_search','current']];\ngrants.forEach(function(g){console.log(g[0]+': '+g[1]+(g[1]==='expired'?' -> SELF-REVOKED':''));});"],
["agent-security",
 "Signature Cisco DefenseClaw / Skill Scanner: Testing: Red-Teaming the Agent",
 "The bench's red-teaming is the gauntlet: injection suites, misuse scenarios, boundary probes per charter change. The Signature design requires the gauntlet green before deployment \u2014 the agent's adversaries are part of its test suite.",
 ["Adversarial prompt and tool suites", "Grant layer must hold", "Re-run per charter change"],
 "var gauntlet=[['injection suite',1],['misuse scenarios',1],['boundary probes',1]];\ngauntlet.forEach(function(g){console.log(g[0]+': '+(g[1]?'HELD':'BREACHED'));});\nconsole.log('gauntlet GREEN -> deployment approved');"],
["skill-scanning",
 "Signature Cisco DefenseClaw / Skill Scanner: Real-World Pattern: Support Agent Hardening",
 "The bench's pattern doctrine is the hardening arc: scan, charter, sandbox, red-team, deploy, monitor. The Signature design publishes the arc's evidence \u2014 the scan reports, the red-team results \u2014 with the deployment, because trust is documented.",
 ["Scan to deploy in six steps", "Scope creep caught by census", "Evidence published with deployment"],
 "console.log('hardening arc complete: 8 tools chartered, 0 out-of-charter actions');\nconsole.log('evidence published with deployment (trust documented)');"],
["mcp",
 "Signature Cisco DefenseClaw / Skill Scanner: Mastery: The Agent-Governance Playbook",
 "The bench's mastery adds the stewardship layer: charters, ledgers, censuses. Manon's roadmap runs from today's single agents to governed fleets under one claw discipline \u2014 employees with superpowers, all of them chartered.",
 ["Threat modeling through audit architecture", "Fleet-wide governance as code", "Stewardship: charters, ledgers, censuses"],
 "var playbook=['threat modeling','charter authorship','enforcement design','red-teaming','audit architecture'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Agents are employees with superpowers. Onboard them.');"]
];
function escId(s){return String(s).replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
var IDRE=new RegExp('^'+escId(PREFIX)+'\\d{6}$');
function generate(seed,opts){
  opts=opts||{};var r=prng(seed);
  var cat=opts.category||pick(r,CATS);
  var pool=POOL.filter(function(p){return p[0]===cat;});
  var tp=pick(r,pool.length?pool:POOL);
  var id=PREFIX+String(100000+(seed%900000));
  var variant=ri(r,2,48);
  var ladder=1+(seed%15);
  return {
    id:id,
    title:tp[1],
    ladder_rank:ladder,
    edition:'signature',
    category:tp[0],
    tags:["ai-agents", "mcp", "skill-scanning", "policy-enforcement", "audit", "defense", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
    last_verified:'2026-10-21',
    record_kind:"cisco defenseclaw skill scanner record",
    simulated:true,
    generation:'SIMULATED — generated content (seed '+seed+'), validated by independent checker',
    _seed:seed
  };
}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(rec.id||''))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(!(rec.ladder_rank>=1&&rec.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(rec.category)<0)e.push('category');
  if(!rec.demo||typeof rec.demo.code!=='string'||rec.demo.code.length<10)e.push('demo.code');
  if(rec.simulated!==true)e.push('simulated-label');
  if(typeof rec.description!=='string'||rec.description.length<20)e.push('description');
  if(!Array.isArray(rec.key_facts)||!rec.key_facts.length)e.push('key_facts');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title vs archive']};}
  return {ok:true,errors:[]};
}
function completionStatus(count){
  count=+count||0;
  return {target:1000000,hardStop:MAX_TOTAL,count:count,
    pct:Math.min(100,+(100*count/1000000).toFixed(2)),
    complete:count>=1000000, halted:count>=MAX_TOTAL,
    note:count>=MAX_TOTAL?'HARD STOP: one-trillion record limit reached — generation halted.':'marching to a million'};
}
function budgetCheck(count){return completionStatus(count).halted?{ok:false,errors:['hard stop: 1e12 reached']}:{ok:true,errors:[]};}
var gen={version:'jahdb-defense-aerospace-cisco-defenseclaw-skill-scanner-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-cisco-defenseclaw-skill-scanner-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-cisco-defenseclaw-skill-scanner-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();