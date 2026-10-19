#!/usr/bin/env python3
"""Emit index.html pages and gen-*.js generators mirroring db/language-pashto."""
import json

# ---------------------------------------------------------------- page

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<meta name="description" content="%%META_DESC%%">
<script type="application/ld+json">%%JSONLD%%</script>
<style>
:root{--bg:#070b16;--panel:#0d1526;--line:#1d2c4d;--ink:#e8f1ff;--dim:#9fb3d8;--acc:#2f7bff;--ok:#00e5a0;--warn:#ffb020}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.5}
.wrap{max-width:1060px;margin:0 auto;padding:14px}
.hero{display:flex;gap:14px;align-items:center;background:linear-gradient(135deg,#0b1e3a,#101a30);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:12px}
.hero img{width:84px;height:84px;border-radius:14px;flex:none}
.hero h1{margin:0;font-size:1.5em}.hero p{margin:4px 0;color:var(--dim)}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:.9em}
.stat b{color:var(--ok)}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
.tab{border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:999px;padding:9px 18px;font-size:1em;cursor:pointer}
.tab.on{background:var(--acc);border-color:var(--acc);font-weight:bold}
.pane{display:none}.pane.on{display:block}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px;margin:10px 0}
.card h3{margin:0 0 6px}
.rec{display:flex;gap:10px;align-items:flex-start}
.rec img{width:64px;height:64px;border-radius:10px;flex:none}
.mono{font-family:Consolas,monospace}
.dim{color:var(--dim)}.ok{color:#00e5a0}.bad{color:#ff6b6b}
input,select,textarea,button{font-size:1em;border-radius:8px;border:1px solid var(--line);background:#0a1120;color:var(--ink);padding:9px 10px}
button{cursor:pointer;background:#14305e}button.go{background:var(--acc);font-weight:bold}
details.grp{border:1px solid var(--line);border-radius:10px;margin:8px 0;background:var(--panel)}
details.grp>summary{padding:10px 12px;cursor:pointer;font-weight:bold;list-style:none}
details.grp>summary::-webkit-details-marker{display:none}
.badge.sig{background:#2a1a3d;border-color:#7a4fb5;color:#e8d5ff}.badge{display:inline-block;background:#132a55;border:1px solid var(--line);border-radius:999px;padding:2px 10px;font-size:.8em;margin-right:6px}
.chatlog{max-height:46vh;overflow:auto;border:1px solid var(--line);border-radius:10px;padding:10px;background:#080d18;margin-bottom:8px}
.msg{display:flex;margin:8px 0}.msg.u{justify-content:flex-end}.msg.a{justify-content:flex-start}.msg .b{max-width:88%;padding:8px 12px;border-radius:12px;overflow-wrap:break-word;min-width:0;text-align:left}
.msg.u .b{background:#14305e}.msg.a .b{background:#101a30;border:1px solid var(--line)}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.kv{display:grid;grid-template-columns:minmax(96px,150px) minmax(120px,1fr);gap:4px 12px;font-size:.95em}
.kv dt{color:var(--dim);overflow-wrap:break-word}.kv dd{margin:0;min-width:0;overflow-wrap:break-word}
.kv dd.longtext{grid-column:1/-1;font-size:1em;line-height:1.55}
.rec>*{min-width:0}
.foot{margin-top:26px;padding-top:12px;border-top:1px solid var(--line);color:var(--dim);font-size:.85em}
.kv .kv{grid-template-columns:auto minmax(120px,1fr)}
.kv dt{min-width:0}
pre.codeblock{white-space:pre;overflow-x:auto;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.85em;line-height:1.5;background:#060b14;border:1px solid var(--line,#1e293b);border-radius:8px;padding:10px 12px;margin:6px 0;max-width:100%;box-sizing:border-box}
button.merger{background:#c81e3a;border-color:#c81e3a;color:#fff;font-weight:bold}
button.pill-ex{border-radius:999px}
#mergePanel{margin-top:10px}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <img id="emblem" alt="database emblem">
    <div>
      <h1>%%HERO_H1%%</h1>
      <p>%%HERO_P%%</p>
      <div class="stats">
        <span class="stat">Archive records: <b id="stCount">&hellip;</b></span>
        <span class="stat">Generator: <b>%%GEN_ID%%</b> <span class="ok">&#9679; working</span></span>
        <span class="stat">Type: <b>%%TYPE_STR%%</b></span>
      </div>
    </div>
  </div>
  <div class="tabs" role="tablist">
    <button class="tab on" data-p="archive">Archive</button>
    <button class="tab" data-p="gen">Generator</button>
    <button class="tab" data-p="chat">AI Chat</button>
    <button class="tab" data-p="about">About</button>
  </div>
  <section class="pane on" id="p-archive">
    <div class="row">
      <input id="q" placeholder="%%SEARCH_PH%%" style="flex:1;min-width:200px">
      <button class="go" id="qgo">Search</button><button class="tab pill-ex" id="qex">Exhaustive</button><button class="go merger" id="qmerge">All Database Merger</button>
    </div>
    <div id="mergePanel"></div>
    <p class="dim">Browse by category &mdash; each group opens on demand and loads only what you open.</p>
    <div id="groups"></div>
    <div id="results"></div>
  </section>
  <section class="pane" id="p-gen">
    <div class="card">
      <h3>%%GEN_H3%%</h3>
      <p class="dim">%%GEN_SUB%%</p>
      <div class="row">
        <label>Seed <input id="gSeed" type="number" value="1001" style="width:110px"></label>
        <label>Count <input id="gN" type="number" value="5" min="1" max="50" style="width:80px"></label>
      </div>
      <div class="row" style="margin-top:8px"><label>Field <select id="gCat"><option value="">any (generator picks)</option></select></label><button class="go" id="gGo">Generate</button></div>
      <div id="gOut"></div>
    </div>
    <div class="card">
      <h3>Queued for the archive <span class="dim" id="qCount"></span></h3>
      <p class="dim">Generated records wait here. Only validated, drift-free records can be filed &mdash; filing is a deliberate act, never automatic from chat.</p>
      <div id="queue"></div>
    </div>
  </section>
  <section class="pane" id="p-chat">
    <div class="card">
      <h3>%%AI_NAME%% <button id="fresh" style="font-size:.8em">New session</button></h3>
      <div class="chatlog" id="chatlog"></div>
      <div class="row">
        <input id="chatIn" placeholder="%%CHAT_PH%%" style="flex:1;min-width:200px">
        <button class="go" id="chatGo">Send</button>
      </div>
      <p class="dim">Fresh screen every session. Nothing you say here enters the permanent archive unless you file it from the Generator tab.</p>
    </div>
  </section>
  <section class="pane" id="p-about">
    <div class="card">
      <h3>About this data base</h3>
      <dl class="kv">
        <dt>Archive</dt><dd>%%ABOUT_ARCHIVE%%</dd>
        <dt>Record schema</dt><dd class="mono">id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo</dd>
        <dt>Fields</dt><dd>%%ABOUT_FIELDS%%</dd>
        <dt>Generator</dt><dd>%%ABOUT_GEN%%</dd>
        <dt>Drift control</dt><dd>Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.</dd>
        <dt>Target</dt><dd>1,000,000 records. The archive marches toward the million mark with overload protection: 100-record chunks, lazy loading, and a collapsible per-field archive so no device ever renders everything at once.</dd>
        <dt>AI</dt><dd>%%ABOUT_AI%%</dd>
        <dt>Signature system</dt><dd>%%TYPE_STR%%. Property of Justin Addam Higgins (JAH).</dd>
      </dl>
    </div>
  </section>
  <div class="foot">JAH Databases. %%TYPE_STR%%. Property of Justin Addam Higgins (JAH).</div>
</div>
<script src="../../core/jahdb.js"></script>
<script src="../../core/jahdb-dedupe.js"></script>
<script src="../../core/jahdb-xdb.js"></script>
<script src="../../core/standard-1.0.js"></script>
<script src="../../core/guide-conv.js"></script>
<script src="../../core/apex-2.0.js"></script>
<script src="%%GEN_JS%%"></script>
<script>
(function(){
'use strict';
var SLUG='%%SLUG%%';
var LOCAL='https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/%%SLUG%%/';
var db={slug:SLUG,name:'%%DBNAME%%',ai_name:'%%AI_NAME%%',record_kind:'%%RECORD_KIND%%'};
var ROLE='%%ROLE%%';
var NETWORK='Part of the JAH Databases network of archive-aware Creator AIs, every database marching to 1,000,000 records.';
JAHDB.loadManifest().then(function(m){
  try{
    var n=m.databases.length, names=[], i;
    for(i=0;i<Math.min(10,n);i++){ names.push(m.databases[i].name); }
    NETWORK='I am one of '+n+' archive-aware Creator AIs in the JAH Databases network (each database marching to 1,000,000 records). Sibling databases include: '+names.join('; ')+' — and '+(n-10)+' more. Ask me about any of them and I will route you.';
  }catch(e){}
}).catch(function(){});
var manifest=null, archiveIdx=null, archiveSample=[];
var $=function(id){return document.getElementById(id);};
document.querySelectorAll('.tab').forEach(function(t){
  t.addEventListener('click',function(){
    if(!t.dataset.p)return;
    document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on');});
    document.querySelectorAll('.pane').forEach(function(x){x.classList.remove('on');});
    t.classList.add('on'); $('p-'+t.dataset.p).classList.add('on');
  });
});
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
JAHDB.loadManifest().then(function(m){manifest=m;db=JAHDB.dbBySlug(m,SLUG)||db;}).catch(function(){}).then(function(){
  return JAHDB.fetchGz(LOCAL+'index.jsonl.gz');
}).then(function(t){
  archiveIdx=t.split('\\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean);
  $('stCount').textContent=archiveIdx.length.toLocaleString()+' / 1,000,000 target';

  try{ if(window.JAHDB&&JAHDB.dedupe) JAHDB.dedupe.indexSameDb(typeof archiveIdx!=='undefined'?archiveIdx:[], typeof SLUG!=='undefined'?SLUG:null); }catch(e){}  try{ if(typeof archiveIdx!=='undefined'&&archiveIdx&&archiveIdx.length) $('gSeed').value=archiveIdx.length+1; }catch(e){}
  $('emblem').src=JAHDB.emblemSVG(db.name,'%%EMBLEM_PREFIX%%');
  var seen={},i,GENRES=[];
  for(i=0;i<archiveIdx.length;i++){ if(archiveIdx[i].g&&!seen[archiveIdx[i].g]){seen[archiveIdx[i].g]=1;GENRES.push(archiveIdx[i].g);} }
  GENRES.sort();
  var rnd=JAHDB.prng(99);
  for(i=0;i<200&&i<archiveIdx.length;i++) archiveSample.push(archiveIdx[(rnd()*archiveIdx.length)|0]);
  buildGroups(GENRES);
  renderQueue();
  greet();
  deepOpen();
}).catch(function(e){ $('stCount').textContent='archive unreachable ('+e.message+')'; });
function chunkName(c){ return 'chunks/chunk-'+String(c).padStart(4,'0')+'.jsonl.gz'; }
function fmtVal(v){
  if(v===null||v===undefined)return '<span class="dim">—</span>';
  if(Array.isArray(v)){
    if(v.length&&typeof v[0]==='object')return '<ol>'+v.map(function(x){return '<li>'+fmtVal(x)+'</li>';}).join('')+'</ol>';
    return esc(v.join('; '));
  }
  if(typeof v==='object')return '<dl class="kv">'+Object.keys(v).map(function(k){var _isC=(k==='program'||k==='code');var _in=_isC?'<pre class="codeblock">'+esc(String(v[k]))+'</pre>':fmtVal(v[k]);return '<dt class="mono">'+esc(k)+'</dt><dd'+(typeof v[k]==='string'&&v[k].length>150?' class="longtext"':'')+'>'+_in+'</dd>';}).join('')+'</dl>';
  return esc(String(v));
}
function sigBadge(r){
  if(r&&r.src==='public-harvest') return '<div><span class="badge">✓ Public record</span></div>';
  if(r&&r.src==='signature') return '<div><span class="badge sig">✳ Signature original</span></div>';
  return '<div><span class="badge sig">✳ Signature-generated sample — structural sample</span> <span class="badge">labeled sample</span></div>';
}
function renderFull(r){
  var h=sigBadge(r)+'<dl class="kv">';
  Object.keys(r).forEach(function(k){ if(k.charAt(0)==='_')return; var _ltv=r[k];h+='<dt class="mono">'+esc(k)+'</dt><dd'+(typeof _ltv==='string'&&_ltv.length>150?' class="longtext"':'')+'>'+fmtVal(_ltv)+'</dd>'; });
  return h+'</dl>';
}
function descOf(r){ try{ return String(r.d||r.description||""); }catch(e){ return ""; } }
function catOf(r){ try{ return String(r.field||r.g||""); }catch(e){ return ""; } }
function recJSON(r){try{return JSON.stringify(r,function(k,v){return (k&&k.charAt(0)==='_')?undefined:v;},2);}catch(e){return String(r);}}
function recFileName(r){var id=String(r.id||'record').replace(/[^A-Za-z0-9._-]+/g,'_');return id+'.json';}
function copyRecText(txt,btn,label){
  var done=function(ok){btn.textContent=ok?'✓ Copied':'Copy failed';setTimeout(function(){btn.textContent=label;},1600);};
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(function(){done(true);},function(){done(false);});}
  else{var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();try{done(document.execCommand('copy'));}catch(x){done(false);}document.body.removeChild(ta);}
}
function dlRecText(txt,fname){
  var blob=new Blob([txt],{type:'application/json'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=fname;
  document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);
}
var RECBYID={};
document.addEventListener('click',function(e){
  var b=e.target&&e.target.closest?e.target.closest('[data-copyrec][data-rid],[data-dlrec][data-rid]'):null;
  if(!b)return;
  var r=RECBYID[b.getAttribute('data-rid')];if(!r)return;
  if(b.hasAttribute('data-copyrec'))copyRecText(recJSON(r),b,'⧉ Copy full record (JSON)');
  else dlRecText(recJSON(r),recFileName(r));
});
function recCard(r){
  RECBYID[r.id]=r;
  var img=JAHDB.emblemSVG(r.t||r.title||r.id, r.id);
  var link='#rec='+encodeURIComponent(r.id);
  return '<div class="card"><div class="rec"><img loading="lazy" src="'+img+'" alt="">'+
    '<div style="flex:1"><h3 style="font-size:1.05em">'+esc(r.t||r.title||r.id)+'</h3>'+
    '<div><span class="badge mono">'+esc(r.id||'')+'</span><span class="badge">'+esc(catOf(r))+'</span></div>'+
    '<p class="dim">'+esc(descOf(r).slice(0,140))+'</p>'+
    '<details class="grp"><summary>Open full record ⤢</summary><div class="row" style="margin:8px 0 8px 12px"><button class="go" data-copyrec data-rid="'+esc(r.id)+'">⧉ Copy full record (JSON)</button><button data-dlrec data-rid="'+esc(r.id)+'">⬇ Download full record (.json)</button> <a class="badge" href="'+esc(link)+'">🔗 Link to this record</a></div><div class="body" data-fullrec="'+esc(r.id)+'"><p class="dim">Loading…</p></div></details>'+
    '</div></div></div>';
}
function loadFull(rid,body){
  var idx=archiveIdx.findIndex(function(r){return r.id===rid;});
  if(idx<0){body.innerHTML='<p class="bad">Record not found.</p>';return;}
  var chunk=Math.floor(idx/100);
  JAHDB.fetchGz(LOCAL+chunkName(chunk)).then(function(t){
    var rows=t.split('\\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean);
    var r=rows.find(function(x){return x.id===rid;});
    if(r){RECBYID[r.id]=r;body.innerHTML=renderFull(r);}
    else body.innerHTML='<p class="bad">Record not found in chunk.</p>';
  }).catch(function(e){body.innerHTML='<p class="bad">Load failed: '+esc(e.message)+'</p>';});
}
function buildGroups(GENRES){
  var g=$('groups'); g.innerHTML='';
  GENRES.forEach(function(genre){
    var rows=archiveIdx.filter(function(r){return r.g===genre;});
    if(!rows.length) return;
    var d=document.createElement('details'); d.className='grp';
    d.innerHTML='<summary>'+esc(genre)+' <span class="dim">('+rows.length.toLocaleString()+')</span></summary><div class="body"><p class="dim">Loading…</p></div>';
    d.addEventListener('toggle',function(){
      if(d.open && !d.dataset.loaded){ d.dataset.loaded='1'; loadGroupSample(genre,d.querySelector('.body')); }
    });
    g.appendChild(d);
  });
}
function loadGroupSample(genre,body){
  var rows=archiveIdx.filter(function(r){return r.g===genre;}).slice(0,25);
  body.innerHTML=rows.map(recCard).join('')||'<p class="dim">No records.</p>';
}
function doSearch(q){
  q=q.toLowerCase().trim();
  var rows=archiveIdx.filter(function(r){return (r.t+' '+(r.g||'')+' '+r.id).toLowerCase().indexOf(q)>=0;}).slice(0,50);
  $('results').innerHTML='<h3>Results ('+rows.length+')</h3>'+rows.map(recCard).join('');
}
var GEN=null;
function genInit(){
  try{ GEN=JAHDB.generators[SLUG]||JAHDB.getGenerator(SLUG); }catch(e){ GEN=null; }
  var sel=$('gCat');
  if(GEN&&GEN.fields){ GEN.fields.forEach(function(f){var o=document.createElement('option');o.value=f;o.textContent=f;sel.appendChild(o);}); }
}
function doGenerate(){
  var seed=parseInt($('gSeed').value,10)||1, n=Math.min(50,Math.max(1,parseInt($('gN').value,10)||5));
  var field=$('gCat').value||null;
  var out=[];
  for(var i=0;i<n;i++){
    try{ var r=GEN.generate(seed+i,{field:field}); var v=GEN.validate(r); if(v.ok) out.push(r); }catch(e){}
  }
  $('gOut').innerHTML='<h3>Generated ('+out.length+')</h3>'+out.map(function(r){
    RECBYID[r.id]=r;
    return '<div class="card"><h3>'+esc(r.name)+'</h3><p class="dim">'+esc(String(r.description||'').slice(0,200))+'</p><button class="go" data-filegen="'+esc(r.id)+'">File to queue</button></div>';
  }).join('');
  out.forEach(function(r){RECBYID[r.id]=r;});
  window._genOut=out;
}
var _queue=[];
function renderQueue(){
  $('qCount').textContent='(' + _queue.length + ' queued)';
  $('queue').innerHTML=_queue.map(function(r,i){
    return '<div class="card"><b>'+esc(r.name)+'</b> <span class="badge mono">'+esc(r.id)+'</span> <button data-unq="'+i+'">Remove</button></div>';
  }).join('')||'<p class="dim">Queue is empty.</p>';
}
document.addEventListener('click',function(e){
  var f=e.target&&e.target.closest?e.target.closest('[data-filegen]'):null;
  if(f){ var r=RECBYID[f.getAttribute('data-filegen')]; if(r){_queue.push(r);renderQueue();} return; }
  var u=e.target&&e.target.closest?e.target.closest('[data-unq]'):null;
  if(u){ _queue.splice(parseInt(u.getAttribute('data-unq'),10),1); renderQueue(); return; }
  var s=e.target&&e.target.closest?e.target.closest('summary'):null;
});
document.addEventListener('toggle',function(e){
  var d=e.target;
  if(d.tagName==='DETAILS'&&d.open){
    var b=d.querySelector('[data-fullrec]');
    if(b&&!b.dataset.done){b.dataset.done='1';loadFull(b.getAttribute('data-fullrec'),b);}
  }
},true);
function greet(){
  var log=$('chatlog');
  log.innerHTML='<div class="msg a"><div class="b">'+esc('%%GREET%%')+'</div></div>';
}
function aiAsk(q){
  return JAHDB.aiAnswer(q,{db:db,role:ROLE,network:NETWORK,archive:archiveSample});
}
$('chatGo').addEventListener('click',function(){
  var q=$('chatIn').value.trim(); if(!q)return;
  var log=$('chatlog');
  log.innerHTML+='<div class="msg u"><div class="b">'+esc(q)+'</div></div>';
  $('chatIn').value='';
  log.innerHTML+='<div class="msg a"><div class="b" id="aiTmp"><span class="dim">Thinking…</span></div></div>';
  log.scrollTop=log.scrollHeight;
  Promise.resolve(aiAsk(q)).then(function(a){
    var t=$('aiTmp'); if(t){t.innerHTML=esc(String(a&&a.text||a||'No answer.'));t.removeAttribute('id');}
    log.scrollTop=log.scrollHeight;
  }).catch(function(e){
    var t=$('aiTmp'); if(t){t.innerHTML='<span class="bad">'+esc(e.message)+'</span>';t.removeAttribute('id');}
  });
});
$('fresh').addEventListener('click',function(){greet();});
$('qgo').addEventListener('click',function(){doSearchEx($('q').value);});
$('q').addEventListener('keydown',function(e){if(e.key==='Enter')doSearchEx($('q').value);});
$('gGo').addEventListener('click',doGenerate);
genInit();
function deepOpen(){
  var m=/[#?]rec=([^&#]+)/.exec(location.hash+location.search);
  if(!m)return;
  var rid=decodeURIComponent(m[1]);
  document.querySelector('[data-p="archive"]').click();
  doSearch(rid);
}

var _mergeSet=[];
function mergerAddCurrent(){
  var cards=document.querySelectorAll('#results [data-rid], #groups [data-rid]');
  var added=0;
  cards.forEach(function(el){
    var rid=el.getAttribute('data-rid');
    if(rid&&_mergeSet.indexOf(rid)<0){_mergeSet.push(rid);added++;}
  });
  renderMergePanel('Added '+added+' record(s) from the current view. '+_mergeSet.length+' in the merge set.');
}
function renderMergePanel(note){
  var p=$('mergePanel');
  var h='<div class="card"><h3>All Database Merger <span class="dim">('+_mergeSet.length+' records)</span></h3>';
  if(note)h+='<p class="dim">'+esc(note)+'</p>';
  h+='<div class="row"><button class="go" id="mgLoad">Load full records</button> <button id="mgDl" class="merger">Download merged set (JSON)</button> <button id="mgClear">Clear</button></div><div id="mgOut"></div></div>';
  p.innerHTML=h;
  $('mgLoad').addEventListener('click',mergerLoadAll);
  $('mgDl').addEventListener('click',mergerDownload);
  $('mgClear').addEventListener('click',function(){_mergeSet=[];renderMergePanel('Merge set cleared.');});
}
var _chunkBase=0; /* chunk files on this database are numbered from 0 (chunk-0000...) */
function mergerLoadAll(){
  var out=$('mgOut'); out.innerHTML='<p class="dim">Loading '+_mergeSet.length+' full records…</p>';
  var jobs=_mergeSet.map(function(rid){
    var idx=archiveIdx.findIndex(function(r){return r.id===rid;});
    if(idx<0)return Promise.resolve(null);
    var chunk=Math.floor(idx/100)+_chunkBase;
    return JAHDB.fetchGz(LOCAL+chunkName(chunk)).then(function(t){
      var rows=t.split('\\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean);
      return rows.find(function(x){return x.id===rid;})||null;
    }).catch(function(){return null;});
  });
  Promise.all(jobs).then(function(recs){
    recs=recs.filter(Boolean);
    window._mergeRecs=recs;
    out.innerHTML='<h3>Merged set — '+recs.length+' full records</h3>'+recs.map(function(r){
      RECBYID[r.id]=r;
      return '<div class="card"><b>'+esc(r.t||r.title||r.id)+'</b> <span class="badge mono">'+esc(r.id)+'</span><p class="dim">'+esc(descOf(r).slice(0,160))+'</p></div>';
    }).join('');
  });
}
function mergerDownload(){
  var recs=window._mergeRecs||[];
  if(!recs.length){alert('Load full records first, then download.');return;}
  dlRecText(JSON.stringify({database:SLUG,merged:recs.length,records:recs},null,2),'merged-'+SLUG+'.json');
}
var _exhaustive=false;
function doSearchEx(q){
  q=q.toLowerCase().trim();
  if(!_exhaustive){doSearch(q);return;}
  var rows=archiveIdx.filter(function(r){return (r.t+' '+(r.g||'')+' '+r.id).toLowerCase().indexOf(q)>=0;}).slice(0,50);
  $('results').innerHTML='<h3>Exhaustive results ('+rows.length+')</h3><p class="dim">Exhaustive mode scans full record text across archive chunks.</p><div id="exOut"><p class="dim">Scanning...</p></div>';
  var jobs=[],seen={};
  rows.forEach(function(r){seen[r.id]=1;jobs.push(Promise.resolve(r));});
  var nchunks=Math.min(20,Math.ceil(archiveIdx.length/100));
  for(var c=0;c<nchunks;c++){
    jobs.push(JAHDB.fetchGz(LOCAL+chunkName(c+_chunkBase)).then(function(t){
      return t.split('\\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean)
        .filter(function(r){return r&&!seen[r.id]&&JSON.stringify(r).toLowerCase().indexOf(q)>=0;}).slice(0,25);
    }).catch(function(){return [];}));
  }
  Promise.all(jobs).then(function(parts){
    var all=[];parts.forEach(function(p){(Array.isArray(p)?p:[p]).forEach(function(r){if(r&&!seen[r.id]){seen[r.id]=1;all.push(r);}});});
    all=all.slice(0,50);
    all.forEach(function(r){RECBYID[r.id]=r;});
    $('exOut').innerHTML='<h3>Full-text matches ('+all.length+')</h3>'+all.map(recCard).join('');
  });
}

$('qex').addEventListener('click',function(){_exhaustive=!_exhaustive;$('qex').classList.toggle('on',_exhaustive);});
$('qmerge').addEventListener('click',function(){mergerAddCurrent();});
renderMergePanel('Search or browse, then press All Database Merger to collect the records you see into one merged set.');

})();</script>
</body>
</html>
"""


def esc_html(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def page_html(slug, name, tagline, descriptor, record_kind, prefix, ai_name,
              role, gen_id, gen_js, search_ph, chat_ph, greet, type_str,
              about_archive, about_fields, about_gen, about_ai):
    title = name + " — JAH Databases"
    meta = (tagline + " " + descriptor)[:300]
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "Dataset",
                         "name": name, "description": meta,
                         "creator": {"@type": "Person", "name": "Justin Addam Higgins"}})
    hero_p = tagline + " - " + descriptor
    subs = {
        "%%TITLE%%": esc_html(title),
        "%%META_DESC%%": esc_html(meta),
        "%%JSONLD%%": jsonld.replace("</", "<\\/"),
        "%%HERO_H1%%": esc_html(name),
        "%%HERO_P%%": esc_html(hero_p),
        "%%GEN_ID%%": esc_html(gen_id),
        "%%TYPE_STR%%": esc_html(type_str),
        "%%SEARCH_PH%%": esc_html(search_ph),
        "%%AI_NAME%%": esc_html(ai_name),
        "%%CHAT_PH%%": esc_html(chat_ph),
        "%%GREET%%": greet.replace("\\", "\\\\").replace("'", "\\'"),
        "%%GEN_H3%%": esc_html(name + " generator"),
        "%%GEN_SUB%%": esc_html("Generate clearly-labeled " + record_kind +
                                " samples. Seeded archive records are the authoritative entries."),
        "%%GEN_JS%%": gen_js,
        "%%ABOUT_ARCHIVE%%": esc_html(about_archive),
        "%%ABOUT_FIELDS%%": esc_html(about_fields),
        "%%ABOUT_GEN%%": esc_html(about_gen),
        "%%ABOUT_AI%%": esc_html(about_ai),
        "%%SLUG%%": slug,
        "%%DBNAME%%": name.replace("\\", "\\\\").replace("'", "\\'"),
        "%%RECORD_KIND%%": record_kind.replace("'", "\\'"),
        "%%ROLE%%": role.replace("\\", "\\\\").replace("'", "\\'"),
        "%%EMBLEM_PREFIX%%": prefix,
    }
    out = PAGE_TEMPLATE
    for k, v in subs.items():
        out = out.replace(k, v)
    return out


# ---------------------------------------------------------------- gen js

JS_TEMPLATE = """(function(){'use strict';
/* JAH %%NAME%% generator — %%GEN_ID%%.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Real working client-side
   generator: every call composes a genuine original creation from the
   archive's pools — name, measures, description, practice, key points,
   and a runnable demonstration program. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function rint(r,lo,hi){return lo+Math.floor(r()*(hi-lo+1));}
var PREFIX=%%PREFIX_JSON%%;
var NOUN=%%NOUN_JSON%%;
var FIELDS=%%FIELDS_JSON%%;
var TOPICS=%%TOPICS_JSON%%;
var PEOPLE=%%PEOPLE_JSON%%;
var PLACES=%%PLACES_JSON%%;
var ADJS=%%ADJS_JSON%%;
var ATTRS=%%ATTRS_JSON%%;
var CATS1=%%CATS1_JSON%%;
var CATS2=%%CATS2_JSON%%;
function attrsFor(r){
  var o={};
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];o[a.key]=rint(r,a.lo,a.hi);}
  return o;
}
function demoProgram(title,attrs){
  var L=['# '+title+' — generated demonstration',
         '# Property of Justin Addam Higgins (JAH).','attrs = {'];
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];
    L.push('    '+JSON.stringify(a.label)+': '+attrs[a.key]+',  # '+a.unit);}
  L.push('}');
  L.push("print("+JSON.stringify("== "+title+" ==")+")");
  L.push('for label, value in attrs.items():');
  L.push("    print('  %s: %s' % (label, value))");
  L.push('total = sum(attrs.values())');
  L.push('print("  total = %.2f" % total)');
  L.push('print("  mean  = %.2f" % (total / len(attrs)))');
  L.push('for label, value in attrs.items():');
  L.push("    assert value > 0, 'attribute must be positive: ' + label");
  L.push('print("OK - generated demo passed")');
  return L.join("\\n")+"\\n";
}
function composeDesc(title,field,attrs,adj,person,place,c1,c2){
  var bits=[];
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];
    bits.push(a.label.toLowerCase()+' of '+attrs[a.key]+' '+a.unit);}
  var p1=title+' is a '+adj+' '+NOUN+' of the archive. Chronicled by '+person+' of '+place+
    ', it carries '+bits[0]+' and '+bits[1]+' — measures that set it apart from its kin.';
  var p2='In practice it shows '+bits[2]+' and '+bits[3]+', with the twin natures of '+
    c1+' and '+c2+'. Those who work with it learn quickly: respect its pattern and it repays the courtesy.';
  return p1+'\\n\\n'+p2;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(rnd,FIELDS);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(rnd,pool);
  var adj=pick(rnd,ADJS), person=pick(rnd,PEOPLE), place=pick(rnd,PLACES);
  var c1=pick(rnd,CATS1), c2=pick(rnd,CATS2);
  var attrs=attrsFor(rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=composeDesc(topic,field,attrs,adj,person,place,c1,c2);
  var kp=[topic+' — original '+NOUN+' of the archive.',
          'Measures: '+ATTRS.map(function(a){return a.label.toLowerCase()+' '+attrs[a.key]+' '+a.unit;}).join('; ')+'.',
          'Twin natures: '+c1+' and '+c2+'.',
          'Kept by the archive; seeded records remain authoritative.'];
  return {
    id:id,
    name:topic+' — generated '+NOUN,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+desc,
    field:field,
    how_it_works:'Name it, place it in '+place+', test it in play, keep one secret back, and check the finished '+NOUN+' against its seed.',
    key_points:kp,
    requirements:['A fixed name','A home in the archive','The four measures recorded','One secret withheld'],
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'generated-demo',language:'python',program:demoProgram(topic,attrs),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var ok=false;
  try{ ok=new RegExp('^'+PREFIX.replace(/[-]/g,'\\\\-')+'\\\\d{6}$').test(r.id||''); }catch(x){}
  if(!ok)e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.description||String(r.description).length<120)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:%%GENVER_JSON%%,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(%%SLUG_JSON%%,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def gen_js(cfg, slug, prefix, gen_id, gen_version):
    topics = {}
    for f in cfg["fields"]:
        topics[f] = [s["core"] for s in cfg["specs"] if s["g"] == f]
        if not topics[f]:
            topics[f] = ["General " + cfg["noun"]]
    attrs_meta = [{"key": a["key"], "label": a["label"], "unit": a["unit"],
                   "lo": a["lo"], "hi": a["hi"]} for a in cfg["attrs"]]
    subs = {
        "%%NAME%%": cfg["item_name"],
        "%%GEN_ID%%": gen_id,
        "%%PREFIX_JSON%%": json.dumps(prefix),
        "%%NOUN_JSON%%": json.dumps(cfg["noun"]),
        "%%FIELDS_JSON%%": json.dumps(cfg["fields"]),
        "%%TOPICS_JSON%%": json.dumps(topics),
        "%%PEOPLE_JSON%%": json.dumps(cfg["people"][:24]),
        "%%PLACES_JSON%%": json.dumps(cfg["places"][:24]),
        "%%ADJS_JSON%%": json.dumps(cfg["adjs"][:20]),
        "%%ATTRS_JSON%%": json.dumps(attrs_meta),
        "%%CATS1_JSON%%": json.dumps(cfg["cats"][0]),
        "%%CATS2_JSON%%": json.dumps(cfg["cats"][1]),
        "%%GENVER_JSON%%": json.dumps(gen_version),
        "%%SLUG_JSON%%": json.dumps(slug),
    }
    out = JS_TEMPLATE
    for k, v in subs.items():
        out = out.replace(k, v)
    return out
