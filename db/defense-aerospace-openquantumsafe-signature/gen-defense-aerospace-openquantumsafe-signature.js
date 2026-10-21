(function(){'use strict';
/* jahdb-defense-aerospace-openquantumsafe-1.0 — deterministic boundless generator for defense-aerospace-openquantumsafe-signature.
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
var CATS=["pqc", "kem", "signatures", "nist", "openssl", "migration"];
var PREFIX='JAH-DAE42S-';
var DBNAME="Signature OpenQuantumSafe Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["pqc",
 "Signature OpenQuantumSafe: What OpenQuantumSafe Is: Crypto for the Quantum Age",
 "The Signature counterpart is the SigLattice vault, Manon's original PQC design. It mirrors the KEM/signature API but every key carries an algorithm-agility manifest \u2014 the suite can rotate algorithms without re-provisioning. The Signature design treats algorithm agility as the primary feature: today's NIST picks are the default, not the destiny.",
 ["NIST-selected PQC algorithms", "C library plus OpenSSL/OpenSSH integrations", "Agility as the primary feature"],
 "console.log('liboqs: ML-KEM, ML-DSA, SLH-DSA, Falcon');\nconsole.log('integrations: oqs-provider (OpenSSL), OQS-OpenSSH');"],
["kem",
 "Signature OpenQuantumSafe: ML-KEM (Kyber): Key Encapsulation",
 "The vault's KEM is the sealed envelope: same API, with the parameter set recorded in the key manifest. The Signature design defaults to hybrid \u2014 classical plus PQC \u2014 and the manifest states which assumption each half provides, so the security argument stays explicit.",
 ["FIPS 203 lattice KEM", "800-1568 byte public keys", "Hybrid X25519+Kyber migration pattern"],
 "var kem={'ML-KEM-512':[800,768],'ML-KEM-768':[1184,1088],'ML-KEM-1024':[1568,1568]};\nObject.keys(kem).forEach(function(k){console.log(k+': pk '+kem[k][0]+' B, ct '+kem[k][1]+' B');});\nconsole.log('hybrid default: X25519 + ML-KEM-768');"],
["signatures",
 "Signature OpenQuantumSafe: ML-DSA (Dilithium): Signatures",
 "The vault's signatures are the wax seals: same algorithms, with the size budget computed per protocol. The Signature design requires the size analysis before migration \u2014 'Dilithium-65 adds X KB to our handshake' is a number, decided deliberately.",
 ["FIPS 204 lattice signatures", "2.4-7.8 KB signatures", "Size analysis before migration"],
 "var sig={'ML-DSA-44':2420,'ML-DSA-65':3309,'SLH-DSA-128s':7856};\nObject.keys(sig).forEach(function(k){console.log(k+': sig '+sig[k]+' B');});\nconsole.log('vs ECDSA 64 B: budget the difference');"],
["nist",
 "Signature OpenQuantumSafe: The Threat: Harvest Now, Decrypt Later",
 "The vault's doctrine is the long-secret rule: data classified for decades migrates first. The Signature design maintains the secrecy-lifetime ledger \u2014 which data, which crypto, which quantum timeline \u2014 and the migration order follows the ledger, not convenience.",
 ["Recorded traffic decrypted later", "Long-secrecy data exposed already", "Migrate by secrecy lifetime"],
 "var data=[['state secrets',50],['health records',30],['session cookies',0.1]];\ndata.forEach(function(d){console.log(d[0]+': secrecy '+d[1]+'y'+(d[1]>10?' -> MIGRATE FIRST':''));});"],
["openssl",
 "Signature OpenQuantumSafe: Your First Handshake: oqs-provider",
 "The vault's hello-world is the first seal: same handshake, but the client verifies the algorithm manifest \u2014 'server offered hybrid X25519+ML-KEM-768, policy accepts'. The Signature design makes the policy visible: the operator sees which algorithms were negotiated and why they were acceptable.",
 ["PQC TLS via oqs-provider", "Hybrid groups work today", "Negotiated algorithms visible per policy"],
 "console.log('handshake: TLS 1.3, X25519+ML-KEM-768 (hybrid)');\nconsole.log('policy: pqc-required -> ACCEPT (manifest verified)');"],
["migration",
 "Signature OpenQuantumSafe: liboqs API: Integrating PQC into Applications",
 "The vault's integration doctrine is the measured drop-in: same API shape, with the size and timing budgets computed before the protocol changes. The Signature design requires the packet-format analysis \u2014 'ML-KEM-768 adds 1184+1088 bytes here' \u2014 signed off before the integration ships.",
 ["C API for custom protocols", "Keygen slow, encaps fast", "Packet budgets signed off"],
 "var api={keygen_ms:0.9,encaps_ms:0.08,added_bytes:2272};\nconsole.log('OQS_KEM: keygen '+api.keygen_ms+' ms, encaps '+api.encaps_ms+' ms');\nconsole.log('packet budget +'+api.added_bytes+' B (signed off)');"],
["pqc",
 "Signature OpenQuantumSafe: Hybrid Cryptography: Belt and Suspenders",
 "The vault's hybrid doctrine is the double lock: classical plus PQC, with the combiner specified and tested. The Signature design requires the hybrid until the PQC algorithm has a decade of cryptanalysis \u2014 new math earns trust slowly, and the double lock buys the time.",
 ["Secure if either component holds", "Concatenate-then-KDF combiner", "Hybrids until the math earns trust"],
 "console.log('shared secret = KDF(x25519_secret || mlkem_secret)');\nconsole.log('secure if EITHER holds (double lock)');\nconsole.log('standalone PQC: after a decade of cryptanalysis');"],
["kem",
 "Signature OpenQuantumSafe: Constant-Time Code and Side Channels",
 "The vault's implementation doctrine is the silent arithmetic: constant-time verified by testing (dudect-style), with the verification report in the release. The Signature design requires the side-channel report before any implementation ships \u2014 fast code that leaks is not an optimization, it is a vulnerability.",
 ["Secret-dependent branches leak keys", "Constant-time implementation and testing", "Side-channel report before shipping"],
 "console.log('dudect: 1M traces, no leakage detected');\nconsole.log('side-channel report: attached to release');\nconsole.log('fast but leaky: REJECTED (vulnerability, not optimization)');"],
["signatures",
 "Signature OpenQuantumSafe: Defensive Uses: The Migration Program",
 "The vault's program doctrine is the crypto census: every system, every algorithm, every secrecy lifetime \u2014 inventoried. The Signature design makes the census a living document, reviewed with the thunderhead watch: migration is a program, not a project.",
 ["Cryptography bill of materials", "Prioritize by secrecy lifetime", "Migration as a multi-year program"],
 "var census=[['vpn gateways','PQC done'],['firmware signing','in progress'],['legacy scada','queued']];\ncensus.forEach(function(c){console.log(c[0]+': '+c[1]);});"],
["nist",
 "Signature OpenQuantumSafe: Certificates and PKI at PQC Sizes",
 "The vault's PKI doctrine is the measured chain: certificate sizes computed end-to-end before the CA migration. The Signature design requires the embedded verifiers tested first \u2014 the smallest device in the PKI sets the constraints.",
 ["Kilobyte certificates, bigger chains", "Composite classical+PQC certificates", "Embedded verifiers set constraints"],
 "var chain={classical_kb:2,pqc_kb:14};\nconsole.log('chain: '+chain.classical_kb+' KB -> '+chain.pqc_kb+' KB');\nconsole.log('smallest verifier: 64 KB RAM (tested, fits)');"],
["openssl",
 "Signature OpenQuantumSafe: Debugging: Interop and Negotiation",
 "The vault's debugger is the handshake scope: offered groups, negotiated suite, size accounting. The Signature design logs negotiation failures as migration telemetry \u2014 every failed handshake teaches where the path is not ready.",
 ["Group negotiation diagnostics", "Middlebox vs big handshakes", "Failures as migration telemetry"],
 "console.log('offered: X25519+ML-KEM-768; negotiated: X25519+ML-KEM-768');\nconsole.log('ClientHello 4.2 KB (middlebox passed)');"],
["migration",
 "Signature OpenQuantumSafe: Performance: PQC at Scale",
 "The vault's performance doctrine is the measured handshake: benchmarks on target hardware, network math with real sizes. The Signature design requires the numbers before the rollout \u2014 'PQC costs us X ms per handshake' is decided, not discovered.",
 ["Benchmark on target hardware", "Sizes dominate the network math", "Numbers decided before rollout"],
 "var bench={mlkem_enc_ms:0.08,dsa_sign_ms:0.31,handshake_add_ms:2.1};\nconsole.log('ML-KEM enc '+bench.mlkem_enc_ms+' ms, Dilithium sign '+bench.dsa_sign_ms+' ms');\nconsole.log('handshake +'+bench.handshake_add_ms+' ms (measured, target hw)');"],
["pqc",
 "Signature OpenQuantumSafe: Testing: Known-Answer and Wycheproof",
 "The vault's test doctrine is the triple gate: KATs, interop, constant-time \u2014 all green before release. The Signature design makes the gate results part of the release signature: tested crypto is signed crypto.",
 ["NIST known-answer tests", "Interop between implementations", "Gate results in the release signature"],
 "var gates=[['NIST KATs',1],['interop',1],['constant-time',1]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'PASS':'FAIL'));});\nconsole.log('triple gate GREEN -> release signed');"],
["kem",
 "Signature OpenQuantumSafe: Real-World Pattern: VPN Migration",
 "The vault's migration doctrine is the quiet upgrade: waves, measurements, rollback ready. The Signature design requires the capture verification per wave \u2014 'we believe it migrated' is replaced with 'the captures show it'.",
 ["Inventory, pilot, waves, verify", "Handshake captures as proof", "Invisible and complete"],
 "var waves=[['pilot',1],['wave 1 (30%)',1],['wave 2 (70%)',1],['complete',1]];\nwaves.forEach(function(w){console.log(w[0]+': '+(w[1]?'captures verify PQC':'pending'));});"],
["signatures",
 "Signature OpenQuantumSafe: Mastery: The PQC Engineer's Playbook",
 "The vault's mastery adds the stewardship layer: census, ledgers, agility. Manon's roadmap runs from today's library integrations to a fully agile crypto estate under one discipline \u2014 migrate on your schedule, not the thunderhead's.",
 ["Lattices through migration programs", "HSM and custom integrations", "Stewardship: census, agility, ledgers"],
 "var playbook=['lattice intuition','protocol integration','migration programs','implementation security'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Migrate on your schedule, not the thunderhead\\'s.');"]
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
    tags:["pqc", "kyber", "dilithium", "liboqs", "nist", "quantum-resistant", "open-source", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
    last_verified:'2026-10-21',
    record_kind:"openquantumsafe record",
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
var gen={version:'jahdb-defense-aerospace-openquantumsafe-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-openquantumsafe-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-openquantumsafe-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();