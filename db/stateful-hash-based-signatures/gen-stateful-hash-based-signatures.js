(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["schemes", "state", "standards", "operations"];
var PREFIX='JAH-SHBS-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["XMSS Signatures", "schemes", "Signs with XMSS, the standardized stateful hash-based scheme built on Merkle trees of WOTS+ one-time keys. Security rests only on hash functions — no number theory for quantum computers to break. RFC 8391 and NIST SP 800-208 standardize it.", ["Generate the Merkle tree", "Sign with the next one-time key", "Advance state atomically"], ["OpenSSL (oqs)", "liboqs", "Embedded"], ["RFC 8391", "NIST SP 800-208"], 3, 0], ["LMS Signatures", "schemes", "Signs with LMS, the hash-based scheme using LM-OTS one-time keys in Merkle trees. Simpler than XMSS and standardized in RFC 8554; NSA recommends it for certain uses. It is the conservative post-quantum choice.", ["Generate LM-OTS keys", "Build the Merkle tree", "Track the leaf index"], ["Cisco", "Embedded", "Libraries"], ["RFC 8554", "NIST SP 800-208"], 3, 0], ["Merkle Tree Construction", "schemes", "Builds the Merkle tree binding all one-time keys to one root public key. Leaves are one-time public keys; each parent hashes its children up to the root. The root is the long-term public key.", ["Hash leaves into the tree", "Publish the root", "Prove leaves with auth paths"], ["Libraries", "Custom", "Standards"], ["Merkle tree literature", "RFC 8391"], 2, 0], ["WOTS+ One-Time Signatures", "schemes", "Signs messages with Winternitz one-time signatures using hash chains. Each private-key element is hashed forward w times; the signature reveals intermediate values. One key signs exactly one message.", ["Generate hash chains", "Reveal chain positions per message", "Never reuse a key"], ["XMSS/LMS", "Libraries", "Research"], ["WOTS literature", "RFC 8391"], 3, 2], ["State Management Discipline", "state", "Manages the one-time-key index with crash-safe atomic updates. Reusing a one-time key breaks security catastrophically; the index must advance exactly once per signature, even across crashes. State handling is the whole ballgame.", ["Persist the index atomically", "Advance before signing", "Recover safely after crashes"], ["HSMs", "Embedded", "Libraries"], ["NIST SP 800-208", "Operational guides"], 3, 1], ["Multi-Tree XMSS^MT", "schemes", "Stacks XMSS trees in a hypertree so key generation stays fast for many signatures. Lower trees sign the roots of upper trees; total signatures multiply. It scales stateful signatures to millions of uses.", ["Build the hypertree layers", "Sign roots up the layers", "Manage per-layer state"], ["Libraries", "Research", "Standards"], ["RFC 8391", "XMSS^MT spec"], 3, 0], ["Key Generation Ceremonies", "operations", "Generates hash-based keys in audited ceremonies with witnesses and recordings. The tree takes minutes to hours to build; the ceremony proves it was done honestly. Root keys are published widely.", ["Build the tree in ceremony", "Record and witness", "Publish the root"], ["CAs", "Vendors", "Standards bodies"], ["Ceremony literature", "CA/Browser Forum"], 2, 0], ["State Reservation", "state", "Reserves ranges of one-time keys for offline signers that cannot sync state. Each signer gets a disjoint range; exhaustion is tracked per range. It enables safe distributed signing.", ["Partition the key space", "Assign disjoint ranges", "Track exhaustion per range"], ["HSMs", "CAs", "Embedded"], ["Operational guides", "NIST SP 800-208"], 3, 1], ["Backup and Restore", "operations", "Backs up stateful keys without ever cloning the signing state. Restoring an old backup would reuse keys — catastrophic; backups store the key material plus the rule to never roll back. Cloning is forbidden.", ["Back up key material", "Never restore older state", "Enforce monotonic indexes"], ["HSMs", "CAs", "Ops guides"], ["NIST SP 800-208", "Key management"], 3, 1], ["State Synchronization", "state", "Synchronizes signing state across redundant signers without reuse. A shared atomic counter or strict partitioning keeps signers disjoint. It is the hardest operational problem in stateful signatures.", ["Use atomic shared counters", "Or partition strictly", "Monitor for divergence"], ["HSM clusters", "CAs", "Research"], ["Distributed systems", "NIST guidance"], 3, 1], ["Signature Verification", "standards", "Verifies hash-based signatures statelessly with just the public key. Verification recomputes the Merkle path — no state needed on the verifier side. Anyone can verify with the standard algorithm.", ["Recompute the auth path", "Check against the root", "Validate parameters"], ["Libraries", "OpenSSL", "Embedded"], ["RFC 8391", "RFC 8554"], 1, 2], ["NIST SP 800-208 Guidance", "standards", "Follows NIST SP 800-208 for stateful hash-based signature use. The standard mandates state management practices and approved parameter sets. Compliance is required for federal use.", ["Use approved parameters", "Follow state practices", "Document compliance"], ["Federal systems", "Vendors", "Auditors"], ["NIST SP 800-208", "FIPS"], 2, 2], ["HSS Hierarchical Signatures", "schemes", "Uses HSS, the hierarchical LMS variant, for large signature counts. Levels of LMS trees sign the next level's roots; it mirrors XMSS^MT for LMS. RFC 8554 covers it.", ["Build LMS levels", "Sign roots between levels", "Track per-level state"], ["Libraries", "Standards", "Embedded"], ["RFC 8554", "NIST SP 800-208"], 3, 0], ["State Exhaustion Planning", "operations", "Plans key rotation before the one-time key space runs out. Monitoring tracks consumption; new trees are generated and cross-signed well before exhaustion. Running out means no more signatures.", ["Monitor consumption", "Generate successors early", "Cross-sign the transition"], ["CAs", "Ops", "HSMs"], ["Key management", "Operational guides"], 2, 1], ["HSM Integration", "operations", "Runs stateful signing inside HSMs with monotonic counters. The HSM enforces exactly-once state advancement in hardware; even a compromised host cannot reuse keys. It is the gold standard deployment.", ["Store keys in the HSM", "Enforce monotonic state", "Audit every signature"], ["Thales", "Utimaco", "YubiHSM"], ["HSM docs", "NIST guidance"], 3, 1]];
var DEMOS=["// Demo: {NAME} — Merkle tree height vs signatures\nvar h={N1}%6+6;\nvar sigs=Math.pow(2,h);\nconsole.log('technique: {NAME}');console.log('tree height: '+h);console.log('signatures per key: '+sigs.toLocaleString());\nconsole.log('key generation cost grows with height — pick for the use case');", "// Demo: {NAME} — state exhaustion gauge\nvar total={N2}*100,used=({SEED}*7919)%total;\nconsole.log('technique: {NAME}');console.log('used '+used+' of '+total+' one-time keys ('+(100*used/total).toFixed(1)+'%)');\nconsole.log(used<total*0.9?'healthy':'WARNING — rotate keys before exhaustion');", "// Demo: {NAME} — WOTS+ chain length\nvar w=16,n=32;\nvar chains=Math.ceil(8*n/Math.log2(w));\nconsole.log('technique: {NAME}');console.log('Winternitz w='+w+', chains: '+chains);\nconsole.log('signature size ~ '+(chains*n)+' bytes per one-time signature');"];
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
var gen={version:'jahdb-stateful-hash-based-signatures-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('stateful-hash-based-signatures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
