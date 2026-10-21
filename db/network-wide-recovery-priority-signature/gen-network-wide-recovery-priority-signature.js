(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["tiers", "sequencing", "validation", "communication", "review"];
var PREFIX='JAH-NWR-S-';
var USE="Used by incident commanders to bring systems back in dependency order.";
var FLD=[["tier", "Tier"], ["rto", "RTO"], ["includes", "Includes"]];
var DEMO="# {title} - tier order check (python3)\ntiers={d1}\nfirst={d2}\nlast={d3}\nok = tiers == sorted(tiers) and tiers[0] == first and tiers[-1] == last\nprint(\"recovery order:\", tiers)\nprint(\"ORDER VALID\" if ok else \"REORDER TIERS\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["tiers", "Tier 0 - Control Plane", "Recovers orchestration first; nothing else can be managed without it.", "Tier 0 - Control Plane", "15 min", "schedulers, APIs", "[0, 1, 2, 3]", "0", "3"], ["sequencing", "Tier 1 - Identity", "Restores authentication so services can verify each other.", "Tier 1 - Identity", "20 min", "IdP, PKI", "[0, 1, 2]", "0", "2"], ["validation", "Tier 2 - Data Stores", "Brings back databases with integrity checks before writers return.", "Tier 2 - Data Stores", "45 min", "primaries, replicas", "[0, 1, 2, 3, 4]", "0", "4"], ["communication", "Tier 3 - Ingest Pipelines", "Restarts data intake so fresh data flows once stores are up.", "Tier 3 - Ingest Pipelines", "60 min", "queues, connectors", "[1, 2, 3]", "1", "3"], ["review", "Tier 4 - Compute Fleets", "Scales compute back to serve the restored data and traffic.", "Tier 4 - Compute Fleets", "75 min", "workers, GPUs", "[2, 3, 4]", "2", "4"], ["tiers", "Tier 5 - Caches", "Warms caches after backends are healthy to avoid stampedes.", "Tier 5 - Caches", "90 min", "CDN, Redis", "[3, 4, 5]", "3", "5"], ["sequencing", "Tier 6 - Analytics", "Restores batch analytics once operational systems are stable.", "Tier 6 - Analytics", "120 min", "warehouses, jobs", "[4, 5, 6]", "4", "6"], ["validation", "Tier 7 - Batch Jobs", "Resumes non-urgent batch work last.", "Tier 7 - Batch Jobs", "180 min", "cron, ETL", "[5, 6, 7]", "5", "7"], ["communication", "Tier 8 - Dev Tooling", "Brings back CI/CD and dev environments after production is safe.", "Tier 8 - Dev Tooling", "240 min", "CI, registries", "[6, 7, 8]", "6", "8"], ["review", "Tier 9 - Archives", "Restores cold archives and backups last.", "Tier 9 - Archives", "24 h", "cold storage", "[7, 8, 9]", "7", "9"], ["tiers", "Dependency-ordered Startup", "Starts services strictly after their dependencies report healthy.", "Dependency-ordered Startup", "per tier", "health gates", "[0, 1, 2, 3, 4, 5]", "0", "5"], ["sequencing", "Blast-radius Limiting", "Restores one availability zone at a time to contain regressions.", "Blast-radius Limiting", "per zone", "zone batches", "[0, 1, 2]", "0", "2"], ["validation", "Canary Restore", "Restores a slice of traffic first and validates before full restore.", "Canary Restore", "per service", "traffic %", "[0, 1]", "0", "1"], ["communication", "Traffic Ramp", "Ramps traffic gradually with automatic rollback on error budget burn.", "Traffic Ramp", "per edge", "ramp plan", "[0, 1, 2, 3]", "0", "3"], ["review", "Health-gate Promotion", "Promotes each tier only after health checks pass.", "Health-gate Promotion", "per tier", "checks", "[0, 1, 2, 3, 4]", "0", "4"], ["tiers", "Rollback Priority", "Defines which restores roll back first if the recovery itself fails.", "Rollback Priority", "per tier", "rollback order", "[4, 3, 2, 1, 0]", "4", "0"], ["sequencing", "Communication Tree", "Specifies who tells whom what during the recovery.", "Communication Tree", "org", "tree", "[0, 1, 2]", "0", "2"], ["validation", "War-room Roles", "Assigns incident commander, comms, and scribe before the crisis.", "War-room Roles", "org", "roles", "[0, 1, 2, 3]", "0", "3"], ["communication", "Status Page Updates", "Publishes recovery progress publicly on a fixed cadence.", "Status Page Updates", "comms", "updates", "[0, 1]", "0", "1"], ["review", "Post-incident Review", "Schedules blameless review with action items after service is restored.", "Post-incident Review", "learning", "review", "[0, 1, 2]", "0", "2"]];
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
var gen={version:'jahdb-network-wide-recovery-priority-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-wide-recovery-priority-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
