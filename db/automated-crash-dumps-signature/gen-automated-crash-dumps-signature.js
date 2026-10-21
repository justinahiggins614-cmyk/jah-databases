(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["os", "mobile", "tooling", "cloud", "embedded"];
var PREFIX='JAH-AUTOMA3-S-';
var GENVER='jahdb-automated-crash-dumps-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["system", "captures", "format", "pipeline"];
var DEMO_TPL="// $TITLE - crash dump capture demo\nfunction risky(n) { if (n < 0) throw new Error(\"negative input: \" + n); return Math.sqrt(n); }\nvar dump = null;\ntry { risky(-4); } catch (e) {\n  dump = { system: \"$SYSTEM\", error: e.message, stack: e.stack.split(\"\\n\").slice(0, 3).join(\" <- \"), time: new Date().toISOString() };\n}\nconsole.log(\"System: \" + dump.system + \" | Captures: $CAPTURES\");\nconsole.log(\"Dump: \" + JSON.stringify(dump));\nconsole.log(\"Pipeline: $PIPELINE -> filed\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["os", "SigDump-Native", "Signature-original: native dumps with heap snapshots and allocation-site tags included. It captures all faults as .sigdump; the pipeline is SigCrash analyzer.", {"system": "SigDump", "captures": "all faults", "format": ".sigdump", "pipeline": "SigCrash analyzer"}], ["cloud", "SigDump-Remote", "Signature-original: streaming dump upload with PII scrubbing before it leaves the host. It captures fleet crashes as scrubbed .sigdump; the pipeline is SigCrash cloud.", {"system": "SigDump-Remote", "captures": "fleet crashes", "format": "scrubbed .sigdump", "pipeline": "SigCrash cloud"}], ["tooling", "SigWatch-Hang", "Signature-original: hang detection dumping stacks when event loops stall past budget. It captures hangs as stack samples; the pipeline is auto-filed issues.", {"system": "SigWatch", "captures": "hangs", "format": "stack samples", "pipeline": "auto-filed issues"}], ["tooling", "SigReplay-Crash", "Signature-original: crash-time recording enabling deterministic replay of the failure. It captures pre-crash trace as event log; the pipeline is replay debugger.", {"system": "SigReplay", "captures": "pre-crash trace", "format": "event log", "pipeline": "replay debugger"}], ["cloud", "SigClassify", "Signature-original: ML classifiers grouping crashes by root cause across the fleet. It captures grouped crashes as signatures; the pipeline is dedupe + assign.", {"system": "SigClassify", "captures": "grouped crashes", "format": "signatures", "pipeline": "dedupe + assign"}], ["tooling", "SigSymbol", "Signature-original: symbol server resolving every Sig build’s symbols automatically. It captures symbolication as symbol store; the pipeline is auto-resolve.", {"system": "SigSymbol", "captures": "symbolication", "format": "symbol store", "pipeline": "auto-resolve"}], ["os", "SigCanary", "Signature-original: canary analysis comparing crash rates between releases. It captures release health as rate metrics; the pipeline is release gates.", {"system": "SigCanary", "captures": "release health", "format": "rate metrics", "pipeline": "release gates"}], ["tooling", "SigFuzz-Crash", "Signature-original: fuzzer-found crashes minimized and filed with reproducers. It captures fuzz crashes as minimized repro; the pipeline is auto-file.", {"system": "SigFuzz", "captures": "fuzz crashes", "format": "minimized repro", "pipeline": "auto-file"}], ["mobile", "SigMobile", "Signature-original: mobile crash capture with offline queuing and battery-aware upload. It captures mobile faults as compact dump; the pipeline is SigCrash cloud.", {"system": "SigMobile-Crash", "captures": "mobile faults", "format": "compact dump", "pipeline": "SigCrash cloud"}], ["embedded", "SigEmbed", "Signature-original: embedded fault capture to reserved RAM surviving watchdog resets. It captures firmware faults as RAM log; the pipeline is post-mortem pull.", {"system": "SigEmbed", "captures": "firmware faults", "format": "RAM log", "pipeline": "post-mortem pull"}], ["mobile", "SigAnr", "Signature-original: ANR detection with main-thread samples and strict-mode mapping. It captures ANRs as thread dumps; the pipeline is SigCrash cloud.", {"system": "SigANR", "captures": "ANRs", "format": "thread dumps", "pipeline": "SigCrash cloud"}], ["os", "SigOOM", "Signature-original: OOM forensics capturing allocation leaders before the killer acts. It captures OOM events as alloc leaderboard; the pipeline is capacity alerts.", {"system": "SigOOM", "captures": "OOM events", "format": "alloc leaderboard", "pipeline": "capacity alerts"}], ["os", "SigKernel", "Signature-original: kernel crash capture via the Sig capture kernel with vmcore analysis. It captures kernel panics as sigcore; the pipeline is sigcrash tool.", {"system": "SigKdump", "captures": "kernel panics", "format": "sigcore", "pipeline": "sigcrash tool"}], ["cloud", "SigRegression", "Signature-original: regression detection alerting when old crash signatures return. It captures regressions as signature DB; the pipeline is CI gates.", {"system": "SigRegression", "captures": "regressions", "format": "signature DB", "pipeline": "CI gates"}], ["cloud", "SigCrash-One", "Signature-original: the united crash plane — capture, classify, and fix workflow in one. It captures everything as .sigdump; the pipeline is unified console.", {"system": "SigCrash-One", "captures": "everything", "format": ".sigdump", "pipeline": "unified console"}]];
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
  if(!new RegExp('^'+'JAH\\-AUTOMA3\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-crash-dumps-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
