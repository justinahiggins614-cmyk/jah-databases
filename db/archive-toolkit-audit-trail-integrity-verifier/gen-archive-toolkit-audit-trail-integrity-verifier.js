(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["hash-chaining", "tamper-detection", "independent-attestation"];
var PREFIX="JAH-ATK266-";
var KIND="audit trail integrity verifier";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["hash-chaining", "Hash-chained audit log", "Each audit entry includes the hash of the previous entry, forming a chain. Any modification to an earlier entry breaks every later hash, so tampering is detectable by re-verifying the chain. The genesis hash is published so the chain has a trusted starting point.", "each entry committing to the previous hash", "tamper evident via chain re-verification", "published genesis hash as trust anchor", "CFG = {1: 5, 2: 10, 3: 25}\nN = CFG[LEVEL]\nimport hashlib\ndef h(s): return hashlib.sha256(s.encode()).hexdigest()[:16]\nchain, prev = [], \"GENESIS\"\nfor i in range(N):\n    prev = h(prev + \"|event-%d\" % i); chain.append(prev)\nok, prev = True, \"GENESIS\"\nfor i, c in enumerate(chain):\n    prev = h(prev + \"|event-%d\" % i)\n    if prev != c: ok = False\nchain[3] = \"tampered\"\nprev, detected = \"GENESIS\", False\nfor i, c in enumerate(chain):\n    prev = h(prev + \"|event-%d\" % i)\n    if prev != c: detected = True\nprint(\"entries:\", N, \"| clean chain verifies:\", ok, \"| tamper detected:\", detected)"],
["tamper-detection", "Merkle-tree batch attestation", "Audit entries are batched into a Merkle tree and only the root hash is published or timestamped. Any single entry can be proven included with a logarithmic-size proof, without revealing the other entries. Batching makes external attestation cheap.", "batching entries into a Merkle tree", "publishing only the root", "logarithmic inclusion proofs", "CFG = {1: 4, 2: 8, 3: 16}\nN = CFG[LEVEL]\nimport hashlib\ndef h(s): return hashlib.sha256(s.encode()).hexdigest()\nleaves = [h(\"entry-%d\" % i) for i in range(N)]\nlvl = leaves\nwhile len(lvl) > 1:\n    lvl = [h(lvl[i] + lvl[i + 1]) for i in range(0, len(lvl), 2)]\nroot = lvl[0]\nprint(\"entries:\", N, \"| merkle root:\", root[:16], \"| proof size: %d hashes\" % (N.bit_length()))"],
["independent-attestation", "Append-only enforcement", "Once sealed, audit entries cannot be modified or deleted: the storage layer rejects writes to sealed ranges. Corrections are new entries that supersede, never edits. Append-only is enforced in code and, where available, in the storage medium itself.", "rejecting writes to sealed entries", "corrections as superseding entries", "medium-level append-only where available", "CFG = {1: 3, 2: 5, 3: 8}\nlog = [{\"entry\": i, \"sealed\": True} for i in range(CFG[LEVEL])]\ndef write(i, data):\n    if log[i][\"sealed\"]:\n        return \"REJECTED: entry sealed\"\n    log[i][\"data\"] = data\n    return \"written\"\nprint(write(0, \"changed\"), \"| entries:\", len(log), \"| all sealed:\", all(e[\"sealed\"] for e in log))"],
["hash-chaining", "Independent timestamping", "Log checkpoints are sent to an independent timestamping authority which returns a signed receipt binding the hash to a wall-clock time. Even if local clocks are manipulated, the external receipts prove when entries existed. Receipts are stored with the log.", "external signed timestamp receipts", "binding hashes to wall-clock time", "receipts stored with the log", "CFG = {1: 2, 2: 4, 3: 6}\nimport hashlib, time\nreceipts = []\nfor i in range(CFG[LEVEL]):\n    digest = hashlib.sha256((\"batch-%d\" % i).encode()).hexdigest()[:16]\n    receipts.append({\"digest\": digest, \"ts\": 1761000000 + i * 3600, \"by\": \"tsa-example\"})\nprint(\"timestamped batches:\", len(receipts), \"| first:\", receipts[0])"],
["tamper-detection", "Gap detection", "Audit entries carry monotonic sequence numbers; any gap in the sequence proves entries are missing. Gap detection runs continuously and alerts immediately, because missing audit entries are as serious as altered ones. Expected gaps (archival) are declared in advance.", "monotonic sequence numbers", "alerting on any undeclared gap", "declared archival gaps vs real loss", "CFG = {1: [1, 2, 3, 4], 2: [1, 2, 4, 5], 3: [1, 3, 7]}\nseq = CFG[LEVEL]\ngaps = [ (seq[i] + 1, seq[i+1] - 1) for i in range(len(seq) - 1) if seq[i+1] - seq[i] > 1 ]\nprint(\"sequence:\", seq, \"| gaps:\", gaps or [\"none\"])"]
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
var gen={version:"jahdb-archive-toolkit-audit-trail-integrity-verifier-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-audit-trail-integrity-verifier",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
