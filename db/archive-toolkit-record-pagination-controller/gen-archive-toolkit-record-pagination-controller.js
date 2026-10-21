(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK124-";
var KIND="traversal method";
var TOOLNAME="Record Pagination Controller";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Offset/limit pagination", "d": "OFFSET skips rows and LIMIT takes a page; page p of size s is OFFSET (p-1)*s LIMIT s. It is simple and universal across SQL databases. Offset pagination underlies most list UIs.", "c": "fundamentals", "r": 1, "p": {"PAGE": "2", "SIZE": "5", "TOTAL": "23"}}, {"t": "Total-count queries", "d": "'Page 2 of 47' needs the total, usually from COUNT(*) over the same filters. Counts can be expensive; estimates or cached counts often suffice. Showing totals trades one extra query for user orientation.", "c": "algorithms", "r": 1, "p": {"PAGE": "1", "SIZE": "10", "TOTAL": "95"}}, {"t": "Page-window rendering", "d": "UIs show a window of page numbers around the current page (1 ... 4 5 6 ... 47). Windows keep navigation compact on huge result sets. Ellipses mark the skipped ranges.", "c": "implementation", "r": 1, "p": {"PAGE": "5", "SIZE": "10", "TOTAL": "230"}}, {"t": "Unstable offsets", "d": "Inserts and deletes shift offsets, so page 2 may repeat or skip rows. Offset pagination assumes a stable snapshot. Live datasets need cursor pagination for stability.", "c": "optimization", "r": 1, "p": {"PAGE": "3", "SIZE": "5", "TOTAL": "40"}}, {"t": "Deep-offset cost", "d": "OFFSET 100000 still scans and discards 100000 rows; cost grows with page number. Deep pages are the classic pagination performance cliff. Seek-based methods fix deep offsets.", "c": "evaluation", "r": 1, "p": {"PAGE": "20", "SIZE": "10", "TOTAL": "500"}}, {"t": "Seek (keyset) pagination", "d": "Keyset pagination remembers the last seen key and fetches 'WHERE id > last LIMIT s'. It pages in constant time regardless of depth and stays stable under inserts. Keyset is the production choice for large lists.", "c": "fundamentals", "r": 2, "p": {"PAGE": "2", "SIZE": "5", "TOTAL": "23"}}, {"t": "Page-size choices", "d": "Sizes balance round-trips against payload: 20-50 for humans, 100-1000 for APIs. Allowing user-chosen sizes needs server-side caps. Sane defaults with caps prevent abuse.", "c": "algorithms", "r": 2, "p": {"PAGE": "1", "SIZE": "25", "TOTAL": "120"}}, {"t": "First/prev/next/last controls", "d": "Navigation controls expose the four moves plus direct page entry. Disabled states communicate boundaries. Complete controls need the total page count.", "c": "implementation", "r": 2, "p": {"PAGE": "4", "SIZE": "5", "TOTAL": "23"}}, {"t": "Sorting stability", "d": "Pagination requires a deterministic ORDER BY; ties need a unique tiebreaker. Without it, rows wander between pages. (sort_key, id) ordering guarantees stability.", "c": "optimization", "r": 2, "p": {"PAGE": "2", "SIZE": "5", "TOTAL": "30"}}, {"t": "Filtered pagination", "d": "Filters apply before pagination; counts and pages reflect the filtered set. Changing filters resets to page 1. Filter-then-paginate is the correct order.", "c": "evaluation", "r": 2, "p": {"PAGE": "1", "SIZE": "5", "TOTAL": "17"}}, {"t": "Empty-page handling", "d": "Requests beyond the last page return empty with a hint, not an error. Clamping to the last page is friendlier. Graceful empties keep UIs robust.", "c": "fundamentals", "r": 3, "p": {"PAGE": "99", "SIZE": "5", "TOTAL": "23"}}, {"t": "Prefetching neighbors", "d": "Prefetching page p+1 while the user reads page p hides latency. Cache the prefetched page briefly. Speculative prefetch trades bandwidth for snappiness.", "c": "algorithms", "r": 3, "p": {"PAGE": "2", "SIZE": "5", "TOTAL": "50"}}, {"t": "Export versus paginate", "d": "Bulk export streams the whole set instead of paging through it. Pagination is for browsing; cursors or dumps are for extraction. Using the right tool avoids thousand-page crawls.", "c": "implementation", "r": 3, "p": {"PAGE": "1", "SIZE": "10", "TOTAL": "1000"}}, {"t": "Accessibility of paging", "d": "Pagination controls need labels, current-page announcement, and keyboard support. 'Page 3 of 12' text beats bare numbers for screen readers. Accessible paging serves every user.", "c": "optimization", "r": 3, "p": {"PAGE": "3", "SIZE": "5", "TOTAL": "60"}}, {"t": "Pagination metadata APIs", "d": "APIs return {items, page, size, total, has_next} so clients render controls. Cursor APIs return {items, next_cursor} instead. Consistent metadata contracts simplify every client.", "c": "evaluation", "r": 3, "p": {"PAGE": "2", "SIZE": "5", "TOTAL": "23"}}];
var DEMO="# Pagination: offset/limit pages plus page-window navigation metadata.\nrecords = [\"rec-%02d\" % i for i in range(1, %%TOTAL%% + 1)]\npage, size = %%PAGE%%, %%SIZE%%\ntotal_pages = (len(records) + size - 1) // size\npage = max(1, min(page, total_pages))\nstart = (page - 1) * size\nitems = records[start:start + size]\nwindow = [p for p in range(max(1, page-2), min(total_pages, page+2) + 1)]\nprint(f\"Page {page}/{total_pages} (size {size}, total {len(records)}): {items}\")\nprint(\"window:\", window, \"| has_prev:\", page > 1, \"| has_next:\", page < total_pages)\n";
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
  if(!new RegExp("^JAH\\-ATK124\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-record-pagination-controller-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-record-pagination-controller",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
