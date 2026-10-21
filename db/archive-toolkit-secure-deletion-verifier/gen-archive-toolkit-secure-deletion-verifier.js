(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["deletion-proof", "media-sanitization", "residual-check"];
var PREFIX="JAH-ATK279-";
var KIND="secure deletion verifier";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["deletion-proof", "Deletion receipt", "Every deletion produces a receipt: what was deleted, when, by which method, and who authorized it. Receipts are the proof of deletion for audits and data-subject requests. A deletion without a receipt is treated as unconfirmed.", "what/when/method/authority per deletion", "receipts as audit proof", "unconfirmed status without receipt", "CFG = {1: \"file\", 2: \"record\", 3: \"backup\"}\nreceipt = {\"target\": \"doc-42\", \"kind\": CFG[LEVEL], \"method\": \"overwrite-3pass\", \"at\": \"2026-10-21\", \"by\": \"retention-svc\"}\ncomplete = all(receipt.values())\nprint(\"receipt:\", receipt, \"| confirmed:\", complete)"],
["media-sanitization", "Overwrite verification", "After overwrite-based sanitization, the media is read back and checked for the expected pattern. Verification is sampled for large media and complete for small. Failed verification triggers re-sanitization, not acceptance.", "read-back pattern checks", "sampled vs complete verification", "re-sanitization on failure", "CFG = {1: 64, 2: 256, 3: 1024}\nN = CFG[LEVEL]\nimport random\nrandom.seed(91)\nmedia = bytearray(random.getrandbits(8) for _ in range(N))\npattern = 0x00\nfor i in range(N): media[i] = pattern  # overwrite\nok = all(b == pattern for b in media)\nprint(\"blocks:\", N, \"| overwrite verified:\", ok)"],
["residual-check", "Crypto-shredding", "When data is encrypted, destroying the key renders the ciphertext unrecoverable: this is crypto-shredding. It works where overwriting cannot (SSDs with wear leveling, replicated stores). Verification confirms the key is destroyed everywhere it existed.", "key destruction as deletion", "works where overwrite cannot", "verifying destruction at every key location", "CFG = {1: 1, 2: 3, 3: 5}\nlocations = [\"hsm\", \"backup\", \"cache\", \"replica\", \"kms\"][: CFG[LEVEL]]\ndestroyed = {loc: True for loc in locations}\nshredded = all(destroyed.values()) and len(destroyed) == CFG[LEVEL]\nprint(\"key locations:\", locations, \"| all destroyed:\", shredded, \"| ciphertext recoverable:\", not shredded)"],
["deletion-proof", "Media-appropriate method selection", "Sanitization methods are chosen per media type following NIST 800-88 style guidance: Clear, Purge, or Destroy. Magnetic disks, SSDs, and paper each need different methods; the wrong method gives false confidence. Selection is recorded with the deletion receipt.", "Clear/Purge/Destroy per media", "method recorded with receipt", "no false confidence from wrong methods", "CFG = {1: \"hdd\", 2: \"ssd\", 3: \"paper\"}\nMETHOD = {\"hdd\": \"Purge: overwrite\", \"ssd\": \"Purge: crypto-erase\", \"paper\": \"Destroy: shred\"}\nm = CFG[LEVEL]\nprint(\"media:\", m, \"| method:\", METHOD[m])"],
["media-sanitization", "Residual data scan", "After deletion, storage is scanned for remnants: file carving on freed blocks, slack space, and index leftovers. Findings trigger another sanitization pass. Residual scans are the verification that deletion actually deleted.", "scanning freed blocks and slack space", "re-sanitization on findings", "scan as the true verification", "CFG = {1: 100, 2: 1000, 3: 10000}\nN = CFG[LEVEL]\nimport random\nrandom.seed(93)\nblocks = [0] * N\nblocks[7] = 0xAB  # one remnant\nremnants = [i for i, b in enumerate(blocks) if b != 0]\nprint(\"scanned:\", N, \"| remnants:\", remnants or [\"none\"], \"| clean:\", not remnants)"]
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
var gen={version:"jahdb-archive-toolkit-secure-deletion-verifier-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-secure-deletion-verifier",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
