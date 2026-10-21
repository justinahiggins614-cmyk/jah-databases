(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["rubric","worked-example"];
var PREFIX="JAH-FRSCS-";
var WEIGHTS={"completeness":20,"validity":25,"demo_executed":20,"description_depth":15,"spec_linked":10,"proof_validation":10};
/* Deterministic published scoring rubric: observations -> 0-100 score. */
function dimScores(o){
  var d={},s=0;
  if(o.n_index===o.n_expected)s+=4; if(o.fields_complete)s+=3; if(o.chunks_present)s+=3; d.completeness=s;
  s=0; if(o.jsonl_clean)s+=2; if(o.ids_unique)s+=2; if(o.ids_prefixed)s+=2; if(o.slug_format)s+=2; if(o.slug_unique)s+=2; d.validity=s;
  if(o.demo_executed_live)s=10; else if(o.demos_all_compile)s=7; else if(o.demos_parse)s=4; else s=0; d.demo_executed=s;
  var mw=o.mean_desc_words||0,minw=o.min_desc_words||0;
  if(mw>=40&&minw>=25)s=10; else if(mw>=25)s=7; else if(mw>=15)s=5; else if(mw>=5)s=3; else s=0; d.description_depth=s;
  s=0; if(o.fullspec_pane)s+=4; if(o.spec_filed)s+=3; if(o.wiki_entry)s+=2; if(o.dict_entry)s+=1; d.spec_linked=s;
  s=0; if(o.validation_green)s+=4; if(o.demo_compile_evidence)s+=3; if(o.demo_confirmed_this_file)s+=3; d.proof_validation=s;
  return d;
}
function score(o){var d=dimScores(o),t=0,k;for(k in WEIGHTS)t+=d[k]*WEIGHTS[k];return Math.floor(t/10+0.5);}
var DEMO_SCORER='\nimport math\nWEIGHTS = {"completeness": 20, "validity": 25, "demo_executed": 20,\n           "description_depth": 15, "spec_linked": 10, "proof_validation": 10}\n\ndef dim_scores(o):\n    """o: dict of observations. Returns {dimension: 0-10}."""\n    d = {}\n    s = 0\n    if o.get("n_index") == o.get("n_expected"):\n        s += 4\n    if o.get("fields_complete"):\n        s += 3\n    if o.get("chunks_present"):\n        s += 3\n    d["completeness"] = s\n    s = 0\n    if o.get("jsonl_clean"):\n        s += 2\n    if o.get("ids_unique"):\n        s += 2\n    if o.get("ids_prefixed"):\n        s += 2\n    if o.get("slug_format"):\n        s += 2\n    if o.get("slug_unique"):\n        s += 2\n    d["validity"] = s\n    if o.get("demo_executed_live"):\n        s = 10\n    elif o.get("demos_all_compile"):\n        s = 7\n    elif o.get("demos_parse"):\n        s = 4\n    else:\n        s = 0\n    d["demo_executed"] = s\n    mw = o.get("mean_desc_words", 0) or 0\n    minw = o.get("min_desc_words", 0) or 0\n    if mw >= 40 and minw >= 25:\n        s = 10\n    elif mw >= 25:\n        s = 7\n    elif mw >= 15:\n        s = 5\n    elif mw >= 5:\n        s = 3\n    else:\n        s = 0\n    d["description_depth"] = s\n    s = 0\n    if o.get("fullspec_pane"):\n        s += 4\n    if o.get("spec_filed"):\n        s += 3\n    if o.get("wiki_entry"):\n        s += 2\n    if o.get("dict_entry"):\n        s += 1\n    d["spec_linked"] = s\n    s = 0\n    if o.get("validation_green"):\n        s += 4\n    if o.get("demo_compile_evidence"):\n        s += 3\n    if o.get("demo_confirmed_this_file"):\n        s += 3\n    d["proof_validation"] = s\n    return d\n\ndef total_score(dims):\n    t = sum(dims[k] * WEIGHTS[k] for k in WEIGHTS) / 10.0\n    return int(math.floor(t + 0.5))  # round half-up, whole number\n\n# Usage: build an OBS dict of the six dimension observations,\n# then dims = dim_scores(OBS); print(total_score(dims)).\n';
var SIG_SUFFIX=' Signature original by Justin Addam Higgins.';
var PROV='Signature original by Justin Addam Higgins - a Signature-authored scoring analysis, never presented as public record.';
var SRC='signature-generated-completion';
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed*2654435761>>>0);
  var cat=opts.category||pick(CATS,rnd);
  var rank=1+((rnd()*3)|0);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=(cat==='rubric'?'Rubric dimension scoring record':'Worked leaderboard scoring record')+' #'+seed;
  var r={id:id,title:title,description:title+'. Deterministic rubric scoring record, rank '+rank+'.'+SIG_SUFFIX,category:cat,ladder_rank:rank,
    demo:{kind:'code',title:'Runnable rubric scorer',program:DEMO_SCORER,language:'python'},
    provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed,
    weights:WEIGHTS};
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-file-ranker-scorer-signature-1.0",generate:generate,validate:validate,score:score,dimScores:dimScores};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("file-ranker-scorer-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
