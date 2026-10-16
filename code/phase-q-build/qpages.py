#!/usr/bin/env python3
"""Build db/<slug>/index.html + gen-<slug>.js for Phase-Q new databases.

Based on the db/public-synthetic-intelligence/index.html template, with:
  - .kv grid minmax(120px,1fr) (canon)
  - id="stCount" live count wiring
  - red "All Database Merger" button AFTER the "Exhaustive" pill in the
    archive search row (never beside Search)
  - generateChecked-style generator JS (generate/validate/driftCheck)
"""
import os, re, html

HUB = os.path.expanduser("~/workspace/jah-databases")
TEMPLATE = open(os.path.join(HUB, "db/public-synthetic-intelligence/index.html")).read()

MERGER_CSS = """
button.merger{background:#c81e3a;border-color:#c81e3a;color:#fff;font-weight:bold}
button.pill-ex{border-radius:999px}
#mergePanel{margin-top:10px}"""

MERGER_HTML = """
    <div id="mergePanel"></div>"""

MERGER_JS = """
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
function mergerLoadAll(){
  var out=$('mgOut'); out.innerHTML='<p class="dim">Loading '+_mergeSet.length+' full records…</p>';
  var jobs=_mergeSet.map(function(rid){
    var idx=archiveIdx.findIndex(function(r){return r.id===rid;});
    if(idx<0)return Promise.resolve(null);
    var chunk=Math.floor(idx/100);
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
  $('results').innerHTML='<h3>Exhaustive results ('+rows.length+')</h3><p class="dim">Exhaustive mode scans full record text across archive chunks.</p><div id="exOut"><p class="dim">Scanning…</p></div>';
  var jobs=[],seen={};
  rows.forEach(function(r){seen[r.id]=1;jobs.push(Promise.resolve(r));});
  var nchunks=Math.min(20,Math.ceil(archiveIdx.length/100));
  for(var c=0;c<nchunks;c++){
    jobs.push(JAHDB.fetchGz(LOCAL+chunkName(c)).then(function(t){
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
"""

def esc_h(s):
    return html.escape(s or "", quote=True)

def build_page(cfg):
    slug = cfg["slug"]; name = cfg["name"]; ai = cfg["ai"]; role = cfg["role"]
    desc = cfg["desc"]; prefix = cfg["prefix"]; genver = "jahdb-%s-1.0" % slug
    kind = cfg["kind"]
    sig = cfg.get("signature", False)
    t = TEMPLATE
    # textual substitutions
    t = t.replace("Public Synthetic Intelligence Database", esc_h(name))
    t = t.replace("public-synthetic-intelligence", slug)
    t = t.replace("Public Synthetic Intelligence", esc_h(name.replace(" Database", "")))
    t = t.replace("JAH Synthetic Intelligence Archivist", esc_h(ai))
    t = t.replace("synthetic intelligence archivist — synthetic cognition, synthetic minds, whole brain emulation, synthetic agents", esc_h(role))
    t = t.replace("JAH-SI-", prefix)
    t = t.replace("jahdb-public-synthetic-intelligence-1.0", genver)
    t = t.replace("gen-public-synthetic-intelligence.js", "gen-%s.js" % slug)
    # hero paragraph + meta description
    t = t.replace(
        "Synthetic minds, <b>synthetic cognition</b>, <b>whole brain emulation</b>, <b>neuromorphic systems</b>, and <b>synthetic agents</b> — real-world research organized in the Signature system. Every record carries the full entry: description, history, key figures, how it works, and citations.",
        esc_h(desc) + " Every record carries the full entry — description, how it works, key points, requirements, citations, and a runnable demo program.")
    t = t.replace(
        "Real-world synthetic intelligence — synthetic cognition, whole brain emulation, neuromorphic computing, synthetic agents, and 56 more. Full research records. Public records organized in the Signature system. Property of Justin Addam Higgins.",
        esc_h(desc) + " Full %s. Property of Justin Addam Higgins." % esc_h(kind + "s"))
    t = t.replace(
        "Real-world synthetic intelligence — synthetic cognition, whole brain emulation, neuromorphic computing, synthetic agents, and 56 more. Full research records. Public records organized in the Signature system.",
        esc_h(desc))
    t = t.replace(
        "The Public Synthetic Intelligence archive (JAH-SI- records): real-world synthetic intelligence — concepts, approaches, history, systems, and research. Every record carries the full entry — description, history, key figures, how it works, and citations — never a stub.",
        "The %s archive (%s records): %s Every record carries the full entry — description, how it works, key points, requirements, citations, and a runnable demo — never a stub." % (esc_h(name), prefix, esc_h(desc)))
    t = t.replace("concepts · approaches · history · systems · research-areas",
                  esc_h(" · ".join(cfg.get("fields", ["general"]))))
    t = t.replace("Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
                  "Generate structural %s. Seeded archive records are the authoritative entries." % esc_h(kind + "s"))
    t = t.replace("Search synthetic intelligence concepts, systems, history…",
                  "Search %s…" % esc_h(kind + "s"))
    t = t.replace("Ask about synthetic intelligence…", "Ask about %s…" % esc_h(kind + "s"))
    t = t.replace("Ask about synthetic intelligence.", "Ask about %s." % esc_h(kind + "s"))
    t = t.replace("I am the JAH Synthetic Intelligence Archivist. Ask me about synthetic intelligence.",
                  "I am the %s. Ask me about %s." % (esc_h(ai), esc_h(kind + "s")))
    # inject merger CSS
    t = t.replace("pre.codeblock{", MERGER_CSS + "\npre.codeblock{", 1)
    # search row: add Exhaustive pill + red merger button AFTER it (never beside Search)
    old_row = '''      <button class="go" id="qgo">Search</button>
    </div>'''
    new_row = '''      <button class="go" id="qgo">Search</button>
      <button class="tab pill-ex" id="qex">Exhaustive</button><button class="go merger" id="qmerge">All Database Merger</button>
    </div>''' + MERGER_HTML
    assert old_row in t, "search row not found in template"
    t = t.replace(old_row, new_row, 1)
    # wire search to exhaustive variant + merger
    t = t.replace("$('qgo').addEventListener('click',function(){doSearch($('q').value);});",
                  "$('qgo').addEventListener('click',function(){doSearchEx($('q').value);});")
    t = t.replace("$('q').addEventListener('keydown',function(e){if(e.key==='Enter')doSearch($('q').value);});",
                  "$('q').addEventListener('keydown',function(e){if(e.key==='Enter')doSearchEx($('q').value);});")
    # inject merger JS before genInit();
    assert "genInit();" in t
    t = t.replace("genInit();", MERGER_JS + "\n$('qex').addEventListener('click',function(){_exhaustive=!_exhaustive;$('qex').classList.toggle('on',_exhaustive);});\n"
                    "$('qmerge').addEventListener('click',function(){mergerAddCurrent();});\n"
                    "renderMergePanel('Search or browse, then press All Database Merger to collect the records you see into one merged set.');\n"
                    "genInit();", 1)
    # canon checks
    assert 'id="stCount"' in t
    assert "minmax(120px,1fr)" in t
    assert "All Database Merger" in t
    assert "bat belt" not in t.lower()
    assert "facebook" not in t.lower()
    # type line
    if sig:
        t = t.replace("Type: <b>Public records in Signature system</b>",
                      "Type: <b>Signature originals</b>")
    return t

