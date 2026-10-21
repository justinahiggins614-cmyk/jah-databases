(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["os", "mobile", "tooling", "cloud", "embedded"];
var PREFIX='JAH-AUTOMA3-';
var GENVER='jahdb-automated-crash-dumps-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "captures", "format", "pipeline"];
var DEMO_TPL="// $TITLE - crash dump capture demo\nfunction risky(n) { if (n < 0) throw new Error(\"negative input: \" + n); return Math.sqrt(n); }\nvar dump = null;\ntry { risky(-4); } catch (e) {\n  dump = { system: \"$SYSTEM\", error: e.message, stack: e.stack.split(\"\\n\").slice(0, 3).join(\" <- \"), time: new Date().toISOString() };\n}\nconsole.log(\"System: \" + dump.system + \" | Captures: $CAPTURES\");\nconsole.log(\"Dump: \" + JSON.stringify(dump));\nconsole.log(\"Pipeline: $PIPELINE -> filed\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["os", "Windows Error Reporting", "WER captures user-mode dumps and can upload them to Microsoft’s Watson pipeline. It captures user/kernel crashes as minidump (.dmp); the pipeline is Watson buckets.", {"system": "WER", "captures": "user/kernel crashes", "format": "minidump (.dmp)", "pipeline": "Watson buckets"}], ["os", "Linux core dumps", "The kernel writes ELF core files on fatal signals; coredumpctl manages them under systemd. It captures fatal signals as ELF core / lz4 journal; the pipeline is coredumpctl + gdb.", {"system": "systemd-coredump", "captures": "fatal signals", "format": "ELF core / lz4 journal", "pipeline": "coredumpctl + gdb"}], ["os", "macOS crash reports", "CrashReporter writes .ips files with thread states to ~/Library/Logs/DiagnosticReports. It captures app/hang crashes as .ips JSON; the pipeline is Xcode Organizer.", {"system": "CrashReporter", "captures": "app/hang crashes", "format": ".ips JSON", "pipeline": "Xcode Organizer"}], ["mobile", "Android tombstones", "debuggerd writes tombstones with registers and backtraces to /data/tombstones. It captures native crashes as tombstone text; the pipeline is Play Console / Firebase.", {"system": "debuggerd", "captures": "native crashes", "format": "tombstone text", "pipeline": "Play Console / Firebase"}], ["tooling", "Breakpad", "Google’s cross-platform crash library generating minidumps with a symbol server pipeline. It captures C++ crashes as minidump; the pipeline is Socorro/symbol server.", {"system": "Breakpad", "captures": "C++ crashes", "format": "minidump", "pipeline": "Socorro/symbol server"}], ["tooling", "Crashpad", "Breakpad’s successor with out-of-process dump generation used by Chrome and Electron. It captures crashes + hangs as minidump; the pipeline is Crashpad server.", {"system": "Crashpad", "captures": "crashes + hangs", "format": "minidump", "pipeline": "Crashpad server"}], ["cloud", "Sentry", "Sentry’s SDKs capture exceptions with breadcrumbs, releases, and suspect-commit mapping. It captures exceptions + native as Sentry envelope; the pipeline is Sentry issues.", {"system": "Sentry", "captures": "exceptions + native", "format": "Sentry envelope", "pipeline": "Sentry issues"}], ["os", "Apport", "Ubuntu’s crash interceptor filing Launchpad bugs with retraced stack traces. It captures app crashes as .crash files; the pipeline is Launchpad + retracer.", {"system": "Apport", "captures": "app crashes", "format": ".crash files", "pipeline": "Launchpad + retracer"}], ["os", "kdump", "kdump boots a capture kernel on panic to save vmcore for post-mortem analysis. It captures kernel panics as vmcore (ELF); the pipeline is crash utility.", {"system": "kdump", "captures": "kernel panics", "format": "vmcore (ELF)", "pipeline": "crash utility"}], ["os", "Dr. Watson", "The classic Windows 9x/XP debugger logging crashes before WER replaced it. It captures app faults as drwtsn32.log; the pipeline is local log review.", {"system": "Dr. Watson", "captures": "app faults", "format": "drwtsn32.log", "pipeline": "local log review"}], ["tooling", "Minidump format", "Microsoft’s compact dump standard: threads, stacks, and modules without full memory. It captures portable snapshots as .dmp streams; the pipeline is any minidump reader.", {"system": "minidump", "captures": "portable snapshots", "format": ".dmp streams", "pipeline": "any minidump reader"}], ["mobile", "Firebase Crashlytics", "Real-time crash reporting for mobile with velocity alerts and custom keys. It captures mobile crashes as Crashlytics payload; the pipeline is Firebase console.", {"system": "Crashlytics", "captures": "mobile crashes", "format": "Crashlytics payload", "pipeline": "Firebase console"}], ["cloud", "Backtrace.io", "Coroner-style dump analysis with classifiers grouping crashes by root cause. It captures native/web crashes as minidump + objects; the pipeline is Backtrace coroner.", {"system": "Backtrace", "captures": "native/web crashes", "format": "minidump + objects", "pipeline": "Backtrace coroner"}], ["os", "ABRT", "Fedora’s Automatic Bug Reporting Tool catching C, Python, and Java crashes alike. It captures multi-language as problem dirs; the pipeline is Bugzilla filing.", {"system": "ABRT", "captures": "multi-language", "format": "problem dirs", "pipeline": "Bugzilla filing"}], ["embedded", "Nintendo? no — QNX slog2", "QNX’s slog2 captures structured crash data on real-time embedded targets. It captures RTOS faults as slog2 buffers; the pipeline is Momentics IDE.", {"system": "QNX slog2", "captures": "RTOS faults", "format": "slog2 buffers", "pipeline": "Momentics IDE"}]];
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
  if(!new RegExp('^'+'JAH\\-AUTOMA3\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-crash-dumps',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
