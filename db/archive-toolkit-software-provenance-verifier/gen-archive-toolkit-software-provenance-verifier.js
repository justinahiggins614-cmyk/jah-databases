(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["signature-verification", "hash-attestation", "origin-records"];
var PREFIX="JAH-ATK272-";
var KIND="software provenance verifier";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["signature-verification", "Hash verification against published digests", "The artifact's hash is recomputed locally and compared against the digest published by the distributor. A match proves the bytes are exactly what the distributor released. Verification happens before installation, never after.", "recomputing hashes locally", "comparing against distributor-published digests", "verifying before installation", "CFG = {1: b\"release-1.0\", 2: b\"release-1.0 tampered\", 3: b\"release-2.0\"}\nimport hashlib\npublished = hashlib.sha256(b\"release-1.0\").hexdigest()\ngot = hashlib.sha256(CFG[LEVEL]).hexdigest()\nprint(\"published:\", published[:16], \"| computed:\", got[:16], \"| verified:\", got == published)"],
["hash-attestation", "Signature verification workflow", "Detached signatures over the artifact are verified with the distributor's public key before use. Signature verification proves both integrity and origin: the bytes are intact and they came from the key holder. Keys are fetched through trusted channels, never alongside the artifact alone.", "verifying detached signatures with public keys", "proving integrity and origin together", "keys via trusted channels", "CFG = {1: b\"data\", 2: b\"data!\", 3: b\"data\"}\nimport hashlib, hmac\nKEY = b\"distributor-key\"\ndef sign(m): return hmac.new(KEY, m, hashlib.sha256).hexdigest()\nsig = sign(b\"data\")  # distributor's signature (teaching illustration with HMAC)\nok = hmac.compare_digest(sig, sign(CFG[LEVEL]))\nprint(\"artifact:\", CFG[LEVEL], \"| signature valid:\", ok)"],
["origin-records", "SLSA-style provenance attestation", "Build provenance records who built the artifact, from which source, with which steps. The attestation is signed by the builder and verified by the consumer before use. Provenance closes the gap between 'the source looks fine' and 'this binary came from that source'.", "recording builder, source, and steps", "signed attestations verified before use", "binding binaries to their source", "CFG = {1: {\"builder\": \"ci-1\", \"src\": \"abc123\"}, 2: {\"builder\": \"ci-1\", \"src\": \"abc123\", \"signed\": True}, 3: {\"builder\": \"laptop-x\", \"src\": \"abc123\", \"signed\": True}}\natt = CFG[LEVEL]\nTRUSTED = {\"ci-1\"}\nok = att.get(\"signed\") and att[\"builder\"] in TRUSTED\nprint(\"attestation:\", att, \"| trusted:\", ok)"],
["signature-verification", "Trusted publisher check", "Artifacts are accepted only from publisher identities on the trusted list. Publisher identity is verified cryptographically, not by self-declaration in metadata. New publishers are onboarded through a vetting process, not by first use.", "publisher allowlists", "cryptographic publisher identity", "vetted onboarding for new publishers", "CFG = {1: \"acme-corp\", 2: \"unknown-vendor\", 3: \"acme-corp\"}\nTRUSTED = {\"acme-corp\", \"open-foundation\"}\npub = CFG[LEVEL]\nprint(\"publisher:\", pub, \"->\", \"ACCEPT\" if pub in TRUSTED else \"REJECT: untrusted publisher\")"],
["hash-attestation", "Reproducible-build verification", "The artifact is rebuilt from source in a controlled environment and the resulting bytes are compared to the distributed artifact. Bit-for-bit equality proves the binary matches the source. Reproducibility is the strongest provenance claim.", "rebuilding from source in controlled environments", "bit-for-bit comparison", "reproducibility as the strongest claim", "CFG = {1: \"v1.0\", 2: \"v1.0\", 3: \"v1.0+backdoor\"}\nimport hashlib\ndef build(src): return hashlib.sha256((\"build:\" + src).encode()).hexdigest()\npublished = build(\"v1.0\")\nrebuilt = build(CFG[LEVEL])\nprint(\"source:\", CFG[LEVEL], \"| reproducible:\", rebuilt == published)"]
];
function escRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(r){return r[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var ladder=1+((seed>>>0)%3);
  var focus=[row[3],row[4],row[5]][ladder-1];
  var stage=['','At ladder rank 1 (foundation), this record covers ','At ladder rank 2 (compounded), it builds on the foundation with ','At ladder rank 3 (full complexity), it extends to production scale with '][ladder];
  var id=PREFIX+String(seed>>>0).padStart(6,'0');
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Public harvest — documented archive-engineering practice; method fact-checked against standard references.",last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length||r.t!==r.title)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('LEVEL = '+r.ladder_rank)!==0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-software-provenance-verifier-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-software-provenance-verifier",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
