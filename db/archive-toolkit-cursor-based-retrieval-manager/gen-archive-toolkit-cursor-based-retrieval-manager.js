(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK125-";
var KIND="traversal method";
var TOOLNAME="Cursor-Based Retrieval Manager";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Opaque cursor tokens", "d": "Cursors are opaque to clients: base64 blobs encoding position, never raw offsets. Opacity lets servers change the encoding without breaking clients. Clients treat cursors as bookmarks.", "c": "fundamentals", "r": 1, "p": {"TOTAL": "12", "SIZE": "5", "STEPS": "3"}}, {"t": "Stability under inserts", "d": "New rows inserted ahead do not shift a cursor anchored at the last seen key. Cursor pagination never duplicates or skips on live data. Stability is why feeds and APIs prefer cursors.", "c": "algorithms", "r": 1, "p": {"TOTAL": "15", "SIZE": "5", "STEPS": "3"}}, {"t": "Keyset encoding", "d": "The cursor encodes the last row's sort key values, e.g. (created_at, id). Decoding restores the WHERE clause for the next page. Composite keys need tuple comparison.", "c": "implementation", "r": 1, "p": {"TOTAL": "10", "SIZE": "4", "STEPS": "3"}}, {"t": "Bidirectional cursors", "d": "Backward paging encodes the first row's keys and reverses the sort. Both directions share the same encoding scheme. Bidirectional cursors serve 'load newer' and 'load older'.", "c": "optimization", "r": 1, "p": {"TOTAL": "12", "SIZE": "5", "STEPS": "2"}}, {"t": "Cursor expiry", "d": "Cursors embed timestamps; servers reject stale ones to bound state. Expiry prevents ancient bookmarks from hitting cold storage. Short TTLs suit fast-moving data.", "c": "evaluation", "r": 1, "p": {"TOTAL": "8", "SIZE": "3", "STEPS": "3"}}, {"t": "Stateless versus stateful", "d": "Stateless cursors encode everything; stateful cursors reference server-side snapshots. Stateless scales horizontally; stateful guarantees repeatability. The choice trades infrastructure for semantics.", "c": "fundamentals", "r": 2, "p": {"TOTAL": "10", "SIZE": "5", "STEPS": "2"}}, {"t": "Tamper-proofing", "d": "Signed cursors (HMAC) stop clients from forging positions. Verification is one hash check per request. Signing matters when cursors gate access.", "c": "algorithms", "r": 2, "p": {"TOTAL": "9", "SIZE": "3", "STEPS": "3"}}, {"t": "Page-size in cursor flow", "d": "Clients request n items per fetch; servers cap n. Consistent sizes keep memory predictable. Caps protect shared infrastructure.", "c": "implementation", "r": 2, "p": {"TOTAL": "14", "SIZE": "6", "STEPS": "3"}}, {"t": "End-of-data signals", "d": "A null next-cursor (or empty page with no cursor) signals completion. Clients stop cleanly instead of polling forever. Explicit termination beats guessing.", "c": "optimization", "r": 2, "p": {"TOTAL": "7", "SIZE": "5", "STEPS": "3"}}, {"t": "Resuming interrupted scans", "d": "Saved cursors resume long scans after crashes. Checkpointing the cursor per batch bounds rework. Resumability turns days-long scans into safe operations.", "c": "evaluation", "r": 2, "p": {"TOTAL": "20", "SIZE": "7", "STEPS": "3"}}, {"t": "Cursors over joins", "d": "Join cursors encode keys from the driving table plus tiebreakers. Correct encoding preserves join order across pages. Join paging needs the full ORDER BY in the cursor.", "c": "fundamentals", "r": 3, "p": {"TOTAL": "11", "SIZE": "4", "STEPS": "3"}}, {"t": "Time-based cursors", "d": "Event streams cursor on (timestamp, sequence): 'everything after T#seq'. Monotonic sequence numbers disambiguate same-timestamp events. Time cursors suit logs and feeds.", "c": "algorithms", "r": 3, "p": {"TOTAL": "13", "SIZE": "5", "STEPS": "3"}}, {"t": "Cursor invalidation", "d": "Schema or filter changes invalidate saved cursors; version tags detect this. Mismatched versions get a clean error, not wrong data. Invalidation keeps semantics honest.", "c": "implementation", "r": 3, "p": {"TOTAL": "10", "SIZE": "5", "STEPS": "2"}}, {"t": "Rate-limited fetching", "d": "Fetch loops respect rate limits, backing off between pages. Jittered delays avoid thundering herds. Polite fetching keeps APIs healthy.", "c": "optimization", "r": 3, "p": {"TOTAL": "16", "SIZE": "5", "STEPS": "3"}}, {"t": "Cursor debugging", "d": "Decoding tools reveal what a cursor encodes during development. Never expose decoders that leak internals to untrusted clients. Debuggability speeds integration.", "c": "evaluation", "r": 3, "p": {"TOTAL": "6", "SIZE": "2", "STEPS": "3"}}];
var DEMO="# Cursor pagination: opaque base64 cursors encode (last_id); each fetch continues.\nimport base64, json\nrecords = [{\"id\": i, \"v\": \"rec-%02d\" % i} for i in range(1, %%TOTAL%% + 1)]\ndef encode(last_id): return base64.urlsafe_b64encode(json.dumps({\"last\": last_id}).encode()).decode()\ndef decode(cur): return json.loads(base64.urlsafe_b64decode(cur.encode()))[\"last\"] if cur else 0\ndef fetch(cursor, n):\n    last = decode(cursor)\n    batch = [r for r in records if r[\"id\"] > last][:n]\n    nxt = encode(batch[-1][\"id\"]) if len(batch) == n and batch[-1][\"id\"] < records[-1][\"id\"] else None\n    return batch, nxt\ncur, n = None, %%SIZE%%\nfor step in range(%%STEPS%%):\n    batch, cur = fetch(cur, n)\n    print(f\"batch: {[r['v'] for r in batch]} -> next cursor: {cur[:12] + '...' if cur else None}\")\n    if not cur: break\n";
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
  if(!new RegExp("^JAH\\-ATK125\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-cursor-based-retrieval-manager-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-cursor-based-retrieval-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
