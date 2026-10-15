(function(){'use strict';
/* JAH The Developer Tools Database generator — jahdb-developer-tools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DVT-";
var FIELDS=["build"];
var TOPICS={
 "build": [
  "Toolchains \u2014 build",
  "Compilers \u2014 build",
  "Decompilers \u2014 build",
  "Cross-Compilers \u2014 build",
  "JIT Compilers \u2014 build",
  "AOT Compilers \u2014 build",
  "Interpreters \u2014 build",
  "Transpilers \u2014 build",
  "Assemblers \u2014 build",
  "Disassemblers \u2014 build",
  "Linkers \u2014 build",
  "Loaders \u2014 build",
  "Debuggers \u2014 build",
  "Source-Level Debuggers \u2014 build",
  "Profilers \u2014 build",
  "CPU Profilers \u2014 build",
  "Memory Profilers \u2014 build",
  "Linters \u2014 build",
  "Code Formatters \u2014 build",
  "Static Analyzers \u2014 build",
  "Code Generators \u2014 build",
  "Bundlers \u2014 build",
  "Minifiers \u2014 build",
  "Obfuscators \u2014 build",
  "Package Managers \u2014 build",
  "Build Systems \u2014 build",
  "Task Runners \u2014 build",
  "CI/CD Runners \u2014 build",
  "Schema Generators \u2014 build",
  "API Generators \u2014 build",
  "Interface Generators \u2014 build",
  "Program Loaders \u2014 build",
  "Kernel Debuggers \u2014 build",
  "Network Profilers \u2014 build",
  "Dynamic Analyzers \u2014 build",
  "Module Bundlers \u2014 build",
  "Static Linkers \u2014 build",
  "Dynamic Linkers \u2014 build",
  "Hardware Debuggers \u2014 build",
  "Orchestrators \u2014 build",
  "Dependency Resolvers \u2014 build",
  "Code Optimizers \u2014 build",
  "Benchmark Harnesses \u2014 build",
  "Stress Test Tools \u2014 build",
  "Test Frameworks \u2014 build",
  "Mock Servers \u2014 build",
  "Fuzzers \u2014 build",
  "Log Analyzers \u2014 build",
  "API Documentation Generators \u2014 build",
  "Internationalization Tools \u2014 build",
  "Container Builders \u2014 build",
  "Cross-Platform Build Tools \u2014 build",
  "Release Managers \u2014 build",
  "Static Site Generators \u2014 build",
  "Refactoring Tools \u2014 build",
  "Code Search Tools \u2014 build",
  "Dependency Scanners \u2014 build",
  "SBOM Generators \u2014 build",
  "Secret Scanners \u2014 build",
  "Documentation Linters \u2014 build"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Developer Tools — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — developer tool record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A developer tool record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-developer-tools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('developer-tools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
