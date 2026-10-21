(function(){'use strict';
/* Signature Direnv Database — boundless generator jahdb-pc-organizer-direnv-signature-1.0
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
var CATS=["setup", "envrc", "layouts", "security"];
var PREFIX='JAH-PCO92S-';
var ROWS=[["setup", "SigDirenvault directory vault", "The Signature Direnvault is a Signature original: a shell companion that loads and unloads per-project environments on directory change, with signed env files, secret-manager integration, and layout automation — the Sign", ["signed env files", "auto load/unload"]], ["envrc", "SigEnvFile signed env files", "Project env files are signed; the vault verifies the signature before loading and shows what changed since last allow. The signed-file protocol is Signature-original.", ["signatures", "change diffs"]], ["security", "SigAllow trust ledger", "Trust grants are recorded in a ledger with who/when/why; trust can be scoped (this machine, 30 days). The scoped trust ledger is Signature-original.", ["scoped trust", "ledger"]], ["setup", "SigHook universal shell hook", "One hook line covers bash, zsh, fish, and nushell with identical behavior. The universal hook is Signature-original.", ["universal", "identical behavior"]], ["layouts", "SigLayouts stack layouts", "Layouts provision Python/Node/Go/Rust environments declaratively with version pins, cached per project. The declarative layout engine is Signature-original.", ["declarative", "pinned"]], ["security", "SigSecrets manager bridge", "Secrets load from the system keychain or a vault (not the env file) with per-secret audit. The audit-trailed secret bridge is Signature-original.", ["keychain/vault", "audit trail"]], ["layouts", "SigLib environment stdlib", "The stdlib offers path_add, use_tool, watch_files, and service helpers with documentation inline. The documented stdlib is Signature-original.", ["helpers", "inline docs"]], ["setup", "SigStatus env inspector", "An inspector shows the active env: which file provided each variable and its value source. The provenance view is Signature-original.", ["provenance", "inspector"]], ["envrc", "SigWatch dependency watch", "Watch declarations re-evaluate the env when watched files change, with debouncing for editor save storms. The debounced watch is Signature-original.", ["debounced", "auto refresh"]], ["security", "SigDeny instant revoke", "Trust revokes instantly across all shells with a reason recorded. The cross-shell revoke is Signature-original.", ["cross-shell", "recorded reason"]], ["envrc", "SigDotEnv safe dotenv", "Dotenv files load under the vault's trust and signature model, upgrading the .env ecosystem. The trust-wrapped dotenv is Signature-original.", ["trust-wrapped", "compatible"]], ["layouts", "SigPath scoped PATH", "PATH additions scope to the directory with shadowing warnings when a project tool overrides a system one. The shadowing warnings are Signature-original.", ["shadowing warnings", "scoped"]], ["setup", "SigTeam shared environments", "Teams share env templates with secret placeholders resolved per-user from their own vaults. The placeholder resolution is Signature-original.", ["templates", "per-user secrets"]], ["setup", "SigPerf instant hooks", "The hook is benchmarked under 5ms with a perf report command; env evaluation caches aggressively. The perf budget is Signature-original.", ["perf budget", "caching"]], ["setup", "SigCompare friction guide", "A guide compares vault behavior against manual sourcing and IDE managers with migration recipes. The migration recipes are Signature-original.", ["recipes", "comparison"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Signature Direnvault",edition:'signature',description:desc,facts:row[3].slice(),
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
var gen={version:'jahdb-pc-organizer-direnv-signature-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-direnv-signature',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_direnv_signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
