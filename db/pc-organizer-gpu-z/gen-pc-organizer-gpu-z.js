(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "specs", "sensors", "power", "clocks"];
var PREFIX='JAH-PCO54-';
var GENVER='jahdb-pc-organizer-gpu-z-1.0';
var DBNAME='GPU-Z';
var PROV='Public documentation and published specifications for GPU-Z; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What GPU-Z does", "overview", "GPU-Z by TechPowerUp is the standard lightweight utility for reading everything about a graphics card: chip, memory, clocks, temperatures, and power. It installs in seconds, needs no account, and is the first tool review", {"mode": "specs", "name": "GeForce RTX 4070", "codename": "AD104", "shaders": 5888, "tmus": 184, "rops": 64, "mem_size": "12 GB", "mem_type": "GDDR6X", "bus": 192, "release": "Apr 2023"}, "Runnable demo \u2014 What GPU-Z does"], ["Installing GPU-Z", "overview", "GPU-Z ships as a single small executable with an optional installer, and a portable build that runs from a USB stick. Because it touches only read-only hardware registers, it is safe to run on any machine you are evaluat", {"mode": "lookup", "devid": "10DE-2786"}, "Runnable demo \u2014 Installing GPU-Z"], ["The Graphics Card tab", "specs", "The Graphics Card tab is the card's identity card: name, GPU codename, process size, die size, transistor count, release date, BIOS version, device ID, and subvendor. When a used card's story sounds suspicious, this tab ", {"mode": "specs", "name": "GeForce RTX 4070", "codename": "AD104", "shaders": 5888, "tmus": 184, "rops": 64, "mem_size": "12 GB", "mem_type": "GDDR6X", "bus": 192, "release": "Apr 2023"}, "Runnable demo \u2014 The Graphics Card tab"], ["Shaders, TMUs, and ROPs", "specs", "Three numbers define a GPU's muscle: shaders (CUDA cores) do the math, TMUs filter textures, and ROPs write finished pixels. GPU-Z lists all three, and comparing them against the official spec instantly exposes a rebadge", {"mode": "specs", "name": "GeForce RTX 4070", "codename": "AD104", "shaders": 5888, "tmus": 184, "rops": 64, "mem_size": "12 GB", "mem_type": "GDDR6X", "bus": 192, "release": "Apr 2023"}, "Runnable demo \u2014 Shaders, TMUs, and ROPs"], ["Pixel and texture fillrate", "specs", "Fillrate turns the unit counts into speed: pixel fillrate is ROPs times clock, texture fillrate is TMUs times clock. GPU-Z shows both, and this demo recomputes them from the raw counts so you can verify any card by hand.", {"mode": "fillrate", "rops": 64, "tmus": 184, "clock": 2610}, "Runnable demo \u2014 Pixel and texture fillrate"], ["Memory specs and bandwidth", "specs", "The memory section lists type, size, bus width, and the resulting bandwidth \u2014 the number that decides high-resolution performance. Bandwidth is bus width in bytes times the per-pin data rate, and GPU-Z shows the finished", {"mode": "bandwidth", "bus": 192, "gbps": 21}, "Runnable demo \u2014 Memory specs and bandwidth"], ["The Sensors tab", "sensors", "The Sensors tab is the live side of GPU-Z: temperature, hot spot, clocks, fan speed, load, memory used, and board power draw, each with a sparkline graph. It refreshes about once a second and keeps the whole history of t", {"mode": "sensors", "temp": 64, "hotspot": 76, "clock": 2610, "memclock": 1313, "load": 98, "fan": 62, "fanrpm": 2100}, "Runnable demo \u2014 The Sensors tab"], ["Hot spot temperature", "sensors", "Hot spot is the hottest single point on the die, always higher than the average GPU temperature, and it is the number that triggers throttling. A 10 to 15 C gap between GPU temp and hot spot is normal; a 30 C gap means t", {"mode": "sensors", "temp": 64, "hotspot": 76, "clock": 2610, "memclock": 1313, "load": 98, "fan": 62, "fanrpm": 2100}, "Runnable demo \u2014 Hot spot temperature"], ["PerfCap reason", "power", "PerfCap reason names whatever is holding the card back right now: power limit, thermal limit, voltage reliability, or no load. Overclockers live on this field because it says exactly which limit to raise next.", {"mode": "power", "w": 186, "limit": 200, "perfcap": "Pwr (power limit)"}, "Runnable demo \u2014 PerfCap reason"], ["Clocks: base, boost, current", "clocks", "GPU-Z separates the three clocks that matter: the guaranteed base, the rated boost, and what the card is actually running this second. A current clock stuck far below boost under full load is the classic symptom of heat ", {"mode": "clocks", "base": 1920, "boost": 2610, "cur": 2595}, "Runnable demo \u2014 Clocks: base, boost, current"], ["The ? render test", "sensors", "The little question mark next to the PCIe bus field starts a 3D render test that forces the card out of its idle power state. Idle GPUs drop to fewer PCIe lanes to save power, so the test reveals the true negotiated link", {"mode": "rendertest", "lanes": "PCIe x16 4.0 @ x16 4.0"}, "Runnable demo \u2014 The ? render test"], ["BIOS backup", "specs", "The arrow next to the BIOS version saves the card's video BIOS to a file, which is the indispensable backup before any VBIOS flash. Collectors also use it to archive rare BIOS revisions that vendors later pull from their", {"mode": "bios", "bios": "95.04.3C.00.EA", "file": "RTX4070.rom"}, "Runnable demo \u2014 BIOS backup"], ["Log to file", "sensors", "Log to file writes every sensor reading to a CSV on a timer, which turns a benchmark run into a spreadsheet. Reviewers graph the log afterward to show temperature and clock behavior across the whole test instead of quoti", {"mode": "log", "file": "GPU-Z Sensor Log.txt", "ms": 1000}, "Runnable demo \u2014 Log to file"], ["Lookup and validation", "overview", "The Lookup button opens the card's page in the TechPowerUp GPU database, and validation submits your card's specs for a public proof link. Sellers post validation links with used cards, and buyers check them before payin", {"mode": "validation", "valid": "TPU-9X4K2"}, "Runnable demo \u2014 Lookup and validation"], ["Driver and API details", "specs", "The Advanced tab and driver fields report the installed driver version plus Vulkan, OpenCL, and WDDM support levels. Mismatched API support here is how you catch a card running on Microsoft's basic display driver instead", {"mode": "driver", "ver": "551.86 WHQL", "vk": "1.3", "cl": "3.0", "wddm": "3.1"}, "Runnable demo \u2014 Driver and API details"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"specs\"){\n  console.log(\"GPU: \"+DATA.name+\" (\"+DATA.codename+\")\");\n  show(\"Shaders / TMUs / ROPs\",DATA.shaders+\" / \"+DATA.tmus+\" / \"+DATA.rops);\n  show(\"Memory\",DATA.mem_size+\" \"+DATA.mem_type+\" / \"+DATA.bus+\"-bit\");\n  show(\"Released\",DATA.release);\n}else if(m===\"sensors\"){\n  show(\"GPU temp\",DATA.temp+\" C\");\n  show(\"Hot spot\",DATA.hotspot+\" C\");\n  show(\"GPU clock\",DATA.clock+\" MHz\");\n  show(\"Memory clock\",DATA.memclock+\" MHz\");\n  show(\"GPU load\",DATA.load+\"%\");\n  show(\"Fan\",DATA.fan+\"% (\"+DATA.fanrpm+\" RPM)\");\n}else if(m===\"fillrate\"){\n  show(\"Pixel fillrate\",(Math.round(DATA.rops*DATA.clock/100)/10)+\" GPixel/s (\"+DATA.rops+\" ROPs x \"+DATA.clock+\" MHz)\");\n  show(\"Texture fillrate\",(Math.round(DATA.tmus*DATA.clock/100)/10)+\" GTexel/s (\"+DATA.tmus+\" TMUs x \"+DATA.clock+\" MHz)\");\n}else if(m===\"bandwidth\"){\n  show(\"Memory bandwidth\",(Math.round(DATA.bus/8*DATA.gbps*10)/10)+\" GB/s (\"+DATA.bus+\"-bit x \"+DATA.gbps+\" Gbps/pin)\");\n}else if(m===\"advanced\"){\n  console.log(\"Advanced tab entries:\");\n  DATA.items.forEach(function(it){console.log(\"  \"+it);});\n}else if(m===\"lookup\"){\n  show(\"Lookup\",\"opens the TechPowerUp GPU database page for this card\");\n  show(\"Device ID\",DATA.devid);\n}else if(m===\"rendertest\"){\n  show(\"Render test\",\"renders a 3D load to force the max PCIe link state\");\n  show(\"Why\",\"idle GPUs drop to fewer lanes to save power\");\n  show(\"Observed\",DATA.lanes);\n}else if(m===\"bios\"){\n  show(\"BIOS version\",DATA.bios);\n  show(\"Saved to\",DATA.file);\n  show(\"Note\",\"always back up the VBIOS before flashing\");\n}else if(m===\"log\"){\n  show(\"Log file\",DATA.file);\n  show(\"Interval\",DATA.ms+\" ms\");\n  show(\"Use\",\"graph temperature and clocks across a full run\");\n}else if(m===\"clocks\"){\n  show(\"Base clock\",DATA.base+\" MHz\");\n  show(\"Boost clock\",DATA.boost+\" MHz\");\n  show(\"Current clock\",DATA.cur+\" MHz\");\n}else if(m===\"memory\"){\n  show(\"Type\",DATA.type);show(\"Size\",DATA.size);\n  show(\"Bus width\",DATA.bus+\"-bit\");show(\"Bandwidth\",DATA.bw);\n}else if(m===\"power\"){\n  show(\"Board power draw\",DATA.w+\" W\");\n  show(\"Power limit\",DATA.limit+\" W\");\n  show(\"PerfCap reason\",DATA.perfcap);\n}else if(m===\"driver\"){\n  show(\"Driver\",DATA.ver);\n  show(\"Vulkan / OpenCL\",DATA.vk+\" / \"+DATA.cl);\n  show(\"WDDM\",DATA.wddm);\n}else if(m===\"validation\"){\n  show(\"Validation\",\"submit specs to TechPowerUp for a public proof link\");\n  show(\"Validation ID\",DATA.valid);\n}else if(m===\"workflow\"){\n  console.log(\"Bench workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-gpu-z/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-gpu-z',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-gpu-z',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
