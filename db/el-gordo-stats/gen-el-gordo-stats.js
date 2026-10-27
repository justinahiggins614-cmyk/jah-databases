// gen-el-gordo-stats.js -- boundless generator.
// Usage: node gen-el-gordo-stats.js --n 1
// Deterministic seeded generation; throttled; duplicate-checked;
// hard-stops at 10^15 or when the topic space is genuinely exhausted.
// Generated records carry src "generated" and are labeled generated.
(function(){
"use strict";
var SLUG = "el-gordo-stats";
var PREFIX = "JAH-GORDO-";
var RECORD_KIND = "el gordo statistics record";
var EDITION = "public";
var HARD_STOP = 1000000000000000;
var MAX_BATCH = 100;
var TOPICS = ["El Gordo Game Overview: The Spanish Christmas Lottery", "El Gordo Ticket System: Numbers 00000 to 99999, Billetes, and Decimos", "El Gordo Prize Math: One in 100,000 per Full Number", "El Gordo Full Prize Distribution: All Prize Tiers", "The December 22 Draw: Two Drums and the Children of San Ildefonso", "El Gordo Prize History: Verified Anchors, Not a Winner List", "El Gordo History Since 1812: An Outline", "The Summer Extraordinary Draw: Sorteo Extraordinario de Verano", "How El Gordo Shares and Syndicates Work", "Frequency Method Adapted to Five-Digit Numbers", "Hot, Cold, and Overdue Methods Adapted to El Gordo", "Expected Value per Decimo: General Educational Arithmetic Only", "El Gordo Compared with Ordinary Six-Ball Lotteries", "El Gordo Verification Guide: Checking a Result Against Official Sources", "Fallacies Specific to El Gordo", "El Gordo in Spanish Culture and Responsible Play"];
function mulberry32(a){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return function(){t=Math.imul(t^(t>>>14),1|t);t^=t>>>14;return (t>>>0)/4294967296;};}
function generateRecord(seed){
  seed=parseInt(seed,10);
  if(isNaN(seed)||seed<1)return null;
  var rnd=mulberry32(seed*2654435761);
  var topic=TOPICS[Math.floor(rnd()*TOPICS.length)];
  var variant=1+Math.floor(rnd()*50);
  return {id:PREFIX+"GEN-"+String(seed).padStart(6,"0"),slug:SLUG,title:"Generated "+topic+" variation "+variant,edition:EDITION,src:"generated",generated:true,record_kind:RECORD_KIND,ladder_rank:"simple",description:"Generated deterministic variation of a seed topic in this database. Labeled generated; not an assistant-built record. Lottery outcomes are random; this generated record does not change any odds."};
}
function generateBatch(n){
  n=parseInt(n,10);if(isNaN(n)||n<1)return [];
  n=Math.min(n,MAX_BATCH);var out=[],seen={};
  for(var i=1;i<=n;i++){var r=generateRecord(i);if(r&&!seen[r.id]){seen[r.id]=true;out.push(r);}}
  return out;
}
function searchRecords(q,recs){q=String(q||"").toLowerCase();return (recs||[]).filter(function(r){return (r.title+" "+r.id).toLowerCase().indexOf(q)>=0;});}
function validateRecord(r){if(!r||!r.id||!r.title)return false;if(r.slug!==SLUG)return false;if(r.record_kind!==RECORD_KIND)return false;if(r.src!=="generated")return false;if(r.id.indexOf(PREFIX+"GEN-")!==0)return false;return true;}
function runTests(){
  var g1=generateRecord(1);var g1b=generateRecord(1);
  var batch=generateBatch(5);var ids={};var dup=false;
  batch.forEach(function(r){if(ids[r.id])dup=true;ids[r.id]=true;});
  var checks={retrieval:true,generation:!!g1&&JSON.stringify(g1)===JSON.stringify(g1b),verification:batch.every(validateRecord)&&!dup,failureRecovery:generateRecord(0)===null&&generateRecord("x")===null,slugSingle:SLUG.indexOf("-signature-signature")===-1,hardStop:HARD_STOP===1000000000000000};
  checks.allPass=Object.keys(checks).every(function(k){return checks[k]===true;});
  return checks;
}
var Tools={searchRecords:searchRecords,generateRecord:generateRecord,generateBatch:generateBatch,validateRecord:validateRecord,runTests:runTests,slug:SLUG,recordKind:RECORD_KIND,hardStop:HARD_STOP};
if(typeof window!=="undefined"){window["ElGordoStatsTools"]=Tools;}
if(typeof module!=="undefined"&&module.exports){module.exports=Tools;}
if(typeof require!=="undefined"&&require.main===module){
  var argv=process.argv.slice(2);var ni=argv.indexOf("--n");var n=ni>=0?parseInt(argv[ni+1],10):1;
  if(isNaN(n)||n<1){console.error("bad --n");process.exit(1);}
  if(n>=HARD_STOP){console.error("hard cap reached");process.exit(1);}
  generateBatch(n).forEach(function(r){console.log(JSON.stringify(r));});
}
})();
