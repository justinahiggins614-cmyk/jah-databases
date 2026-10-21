(function(){'use strict';
var PREFIX="JAH-ATK215-";
var METHODS=[["Batched paging", "Export in fixed-size batches with stable cursors so a failure resumes mid-export instead of restarting."], ["Format selection", "Offer JSON lines, CSV, Parquet, and XML with per-format type mapping documented up front."], ["Compression on the fly", "Gzip or zstd each batch as it is produced so network and disk costs stay proportional."], ["Permission pre-check", "Verify the caller may export every record in the set before producing byte one."], ["Redaction pipeline", "Apply field-level redaction during export so restricted fields never land in the file."], ["Checksum manifests", "Ship a manifest with per-batch hashes so the caller verifies completeness on receipt."], ["Export quotas", "Cap rows and bytes per caller per day, with explicit escalation for legitimate bulk needs."], ["Progress callbacks", "Report rows written, bytes, and ETA through a job API the caller can poll or subscribe to."], ["Format validation", "Validate each batch against the target format's schema before writing so the file opens cleanly."], ["Incremental exports", "Export only records changed since a watermark for recurring sync jobs."], ["Column selection", "Let the caller choose columns at export time to shrink files and limit exposure."], ["Direct-to-storage delivery", "Write large exports straight to the caller's object storage instead of through the app server."], ["Export audit log", "Record who exported what, when, and under which policy for compliance review."], ["Sample-before-full", "Offer a 100-row sample export so callers validate shape before committing to the full run."], ["Retention-bounded files", "Expire export files after a policy window and notify before deletion."]];
var CATS=["export", "delivery", "batch"];
var DEMO="# Large-Result Exporter demo: batched JSONL export with manifest + resume.\nimport json,hashlib,gzip,io\nRECS=[{\"id\":\"r%03d\"%i,\"v\":i} for i in range(10)]\ndef export_batch(recs,batch=4,start=0):\n    out=io.BytesIO(); manifest=[]\n    for b in range(start,len(recs),batch):\n        chunk=recs[b:b+batch]\n        data=b\"\".join((json.dumps(r)+\"\\n\").encode() for r in chunk)\n        comp=gzip.compress(data)\n        h=hashlib.sha256(comp).hexdigest()[:12]\n        manifest.append({\"batch\":b//batch,\"rows\":len(chunk),\"sha\":h,\"bytes\":len(comp)})\n    return manifest\nm=export_batch(RECS); print(\"batches:\",len(m))\nprint(\"manifest[0]:\",m[0]); print(\"total rows:\",sum(x[\"rows\"] for x in m))\nprint(\"resume from batch 2 ->\",len(export_batch(RECS,start=8)),\"batch(es)\")\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Large-Result Exporter";
  return {id:id,t:title,title:title,description:"The large-result exporter moves big answer sets out of the archive and into the caller's hands without breaking either side: paged batches, multiple formats, compression, checksums, and resume support. It enforces permission checks before a single byte leaves, applies redaction where policy demands, and treats a 10-million-row export as normal operations rather than an emergency. Every export is a",
    kind:"delivery tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-large-result-exporter-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-large-result-exporter",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();