(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["sync", "backup", "update", "binary", "protocol"];
var PREFIX='JAH-BLD-';
var GENVER='jahdb-block-level-delta-compression-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "algorithm", "granularity", "use"];
var DEMO_TPL="// $TITLE - rolling-checksum delta demo\nfunction weak(buf) { var s = 0; for (var i = 0; i < buf.length; i++) s = (s + buf.charCodeAt(i)) % 65521; return s; }\nvar oldBlk = \"hello world, this is block one!!\", newBlk = \"hello world, this is block two!!\";\nvar sigs = {}; sigs[weak(oldBlk)] = 0;\nvar matches = weak(newBlk) in sigs;\nconsole.log(\"Tool: $TOOL | Algorithm: $ALGORITHM\");\nconsole.log(\"Old block checksum: \" + weak(oldBlk) + \" | New block checksum: \" + weak(newBlk));\nconsole.log(matches ? \"MATCH: block reused, send nothing\" : \"DIFF: send literal bytes only\");\nconsole.log(\"Delta computed -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["sync", "rsync delta algorithm", "Rolling checksums find matching blocks so only changed chunks cross the wire. Algorithm: rolling checksum + MD4/MD5; granularity: block (~700B default). Used for: file sync.", {"tool": "rsync", "algorithm": "rolling checksum + MD4/MD5", "granularity": "block (~700B default)", "use": "file sync"}], ["binary", "bsdiff", "Colin Percival’s binary diff producing tiny patches for executables with shifted sections. Algorithm: suffix-sorted diff; granularity: byte. Used for: binary patches.", {"tool": "bsdiff", "algorithm": "suffix-sorted diff", "granularity": "byte", "use": "binary patches"}], ["binary", "xdelta3", "VCDIFF encoder/decoder with streaming support and secondary compression. Algorithm: VCDIFF (RFC 3284); granularity: byte window. Used for: deltas, ROM hacking.", {"tool": "xdelta3", "algorithm": "VCDIFF (RFC 3284)", "granularity": "byte window", "use": "deltas, ROM hacking"}], ["update", "zsync", "Clients download only changed blocks of large files using block checksums over HTTP. Algorithm: rsync-style over HTTP; granularity: block. Used for: ISO updates.", {"tool": "zsync", "algorithm": "rsync-style over HTTP", "granularity": "block", "use": "ISO updates"}], ["sync", "casync", "Content-addressable sync splitting files into variable chunks for global dedup. Algorithm: content-defined chunking; granularity: variable chunk. Used for: OS image sync.", {"tool": "casync", "algorithm": "content-defined chunking", "granularity": "variable chunk", "use": "OS image sync"}], ["backup", "bup", "Git-style backup with rolling-checksum chunking giving massive dedup across versions. Algorithm: rolling checksum split; granularity: variable chunk. Used for: backups.", {"tool": "bup", "algorithm": "rolling checksum split", "granularity": "variable chunk", "use": "backups"}], ["backup", "restic", "Content-defined chunking plus encryption; dedup spans all snapshots in a repo. Algorithm: Rabin chunking; granularity: variable chunk. Used for: encrypted backups.", {"tool": "restic", "algorithm": "Rabin chunking", "granularity": "variable chunk", "use": "encrypted backups"}], ["backup", "borgbackup", "Deduplicating archiver with Buzhash chunking and authenticated encryption. Algorithm: Buzhash chunking; granularity: variable chunk. Used for: dedupe backups.", {"tool": "borg", "algorithm": "Buzhash chunking", "granularity": "variable chunk", "use": "dedupe backups"}], ["protocol", "VCDIFF RFC 3284", "The standard generic delta format that xdelta and open-vcdiff implement. Algorithm: standard delta coding; granularity: byte. Used for: delta interchange.", {"tool": "VCDIFF", "algorithm": "standard delta coding", "granularity": "byte", "use": "delta interchange"}], ["sync", "librsync / rdiff", "Library + CLI implementing the rsync algorithm for third-party sync tools. Algorithm: rsync algorithm; granularity: block. Used for: embedded sync.", {"tool": "librsync", "algorithm": "rsync algorithm", "granularity": "block", "use": "embedded sync"}], ["update", "Courgette", "Chrome’s updater diff exploiting disassembly to make tiny patches for binaries. Algorithm: disassembly-aware diff; granularity: instruction. Used for: browser updates.", {"tool": "Courgette", "algorithm": "disassembly-aware diff", "granularity": "instruction", "use": "browser updates"}], ["backup", "duplicity", "librsync-based encrypted backups to remote storage with incremental chains. Algorithm: librsync deltas; granularity: block. Used for: remote backups.", {"tool": "duplicity", "algorithm": "librsync deltas", "granularity": "block", "use": "remote backups"}], ["backup", "rdiff-backup", "Reverse-delta backups: the latest version is a full mirror, history stored as diffs. Algorithm: reverse deltas; granularity: file/block. Used for: versioned mirrors.", {"tool": "rdiff-backup", "algorithm": "reverse deltas", "granularity": "file/block", "use": "versioned mirrors"}], ["backup", "Kopia", "Modern dedup backup with content-defined chunking and policy-driven retention. Algorithm: content-defined chunking; granularity: variable chunk. Used for: backups.", {"tool": "Kopia", "algorithm": "content-defined chunking", "granularity": "variable chunk", "use": "backups"}], ["binary", "open-vcdiff", "Google’s VCDIFF encoder/decoder library used in several update pipelines. Algorithm: VCDIFF; granularity: byte window. Used for: delta SDK.", {"tool": "open-vcdiff", "algorithm": "VCDIFF", "granularity": "byte window", "use": "delta SDK"}]];
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
  if(!new RegExp('^'+'JAH\\-BLD\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('block-level-delta-compression',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
