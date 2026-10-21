(function(){'use strict';
var PREFIX="JAH-ATK210-";
var METHODS=[["Manifest parsing", "Read package manifests, lockfiles, and environment specs to seed the dependency graph automatically."], ["Import graph extraction", "Statically scan source imports to catch dependencies the manifest forgot to declare."], ["Transitive closure", "Walk the graph to full depth so indirect dependencies are included, with cycle detection."], ["Version pinning", "Resolve every dependency to an exact version (or hash) so the retrieved set reproduces bit-for-bit."], ["Conflict detection", "Flag version conflicts where two branches of the graph demand incompatible versions of one library."], ["Data dependency tracking", "Treat datasets and model weights as first-class dependencies with their own versions and checksums."], ["Environment capture", "Record OS, interpreter, and system library versions alongside code dependencies."], ["Credential inventory", "List required secrets and credentials without retrieving their values, so operators know what to provision."], ["Hardware requirements", "Surface CPU, GPU, memory, and device requirements declared or inferred from the dependency set."], ["License compatibility check", "Check the dependency set's licenses for conflicts before the caller builds on it."], ["Minimal install sets", "Compute the smallest subset that still runs the target, pruning dev-only and optional dependencies."], ["Dependency freshness report", "Flag dependencies that are unmaintained or carry known vulnerabilities."], ["Reproducibility bundle export", "Package code, data, environment spec, and pins into one bundle another machine can replay."], ["Graph visualization", "Render the dependency graph so humans can see the shape of what they are about to install."], ["Drift detection", "Re-run retrieval later and diff the set, catching dependencies that moved under a floating version."]];
var CATS=["dependencies", "reproducibility", "graphs"];
var DEMO="# Retrieval-by-Dependency demo: transitive closure with cycle detection + pinning.\nGRAPH={\"app\":[\"libA\",\"dataX\"],\"libA\":[\"libB\",\"libA2\"],\"libB\":[],\"libA2\":[\"libB\"],\n       \"dataX\":[],\"loop1\":[\"loop2\"],\"loop2\":[\"loop1\"]}\nPINS={\"libA\":\"1.4.2\",\"libB\":\"0.9.1\",\"libA2\":\"2.0.0\",\"dataX\":\"sha256:abc\"}\ndef closure(root):\n    seen=set(); stack=[root]\n    while stack:\n        n=stack.pop()\n        if n in seen: continue\n        seen.add(n); stack.extend(GRAPH.get(n,[]))\n    seen.discard(root); return sorted(seen)\ndeps=closure(\"app\")\nprint(\"dependencies:\",deps)\nprint(\"pins:\",{d:PINS.get(d,\"unpinned!\") for d in deps})\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Retrieval-by-Dependency";
  return {id:id,t:title,title:title,description:"Retrieval-by-dependency answers 'what do I need to run this?': given a program, a result, or a project, it walks the dependency graph and returns every resource required \u2014 libraries, data files, models, credentials, hardware, documentation. It turns reproducibility from archaeology into a query. The core is a dependency graph built from manifests, imports, and provenance records, with version pinn",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
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
var gen={version:"jahdb-archive-toolkit-retrieval-by-dependency-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-retrieval-by-dependency",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();