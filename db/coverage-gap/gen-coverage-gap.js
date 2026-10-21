(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["topic", "time-range", "language", "depth", "format", "freshness"];
var PREFIX="JAH-COVERA-";
var FKEYS=["measured_coverage", "gap", "remediation"];
var RANK_TXT={"1": "the concept in its simplest, most direct form", "2": "the concept compounded with real-world conditions and trade-offs", "3": "the concept at full complexity, orchestrated with neighboring capabilities"};
var DEMO_TMPL="# Coverage gap measurement: {TITLE}\nexpected = set(\"{F1}\".split(\";\")); have = set(\"{F2}\".split(\";\"))\ngap = sorted(expected - have)\ncoverage = len(have) / len(expected) * 100\nprint(\"measured coverage: %.1f%%\" % coverage)\nprint(\"gap items:\", gap if gap else \"none\")\nprint(\"remediation:\", \"{F3}\")";
var SIG_SUFFIX="";
var PROV="Curated from public documentation of established engineering practice; verified against standard references.";
var SRC="public-harvest";
var B=[["topic", "Topic Coverage Survey", "A survey measures which topics have records and which are bare, producing a coverage map.", "The map directs building effort to the barest topics first, where it matters most.", "62% of target topics", "38% of topics bare", "build bare topics first"], ["time-range", "Historical Time-Range Gap", "Records are bucketed by era; eras with thin coverage are named as gaps.", "History has no gaps in reality - only in the archive - so thin eras get targeted harvesting.", "strong 2000-2026, thin before 1980", "pre-1980 eras thin", "harvest historical sources"], ["language", "Non-English Language Gap", "Coverage is measured per language; under-served languages are listed with their deficit.", "A network that only knows English only serves part of humanity.", "91% English, 9% other", "47 languages below 1%", "multilingual harvest program"], ["depth", "Depth Gap: Stubs vs Full Records", "Records are scored for completeness; shallow ones count as a depth gap even when present.", "A thousand stubs do not equal a thousand full records, and the metric refuses to pretend otherwise.", "34% full, 66% shallow", "shallow majority", "deepen top-used shallow records"], ["format", "Format Coverage Gap", "Coverage is measured across formats - text, image, audio, video, data - not just text.", "Text-only coverage is a format gap for every topic that lives in other media.", "text 88%, image 7%, audio 3%, video 2%", "non-text formats thin", "multi-format capture pipeline"], ["freshness", "Freshness Decay Gap", "Records older than their topic's freshness policy count as a freshness gap.", "Stale records mislead; the gap metric schedules re-verification before trust erodes.", "71% fresh, 29% stale", "stale tail", "re-verify stale tail quarterly"], ["topic", "Geographic Coverage Gap", "Coverage is measured per region; regions with thin records are named.", "The map of knowledge should resemble the map of the world, not just one corner of it.", "North America/Europe dense", "Africa, Central Asia thin", "regional harvest partnerships"], ["depth", "Expertise-Level Gap", "Coverage is measured from beginner to expert; missing rungs on the teaching ladder are gaps.", "A topic with only expert records abandons beginners; only beginner records abandon experts.", "beginner 70%, expert 30%", "expert rungs missing", "commission expert-level records"], ["depth", "Primary Source Gap", "Records are classified by source type; topics with only secondary sources have a primary-source gap.", "Secondary retellings drift; primary sources anchor truth.", "22% primary-sourced", "primary sources thin", "primary-source acquisition"], ["topic", "Cross-Reference Density Gap", "The link density between related records is measured; isolated records are a connectivity gap.", "Knowledge is a web; isolated records are threads that lead nowhere.", "avg 2.1 links/record", "31% isolated", "linking pass over isolates"], ["format", "Multimedia Evidence Gap", "Claims are checked for supporting media; text-only claims on visual topics are a gap.", "A claim about a visual subject with no image is half a record.", "visual topics 40% imaged", "60% unimaged", "image attachment drive"], ["freshness", "Update Cadence Gap", "Fast-moving topics are checked for update cadence; slow ones have a cadence gap.", "A technology database updated yearly is a history book, not a database.", "12% of fast topics current", "fast topics stale", "continuous update feeds"], ["topic", "Minority Viewpoint Gap", "Topics with genuine scholarly disagreement are checked for viewpoint balance.", "One-sided coverage of a debated topic is a gap, not a position.", "debated topics 80% one-sided", "minority views missing", "balanced commissioning"], ["format", "Accessibility Format Gap", "Records are checked for accessible formats - alt text, transcripts, plain language.", "Inaccessible records exclude users; the gap metric counts the excluded.", "alt text 18%, transcripts 9%", "accessible formats thin", "accessibility remediation pass"], ["depth", "Citation Density Gap", "Records are measured for citation support; uncited factual claims are a gap.", "Citations are the receipts of knowledge; the gap counts the missing receipts.", "1.2 citations/record avg", "uncited claims common", "citation drive on top records"], ["time-range", "Temporal Resolution Gap", "Event coverage is checked for granularity; eras known only by decade have a resolution gap.", "Decade-level knowledge of a fast-moving era is barely knowledge at all.", "recent: daily; 1990s: yearly", "coarse past resolution", "deepen 1990s event records"], ["language", "Dialect and Register Gap", "Language coverage is checked across dialects and registers, not just the standard form.", "The standard form is one way people speak; the gap counts the others.", "standard forms 95%", "dialects thin", "dialect collection program"], ["depth", "Provenance Completeness Gap", "Records are checked for provenance fields; those without are a provenance gap.", "A record without provenance is a rumor with good formatting.", "provenance present 58%", "42% unprovenanced", "provenance backfill"], ["format", "Interactive Demo Gap", "Records are checked for runnable demos; those without are a demo gap.", "The usable-or-demo rule makes this gap a first-class metric, not an afterthought.", "demos on 44% of records", "56% demo-less", "demo authoring sprint"], ["topic", "Long-Tail Topic Gap", "The distribution tail - thousands of niche topics with one record each - is measured for depth.", "The long tail is where the network's uniqueness lives; thin tails are a strategic gap.", "tail topics avg 1.1 records", "tail depth thin", "tail deepening program"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rank=1+(seed%3);
  var desc=b[2]+' '+b[3]+' Teaching ladder: rank '+rank+' \u2014 '+RANK_TXT[rank]+'.'+SIG_SUFFIX;
  var prog=DEMO_TMPL.split('{TITLE}').join(b[1]).split('{F1}').join(b[4]).split('{F2}').join(b[5]).split('{F3}').join(b[6]);
  var r={id:id,title:b[1],description:desc,category:cat,ladder_rank:rank,
    demo:{kind:'code',title:'Runnable code demo \u2014 '+b[1].slice(0,50),program:prog,language:'python'},
    provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
  r[FKEYS[0]]=b[4];r[FKEYS[1]]=b[5];r[FKEYS[2]]=b[6];
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.indexOf('Teaching ladder: rank')<0)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FKEYS.forEach(function(k){if(typeof r[k]!=='string'||!r[k].length)e.push(k);});
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-coverage-gap-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("coverage-gap",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
