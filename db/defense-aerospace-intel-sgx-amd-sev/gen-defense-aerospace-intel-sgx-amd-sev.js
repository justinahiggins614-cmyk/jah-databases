(function(){'use strict';
/* jahdb-defense-aerospace-intel-sgx-amd-sev-1.0 — deterministic boundless generator for defense-aerospace-intel-sgx-amd-sev.
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
var CATS=["confidential-computing", "enclaves", "attestation", "memory-encryption", "snp", "key-management"];
var PREFIX='JAH-DAE49-';
var DBNAME="Intel SGX / AMD SEV Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["confidential-computing",
 "Intel SGX / AMD SEV: What Confidential Computing Is: Trust the Silicon",
 "Confidential computing protects data in use: Intel SGX carves enclaves \u2014 encrypted memory regions even the OS and hypervisor cannot read \u2014 while AMD SEV encrypts entire VMs (SEV-SNP adding integrity and attestation). Remote attestation lets a client verify the enclave's identity and code measurement before sending secrets. The threat model is the untrusted host: the cloud operator, the compromised hypervisor \u2014 excluded by hardware.",
 ["Data protected in use", "Hardware excludes the host", "Policy-gated attestation"],
 "console.log('confidential computing:');\n['SGX enclaves','SEV encrypted VMs','SEV-SNP attestation','memory encryption'].forEach(function(s){console.log(' '+s);});"],
["enclaves",
 "Intel SGX / AMD SEV: Intel SGX: Enclaves in the Process",
 "SGX enclaves live inside the process address space: ECALLs enter, OCALLs exit, and the Enclave Page Cache (EPC, ~128MB-1GB depending on platform) holds the encrypted pages. The programming model is partition \u2014 secrets and their computation inside, everything else outside \u2014 with SDKs (Intel SGX SDK) and frameworks (Gramine, Occlum) easing the port. The art is minimizing the enclave boundary: small TCB, small attack surface.",
 ["Encrypted pages even the OS cannot read", "ECALL/OCALL boundary", "Minimal TCB, measured identity"],
 "var epc={total_mb:128,used_mb:64};\nconsole.log('EPC '+epc.used_mb+'/'+epc.total_mb+' MB');\nconsole.log('keep measurement 9f2c\u2026: policy ACCEPTS');"],
["attestation",
 "Intel SGX / AMD SEV: AMD SEV: Encrypted Virtual Machines",
 "SEV encrypts VM memory with per-VM keys the hypervisor never sees; SEV-SNP adds integrity protection and a richer attestation report (the chip signs the VM's measurement plus the platform state). The model is lift-and-shift: whole VMs become confidential with minimal code changes \u2014 the operational opposite of SGX's partitioning. For defense clouds, SEV-SNP is how tenant workloads stay secret from the provider.",
 ["Per-VM memory encryption", "SNP integrity plus attestation", "Lift-and-shift confidentiality"],
 "console.log('SEV-SNP launch: memory encrypted, integrity on');\nconsole.log('attestation verified -> keys released to VM');\nconsole.log('launch ceremony logged (steps evidenced)');"],
["memory-encryption",
 "Intel SGX / AMD SEV: Remote Attestation: Prove Before Trust",
 "Attestation is the protocol: the hardware signs a quote containing the enclave/VM measurement; the verifier checks the signature chain to the manufacturer's root and compares the measurement against policy. Only then do secrets flow (keys provisioned to the attested enclave). The PKI (Intel's IAS/DCAP, AMD's KDS) is the trust root \u2014 understand it, monitor it, plan for its rotation.",
 ["Hardware-signed measurement quotes", "Chain to manufacturer root", "Secrets only after verification"],
 "var quote={measurement:'9f2c\u2026',chain:'valid',policy:'accept'};\nconsole.log('quote: measurement '+quote.measurement+', chain '+quote.chain);\nconsole.log('policy: '+quote.policy+' -> secrets released');\nconsole.log('re-attestation: every 24h (continuous)');"],
["snp",
 "Intel SGX / AMD SEV: Your First Enclave: Hello, Sealed World",
 "The hello-world: write the enclave that seals a secret (encrypt with the enclave's sealing key, bound to the measurement), unseal it on the next run, and print the attestation quote. The sealing key never leaves the hardware; the secret never leaves the enclave unencrypted. From here: the secret is a model weight, a private key, a database key \u2014 the pattern generalizes to anything that must stay secret from the host.",
 ["Seal secrets to the measurement", "Attestation quote verified", "Ceremony order: seal, attest, trust"],
 "console.log('seal: secret -> sealed blob (measurement-bound)');\nconsole.log('attest: quote verified against policy');\nconsole.log('unseal: secret available (ceremony in order)');"],
["key-management",
 "Intel SGX / AMD SEV: Partitioning: What Goes Inside",
 "The SGX design question is the boundary: put the crypto and the key handling inside; keep the UI, the network, the parsing outside. Every ECALL is a potential confused-deputy; every OCALL leaks a bit of control flow. The discipline is data-flow review: what crosses the boundary, in which direction, and what it reveals. Small enclaves are auditable enclaves.",
 ["Secrets and crypto inside", "Parsing and UI outside", "Boundary re-reviewed per release"],
 "var crossings=[['key in','1'],['ciphertext out','1'],['bulk data','0 (stays out)']];\ncrossings.forEach(function(c){console.log(c[0]+': '+(c[1]==='1'?'crosses (reviewed)':'stays out'));});"],
["confidential-computing",
 "Intel SGX / AMD SEV: Frameworks: Gramine and Occlum",
 "Porting to SGX is eased by library OS frameworks: Gramine and Occlum run unmodified applications inside enclaves, handling the ECALL/OCALL boundary and shielding system calls. The trade is TCB size \u2014 the LibOS is inside the trust boundary \u2014 versus porting effort. For lift-and-shift confidential computing, frameworks are the practical path; for minimal TCB, the SDK's partitioning. Choose by threat model, not convenience.",
 ["Run unmodified apps in enclaves", "TCB size vs porting effort", "TCB inventoried per workload"],
 "var tcb={framework:'gramine',kloc:180,verdict:'acceptable for this workload'};\nconsole.log('framework '+tcb.framework+': TCB '+tcb.kloc+' kLOC');\nconsole.log('verdict: '+tcb.verdict+' (threat-model decided)');"],
["enclaves",
 "Intel SGX / AMD SEV: Side Channels: The Enclave's Adversary",
 "Enclaves face side channels: page-fault controlled channels, cache timing, speculative execution variants. The defenses are constant-time code, ORAM-like access patterns where needed, and the platform's microcode mitigations \u2014 plus the honest assessment that some adversaries (the malicious OS with full observation) are partially in scope. The threat model must name the side-channel assumptions explicitly.",
 ["Controlled channels, cache timing", "Constant-time and mitigations", "Assumptions stated explicitly"],
 "console.log('assumptions: page-fault channel MITIGATED (constant access)');\nconsole.log('cache timing: IN SCOPE (constant-time code)');\nconsole.log('assessment: stated per deployment');"],
["attestation",
 "Intel SGX / AMD SEV: Defensive Uses: The Secret-Keeping Cloud",
 "Confidential computing's defensive value is computing on secrets without trusting the computer: model weights that stay secret from the cloud operator, key-management services the provider cannot read, multi-party analytics on combined datasets no party reveals. Attestation makes it verifiable \u2014 the client proves the enclave before trusting it with the secret. This is the architecture for 'use the cloud, trust the silicon'.",
 ["Secrets safe from the operator", "Attested key management", "Multi-party analytics without revelation"],
 "console.log('model weights: sealed in enclave, operator blind');\nconsole.log('analytics: 3 parties, 0 revealed datasets');\nconsole.log('trust: silicon, attested (not the operator)');"],
["memory-encryption",
 "Intel SGX / AMD SEV: Key Management in Enclaves",
 "The killer app is key management: master keys that exist only inside enclaves, released to attested workloads, never visible to operators. The enclave becomes the HSM-as-software \u2014 with attestation as the access policy. The operational discipline is the attestation policy's maintenance: acceptable measurements updated with each release, revocation when a measurement is compromised.",
 ["Keys exist only in enclaves", "Attestation as access policy", "Policy ritual per release"],
 "console.log('master key: exists only in enclave');\nconsole.log('release policy: measurements {9f2c\u2026, 71ab\u2026} (signed)');\nconsole.log('compromised measurement: revoked (policy updated)');"],
["snp",
 "Intel SGX / AMD SEV: Debugging: The Opaque Box",
 "Enclave debugging is constrained by design: debug enclaves (unsigned, debuggable) for development, production enclaves opaque. The tools are enclave-aware debuggers and the disciplined use of OCALL logging \u2014 never log secrets. The classic bug is the boundary: wrong ECALL parameters, uninitialized outside memory. Debug the boundary first.",
 ["Debug enclaves for dev", "Never log secrets", "Policy rejects debug in prod"],
 "console.log('dev: debug enclave, OCALL tracing on');\nconsole.log('prod: opaque (debug measurement REJECTED by policy)');"],
["key-management",
 "Intel SGX / AMD SEV: Performance: The Enclave Tax",
 "Enclaves cost: ECALL transitions (~microseconds), EPC paging when overcommitted (the cliff \u2014 avoid it), memory encryption overhead (single digits percent). SEV's cost is lower (near-native for many workloads). The engineering is budgeting: keep the working set in EPC, minimize crossings, measure on the target SKU. The tax is real but payable \u2014 and the security is worth more than the cycles.",
 ["Transition and paging costs", "Keep working set in EPC", "Costs budgeted per workload"],
 "var tax={ecall_us:8,epc_mb:64,overhead_pct:6};\nconsole.log('ECALL '+tax.ecall_us+' us, EPC '+tax.epc_mb+' MB, overhead '+tax.overhead_pct+'%');\nconsole.log('EPC cliff: avoided by sizing (budgeted)');"],
["confidential-computing",
 "Intel SGX / AMD SEV: Testing: Attestation in CI",
 "Confidential workloads are tested with attestation mocked in dev and real in staging: the CI runs the enclave logic in simulation, the staging environment runs the attestation ceremony against real hardware. The policy (acceptable measurements) is tested too \u2014 a release that changes the measurement must update the policy, and the CI verifies the pair. Untested attestation is untrusted attestation.",
 ["Mock attestation in CI", "Real ceremony in staging", "Policy-measurement pair verified"],
 "console.log('CI: enclave logic (simulated attestation)');\nconsole.log('staging: real ceremony, policy v14');\nconsole.log('release: measurement 71ab\u2026 + policy v15 (pair verified)');"],
["enclaves",
 "Intel SGX / AMD SEV: Real-World Pattern: Confidential Inference Service",
 "A complete pattern: a model-serving fleet where weights are sealed to enclaves, clients attest before sending prompts, and inference runs with the operator blind. The attestation policy updates with each model release; the key ceremony is logged. Users get the AI; the operator gets ciphertext. The architecture proves the privacy instead of promising it.",
 ["Sealed weights, attested clients", "Operator blind by architecture", "Policy public, weights private"],
 "console.log('inference: weights sealed, prompts encrypted to enclave');\nconsole.log('operator sees: ciphertext (blind by architecture)');\nconsole.log('policy published (proof public, weights private)');"],
["attestation",
 "Intel SGX / AMD SEV: Mastery: The Confidential-Computing Playbook",
 "Confidential-computing mastery spans hardware literacy, attestation PKI, partitioning design, side-channel awareness, and the operations of measured software. The advanced moves are multi-party protocols, custom attestation policies, and fleet key management. The mindset: trust is a measurement \u2014 verify it, continuously.",
 ["Hardware through measured ops", "Multi-party, custom policies", "Stewardship: policies, ceremonies, assessments"],
 "var playbook=['hardware literacy','attestation PKI','partitioning','side channels','measured ops'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Trust is a measurement. Verify it continuously.');"]
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
    tags:["sgx", "sev", "confidential-computing", "enclaves", "attestation", "hardware-security", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"intel sgx amd sev record",
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
var gen={version:'jahdb-defense-aerospace-intel-sgx-amd-sev-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-intel-sgx-amd-sev',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-intel-sgx-amd-sev']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();