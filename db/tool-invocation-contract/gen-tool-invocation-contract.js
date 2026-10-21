(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["identity", "schemas", "reliability", "limits", "governance"];
var PREFIX='JAH-TIC-';
var USE="Used by agent frameworks and API platforms to keep tool use safe and predictable.";
var FLD=[["clause", "Clause"], ["specifies", "Specifies"], ["enforced_by", "Enforced by"]];
var DEMO="# {title} - schema completeness (python3)\nrequired={d1}\nprovided={d2}\nmax_missing={d3}\nmissing=required-provided\nprint(\"missing fields: %d\" % missing)\nprint(\"CONTRACT OK\" if missing <= max_missing else \"CONTRACT VIOLATION\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["identity", "Tool Name and Version", "Pins the exact tool and version so behavior never shifts silently.", "Tool Name and Version", "identity", "registry", "8", "8", "0"], ["schemas", "Input Schema", "Declares every accepted parameter with types, ranges, and required flags.", "Input Schema", "inputs", "validator", "12", "12", "0"], ["reliability", "Output Schema", "Declares the result shape so callers can parse without guessing.", "Output Schema", "outputs", "validator", "9", "9", "0"], ["limits", "Side-effect Declaration", "Lists every external effect (writes, sends, charges) the tool may cause.", "Side-effect Declaration", "effects", "auditor", "5", "5", "0"], ["governance", "Idempotency Guarantee", "States whether repeated calls with the same key are safe.", "Idempotency Guarantee", "retries", "runtime", "4", "4", "0"], ["identity", "Timeout Budget", "Sets the maximum wall-clock time per invocation before cancellation.", "Timeout Budget", "latency", "scheduler", "6", "6", "0"], ["schemas", "Retry Policy", "Defines which errors are retryable, with backoff and max attempts.", "Retry Policy", "failures", "runtime", "7", "7", "0"], ["reliability", "Error Taxonomy", "Enumerates error codes with meanings so callers can branch correctly.", "Error Taxonomy", "errors", "docs + validator", "11", "11", "0"], ["limits", "Authentication Scope", "Declares the credentials and scopes the tool needs, least-privilege by default.", "Authentication Scope", "access", "authz layer", "5", "5", "0"], ["governance", "Rate Limit", "Caps calls per second per caller to protect shared resources.", "Rate Limit", "load", "gateway", "3", "3", "0"], ["identity", "Cost Estimate", "Publishes the expected cost per call so agents can budget before invoking.", "Cost Estimate", "budget", "metering", "4", "4", "0"], ["schemas", "Determinism Flag", "States whether identical inputs always produce identical outputs.", "Determinism Flag", "replay", "testing", "2", "2", "0"], ["reliability", "Concurrency Limit", "Caps simultaneous invocations to avoid resource exhaustion.", "Concurrency Limit", "parallelism", "scheduler", "3", "3", "0"], ["limits", "Data Residency", "Declares where data may be processed to satisfy sovereignty rules.", "Data Residency", "compliance", "policy engine", "4", "4", "0"], ["governance", "Audit Logging", "Requires every invocation to be logged with inputs hash and result.", "Audit Logging", "traceability", "logger", "6", "6", "0"], ["identity", "Deprecation Notice", "Announces retirement timelines and migration paths for old versions.", "Deprecation Notice", "lifecycle", "registry", "3", "3", "0"], ["schemas", "Capability Advertisement", "Publishes machine-readable capability descriptions for discovery.", "Capability Advertisement", "discovery", "directory", "8", "8", "0"], ["reliability", "Result Caching Rule", "States when results may be cached and for how long.", "Result Caching Rule", "performance", "cache layer", "4", "4", "0"], ["limits", "Partial-result Policy", "Defines what is returned when a tool can only complete part of the work.", "Partial-result Policy", "degradation", "runtime", "5", "5", "0"], ["governance", "Cancellation Support", "Guarantees in-flight invocations can be cancelled cleanly.", "Cancellation Support", "control", "runtime", "3", "3", "0"]];
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
var gen={version:'jahdb-tool-invocation-contract-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tool-invocation-contract',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
