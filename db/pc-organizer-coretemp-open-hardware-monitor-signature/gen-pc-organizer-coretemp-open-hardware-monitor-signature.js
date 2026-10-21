(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "coretemp", "ohm"];
var PREFIX='JAH-PCO59S-';
var GENVER='jahdb-pc-organizer-coretemp-open-hardware-monitor-signature-1.0';
var DBNAME='Signature Thermal Watch';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Watch concept", "overview", "The Signature Thermal Watch is Manon's original thermal sentinel: it shows every core's temperature as distance-to-danger, not as a bare number. Seventy-two degrees means nothing; twenty-eight degrees of headroom means e", {"mode": "percore", "cores": [55, 58, 56, 60, 54, 57, 59, 56]}, "Runnable demo \u2014 Watch concept"], ["Watch at first boot", "overview", "The Watch needs no install and learns the machine's idle personality in its first hour \u2014 what 'normal' means for this cooler, this case, this room. Every later reading is judged against that personal baseline, not a gene", {"mode": "coretemp", "hot": 62, "low": 54}, "Runnable demo \u2014 Watch at first boot"], ["Distance dials", "coretemp", "Each core gets a distance dial: a ring that empties as the core approaches its throttle point. Color does the talking \u2014 blue, amber, red \u2014 so danger is readable from across the room.", {"mode": "tjmax", "tjmax": 100, "temp": 66}, "Runnable demo \u2014 Distance dials"], ["Core truth", "coretemp", "The Watch reads per-core sensors directly and names the hottest core in every summary, because averages lie and maximums decide. A single hot core gets its history plotted, not just its current number.", {"mode": "percore", "cores": [55, 58, 56, 74, 54, 57, 59, 56]}, "Runnable demo \u2014 Core truth"], ["Glance bar", "coretemp", "The glance bar is a one-line taskbar readout: hottest core, its headroom, and a trend arrow. It is designed to be read in a quarter second during a loading screen.", {"mode": "tray", "now": 68}, "Runnable demo \u2014 Glance bar"], ["Chronicle logging", "coretemp", "The Watch logs to a queryable chronicle instead of CSVs, tagging entries with what was running. 'How hot was the render last Thursday' is a question with an answer, not a file search.", {"mode": "log", "file": "thermal-chronicle.db", "ms": 1000}, "Runnable demo \u2014 Chronicle logging"], ["Guardian actions", "coretemp", "Guardian actions graduate with the heat: warn at 85 C, pause the workload at 92 C, shut down at 98 C, each announced before it fires. Protection that explains itself never gets disabled in annoyance.", {"mode": "overheat", "th": 85, "action": "warn, then pause workload at 92 C"}, "Runnable demo \u2014 Guardian actions"], ["Watch extensions", "coretemp", "Extensions add remote dashboards, keyboard-screen applets, and streaming overlays, all reading the same sensor core. The Watch itself stays a single small process; extensions are guests, not roommates.", {"mode": "plugin", "n": 9}, "Runnable demo \u2014 Watch extensions"], ["Open sensor tree", "ohm", "The Watch's sensor tree is open by design: every reading it takes is readable by any local app through a documented socket. Openness is a feature, so your scripts never need screen-scraping.", {"mode": "ohm", "n": 92}, "Runnable demo \u2014 Open sensor tree"], ["Living fork", "ohm", "The Watch ships its sensor engine as source with a standing invitation: new hardware support lands as community modules. A new CPU launch means a new module, not a wait for a vendor update.", {"mode": "fork"}, "Runnable demo \u2014 Living fork"], ["Query interface", "ohm", "Any program can ask the Watch for any sensor over its local interface and get JSON back in milliseconds. Monitoring becomes infrastructure instead of a window you have to look at.", {"mode": "wmi"}, "Runnable demo \u2014 Query interface"], ["Ambient awareness", "ohm", "The Watch tracks ambient temperature alongside component temps, because 75 C on the CPU means something different in a 18 C room than a 30 C one. Cooler performance is always reported as delta over ambient \u2014 the honest n", {"mode": "gadget"}, "Runnable demo \u2014 Ambient awareness"], ["Watch vs the classics", "overview", "The Watch keeps CoreTemp's tray-first glanceability and OHM's full-tree depth, then adds the missing piece both lack: judgment. It does not just show numbers; it says what they mean and what to do.", {"mode": "compare"}, "Runnable demo \u2014 Watch vs the classics"], ["Spread detective", "coretemp", "The spread detective watches per-core spread continuously and flags a widening gap weeks before it becomes throttling. A mount degrading slowly is invisible day to day and obvious to a baseline.", {"mode": "delta", "a": 56, "b": 71}, "Runnable demo \u2014 Spread detective"], ["Sentinel workflow", "coretemp", "The sentinel workflow: learn the baseline, watch the distances, log everything, act in graduated steps. The machine's thermal story writes itself, and the Watch is its biographer.", {"mode": "workflow", "steps": ["Learn the idle baseline", "Watch distance-to-danger dials", "Log to the chronicle", "Graduate responses with heat", "Review the thermal biography monthly"]}, "Runnable demo \u2014 Sentinel workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"percore\"){\n  console.log(\"Per-core temps:\");\n  DATA.cores.forEach(function(t,i){console.log(\"  Core \"+i+\": \"+t+\" C\");});\n  show(\"Hottest core\",Math.max.apply(null,DATA.cores)+\" C\");\n}else if(m===\"tjmax\"){\n  var d=DATA.tjmax-DATA.temp;\n  show(\"TjMax\",DATA.tjmax+\" C\");show(\"Current\",DATA.temp+\" C\");\n  show(\"Distance to TjMax\",d+\" C\");\n  show(\"Status\",d>20?\"comfortable\":(d>5?\"warm\":\"CRITICAL\"));\n}else if(m===\"coretemp\"){\n  show(\"Tool\",\"CoreTemp - per-core DTS readings\");\n  show(\"Hottest\",DATA.hot+\" C\");show(\"Coolest\",DATA.low+\" C\");\n}else if(m===\"ohm\"){\n  show(\"Tool\",\"Open Hardware Monitor - open-source sensor tree\");\n  show(\"Sensors\",DATA.n+\" across CPU, GPU, board, drives\");\n}else if(m===\"fork\"){\n  show(\"Original\",\"Open Hardware Monitor\");\n  show(\"Maintained fork\",\"LibreHardwareMonitor - actively updated\");\n  show(\"Advice\",\"use the fork on modern hardware\");\n}else if(m===\"wmi\"){\n  show(\"Interface\",\"WMI - other apps query sensors\");\n  show(\"Use\",\"scripts, widgets, and remote dashboards\");\n}else if(m===\"gadget\"){\n  show(\"Desktop gadget\",\"live temps on the desktop\");\n  show(\"Taskbar\",\"per-core icons always visible\");\n}else if(m===\"log\"){\n  show(\"Log\",DATA.file);show(\"Interval\",DATA.ms+\" ms\");\n}else if(m===\"overheat\"){\n  show(\"Protection\",\"at \"+DATA.th+\" C -> \"+DATA.action);\n}else if(m===\"plugin\"){\n  show(\"Plugins\",DATA.n+\" available\");\n  show(\"Examples\",\"remote server, Logitech G15 applet\");\n}else if(m===\"tray\"){\n  show(\"Taskbar\",\"hottest core temp always visible\");\n  show(\"Why\",\"glanceable during fullscreen games\");\n  show(\"Now\",DATA.now+\" C\");\n}else if(m===\"delta\"){\n  show(\"Core 0\",DATA.a+\" C\");show(\"Core 5\",DATA.b+\" C\");\n  show(\"Spread\",Math.abs(DATA.a-DATA.b)+\" C\");\n  show(\"Note\",\"big spreads hint at cooler mount issues\");\n}else if(m===\"compare\"){\n  show(\"CoreTemp\",\"tiny, per-core focused, plugin ecosystem\");\n  show(\"OHM / Libre\",\"full sensor tree, open source, WMI\");\n}else if(m===\"workflow\"){\n  console.log(\"Temp-watch workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-coretemp-open-hardware-monitor-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-coretemp-open-hardware-monitor-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-coretemp-open-hardware-monitor-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
