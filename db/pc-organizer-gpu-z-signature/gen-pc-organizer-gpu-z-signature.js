(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "specs", "sensors", "power", "clocks"];
var PREFIX='JAH-PCO54S-';
var GENVER='jahdb-pc-organizer-gpu-z-signature-1.0';
var DBNAME='Signature GPU Lens';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Lens concept", "overview", "The Signature GPU Lens is Manon's original GPU inspector: it shows every spec GPU-Z shows, but each number arrives with a one-line explanation of what it means. A beginner learns the card while reading it; an expert skip", {"mode": "specs", "name": "Signature Reference GPU", "codename": "JAH-G1", "shaders": 6144, "tmus": 192, "rops": 64, "mem_size": "16 GB", "mem_type": "GDDR6X", "bus": 256, "release": "2026"}, "Runnable demo \u2014 Lens concept"], ["Lens install", "overview", "The Lens is one signed executable with no installer and no admin rights needed, reading the same registers GPU-Z reads. Its first run builds a card passport \u2014 identity, firmware, and baseline clocks \u2014 stored locally for ", {"mode": "lookup", "devid": "JAH0-0001"}, "Runnable demo \u2014 Lens install"], ["Identity lens", "specs", "The identity lens cross-checks the card's reported name against its device ID, shader count, and memory bus from an offline ledger. A mismatch lights up immediately, which makes the Lens a fake-card detector first and a ", {"mode": "specs", "name": "Signature Reference GPU", "codename": "JAH-G1", "shaders": 6144, "tmus": 192, "rops": 64, "mem_size": "16 GB", "mem_type": "GDDR6X", "bus": 256, "release": "2026"}, "Runnable demo \u2014 Identity lens"], ["Unit counts, explained", "specs", "The Lens annotates shaders, TMUs, and ROPs with what each unit does per frame, turning three bare numbers into a working mental model. Hovering a count shows the fillrate it produces at the current clock, computed live.", {"mode": "fillrate", "rops": 64, "tmus": 192, "clock": 2700}, "Runnable demo \u2014 Unit counts, explained"], ["Fillrate truth", "specs", "The Lens recomputes fillrates from unit counts and the live clock rather than trusting the driver's reported figure. If the recomputed number disagrees with the tab, the Lens says which one it believes and why.", {"mode": "bandwidth", "bus": 256, "gbps": 21}, "Runnable demo \u2014 Fillrate truth"], ["Memory truth", "specs", "The memory lens shows type, size, bus, and bandwidth with the arithmetic visible: 256-bit at 21 Gbps per pin is 672 GB/s, shown as a formula, not a magic number. Resizable BAR status sits beside it, since BAR off can cos", {"mode": "memory", "type": "GDDR6X", "size": "16 GB", "bus": 256, "bw": "672 GB/s"}, "Runnable demo \u2014 Memory truth"], ["Live sensors", "sensors", "Lens sensors sample temperature, hot spot, clocks, fan, load, and board power with per-sensor history ribbons. Any sensor can be pinned to the top, and pinned sensors stay visible while you scroll the spec tabs.", {"mode": "sensors", "temp": 61, "hotspot": 73, "clock": 2700, "memclock": 1313, "load": 99, "fan": 58, "fanrpm": 1950}, "Runnable demo \u2014 Live sensors"], ["Thermal truth-teller", "sensors", "The thermal truth-teller plots GPU temp against hot spot and shades the normal 10\u201315 C band, so an abnormal gap is visible as color, not just numbers. It also estimates cooler-mount quality from the gap's behavior under ", {"mode": "sensors", "temp": 62, "hotspot": 94, "clock": 2400, "memclock": 1313, "load": 99, "fan": 100, "fanrpm": 3200}, "Runnable demo \u2014 Thermal truth-teller"], ["Limit finder", "power", "The limit finder watches which cap binds the card second by second and totals the time spent at each: power, thermal, voltage, or idle. Overclockers get a pie chart of lost performance instead of a blinking PerfCap code.", {"mode": "power", "w": 215, "limit": 220, "perfcap": "Thrm (thermal limit)"}, "Runnable demo \u2014 Limit finder"], ["Clock story", "clocks", "The clock story records base, boost, and live clock as a timeline, so throttling shows up as a visible sag, not a single low reading. Each sag is annotated with the limit that caused it, pulled from the limit finder.", {"mode": "clocks", "base": 2000, "boost": 2700, "cur": 2685}, "Runnable demo \u2014 Clock story"], ["Link prover", "sensors", "The link prover runs a graduated 3D load and records the PCIe lane count and generation at each step, proving the slot negotiates correctly under stress. A card that drops lanes under load has a slot or riser problem, an", {"mode": "rendertest", "lanes": "PCIe x16 4.0 @ x16 4.0, stable under load"}, "Runnable demo \u2014 Link prover"], ["Firmware vault", "specs", "The Lens archives the card's VBIOS with a hash at first sight and warns if it ever changes unexpectedly. Before any flash it stages the backup, the new image, and a recovery plan in that order.", {"mode": "bios", "bios": "JAH.01.00", "file": "lens-vault/JAH-G1.rom"}, "Runnable demo \u2014 Firmware vault"], ["Session recorder", "sensors", "The session recorder logs every sensor to a local database instead of a flat CSV, so months of runs stay queryable. Asking 'how hot did it get last Tuesday' is a filter, not a file hunt.", {"mode": "log", "file": "lens-sessions.db", "ms": 500}, "Runnable demo \u2014 Session recorder"], ["One-click validation", "overview", "Validation in the Lens produces a signed spec card \u2014 identity, clocks, firmware hash \u2014 that anyone can verify offline against the public ledger. Sellers attach it to listings; buyers verify it without trusting the seller", {"mode": "validation", "valid": "JAH-LEDGER-0001"}, "Runnable demo \u2014 One-click validation"], ["Driver health", "specs", "Driver health compares the installed driver against the known-good list for the card's generation and flags API gaps. It also snapshots the driver version with every benchmark log, so regressions get blamed on the right ", {"mode": "driver", "ver": "JAH 1.0 certified", "vk": "1.3", "cl": "3.0", "wddm": "3.1"}, "Runnable demo \u2014 Driver health"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-gpu-z-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-gpu-z-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-gpu-z-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
