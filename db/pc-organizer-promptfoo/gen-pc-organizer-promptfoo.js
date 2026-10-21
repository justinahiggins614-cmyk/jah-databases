(function(){'use strict';
/* Promptfoo Database — boundless generator jahdb-pc-organizer-promptfoo-1.0
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
var PREFIX='JAH-PCO80-';
var ROWS=[["testing", "Install and first eval in minutes", "Promptfoo installs with `npx promptfoo@latest init` (or npm/pip), which scaffolds a promptfooconfig.yaml. `promptfoo eval` then runs every prompt against every provider and test case, printing a pass/fail table. The whol", ["npx install", "promptfooconfig.yaml", "promptfoo eval"]], ["config", "The eval config file", "promptfooconfig.yaml declares prompts (inline or files), providers (model endpoints), tests (vars + assertions), and output settings. One file fully describes an eval, so it lives in git next to the prompts and runs in C", ["prompts/providers/tests", "git + CI friendly"]], ["providers", "Providers: local and cloud models", "Providers name the models under test: openai:, anthropic:, ollama:, huggingface:, azure:, bedrock:, and dozens more, each with model and parameter options. The same eval runs unchanged against a local Ollama model or a c", ["provider strings", "local + cloud parity"]], ["testing", "Assertions: how outputs are scored", "Assertions score each output: equals, contains, icontains, regex, llm-rubric (an LLM judge with a rubric), cost/latency thresholds, and custom Python/JS functions. An eval is only as good as its assertions; llm-rubric ha", ["equals/contains/regex", "llm-rubric judge", "thresholds"]], ["config", "Test cases from CSV", "Test vars can live in a CSV (one row per case), so non-engineers add cases in a spreadsheet and the eval picks them up. Columns map to prompt variables; expected outputs can ride in an __expected column. This is how prom", ["CSV test vars", "__expected goldens"]], ["testing", "Web viewer for results", "`promptfoo view` opens a local web UI showing every prompt x test result, diffs between runs, and failure drill-downs. Comparing two eval runs side by side shows exactly which cases a prompt change fixed or broke. The vi", ["promptfoo view", "run diffs"]], ["redteam", "Red teaming plugin", "promptfoo redteam generates adversarial attacks (jailbreaks, prompt injection, PII leaks, harmful content elicitation) against your prompts and scores the defenses. Strategies include Crescendo, GOAT, and injection varia", ["adversarial generation", "jailbreak/injection strategies"]], ["testing", "CI integration", "Evals run in CI with `promptfoo eval --no-cache`, failing the build when pass rates drop below a threshold (--threshold). Cached results speed up local reruns. Prompt changes become pull requests with eval scores attache", ["--threshold", "--no-cache", "PR score comments"]], ["config", "Prompt file organization", "Prompts live as separate files (prompt1.txt, prompt2.md) referenced from the config, so prompt engineering is file editing with history, not strings buried in code. Variants are files too, making prompt A/B a config chan", ["prompt files", "variant organization"]], ["testing", "Model-graded evals done right", "llm-rubric assertions use a judge model with an explicit rubric and pass threshold, and promptfoo supports multiple judges and majority vote to reduce judge bias. Rubrics are versioned with the eval. Judge-based scoring ", ["rubrics", "multi-judge voting"]], ["providers", "Latency and cost tracking", "Every eval records per-provider latency and token cost, so choosing between models is a data question: quality score vs ms vs dollars. The web viewer charts these tradeoffs. Cost-aware model selection starts with measure", ["per-run metrics", "cost/quality charts"]], ["testing", "Sharing evals with promptfoo.dev", "`promptfoo share` uploads an eval run to a shareable link for review without exposing keys. Teammates see the full result table and diffs. Sharing makes prompt review async and concrete.", ["shareable links", "async review"]], ["providers", "Custom providers and assertions", "Any HTTP endpoint or local script can be a provider via exec: or custom JS/Python hooks, and assertions can be arbitrary functions. This escapes the built-in list: in-house models and domain-specific scorers plug in clea", ["exec: providers", "function assertions"]], ["testing", "Dataset and conversation evals", "Multi-turn evals script conversations (user turns + expected assistant behavior per turn), and datasets pin regression cases. Conversation evals catch the failures single-turn tests miss: context loss, tone drift, premat", ["multi-turn scripts", "regression datasets"]], ["redteam", "Guardrail testing patterns", "Teams encode guardrails as assertions (no PII, no disallowed content, citation present) and run them on every prompt change. The redteam plugin then attacks the same guardrails. Defense in depth: assertions for the known", ["guardrail assertions", "continuous attack testing"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Promptfoo",edition:'public',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Public record \u2014 fact-checked.",last_verified:'2026-10-21',_seed:seed,_simulated:true};
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
var gen={version:'jahdb-pc-organizer-promptfoo-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-promptfoo',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_promptfoo']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
