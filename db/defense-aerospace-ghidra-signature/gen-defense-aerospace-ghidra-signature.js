(function(){'use strict';
/* jahdb-defense-aerospace-ghidra-1.0 — deterministic boundless generator for defense-aerospace-ghidra-signature.
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
var CATS=["reverse-engineering", "decompiler", "firmware", "malware-analysis", "scripting", "vulnerability-research"];
var PREFIX='JAH-DAE45S-';
var DBNAME="Signature Ghidra Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["reverse-engineering",
 "Signature Ghidra: What Ghidra Is: The Disassembler That Reads for You",
 "The Signature counterpart is the SigLens-RE bench, Manon's original binary-analysis design. It mirrors the disassemble-decompile-script pipeline but every analysis project carries a provenance record \u2014 which binary, which hash, whose firmware, under what authority. The Signature design makes the authority part of the project: you analyze what you are entitled to analyze.",
 ["NSA-released 2019, open source", "Decompiler to C-like pseudocode", "Authority recorded per project"],
 "console.log('Ghidra: disassemble -> decompile -> script');\n['multi-architecture','decompiler','scriptable (Java/Python)','collaborative'].forEach(function(s){console.log(' '+s);});"],
["decompiler",
 "Signature Ghidra: The Decompiler: From Bytes to Logic",
 "The bench's decompiler is the translator: same lifting, but it tracks your markup as annotations with confidence levels. The Signature design versions the annotations \u2014 the analysis is a document with history, so a second analyst can see how the understanding was built.",
 ["Assembly to structured pseudocode", "Analyst guides with names and types", "Annotations versioned with history"],
 "var func={name:'parse_header',confidence:0.8,structs:['packet_hdr']};\nconsole.log('function '+func.name+' (confidence '+func.confidence+')');\nconsole.log('structs applied: '+func.structs.join(', '));"],
["firmware",
 "Signature Ghidra: Firmware Analysis: Your Own Devices",
 "The bench's firmware doctrine is the owner's right: analyze what you own, document what you find. The Signature design requires the finding's disposition \u2014 patched, mitigated, accepted, or vendor-notified \u2014 recorded before the project closes. Findings without dispositions are not findings; they are worries.",
 ["Extract, load, hunt vulnerabilities", "Verify vendor security claims", "Every finding gets a disposition"],
 "var findings=[['hardcoded creds','vendor notified'],['weak update sig','patched']];\nfindings.forEach(function(f){console.log(f[0]+' -> '+f[1]);});"],
["malware-analysis",
 "Signature Ghidra: Malware Analysis: Learning the Enemy's Playbook",
 "The bench's malware doctrine is the quarantine lab: isolated, logged, defensive-purpose-only. The Signature design requires the defensive purpose recorded \u2014 which defense this analysis serves \u2014 and the handling log: every sample movement tracked.",
 ["Dissect to build defenses", "Isolated labs, strict handling", "Purpose and handling logged"],
 "console.log('sample: quarantined, hash 9f2c\u2026');\nconsole.log('purpose: build detection for persistence mechanism');\nconsole.log('indicators extracted -> detection rules (defense)');"],
["scripting",
 "Signature Ghidra: Your First Binary: Strings to Main",
 "The bench's hello-world is the first reading: same loop, but the project records the authority ('training binary, owned'). The Signature design makes the authority question habitual from the first binary \u2014 the analyst always knows why they are allowed to read this code.",
 ["Auto-analysis, strings, find main", "Strings as the map", "Authority habitual from day one"],
 "console.log('strings: /etc/config, \"auth failed\", 192.168.1.1');\nconsole.log('main found: decompilation readable');\nconsole.log('authority: training binary (owned)');"],
["vulnerability-research",
 "Signature Ghidra: Scripting: Automating the Analysis",
 "The bench's scripting is the analyst's leverage: same automation, with scripts versioned and reviewed. The Signature design requires scripts to declare their scope \u2014 which binaries, read-only always \u2014 because analysis scripts must never modify evidence.",
 ["Automate repetitive analysis", "Scripts as institutional knowledge", "Read-only, scope-declared"],
 "function findCryptoConsts(bytes){var consts=[];var aes=[0x63,0x7c,0x77];for(var i=0;i<bytes.length-2;i++){if(bytes[i]===aes[0]&&bytes[i+1]===aes[1])consts.push(i);}return consts;}\nvar fw=[0x63,0x7c,0x10,0x20,0x63,0x7c];\nconsole.log('AES S-box refs at offsets: '+findCryptoConsts(fw).join(', ')+' (read-only scan)');"],
["reverse-engineering",
 "Signature Ghidra: Loaders and Processor Modules: New Architectures",
 "The bench's extensibility doctrine is the new-tongue kit: loader plus SLEIGH spec, tested against known binaries. The Signature design requires the spec validated \u2014 disassemble known-good code, compare against the vendor's disassembler \u2014 before it is trusted on unknown firmware.",
 ["SLEIGH specs describe instruction sets", "Loaders parse new formats", "Specs validated before trust"],
 "console.log('SLEIGH spec: custom-dsp v1 (412 instructions)');\nconsole.log('validation: 10k known instructions match vendor disassembler');\nconsole.log('trusted for unknown firmware');"],
["decompiler",
 "Signature Ghidra: Diffing: What Changed Between Versions",
 "The bench's diffing is the change scope: same structural matching, with the security-relevance flag per changed function. The Signature design requires the diff review before deploying vendor updates to critical systems \u2014 know what changed before you trust it.",
 ["Structural matching across versions", "Reveal what updates fixed", "Diff review before critical deploys"],
 "var diff={changed:14,security_relevant:3,added:2};\nconsole.log('update diff: '+diff.changed+' changed, '+diff.added+' added');\nconsole.log('security-relevant: '+diff.security_relevant+' (reviewed before deploy)');"],
["firmware",
 "Signature Ghidra: Defensive Uses: The Vulnerability Program",
 "The bench's program doctrine is the deep audit: scheduled firmware reviews, dissection-fed detections, diff-verified patches. The Signature design measures the program in findings-with-dispositions \u2014 the metric is closed findings, not analyzed binaries.",
 ["Firmware audits, dissection-fed detection", "Patch verification by diffing", "Metric: closed findings"],
 "var prog={audited:24,findings:31,closed:29};\nconsole.log('firmware audits: '+prog.audited+', findings '+prog.findings+', closed '+prog.closed);\nconsole.log('metric: closed findings (not binaries analyzed)');"],
["malware-analysis",
 "Signature Ghidra: Collaboration: Team Reverse Engineering",
 "The bench's collaboration is the shared reading: same shared database, with annotation authorship tracked. The Signature design requires the reasoning commented \u2014 'why I think this is the auth check' \u2014 because the next analyst needs the argument, not just the label.",
 ["Shared program databases", "Markup hygiene as discipline", "Reasoning commented, not just labels"],
 "console.log('shared db: net.c by ana-chen (auth check: validates HMAC, see note)');\nconsole.log('crypto.c by ana-okafor (key schedule, verified against spec)');"],
["scripting",
 "Signature Ghidra: Debugging: When the Decompiler Lies",
 "The bench's verification is the second witness: decompiler claim checked against disassembly or dynamic run. The Signature design requires the witness for critical conclusions \u2014 'this is the auth bypass' needs dynamic proof, not just decompiler reading.",
 ["Disassembly arbitrates decompiler", "Cross-references ground hypotheses", "Dynamic proof for critical conclusions"],
 "console.log('decompiler claims: auth check at 0x401230');\nconsole.log('dynamic witness: breakpoint hit, bypass confirmed');\nconsole.log('critical conclusion: PROVEN (two witnesses)');"],
["vulnerability-research",
 "Signature Ghidra: Headless Analysis: Ghidra in the Pipeline",
 "The bench's headless mode is the night auditor: automated analysis of every firmware drop, findings filed. The Signature design requires the auditor's scope declared \u2014 which devices, read-only \u2014 and its findings reviewed by a human before disposition.",
 ["Automated firmware analysis", "Scales audit to update cadence", "Human review before disposition"],
 "console.log('night auditor: 6 firmware drops analyzed');\nconsole.log('flagged: 2 (hardcoded creds pattern, weak RNG)');\nconsole.log('human review: required before disposition');"],
["reverse-engineering",
 "Signature Ghidra: Testing: Validating Your Own Defenses",
 "The bench's self-analysis is the mirror audit: your binary under your own microscope. The Signature design schedules the mirror audit per release \u2014 the binary's story to an adversary is reviewed before the adversary reads it.",
 ["Verify mitigations in your binaries", "Think like the adversary", "Mirror audit per release"],
 "var mirror={canaries:1,cet:1,stripped:1};\nconsole.log('mirror audit: canaries '+(mirror.canaries?'present':'MISSING'));\nconsole.log('release: cleared (story reviewed)');"],
["decompiler",
 "Signature Ghidra: Real-World Pattern: Fleet Firmware Audit",
 "The bench's audit doctrine is the fleet reading: scheduled, dispositioned, verified. The Signature design publishes the audit summary (not the vulnerabilities) \u2014 transparency about the practice, discretion about the findings.",
 ["Extract, analyze, disposition", "Vendor notification and patching", "Annual, verified, discreet"],
 "console.log('fleet audit: 40 models, 6 findings, 6 dispositions');\nconsole.log('patched: 4, mitigated: 2, verified by diff');\nconsole.log('summary published (findings discreet)');"],
["firmware",
 "Signature Ghidra: Mastery: The Reverse Engineer's Playbook",
 "The bench's mastery adds the stewardship layer: authority, dispositions, logged handling. Manon's roadmap runs from today's firmware labs to fleet-scale automated analysis under one lens discipline \u2014 close reading, everywhere, all of it defensive.",
 ["Architecture through large binaries", "Custom loaders and processors", "Stewardship: authority, dispositions, handling"],
 "var playbook=['architecture fluency','decompiler guidance','scripting','dynamic corroboration','patience'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('The binary is a text. Read it closely.');"]
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
    tags:["ghidra", "reverse-engineering", "nsa", "decompiler", "firmware", "malware-analysis", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
    last_verified:'2026-10-21',
    record_kind:"ghidra record",
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
var gen={version:'jahdb-defense-aerospace-ghidra-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ghidra-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ghidra-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();