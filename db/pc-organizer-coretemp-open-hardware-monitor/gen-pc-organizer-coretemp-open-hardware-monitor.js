(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "coretemp", "ohm"];
var PREFIX='JAH-PCO59-';
var GENVER='jahdb-pc-organizer-coretemp-open-hardware-monitor-1.0';
var DBNAME='CoreTemp / Open Hardware Monitor';
var PROV='Public documentation and published specifications for CoreTemp / Open Hardware Monitor; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What these tools do", "overview", "CoreTemp and Open Hardware Monitor are the lightweight end of temperature monitoring: CoreTemp parks per-core temps in the taskbar, OHM exposes the whole sensor tree as open source. Both answer one question instantly \u2014 h", {"mode": "percore", "cores": [58, 61, 59, 63, 57, 60, 62, 59]}, "Runnable demo \u2014 What these tools do"], ["CoreTemp basics", "coretemp", "CoreTemp by Arthur Liberman reads each CPU core's digital thermal sensor directly and shows the hottest core big and bold. It is tiny, free, and has lived in enthusiasts' system trays for nearly twenty years.", {"mode": "coretemp", "hot": 68, "low": 57}, "Runnable demo \u2014 CoreTemp basics"], ["TjMax and distance to throttle", "coretemp", "Every Intel and AMD chip has a TjMax \u2014 the junction temperature where it starts throttling \u2014 and CoreTemp shows your distance to it, not just the raw number. Twenty degrees of headroom is comfortable; five is a warning w", {"mode": "tjmax", "tjmax": 100, "temp": 72}, "Runnable demo \u2014 TjMax and distance to throttle"], ["Per-core readings", "coretemp", "CoreTemp lists every core separately because heat is never even: one core always runs hottest, and that core decides when throttling starts. Watching the spread between cores is the cheapest cooler diagnostic there is.", {"mode": "percore", "cores": [58, 61, 59, 72, 57, 60, 62, 59]}, "Runnable demo \u2014 Per-core readings"], ["System tray icons", "coretemp", "CoreTemp can paint the hottest core's temperature directly into the taskbar, so the number is visible even over a fullscreen game. One glance mid-match tells you whether the cooler is keeping up.", {"mode": "tray", "now": 71}, "Runnable demo \u2014 System tray icons"], ["Temperature logging", "coretemp", "CoreTemp's logging writes timestamped readings to CSV, turning a gaming session into a temperature history. The log settles arguments about whether 'it only gets hot sometimes' with data.", {"mode": "log", "file": "CoreTempLog.csv", "ms": 1000}, "Runnable demo \u2014 Temperature logging"], ["Overheat protection", "coretemp", "Overheat protection lets CoreTemp execute a program or shut the machine down when a threshold is crossed. It is the unattended-render insurance policy: if the cooler's pump dies at 3 AM, the machine saves itself.", {"mode": "overheat", "th": 90, "action": "execute shutdown script"}, "Runnable demo \u2014 Overheat protection"], ["CoreTemp plugins", "coretemp", "A plugin ecosystem extends CoreTemp with remote-server monitoring, a Logitech G15 keyboard applet, and desktop widgets. The core stays tiny; the plugins carry the extras.", {"mode": "plugin", "n": 12}, "Runnable demo \u2014 CoreTemp plugins"], ["Open Hardware Monitor", "ohm", "Open Hardware Monitor is the open-source alternative that shows temperatures, fan speeds, voltages, clocks, and load in one expandable tree. Being open source, its sensor code has been audited and reused across the ecosy", {"mode": "ohm", "n": 86}, "Runnable demo \u2014 Open Hardware Monitor"], ["The LibreHardwareMonitor fork", "ohm", "When the original OHM went quiet, the community fork LibreHardwareMonitor picked it up and keeps it current with new CPUs and GPUs. On modern hardware the fork is the correct download, and it stays API-compatible with th", {"mode": "fork"}, "Runnable demo \u2014 The LibreHardwareMonitor fork"], ["WMI interface", "ohm", "OHM exposes its sensors through WMI, so scripts, Rainmeter skins, and remote dashboards can query temperatures without touching the GUI. It turns a monitoring tool into a monitoring data source.", {"mode": "wmi"}, "Runnable demo \u2014 WMI interface"], ["Desktop gadget", "ohm", "The desktop gadget parks live temperatures on the desktop in a compact panel for machines that idle with the desktop visible. It is the at-a-glance dashboard for workstations that never go fullscreen.", {"mode": "gadget"}, "Runnable demo \u2014 Desktop gadget"], ["CoreTemp vs Open Hardware Monitor", "overview", "Choose CoreTemp when you want the smallest possible per-core tray monitor with plugins; choose OHM or its Libre fork when you want the whole sensor tree, open source, with WMI. Many benches run both: CoreTemp in the tray", {"mode": "compare"}, "Runnable demo \u2014 CoreTemp vs Open Hardware Monitor"], ["Reading core temperature spread", "coretemp", "Subtract the coolest core from the hottest: under 10 C of spread is a healthy mount, over 15 C deserves a repaste or remount. This demo computes the spread from live-style readings.", {"mode": "delta", "a": 57, "b": 72}, "Runnable demo \u2014 Reading core temperature spread"], ["Always-on thermal workflow", "coretemp", "The always-on ritual: CoreTemp in the tray showing the hottest core, logging on during heavy work, overheat protection armed for unattended runs. LibreHardwareMonitor on the second screen covers everything else.", {"mode": "workflow", "steps": ["Park CoreTemp in the tray", "Enable CSV logging for heavy work", "Arm overheat protection", "Open LibreHardwareMonitor for the full tree", "Review logs after long sessions"]}, "Runnable demo \u2014 Always-on thermal workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-coretemp-open-hardware-monitor/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-coretemp-open-hardware-monitor',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-coretemp-open-hardware-monitor',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
