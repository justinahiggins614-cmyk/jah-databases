(function(){'use strict';
var PREFIX="JAH-ATK218S-";
var METHODS=[["Query recipe capture", "Serialize the full query \u2014 text, filters, facets, ranking config \u2014 into a versioned recipe file."], ["Index version pinning", "Record the exact index builds the search ran against so replay uses the same data, not today's."], ["Deterministic ranking", "Force deterministic tie-breaking in the ranker so identical inputs always produce identical orders."], ["Result set hashing", "Hash the delivered result ids so replay can prove equality or pinpoint divergence."], ["Environment capture", "Record software versions of the retrieval stack alongside the recipe."], ["Diff-on-replay", "On replay, diff the new results against the saved set and classify changes (new records, re-ranked, removed)."], ["Recipe sharing", "Make recipes portable artifacts colleagues can run without reconstructing the original session."], ["Parameter sensitivity notes", "Record which parameters the result set is sensitive to, guiding safe recipe edits."], ["Time-travel queries", "Support replaying a recipe against historical index snapshots, not just the pinned one."], ["Recipe validation", "Lint recipes for deprecated parameters or retired sources before they run."], ["Provenance embedding", "Embed the recipe id in every delivered result so results point back to how they were found."], ["Batch recipe runs", "Run many recipes on a schedule and alert when their result sets drift past a threshold."], ["Access-scoped replay", "Replay under the original caller's permissions so restricted results do not leak through sharing."], ["Recipe templates", "Provide templates for common reproducible searches (systematic review, compliance sweep)."], ["Citation export", "Export the recipe plus result hashes in citation format for papers and reports."]];
var CATS=["reproducibility", "provenance", "packaging"];
var DEMO="# Reproducible Retrieval Packager demo: recipe capture, deterministic replay, diff.\nimport hashlib,json\nINDEX=[{\"id\":\"d1\",\"text\":\"solar sails\"},{\"id\":\"d2\",\"text\":\"sail boats\"},{\"id\":\"d3\",\"text\":\"photon sails\"}]\ndef run(recipe):\n    q=recipe[\"query\"]; k=recipe[\"k\"]\n    hits=sorted([d for d in INDEX if q in d[\"text\"]],key=lambda d:d[\"id\"])[:k]\n    return [h[\"id\"] for h in hits]\nrecipe={\"query\":\"sail\",\"k\":2,\"index_version\":\"idx-2026-10-21\",\"ranker\":\"det-v1\"}\nr1=run(recipe)\nh1=hashlib.sha256(json.dumps(r1).encode()).hexdigest()[:12]\nprint(\"recipe:\",recipe); print(\"results:\",r1,\"hash:\",h1)\nINDEX.append({\"id\":\"d0\",\"text\":\"sail repair\"})  # archive grew\nr2=run(recipe)\nprint(\"replay after growth:\",r2,\"changed:\",set(r1)^set(r2) or \"none\")\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Reproducible Retrieval Packager (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. The reproducible retrieval packager makes a search replayable: it saves the query text, filters, source identifiers, ranking configuration, index versions, and timestamps into a retrieval recipe. Anyone running the recipe later gets the same result set \u2014 or a precise diff explaining what changed and why. In regulated and scientific work, 'I searched and found' is not enough; the search itself must",
    kind:"delivery tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
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
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-reproducible-retrieval-packager-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-reproducible-retrieval-packager-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();