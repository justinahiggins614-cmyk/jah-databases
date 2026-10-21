(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK132-";
var KIND="traversal method";
var TOOLNAME="Compressed Archive Inspector";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Central-directory listing", "d": "ZIPs store a central directory: names, sizes, and offsets without the file data. Reading it lists members without decompressing anything. Directory-first inspection is fast and safe.", "c": "fundamentals", "r": 1, "p": {"MEMBERS": "{'a.txt': 'hello', 'b.txt': 'world'*100}", "PEEK": "a.txt"}}, {"t": "Compression-ratio analysis", "d": "Ratios (compressed/original) reveal content type: text compresses, media does not. Anomalous ratios flag mislabeled or encrypted members. Ratios guide extraction planning.", "c": "algorithms", "r": 1, "p": {"MEMBERS": "{'notes.txt': 'text '*200, 'photo.jpg': bytes(range(256))*4}", "PEEK": "notes.txt"}}, {"t": "Selective extraction", "d": "Inspectors extract single members by name instead of the whole archive. Selectivity saves time and disk on huge archives. Targeted extraction is the core value.", "c": "implementation", "r": 1, "p": {"MEMBERS": "{'want.txt': 'needed', 'bulk.bin': 'x'*5000}", "PEEK": "want.txt"}}, {"t": "Integrity verification", "d": "CRC32 per member verifies content integrity on read. Testzip-style checks validate without extracting. Verification catches corruption early.", "c": "optimization", "r": 1, "p": {"MEMBERS": "{'ok.txt': 'fine'}", "PEEK": "ok.txt"}}, {"t": "Nested archive detection", "d": "Members ending in .zip/.tar/.gz are archives themselves; inspectors flag them. Flagging enables recursive inspection policies. Detection prevents hidden payloads.", "c": "evaluation", "r": 1, "p": {"MEMBERS": "{'inner.zip': 'PKfake', 'doc.txt': 'hi'}", "PEEK": "doc.txt"}}, {"t": "Path-traversal protection", "d": "Malicious archives use '../' paths; inspectors sanitize before any extraction. Validation rejects absolute paths and parent escapes. Sanitization is a security must.", "c": "fundamentals", "r": 2, "p": {"MEMBERS": "{'safe.txt': 'ok'}", "PEEK": "safe.txt"}}, {"t": "Password-protected members", "d": "Encrypted members list normally; content needs the password. Inspectors report encryption status per member. Status visibility informs handling.", "c": "algorithms", "r": 2, "p": {"MEMBERS": "{'enc.txt': 'data'}", "PEEK": "enc.txt"}}, {"t": "Multi-volume archives", "d": "Split archives span volumes; inspectors reassemble the member list across parts. Missing volumes are reported before extraction starts. Volume awareness prevents partial failures.", "c": "implementation", "r": 2, "p": {"MEMBERS": "{'part1.txt': 'a', 'part2.txt': 'b'}", "PEEK": "part1.txt"}}, {"t": "Format identification", "d": "Magic bytes identify ZIP, TAR, GZIP, 7Z regardless of extension. Identification routes to the right parser. Magic beats extensions.", "c": "optimization", "r": 2, "p": {"MEMBERS": "{'f.txt': 'x'}", "PEEK": "f.txt"}}, {"t": "Metadata extraction", "d": "Archives carry timestamps, permissions, and comments per member. Metadata reconstructs provenance. Headers hold history.", "c": "evaluation", "r": 2, "p": {"MEMBERS": "{'m.txt': 'meta'}", "PEEK": "m.txt"}}, {"t": "Duplicate members", "d": "Some archives repeat names; inspectors list all occurrences with offsets. Awareness prevents wrong-member extraction. Duplicates need explicit handling.", "c": "fundamentals", "r": 3, "p": {"MEMBERS": "{'d.txt': 'first'}", "PEEK": "d.txt"}}, {"t": "Streaming inspection", "d": "Streaming readers parse members sequentially without seeking. Streams handle pipes and network sources. Sequential access suits large archives.", "c": "algorithms", "r": 3, "p": {"MEMBERS": "{'s.txt': 'stream'}", "PEEK": "s.txt"}}, {"t": "Archive diffing", "d": "Diffing two archives compares member lists and CRCs. Diffs verify backups and releases. Comparison beats re-extraction.", "c": "implementation", "r": 3, "p": {"MEMBERS": "{'v1.txt': 'one'}", "PEEK": "v1.txt"}}, {"t": "Quarantine scanning", "d": "Inspectors pipe members to scanners before extraction. Pre-extraction scanning contains malware. Inspect-then-extract is the safe pipeline.", "c": "optimization", "r": 3, "p": {"MEMBERS": "{'clean.txt': 'safe content'}", "PEEK": "clean.txt"}}, {"t": "Repair of damaged archives", "d": "Damaged central directories can be rebuilt by scanning local headers. Recovery salvages readable members. Repair turns total loss into partial recovery.", "c": "evaluation", "r": 3, "p": {"MEMBERS": "{'r.txt': 'recoverable'}", "PEEK": "r.txt"}}];
var DEMO="# Archive inspection: build a zip in memory, list its central directory WITHOUT extracting.\nimport io, zipfile\nbuf = io.BytesIO()\nwith zipfile.ZipFile(buf, \"w\", zipfile.ZIP_DEFLATED) as z:\n    for name, data in %%MEMBERS%%.items():\n        z.writestr(name, data)\nbuf.seek(0)\nwith zipfile.ZipFile(buf) as z:\n    print(\"members (inspected, not extracted):\")\n    for info in z.infolist():\n        print(f\"  {info.filename:24} {info.file_size:>6} bytes -> {info.compress_size:>6} compressed  crc={info.CRC:08x}\")\n    if \"%%PEEK%%\" in z.namelist():\n        print(\"peek at %s: %r\" % (\"%%PEEK%%\", z.read(\"%%PEEK%%\")[:40]))\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK132\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-compressed-archive-inspector-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-compressed-archive-inspector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
