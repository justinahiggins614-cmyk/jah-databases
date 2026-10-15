(function(){'use strict';
/* JAH The Binary Tools Database generator — jahdb-binary-tools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIN-";
var FIELDS=["binary"];
var TOPICS={
 "binary": [
  "Hex Editors \u2014 binary",
  "Binary Patchers \u2014 binary",
  "Disassemblers \u2014 binary",
  "Interactive Disassemblers \u2014 binary",
  "Decompilers \u2014 binary",
  "IR Lifters \u2014 binary",
  "Control-Flow Graphs \u2014 binary",
  "Call Graph Builders \u2014 binary",
  "Binary Diffing Tools \u2014 binary",
  "Unpackers \u2014 binary",
  "Decryptors \u2014 binary",
  "PE Parsers \u2014 binary",
  "ELF Parsers \u2014 binary",
  "Mach-O Parsers \u2014 binary",
  "DWARF Parsers \u2014 binary",
  "Symbol Demanglers \u2014 binary",
  "String Extractors \u2014 binary",
  "Entropy Analyzers \u2014 binary",
  "Packer Detectors \u2014 binary",
  "Import Rebuilders \u2014 binary",
  "Relocation Fixers \u2014 binary",
  "Memory Dump Analyzers \u2014 binary",
  "Crash Dump Analyzers \u2014 binary",
  "Core Analyzers \u2014 binary",
  "ROP Finders \u2014 binary",
  "Shellcode Analyzers \u2014 binary",
  "Shellcode Packers \u2014 binary",
  "Exploit Mitigation Checkers \u2014 binary",
  "Fuzzing Harnesses \u2014 binary",
  "Coverage Tracers \u2014 binary",
  "Taint Trackers \u2014 binary",
  "Symbolic Executors \u2014 binary",
  "Concolic Testers \u2014 binary",
  "Emulation Sandboxes \u2014 binary",
  "API Monitors \u2014 binary",
  "Registry Monitors \u2014 binary",
  "File Monitors \u2014 binary",
  "Network Monitors \u2014 binary",
  "Behavior Blockers \u2014 binary",
  "YARA Scanners \u2014 binary",
  "Signature Generators \u2014 binary",
  "Threat Intel Matchers \u2014 binary",
  "Sandbox Reporters \u2014 binary",
  "Malware Config Extractors \u2014 binary",
  "Document Analyzers \u2014 binary",
  "PDF Analyzers \u2014 binary",
  "Script Deobfuscators \u2014 binary",
  "PowerShell Analyzers \u2014 binary",
  "Firmware Extractors \u2014 binary",
  "Bootkit Detectors \u2014 binary",
  "Rootkit Scanners \u2014 binary",
  "Anti-Debug Detectors \u2014 binary",
  "Anti-VM Detectors \u2014 binary",
  "Code Signing Verifiers \u2014 binary",
  "Certificate Inspectors \u2014 binary"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Binary Tools — "+safe+"\n"
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
    name:topic+' — binary tool record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A binary tool record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-binary-tools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('binary-tools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
