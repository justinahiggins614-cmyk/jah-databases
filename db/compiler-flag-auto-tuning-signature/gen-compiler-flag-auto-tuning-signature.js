(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["search", "ml", "empirical", "compiler", "runtime"];
var PREFIX='JAH-CFAT-S-';
var GENVER='jahdb-compiler-flag-auto-tuning-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tuner", "searches", "method", "result"];
var DEMO_TPL="// $TITLE - autotuner search demo (hill climbing)\nfunction perf(flags) { var s = 0; for (var i = 0; i < flags.length; i++) s += flags.charCodeAt(i) * (i + 1); return 100000 - (s % 5000); }\nvar flags = [\"-O2\", \"-O3 -funroll-loops\", \"-Os\", \"-O3 -march=native\"];\nvar best = flags.map(function(f) { return { f: f, score: perf(f) }; }).sort(function(a, b) { return b.score - a.score; })[0];\nconsole.log(\"Tuner: $TUNER | Method: $METHOD\");\nflags.forEach(function(f) { console.log(\"  \" + f + \" -> \" + perf(f)); });\nconsole.log(\"Best: \" + best.f + \" (\" + best.score + \") -> TUNED\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["search", "SigTune-Auto", "Signature-original: automatic flag tuning in CI for every Sig build. Searches flag spaces via CI search. Result: tuned builds.", {"tuner": "SigTune", "searches": "flag spaces", "method": "CI search", "result": "tuned builds"}], ["ml", "SigTune-ML", "Signature-original: learned cost models predicting the best flags per function. Searches per-function flags via learned cost. Result: fine-tuned.", {"tuner": "SigTune-ML", "searches": "per-function flags", "method": "learned cost", "result": "fine-tuned"}], ["empirical", "SigTune-Fleet", "Signature-original: fleet-wide tuning sharing results across machines. Searches fleet params via shared empirical. Result: fleet-optimal.", {"tuner": "SigTune-Fleet", "searches": "fleet params", "method": "shared empirical", "result": "fleet-optimal"}], ["runtime", "SigTune-Online", "Signature-original: online tuning adjusting flags as workloads shift. Searches runtime flags via bandit search. Result: adaptive.", {"tuner": "SigTune-Online", "searches": "runtime flags", "method": "bandit search", "result": "adaptive"}], ["ml", "SigTune-Energy", "Signature-original: tuning for joules, not just cycles, on mobile. Searches energy flags via joule modeling. Result: efficient.", {"tuner": "SigTune-Energy", "searches": "energy flags", "method": "joule modeling", "result": "efficient"}], ["search", "SigTune-Size", "Signature-original: tuning for minimal binary size on embedded. Searches size flags via size search. Result: tiny.", {"tuner": "SigTune-Size", "searches": "size flags", "method": "size search", "result": "tiny"}], ["empirical", "SigTune-GPU", "Signature-original: GPU kernel autotuning per device in the fleet. Searches kernel params via empirical. Result: per-GPU.", {"tuner": "SigTune-GPU", "searches": "kernel params", "method": "empirical", "result": "per-GPU"}], ["compiler", "SigTune-Verify", "Signature-original: verified tuning proving tuned flags preserve semantics. Searches safe flags via verified search. Result: correct + fast.", {"tuner": "SigTune-Verify", "searches": "safe flags", "method": "verified search", "result": "correct + fast"}], ["search", "SigTune-Multi", "Signature-original: multi-objective tuning balancing speed, size, and energy. Searches pareto frontier via MOO search. Result: trade-off curve.", {"tuner": "SigTune-Multi", "searches": "pareto frontier", "method": "MOO search", "result": "trade-off curve"}], ["empirical", "SigTune-Cache", "Signature-original: tuning results cached and shared fleet-wide. Searches cached spaces via shared cache. Result: instant reuse.", {"tuner": "SigTune-Cache", "searches": "cached spaces", "method": "shared cache", "result": "instant reuse"}], ["compiler", "SigTune-Audit", "Signature-original: audit logs explaining why each flag was chosen. Searches logged via decision log. Result: explainable.", {"tuner": "SigTune-Audit", "searches": "logged", "method": "decision log", "result": "explainable"}], ["runtime", "SigTune-Canary", "Signature-original: canary-validated tuning rolling back regressions. Searches safe rollout via canary gate. Result: safe tuning.", {"tuner": "SigTune-Canary", "searches": "safe rollout", "method": "canary gate", "result": "safe tuning"}], ["runtime", "SigTune-Warm", "Signature-original: warm-start tuning from similar workloads’ results. Searches transfer via transfer learning. Result: fast converge.", {"tuner": "SigTune-Warm", "searches": "transfer", "method": "transfer learning", "result": "fast converge"}], ["search", "SigTune-Budget", "Signature-original: budgeted tuning stopping when gains flatten. Searches bounded via early stopping. Result: efficient search.", {"tuner": "SigTune-Budget", "searches": "bounded", "method": "early stopping", "result": "efficient search"}], ["ml", "SigTune-One", "Signature-original: the united tuner — one brain tuning every Sig compiler. Searches everything via unified. Result: global optimal.", {"tuner": "SigTune-One", "searches": "everything", "method": "unified", "result": "global optimal"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-CFAT\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compiler-flag-auto-tuning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
