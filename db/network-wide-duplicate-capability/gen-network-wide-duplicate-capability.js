(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["identity", "equivalence", "merging", "governance", "audit"];
var PREFIX='JAH-NWD-';
var USE="Used by network operators to keep capability directories clean and trustworthy.";
var FLD=[["rule", "Rule"], ["identifies", "Identifies"], ["action", "Action"]];
var DEMO="# {title} - dedup ratio (python3)\nraw={d1}\nunique={d2}\nmin_pct={d3}\nsaved=100.0*(raw-unique)/raw\nprint(\"duplicates removed: %d (%.1f%%)\" % (raw-unique, saved))\nprint(\"DIRECTORY CLEAN\" if saved >= min_pct else \"LOW DUPLICATION\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["identity", "Canonical ID Assignment", "Gives every capability one canonical ID; duplicates collapse to it.", "Canonical ID Assignment", "identity", "assign canonical", "1200", "1000", "10.0"], ["equivalence", "Content Fingerprinting", "Hashes the contract to find byte-identical duplicates.", "Content Fingerprinting", "exact dupes", "merge", "1150", "1000", "10.0"], ["merging", "Semantic Equivalence", "Detects capabilities that differ in name but do the same thing.", "Semantic Equivalence", "near dupes", "review merge", "1300", "1000", "15.0"], ["governance", "Version Collapse", "Merges patch-level versions into one entry with a version range.", "Version Collapse", "version sprawl", "collapse", "1500", "1000", "20.0"], ["audit", "Alias Resolution", "Resolves renamed or moved capabilities to their current identity.", "Alias Resolution", "renames", "redirect", "1100", "1000", "5.0"], ["identity", "Namespace Normalization", "Normalizes naming so team-a/tool and teama.tool compare equal.", "Namespace Normalization", "naming drift", "normalize", "1250", "1000", "12.0"], ["equivalence", "Owner Attribution", "Attributes each capability to one owner to resolve conflicting registrations.", "Owner Attribution", "conflicts", "assign owner", "1050", "1000", "3.0"], ["merging", "Provenance Merge", "Merges provenance histories when two entries are found to be one.", "Provenance Merge", "split history", "union history", "1180", "1000", "8.0"], ["governance", "Capability Union", "Merges overlapping capability sets into one superset entry.", "Capability Union", "overlap", "union", "1400", "1000", "20.0"], ["audit", "Shadow Registry Cleanup", "Removes entries from decommissioned shadow registries.", "Shadow Registry Cleanup", "stale", "delete", "1600", "1000", "25.0"], ["identity", "Duplicate Advertisement Suppression", "Suppresses repeated advertisements of the same capability.", "Duplicate Advertisement Suppression", "chatter", "dedupe", "2000", "1000", "30.0"], ["equivalence", "Cross-region Sync", "Syncs directories across regions so dedupe is global.", "Cross-region Sync", "drift", "sync", "1800", "1500", "10.0"], ["merging", "Hash-chained Identity", "Chains identity to code hash so rewrites get new IDs automatically.", "Hash-chained Identity", "rewrites", "re-id", "1120", "1000", "5.0"], ["governance", "Deprecation Redirect", "Points deprecated duplicates at their canonical replacements.", "Deprecation Redirect", "legacy", "redirect", "1350", "1000", "15.0"], ["audit", "Test-instance Exclusion", "Excludes test and staging instances from the production directory.", "Test-instance Exclusion", "pollution", "filter", "1700", "1000", "30.0"], ["identity", "Stale Entry Expiry", "Expires entries whose heartbeats stopped long ago.", "Stale Entry Expiry", "dead", "expire", "1900", "1000", "35.0"], ["equivalence", "Manual Merge Review", "Routes uncertain merges to a human with a side-by-side diff.", "Manual Merge Review", "ambiguity", "review", "1080", "1000", "5.0"], ["merging", "Confidence Scoring", "Scores each merge decision so low-confidence ones can be revisited.", "Confidence Scoring", "risk", "score", "1220", "1000", "10.0"], ["governance", "Audit Log", "Logs every merge and split for later inspection.", "Audit Log", "traceability", "log", "1000", "1000", "0.0"], ["audit", "Rollback Plan", "Keeps pre-merge snapshots so bad merges can be undone.", "Rollback Plan", "safety", "snapshot", "1000", "1000", "0.0"]];
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
var gen={version:'jahdb-network-wide-duplicate-capability-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-wide-duplicate-capability',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
