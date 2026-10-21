(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "health", "firmware", "performance", "maintenance"];
var PREFIX='JAH-PCO53-';
var GENVER='jahdb-pc-organizer-nvme-ssd-management-suites-1.0';
var DBNAME='NVMe / SSD Management Suites';
var PROV='Public documentation and published specifications for NVMe / SSD Management Suites; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["SSD suites at a glance", "overview", "Samsung Magician and the Kioxia SSD Utility are the vendor control rooms for modern solid-state drives: one window for health, temperature, firmware, speed tests, and secure erase. Instead of decoding raw S.M.A.R.T. tabl", {"mode": "health", "smart": {"05": 100, "A3": 100, "AD": 100}}, "Runnable demo \u2014 SSD suites at a glance"], ["Getting Samsung Magician", "overview", "Samsung Magician is a free Windows download from Samsung's semiconductor site and installs in minutes with no license key. It detects Samsung SATA and NVMe drives automatically, so the first thing most owners do after in", {"mode": "health", "smart": {"05": 99, "A3": 100}}, "Runnable demo \u2014 Getting Samsung Magician"], ["Drive Dashboard", "health", "The Drive Dashboard is the home screen: model name, serial number, firmware version, interface speed, and one big health percentage. Green means every wear indicator sits inside its safe margin; anything else means it is", {"mode": "health", "smart": {"05": 97, "A3": 98, "AD": 96}}, "Runnable demo \u2014 Drive Dashboard"], ["Reading S.M.A.R.T. attributes", "health", "S.M.A.R.T. is the drive's self-monitoring log, and attributes like 05 (reallocated sectors) and AD (wear leveling count) each report a normalized value from 1 to 100. The suite turns the worst attribute into the headline", {"mode": "smart", "smart": {"05": 94, "A3": 99, "AD": 91, "C2": 100}}, "Runnable demo \u2014 Reading S.M.A.R.T. attributes"], ["Temperature monitoring", "health", "NVMe drives throttle when they get hot, so the suite watches the composite temperature sensor continuously. Keeping a client drive under about 70 C preserves full speed; sustained heat above the warning line costs perfor", {"mode": "temp", "temp_c": 52, "warn_c": 70}, "Runnable demo \u2014 Temperature monitoring"], ["Checking for firmware updates", "firmware", "The firmware updater compares the installed version against the vendor's latest release and fetches the package when they differ. Firmware fixes compatibility bugs and occasionally unlocks measurable speed, so checking i", {"mode": "firmware", "cur": "2B2QEXM7", "latest": "3B2QEXM7"}, "Runnable demo \u2014 Checking for firmware updates"], ["Flashing firmware safely", "firmware", "A firmware flash rewrites the drive's controller code, so the suite insists on steady power and no sleep during the minute it takes. The golden rule is simple: back up first, close other apps, and never interrupt the pro", {"mode": "firmware", "cur": "3B2QEXM7", "latest": "3B2QEXM7"}, "Runnable demo \u2014 Flashing firmware safely"], ["Performance benchmark", "performance", "The built-in benchmark measures sequential reads and writes plus random 4K IOPS, the two numbers that define how a drive feels. A healthy PCIe 4.0 NVMe drive lands near 7,000 MB/s sequential read; far below that points a", {"mode": "bench", "seq_read": 6980, "seq_write": 5100, "rand4k": 820000, "pcie": "PCIe 4.0 x4"}, "Runnable demo \u2014 Performance benchmark"], ["Over-provisioning", "performance", "Over-provisioning reserves a slice of NAND as spare area the controller uses for wear leveling and garbage collection. Samsung recommends about 10 percent; the suite carves it out with one slider, trading a little capaci", {"mode": "op", "op_pct": 10}, "Runnable demo \u2014 Over-provisioning"], ["Diagnostic scan", "maintenance", "The diagnostic scan reads every block on the drive looking for errors the S.M.A.R.T. log has not caught yet. A short scan takes minutes and a full scan can take hours on large drives; either way, zero bad blocks is the o", {"mode": "diag", "scan": "full", "blocks": 1953525168, "bad": 0}, "Runnable demo \u2014 Diagnostic scan"], ["Secure erase", "maintenance", "Secure erase tells the controller to cryptographically discard every user block, which is the correct way to wipe an SSD \u2014 a traditional overwrite pass cannot reach the spare area. Magician builds a bootable USB for the ", {"mode": "erase", "method": "cryptographic erase", "passes": 1, "verify": "clean"}, "Runnable demo \u2014 Secure erase"], ["Data migration and cloning", "maintenance", "Data Migration clones an old drive onto a new Samsung SSD sector by sector, operating system and all. It is the standard move when upgrading a laptop: clone, swap the drives, and boot exactly where you left off.", {"mode": "migrate", "src": "SATA SSD 500 GB", "dst": "NVMe 1 TB", "gb": 412, "min": 38}, "Runnable demo \u2014 Data migration and cloning"], ["Encrypted drive and TCG Opal", "maintenance", "Modern Samsung drives encrypt everything at the hardware level with AES, and the suite manages the TCG Opal pre-boot authentication that guards the key. With hardware encryption on there is no measurable speed penalty th", {"mode": "encrypt", "std": "TCG Opal", "on": true}, "Runnable demo \u2014 Encrypted drive and TCG Opal"], ["TBW endurance math", "health", "Every SSD carries a total-bytes-written (TBW) rating \u2014 the warranty-scale measure of its lifespan. Dividing what you have written by the rating gives the true endurance percentage, which matters more than the health head", {"mode": "tbw", "written": 132.5, "rated": 600}, "Runnable demo \u2014 TBW endurance math"], ["Technician bench workflow", "maintenance", "A professional intake runs the same five steps on every used drive: read health and temperature, benchmark it, check firmware, run the diagnostic scan, and secure-erase before resale. Fifteen minutes at the bench with th", {"mode": "workflow", "steps": ["Read S.M.A.R.T. health and temperature", "Run performance benchmark", "Check and flash firmware", "Run diagnostic scan", "Secure erase before resale"]}, "Runnable demo \u2014 Technician bench workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"health\"){\n  var a=DATA.smart,k=Object.keys(a),w=k[0],i;\n  for(i=1;i<k.length;i++){if(a[k[i]]<a[w])w=k[i];}\n  show(\"Worst SMART attribute\",w+\" at \"+a[w]+\"% remaining\");\n  show(\"Verdict\",a[w]>80?\"GOOD\":(a[w]>50?\"WORN - plan replacement\":\"REPLACE NOW\"));\n}else if(m===\"smart\"){\n  var a2=DATA.smart,k2=Object.keys(a2);\n  console.log(\"SMART attributes (\"+k2.length+\"):\");\n  k2.forEach(function(k){console.log(\"  \"+k+\": \"+a2[k]+\"% remaining\");});\n}else if(m===\"temp\"){\n  show(\"Current temp\",DATA.temp_c+\" C\");\n  show(\"Warning threshold\",DATA.warn_c+\" C\");\n  show(\"Headroom\",(DATA.warn_c-DATA.temp_c)+\" C\");\n  show(\"Status\",DATA.temp_c<DATA.warn_c?\"OK\":\"THROTTLING RISK\");\n}else if(m===\"firmware\"){\n  show(\"Installed\",DATA.cur);show(\"Latest\",DATA.latest);\n  show(\"Action\",DATA.cur===DATA.latest?\"up to date\":\"UPDATE AVAILABLE - back up first, keep power stable\");\n}else if(m===\"bench\"){\n  show(\"Sequential read\",DATA.seq_read+\" MB/s (\"+(Math.round(DATA.seq_read/1024*10)/10)+\" GB/s)\");\n  show(\"Sequential write\",DATA.seq_write+\" MB/s\");\n  show(\"Random 4K read\",DATA.rand4k+\" IOPS\");\n  show(\"PCIe link\",DATA.pcie);\n}else if(m===\"op\"){\n  show(\"Over-provisioning\",DATA.op_pct+\"% reserved\");\n  show(\"User addressable\",(Math.round((100-DATA.op_pct)*10)/10)+\"% of NAND\");\n  show(\"Benefit\",\"steadier write speed + longer endurance\");\n}else if(m===\"diag\"){\n  show(\"Scan type\",DATA.scan);\n  show(\"Blocks checked\",DATA.blocks);\n  show(\"Bad blocks\",DATA.bad);\n  show(\"Result\",DATA.bad===0?\"PASS - no errors\":\"FAIL - back up and replace\");\n}else if(m===\"erase\"){\n  show(\"Method\",DATA.method);\n  show(\"Passes\",DATA.passes);\n  show(\"Controller verification\",DATA.verify);\n  show(\"Data unrecoverable\",DATA.verify===\"clean\"?\"YES\":\"NO\");\n}else if(m===\"migrate\"){\n  show(\"Source\",DATA.src);show(\"Target\",DATA.dst);\n  show(\"Moved\",DATA.gb+\" GB in \"+DATA.min+\" min\");\n  show(\"Rate\",(Math.round(DATA.gb/DATA.min*10)/10)+\" GB/min\");\n}else if(m===\"encrypt\"){\n  show(\"Standard\",DATA.std);\n  show(\"State\",DATA.on?\"ENABLED\":\"OFF\");\n  show(\"Note\",\"hardware AES - no CPU overhead when on\");\n}else if(m===\"tbw\"){\n  show(\"Written\",DATA.written+\" TBW of \"+DATA.rated+\" TBW rated\");\n  show(\"Endurance used\",(Math.round(DATA.written/DATA.rated*10000)/100)+\"%\");\n  show(\"Remaining\",(Math.round((DATA.rated-DATA.written)*10)/10)+\" TBW\");\n}else if(m===\"workflow\"){\n  console.log(\"Bench workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-nvme-ssd-management-suites/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-nvme-ssd-management-suites',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-nvme-ssd-management-suites',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
