(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["sync", "backup", "update", "binary", "protocol"];
var PREFIX='JAH-BLD-S-';
var GENVER='jahdb-block-level-delta-compression-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tool", "algorithm", "granularity", "use"];
var DEMO_TPL="// $TITLE - rolling-checksum delta demo\nfunction weak(buf) { var s = 0; for (var i = 0; i < buf.length; i++) s = (s + buf.charCodeAt(i)) % 65521; return s; }\nvar oldBlk = \"hello world, this is block one!!\", newBlk = \"hello world, this is block two!!\";\nvar sigs = {}; sigs[weak(oldBlk)] = 0;\nvar matches = weak(newBlk) in sigs;\nconsole.log(\"Tool: $TOOL | Algorithm: $ALGORITHM\");\nconsole.log(\"Old block checksum: \" + weak(oldBlk) + \" | New block checksum: \" + weak(newBlk));\nconsole.log(matches ? \"MATCH: block reused, send nothing\" : \"DIFF: send literal bytes only\");\nconsole.log(\"Delta computed -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["sync", "SigDelta-Roll", "Signature-original: rolling-checksum sync with adaptive block sizes per file type. Algorithm: adaptive rolling checksum; granularity: adaptive block. Used for: file sync.", {"tool": "SigDelta-Roll", "algorithm": "adaptive rolling checksum", "granularity": "adaptive block", "use": "file sync"}], ["binary", "SigDelta-Bin", "Signature-original: binary differ understanding ELF/Mach-O section moves. Algorithm: section-aware diff; granularity: section. Used for: binary patches.", {"tool": "SigDelta-Bin", "algorithm": "section-aware diff", "granularity": "section", "use": "binary patches"}], ["sync", "SigDelta-Mesh", "Signature-original: deltas fetched from the nearest mesh peer instead of origin. Algorithm: peer delta exchange; granularity: chunk. Used for: mesh updates.", {"tool": "SigDelta-Mesh", "algorithm": "peer delta exchange", "granularity": "chunk", "use": "mesh updates"}], ["update", "SigDelta-Stream", "Signature-original: streaming deltas applied while still downloading. Algorithm: streaming VCDIFF; granularity: window. Used for: live updates.", {"tool": "SigDelta-Stream", "algorithm": "streaming VCDIFF", "granularity": "window", "use": "live updates"}], ["backup", "SigDelta-DB", "Signature-original: database page deltas with write-ahead coordination. Algorithm: page diff; granularity: page. Used for: DB replication.", {"tool": "SigDelta-DB", "algorithm": "page diff", "granularity": "page", "use": "DB replication"}], ["backup", "SigDelta-VM", "Signature-original: VM image deltas tracking dirty pages from the hypervisor. Algorithm: dirty-page diff; granularity: page. Used for: VM backup.", {"tool": "SigDelta-VM", "algorithm": "dirty-page diff", "granularity": "page", "use": "VM backup"}], ["binary", "SigDelta-Media", "Signature-original: media-aware deltas keyed on scene cuts for video. Algorithm: scene-keyed diff; granularity: frame group. Used for: video sync.", {"tool": "SigDelta-Media", "algorithm": "scene-keyed diff", "granularity": "frame group", "use": "video sync"}], ["binary", "SigDelta-Model", "Signature-original: model-weight deltas shipping only changed tensors. Algorithm: tensor diff; granularity: tensor. Used for: AI model updates.", {"tool": "SigDelta-Model", "algorithm": "tensor diff", "granularity": "tensor", "use": "AI model updates"}], ["sync", "SigDelta-FS", "Signature-original: filesystem-level delta sync built into the Sig filesystem. Algorithm: extent diff; granularity: extent. Used for: FS replication.", {"tool": "SigDelta-FS", "algorithm": "extent diff", "granularity": "extent", "use": "FS replication"}], ["binary", "SigDelta-Patch", "Signature-original: signed delta patches with rollback on failed apply. Algorithm: signed VCDIFF; granularity: byte. Used for: secure updates.", {"tool": "SigDelta-Patch", "algorithm": "signed VCDIFF", "granularity": "byte", "use": "secure updates"}], ["sync", "SigDelta-Cache", "Signature-original: cache-fill deltas warming edge caches with minimal transfer. Algorithm: cache diff; granularity: object. Used for: CDN warming.", {"tool": "SigDelta-Cache", "algorithm": "cache diff", "granularity": "object", "use": "CDN warming"}], ["sync", "SigDelta-Config", "Signature-original: config deltas with semantic merge for structured files. Algorithm: tree diff; granularity: node. Used for: config sync.", {"tool": "SigDelta-Config", "algorithm": "tree diff", "granularity": "node", "use": "config sync"}], ["backup", "SigDelta-Log", "Signature-original: log-structured deltas for append-mostly datasets. Algorithm: segment diff; granularity: segment. Used for: log shipping.", {"tool": "SigDelta-Log", "algorithm": "segment diff", "granularity": "segment", "use": "log shipping"}], ["sync", "SigDelta-Airgap", "Signature-original: sneakernet deltas sized for USB couriers between sites. Algorithm: courier chunking; granularity: courier chunk. Used for: air-gap sync.", {"tool": "SigDelta-Airgap", "algorithm": "courier chunking", "granularity": "courier chunk", "use": "air-gap sync"}], ["sync", "SigDelta-One", "Signature-original: the united delta plane — one algorithm family for every payload. Algorithm: SigDelta family; granularity: adaptive. Used for: everything.", {"tool": "SigDelta-One", "algorithm": "SigDelta family", "granularity": "adaptive", "use": "everything"}]];
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
  if(!new RegExp('^'+'JAH\\-BLD\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('block-level-delta-compression-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
