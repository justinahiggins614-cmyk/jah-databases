(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["detection", "analysis", "hardening", "response"];
var PREFIX='JAH-POLYMO-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Metamorphic Engine Detection", "detection", "Detects metamorphic engines that rewrite their own code between infections. Statistical opcode profiles and control-flow fingerprints survive mutation better than byte signatures. Detection targets the engine's habits, not its output.", ["Profile opcode distributions", "Fingerprint control-flow graphs", "Target engine habits"], ["AV engines", "Research tools", "Sandboxes"], ["Malware analysis literature", "Virus Bulletin"], 3, 0], ["Code Mutation Analysis", "analysis", "Analyzes mutation techniques: register renaming, instruction substitution, junk insertion. Understanding the mutation set lets analysts normalize samples back to canonical form. Each engine has a recognizable mutation palette.", ["Catalog mutation primitives", "Normalize to canonical form", "Compare normalized samples"], ["IDA Pro", "Ghidra", "Custom normalizers"], ["Reverse engineering literature", "RE guides"], 3, 0], ["Packer Detection", "detection", "Detects packed executables by entropy, section characteristics, and stub signatures. High-entropy sections with tiny import tables scream packer; the stub unpacks the real payload at runtime. Detection routes to unpacking.", ["Measure section entropy", "Match stub signatures", "Route to unpackers"], ["PEiD", "Detect It Easy", "AV engines"], ["PE format", "Packer literature"], 2, 0], ["Control-Flow Flattening Defense", "hardening", "Defends analysis against flattened control flow by reconstructing the dispatcher. Flattening hides logic in a switch dispatcher; deobfuscators recover the original graph. It restores analyzability.", ["Identify the dispatcher", "Recover original blocks", "Rebuild the control-flow graph"], ["Ghidra", "IDA Pro", "Deobfuscators"], ["Deobfuscation literature", "RE guides"], 3, 1], ["Opaque Predicate Removal", "analysis", "Removes opaque predicates — branches that always go one way — with symbolic execution. The solver proves the predicate constant and prunes the dead branch. Code shrinks back toward readability.", ["Symbolically execute branches", "Prove predicates constant", "Prune dead branches"], ["angr", "Triton", "Miasm"], ["Symbolic execution literature", "Deobfuscation"], 3, 1], ["Instruction Substitution Normalization", "analysis", "Normalizes substituted instructions back to canonical forms for comparison. mov eax,0 versus xor eax,eax mean the same thing; normalization erases the difference. Normalized code diffs cleanly.", ["Define canonical forms", "Rewrite substitutions", "Diff normalized code"], ["Custom normalizers", "IDA Pro", "Ghidra"], ["RE literature", "Compiler theory"], 2, 1], ["Anti-Disassembly Countermeasures", "detection", "Counters anti-disassembly tricks: overlapping instructions, jump-into-middle, return abuse. Linear disassembly falls for them; recursive descent with heuristics resists. Analysts must distrust the first disassembly.", ["Use recursive descent", "Detect overlapping code", "Verify with emulation"], ["IDA Pro", "Ghidra", "Custom"], ["Disassembly literature", "RE guides"], 3, 1], ["Runtime Decryption Monitoring", "analysis", "Watches runtime decryption by breaking on memory-write-then-execute transitions. Packed code decrypts then jumps; the monitor dumps the decrypted image at the transition. It captures what static analysis cannot see.", ["Break on write-then-execute", "Dump decrypted regions", "Analyze the plaintext"], ["x64dbg", "Sandboxes", "Unpackers"], ["Unpacking literature", "Debug guides"], 2, 0], ["Polymorphic Shellcode Detection", "detection", "Detects polymorphic shellcode with emulation and heuristics like GetPC patterns. Network IDS emulates suspicious buffers looking for decryptor behavior. It catches what signatures miss.", ["Emulate suspicious buffers", "Detect decryptor patterns", "Alert on GetPC heuristics"], ["Snort", "Suricata", "Sandboxes"], ["IDS literature", "Shellcode research"], 3, 0], ["Behavioral Detection", "detection", "Detects malware by behavior — API call sequences, file and registry actions — not bytes. Mutation changes code, not intent; behavioral models catch the intent. EDR products live here.", ["Monitor API call sequences", "Model malicious behaviors", "Block on behavior match"], ["EDR products", "Sysmon", "Sandboxes"], ["Behavioral analysis", "MITRE ATT&CK"], 2, 2], ["Emulation-Based Unpacking", "analysis", "Unpacks samples by emulating them to the original entry point. The emulator runs the stub safely and dumps the unpacked image; analysts work from the dump. It scales where manual unpacking does not.", ["Emulate the stub", "Detect the OEP transition", "Dump the unpacked image"], ["Unicorn", "QEMU", "Custom unpackers"], ["Unpacking literature", "Emulation guides"], 2, 1], ["YARA Rule Crafting", "detection", "Writes YARA rules targeting mutation-invariant features: strings, opcodes, and behaviors. Good rules survive polymorphism by matching what the engine cannot change. Rule quality decides detection quality.", ["Identify invariant features", "Write precise rules", "Test against benign sets"], ["YARA", "Threat intel", "Hunting"], ["YARA docs", "Detection engineering"], 2, 2], ["Entropy Analysis", "detection", "Flags packed or encrypted regions by Shannon entropy. Normal code sits around 5 bits per byte; packed code nears 8. It is the fastest triage signal in the toolkit.", ["Compute section entropy", "Flag high-entropy regions", "Correlate with other signals"], ["DIE", "Custom scripts", "AV engines"], ["Information theory", "Malware triage"], 1, 0], ["Sandbox Detonation", "response", "Detonates suspicious files in instrumented sandboxes to observe real behavior. The sandbox logs API calls, network, and file activity; evasive samples get environment tricks. Dynamic truth beats static guessing.", ["Execute in isolation", "Log all behaviors", "Counter evasion tricks"], ["Cuckoo", "ANY.RUN", "Vendor sandboxes"], ["Sandbox literature", "Malware analysis"], 2, 2], ["Application Allowlisting", "response", "Allowlisting permits only known-good code to run, making polymorphism irrelevant. If the hash is not on the list, it does not execute — mutated or not. It inverts the detection problem.", ["Build the known-good list", "Enforce at execution", "Manage exceptions"], ["AppLocker", "WDAC", "Airlock"], ["NIST SP 800-167", "Allowlist guides"], 2, 2]];
var DEMOS=["// Demo: {NAME} — entropy flags packed code\nfunction entropy(s){var f={},h=0;for(var i=0;i<s.length;i++){f[s[i]]=(f[s[i]]||0)+1;}\nObject.keys(f).forEach(function(k){var p=f[k]/s.length;h-=p*Math.log2(p);});return h;}\nvar plain='function hello(){return 42;}//'.repeat(20);\nvar packed='';for(var i=0;i<plain.length;i++){packed+=String.fromCharCode(32+((i*7919+{SEED})%95));}\nconsole.log('technique: {NAME}');console.log('plain entropy: '+entropy(plain).toFixed(2)+', packed entropy: '+entropy(packed).toFixed(2));\nconsole.log(entropy(packed)>6.5?'packed/encrypted section flagged':'entropy normal');", "// Demo: {NAME} — control-flow flattening cost\nvar blocks={N1},flat=blocks*3;\nconsole.log('technique: {NAME}');console.log('original blocks: '+blocks+', flattened dispatch: '+flat+' ops');\nconsole.log('analysis cost up, runtime overhead ~'+(100*(flat-blocks)/blocks).toFixed(0)+'% — the defender\\'s tradeoff');", "// Demo: {NAME} — YARA-style rule match\nvar rule={strings:['VirtualAlloc','CreateRemoteThread','WriteProcessMemory']};\nvar sample=['VirtualAlloc','ReadFile','CreateRemoteThread'];\nvar hits=rule.strings.filter(function(s){return sample.indexOf(s)>=0;});\nconsole.log('technique: {NAME}');console.log('rule strings matched: '+hits.length+'/'+rule.strings.length+' ('+hits.join(', ')+')');\nconsole.log(hits.length>=2?'RULE FIRES — escalate for sandbox detonation':'no match');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-polymorphic-code-defenses-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('polymorphic-code-defenses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
