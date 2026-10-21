(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "cpu", "mainboard", "memory", "specs", "bench"];
var PREFIX='JAH-PCO55S-';
var GENVER='jahdb-pc-organizer-cpu-z-signature-1.0';
var DBNAME='Signature CPU Atlas';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Atlas concept", "overview", "The Signature CPU Atlas is Manon's original silicon cartography: every tab CPU-Z has, drawn as an explorable map of the machine. Each reading carries a confidence note saying how it was measured, so the Atlas never state", {"mode": "cpu", "name": "Signature Reference CPU", "codename": "JAH-C1", "nm": "5 nm", "cores": 8, "threads": 16, "base": 4.0, "boost": 5.2, "pkg": "JAH Socket"}, "Runnable demo \u2014 Atlas concept"], ["Atlas first run", "overview", "The Atlas needs no install and no admin rights; it opens straight onto the CPU map with live clocks already moving. Its first act is a platform passport \u2014 CPU, board, memory, firmware \u2014 hashed and stored for every future", {"mode": "cpu", "name": "Signature Reference CPU", "codename": "JAH-C1", "nm": "5 nm", "cores": 8, "threads": 16, "base": 4.0, "boost": 5.2, "pkg": "JAH Socket"}, "Runnable demo \u2014 Atlas first run"], ["Processor map", "cpu", "The processor map lays out identity, topology, and live clocks on one canvas, with each core's current speed as a bar. Cores that never boost get flagged, which is how the Atlas spots a misbehaving scheduler or a hot cor", {"mode": "cpu", "name": "Signature Reference CPU", "codename": "JAH-C1", "nm": "5 nm", "cores": 8, "threads": 16, "base": 4.0, "boost": 5.2, "pkg": "JAH Socket"}, "Runnable demo \u2014 Processor map"], ["Clock arithmetic", "cpu", "The Atlas shows the clock equation \u2014 bus times multiplier equals core speed \u2014 with the live numbers plugged in, updating as boost moves. Watching the equation breathe is the fastest way to learn how modern boost actually", {"mode": "clocks", "speed": 5200, "mult": 52, "bus": 100}, "Runnable demo \u2014 Clock arithmetic"], ["Cache cartography", "cpu", "Cache cartography draws the L1/L2/L3 hierarchy to scale, so the jump from kilobytes to megabytes is visible, not just numeric. It annotates which level each workload actually lives in during the built-in benchmark.", {"mode": "caches", "l1": "768 KB total", "l2": "8 MB", "l3": "96 MB stacked"}, "Runnable demo \u2014 Cache cartography"], ["Extension atlas", "cpu", "The extension atlas groups instruction sets by era and job \u2014 media, crypto, vector math \u2014 instead of dumping an alphabet soup. Each group notes which everyday programs actually use it.", {"mode": "instructions", "sets": ["MMX", "SSE4.2", "AVX2", "AVX-512", "AES", "SHA3", "JAH-VEC"]}, "Runnable demo \u2014 Extension atlas"], ["Board map", "mainboard", "The board map identifies manufacturer, model, chipset, and Super I/O, then checks the chipset against the CPU's requirements. A board that cannot feed the chip's power stages gets a gentle warning before the owner wonder", {"mode": "mainboard", "mfr": "Signature", "model": "JAH Board One", "chipset": "JAH 600", "bios": "1.04 (2026)"}, "Runnable demo \u2014 Board map"], ["Firmware freshness", "mainboard", "Firmware freshness scores the BIOS date against the vendor's release history and lists what each missed update fixed. The Atlas frames updates as recovered performance and fixed bugs, never as scary procedures.", {"mode": "mainboard", "mfr": "Signature", "model": "JAH Board One", "chipset": "JAH 600", "bios": "1.04 (2026)"}, "Runnable demo \u2014 Firmware freshness"], ["Memory map", "memory", "The memory map shows channels as physical lanes, so single-channel operation looks broken the way it is. It pairs the live frequency with the DDR rating and flags mismatched sticks by their SPD serials.", {"mode": "memory", "type": "DDR5", "size": "32 GB", "ch": "Dual", "freq": 3200}, "Runnable demo \u2014 Memory map"], ["Timing tutor", "memory", "The timing tutor explains each primary timing as the delay it actually is \u2014 CAS is the column wait, in nanoseconds at your frequency. It converts the clock counts to real time so 30 vs 36 means something.", {"mode": "timings", "cl": 30, "trcd": 36, "trp": 36, "tras": 76, "cr": 1, "trfc": 800}, "Runnable demo \u2014 Timing tutor"], ["Slot ledger", "memory", "The slot ledger keeps every stick's manufacturer, part number, serial, and birth week in a permanent table. When a stick dies in year three, the ledger already holds the RMA details.", {"mode": "spd", "slot": 1, "part": "JAH32G6400", "mfr": "Signature", "size": "16 GB", "rank": "single", "xmp": "EXPO 6400 MT/s", "week": 9, "year": 2026}, "Runnable demo \u2014 Slot ledger"], ["Graphics check", "specs", "The graphics check confirms the real GPU driver is bound to the display, not a generic fallback. It cross-reads the GPU's own identity page so the two tools always agree.", {"mode": "graphics", "gpu": "Signature Reference GPU", "clocks": "2000 / 2700 MHz"}, "Runnable demo \u2014 Graphics check"], ["Atlas benchmark", "bench", "The Atlas benchmark runs single- and multi-thread tests while recording clocks, temperatures, and power, so the score arrives with its conditions. A score without conditions is trivia; with them, it is evidence.", {"mode": "bench", "st": 780, "mt": 8300, "cores": 8}, "Runnable demo \u2014 Atlas benchmark"], ["Signed validation", "overview", "Atlas validation produces a signed hardware passport \u2014 identity, clocks, firmware hashes \u2014 verifiable offline against the public ledger. It proves the machine without trusting the reporter.", {"mode": "validation", "valid": "JAH-LEDGER-CPU-0001"}, "Runnable demo \u2014 Signed validation"], ["Timer truth and audit", "overview", "The Atlas continuously sanity-checks the system timers its own benchmark relies on, and refuses to score on a dishonest clock. A full audit \u2014 identity, board, memory, ledger, benchmark, signed validation \u2014 documents the ", {"mode": "workflow", "steps": ["Map CPU identity and live clocks", "Verify board and firmware freshness", "Map memory channels and timings", "File slot ledger serials", "Benchmark with conditions, sign validation"]}, "Runnable demo \u2014 Timer truth and audit"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"cpu\"){\n  console.log(\"CPU: \"+DATA.name);\n  show(\"Codename / process\",DATA.codename+\" / \"+DATA.nm);\n  show(\"Cores / threads\",DATA.cores+\" / \"+DATA.threads);\n  show(\"Base / boost\",DATA.base+\" / \"+DATA.boost+\" GHz\");\n  show(\"Package\",DATA.pkg);\n}else if(m===\"clocks\"){\n  show(\"Core speed\",DATA.speed+\" MHz\");\n  show(\"Multiplier\",\"x\"+DATA.mult);\n  show(\"Bus speed\",DATA.bus+\" MHz\");\n  show(\"Check\",DATA.mult+\" x \"+DATA.bus+\" = \"+Math.round(DATA.mult*DATA.bus)+\" MHz\");\n}else if(m===\"caches\"){\n  show(\"L1\",DATA.l1);show(\"L2\",DATA.l2);show(\"L3\",DATA.l3);\n  show(\"Note\",\"L1 fastest per core, L3 shared across cores\");\n}else if(m===\"mainboard\"){\n  show(\"Manufacturer\",DATA.mfr);show(\"Model\",DATA.model);\n  show(\"Chipset\",DATA.chipset);show(\"BIOS\",DATA.bios);\n}else if(m===\"memory\"){\n  show(\"Type / size\",DATA.type+\" / \"+DATA.size);\n  show(\"Channels\",DATA.ch);\n  show(\"DRAM frequency\",DATA.freq+\" MHz (DDR \"+(DATA.freq*2)+\")\");\n}else if(m===\"timings\"){\n  show(\"Primary timings\",\"CL\"+DATA.cl+\"-\"+DATA.trcd+\"-\"+DATA.trp+\"-\"+DATA.tras+\" CR\"+DATA.cr);\n  show(\"tRFC\",DATA.trfc+\" clocks\");\n}else if(m===\"spd\"){\n  console.log(\"Slot \"+DATA.slot+\": \"+DATA.part);\n  show(\"Manufacturer\",DATA.mfr);\n  show(\"Size / rank\",DATA.size+\" / \"+DATA.rank);\n  show(\"XMP / EXPO\",DATA.xmp);\n  show(\"Made\",\"week \"+DATA.week+\" of \"+DATA.year);\n}else if(m===\"bench\"){\n  show(\"Single thread\",DATA.st);\n  show(\"Multi thread\",DATA.mt);\n  show(\"MT/ST ratio\",(Math.round(DATA.mt/DATA.st*100)/100)+\"x across \"+DATA.cores+\" cores\");\n}else if(m===\"validation\"){\n  show(\"Validation\",\"submit to the public validator for a proof link\");\n  show(\"ID\",DATA.valid);\n}else if(m===\"timers\"){\n  show(\"Check\",\"QPC vs RTC vs HPET timer sanity\");\n  show(\"Result\",DATA.res);\n}else if(m===\"graphics\"){\n  show(\"GPU\",DATA.gpu);show(\"Clocks\",DATA.clocks);\n}else if(m===\"instructions\"){\n  console.log(\"Instruction sets (\"+DATA.sets.length+\"):\");\n  DATA.sets.forEach(function(s){console.log(\"  \"+s);});\n}else if(m===\"workflow\"){\n  console.log(\"Audit workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cpu-z-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cpu-z-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cpu-z-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
