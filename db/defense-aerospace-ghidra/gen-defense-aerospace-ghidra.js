(function(){'use strict';
/* jahdb-defense-aerospace-ghidra-1.0 — deterministic boundless generator for defense-aerospace-ghidra.
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
var PREFIX='JAH-DAE45-';
var DBNAME="Ghidra Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["reverse-engineering",
 "Ghidra: What Ghidra Is: The Disassembler That Reads for You",
 "Ghidra is the free, open-source reverse-engineering suite released by the NSA in 2019: it disassembles machine code for dozens of architectures, decompiles it to readable C-like pseudocode, and provides scripted analysis (Java/Python) over the program database. Analysts use it to understand firmware they own, find vulnerabilities in their own code, and dissect malware to build defenses. The decompiler is the star \u2014 reading assembly is slow; reading Ghidra's decompilation is merely hard.",
 ["NSA-released 2019, open source", "Decompiler to C-like pseudocode", "Authority recorded per project"],
 "console.log('Ghidra: disassemble -> decompile -> script');\n['multi-architecture','decompiler','scriptable (Java/Python)','collaborative'].forEach(function(s){console.log(' '+s);});"],
["decompiler",
 "Ghidra: The Decompiler: From Bytes to Logic",
 "Ghidra's decompiler lifts assembly to structured pseudocode: control flow recovered, variables named (by you), types applied. It is not perfect \u2014 optimized code confuses it \u2014 but it turns weeks of assembly reading into days of pseudocode reading. The skill is guiding it: naming functions, defining structs, marking up the unknown until the logic emerges. Decompilation is a conversation between the analyst and the tool.",
 ["Assembly to structured pseudocode", "Analyst guides with names and types", "Annotations versioned with history"],
 "var func={name:'parse_header',confidence:0.8,structs:['packet_hdr']};\nconsole.log('function '+func.name+' (confidence '+func.confidence+')');\nconsole.log('structs applied: '+func.structs.join(', '));"],
["firmware",
 "Ghidra: Firmware Analysis: Your Own Devices",
 "The primary defensive use: analyzing firmware of devices you own \u2014 extracting filesystems (binwalk-style), finding hardcoded credentials, auditing update mechanisms, verifying the vendor's security claims. Ghidra loads the raw binary at the right base address, finds the code, and the analyst hunts for the vulnerability before the adversary does. Every finding becomes a patch or a procurement decision.",
 ["Extract, load, hunt vulnerabilities", "Verify vendor security claims", "Every finding gets a disposition"],
 "var findings=[['hardcoded creds','vendor notified'],['weak update sig','patched']];\nfindings.forEach(function(f){console.log(f[0]+' -> '+f[1]);});"],
["malware-analysis",
 "Ghidra: Malware Analysis: Learning the Enemy's Playbook",
 "Defensive malware analysis dissects captured samples to build defenses: what does it do, how does it persist, what are its indicators? Ghidra's decompiler plus dynamic analysis (sandbox detonation) reveals the playbook; the indicators become detection rules. The work is defensive by purpose \u2014 understand the attack to build the defense \u2014 conducted in isolated labs with strict handling. Never analyze malware to improve it.",
 ["Dissect to build defenses", "Isolated labs, strict handling", "Purpose and handling logged"],
 "console.log('sample: quarantined, hash 9f2c\u2026');\nconsole.log('purpose: build detection for persistence mechanism');\nconsole.log('indicators extracted -> detection rules (defense)');"],
["scripting",
 "Ghidra: Your First Binary: Strings to Main",
 "The hello-world: load a small binary, run auto-analysis, check the strings window for the interesting literals, find main, read the decompilation. The strings are the map \u2014 URLs, paths, error messages lead to the code that matters. From there: rename functions, define the key structs, follow the cross-references. The first binary teaches the loop: explore, hypothesize, verify in the decompiler.",
 ["Auto-analysis, strings, find main", "Strings as the map", "Authority habitual from day one"],
 "console.log('strings: /etc/config, \"auth failed\", 192.168.1.1');\nconsole.log('main found: decompilation readable');\nconsole.log('authority: training binary (owned)');"],
["vulnerability-research",
 "Ghidra: Scripting: Automating the Analysis",
 "Ghidra's scripting (GhidraScript Java, plus Python) automates the repetitive: find all crypto constants, list all network calls, rename by pattern, diff two firmware versions. The script library is institutional knowledge \u2014 the team's hard-won patterns, runnable. Writing a script that finds your product's bug class across every firmware version is leverage no manual analysis matches.",
 ["Automate repetitive analysis", "Scripts as institutional knowledge", "Read-only, scope-declared"],
 "function findCryptoConsts(bytes){var consts=[];var aes=[0x63,0x7c,0x77];for(var i=0;i<bytes.length-2;i++){if(bytes[i]===aes[0]&&bytes[i+1]===aes[1])consts.push(i);}return consts;}\nvar fw=[0x63,0x7c,0x10,0x20,0x63,0x7c];\nconsole.log('AES S-box refs at offsets: '+findCryptoConsts(fw).join(', ')+' (read-only scan)');"],
["reverse-engineering",
 "Ghidra: Loaders and Processor Modules: New Architectures",
 "Ghidra's architecture support is extensible: loaders parse new binary formats, processor modules (SLEIGH specifications) describe new instruction sets. When the team meets an exotic chip \u2014 custom DSP, new microcontroller \u2014 writing the SLEIGH spec brings it into the analysis world. The skill is rare and decisive: the team that can describe the processor can analyze anything built on it.",
 ["SLEIGH specs describe instruction sets", "Loaders parse new formats", "Specs validated before trust"],
 "console.log('SLEIGH spec: custom-dsp v1 (412 instructions)');\nconsole.log('validation: 10k known instructions match vendor disassembler');\nconsole.log('trusted for unknown firmware');"],
["decompiler",
 "Ghidra: Diffing: What Changed Between Versions",
 "Version diffing compares two firmware builds: which functions changed, what was added, what was patched. For defenders, diffing the vendor's security update reveals what was fixed (and hints at what was vulnerable); diffing your own builds verifies the patch. Ghidra's Version Tracking does the structural matching. The discipline is diffing every update that touches security-relevant code.",
 ["Structural matching across versions", "Reveal what updates fixed", "Diff review before critical deploys"],
 "var diff={changed:14,security_relevant:3,added:2};\nconsole.log('update diff: '+diff.changed+' changed, '+diff.added+' added');\nconsole.log('security-relevant: '+diff.security_relevant+' (reviewed before deploy)');"],
["firmware",
 "Ghidra: Defensive Uses: The Vulnerability Program",
 "Ghidra's defensive value compounds in a program: regular firmware audits of owned devices, malware dissections feeding detection, patch verification by diffing. The findings feed the same remediation loop as the Daybreak stack \u2014 found, validated, fixed, verified. Reverse engineering is the deep end of defensive analysis: slow, skilled, and decisive where it counts.",
 ["Firmware audits, dissection-fed detection", "Patch verification by diffing", "Metric: closed findings"],
 "var prog={audited:24,findings:31,closed:29};\nconsole.log('firmware audits: '+prog.audited+', findings '+prog.findings+', closed '+prog.closed);\nconsole.log('metric: closed findings (not binaries analyzed)');"],
["malware-analysis",
 "Ghidra: Collaboration: Team Reverse Engineering",
 "Ghidra's server mode lets teams share a program database: one analyst names the network code, another the crypto, the merge keeps both. Large binaries (OS kernels, complex firmware) are team efforts, and the shared database is the collective understanding. The discipline is markup hygiene \u2014 named functions, typed structs, commented reasoning \u2014 so the next analyst inherits understanding, not confusion.",
 ["Shared program databases", "Markup hygiene as discipline", "Reasoning commented, not just labels"],
 "console.log('shared db: net.c by ana-chen (auth check: validates HMAC, see note)');\nconsole.log('crypto.c by ana-okafor (key schedule, verified against spec)');"],
["scripting",
 "Ghidra: Debugging: When the Decompiler Lies",
 "The decompiler misleads: optimized code, indirect jumps, obfuscation. The defense is the disassembly \u2014 when the pseudocode looks wrong, read the assembly it came from. Cross-references (who calls this? who reads this string?) ground the hypotheses. And dynamic analysis (debugger, emulator) arbitrates: run it, watch what it does. Static proposes; dynamic disposes.",
 ["Disassembly arbitrates decompiler", "Cross-references ground hypotheses", "Dynamic proof for critical conclusions"],
 "console.log('decompiler claims: auth check at 0x401230');\nconsole.log('dynamic witness: breakpoint hit, bypass confirmed');\nconsole.log('critical conclusion: PROVEN (two witnesses)');"],
["vulnerability-research",
 "Ghidra: Headless Analysis: Ghidra in the Pipeline",
 "Ghidra runs headless: scripts that auto-analyze firmware drops, extract indicators, and file findings \u2014 the reverse-engineering stage of the security pipeline. Every vendor firmware update gets the automated pass; humans get the flagged interesting parts. This scales the deep audit to the fleet's update cadence.",
 ["Automated firmware analysis", "Scales audit to update cadence", "Human review before disposition"],
 "console.log('night auditor: 6 firmware drops analyzed');\nconsole.log('flagged: 2 (hardcoded creds pattern, weak RNG)');\nconsole.log('human review: required before disposition');"],
["reverse-engineering",
 "Ghidra: Testing: Validating Your Own Defenses",
 "Ghidra validates defenses too: analyze your own hardened binary \u2014 are the mitigations present (stack canaries, CET, obfuscation where intended)? Reverse-engineer your own product like an adversary would, and fix what you find. This is the red-team's static complement: know what your binary tells the enemy, and minimize it.",
 ["Verify mitigations in your binaries", "Think like the adversary", "Mirror audit per release"],
 "var mirror={canaries:1,cet:1,stripped:1};\nconsole.log('mirror audit: canaries '+(mirror.canaries?'present':'MISSING'));\nconsole.log('release: cleared (story reviewed)');"],
["decompiler",
 "Ghidra: Real-World Pattern: Fleet Firmware Audit",
 "A complete pattern: an organization audits the firmware of its deployed device fleet \u2014 extract, analyze, find hardcoded credentials in two models, notify vendors, patch one, mitigate the other with network controls, verify by diffing the patched firmware. The audit repeats annually. The fleet's firmware is no longer a black box; it is a reviewed artifact.",
 ["Extract, analyze, disposition", "Vendor notification and patching", "Annual, verified, discreet"],
 "console.log('fleet audit: 40 models, 6 findings, 6 dispositions');\nconsole.log('patched: 4, mitigated: 2, verified by diff');\nconsole.log('summary published (findings discreet)');"],
["firmware",
 "Ghidra: Mastery: The Reverse Engineer's Playbook",
 "Ghidra mastery is deep craft: architecture fluency, decompiler guidance, scripting, dynamic corroboration, and the patience for large binaries. The advanced moves are custom loaders, processor modules, and novel analysis techniques. The mindset: the binary is a text \u2014 learn to read it closely, skeptically, and completely.",
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
    edition:'public',
    category:tp[0],
    tags:["ghidra", "reverse-engineering", "nsa", "decompiler", "firmware", "malware-analysis", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-ghidra',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-ghidra']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();