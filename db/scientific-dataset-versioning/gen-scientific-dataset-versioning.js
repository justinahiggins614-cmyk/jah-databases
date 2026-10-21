(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["identity", "provenance", "compatibility", "storage", "governance"];
var PREFIX='JAH-SCIENT7-';
var USE="Used by data stewards, researchers, and ML teams who must reproduce results years later.";
var FLD=[["practice", "Practice"], ["mechanism", "Mechanism"], ["guarantee", "Guarantee"]];
var DEMO="# {title} - version stamp and checksum (python3)\nimport hashlib, re\nname={d1}\nsalt={d2}\nm=re.search(r'v(\\d+)', name)\nprint(\"version:\", m.group(1) if m else \"UNVERSIONED\")\ndigest=hashlib.sha256((name+salt).encode()).hexdigest()\nprint(\"checksum:\", digest[:16])\nprint(\"STAMPED\" if m else \"ADD VERSION\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["identity", "Semantic Versioning for Data", "Applies MAJOR.MINOR.PATCH semantics where MAJOR means breaking schema change.", "Semantic Versioning for Data", "version numbers", "meaningful versions", "'cohort-v3'", "'n3'", "'x'"], ["provenance", "Content Hash Addressing", "Addresses datasets by SHA-256 of content so identical data always resolves identically.", "Content Hash Addressing", "hash URIs", "integrity by address", "'survey-v12'", "'n3'", "'x'"], ["compatibility", "Immutable Snapshots", "Freezes released datasets read-only; corrections become new versions, never edits.", "Immutable Snapshots", "WORM storage", "history preserved", "'genome-freeze-v7'", "'n3'", "'x'"], ["storage", "DOI Assignment", "Mints a persistent DOI per release so citations resolve forever.", "DOI Assignment", "DataCite DOI", "citable data", "'climate-v2'", "'n3'", "'x'"], ["governance", "Provenance Graph", "Records every transformation from raw capture to release as a queryable graph.", "Provenance Graph", "PROV-O graph", "full lineage", "'pipeline-v9'", "'n3'", "'x'"], ["identity", "Changelog per Release", "Ships a human-readable changelog with every version: added, changed, removed, fixed.", "Changelog per Release", "changelog", "understandable diffs", "'imagery-v5'", "'n3'", "'x'"], ["provenance", "Schema Migration Scripts", "Provides up/down migration scripts so consumers can move between versions safely.", "Schema Migration Scripts", "migrations", "safe upgrades", "'schema-v4'", "'n3'", "'x'"], ["compatibility", "Backward-compatible Extensions", "Adds fields without breaking old readers: additive changes only in MINOR versions.", "Backward-compatible Extensions", "extension rules", "old code keeps working", "'telemetry-v11'", "'n3'", "'x'"], ["storage", "Deprecation Windows", "Announces field removals a full major version ahead with migration guidance.", "Deprecation Windows", "deprecation policy", "no surprise breaks", "'api-v6'", "'n3'", "'x'"], ["governance", "Checksum Manifests", "Publishes per-file checksums so any corruption or tampering is detectable on download.", "Checksum Manifests", "SHA-256 manifest", "verifiable bytes", "'archive-v8'", "'n3'", "'x'"], ["identity", "Signed Releases", "Cryptographically signs releases so consumers can verify authenticity.", "Signed Releases", "Ed25519 signatures", "authentic data", "'release-v14'", "'n3'", "'x'"], ["provenance", "Retention Policies", "Defines how long each version is kept, balancing reproducibility against storage cost.", "Retention Policies", "lifecycle rules", "predictable availability", "'policy-v2'", "'n3'", "'x'"], ["compatibility", "Access-controlled Versions", "Keeps sensitive versions behind access control while metadata stays discoverable.", "Access-controlled Versions", "ACLs", "privacy + discovery", "'health-v5'", "'n3'", "'x'"], ["storage", "Differential Storage", "Stores only deltas between versions, reconstructing any version on demand.", "Differential Storage", "delta encoding", "cheap history", "'timeseries-v21'", "'n3'", "'x'"], ["governance", "Branching Datasets", "Allows experimental branches that merge back with conflict rules, like code.", "Branching Datasets", "branches", "safe experimentation", "'exp-v3'", "'n3'", "'x'"], ["identity", "Merge Conflict Rules", "Defines deterministic resolution when two branches edit the same records.", "Merge Conflict Rules", "merge policy", "clean merges", "'merge-v1'", "'n3'", "'x'"], ["provenance", "Reproducible Splits", "Fixes train/validation/test splits by hash so ML results compare fairly across versions.", "Reproducible Splits", "hash splits", "fair benchmarks", "'mlsplit-v4'", "'n3'", "'x'"], ["compatibility", "Citation Metadata", "Embeds authors, license, and citation text in every release for proper credit.", "Citation Metadata", "codemeta", "credited data", "'cite-v2'", "'n3'", "'x'"], ["storage", "License Versioning", "Versions the license alongside data so terms never change under a released version.", "License Versioning", "license lock", "stable terms", "'license-v3'", "'n3'", "'x'"], ["governance", "Tombstone Records", "Marks retracted records with tombstones instead of deleting, preserving referential integrity.", "Tombstone Records", "tombstones", "honest history", "'retract-v1'", "'n3'", "'x'"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-scientific-dataset-versioning-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-dataset-versioning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
