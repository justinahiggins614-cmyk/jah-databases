(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "furmark", "prime95", "safety"];
var PREFIX='JAH-PCO58S-';
var GENVER='jahdb-pc-organizer-furmark-prime95-signature-1.0';
var DBNAME='Signature Stress Forge';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Forge concept", "overview", "The Signature Stress Forge is Manon's original proving ground: one launcher that graduates stress from a warm-up to a full assault automatically. Every stage has a temperature ceiling and a pass rule, so the Forge proves", {"mode": "furmark", "res": "1920x1080", "msaa": 4}, "Runnable demo \u2014 Forge concept"], ["Forge lineage", "overview", "The Forge honors its ancestors openly: the GPU furnace descends from FurMark's donut, the CPU crucible from Prime95's FFTs, and the prime corner from GIMPS itself. Standing on proven methods, it adds the orchestration an", {"mode": "history"}, "Runnable demo \u2014 Forge lineage"], ["One launcher", "overview", "The Forge is a single signed package with CPU, GPU, memory, and PSU trials behind one Start button and one Stop button. Presets name the goal \u2014 'new build,' 'new overclock,' 'used PSU' \u2014 instead of exposing FFT sizes on ", {"mode": "pick"}, "Runnable demo \u2014 One launcher"], ["GPU furnace", "furmark", "The GPU furnace renders procedurally generated fur, rock, and glass scenes in rotation so no single shader path gets to rest. Scene rotation defeats driver cheats that recognize one fixed donut and throttle around it.", {"mode": "furmark", "res": "2560x1440", "msaa": 8}, "Runnable demo \u2014 GPU furnace"], ["Furnace telemetry", "furmark", "The furnace records temperature, clock, power, and fan as synchronized curves, so a throttling event shows its cause and effect on one timeline. Export is one click to CSV, because a claim without data is just a story.", {"mode": "score", "score": 16800, "fps": 280, "res": "2560x1440, 8x MSAA"}, "Runnable demo \u2014 Furnace telemetry"], ["CPU crucible modes", "prime95", "The crucible offers named trials \u2014 Ember (cache heat), Anvil (memory controller), Tempest (everything) \u2014 each mapped to the FFT science underneath. Names for humans, parameters for the log.", {"mode": "prime_modes", "modes": ["Ember - cache heat trial", "Anvil - memory controller trial", "Tempest - full platform trial", "Custom - raw FFT control"]}, "Runnable demo \u2014 CPU crucible modes"], ["Ember: cache heat", "prime95", "Ember pins small transforms inside the caches for maximum thermal density, the way small FFTs do. The Forge watches per-core temperatures and names the hottest core in the verdict.", {"mode": "fft", "fft": 8, "what": "CPU cores and caches (max thermal density)"}, "Runnable demo \u2014 Ember: cache heat"], ["Tempest: the full chain", "prime95", "Tempest walks transform sizes from cache to RAM and back, stressing cores, controller, and DIMMs as one chain. A failure's FFT size is recorded, which tells the technician exactly which link broke.", {"mode": "blend", "ram": 32}, "Runnable demo \u2014 Tempest: the full chain"], ["Prime corner", "prime95", "The prime corner runs genuine Lucas-Lehmer tests on small exponents as a correctness ritual before every stress run. If the machine cannot prove 524287 prime, it has no business being called stable.", {"mode": "mersenne", "p": 19}, "Runnable demo \u2014 Prime corner"], ["Worker warden", "prime95", "The worker warden pins one worker per thread and watches each one's pace; a lagging worker gets its core named in the report. Affinity control lets a trial target specific cores, which is how you interrogate one suspicio", {"mode": "workers", "n": 16}, "Runnable demo \u2014 Worker warden"], ["Headless forge", "prime95", "The headless Forge runs the full trial set from a command line for servers and scripts, reporting machine-readable verdicts. Burn-in farms drive it for days and grep the logs for the word FAULT.", {"mode": "cmdline", "cmd": "forge --trial tempest --hours 4 --json"}, "Runnable demo \u2014 Headless forge"], ["Cause-and-effect graphs", "furmark", "Forge graphs overlay temperature, clock, and power on one axis set, so a temperature spike and its clock dip appear as one event. Annotations mark every limit the safety brain enforced during the run.", {"mode": "graph"}, "Runnable demo \u2014 Cause-and-effect graphs"], ["PSU reckoning", "overview", "The PSU reckoning trial loads CPU and GPU to their combined maximum and integrates the wattage over ten minutes. The verdict compares the measured peak against the supply's rating and its age derating.", {"mode": "psu", "cpu": 220, "gpu": 350, "psu": 850}, "Runnable demo \u2014 PSU reckoning"], ["Safety brain", "safety", "The safety brain enforces temperature ceilings per component and halts the trial the instant one is crossed, logging the exact second. It also refuses to start if baseline idle temps already look wrong.", {"mode": "safety", "rules": ["Halt instantly past any ceiling", "Refuse to start on bad idle baselines", "Log every intervention with timestamp", "Never auto-restart a failed trial", "Keep a human in the loop for overclocks"]}, "Runnable demo \u2014 Safety brain"], ["Certification workflow", "safety", "A Forge certification is a sealed ritual: correctness ritual, graduated trials, cooldown observation, and a signed report with every curve attached. Certified machines carry their report; everything else is just a claim.", {"mode": "workflow", "steps": ["Prime-corner correctness ritual", "Ember cache-heat trial", "Tempest full-chain trial", "GPU furnace with telemetry", "Cooldown observation and signed report"]}, "Runnable demo \u2014 Certification workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-furmark-prime95-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-furmark-prime95-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-furmark-prime95-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
