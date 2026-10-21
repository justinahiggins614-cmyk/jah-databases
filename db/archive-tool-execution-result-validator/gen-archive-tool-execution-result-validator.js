(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["output-capture", "requirement-assertion", "tolerance-checking", "regression-comparison", "validation-verdict"];
var PREFIX='JAH-AT89-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Output capture with isolation", "k": "method", "d": "The program under test runs in a controlled harness that captures stdout, stderr, return code, and runtime. Capture is isolated so a crashing program cannot take the validator down with it. The captured bundle is the evidence the validator judges.", "demo": "import subprocess, sys\nr = subprocess.run([sys.executable, '-c', 'print(40 + 2)'], capture_output=True, text=True, timeout=10)\nprint('returncode:', r.returncode, '| stdout:', r.stdout.strip())\n"}, {"t": "Requirement assertions as test predicates", "k": "algorithm", "d": "Task requirements are expressed as predicate functions over the captured output: exact match, contains, numeric range, or custom check. Each predicate returns pass or fail with a message. Predicates are small, named, and reusable across validations.", "demo": "def contains_42(out): return ('42' in out, 'output contains 42')\ndef fast_enough(ms): return (ms < 1000, f'ran in {ms}ms')\nprint(contains_42('the answer is 42'))\nprint(fast_enough(120))\n"}, {"t": "Tolerance checking for numeric outputs", "k": "method", "d": "Numeric outputs are compared with an explicit tolerance, absolute or relative, declared per requirement. Tolerance checking avoids false failures from floating-point representation, where 0.1 + 0.2 is not exactly 0.3. The tolerance used is recorded with the verdict.", "demo": "got, want, tol = 0.1 + 0.2, 0.3, 1e-9\nprint('within tolerance:', abs(got - want) <= tol, f'(tol={tol})')\n"}, {"t": "Regression comparison against golden outputs", "k": "algorithm", "d": "Current output is diffed against a golden output recorded from a known-good run. Diffs are reported line by line so the change is visible, not just 'different'. Golden outputs are versioned with the program so the comparison stays meaningful as the program evolves.", "demo": "import difflib\ngolden = ['hits: 42\\n', 'time: 0.4s\\n']\ncurrent = ['hits: 42\\n', 'time: 0.6s\\n']\ndiff = list(difflib.unified_diff(golden, current, lineterm=''))\nprint('regression diff lines:', len(diff), '| sample:', diff[4].strip() if len(diff) > 4 else 'none')\n"}, {"t": "Validation verdict with evidence", "k": "procedure", "d": "The validator emits a verdict of pass or fail with every predicate result attached as evidence. A failing verdict names the exact requirement violated and shows the offending output. The verdict bundle is stored with the program version so validation history is complete.", "demo": "verdict = {'program': 'demo-1.0', 'predicates': {'contains_42': True, 'fast_enough': True}, 'verdict': 'PASS'}\nprint('validation verdict:', verdict['verdict'])\n"}];
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
var gen={version:'jahdb-archive-tool-execution-result-validator-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-execution-result-validator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
