(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["search", "ml", "empirical", "compiler", "runtime"];
var PREFIX='JAH-CFAT-';
var GENVER='jahdb-compiler-flag-auto-tuning-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tuner", "searches", "method", "result"];
var DEMO_TPL="// $TITLE - autotuner search demo (hill climbing)\nfunction perf(flags) { var s = 0; for (var i = 0; i < flags.length; i++) s += flags.charCodeAt(i) * (i + 1); return 100000 - (s % 5000); }\nvar flags = [\"-O2\", \"-O3 -funroll-loops\", \"-Os\", \"-O3 -march=native\"];\nvar best = flags.map(function(f) { return { f: f, score: perf(f) }; }).sort(function(a, b) { return b.score - a.score; })[0];\nconsole.log(\"Tuner: $TUNER | Method: $METHOD\");\nflags.forEach(function(f) { console.log(\"  \" + f + \" -> \" + perf(f)); });\nconsole.log(\"Best: \" + best.f + \" (\" + best.score + \") -> TUNED\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["search", "OpenTuner", "An extensible framework with ensembles of search techniques for program autotuning. Searches flag spaces via ensemble search. Result: best config.", {"tuner": "OpenTuner", "searches": "flag spaces", "method": "ensemble search", "result": "best config"}], ["ml", "Collective Mind / cTuning", "Crowdsourced optimization sharing tuning knowledge across machines. Searches flags + params via crowdsourced ML. Result: shared models.", {"tuner": "cTuning", "searches": "flags + params", "method": "crowdsourced ML", "result": "shared models"}], ["ml", "Milepost GCC", "Machine-learning driven GCC optimization using program features. Searches optimization passes via ML prediction. Result: per-program flags.", {"tuner": "Milepost GCC", "searches": "optimization passes", "method": "ML prediction", "result": "per-program flags"}], ["empirical", "ATLAS", "Automatically Tuned Linear Algebra Software empirically finding the fastest kernels. Searches kernel params via empirical install-time. Result: tuned BLAS.", {"tuner": "ATLAS", "searches": "kernel params", "method": "empirical install-time", "result": "tuned BLAS"}], ["empirical", "FFTW wisdom", "FFTW plans FFTs empirically, saving wisdom for reuse. Searches FFT plans via empirical planning. Result: wisdom file.", {"tuner": "FFTW", "searches": "FFT plans", "method": "empirical planning", "result": "wisdom file"}], ["ml", "TVM Ansor", "ML-based tensor program autotuning for deep learning compilers. Searches schedules via evolutionary + learned cost. Result: fast kernels.", {"tuner": "Ansor", "searches": "schedules", "method": "evolutionary + learned cost", "result": "fast kernels"}], ["ml", "Halide autoscheduler", "Mullapudi’s autoscheduler finding Halide schedules automatically. Searches schedules via beam search + ML. Result: fast pipelines.", {"tuner": "Halide", "searches": "schedules", "method": "beam search + ML", "result": "fast pipelines"}], ["ml", "CompilerGym", "OpenAI/Facebook’s RL environments for compiler optimization. Searches pass sequences via reinforcement learning. Result: learned policies.", {"tuner": "CompilerGym", "searches": "pass sequences", "method": "reinforcement learning", "result": "learned policies"}], ["compiler", "Clang autotune", "-mllvm autotuning hooks exploring backend parameters. Searches backend params via parameter search. Result: tuned codegen.", {"tuner": "Clang", "searches": "backend params", "method": "parameter search", "result": "tuned codegen"}], ["compiler", "GCC -fauto-profile", "AutoFDO-driven feedback without instrumentation builds. Searches profile use via sample profiles. Result: guided opts.", {"tuner": "GCC AutoFDO", "searches": "profile use", "method": "sample profiles", "result": "guided opts"}], ["search", "Bayesian flag search", "Gaussian-process optimization over flag spaces with few evaluations. Searches flag combos via GP surrogate. Result: near-optimal.", {"tuner": "Bayesian opt", "searches": "flag combos", "method": "GP surrogate", "result": "near-optimal"}], ["ml", "MetaSchedule", "TVM’s modular autotuning framework replacing AutoTVM. Searches tensor schedules via modular search. Result: fast kernels.", {"tuner": "MetaSchedule", "searches": "tensor schedules", "method": "modular search", "result": "fast kernels"}], ["empirical", "PPoly", "Empirical tuning for polyhedral compilation tile sizes. Searches tile sizes via empirical. Result: tuned tiles.", {"tuner": "PPoly", "searches": "tile sizes", "method": "empirical", "result": "tuned tiles"}], ["search", "ATF (autotuning framework)", "A general C++ autotuning framework with many search strategies. Searches parameter spaces via pluggable search. Result: best params.", {"tuner": "ATF", "searches": "parameter spaces", "method": "pluggable search", "result": "best params"}], ["empirical", "Kernel Tuner", "Python-embedded GPU kernel autotuning across devices. Searches GPU params via empirical. Result: per-GPU kernels.", {"tuner": "Kernel Tuner", "searches": "GPU params", "method": "empirical", "result": "per-GPU kernels"}]];
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
  if(!new RegExp('^'+'JAH\\-CFAT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compiler-flag-auto-tuning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