GEN_JS_TEMPLATE = r"""(function(){'use strict';
/* JAH __NAME__ generator — __GENVER__.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. generateChecked: every generated
   record passes validate() and driftCheck() before it may be filed. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escQ(s){return String(s).split("\\").join("\\\\").split("'").join("\\'");}
var PREFIX=__PREFIX__;
var FIELDS=__FIELDS__;
var TOPICS=__TOPICS__;
function demoProgram(topic,field){
  return '# __KIND__ study demo\n'
   + "print('Study: ' + '" + escQ(topic) + "')\n"
   + "print('Field: ' + '" + escQ(field) + "')\n"
   + "print('Full entries: description, how it works, key points, requirements, citations, demo.')\n"
   + "print('Sample record - structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' - __KIND__ study',
    title:topic,
    description:'SAMPLE RECORD (generated - structural sample). A __KIND__ study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'study-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
function generateChecked(seed,opts,sample){
  var r=generate(seed,opts||{});
  var v=validate(r);
  if(!v.ok)return {ok:false,errors:v.errors};
  var d=driftCheck(r,sample||[]);
  if(!d.ok)return {ok:false,errors:d.errors};
  return {ok:true,record:r};
}
var gen={version:__GENVER__,generate:generate,validate:validate,driftCheck:driftCheck,generateChecked:generateChecked,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(__SLUG__,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

def build_gen_js(cfg, topics):
    import json as _json
    t = GEN_JS_TEMPLATE
    t = t.replace("__NAME__", cfg["name"])
    t = t.replace("__GENVER__", _json.dumps("jahdb-%s-1.0" % cfg["slug"]))
    t = t.replace("__PREFIX__", _json.dumps(cfg["prefix"]))
    t = t.replace("__FIELDS__", _json.dumps(cfg.get("fields", ["general"])))
    t = t.replace("__TOPICS__", _json.dumps(topics, ensure_ascii=False))
    t = t.replace("__KIND__", cfg["kind"])
    t = t.replace("__SLUG__", _json.dumps(cfg["slug"]))
    return t

def write_db_files(cfg, topics):
    d = os.path.join(HUB, "db", cfg["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_page(cfg))
    with open(os.path.join(d, "gen-%s.js" % cfg["slug"]), "w", encoding="utf-8") as f:
        f.write(build_gen_js(cfg, topics))
    return d
