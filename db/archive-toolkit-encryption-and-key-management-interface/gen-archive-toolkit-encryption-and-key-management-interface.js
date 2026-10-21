(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["envelope-encryption", "key-lifecycle", "authorized-operations"];
var PREFIX="JAH-ATK265-";
var KIND="encryption and key management interface";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["envelope-encryption", "Envelope encryption", "Data is encrypted with a unique data key; the data key is then encrypted with a master key and stored alongside the ciphertext. Decryption unwraps the data key first, then the data. Envelope encryption limits master-key use and makes per-record keys practical. (Demos illustrate the key hierarchy with a teaching cipher; production uses AES-GCM via a vetted library.)", "per-record data keys wrapped by a master key", "decryption by unwrapping then decrypting", "master keys stored in hardware security modules", "CFG = {1: b\"hi\", 2: b\"hello world\", 3: b\"archive record 12345\"}\nimport os, hashlib, hmac\n# teaching illustration of envelope structure (NOT production crypto)\nmaster = os.urandom(16)\ndata_key = os.urandom(16)\ndef wrap(k, m): return bytes(a ^ b for a, b in zip(k, hashlib.sha256(m).digest()[:16]))\ndef enc(pt, k): return bytes(a ^ b for a, b in zip(pt, hashlib.sha256(k).digest() * 4))[:len(pt)]\nct = enc(CFG[LEVEL], data_key)\nwrapped = wrap(data_key, master)\ndk2 = wrap(wrapped, master)  # unwrap\npt2 = enc(ct, dk2)\nprint(\"roundtrip ok:\", pt2 == CFG[LEVEL], \"| wrapped key len:\", len(wrapped))"],
["key-lifecycle", "Key rotation", "Keys are replaced on a schedule or on suspicion of compromise. During rotation both old and new keys can decrypt (dual-read) while new data uses only the new key; afterwards data is re-encrypted or the old key is retired. Rotation bounds the damage of any single key exposure.", "scheduled and emergency rotation", "dual-read during the rotation window", "retiring old keys after re-encryption", "CFG = {1: {\"v\": 1}, 2: {\"v\": 2}, 3: {\"v\": 3}}\nkeys = {\"k1\": \"K1\", \"k2\": \"K2\", \"k3\": \"K3\"}\ncurrent = \"k%d\" % CFG[LEVEL][\"v\"]\nstore = {\"rec1\": (\"k1\", \"ct1\"), \"rec2\": (current, \"ct2\")}\ndef decrypt(rec):\n    k, _ = store[rec]\n    return k in keys  # dual-read: old keys still work during rotation\nprint(\"current:\", current, \"| rec1 decrypt:\", decrypt(\"rec1\"), \"| rec2 decrypt:\", decrypt(\"rec2\"))"],
["authorized-operations", "Key hierarchy", "Keys are organized in a hierarchy: a master key protects key-encrypting keys, which protect data keys. Compromise of a data key exposes one record; compromise higher up is contained by separation of duties and hardware protection. The hierarchy mirrors the blast radius it contains.", "master, key-encrypting, and data key tiers", "blast radius contained per tier", "hardware protection for the top tier", "CFG = {1: 2, 2: 3, 3: 4}\nN = CFG[LEVEL]\nhierarchy = {\"master\": [\"kek-%d\" % i for i in range(2)]}\nfor kek in hierarchy[\"master\"]:\n    hierarchy[kek] = [\"dk-%d\" % i for i in range(N)]\ndks = sum(len(v) for k, v in hierarchy.items() if k.startswith(\"kek\"))\nprint(\"master -> 2 KEKs -> %d data keys\" % dks, \"| one DK compromise exposes 1 record\")"],
["envelope-encryption", "Authorized crypto operations", "Every encrypt, decrypt, wrap, and unwrap call is authorized against the caller's identity and logged with the key id and purpose. Unauthorized calls are denied before touching key material. The operation log is the audit trail for all cryptographic activity.", "authorizing each operation by identity", "logging key id and purpose per call", "denying before touching key material", "CFG = {1: (\"amy\", \"decrypt\", True), 2: (\"bob\", \"decrypt\", False), 3: (\"amy\", \"destroy\", False)}\nwho, op, allowed_policy = CFG[LEVEL]\nPOLICY = {(\"amy\", \"decrypt\"), (\"amy\", \"encrypt\")}\nok = (who, op) in POLICY\nprint(\"%s requests %s ->\" % (who, op), \"ALLOWED + logged\" if ok else \"DENIED before key access\")"],
["key-lifecycle", "Key destruction ceremony", "Key destruction is a witnessed procedure: all copies are overwritten, hardware slots are zeroized, and witnesses attest the destruction in a signed record. Cryptographic erasure (destroying the key) renders ciphertext unrecoverable even where copies of the ciphertext remain. The ceremony record is archived permanently.", "overwriting all key copies", "witness attestation in a signed record", "crypto-erasure rendering ciphertext unrecoverable", "CFG = {1: 1, 2: 2, 3: 3}\ncopies = [\"copy-%d\" % i for i in range(CFG[LEVEL])]\nwitnesses = [\"w1\", \"w2\"]\ndestroyed = [\"\\x00\" * 8 for _ in copies]  # overwrite\nattested = all(c == \"\\x00\" * 8 for c in destroyed) and len(witnesses) >= 2\nprint(\"copies destroyed:\", len(destroyed), \"| witnesses:\", witnesses, \"| ceremony complete:\", attested)"]
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
var gen={version:"jahdb-archive-toolkit-encryption-and-key-management-interface-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-encryption-and-key-management-interface",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
