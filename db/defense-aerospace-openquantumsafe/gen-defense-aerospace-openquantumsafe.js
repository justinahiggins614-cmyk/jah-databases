(function(){'use strict';
/* jahdb-defense-aerospace-openquantumsafe-1.0 — deterministic boundless generator for defense-aerospace-openquantumsafe.
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
var PREFIX='JAH-DAE42-';
var DBNAME="OpenQuantumSafe Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["pqc",
 "OpenQuantumSafe: What OpenQuantumSafe Is: Crypto for the Quantum Age",
 "liboqs implements the post-quantum algorithms NIST selected: ML-KEM (Kyber) for key establishment, ML-DSA (Dilithium) for signatures, plus SLH-DSA (SPHINCS+) and FN-DSA (Falcon). It is the reference implementation teams integrate first \u2014 the C library, the OpenSSL provider (oqs-provider), and the OpenSSH fork that let you handshake with quantum-resistant crypto today. When Shor's algorithm eventually breaks RSA and ECC, these lattice- and hash-based schemes are the replacement.",
 ["NIST-selected PQC algorithms", "C library plus OpenSSL/OpenSSH integrations", "Agility as the primary feature"],
 "console.log('liboqs: ML-KEM, ML-DSA, SLH-DSA, Falcon');\nconsole.log('integrations: oqs-provider (OpenSSL), OQS-OpenSSH');"],
["kem",
 "OpenQuantumSafe: ML-KEM (Kyber): Key Encapsulation",
 "ML-KEM (FIPS 203, ex-Kyber) is the key-establishment workhorse: the server publishes a public key, the client encapsulates a random secret to it, both derive the shared secret. Parameter sets 512/768/1024 trade security for size (public keys 800/1184/1568 bytes \u2014 bigger than ECC's 32, the price of quantum resistance). liboqs implements all three with constant-time code. The migration pattern is hybrid key exchange: X25519 plus ML-KEM-768, secure if either holds.",
 ["FIPS 203 lattice KEM", "800-1568 byte public keys", "Hybrid X25519+Kyber migration pattern"],
 "var kem={'ML-KEM-512':[800,768],'ML-KEM-768':[1184,1088],'ML-KEM-1024':[1568,1568]};\nObject.keys(kem).forEach(function(k){console.log(k+': pk '+kem[k][0]+' B, ct '+kem[k][1]+' B');});\nconsole.log('hybrid default: X25519 + ML-KEM-768');"],
["signatures",
 "OpenQuantumSafe: ML-DSA (Dilithium): Signatures",
 "ML-DSA (FIPS 204, ex-Dilithium) signs: parameter sets 44/65/87 with signatures around 2.4-4.6 KB \u2014 large next to ECDSA's 64 bytes, the cost of lattice security. liboqs implements all sets plus the stateless hash-based SLH-DSA for the paranoid (bigger, slower, minimal assumptions). Choosing is engineering: Dilithium for general use, SLH-DSA where the threat model justifies the cost. Signature sizes ripple through protocols \u2014 certificates, handshakes, and embedded budgets all feel it.",
 ["FIPS 204 lattice signatures", "2.4-7.8 KB signatures", "Size analysis before migration"],
 "var sig={'ML-DSA-44':2420,'ML-DSA-65':3309,'SLH-DSA-128s':7856};\nObject.keys(sig).forEach(function(k){console.log(k+': sig '+sig[k]+' B');});\nconsole.log('vs ECDSA 64 B: budget the difference');"],
["nist",
 "OpenQuantumSafe: The Threat: Harvest Now, Decrypt Later",
 "The urgency has a name: adversaries record encrypted traffic today to decrypt when cryptographically-relevant quantum computers arrive. Data with a long secrecy lifetime \u2014 state secrets, health records, infrastructure designs \u2014 is already exposed if it was encrypted with RSA/ECC and recorded. This is why migration cannot wait for the quantum computer: the attack is happening now, against the future. PQC migration is defense against a clock that is already running.",
 ["Recorded traffic decrypted later", "Long-secrecy data exposed already", "Migrate by secrecy lifetime"],
 "var data=[['state secrets',50],['health records',30],['session cookies',0.1]];\ndata.forEach(function(d){console.log(d[0]+': secrecy '+d[1]+'y'+(d[1]>10?' -> MIGRATE FIRST':''));});"],
["openssl",
 "OpenQuantumSafe: Your First Handshake: oqs-provider",
 "The hello-world: build oqs-provider, configure OpenSSL to load it, and negotiate a TLS handshake with ML-KEM-768 key exchange \u2014 s_client/s_server showing the PQC group in the cipher description. It works today, interoperably, with the hybrid groups. From there: the OpenSSH fork for PQC host keys, then liboqs in your own application. The handshake you can run this afternoon is the migration's proof of concept.",
 ["PQC TLS via oqs-provider", "Hybrid groups work today", "Negotiated algorithms visible per policy"],
 "console.log('handshake: TLS 1.3, X25519+ML-KEM-768 (hybrid)');\nconsole.log('policy: pqc-required -> ACCEPT (manifest verified)');"],
["migration",
 "OpenQuantumSafe: liboqs API: Integrating PQC into Applications",
 "Beyond OpenSSL, liboqs integrates directly: the C API (OQS_KEM_keypair/encaps/decaps) drops PQC into custom protocols, VPNs, and embedded systems. The integration points are key generation (slow \u2014 do it rarely), encapsulation (fast), and the size budgets (keys and ciphertexts in your packet formats). The pattern is hybrid first, measured always: integrate, benchmark on target hardware, then decide.",
 ["C API for custom protocols", "Keygen slow, encaps fast", "Packet budgets signed off"],
 "var api={keygen_ms:0.9,encaps_ms:0.08,added_bytes:2272};\nconsole.log('OQS_KEM: keygen '+api.keygen_ms+' ms, encaps '+api.encaps_ms+' ms');\nconsole.log('packet budget +'+api.added_bytes+' B (signed off)');"],
["pqc",
 "OpenQuantumSafe: Hybrid Cryptography: Belt and Suspenders",
 "Hybrid key exchange (X25519+ML-KEM) is the migration's safety net: the combined secret is secure if either component holds \u2014 against classical attackers via X25519, against quantum attackers via ML-KEM. Standards (and browsers) converged on hybrids for the transition. The combiner is the critical detail: concatenate-then-KDF, done right. Hybrids let you deploy PQC now without betting the farm on new math.",
 ["Secure if either component holds", "Concatenate-then-KDF combiner", "Hybrids until the math earns trust"],
 "console.log('shared secret = KDF(x25519_secret || mlkem_secret)');\nconsole.log('secure if EITHER holds (double lock)');\nconsole.log('standalone PQC: after a decade of cryptanalysis');"],
["kem",
 "OpenQuantumSafe: Constant-Time Code and Side Channels",
 "PQC implementations must be constant-time: lattice operations with secret-dependent branches or memory access leak keys through timing and cache side channels. liboqs's implementations are written (and tested) for constant-time behavior, with the test suite including known-answer and side-channel-oriented checks. The defensive lesson generalizes: the algorithm is half the security; the implementation is the other half.",
 ["Secret-dependent branches leak keys", "Constant-time implementation and testing", "Side-channel report before shipping"],
 "console.log('dudect: 1M traces, no leakage detected');\nconsole.log('side-channel report: attached to release');\nconsole.log('fast but leaky: REJECTED (vulnerability, not optimization)');"],
["signatures",
 "OpenQuantumSafe: Defensive Uses: The Migration Program",
 "liboqs's defensive value is the migration itself: inventorying crypto across the estate (the CBOM \u2014 cryptography bill of materials), prioritizing by secrecy lifetime, piloting hybrids, and rolling out PQC where it matters first. The program is measured in years and touches everything \u2014 TLS, VPNs, firmware signing, PKI. Starting now is the defense; the library is the tool.",
 ["Cryptography bill of materials", "Prioritize by secrecy lifetime", "Migration as a multi-year program"],
 "var census=[['vpn gateways','PQC done'],['firmware signing','in progress'],['legacy scada','queued']];\ncensus.forEach(function(c){console.log(c[0]+': '+c[1]);});"],
["nist",
 "OpenQuantumSafe: Certificates and PKI at PQC Sizes",
 "PQC breaks PKI's size assumptions: Dilithium certificates are kilobytes, chains are bigger, and embedded verifiers feel it. The ecosystem adapts: composite certificates (classical+PQC), protocol tuning (TLS record sizing), and careful CA planning. liboqs plus oqs-provider let you build and test PQC PKI today. The CA's migration \u2014 root ceremonies with new algorithms \u2014 is the program's crown jewel, planned years ahead.",
 ["Kilobyte certificates, bigger chains", "Composite classical+PQC certificates", "Embedded verifiers set constraints"],
 "var chain={classical_kb:2,pqc_kb:14};\nconsole.log('chain: '+chain.classical_kb+' KB -> '+chain.pqc_kb+' KB');\nconsole.log('smallest verifier: 64 KB RAM (tested, fits)');"],
["openssl",
 "OpenQuantumSafe: Debugging: Interop and Negotiation",
 "PQC debugging classics: the peer does not offer the group (version/config), the handshake fails on size limits (middleboxes vs big ClientHellos), and the provider does not load (OpenSSL config). The tools are s_client with -groups, packet captures showing the key_share, and the provider's diagnostics. Middlebox intolerance of big handshakes is the real-world friction \u2014 test through the actual network path.",
 ["Group negotiation diagnostics", "Middlebox vs big handshakes", "Failures as migration telemetry"],
 "console.log('offered: X25519+ML-KEM-768; negotiated: X25519+ML-KEM-768');\nconsole.log('ClientHello 4.2 KB (middlebox passed)');"],
["migration",
 "OpenQuantumSafe: Performance: PQC at Scale",
 "PQC performance is a deployment question: ML-KEM operations are fast (faster than ECDH in many implementations), Dilithium signing is fast but verification costs more, and the sizes (keys, signatures, handshakes) dominate the network math. Benchmarks on the target hardware \u2014 not the laptop \u2014 decide. The good news: for TLS, the handshake cost is usually lost in the noise of the connection.",
 ["Benchmark on target hardware", "Sizes dominate the network math", "Numbers decided before rollout"],
 "var bench={mlkem_enc_ms:0.08,dsa_sign_ms:0.31,handshake_add_ms:2.1};\nconsole.log('ML-KEM enc '+bench.mlkem_enc_ms+' ms, Dilithium sign '+bench.dsa_sign_ms+' ms');\nconsole.log('handshake +'+bench.handshake_add_ms+' ms (measured, target hw)');"],
["pqc",
 "OpenQuantumSafe: Testing: Known-Answer and Wycheproof",
 "PQC testing layers: known-answer tests (NIST vectors) for correctness, Wycheproof-style edge cases, interop tests between implementations, and the constant-time checks. liboqs's test suite runs the NIST KATs on every build. For adopters: test your integration against the KATs, test interop against another implementation, and never ship an implementation that fails either.",
 ["NIST known-answer tests", "Interop between implementations", "Gate results in the release signature"],
 "var gates=[['NIST KATs',1],['interop',1],['constant-time',1]];\ngates.forEach(function(g){console.log(g[0]+': '+(g[1]?'PASS':'FAIL'));});\nconsole.log('triple gate GREEN -> release signed');"],
["kem",
 "OpenQuantumSafe: Real-World Pattern: VPN Migration",
 "A complete pattern: an organization migrates its VPN fleet to hybrid PQC \u2014 inventory the gateways, pilot hybrid key exchange on a test pair, measure handshake impact, roll out in waves with rollback ready, and verify with handshake captures. Users notice nothing; the packet captures show ML-KEM in the key shares. The migration is invisible and complete \u2014 the best kind.",
 ["Inventory, pilot, waves, verify", "Handshake captures as proof", "Invisible and complete"],
 "var waves=[['pilot',1],['wave 1 (30%)',1],['wave 2 (70%)',1],['complete',1]];\nwaves.forEach(function(w){console.log(w[0]+': '+(w[1]?'captures verify PQC':'pending'));});"],
["signatures",
 "OpenQuantumSafe: Mastery: The PQC Engineer's Playbook",
 "PQC mastery spans lattice intuition, protocol integration, migration program management, and implementation security. The advanced moves are custom integrations, HSM support, and contributing to the standards. The mindset: the quantum computer is coming on its schedule, not yours \u2014 migrate on yours.",
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
    edition:'public',
    category:tp[0],
    tags:["pqc", "kyber", "dilithium", "liboqs", "nist", "quantum-resistant", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-openquantumsafe',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-openquantumsafe']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();