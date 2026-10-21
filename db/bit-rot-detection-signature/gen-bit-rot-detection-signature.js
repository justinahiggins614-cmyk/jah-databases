(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["filesystem", "hardware", "backup", "optical", "tooling"];
var PREFIX='JAH-BITROT-S-';
var GENVER='jahdb-bit-rot-detection-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["system", "checksum", "scrub", "repair"];
var DEMO_TPL="// $TITLE - bit-rot detection demo\nvar crypto = require(\"crypto\");\nfunction sum(b) { return crypto.createHash(\"sha256\").update(b).digest(\"hex\"); }\nvar data = Buffer.from(\"important payload 12345\");\nvar stored = sum(data);\ndata[5] = data[5] ^ 0x01; // silent bit flip\nvar now = sum(data);\nconsole.log(\"System: $SYSTEM | Checksum: $CHECKSUM\");\nconsole.log(\"Stored: \" + stored.slice(0, 16) + \"...\");\nconsole.log(\"Current:\" + now.slice(0, 16) + \"...\");\nconsole.log(stored === now ? \"CLEAN\" : \"BIT-ROT DETECTED -> quarantine + repair from $REPAIR\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["filesystem", "SigScrub-Cont", "Signature-original: continuous background scrubbing with I/O budgets that never disturb serving. Checksum: SHA-256 per extent. Scrub: continuous, budgeted. Repair: mesh replica copy.", {"system": "SigScrub", "checksum": "SHA-256 per extent", "scrub": "continuous, budgeted", "repair": "mesh replica copy"}], ["backup", "SigParity-Mesh", "Signature-original: erasure-coded parity striped across mesh peers, not just local disks. Checksum: per-shard hashes. Scrub: peer audits. Repair: erasure rebuild.", {"system": "SigParity", "checksum": "per-shard hashes", "scrub": "peer audits", "repair": "erasure rebuild"}], ["hardware", "SigECC-Enforce", "Signature-original: fleet policy requiring ECC on all storage hosts, verified at join. Checksum: hardware SECDED. Scrub: patrol scrub. Repair: DIMM alerts.", {"system": "SigECC", "checksum": "hardware SECDED", "scrub": "patrol scrub", "repair": "DIMM alerts"}], ["tooling", "SigManifest", "Signature-original: signed manifests for every dataset; verification is one command. Checksum: signed SHA-256. Scrub: sigmanifest verify. Repair: re-fetch signed copy.", {"system": "SigManifest", "checksum": "signed SHA-256", "scrub": "sigmanifest verify", "repair": "re-fetch signed copy"}], ["hardware", "SigWatch-SMART", "Signature-original: fleet SMART aggregation predicting drive failure weeks ahead. Checksum: drive telemetry. Scrub: continuous. Repair: preemptive migration.", {"system": "SigWatch-SMART", "checksum": "drive telemetry", "scrub": "continuous", "repair": "preemptive migration"}], ["backup", "SigRepair-Auto", "Signature-original: automatic repair from the nearest healthy replica on detection. Checksum: replica compare. Scrub: on-read verify. Repair: auto re-replicate.", {"system": "SigRepair", "checksum": "replica compare", "scrub": "on-read verify", "repair": "auto re-replicate"}], ["tooling", "SigAudit-Chain", "Signature-original: hash-chained audit logs proving data was intact at every check. Checksum: chained hashes. Scrub: scheduled. Repair: alert + quarantine.", {"system": "SigAudit", "checksum": "chained hashes", "scrub": "scheduled", "repair": "alert + quarantine"}], ["backup", "SigSnap-Verify", "Signature-original: snapshots verified at creation so restores never surprise. Checksum: creation-time hash. Scrub: verify-on-write. Repair: re-snapshot.", {"system": "SigSnap-Verify", "checksum": "creation-time hash", "scrub": "verify-on-write", "repair": "re-snapshot"}], ["backup", "SigTape", "Signature-original: tape-tier verification with two independent hash algorithms. Checksum: SHA-256 + BLAKE3. Scrub: restore sampling. Repair: second copy.", {"system": "SigTape", "checksum": "SHA-256 + BLAKE3", "scrub": "restore sampling", "repair": "second copy"}], ["optical", "SigOptical", "Signature-original: archival optical with ECC volumes sized for 50-year retention. Checksum: Reed-Solomon. Scrub: annual read. Repair: ECC rebuild.", {"system": "SigOptical", "checksum": "Reed-Solomon", "scrub": "annual read", "repair": "ECC rebuild"}], ["backup", "SigDB-Page", "Signature-original: database page checksums verified on every read with torn-page detection. Checksum: per-page CRC. Scrub: read-time. Repair: replica page.", {"system": "SigDB-Page", "checksum": "per-page CRC", "scrub": "read-time", "repair": "replica page"}], ["tooling", "SigNet-Transfer", "Signature-original: transfer checksums end-to-end so network corruption is caught. Checksum: stream hashes. Scrub: per-transfer. Repair: retransmit.", {"system": "SigNet", "checksum": "stream hashes", "scrub": "per-transfer", "repair": "retransmit"}], ["backup", "SigCold", "Signature-original: cold-storage audits with random sampling and full annual reads. Checksum: manifest hashes. Scrub: sampled + annual. Repair: multi-copy restore.", {"system": "SigCold", "checksum": "manifest hashes", "scrub": "sampled + annual", "repair": "multi-copy restore"}], ["tooling", "SigReport", "Signature-original: fleet integrity dashboard with per-dataset health scores. Checksum: aggregated. Scrub: continuous. Repair: workflow dispatch.", {"system": "SigReport", "checksum": "aggregated", "scrub": "continuous", "repair": "workflow dispatch"}], ["filesystem", "SigIntegrity-One", "Signature-original: the united integrity plane — every byte checksummed, everywhere. Checksum: universal. Scrub: continuous. Repair: auto from mesh.", {"system": "SigIntegrity-One", "checksum": "universal", "scrub": "continuous", "repair": "auto from mesh"}]];
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
  if(!new RegExp('^'+'JAH\\-BITROT\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bit-rot-detection-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
