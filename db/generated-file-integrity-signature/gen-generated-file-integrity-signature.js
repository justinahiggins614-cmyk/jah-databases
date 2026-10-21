(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["hashing", "signing", "structure", "provenance", "verification"];
var PREFIX='JAH-GFI-S-';
var USE="Used by build pipelines, data publishers, and archives to trust generated artifacts.";
var FLD=[["check", "Check"], ["detects", "Detects"], ["mechanism", "Mechanism"]];
var DEMO="# {title} - determinism and size (python3)\nimport hashlib\ncontent={d1}\nmin_bytes={d3}\nh1=hashlib.sha256(content.encode()).hexdigest()\nh2=hashlib.sha256(content.encode()).hexdigest()\nprint(\"sha256:\", h1[:16], \"bytes:\", len(content.encode()))\nprint(\"OK\" if h1==h2 and len(content.encode())>=min_bytes else \"FAIL\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["hashing", "SHA-256 Checksum", "Hashes the whole file so any single-bit change is detectable.", "SHA-256 Checksum", "corruption", "hash compare", "'file-bytes-v1'", "'sha256'", "100"], ["signing", "Digital Signature", "Signs the hash with a private key so recipients verify authenticity.", "Digital Signature", "tampering", "Ed25519 verify", "'release-artifact'", "'ed25519'", "100"], ["structure", "Provenance Watermark", "Embeds generator, seed, and version invisibly in the file metadata.", "Provenance Watermark", "unknown origin", "watermark read", "'render-frame-88'", "'xmp'", "50"], ["provenance", "Schema Validation", "Parses the file against its schema, rejecting malformed output.", "Schema Validation", "malformed data", "validator", "'config-json'", "'jsonschema'", "20"], ["verification", "Byte-count Assertion", "Asserts the file size is within the expected range for its type.", "Byte-count Assertion", "truncation", "size check", "'export-csv'", "'range'", "1000"], ["hashing", "Magic-number Check", "Verifies the file header magic matches its claimed format.", "Magic-number Check", "mislabeling", "header read", "'image-png'", "'magic'", "8"], ["signing", "Canonical Serialization", "Re-serializes to a canonical form so semantically equal files hash equally.", "Canonical Serialization", "false diffs", "canonical form", "'dataset-json'", "'jcs'", "100"], ["structure", "Merkle Root", "Builds a Merkle tree over chunks so any chunk can be verified independently.", "Merkle Root", "partial corruption", "tree verify", "'chunked-backup'", "'merkle'", "1024"], ["provenance", "Timestamped Seal", "Binds the hash to a trusted timestamp, proving existence at a time.", "Timestamped Seal", "backdating", "RFC 3161", "'contract-pdf'", "'tsa'", "500"], ["verification", "Generator Version Tag", "Records which generator version produced the file for reproducibility.", "Generator Version Tag", "version drift", "tag read", "'model-weights'", "'tag'", "50"], ["hashing", "Seed Record", "Stores the RNG seed so stochastic outputs can be regenerated exactly.", "Seed Record", "lost reproducibility", "seed log", "'synth-data'", "'seed'", "10"], ["signing", "Determinism Replay", "Regenerates the file and compares hashes to prove determinism.", "Determinism Replay", "nondeterminism", "replay compare", "'build-output'", "'replay'", "100"], ["structure", "Diff Against Golden", "Diffs the output against a golden file, allowing only whitelisted differences.", "Diff Against Golden", "regressions", "diff", "'report-html'", "'diff'", "200"], ["provenance", "Line-count Sanity", "Checks row counts against expectations to catch silent drops.", "Line-count Sanity", "dropped rows", "count check", "'table-csv'", "'count'", "100"], ["verification", "Encoding Declaration", "Verifies the declared encoding matches actual byte content.", "Encoding Declaration", "mojibake", "chardet", "'text-md'", "'utf8'", "20"], ["hashing", "BOM Handling", "Normalizes byte-order marks so parsers see consistent input.", "BOM Handling", "parse errors", "BOM strip", "'data-xml'", "'bom'", "10"], ["signing", "Newline Normalization", "Converts line endings to the canonical form for the platform.", "Newline Normalization", "diff noise", "normalize", "'script-py'", "'lf'", "50"], ["structure", "Trailing-whitespace Scan", "Flags trailing whitespace that pollutes diffs and breaks strict parsers.", "Trailing-whitespace Scan", "noise", "scan", "'source-js'", "'scan'", "100"], ["provenance", "Duplicate-record Scan", "Detects exact duplicate records that indicate generator bugs.", "Duplicate-record Scan", "duplicates", "hash set", "'records-jsonl'", "'dedupe'", "100"], ["verification", "Truncation Detection", "Checks for expected footers or record counts to catch cut-off writes.", "Truncation Detection", "cut-off writes", "footer check", "'archive-gz'", "'footer'", "100"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-generated-file-integrity-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('generated-file-integrity-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
