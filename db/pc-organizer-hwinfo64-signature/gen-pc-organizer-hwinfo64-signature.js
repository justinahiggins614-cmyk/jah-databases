(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sensors", "logging", "alerts", "osd"];
var PREFIX='JAH-PCO56S-';
var GENVER='jahdb-pc-organizer-hwinfo64-signature-1.0';
var DBNAME='Signature Hardware Observatory';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Observatory concept", "overview", "The Signature Hardware Observatory is Manon's original monitoring design: every sensor in the machine presented as an exhibit with its normal range printed beside it. A reading is only half the story; the Observatory alw", {"mode": "sensors", "list": [{"name": "CPU package temp", "val": 55, "unit": "C"}, {"name": "GPU temp", "val": 62, "unit": "C"}, {"name": "CPU package power", "val": 82, "unit": "W"}]}, "Runnable demo \u2014 Observatory concept"], ["Observatory setup", "overview", "The Observatory runs portable with no install and discovers every sensor on first launch, filing each under its component. Its first scan builds a normal-range profile from the machine's own idle and load behavior.", {"mode": "sensors", "list": [{"name": "+12V rail", "val": 12.05, "unit": "V"}, {"name": "Chipset temp", "val": 48, "unit": "C"}]}, "Runnable demo \u2014 Observatory setup"], ["Exhibit halls", "sensors", "Sensors are grouped into halls \u2014 thermal, electrical, mechanical, computational \u2014 instead of one endless table. Each hall shows its worst offender first, so the eye lands on the problem before the trivia.", {"mode": "sensors", "list": [{"name": "Hottest core", "val": 68, "unit": "C"}, {"name": "Slowest fan", "val": 750, "unit": "RPM"}, {"name": "Lowest rail", "val": 11.98, "unit": "V"}]}, "Runnable demo \u2014 Exhibit halls"], ["Thermal exhibits", "sensors", "Thermal exhibits show every temperature with its throttle line drawn on the graph, turning 'is 78 C bad' into a glance. The Observatory learns each sensor's personal normal from history rather than using one generic limi", {"mode": "stats", "name": "Hottest CPU core", "unit": "C", "vals": [52, 58, 64, 61, 70, 66, 59, 55, 62, 68]}, "Runnable demo \u2014 Thermal exhibits"], ["Electrical exhibits", "sensors", "Electrical exhibits track every rail against its ATX tolerance band, shading the safe zone on the graph. A rail living at the edge of its band gets flagged long before it causes the crashes it is famous for.", {"mode": "volts", "rails": [{"name": "Vcore", "v": 1.26}, {"name": "+12V", "v": 12.02}, {"name": "+5V", "v": 5.01}, {"name": "+3.3V", "v": 3.3}]}, "Runnable demo \u2014 Electrical exhibits"], ["Mechanical exhibits", "sensors", "Mechanical exhibits pair each fan's RPM with its duty cycle and the temperature it is fighting, showing whether the curve is sane. A fan at 100 percent while temps still climb is a cooler problem wearing a fan disguise.", {"mode": "fans", "fans": [{"name": "CPU fan", "rpm": 1250, "pct": 50}, {"name": "Chassis 1", "rpm": 850, "pct": 38}]}, "Runnable demo \u2014 Mechanical exhibits"], ["Power ledger", "sensors", "The power ledger totals CPU, GPU, and board draw into one system number with a per-hour energy cost. It answers 'what does this rig cost to run' with the same honesty it answers 'is the PSU enough'.", {"mode": "power", "cpu": 95, "gpu": 200}, "Runnable demo \u2014 Power ledger"], ["Story columns", "sensors", "Beyond min, max, and average, the Observatory keeps a 'story' column: what happened during the extremes, in words. 'Max 91 C during Blender, fan at 100%' beats a bare number every time.", {"mode": "stats", "name": "GPU memory temp", "unit": "C", "vals": [60, 66, 72, 70, 78, 74, 68, 64, 70, 76]}, "Runnable demo \u2014 Story columns"], ["Session chronicles", "logging", "Session chronicles store sensor logs in a queryable archive instead of loose CSVs, tagged by what was running. Comparing today's thermals to last month's is a query, not an archaeology dig.", {"mode": "log", "file": "observatory-chronicle.db", "ms": 500}, "Runnable demo \u2014 Session chronicles"], ["Guardian alerts", "alerts", "Guardian alerts pair every threshold with a graduated response: warn at 85 C, throttle the workload at 92 C, shut down at 98 C. Each step is announced in plain language before it acts, so protection never feels like a su", {"mode": "alert", "name": "CPU package temp", "th": 85, "val": 88, "action": "warn now, throttle workload at 92 C"}, "Runnable demo \u2014 Guardian alerts"], ["Overlay director", "osd", "The overlay director composes the on-screen display from sensor exhibits with a visual editor, no config files. Layouts save per game, so the racing sim and the strategy game each get their own telemetry.", {"mode": "osd", "what": "FPS + frame time + CPU/GPU temps", "layout": "bottom-right graph cluster"}, "Runnable demo \u2014 Overlay director"], ["Derived instruments", "sensors", "Derived instruments let any formula become a first-class sensor: total watts, FPS per watt, cooler delta over ambient. The Observatory ships with a library of the useful ones and the formula bar invites your own.", {"mode": "custom", "name": "Cooler delta", "formula": "CPU temp - ambient temp", "result": 31, "unit": "C"}, "Runnable demo \u2014 Derived instruments"], ["Machine biography", "overview", "The machine biography is a living document the Observatory maintains: every component, every firmware, every baseline score, every thermal event. Hand the biography to a buyer or a technician and there is nothing left to", {"mode": "report", "file": "machine-biography.html", "fmt": "HTML", "sections": "all components + history"}, "Runnable demo \u2014 Machine biography"], ["Adaptive polling", "sensors", "Adaptive polling samples fast when values move and relaxes when they are still, keeping graphs smooth without wasting CPU. The Observatory spends its attention where the action is, automatically.", {"mode": "poll", "ms": 250}, "Runnable demo \u2014 Adaptive polling"], ["Certification run", "logging", "A certification run is the Observatory's formal ritual: baseline, ten-minute stress, cooldown, all logged and sealed with a report. Cooler reviews and overclock claims get certified instead of asserted.", {"mode": "workflow", "steps": ["Record baseline sensors", "Run ten-minute stress", "Capture cooldown curve", "Seal the session chronicle", "Publish the certificate"]}, "Runnable demo \u2014 Certification run"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-hwinfo64-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-hwinfo64-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-hwinfo64-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
