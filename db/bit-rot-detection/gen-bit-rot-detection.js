(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["filesystem", "hardware", "backup", "optical", "tooling"];
var PREFIX='JAH-BITROT-';
var GENVER='jahdb-bit-rot-detection-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "checksum", "scrub", "repair"];
var DEMO_TPL="// $TITLE - bit-rot detection demo\nvar crypto = require(\"crypto\");\nfunction sum(b) { return crypto.createHash(\"sha256\").update(b).digest(\"hex\"); }\nvar data = Buffer.from(\"important payload 12345\");\nvar stored = sum(data);\ndata[5] = data[5] ^ 0x01; // silent bit flip\nvar now = sum(data);\nconsole.log(\"System: $SYSTEM | Checksum: $CHECKSUM\");\nconsole.log(\"Stored: \" + stored.slice(0, 16) + \"...\");\nconsole.log(\"Current:\" + now.slice(0, 16) + \"...\");\nconsole.log(stored === now ? \"CLEAN\" : \"BIT-ROT DETECTED -> quarantine + repair from $REPAIR\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["filesystem", "ZFS scrub", "ZFS checksums every block and scrub reads everything verifying against the Merkle tree. Checksum: Fletcher/SHA-256 per block. Scrub: zpool scrub. Repair: self-heal from mirrors.", {"system": "ZFS scrub", "checksum": "Fletcher/SHA-256 per block", "scrub": "zpool scrub", "repair": "self-heal from mirrors"}], ["filesystem", "Btrfs scrub", "Btrfs checksums data and metadata, scrubbing to find mismatches on redundant profiles. Checksum: CRC32c per extent. Scrub: btrfs scrub start. Repair: copy from good mirror.", {"system": "Btrfs scrub", "checksum": "CRC32c per extent", "scrub": "btrfs scrub start", "repair": "copy from good mirror"}], ["hardware", "ECC memory", "Error-correcting RAM fixes single-bit flips and reports multi-bit errors before they persist. Checksum: Hamming/SECDED codes. Scrub: memory controller patrol. Repair: single-bit correction.", {"system": "ECC RAM", "checksum": "Hamming/SECDED codes", "scrub": "memory controller patrol", "repair": "single-bit correction"}], ["backup", "PAR2 parity", "PAR2 creates recovery volumes so corrupted parts of an archive can be rebuilt. Checksum: MD5 per block. Scrub: par2 verify. Repair: Reed-Solomon rebuild.", {"system": "PAR2", "checksum": "MD5 per block", "scrub": "par2 verify", "repair": "Reed-Solomon rebuild"}], ["hardware", "mdadm mismatch_cnt", "mdadm’s monthly check counts mismatched RAID blocks, catching desync early. Checksum: RAID parity compare. Scrub: echo check > sync_action. Repair: resync from parity.", {"system": "mdadm check", "checksum": "RAID parity compare", "scrub": "echo check > sync_action", "repair": "resync from parity"}], ["backup", "restic check", "restic check --read-data verifies pack integrity against repository indexes. Checksum: SHA-256 content keys. Scrub: restic check --read-data. Repair: restore from other snapshots.", {"system": "restic check", "checksum": "SHA-256 content keys", "scrub": "restic check --read-data", "repair": "restore from other snapshots"}], ["backup", "SnapRAID scrub", "SnapRAID scrubs parity-protected arrays and fixes silent corruption from parity. Checksum: MurmurHash per block. Scrub: snapraid scrub. Repair: parity rebuild.", {"system": "SnapRAID", "checksum": "MurmurHash per block", "scrub": "snapraid scrub", "repair": "parity rebuild"}], ["hardware", "S.M.A.R.T.", "Drive self-tests and reallocated-sector counts predict media decay before reads fail. Checksum: drive-internal ECC. Scrub: smartctl -t long. Repair: sector reallocation.", {"system": "S.M.A.R.T.", "checksum": "drive-internal ECC", "scrub": "smartctl -t long", "repair": "sector reallocation"}], ["filesystem", "ReFS integrity streams", "Windows ReFS checksums with integrity streams, auto-correcting on mirrored spaces. Checksum: CRC64 metadata+data. Scrub: integrity scrubber. Repair: mirror copy.", {"system": "ReFS", "checksum": "CRC64 metadata+data", "scrub": "integrity scrubber", "repair": "mirror copy"}], ["filesystem", "dm-integrity", "Linux device-mapper integrity adds checksums under any filesystem for bit-rot detection. Checksum: configurable (crc32c/sha256). Scrub: read-time verify. Repair: RAID layer above.", {"system": "dm-integrity", "checksum": "configurable (crc32c/sha256)", "scrub": "read-time verify", "repair": "RAID layer above"}], ["tooling", "git fsck", "git fsck --full re-hashes every object, catching repository corruption. Checksum: SHA-1/SHA-256 objects. Scrub: git fsck --full. Repair: re-clone / reflog.", {"system": "git fsck", "checksum": "SHA-1/SHA-256 objects", "scrub": "git fsck --full", "repair": "re-clone / reflog"}], ["optical", "dvdisaster", "Adds error-correction data to optical media so scratched discs stay readable. Checksum: Reed-Solomon ECC. Scrub: read with ECC. Repair: ECC rebuild.", {"system": "dvdisaster", "checksum": "Reed-Solomon ECC", "scrub": "read with ECC", "repair": "ECC rebuild"}], ["tooling", "hashdeep", "Cross-platform recursive hashing producing audit files for later verification. Checksum: MD5/SHA-256 sets. Scrub: hashdeep -a -r -k. Repair: re-copy from source.", {"system": "hashdeep", "checksum": "MD5/SHA-256 sets", "scrub": "hashdeep -a -r -k", "repair": "re-copy from source"}], ["tooling", "cfv", "The classic checksum-file verifier supporting .sfv, .md5, and .sha1 manifests. Checksum: SFV/MD5/SHA-1. Scrub: cfv -t all. Repair: re-download flagged files.", {"system": "cfv", "checksum": "SFV/MD5/SHA-1", "scrub": "cfv -t all", "repair": "re-download flagged files"}], ["filesystem", "APFS metadata checksums", "Apple’s APFS checksums all metadata, catching filesystem-structure rot. Checksum: Fletcher64 metadata. Scrub: fsck_apfs. Repair: snapshot rollback.", {"system": "APFS", "checksum": "Fletcher64 metadata", "scrub": "fsck_apfs", "repair": "snapshot rollback"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-BITROT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bit-rot-detection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
