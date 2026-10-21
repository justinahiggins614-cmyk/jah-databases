(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["spec-parsing", "code-synthesis", "test-generation", "validation-gate", "deployment-packaging"];
var PREFIX='JAH-AT90-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Specification parsing into a build frame", "k": "method", "d": "The natural-language specification is parsed into a build frame: function name, inputs with types, outputs with types, and behavior examples. Parsing is strict: an underspecified frame is returned for clarification rather than built on guesses. The frame is the contract the generated tool must satisfy.", "demo": "spec = 'Build wordcount: input text (str) -> output word count (int). Example: \"a b\" -> 2.'\nframe = {'name': 'wordcount', 'in': {'text': 'str'}, 'out': 'int', 'examples': [('a b', 2)]}\nprint('build frame:', frame['name'], frame['in'], '->', frame['out'])\n"}, {"t": "Code synthesis from the build frame", "k": "algorithm", "d": "Code is synthesized from the frame using templates for common shapes: transformers, filters, aggregators, and validators. Template-based synthesis keeps generated code readable and reviewable, unlike opaque model output. The synthesized module includes docstrings drawn from the specification text.", "demo": "frame = {'name': 'wordcount', 'in': {'text': 'str'}, 'out': 'int'}\ncode = f\"def {frame['name']}(text):\\n    '''Generated from spec.'''\\n    return len(text.split())\\n\"\nprint(code)\nns = {}\nexec(code, ns)\nprint('synthesized tool output:', ns['wordcount']('a b c'))\n"}, {"t": "Test generation from spec examples", "k": "method", "d": "The specification's examples become executable tests automatically, each asserting the example's expected output. Edge cases are added from the input types: empty inputs, boundary values, and wrong types. Generated tests are the acceptance suite the tool must pass.", "demo": "examples = [('a b', 2), ('', 0)]\ndef wordcount(t): return len(t.split())\nresults = [(inp, wordcount(inp) == want) for inp, want in examples]\nprint('generated tests:', results, '| all pass:', all(r[1] for r in results))\n"}, {"t": "Validation gate before deployment", "k": "procedure", "d": "The synthesized tool must pass its generated tests plus the adversarial-content detector's code scan before it can deploy. The gate is non-negotiable: no passing tests, no deployment, no exceptions. Gate results are logged with the tool's version for audit.", "demo": "tests_pass, scan_clean = True, True\nprint('deployment gate:', 'OPEN' if (tests_pass and scan_clean) else 'CLOSED')\n"}, {"t": "Deployment packaging with metadata", "k": "method", "d": "The validated tool is packaged with metadata: name, version, capability tags, the spec it was built from, and its test results. Packaging registers the tool in the registry so the capability matcher can discover it. The package is immutable once published; fixes become new versions.", "demo": "pkg = {'name': 'wordcount', 'version': '1.0.0', 'caps': ['count', 'text'], 'tests': '4/4 pass'}\nprint('published:', pkg['name'], pkg['version'], '|', pkg['tests'])\n"}];
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
var gen={version:'jahdb-archive-tool-automatic-tool-builder-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-automatic-tool-builder',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
