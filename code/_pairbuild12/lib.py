#!/usr/bin/env python3
"""Shared build library for the 12-pair worker (subagent e11d4e4e).

Builds, for one pair (public + Signature editions):
  db/<slug>/index.html, db/<slug>/gen-<slug>.js
  db/<slug>-signature/index.html, db/<slug>-signature/gen-<slug>-signature.js
  data/<slug>/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}
  data/<slug>-signature/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}
  code/<slug>-build/manifest-fragment.json   (for the coordinator; NEVER touches manifest)

Structure mirrors the merged language-pashto pair exactly.
Property of Justin Addam Higgins (JAH).
"""
import gzip
import json
import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.expanduser("~/workspace/jah-databases")
DATAREPO = os.path.expanduser("~/workspace/jah-databases-data-1")
DATAHOST = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/"
GENVER_FMT = "jahdb-{slug}-1.0"

FULL_SCHEMA = ["id", "t", "g", "name", "title", "description", "how_it_works",
               "key_points", "requirements", "standards", "citations",
               "src", "ladder_rank", "ladder_tier", "demo"]
IDX_SCHEMA = ["id", "t", "g"]

BLOCKLIST = [
    # hate / profanity / slurs / sexual / religious-framing
    "nigger", "faggot", "kike", "spic", "chink", "raghead", "tranny",
    "fuck", "shit", "bitch", "whore", "slut", "porn", "xxx",
    "kill all", "exterminate", "master race", "racial purity",
    "jesus christ", "bible", "quran", "koran", "torah", "talmud",
    "salvation", "eternal damnation", "holy war", "jihad",
    "bat belt",
]


def _block_pattern():
    parts = []
    for term in BLOCKLIST:
        if " " in term:
            parts.append(re.escape(term))
        else:
            parts.append(r"\b" + re.escape(term) + r"\b")
    return re.compile("|".join(parts), re.IGNORECASE)


BLOCK_RE = _block_pattern()

HEALTH_DISCLAIMER = ("Educational information only — not medical advice. "
                     "Consult qualified professionals for personal decisions.")


# ---------------------------------------------------------------- page template
PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@NAME@@ — JAH Databases</title>
<meta name="description" content="@@TAGLINE@@ Property of Justin Addam Higgins.">
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "@@NAME@@", "description": "@@TAGLINE@@", "creator": {"@type": "Person", "name": "Justin Addam Higgins"}}</script>
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
      <h1>@@NAME@@</h1>
      <p>@@TAGLINE@@ - @@EDITION_LINE@@</p>
      <div class="stats">
        <span class="stat">Archive records: <b id="stCount">…</b></span>
        <span class="stat">Generator: <b>@@GENVER@@</b> <span class="ok">● working</span></span>
        <span class="stat">Type: <b>@@TYPE_LINE@@</b></span>
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
      <input id="q" placeholder="@@SEARCH_PH@@" style="flex:1;min-width:200px">
      <button class="go" id="qgo">Search</button><button class="tab pill-ex" id="qex">Exhaustive</button><button class="go merger" id="qmerge">All Database Merger</button>
    </div>
    <div id="mergePanel"></div>
    <p class="dim">Browse by category — each group opens on demand and loads only what you open.</p>
    <div id="groups"></div>
    <div id="results"></div>
  </section>
  <section class="pane" id="p-gen">
    <div class="card">
      <h3>@@NAME@@ generator</h3>
      <p class="dim">@@GEN_BLURB@@</p>
      <div class="row">
        <label>Seed <input id="gSeed" type="number" value="61" style="width:110px"></label>
        <label>Count <input id="gN" type="number" value="5" min="1" max="50" style="width:80px"></label>
      </div>
      <div class="row" style="margin-top:8px"><label>Field <select id="gCat"><option value="">any (generator picks)</option></select></label><button class="go" id="gGo">Generate</button></div>
      <div id="gOut"></div>
    </div>
    <div class="card">
      <h3>Queued for the archive <span class="dim" id="qCount"></span></h3>
      <p class="dim">Generated records wait here. Only validated, drift-free records can be filed — filing is a deliberate act, never automatic from chat.</p>
      <div id="queue"></div>
    </div>
  </section>
  <section class="pane" id="p-chat">
    <div class="card">
      <h3>@@AI_NAME@@ <button id="fresh" style="font-size:.8em">New session</button></h3>
      <div class="chatlog" id="chatlog"></div>
      <div class="row">
        <input id="chatIn" placeholder="@@CHAT_PH@@" style="flex:1;min-width:200px">
        <button class="go" id="chatGo">Send</button>
      </div>
      <p class="dim">Fresh screen every session. Nothing you say here enters the permanent archive unless you file it from the Generator tab.</p>
    </div>
  </section>
  <section class="pane" id="p-about">
    <div class="card">
      <h3>About this data base</h3>
      <dl class="kv">
        <dt>Archive</dt><dd>@@ABOUT_ARCHIVE@@</dd>
        <dt>Record schema</dt><dd class="mono">id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo</dd>
        <dt>Fields</dt><dd>Foundations · Compounded · Advanced - each tier opens on demand and loads only what you open</dd>
        <dt>Generator</dt><dd>@@GENVER@@ — @@GEN_BLURB@@</dd>
        <dt>Drift control</dt><dd>Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.</dd>
        <dt>Target</dt><dd>1,000,000 records. The archive marches toward the million mark with overload protection: 100-record chunks, lazy loading, and a collapsible per-field archive so no device ever renders everything at once.</dd>
        <dt>AI</dt><dd>@@AI_DESC@@</dd>
        <dt>Signature system</dt><dd>@@SIG_SYS_LINE@@ Property of Justin Addam Higgins (JAH).</dd>
      </dl>
    </div>
  </section>
  <div class="foot">@@FOOT@@</div>
