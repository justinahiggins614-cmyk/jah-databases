(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK119-";
var KIND="search method";
var TOOLNAME="Absence-Based Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Missing-field queries", "d": "The simplest absence query lists records lacking a required field: 'WHERE author IS NULL'. Indexes need explicit null handling since missing values are not indexed like present ones. Missing-field queries drive data-quality dashboards.", "c": "fundamentals", "r": 1, "p": {"REQUIRED": "['author', 'year']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'author': 'A', 'year': 2020}, {'id': 'r2', 'year': 2021}, {'id': 'r3', 'author': 'B'}]"}}, {"t": "Completeness scoring", "d": "Completeness scores count present versus expected fields per record, often weighted by importance. Scores rank records for curation priority: lowest completeness gets fixed first. Weighted completeness reflects that a missing title hurts more than a missing note.", "c": "algorithms", "r": 1, "p": {"REQUIRED": "['title', 'author', 'year', 'abstract']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'title': 'T', 'author': 'A', 'year': 2020, 'abstract': 'x'}, {'id': 'r2', 'title': 'T2'}]"}}, {"t": "Absent-term search", "d": "Absence also applies to content: documents that never mention a term, found via NOT queries. 'Reports not mentioning budget' combines a topic filter with a negated term test. Negated content tests need the full vocabulary to evaluate correctly.", "c": "implementation", "r": 1, "p": {"REQUIRED": "[]", "ABSENT": "['budget']", "RECORDS": "[{'id': 'r1', 'text': 'the annual report summary'}, {'id': 'r2', 'text': 'the budget report summary'}]"}}, {"t": "Schema-drift detection", "d": "New fields appear over time; absence queries find old records predating a field's introduction. 'Records without geolocation' often means 'records from before we captured locations'. Drift-aware absence separates true gaps from historical practice.", "c": "optimization", "r": 1, "p": {"REQUIRED": "['geo']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'geo': 'x'}, {'id': 'r2', 'title': 'old record'}]"}}, {"t": "Required versus optional", "d": "Schemas distinguish required fields (must exist) from optional ones (may be absent). Absence queries target required-field violations, not optional emptiness. The distinction keeps quality reports actionable instead of noisy.", "c": "evaluation", "r": 1, "p": {"REQUIRED": "['id', 'title']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'title': 'T', 'note': 'n'}, {'id': 'r2', 'note': 'n'}]"}}, {"t": "Conditional requirements", "d": "Some fields are required only when others exist: 'if type=book then ISBN is required'. Rule engines evaluate requirement expressions per record. Conditional rules capture real-world cataloging policy.", "c": "fundamentals", "r": 2, "p": {"REQUIRED": "['isbn']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'type': 'book'}, {'id': 'r2', 'type': 'book', 'isbn': 'x'}, {'id': 'r3', 'type': 'map'}]"}}, {"t": "Empty versus missing", "d": "Empty strings and nulls both look absent but mean different things: unknown versus known-empty. Absence queries let users choose which counts. Collapsing the distinction corrupts downstream statistics.", "c": "algorithms", "r": 2, "p": {"REQUIRED": "['abstract']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'abstract': ''}, {'id': 'r2'}, {'id': 'r3', 'abstract': 'text'}]"}}, {"t": "Absence in time series", "d": "Missing time buckets (no reading for Tuesday) indicate sensor or pipeline gaps. Gap detection scans sorted timestamps for intervals exceeding the expected cadence. Temporal absence queries keep monitoring honest.", "c": "implementation", "r": 2, "p": {"REQUIRED": "['reading']", "ABSENT": "[]", "RECORDS": "[{'id': 'mon', 'reading': 1}, {'id': 'tue'}, {'id': 'wed', 'reading': 3}]"}}, {"t": "Negative evidence in retrieval", "d": "Absence can be evidence: a contract without a termination clause is materially different. Retrieval models score the verified absence of terms, not just their presence. Negative evidence needs explicit checks; absence of evidence is not evidence of absence.", "c": "optimization", "r": 2, "p": {"REQUIRED": "[]", "ABSENT": "['termination']", "RECORDS": "[{'id': 'c1', 'text': 'contract terms payment'}, {'id': 'c2', 'text': 'contract termination terms'}]"}}, {"t": "Coverage analysis", "d": "Coverage asks what fraction of the collection has each field, guiding acquisition. 'Only 40% of records have subjects' justifies a subject-enrichment project. Coverage reports turn absence into a work plan.", "c": "evaluation", "r": 2, "p": {"REQUIRED": "['subject']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'subject': 's'}, {'id': 'r2'}, {'id': 'r3', 'subject': 's2'}, {'id': 'r4'}]"}}, {"t": "Dangling references", "d": "References pointing to nonexistent records are absence at the link level. Integrity checks join references against the record set and report orphans. Dangling-link reports keep citation graphs clean.", "c": "fundamentals", "r": 3, "p": {"REQUIRED": "['target']", "ABSENT": "[]", "RECORDS": "[{'id': 'l1', 'target': 'r9'}, {'id': 'l2'}]"}}, {"t": "Absence-based anomaly detection", "d": "Records missing fields their peers all have are anomalies worth inspecting. Peer-group comparison (same type, same era) defines the expectation. Anomaly flags route to curators instead of failing silently.", "c": "algorithms", "r": 3, "p": {"REQUIRED": "['author', 'year', 'title']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'author': 'A', 'year': 2020, 'title': 'T'}, {'id': 'r2', 'title': 'T2'}]"}}, {"t": "Backfill prioritization", "d": "Absence queries rank incomplete records by value times incompleteness for backfill scheduling. High-value, highly-incomplete records get enriched first. Prioritized backfill spends curation effort where it matters.", "c": "implementation", "r": 3, "p": {"REQUIRED": "['abstract', 'subjects']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'views': 99}, {'id': 'r2', 'abstract': 'a', 'subjects': 's', 'views': 3}]"}}, {"t": "Proving a negative", "d": "'Show me contracts with no arbitration clause' demands exhaustive verified absence. Systems certify the search scope (which collections, which fields) alongside the empty result. Certified absence is auditable; casual absence is a guess.", "c": "optimization", "r": 3, "p": {"REQUIRED": "[]", "ABSENT": "['arbitration']", "RECORDS": "[{'id': 'c1', 'text': 'payment terms'}, {'id': 'c2', 'text': 'arbitration clause present'}]"}}, {"t": "Absence dashboards", "d": "Dashboards track missing-field rates over time, alerting when ingestion degrades. Trend lines distinguish one-off gaps from systemic pipeline failures. Monitoring absence keeps data quality from silently rotting.", "c": "evaluation", "r": 3, "p": {"REQUIRED": "['title', 'date']", "ABSENT": "[]", "RECORDS": "[{'id': 'r1', 'title': 'T', 'date': 'd'}, {'id': 'r2', 'title': 'T2'}]"}}];
var DEMO="# Absence-based search: find records missing required fields or characteristics.\nrecords = %%RECORDS%%\nrequired = %%REQUIRED%%\nabsent_terms = %%ABSENT%%\ndef missing_fields(rec):\n    return [f for f in required if f not in rec or rec[f] in (None, \"\", [])]\nprint(\"Required fields:\", required, \"| must-not-contain:\", absent_terms or \"none\")\nfor r in records:\n    miss = missing_fields(r)\n    text = \" \".join(str(v) for v in r.values()).lower()\n    bad = [t for t in absent_terms if t.lower() in text]\n    if miss or bad:\n        print(f\"  {r['id']}: missing {miss or '-'}; unwanted terms {bad or '-'}\")\n";
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
  if(!new RegExp("^JAH\\-ATK119\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-absence-based-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-absence-based-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
