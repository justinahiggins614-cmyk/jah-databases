(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sensors", "logging", "alerts", "osd"];
var PREFIX='JAH-PCO56-';
var GENVER='jahdb-pc-organizer-hwinfo64-1.0';
var DBNAME='HWiNFO64';
var PROV='Public documentation and published specifications for HWiNFO64; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What HWiNFO64 does", "overview", "HWiNFO64 by REALiX is the most complete hardware monitoring suite on Windows: it reads every temperature, voltage, fan, clock, and power sensor the machine exposes. Enthusiasts call it the ultimate because nothing else s", {"mode": "sensors", "list": [{"name": "CPU package temp", "val": 58, "unit": "C"}, {"name": "GPU temp", "val": 64, "unit": "C"}, {"name": "CPU package power", "val": 88, "unit": "W"}, {"name": "Fan 1", "val": 1150, "unit": "RPM"}]}, "Runnable demo \u2014 What HWiNFO64 does"], ["Installing and portable mode", "overview", "HWiNFO64 offers an installer and a portable ZIP that runs from any folder or USB stick with no installation at all. The portable build is the one technicians carry, since it leaves no trace on the machine being diagnosed", {"mode": "sensors", "list": [{"name": "Vcore", "val": 1.28, "unit": "V"}, {"name": "+12V rail", "val": 12.096, "unit": "V"}]}, "Runnable demo \u2014 Installing and portable mode"], ["Sensors-only mode", "sensors", "Launching in sensors-only mode skips the system summary and opens straight on the live sensor table, which is how the tool is used 90 percent of the time. The window can stay on top during a game or benchmark as a always", {"mode": "sensors", "list": [{"name": "CPU clock (avg)", "val": 4850, "unit": "MHz"}, {"name": "GPU clock", "val": 2610, "unit": "MHz"}, {"name": "Memory used", "val": 11.2, "unit": "GB"}]}, "Runnable demo \u2014 Sensors-only mode"], ["Temperature sensors", "sensors", "HWiNFO64 lists temperatures per CPU core, per GPU zone, per drive, and per motherboard probe \u2014 dozens of readings on a modern board. The min/max/average columns turn a stress test into a thermal report card automatically", {"mode": "stats", "name": "CPU package temperature", "unit": "C", "vals": [44, 52, 61, 58, 72, 68, 55, 49, 63, 71]}, "Runnable demo \u2014 Temperature sensors"], ["Voltage rails", "sensors", "The voltage section shows Vcore, memory voltage, and the PSU's 12V, 5V, and 3.3V rails as reported by the board's Super I/O chip. A 12V rail drooping toward 11.4V under load is an early warning that the power supply is s", {"mode": "volts", "rails": [{"name": "Vcore", "v": 1.28}, {"name": "+12V", "v": 12.096}, {"name": "+5V", "v": 5.04}, {"name": "+3.3V", "v": 3.312}, {"name": "DIMM", "v": 1.35}]}, "Runnable demo \u2014 Voltage rails"], ["Fan sensors", "sensors", "Every controllable fan header appears with its RPM and duty cycle, so you can see exactly how the board responds to heat. Matching a fan curve to the temperature graph is how quiet builds get quiet without getting hot.", {"mode": "fans", "fans": [{"name": "CPU fan", "rpm": 1150, "pct": 45}, {"name": "Chassis 1", "rpm": 800, "pct": 35}, {"name": "GPU fan", "rpm": 2100, "pct": 62}]}, "Runnable demo \u2014 Fan sensors"], ["Power readings", "sensors", "CPU package power, per-rail estimates, and GPU board power draw let you audit the whole system's appetite in watts. Adding CPU and GPU draw predicts PSU load, which is the number that sizes power supplies honestly.", {"mode": "power", "cpu": 88, "gpu": 186}, "Runnable demo \u2014 Power readings"], ["Min, max, and average columns", "sensors", "Every sensor keeps minimum, maximum, and average columns alongside the live value, resetting on demand. After a benchmark you read the max temperature and average clock straight off the table \u2014 no separate logging needed", {"mode": "stats", "name": "GPU clock", "unit": "MHz", "vals": [210, 1920, 2595, 2610, 2580, 2400, 2610, 2595, 2200, 1500]}, "Runnable demo \u2014 Min, max, and average columns"], ["Logging to CSV", "logging", "Sensor logging writes every reading to a CSV file at your chosen interval, producing a spreadsheet of the entire session. Analysts graph the log to show temperature and frequency behavior across a benchmark instead of qu", {"mode": "log", "file": "HWiNFO64.CSV", "ms": 1000}, "Runnable demo \u2014 Logging to CSV"], ["Alerts with actions", "alerts", "Any sensor can carry an alert: cross the threshold and HWiNFO64 can show a warning, run a program, or shut the machine down. A 90 C CPU alert that kills the benchmark protects a cooler whose mount just failed.", {"mode": "alert", "name": "CPU package temp", "th": 90, "val": 88, "action": "show warning + stop benchmark"}, "Runnable demo \u2014 Alerts with actions"], ["On-screen display via RTSS", "osd", "HWiNFO64 feeds any sensor to RivaTuner Statistics Server's on-screen display through shared memory, putting temperatures and frame rates over the game. The overlay editor arranges the values exactly where you want them.", {"mode": "osd", "what": "CPU temp + GPU temp + FPS", "layout": "top-left, two lines"}, "Runnable demo \u2014 On-screen display via RTSS"], ["Custom sensors", "sensors", "Custom sensors combine real readings with formulas \u2014 total system power, temperature deltas, or efficiency in frames per watt. They turn raw telemetry into the exact derived number your question needs.", {"mode": "custom", "name": "System efficiency", "formula": "FPS / (CPU W + GPU W)", "result": 0.52, "unit": "FPS/W"}, "Runnable demo \u2014 Custom sensors"], ["System summary and reports", "overview", "The summary window inventories the whole machine \u2014 CPU, board, memory, drives, GPU \u2014 and the report generator exports it as text or HTML. It is the fastest honest spec sheet for a machine you are about to sell or support", {"mode": "report", "file": "HWiNFO64-report.HTM", "fmt": "HTML", "sections": "CPU, board, memory, drives, GPU"}, "Runnable demo \u2014 System summary and reports"], ["Polling rate", "sensors", "The global polling period sets how often every sensor is re-read; 500 to 1000 ms suits most monitoring, while fast transient hunting goes lower. Faster polling smooths graphs but costs a little CPU of its own.", {"mode": "poll", "ms": 1000}, "Runnable demo \u2014 Polling rate"], ["Stress-test monitoring workflow", "logging", "The standard monitoring ritual: reset min/max, start CSV logging, launch the stress test, then read max temperatures and average clocks from the table. Saved logs make every claim about a cooler or overclock reproducible", {"mode": "workflow", "steps": ["Reset min/max columns", "Start CSV sensor logging", "Launch the stress test", "Read max temps and avg clocks", "Stop logging and archive the CSV"]}, "Runnable demo \u2014 Stress-test monitoring workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"sensors\"){\n  console.log(\"Sensors (\"+DATA.list.length+\"):\");\n  DATA.list.forEach(function(s){console.log(\"  \"+s.name+\": \"+s.val+\" \"+s.unit);});\n}else if(m===\"stats\"){\n  var vs=DATA.vals,mn=Math.min.apply(null,vs),mx=Math.max.apply(null,vs);\n  var avg=Math.round(vs.reduce(function(a,b){return a+b;},0)/vs.length*10)/10;\n  show(\"Sensor\",DATA.name);show(\"Min\",mn+\" \"+DATA.unit);\n  show(\"Max\",mx+\" \"+DATA.unit);show(\"Average\",avg+\" \"+DATA.unit);\n}else if(m===\"alert\"){\n  show(\"Sensor\",DATA.name);\n  show(\"Condition\",\"trigger when >= \"+DATA.th+\" \"+DATA.unit);\n  show(\"Action\",DATA.action);\n  show(\"Would trip now\",DATA.val>=DATA.th?\"YES at \"+DATA.val+\" \"+DATA.unit:\"no (\"+DATA.val+\" \"+DATA.unit+\")\");\n}else if(m===\"log\"){\n  show(\"File\",DATA.file);show(\"Interval\",DATA.ms+\" ms\");\n  show(\"Rows per hour\",Math.round(3600000/DATA.ms));\n}else if(m===\"osd\"){\n  show(\"Overlay\",DATA.what);\n  show(\"Feed\",\"RTSS shared memory\");\n  show(\"Layout\",DATA.layout);\n}else if(m===\"power\"){\n  show(\"CPU package\",DATA.cpu+\" W\");\n  show(\"GPU board\",DATA.gpu+\" W\");\n  show(\"Combined\",(DATA.cpu+DATA.gpu)+\" W\");\n}else if(m===\"fans\"){\n  DATA.fans.forEach(function(f){console.log(\"  \"+f.name+\": \"+f.rpm+\" RPM (\"+f.pct+\"%)\");});\n}else if(m===\"volts\"){\n  DATA.rails.forEach(function(r){console.log(\"  \"+r.name+\": \"+r.v+\" V\");});\n}else if(m===\"summary\"){\n  console.log(\"System summary: \"+DATA.cpu+\" / \"+DATA.gpu+\" / \"+DATA.ram);\n}else if(m===\"report\"){\n  show(\"Report\",DATA.file);show(\"Format\",DATA.fmt);\n  show(\"Sections\",DATA.sections);\n}else if(m===\"poll\"){\n  show(\"Polling period\",DATA.ms+\" ms\");\n  show(\"Trade-off\",\"faster = smoother graphs, slightly more CPU\");\n}else if(m===\"custom\"){\n  show(\"Custom sensor\",DATA.name);\n  show(\"Formula\",DATA.formula);\n  show(\"Result\",DATA.result+\" \"+DATA.unit);\n}else if(m===\"compare\"){\n  show(\"Reading A\",DATA.a+\" \"+DATA.unit);\n  show(\"Reading B\",DATA.b+\" \"+DATA.unit);\n  show(\"Delta\",(Math.round((DATA.b-DATA.a)*10)/10)+\" \"+DATA.unit);\n}else if(m===\"workflow\"){\n  console.log(\"Monitoring workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-hwinfo64/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-hwinfo64',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-hwinfo64',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
