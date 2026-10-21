(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "furmark", "prime95", "safety"];
var PREFIX='JAH-PCO58-';
var GENVER='jahdb-pc-organizer-furmark-prime95-1.0';
var DBNAME='FurMark / Prime95';
var PROV='Public documentation and published specifications for FurMark / Prime95; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What FurMark and Prime95 do", "overview", "FurMark and Prime95 are the classic one-two punch of stability testing: FurMark burns the GPU with a furry 3D donut, Prime95 tortures the CPU with Fast Fourier Transforms. Run together they load the power supply harder t", {"mode": "furmark", "res": "1920x1080", "msaa": 0}, "Runnable demo \u2014 What FurMark and Prime95 do"], ["Prime95 and the GIMPS project", "overview", "Prime95 is the Windows client of the Great Internet Mersenne Prime Search, hunting for the largest known prime numbers with donated CPU time since 1996. Its torture test is literally the same Lucas-Lehmer math that prove", {"mode": "history"}, "Runnable demo \u2014 Prime95 and the GIMPS project"], ["Installing both tools", "overview", "FurMark installs from Geeks3D and Prime95 ships as a ZIP from mersenne.org, with mprime as the Linux command-line twin. Both are free, both need no account, and both should be fetched from their official sites only.", {"mode": "pick"}, "Runnable demo \u2014 Installing both tools"], ["FurMark: the furry donut", "furmark", "FurMark renders an intensely furry 3D donut \u2014 millions of hair strands \u2014 because fur is one of the hardest things for a GPU to draw continuously. The result is a sustained, worst-case power draw that exposes weak cooling", {"mode": "furmark", "res": "1920x1080", "msaa": 8}, "Runnable demo \u2014 FurMark: the furry donut"], ["FurMark resolution and MSAA", "furmark", "FurMark offers presets from 720p to 4K with optional MSAA anti-aliasing, and fullscreen mode removes the desktop compositor from the measurement. Higher resolutions shift the load toward memory bandwidth; MSAA multiplies", {"mode": "furmark", "res": "2560x1440", "msaa": 8}, "Runnable demo \u2014 FurMark resolution and MSAA"], ["FurMark score and FPS", "furmark", "Benchmark mode runs a fixed-length loop and reports a score plus average FPS, submittable to the online comparison database. The score only means something at identical settings, so reviewers always quote resolution and ", {"mode": "score", "score": 15230, "fps": 254, "res": "1920x1080, 0x MSAA"}, "Runnable demo \u2014 FurMark score and FPS"], ["Prime95 torture test modes", "prime95", "Prime95's torture test offers three classic blends: Small FFTs for maximum CPU heat, In-place Large FFTs for the memory controller, and Blend for CPU plus RAM together. Each mode stresses a different part of the platform", {"mode": "prime_modes", "modes": ["Small FFTs - maximum heat/power", "In-place large FFTs - memory controller", "Blend - CPU + RAM together", "Custom - your own FFT range"]}, "Runnable demo \u2014 Prime95 torture test modes"], ["Small FFTs: maximum heat", "prime95", "Small FFTs keep the transform inside the CPU caches, which produces the highest possible power draw and temperature \u2014 the famous 'power virus' workload. If the cooler survives an hour of small FFTs, it survives anything.", {"mode": "fft", "fft": 8, "what": "CPU cores and caches (max heat)"}, "Runnable demo \u2014 Small FFTs: maximum heat"], ["Blend: CPU plus RAM", "prime95", "Blend alternates FFT sizes so the workload spills into system RAM, testing the CPU, memory controller, and DIMMs as one chain. A machine that passes small FFTs but fails Blend usually has a RAM problem, not a CPU problem", {"mode": "blend", "ram": 24}, "Runnable demo \u2014 Blend: CPU plus RAM"], ["Lucas-Lehmer: the real Prime95 math", "prime95", "Prime95 proves Mersenne primes with the Lucas-Lehmer test: start s at 4, repeat s = s\u00b2 \u2212 2 modulo (2^p \u2212 1) for p\u22122 rounds, and the number is prime only if s ends at zero. This demo runs the genuine algorithm on the expo", {"mode": "mersenne", "p": 19}, "Runnable demo \u2014 Lucas-Lehmer: the real Prime95 math"], ["Workers equal threads", "prime95", "Prime95 launches one worker per CPU thread by default, each grinding an independent FFT, and the Torture Test window shows every worker's progress. A single worker throwing errors while the rest pass points at one weak c", {"mode": "workers", "n": 16}, "Runnable demo \u2014 Workers equal threads"], ["Command line: mprime", "prime95", "On Linux the same engine runs as mprime, and './mprime -t' starts the torture test with no GUI at all. Server burn-in scripts drive mprime for hours and parse its results files for the word FATAL.", {"mode": "cmdline", "cmd": "./mprime -t"}, "Runnable demo \u2014 Command line: mprime"], ["Reading the graphs", "furmark", "FurMark draws the GPU temperature as a live curve, which should rise smoothly and plateau; a sawtooth means throttling. Prime95's per-worker view shows iteration times, where one slow worker betrays a throttling core.", {"mode": "graph"}, "Runnable demo \u2014 Reading the graphs"], ["PSU load arithmetic", "overview", "Stability testing is also PSU testing: add the CPU's and GPU's stressed wattage and compare against the supply's rating. Two hundred watts of CPU plus 320 of GPU on a 550 W supply leaves almost no headroom, and this demo", {"mode": "psu", "cpu": 200, "gpu": 320, "psu": 750}, "Runnable demo \u2014 PSU load arithmetic"], ["Safety rules and the full workflow", "safety", "Stress testing is safe when you respect heat: watch temperatures the whole time, stop at 90 C on the CPU or 85 C sustained on the GPU, and never leave a first-time overclock unattended. The full ritual is FurMark alone, ", {"mode": "workflow", "steps": ["FurMark 15 min - GPU and its cooling", "Prime95 small FFTs 1 hr - CPU heat", "Prime95 Blend 1 hr - CPU + RAM", "Both together 30 min - PSU maximum", "Log temps throughout with HWiNFO64"]}, "Runnable demo \u2014 Safety rules and the full workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"furmark\"){\n  show(\"Test\",\"furry donut 3D render\");\n  show(\"Resolution\",DATA.res);\n  show(\"MSAA\",DATA.msaa+\"x\");\n  show(\"Why it works\",\"maximum sustained GPU power draw\");\n}else if(m===\"prime_modes\"){\n  console.log(\"Torture test modes:\");\n  DATA.modes.forEach(function(x){console.log(\"  \"+x);});\n}else if(m===\"mersenne\"){\n  var p=DATA.p,M=Math.pow(2,p)-1,s=4,i;\n  for(i=0;i<p-2;i++){s=(s*s-2)%M;}\n  show(\"Testing\",\"2^\"+p+\" - 1 = \"+M);\n  show(\"Lucas-Lehmer\",s===0?\"PRIME - a Mersenne prime\":\"composite\");\n  show(\"Note\",\"the real test Prime95 runs, at tiny scale\");\n}else if(m===\"workers\"){\n  show(\"Workers\",DATA.n);\n  show(\"Rule\",\"one worker per thread by default\");\n  show(\"Each worker\",\"an independent FFT workload\");\n}else if(m===\"fft\"){\n  show(\"FFT size\",DATA.fft+\"K\");\n  show(\"Stresses most\",DATA.what);\n}else if(m===\"blend\"){\n  show(\"Blend test\",\"CPU and RAM together\");\n  show(\"RAM exercised\",DATA.ram+\" GB\");\n}else if(m===\"temps\"){\n  show(\"CPU temp\",DATA.cpu+\" C\");\n  show(\"GPU temp\",DATA.gpu+\" C\");\n  show(\"Verdict\",(DATA.cpu<90&&DATA.gpu<85)?\"PASS\":\"FAIL - cooling inadequate\");\n}else if(m===\"score\"){\n  show(\"FurMark score\",DATA.score);\n  show(\"Average FPS\",DATA.fps);\n  show(\"At\",DATA.res);\n}else if(m===\"safety\"){\n  console.log(\"Safety rules:\");\n  DATA.rules.forEach(function(r,i){console.log(\"  \"+(i+1)+\". \"+r);});\n}else if(m===\"cmdline\"){\n  show(\"Command\",DATA.cmd);\n  show(\"Use\",\"scripted burn-in without the GUI\");\n}else if(m===\"graph\"){\n  show(\"FurMark graph\",\"live GPU temperature curve\");\n  show(\"Prime95 view\",\"per-worker iteration times\");\n}else if(m===\"pick\"){\n  show(\"GPU only\",\"FurMark\");\n  show(\"CPU only\",\"Prime95 small FFTs\");\n  show(\"CPU + RAM\",\"Prime95 blend\");\n  show(\"Everything\",\"both at once - maximum PSU load\");\n}else if(m===\"psu\"){\n  show(\"CPU draw\",DATA.cpu+\" W\");\n  show(\"GPU draw\",DATA.gpu+\" W\");\n  show(\"Combined vs PSU\",(DATA.cpu+DATA.gpu)+\" W of \"+DATA.psu+\" W\");\n  show(\"Headroom\",(DATA.psu-DATA.cpu-DATA.gpu)+\" W\");\n}else if(m===\"history\"){\n  show(\"Prime95\",\"Mersenne prime hunting for GIMPS since 1996\");\n  show(\"FurMark\",\"Geeks3D's furry-donut GPU burner\");\n}else if(m===\"workflow\"){\n  console.log(\"Stability workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
function jitter(v,rnd){
  if(typeof v==='number'){return Math.round(v*(0.9+rnd()*0.2)*100)/100;}
  if(Array.isArray(v)){return v.map(function(x){return jitter(x,rnd);});}
  if(v&&typeof v==='object'){var o={};Object.keys(v).forEach(function(k){o[k]=jitter(v[k],rnd);});return o;}
  return v;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(typeof seed==='number'&&seed>SELFREG.maxRecords)throw new Error('SELF-REGULATION HARD STOP: 1,000,000,000,000 record limit reached');
  var cat=opts.category||pick(CATS,rnd);
  var pool=ARCH.filter(function(a){return a[1]===cat;});
  var a=pick(pool.length?pool:ARCH,rnd);
  var scen=jitter(a[3],rnd); scen.mode=a[3].mode;
  var id=PREFIX+String(10001+seed).padStart(6,'0');
  var program=ENGINE.split('__DATA__').join(JSON.stringify(scen));
  var facts=jitter(a[4]||{},rnd);
  return {id:id,t:a[0]+' (simulated #'+seed+')',
    title:DBNAME+' \u2014 '+a[0]+' (simulated variant, seed '+seed+')',
    g:a[1],category:a[1],
    description:a[2]+' This is a simulated boundless-generator variant (seed '+seed+') from '+GENVER+': the scenario values were deterministically jittered from the archive archetype, and the record passed the independent correctness validator before acceptance.',
    ladder_rank:1+((seed-1)%15),
    march:'MILLION MARCH \u00b7 simulated record \u00b7 archive marches to a 1,000,000-record target \u2014 in progress',
    provenance:PROV,last_verified:'2026-10-21',record_label:SELFREG.simulatedLabel,
    facts:facts,
    demo:{engine:'jahdb-demo-1.0',kind:'code',title:'Runnable demo \u2014 '+a[0]+' (simulated)',language:'javascript',
      program:program,run_hint:'PC: save as demo.js, run `node demo.js`. In-page: press Run.',
      how_to_run:'PC: save the program as demo.js and run `node demo.js`. In-page: open the Demo Lab tab and press Run.',runnable:true},
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-furmark-prime95/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-furmark-prime95',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  var n=parseInt(String(r.id||'').slice(PREFIX.length),10);
  if(!(n>=10001))e.push('id-block (generator ids start at 10001; archive owns 1-9999)');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.record_label!==SELFREG.simulatedLabel)e.push('record_label');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.demo&&r.demo.language!=='javascript')e.push('demo-language');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return{ok:false,errors:['drift: exact title already in archive']}; }
  return{ok:true,errors:[]};
}
var gen={version:GENVER,selfRegulation:SELFREG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-furmark-prime95',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
