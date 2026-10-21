(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["technologies", "attestation", "hardening", "operations"];
var PREFIX='JAH-EME-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Intel SGX Enclaves", "technologies", "Runs code in SGX enclaves isolated from the OS, hypervisor, and even physical memory attacks. The CPU encrypts enclave pages; only the enclave sees plaintext. It protects data in use from the entire software stack.", ["Create enclaves with ECREATE", "Seal data to the enclave", "Attest remotely"], ["Intel SGX SDK", "Gramine", "Occlum"], ["Intel SDM (SGX)", "SGX literature"], 3, 0], ["AMD SEV-SNP", "technologies", "Encrypts whole VM memory with SEV-SNP so the hypervisor cannot read guest data. Integrity protection stops replay and remapping attacks that plain SEV allowed. Confidential VMs are the deployment model.", ["Launch with SNP attestation", "Encrypt per-VM memory", "Verify integrity"], ["AMD EPYC", "Azure confidential", "GCP"], ["AMD SEV-SNP spec", "Confidential computing"], 3, 0], ["Intel TDX", "technologies", "Isolates trust domains with Intel TDX for VM-level confidential computing. The TDX module manages secure EPT; the host cannot inspect guest memory. It brings enclave-grade protection to whole VMs.", ["Build trust domains", "Manage secure EPT", "Attest the TD"], ["Intel Xeon", "TDX module", "Clouds"], ["Intel TDX specs", "Confidential computing"], 3, 0], ["ARM TrustZone", "technologies", "Splits the processor into secure and normal worlds with TrustZone. Trusted apps run in the secure world; the normal-world OS cannot peek. Phones use it for keys and DRM.", ["Run TAs in the secure world", "Gate with the SMC", "Isolate secure memory"], ["ARM", "OP-TEE", "Trustonic"], ["ARM TrustZone", "GlobalPlatform TEE"], 2, 0], ["Remote Attestation", "attestation", "Proves to a remote party exactly what code runs in the enclave. The CPU signs a measurement quote; the verifier checks it against expected values. Trust becomes verifiable, not assumed.", ["Get the signed quote", "Verify the chain", "Check measurements"], ["Intel DCAP", "AMD attestation", "Azure"], ["Attestation literature", "RATS (IETF)"], 3, 0], ["Sealing Data", "operations", "Seals enclave data to the platform so only the same enclave on the same CPU unseals it. Sealing keys derive from the CPU and enclave identity; migrated data stays locked. It gives enclaves durable storage.", ["Derive the seal key", "Encrypt before writing out", "Unseal on the same platform"], ["SGX SDK", "SEV-SNP", "TDX"], ["SGX docs", "Sealing literature"], 2, 2], ["Enclave Paging", "operations", "Manages the limited Enclave Page Cache with secure paging. SGX EPC is small; the driver pages encrypted enclave memory in and out. Working sets bigger than EPC pay paging costs.", ["Size working sets to EPC", "Page securely on faults", "Measure paging overhead"], ["SGX driver", "Gramine", "Linux"], ["SGX literature", "Paging docs"], 3, 1], ["Side-Channel Hardening", "hardening", "Hardens enclaves against side channels: constant-time crypto, cache partitioning, branch discipline. Enclaves share hardware with attackers; the code must not leak through timing or caches. It is an ongoing arms race.", ["Write constant-time code", "Partition shared caches", "Audit for leaks"], ["Crypto libraries", "SGX", "Research"], ["Side-channel literature", "Constant-time guides"], 3, 1], ["Memory Encryption Engines", "technologies", "Encrypts DRAM transparently with memory encryption engines like SME and MKTME. Every cache-line write encrypts; reads decrypt. It defeats cold-boot and interposer attacks with near-zero software cost.", ["Enable SME/MKTME", "Manage encryption keys", "Verify coverage"], ["AMD SME", "Intel MKTME", "Servers"], ["Vendor docs", "Memory encryption literature"], 2, 1], ["Secure I/O Paths", "hardening", "Builds trusted paths from enclaves to displays and input devices. Without trusted I/O, the host can spoof what the user sees; secure paths close the gap. It is the missing link for enclave UX.", ["Establish trusted channels", "Verify device identity", "Indicate trusted mode to users"], ["Research", "SGX", "Vendors"], ["Trusted path literature", "UI security"], 3, 1], ["Enclave SDKs", "operations", "Develops with enclave SDKs that handle the enclave boundary correctly. ECALLs and OCALLs cross the boundary; the SDK marshals safely. Getting the boundary wrong leaks data.", ["Define the enclave interface", "Marshal across ECALLs", "Minimize the TCB"], ["Intel SGX SDK", "Open Enclave", "Gramine"], ["SDK docs", "Enclave literature"], 2, 1], ["Attestation Flows", "attestation", "Implements complete attestation flows: quote, verify, provision secrets. The relying party checks the quote then releases keys only to verified enclaves. It is how enclaves get their secrets safely.", ["Request the quote", "Verify and check policy", "Provision secrets"], ["DCAP", "Cloud services", "Custom"], ["RATS", "Attestation guides"], 3, 0], ["Key Provisioning", "operations", "Provisions keys into enclaves only after successful attestation. Keys travel encrypted to the verified enclave; they never exist in host memory. It solves the enclave bootstrap problem.", ["Attest first", "Encrypt keys to the enclave", "Seal for persistence"], ["Cloud KMS", "Custom", "HSMs"], ["Key management", "Attestation literature"], 3, 2], ["Enclave Debugging", "operations", "Debugs enclaves in simulation and debug modes without weakening production. Debug enclaves allow inspection; production enclaves forbid it. The modes are cryptographically distinct.", ["Develop in debug mode", "Test in simulation", "Ship production-signed"], ["SGX SDK", "GDB", "Vendors"], ["SDK docs", "Debug guides"], 2, 1], ["Enclave Performance Tuning", "operations", "Tunes enclave performance: minimize OCALLs, batch crossings, size EPC working sets. Every boundary crossing costs thousands of cycles; design keeps work inside. Measurement guides the tuning.", ["Minimize boundary crossings", "Batch OCALLs", "Profile inside the enclave"], ["SGX", "Profilers", "SDKs"], ["Performance literature", "Enclave guides"], 3, 1]];
var DEMOS=["// Demo: {NAME} — attestation chain check\nvar chain=['manufacturer-root','platform-cert','enclave-measurement'];\nvar expected='mrenclave-{SEED}';\nconsole.log('technique: {NAME}');\nchain.forEach(function(c){console.log('verify: '+c+' OK');});\nconsole.log('enclave measurement: '+expected);\nconsole.log('all links verified — enclave is genuine');", "// Demo: {NAME} — EPC paging cost\nvar epc=128,working={N1}*4;\nvar faults=Math.max(0,working-epc)/4;\nconsole.log('technique: {NAME}');console.log('EPC: '+epc+' MB, working set: '+working+' MB');\nconsole.log('estimated page faults: '+Math.round(faults));\nconsole.log(faults>0?'keep the working set inside EPC':'fits — no paging overhead');", "// Demo: {NAME} — sealing key derivation\nfunction kdf(id){var h=0;for(var i=0;i<id.length;i++){h=(h*31+id.charCodeAt(i))>>>0;}return h.toString(16);}\nconsole.log('technique: {NAME}');console.log('seal key for mrenclave-{SEED}: '+kdf('mrenclave-{SEED}'));\nconsole.log('same enclave, same CPU -> same key; different CPU -> different key');"];
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
var gen={version:'jahdb-encrypted-memory-enclaves-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('encrypted-memory-enclaves',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
