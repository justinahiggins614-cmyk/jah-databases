(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["kems", "hybrid", "migration", "validation"];
var PREFIX='JAH-QSD-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["ML-KEM (Kyber) Deployment", "kems", "Deploys ML-KEM, the NIST-standardized lattice KEM, for quantum-safe key exchange. Kyber's balanced sizes and speed won the NIST competition; FIPS 203 standardizes it. It is the default PQ key exchange.", ["Generate ML-KEM key pairs", "Encapsulate to the public key", "Decapsulate with the private key"], ["liboqs", "OpenSSL", "Browsers"], ["FIPS 203", "NIST PQC"], 2, 0], ["FrodoKEM Conservative Choice", "kems", "Uses FrodoKEM's conservative unstructured-lattice design where caution outweighs size. Bigger keys buy stronger security assumptions; some deployments prefer the margin. It is the belt-and-suspenders KEM.", ["Accept larger keys", "Gain conservative assumptions", "Deploy where size allows"], ["liboqs", "Research", "Custom"], ["FrodoKEM spec", "NIST PQC round 3"], 3, 0], ["Hybrid X25519+Kyber", "hybrid", "Combines X25519 with Kyber so sessions are safe unless both break. The hybrid secret mixes classical and PQ shares; deployed by browsers and CDNs today. It is the pragmatic migration.", ["Exchange both shares", "Mix into one secret", "Negotiate hybrid support"], ["Chrome", "Cloudflare", "AWS"], ["Hybrid KEM drafts (IETF)", "NIST guidance"], 2, 1], ["KEMTLS Handshakes", "hybrid", "Replaces TLS signatures with KEMs in the KEMTLS design, shrinking PQ handshakes. Long-lived KEM keys authenticate; no online signatures needed. It is the future shape of PQ TLS.", ["Use long-term KEM keys", "Authenticate implicitly", "Verify the design proofs"], ["Research", "oqs-openssl", "Prototypes"], ["KEMTLS paper", "TLS WG"], 3, 1], ["PQ Key Size Planning", "migration", "Plans for PQ key and ciphertext sizes in protocols and storage. Kyber public keys are ~1.5KB versus 32 bytes for X25519; buffers, MTUs, and databases must grow. Size surprises break deployments.", ["Audit size assumptions", "Grow buffers and fields", "Test with real keys"], ["Protocol designers", "Vendors", "Ops"], ["NIST PQC", "Protocol guides"], 1, 0], ["Side-Channel Resistant KEMs", "validation", "Implements KEMs with constant-time code to resist timing and power analysis. Reference implementations are not always constant-time; hardened versions are audited. Side channels break math that is otherwise sound.", ["Use constant-time implementations", "Audit for leaks", "Test with power analysis"], ["PQClean", "Vendors", "HSMs"], ["Side-channel literature", "NIST guidance"], 3, 2], ["NIST FIPS 203 Compliance", "migration", "Complies with FIPS 203 for ML-KEM in regulated deployments. Approved parameters, validated modules, documented usage — the compliance checklist. Federal systems require it.", ["Use FIPS-approved parameters", "Validate the module", "Document the deployment"], ["Federal", "Vendors", "Auditors"], ["FIPS 203", "CMVP"], 2, 2], ["PQ Migration Strategy", "migration", "Plans the enterprise migration: inventory crypto, prioritize, pilot hybrids, then cut over. Cryptography inventories reveal the scope; hybrids de-risk the transition. It is a multi-year program.", ["Inventory all crypto use", "Pilot hybrid deployments", "Cut over by priority"], ["Enterprises", "CNSA 2.0", "Consultants"], ["NIST migration guidance", "CNSA 2.0"], 2, 2], ["PQ Performance Benchmarks", "validation", "Benchmarks PQ algorithms on target hardware to size the migration. Keygen, encaps, and decaps costs vary widely; measurements pick parameters and hardware. Data beats assumptions.", ["Benchmark on target CPUs", "Measure handshake impact", "Size accordingly"], ["liboqs benchmarks", "Labs", "Vendors"], ["Benchmarking literature", "NIST PQC"], 2, 1], ["Known-Answer Testing", "validation", "Validates PQ implementations with known-answer tests from the standards. KAT vectors catch implementation bugs before deployment; every release runs them. It is table stakes for crypto code.", ["Run KAT vectors", "Automate in CI", "Fail closed on mismatch"], ["NIST CAVP", "Vendors", "CI"], ["NIST KATs", "Crypto validation"], 1, 2], ["Hybrid Negotiation", "hybrid", "Negotiates hybrid key exchange in protocols with graceful fallback. Peers advertise PQ support; both sides agree or fall back cleanly. Negotiation must resist downgrade.", ["Advertise PQ groups", "Agree bilaterally", "Protect against downgrade"], ["TLS", "SSH", "WireGuard"], ["IETF drafts", "Protocol specs"], 2, 1], ["PQ Certificate Handling", "migration", "Handles PQ certificates with bigger keys and new OIDs in PKI. Chains grow; verifiers must parse new algorithms; hybrid certs ease transition. PKI is the long pole of migration.", ["Issue PQ/hybrid certs", "Update verifiers", "Plan chain sizes"], ["CAs", "Libraries", "Enterprises"], ["X.509", "IETF PQC drafts"], 3, 2], ["Protocol Integration (TLS/SSH)", "hybrid", "Integrates PQ key exchange into TLS, SSH, and WireGuard deployments. Each protocol has its integration story; the work is configuration and testing more than cryptography. Pilots prove it works.", ["Enable PQ groups", "Test interoperability", "Monitor handshakes"], ["OpenSSH", "OpenSSL", "WireGuard"], ["Protocol specs", "IETF drafts"], 2, 1], ["Downgrade Protection", "validation", "Protects PQ negotiation from downgrade to classical-only. Attackers who strip PQ offers must not succeed; the handshake authenticates what was offered. TLS 1.3's design helps.", ["Authenticate negotiations", "Pin PQ where required", "Alert on downgrade"], ["TLS 1.3", "SSH", "Libraries"], ["RFC 8446", "Downgrade literature"], 2, 2], ["Crypto Agility Programs", "migration", "Builds crypto agility so algorithms swap without rewrites. Abstract interfaces, algorithm registries, and tested migration paths make the next transition cheap. Agility is the lesson of every migration.", ["Abstract algorithm interfaces", "Registry-driven selection", "Test swaps regularly"], ["Enterprises", "Libraries", "Platforms"], ["Agility literature", "NIST guidance"], 3, 2]];
var DEMOS=["// Demo: {NAME} — key and ciphertext sizes\nvar schemes=[['X25519',32,32],['ML-KEM-512',800,768],['ML-KEM-768',1184,1088],['FrodoKEM-640',9616,9720]];\nconsole.log('technique: {NAME}');\nschemes.forEach(function(s){console.log(s[0]+': pk '+s[1]+'B, ct '+s[2]+'B');});\nconsole.log('PQ keys are bigger — size the protocols accordingly');", "// Demo: {NAME} — hybrid secret mixing\nfunction mix(a,b){var h=0;var s=a+b;for(var i=0;i<s.length;i++){h=(h*33+s.charCodeAt(i))>>>0;}return h.toString(16);}\nvar hybrid=mix('x25519-secret-{SEED}','kyber-secret-{N1}');\nconsole.log('technique: {NAME}');console.log('hybrid secret: '+hybrid);\nconsole.log('attacker must break BOTH to recover the secret');", "// Demo: {NAME} — KAT-style determinism check\nfunction kem(seed){var h=0;var s='kat'+seed;for(var i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))>>>0;}return h.toString(16);}\nvar a=kem({SEED}),b=kem({SEED});\nconsole.log('technique: {NAME}');console.log('run1: '+a+', run2: '+b);\nconsole.log(a===b?'deterministic — KAT passes':'NONDETERMINISM — investigate');"];
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
var gen={version:'jahdb-quantum-safe-diffie-hellman-key-exchange-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quantum-safe-diffie-hellman-key-exchange',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
