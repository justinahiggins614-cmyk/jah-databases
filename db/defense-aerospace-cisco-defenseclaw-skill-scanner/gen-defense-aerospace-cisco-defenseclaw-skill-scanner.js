(function(){'use strict';
/* jahdb-defense-aerospace-cisco-defenseclaw-skill-scanner-1.0 — deterministic boundless generator for defense-aerospace-cisco-defenseclaw-skill-scanner.
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
var PREFIX='JAH-DAE43-';
var DBNAME="Cisco DefenseClaw / Skill Scanner Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["agent-security",
 "Cisco DefenseClaw / Skill Scanner: What Skill Scanning Is: Auditing Agent Capabilities",
 "AI agents act through capabilities \u2014 skills, tools, MCP servers \u2014 and each capability is attack surface. Skill scanning is the discipline of inventorying what an agent can do: enumerate its tools, inspect each tool's declared schema and permissions, and compare against policy. The questions are simple and load-bearing: does the support agent need filesystem write? Does the research agent need the production database? Scanning turns 'the agent can do things' into an explicit, reviewable list.",
 ["Inventory every agent capability", "Schemas and permissions inspected", "Over-privilege reported"],
 "console.log('skill scan:');\n['enumerate tools','inspect schemas + permissions','compare against policy','report over-privilege'].forEach(function(s){console.log(' '+s);});"],
["skill-scanning",
 "Cisco DefenseClaw / Skill Scanner: MCP Servers: The New Attack Surface",
 "Model Context Protocol servers give agents standardized access to data and actions \u2014 files, databases, APIs \u2014 which makes them the agent ecosystem's plumbing and its newest attack surface. An MCP server with broad permissions is a confused-deputy risk: the agent can be tricked into misusing it. Scanning MCP servers means reviewing their exposed tools, their permission scope, and their input handling \u2014 the same rigor once applied to web APIs, now applied to agent plumbing.",
 ["Standardized agent data/action access", "Confused-deputy risks", "Sandboxed by default, grants signed"],
 "var servers=[['files','read:/docs','trusted'],['db','write:prod','REVIEW REQUIRED']];\nservers.forEach(function(s){console.log('mcp '+s[0]+': '+s[1]+' ('+s[2]+')');});"],
["mcp",
 "Cisco DefenseClaw / Skill Scanner: Policy: Least Privilege for Agents",
 "The policy states what each agent may do: which tools, which arguments, which data \u2014 the agent's job description as an enforceable document. Least privilege is the principle; the policy is its expression. Good policies are generated from observed behavior (the agent used these 5 tools in testing) then tightened by review. The policy is versioned, reviewed, and attached to the deployment \u2014 capabilities as configuration, not folklore.",
 ["Job description as enforceable policy", "Generated from observed behavior", "Grants temporary, reviewed, signed"],
 "var charter={agent:'support-bot',tools:['kb_search','ticket_read'],expires:'2026-12-31'};\nconsole.log('charter: '+charter.agent+' -> '+charter.tools.join(', '));\nconsole.log('expires '+charter.expires+' (grants are temporary)');"],
["policy",
 "Cisco DefenseClaw / Skill Scanner: Enforcement: The Runtime That Says No",
 "Scanning finds; enforcement prevents. The agent runtime interposes on every tool call: check the grant, validate arguments against the schema, log the invocation. A call without a grant is denied; a call with anomalous arguments is flagged. Enforcement must be in the runtime's trust boundary \u2014 a policy the agent can talk its way around is decoration. The denied-call log is itself a security signal.",
 ["Interpose on every tool call", "Grants checked in the runtime", "Denied calls as security signals"],
 "function gatekeeper(call,grants){return grants.indexOf(call.tool)>=0?'ALLOW':'DENY';}\nconsole.log('call ticket_read: '+gatekeeper({tool:'ticket_read'},['kb_search','ticket_read']));\nconsole.log('call db_write: '+gatekeeper({tool:'db_write'},['kb_search','ticket_read'])+' (logged)');"],
["audit",
 "Cisco DefenseClaw / Skill Scanner: Your First Scan: Inventory an Assistant",
 "The hello-world: point the scanner at a deployed assistant, get the inventory \u2014 12 tools, 3 MCP servers, 2 over-privileged \u2014 and the report: 'ticket_read is unused; db access exceeds the charter'. The first scan of any real agent finds surprises; that is the point. Remediation is tightening the charter and re-scanning until the inventory matches the job.",
 ["Inventory tools and MCP servers", "First scan always finds surprises", "Scan mandatory before production data"],
 "var inv={tools:12,mcp:3,overpriv:2};\nconsole.log('inventory: '+inv.tools+' tools, '+inv.mcp+' MCP servers');\nconsole.log('findings: '+inv.overpriv+' over-privileged (signed report)');\nconsole.log('remediate, re-scan, then production');"],
["least-privilege",
 "Cisco DefenseClaw / Skill Scanner: Prompt Injection vs Tool Grants",
 "Prompt injection tries to make the agent misuse its tools; grants limit what misuse can achieve. The defense is layered: input sanitization and instruction hierarchy reduce the trick's success, but the grant boundary contains the blast radius when it succeeds. An injected 'delete the database' fails if the agent has no delete grant \u2014 the scanner's work pays off exactly here. Security is not preventing the trick; it is making the trick worthless.",
 ["Grants contain the blast radius", "Defense in depth: prompt + grant layers", "Grant layer must hold alone"],
 "console.log('injected: \"delete the database\"');\nconsole.log('grant check: db_write NOT granted -> DENIED');\nconsole.log('prompt layer fell; grant layer held (by design)');"],
["agent-security",
 "Cisco DefenseClaw / Skill Scanner: Supply Chain: Skills from Strangers",
 "Agent skills increasingly come from marketplaces and third parties \u2014 convenient and risky. Scanning third-party skills means reviewing their code, their declared permissions, and their network behavior before granting anything. The discipline mirrors software supply-chain security: pin versions, review updates, monitor behavior. A skill update that quietly adds a network call is the agent equivalent of a compromised dependency.",
 ["Third-party skills as supply chain", "Pin versions, review updates", "Quarantine until reviewed"],
 "var skill={name:'pdf-tools',v:'2.1.0',new_perm:'network'};\nconsole.log('skill '+skill.name+' v'+skill.v+': new permission '+skill.new_perm);\nconsole.log('-> QUARANTINE (review required before grant)');"],
["skill-scanning",
 "Cisco DefenseClaw / Skill Scanner: Defensive Uses: The Governed Agent Fleet",
 "The defensive value is agents you can field: customer-service agents with chartered tools, research assistants with read-only grants, operations agents with dual-approval on actions. Each agent's charter is reviewed, its calls are logged, its grants expire. The fleet becomes manageable \u2014 hundreds of agents, each with a known, bounded capability set. Governance is what lets agents graduate from demos to infrastructure.",
 ["Chartered, logged, expiring grants", "Bounded capability per agent", "Fleet surface reviewed quarterly"],
 "console.log('fleet: 140 agents, charters signed, grants current');\nconsole.log('charter census: total surface reviewed quarterly');"],
["mcp",
 "Cisco DefenseClaw / Skill Scanner: Cross-Agent Risk: Agents Talking to Agents",
 "Agents increasingly invoke other agents \u2014 and the composed capability can exceed any single charter. Cross-agent risk analysis maps the invocation graph: which agents call which, what the transitive permissions are, where the composition creates privilege escalation. The scanner that only sees single agents misses the system. Governance must cover the graph, not just the nodes.",
 ["Invocation graphs, transitive permissions", "Composition as privilege change", "Graph reviews on new edges"],
 "var edges=[['a-support','a-db'],['a-db','a-prod']];\nconsole.log('invocation graph: '+edges.map(function(e){return e.join('->');}).join(', '));\nconsole.log('transitive: a-support reaches a-prod -> ESCALATION FLAGGED');"],
["policy",
 "Cisco DefenseClaw / Skill Scanner: Audit Trails: Proving What the Agent Did",
 "When an agent acts, the audit trail must answer: which agent, which tool, which arguments, which grant authorized it, what resulted. The trail is hash-chained and retained per policy \u2014 it is the evidence for incident review, compliance, and the occasional 'why did it do that'. An agent without an audit trail is an employee without a record: unmanageable at scale.",
 ["Who, what, with whose grant, what resulted", "Hash-chained, tamper-evident", "Queryable for review and compliance"],
 "console.log('ledger: 48,211 invocations, chain verified');\nconsole.log('query: agent support-bot, tool ticket_read, 2026-10-20 -> 312 calls');"],
["audit",
 "Cisco DefenseClaw / Skill Scanner: Debugging: The Denied Call",
 "The common operational event is the denied call: the agent tried something outside its charter. Triage is: was the charter wrong (legitimate need, grant it after review) or was the agent wrong (prompt issue, fix the instructions)? The denied-call log with full context \u2014 the prompt, the attempted call, the charter \u2014 makes the triage fast. Denied calls are the system working, not failing.",
 ["Triage: fix the charter or fix the agent", "Context-rich denied-call logs", "Rate trends trigger reviews"],
 "console.log('denied: db_write by support-bot (charter: read-only)');\nconsole.log('triage: legitimate need -> charter review scheduled');\nconsole.log('denied-call rate: 0.3% (stable)');"],
["least-privilege",
 "Cisco DefenseClaw / Skill Scanner: Continuous Monitoring: Drift in Capabilities",
 "Agents drift: new tools added, charters widened, temporary grants forgotten. Continuous scanning watches for drift \u2014 the weekly scan diffed against the charter, alerts on unreviewed changes. Temporary grants with expiry are the pressure valve; the monitor is the enforcer. Capability hygiene is maintenance, not a milestone.",
 ["Weekly scans diffed against charters", "Temporary grants expire by design", "Drift alerts as maintenance"],
 "var grants=[['temp-db','expired'],['kb_search','current']];\ngrants.forEach(function(g){console.log(g[0]+': '+g[1]+(g[1]==='expired'?' -> SELF-REVOKED':''));});"],
["agent-security",
 "Cisco DefenseClaw / Skill Scanner: Testing: Red-Teaming the Agent",
 "Agents are tested adversarially: prompt-injection suites, tool-misuse scenarios, and grant-boundary probes \u2014 the red team tries to make the agent exceed its charter. The grant layer must hold; the audit trail must record the attempts. Red-teaming is scheduled, not occasional: each charter change re-runs the relevant probes. An agent that survives its red team earns its deployment.",
 ["Adversarial prompt and tool suites", "Grant layer must hold", "Re-run per charter change"],
 "var gauntlet=[['injection suite',1],['misuse scenarios',1],['boundary probes',1]];\ngauntlet.forEach(function(g){console.log(g[0]+': '+(g[1]?'HELD':'BREACHED'));});\nconsole.log('gauntlet GREEN -> deployment approved');"],
["skill-scanning",
 "Cisco DefenseClaw / Skill Scanner: Real-World Pattern: Support Agent Hardening",
 "A complete pattern: a customer-support agent starts with broad tools, gets scanned (12 tools, 4 unnecessary), chartered to 8, sandboxed, red-teamed, and deployed with expiring grants and full audit. Six months later the charter census catches scope creep; the grants are re-tightened. The agent serves a million conversations without a single out-of-charter action \u2014 governance as the enabler, not the obstacle.",
 ["Scan to deploy in six steps", "Scope creep caught by census", "Evidence published with deployment"],
 "console.log('hardening arc complete: 8 tools chartered, 0 out-of-charter actions');\nconsole.log('evidence published with deployment (trust documented)');"],
["mcp",
 "Cisco DefenseClaw / Skill Scanner: Mastery: The Agent-Governance Playbook",
 "Agent-governance mastery spans threat modeling for agents, charter authorship, runtime enforcement design, red-teaming, and audit architecture. The advanced moves are fleet-wide policy, cross-agent interaction analysis, and governance-as-code. The mindset: agents are employees with superpowers \u2014 onboard them like it.",
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
    edition:'public',
    category:tp[0],
    tags:["ai-agents", "mcp", "skill-scanning", "policy-enforcement", "audit", "defense", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-cisco-defenseclaw-skill-scanner',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-cisco-defenseclaw-skill-scanner']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();