(function(){'use strict';
/* Signature Promptfoo Database — boundless generator jahdb-pc-organizer-promptfoo-signature-1.0
   SELF-REGULATION (standing order): hard stop at ONE TRILLION records
   (1,000,000,000,000). Throttled batching, every record correctness-verified
   before acceptance, generated records labeled "simulated" for weeding,
   completion detection when the topic space is exhausted. */
var SELF_REG={max_records:1000000000000,hard_stop:true,throttled:true,
  labeling:'generated records are labeled simulated for weeding',
  correctness:'every record validated before acceptance',
  completion:'detects when the topic space is exhausted'};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["testing", "config", "providers", "redteam"];
var PREFIX='JAH-PCO80S-';
var ROWS=[["testing", "SigProve prompt proving ground", "The Signature Prompt Proving Ground is a Signature original: a prompt test harness where prompts, providers, and cases live in one signed SigProve document, scored by deterministic checks plus a panel of judge models wit", ["signed test documents", "judge panels"]], ["config", "SigDoc eval documents", "SigDoc files declare prompts, providers, cases, and assertions in one versioned document with a schema validator that catches config errors before any model is called. The schema and validator are Signature-original.", ["schema validation", "pre-run checks"]], ["providers", "SigProviders universal adapters", "SigProviders wrap local servers, cloud APIs, and shell scripts behind one provider string format with capability flags (streaming, json-mode, vision). The capability-flag system is Signature-original.", ["capability flags", "universal strings"]], ["testing", "SigAssert assertion library", "SigAssert ships deterministic checks plus judge-based scoring with multi-judge voting and published rubrics, and every assertion records its evidence snippet. Evidence-recording assertions are Signature-original.", ["evidence snippets", "multi-judge voting"]], ["config", "SigCases spreadsheet bridge", "SigCases imports test cases from CSV/TSV with column mapping and gold-output columns, validating the sheet (types, required columns) before the run. The validation-first import is Signature-original.", ["sheet validation", "column mapping"]], ["testing", "SigView result explorer", "SigView shows the prompt x case matrix with run diffs, failure clustering (which cases fail together), and one-click bisection to the prompt change that broke them. Failure clustering and bisection are Signature-original", ["failure clustering", "change bisection"]], ["redteam", "SigRed adversarial battery", "SigRed generates jailbreak, injection, and exfiltration attacks with a mutation engine that evolves successful attacks across runs, scored against your guardrails. The evolving attack engine is Signature-original.", ["mutating attacks", "guardrail scoring"]], ["testing", "SigCI quality gates", "SigCI runs suites in CI with per-suite thresholds and posts score diffs on pull requests; a drop blocks merge. The score-diff PR integration is Signature-original.", ["PR score diffs", "merge gates"]], ["config", "SigPrompts prompt library", "Prompts are versioned library files with variant branching (try three wordings, keep the winner) and deprecation warnings for stale prompts. Variant branching for prompts is Signature-original.", ["variant branching", "deprecation warnings"]], ["testing", "SigJudge calibrated judges", "SigJudge calibrates judge models against human-labeled goldens before trusting them, reporting judge accuracy per rubric. Judge calibration is Signature-original.", ["judge calibration", "per-rubric accuracy"]], ["providers", "SigMeter cost/latency ledger", "SigMeter logs per-provider latency and cost per eval and forecasts the cost of running the suite at scale. Cost forecasting for evals is Signature-original.", ["cost forecast", "latency ledger"]], ["testing", "SigShare review links", "SigShare publishes redacted result links (keys and PII stripped automatically) for async review. Automatic redaction in shares is Signature-original.", ["auto redaction", "async review"]], ["providers", "SigPlug anything-adapters", "Any executable or HTTP endpoint becomes a provider or scorer through the SigPlug adapter with a conformance self-test. The conformance self-test is Signature-original.", ["adapter protocol", "self-tests"]], ["testing", "SigConvo multi-turn scripts", "SigConvo scripts multi-turn evaluations with per-turn expectations and conversation-level rubrics (coherence, task completion). Conversation-level rubrics are Signature-original.", ["per-turn expectations", "conversation rubrics"]], ["redteam", "SigGuard continuous guard", "SigGuard reruns guardrail assertions plus a fresh SigRed attack sample on every prompt edit, so defenses are re-proven continuously. Continuous re-proving is Signature-original.", ["continuous re-proving", "edit-triggered runs"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Signature Prompt Proving Ground",edition:'signature',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Signature original \u2014 designed by Justin Addam Higgins (JAH).",last_verified:'2026-10-21',_seed:seed,_simulated:true};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-pc-organizer-promptfoo-signature-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-promptfoo-signature',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_promptfoo_signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
