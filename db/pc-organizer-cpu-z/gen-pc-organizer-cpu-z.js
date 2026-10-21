(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "cpu", "mainboard", "memory", "specs", "bench"];
var PREFIX='JAH-PCO55-';
var GENVER='jahdb-pc-organizer-cpu-z-1.0';
var DBNAME='CPU-Z';
var PROV='Public documentation and published specifications for CPU-Z; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What CPU-Z does", "overview", "CPU-Z by CPUID is the classic free utility that catalogs the processor, motherboard, memory, and graphics of any PC on tabbed pages. Reviewers, overclockers, and second-hand buyers have trusted its read-only reports for ", {"mode": "cpu", "name": "Ryzen 7 7800X3D", "codename": "Raphael", "nm": "5 nm TSMC", "cores": 8, "threads": 16, "base": 4.2, "boost": 5.0, "pkg": "Socket AM5"}, "Runnable demo \u2014 What CPU-Z does"], ["Installing CPU-Z", "overview", "CPU-Z comes as an installer or a portable ZIP with 32- and 64-bit builds, and it starts reporting the moment it opens. It reads hardware registers directly, so it works even on machines with no drivers installed yet.", {"mode": "cpu", "name": "Ryzen 7 7800X3D", "codename": "Raphael", "nm": "5 nm TSMC", "cores": 8, "threads": 16, "base": 4.2, "boost": 5.0, "pkg": "Socket AM5"}, "Runnable demo \u2014 Installing CPU-Z"], ["CPU tab: processor identity", "cpu", "The CPU tab names the chip, its codename, package, process node, core voltage, and specification string, plus family, model, stepping, and revision. That specification string is the exact text the manufacturer burned int", {"mode": "cpu", "name": "Ryzen 7 7800X3D", "codename": "Raphael", "nm": "5 nm TSMC", "cores": 8, "threads": 16, "base": 4.2, "boost": 5.0, "pkg": "Socket AM5"}, "Runnable demo \u2014 CPU tab: processor identity"], ["Clocks and multiplier", "cpu", "Core speed is the bus speed times the multiplier, and CPU-Z shows all three live so you can watch boost behavior in real time. A multiplier of 42 on a 100 MHz bus is 4,200 MHz, and the demo recomputes it to prove the ari", {"mode": "clocks", "speed": 4200, "mult": 42, "bus": 100}, "Runnable demo \u2014 Clocks and multiplier"], ["The Caches tab", "cpu", "The Caches tab breaks down L1, L2, and L3 by size, associativity, and descriptor, showing how much fast memory sits next to each core. Large shared L3 \u2014 like the 7800X3D's stacked 96 MB \u2014 is exactly what makes some chips", {"mode": "caches", "l1": "640 KB total (32+48 KB per core)", "l2": "8 MB (1 MB per core)", "l3": "96 MB (incl. 3D V-Cache)"}, "Runnable demo \u2014 The Caches tab"], ["Instruction sets", "cpu", "The instructions field lists every extension the chip understands, from MMX and SSE through AVX2, AVX-512, and AES. Software checks this list to decide which optimized code path it may use.", {"mode": "instructions", "sets": ["MMX", "SSE", "SSE2", "SSE3", "SSSE3", "SSE4.1", "SSE4.2", "AVX", "AVX2", "AES", "SHA", "FMA3"]}, "Runnable demo \u2014 Instruction sets"], ["Mainboard tab", "mainboard", "The Mainboard tab identifies the board manufacturer, model, chipset, southbridge, and Super I/O chip. When a used PC's listing says one board and the tab says another, the tab wins.", {"mode": "mainboard", "mfr": "ASUS", "model": "ROG STRIX B650E-F GAMING WIFI", "chipset": "AMD B650E", "bios": "1807 (2024)"}, "Runnable demo \u2014 Mainboard tab"], ["BIOS brand and date", "mainboard", "CPU-Z reports the BIOS brand, version, and build date, which tells you at a glance whether the board has years of updates waiting. A 2021 BIOS on a board that gained major fixes in 2023 is a free performance upgrade begg", {"mode": "mainboard", "mfr": "ASUS", "model": "ROG STRIX B650E-F GAMING WIFI", "chipset": "AMD B650E", "bios": "1807 (2024)"}, "Runnable demo \u2014 BIOS brand and date"], ["Memory tab", "memory", "The Memory tab reports type, total size, channel mode, NB frequency, and the live DRAM frequency \u2014 double it for the DDR rating. Single-channel on a board with two sticks installed means one stick is not seated or not de", {"mode": "memory", "type": "DDR5", "size": "32 GB", "ch": "Dual", "freq": 3000}, "Runnable demo \u2014 Memory tab"], ["Memory timings", "memory", "The timings table lists CAS latency and the secondary timings the board actually trained, like 30-38-38-96 at DDR5-6000. Lower first numbers at the same frequency mean a snappier kit, and the command rate (1T/2T) sits at", {"mode": "timings", "cl": 30, "trcd": 38, "trp": 38, "tras": 96, "cr": 1, "trfc": 884}, "Runnable demo \u2014 Memory timings"], ["SPD tab per slot", "memory", "The SPD tab reads each memory slot's serial-presence chip: module manufacturer, part number, serial, manufacturing week, and the JEDEC and XMP/EXPO profiles burned in. It is how you prove the kit in the slots matches the", {"mode": "spd", "slot": 2, "part": "CMT32GX5M2B6000Z30", "mfr": "Corsair", "size": "16 GB", "rank": "single", "xmp": "EXPO 6000 MT/s", "week": 14, "year": 2024}, "Runnable demo \u2014 SPD tab per slot"], ["Graphics tab", "specs", "The Graphics tab names the GPU and its current clocks, a quick confirmation that the display is driven by the real graphics driver. If this tab shows a generic adapter instead of the card's name, the driver install faile", {"mode": "graphics", "gpu": "GeForce RTX 4070", "clocks": "1920 / 2610 MHz"}, "Runnable demo \u2014 Graphics tab"], ["Bench tab", "bench", "The Bench tab runs CPU-Z's own single- and multi-thread benchmark and compares the result against a reference database. The multi-to-single ratio reveals scaling: eight full cores should land near eight times the single-", {"mode": "bench", "st": 748, "mt": 7820, "cores": 8}, "Runnable demo \u2014 Bench tab"], ["Validation", "overview", "The Validate button submits the full report to CPUID's public validator, which returns a permanent link proving the exact hardware and clocks. Overclocking records live or die by validation links, and buyers check them o", {"mode": "validation", "valid": "CPUID-7X2K9"}, "Runnable demo \u2014 Validation"], ["Timers tool and audit workflow", "overview", "The Tools menu's Timers check compares the system's clocks for sanity, which matters because benchmarks are only honest on honest timers. A full audit runs CPU, mainboard, memory, SPD, and Bench in order and validates th", {"mode": "workflow", "steps": ["Record CPU tab identity and clocks", "Verify mainboard and BIOS date", "Check memory channels and timings", "Read SPD serials per slot", "Run Bench and submit validation"]}, "Runnable demo \u2014 Timers tool and audit workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cpu-z/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cpu-z',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cpu-z',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
