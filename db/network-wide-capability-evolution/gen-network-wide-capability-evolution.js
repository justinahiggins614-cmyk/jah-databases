(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["versioning", "compatibility", "rollout", "deprecation", "metrics"];
var PREFIX='JAH-NWC-';
var USE="Used by platform teams shipping capability updates to large consumer bases.";
var FLD=[["practice", "Practice"], ["phase", "Phase"], ["safeguard", "Safeguard"]];
var DEMO="# {title} - deprecation notice check (python3)\nsunset={d1}\nelapsed={d2}\nmin_notice={d3}\nremaining=sunset-elapsed\nprint(\"days until sunset: %d\" % remaining)\nprint(\"NOTICE OK\" if remaining >= min_notice else \"EXTEND NOTICE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["versioning", "Version Numbering", "Uses semantic versioning so consumers read breaking risk from the number.", "Version Numbering", "always", "semver", "365", "30", "90"], ["compatibility", "Backward Compatibility", "Keeps old contracts working while new ones are introduced.", "Backward Compatibility", "design", "compat tests", "365", "60", "90"], ["rollout", "Deprecation Notice", "Announces removals with timelines and migration guides well in advance.", "Deprecation Notice", "deprecate", "notice period", "180", "20", "90"], ["deprecation", "Sunset Timeline", "Publishes the exact date an old version stops working.", "Sunset Timeline", "deprecate", "calendar", "180", "45", "90"], ["metrics", "Migration Guide", "Documents step-by-step moves from old to new capability versions.", "Migration Guide", "migrate", "guide", "120", "15", "60"], ["versioning", "Dual-run Period", "Runs old and new side by side so consumers can compare outputs.", "Dual-run Period", "migrate", "shadow traffic", "90", "10", "45"], ["compatibility", "Feature Flags", "Gates new behavior behind flags for gradual rollout and instant rollback.", "Feature Flags", "rollout", "flags", "60", "5", "30"], ["rollout", "Contract Testing", "Verifies consumers against new versions before they ship.", "Contract Testing", "test", "pacts", "45", "5", "30"], ["deprecation", "Canary Release", "Releases to a small cohort first and watches metrics.", "Canary Release", "rollout", "canary", "30", "3", "14"], ["metrics", "Blue-green Deploy", "Switches traffic between identical environments for zero-downtime updates.", "Blue-green Deploy", "deploy", "two envs", "14", "1", "7"], ["versioning", "Rollback Plan", "Keeps the previous version hot so rollback takes minutes.", "Rollback Plan", "deploy", "hot standby", "14", "2", "7"], ["compatibility", "Changelog Discipline", "Records every change with migration notes in a machine-readable changelog.", "Changelog Discipline", "always", "changelog", "365", "90", "180"], ["rollout", "Telemetry Comparison", "Compares old vs new behavior in production telemetry during rollout.", "Telemetry Comparison", "rollout", "diff dashboards", "60", "7", "30"], ["deprecation", "Consumer Impact Review", "Reviews which consumers use deprecated paths before removal.", "Consumer Impact Review", "deprecate", "usage analysis", "90", "10", "45"], ["metrics", "Breaking-change Policy", "Requires major-version bumps and review board approval for breaks.", "Breaking-change Policy", "govern", "policy", "365", "120", "180"], ["versioning", "LTS Branches", "Maintains long-term-support branches for slow-moving consumers.", "LTS Branches", "support", "LTS", "730", "180", "365"], ["compatibility", "Experimental Track", "Ships risky features on an explicit experimental track with no stability promises.", "Experimental Track", "experiment", "track label", "90", "5", "30"], ["rollout", "Graduation Criteria", "Defines what an experimental capability must prove to become stable.", "Graduation Criteria", "experiment", "criteria", "120", "10", "60"], ["deprecation", "Archive of Retired", "Keeps retired versions readable (not runnable) for archaeology.", "Archive of Retired", "retire", "archive", "3650", "300", "365"], ["metrics", "Evolution Metrics", "Tracks adoption, breakage, and migration speed per version.", "Evolution Metrics", "measure", "dashboards", "365", "30", "90"]];
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
var gen={version:'jahdb-network-wide-capability-evolution-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-wide-capability-evolution',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
