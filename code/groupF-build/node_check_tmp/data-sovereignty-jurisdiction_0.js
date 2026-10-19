(function(){
'use strict';
var SLUG='data-sovereignty-jurisdiction';
var LOCAL='https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/data-sovereignty-jurisdiction/';
var db={slug:SLUG,name:'The Data Sovereignty Jurisdiction Database',ai_name:'JAH Data Sovereignty Archivist',record_kind:'data sovereignty record'};
var ROLE='data sovereignty archivist - jurisdiction rules, residency requirements, transfer regimes, adequacy, SCCs, localization; teaching progressively along the ladder; answers from many angles using only archive data';
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
  $('emblem').src=JAHDB.emblemSVG(db.name,'JAH-SI-');
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
  log.innerHTML='<div class="msg a"><div class="b">'+esc('I am the JAH Data Sovereignty Archivist. Ask about data sovereignty, transfers, residency...')+'</div></div>';
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
      var rows=t.split('\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean);
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
      return t.split('\n').filter(function(l){return l.trim();}).map(function(l){try{return JSON.parse(l);}catch(e){return null;}}).filter(Boolean)
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

})();