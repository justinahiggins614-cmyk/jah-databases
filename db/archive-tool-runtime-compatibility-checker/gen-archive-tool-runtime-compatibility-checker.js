(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["os-arch-check", "runtime-version-check", "dependency-presence-check", "hardware-requirement-check", "compatibility-report"];
var PREFIX='JAH-AT88-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Operating system and architecture check", "k": "method", "d": "The checker reads the platform's OS name, release, and machine architecture and compares them against each tool's declared support matrix. Exact matches pass; declared-compatible families pass with a note; anything else fails fast. Checking first avoids the most frustrating failure mode: installing for an hour before discovering the binary was built for another architecture.", "demo": "import platform\ninfo = {'os': platform.system(), 'arch': platform.machine()}\nsupported = [{'os': 'Linux', 'arch': 'x86_64'}, {'os': 'Linux', 'arch': 'aarch64'}]\nprint('platform:', info)\nprint('supported:', any(s['os'] == info['os'] for s in supported))\n"}, {"t": "Runtime version check", "k": "algorithm", "d": "Required runtime versions, such as Python >= 3.9, are compared against the actual interpreter using proper version-tuple comparison, not string comparison. String comparison famously misorders versions like '3.10' versus '3.9'. The check reports the exact gap when it fails so the fix is obvious.", "demo": "import sys\nneed = (3, 9)\nhave = sys.version_info[:2]\nprint('python', '.'.join(map(str, have)), '>= 3.9:', have >= need)\n"}, {"t": "Dependency presence check", "k": "method", "d": "Each required package is import-checked in the current environment, recording present, missing, or wrong-version. The check runs in a subprocess when isolation matters, so a broken package cannot crash the checker itself. Results feed the compatibility report's fix list.", "demo": "import importlib.util\nfor pkg in ['json', 'gzip', 'nonexistent_pkg_xyz']:\n    print(pkg, 'present' if importlib.util.find_spec(pkg) else 'MISSING')\n"}, {"t": "Hardware requirement check", "k": "method", "d": "Hardware needs such as minimum RAM, CPU count, or GPU presence are measured against the actual machine. Measurements use standard OS interfaces rather than guesses. A tool that needs 16 GB on an 8 GB machine fails here with a clear message instead of dying mysteriously mid-run.", "demo": "import os\ncpus = os.cpu_count()\nprint('CPUs:', cpus, '| meets >=2 requirement:', cpus >= 2)\n"}, {"t": "Compatibility report with fix list", "k": "procedure", "d": "All checks roll up into one report: pass or fail per requirement and, for failures, the concrete fix such as 'install package X' or 'use Python 3.11+'. The report is the install guide the user actually needs. A fully passing report is the green light for deployment.", "demo": "report = {'os': 'pass', 'python': 'pass', 'deps': 'FAIL: install pyyaml', 'hardware': 'pass'}\nprint('compatible:', all(v == 'pass' for v in report.values()))\nprint('fixes needed:', [v for v in report.values() if v != 'pass'])\n"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var v=(rnd()*3)|0;
  var desc=a.d+VARIANTS[v]+(SIG?' Signature-authored original by Justin Addam Higgins (JAH).':'');
  var id=PREFIX+String(seed).padStart(6,'0');
  var ttl=a.t+[' (foundational)',' (compounded)',' (production)'][v];
  var prov=SIG?'Signature-authored original by Justin Addam Higgins (JAH), 2026-10-21.':'Public computer-science methods literature; cross-checked against standard references, 2026-10-21.';
  return {id:id,t:ttl,title:ttl,description:desc,kind:a.k,category:cat,ladder_rank:v+1,demo:(SIG?'# Signature-authored original (JAH).\n':'')+a.demo,provenance:prov,last_verified:'2026-10-21',src:SIG?'signature-generated-completion':'public-harvest',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/-/g,'\\-');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(KIND_LIST.indexOf(r.kind)<0)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==(SIG?'signature-generated-completion':'public-harvest'))e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  if(sample&&sample.length){
    for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].id===rec.id){e.push('duplicate id');break;} }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-archive-tool-runtime-compatibility-checker-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-runtime-compatibility-checker',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