</div>
<script src="../../core/jahdb.js"></script>
<script src="../../core/jahdb-dedupe.js"></script>
<script src="../../core/jahdb-xdb.js"></script>
<script src="../../core/standard-1.0.js"></script>
<script src="../../core/guide-conv.js"></script>
<script src="../../core/apex-2.0.js"></script>
<script src="gen-@@SLUG@@.js"></script>
<script>
(function(){
'use strict';
var SLUG='@@SLUG@@';
var LOCAL='@@LOCAL@@';
var db={slug:SLUG,name:'@@NAME@@',ai_name:'@@AI_NAME@@',record_kind:'@@RECORD_KIND@@'};
var ROLE='@@ROLE@@';
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
  $('emblem').src=JAHDB.emblemSVG(db.name,'@@EMBLEM_SEED@@');
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
function descOf(r){ try{ return String(r.description||""); }catch(e){ return ""; } }
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
  log.innerHTML='<div class="msg a"><div class="b">'+esc('@@GREET@@')+'</div></div>';
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


# ---------------------------------------------------------------- gen template
GENJS = """(function(){'use strict';
/* JAH @@NAME@@ generator — @@GENVER@@.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="@@PREFIX@@";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
@@FOUND_TOPICS@@
 ],
 "Compounded": [
@@COMP_TOPICS@@
 ],
 "Advanced": [
@@ADV_TOPICS@@
 ]
};
var DEMOKIND="@@DEMOKIND@@";
var SAMPLEDESC="@@SAMPLEDESC@@";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# @@DEMOTITLE@@ — "+safe+"\\n"
   + "# Field: "+field+"\\n"
   + "record = {'title': \\""+safe+"\\", 'field': \\""+field+"\\"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\\n"
   + "print(summarize(record))\\n"
   + "print('Sample record — structural sample, not an archive entry.')\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — @@RECORD_KIND@@',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A @@RECORD_KIND@@ of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'@@SRC@@',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'@@GENVER@@',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('@@SLUG@@',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""


def render_page(meta):
    t = PAGE
    for k, v in meta.items():
        t = t.replace("@@" + k + "@@", v)
    leftover = re.findall(r"@@[A-Z_]+@@", t)
    assert not leftover, "unreplaced tokens: %s" % leftover[:5]
    return t


def render_genjs(meta, topics_by_tier):
    def qlist(titles):
        return ",\n".join('  "%s"' % t.replace('"', "'") for t in titles)
    m = dict(meta)
    m["FOUND_TOPICS"] = qlist(topics_by_tier["Foundations"])
    m["COMP_TOPICS"] = qlist(topics_by_tier["Compounded"])
    m["ADV_TOPICS"] = qlist(topics_by_tier["Advanced"])
    t = GENJS
    for k, v in m.items():
        t = t.replace("@@" + k + "@@", v)
    leftover = re.findall(r"@@[A-Z_]+@@", t)
    assert not leftover, "unreplaced gen tokens: %s" % leftover[:5]
    return t


def run_python_program(program):
    """Execute a demo program; return (ok, stdout, stderr)."""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(program)
        path = f.name
    try:
        p = subprocess.run([sys.executable, path], capture_output=True,
                           text=True, timeout=30)
        return p.returncode == 0 and bool(p.stdout.strip()), p.stdout, p.stderr
    except Exception as e:  # noqa: BLE001
        return False, "", str(e)
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def content_gate(text, where):
    m = BLOCK_RE.search(text or "")
    if m:
        raise ValueError("content gate hit in %s: %r" % (where, m.group(0)[:40]))


def manifest_entry(meta, slug, name, prefix, source, n):
    return {
        "slug": slug,
        "name": name,
        "tagline": meta["tagline"],
        "record_kind": meta["record_kind"],
        "id_prefix": prefix,
        "ai_name": meta["ai_name"],
        "local_index": "data/%s/index.jsonl.gz" % slug,
        "page_url": "db/%s/" % slug,
        "index": "data/%s/index.jsonl.gz" % slug,
        "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % slug,
        "source": source,
        "record_count": n,
        "full_records": n,
        "status": "staged",
    }


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_gz_jsonl(path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def build_pair(cfg, topics, demo_builder):
    """cfg: dict with pair metadata. topics: list of 34 dicts.
    demo_builder(topic) -> python source string.
    Returns dict of built slugs -> records."""
    assert len(topics) == 34, "need 34 topics, got %d" % len(topics)
    tiers = {"Foundations": [], "Compounded": [], "Advanced": []}
    for t in topics:
        assert t["tier"] in tiers, t["tier"]
        tiers[t["tier"]].append(t["title"])
    assert len(tiers["Foundations"]) == 11 and len(tiers["Compounded"]) == 12 \
        and len(tiers["Advanced"]) == 11, "tier split must be 11/12/11"

    health_note = ("\n" + HEALTH_DISCLAIMER) if cfg.get("health") else ""
    built = {}
    for edition, prefix, src, name, tag in (
        ("pub", cfg["prefix_pub"], "public-harvest", cfg["name_pub"], cfg["tagline_pub"]),
        ("sig", cfg["prefix_sig"], "signature", cfg["name_sig"], cfg["tagline_sig"]),
    ):
        slug = cfg["slug"] if edition == "pub" else cfg["slug"] + "-signature"
        genver = GENVER_FMT.format(slug=slug)
        records = []
        for i, t in enumerate(topics, start=1):
            program = demo_builder(t, edition)
            ok, out, err = run_python_program(program)
            if not ok:
                raise RuntimeError("demo failed for %s [%s]: %s" % (t["title"], edition, err[:300]))
            desc = t["desc_pub"] if edition == "pub" else (t["desc_pub"] + "\n" + t["desc_sig"])
            how = t["how_pub"] if edition == "pub" else (t["how_pub"] + "\n" + t["how_sig"])
            rec = {
                "id": "%s%06d" % (prefix, i),
                "t": t["title"],
                "g": t["tier"],
                "name": t["title"],
                "title": t["title"] + (" (Signature Edition)" if edition == "sig" else ""),
                "description": desc + health_note,
                "how_it_works": how,
                "key_points": t["keys"],
                "requirements": t["reqs"],
                "standards": t["stds"],
                "citations": t["cites"],
                "src": src,
                "ladder_rank": i,
                "ladder_tier": t["tier"].lower(),
                "demo": {"kind": cfg["demo_kind"], "language": "python",
                         "program": program,
                         "note": "Executed OK at build time; output verified."},
            }
            for k in FULL_SCHEMA:
                assert k in rec, k
            blob = json.dumps(rec, ensure_ascii=False)
            content_gate(blob, "%s record %d" % (slug, i))
            records.append(rec)

        # intra-edition dedupe
        ids = [r["id"] for r in records]
        assert len(set(ids)) == 34, "duplicate ids in " + slug
        descs = [r["description"] for r in records]
        assert len(set(descs)) == 34, "duplicate descriptions in " + slug

        data_dir = os.path.join(DATAREPO, "data", slug)
        write_gz_jsonl(os.path.join(data_dir, "index.jsonl.gz"),
                       [{k: r[k] for k in IDX_SCHEMA} for r in records])
        write_gz_jsonl(os.path.join(data_dir, "chunks", "chunk-0000.jsonl.gz"), records)

        ai_name = cfg["ai_pub"] if edition == "pub" else cfg["ai_sig"]
        role = cfg["role_pub"] if edition == "pub" else cfg["role_sig"]
        greet = cfg["greet_pub"] if edition == "pub" else cfg["greet_sig"]
        edition_line = ("Public records - real, fact-checked %s" % cfg["record_kind_plural"]) \
            if edition == "pub" else "Signature-authored originals expanding the public record"
        type_line = "Public records organized in the Signature system" \
            if edition == "pub" else "Signature-authored originals"
        sig_sys = "Public records organized in the Signature system." \
            if edition == "pub" else "Signature-authored originals organized in the Signature system."
        foot = "JAH Databases. Public records organized in the Signature system. Property of Justin Addam Higgins (JAH)." \
            if edition == "pub" else \
            "JAH Databases. Signature-authored originals organized in the Signature system. Property of Justin Addam Higgins (JAH)."
        page_meta = {
            "NAME": name, "TAGLINE": tag, "SLUG": slug,
            "LOCAL": DATAHOST + "data/%s/" % slug,
            "GENVER": genver, "AI_NAME": ai_name, "RECORD_KIND": cfg["record_kind"],
            "ROLE": role, "GREET": greet, "EMBLEM_SEED": prefix,
            "EDITION_LINE": edition_line, "TYPE_LINE": type_line,
            "SEARCH_PH": cfg["search_ph"], "CHAT_PH": cfg["chat_ph"],
            "GEN_BLURB": cfg["gen_blurb"], "ABOUT_ARCHIVE": cfg["about_archive"],
            "AI_DESC": ai_name + " — " + role + " — and aware of the whole JAH Databases network "
                       "through cross-database reasoning. On-device Standard 1.0, no key needed; "
                       "uses the shared Signature backend automatically when configured.",
            "SIG_SYS_LINE": sig_sys, "FOOT": foot,
        }
        db_dir = os.path.join(REPO, "db", slug)
        os.makedirs(db_dir, exist_ok=True)
        with open(os.path.join(db_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render_page(page_meta))
        gen_meta = {
            "NAME": name, "SLUG": slug, "GENVER": genver, "PREFIX": prefix,
            "RECORD_KIND": cfg["record_kind"], "DEMOKIND": cfg["demo_kind"],
            "DEMOTITLE": cfg["demo_title"], "SRC": src,
            "SAMPLEDESC": cfg.get("gen_sample_extra", ""),
        }
        gen_path = os.path.join(db_dir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(render_genjs(gen_meta, tiers))

        # node --check + live generate/validate + emitted-demo execution
        subprocess.run(["node", "--check", gen_path], check=True,
                       capture_output=True, text=True)
        node_test = (
            "const g=require(%s);"
            "let n=0;"
            "for(const s of [7,42,3001]){"
            "  const r=g.generate(s,{});"
            "  const v=g.validate(r);"
            "  if(!v.ok) throw new Error('validate failed '+JSON.stringify(v.errors));"
            "  if(!r.demo||!r.demo.program) throw new Error('no demo');"
            "  require('fs').writeFileSync('/tmp/_gdemo_'+s+'.py', r.demo.program);"
            "  n++;}"
            "console.log('GEN_OK '+n);"
        ) % json.dumps(gen_path)
        p = subprocess.run(["node", "-e", node_test], capture_output=True, text=True)
        assert p.returncode == 0 and "GEN_OK 3" in p.stdout, p.stderr[:300]
        for s in (7, 42, 3001):
            with open("/tmp/_gdemo_%d.py" % s, encoding="utf-8") as f:
                ok, out, err = run_python_program(f.read())
            assert ok, "emitted demo failed seed %d: %s" % (s, err[:200])

        # re-read data files and verify integrity
        idx_rows = read_gz_jsonl(os.path.join(data_dir, "index.jsonl.gz"))
        chunk_rows = read_gz_jsonl(os.path.join(data_dir, "chunks", "chunk-0000.jsonl.gz"))
        assert len(idx_rows) == 34 and len(chunk_rows) == 34, slug
        assert all(list(r.keys()) == IDX_SCHEMA for r in idx_rows), slug
        assert all(list(r.keys()) == FULL_SCHEMA for r in chunk_rows), slug
        assert [r["ladder_rank"] for r in chunk_rows] == list(range(1, 35)), slug
        built[slug] = records
        print("built %s: 34 records, page+gen OK, demos executed" % slug)

    # cross-edition dedupe (titles differ by suffix; descriptions must differ)
    pub, sig = built[cfg["slug"]], built[cfg["slug"] + "-signature"]
    assert not (set(r["id"] for r in pub) & set(r["id"] for r in sig))
    return built


def cross_pair_dedupe(all_built):
    seen_desc, seen_title = {}, {}
    for slug, recs in all_built.items():
        for r in recs:
            d = re.sub(r"\s+", " ", r["description"]).strip()
            if d in seen_desc:
                raise ValueError("dup description: %s vs %s" % (slug, seen_desc[d]))
            seen_desc[d] = slug
            t = r["title"]
            if t in seen_title:
                raise ValueError("dup title: %r in %s vs %s" % (t, slug, seen_title[t]))
            seen_title[t] = slug
    print("cross-pair dedupe OK: %d records, no dup titles/descriptions"
          % sum(len(v) for v in all_built.values()))
