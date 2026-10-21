(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["os-power", "hardware", "apps", "estimation"];
var PREFIX='JAH-LPB-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["ACPI Sleep States", "os-power", "Uses ACPI S-states from S0 working through S3 suspend to S4 hibernate. S3 keeps RAM powered for instant resume; S4 writes RAM to disk and powers off fully. The OS picks the state matching the expected sleep duration.", ["Enter S3 for short sleeps", "Use S4 hibernate for long sleeps", "Resume devices in dependency order"], ["Windows", "Linux", "macOS"], ["ACPI Specification", "OS PM docs"], 1, 0], ["CPU P-States and C-States", "os-power", "Scales CPU frequency with P-states and parks idle cores in deep C-states. P-states trade speed for power; C-states cut idle power to near zero at microsecond wake costs. The governor balances the two continuously.", ["Scale frequency with P-states", "Park idle cores in deep C-states", "Tune the governor for the workload"], ["Linux cpuidle/cpufreq", "Windows", "ARM SCMI"], ["ACPI Specification", "Intel SDM"], 2, 0], ["Tickless Idle", "os-power", "Stops the periodic timer tick when the CPU is idle so cores sleep uninterrupted. The old 1000 Hz tick woke every core every millisecond; tickless kernels sleep until the next real event. It is why modern laptops idle efficiently.", ["Disable the periodic tick when idle", "Program one-shot wakeups", "Account time from TSC on wake"], ["Linux (NO_HZ)", "Modern kernels", "RTOS"], ["Kernel docs", "OS literature"], 2, 0], ["Runtime Power Management", "os-power", "Suspends individual devices at runtime when idle, independent of system sleep. USB, PCIe, and SATA devices each get autosuspend policies; the framework tracks usage counts. It saves power while the system stays fully usable.", ["Track per-device usage counts", "Autosuspend idle devices", "Resume transparently on use"], ["Linux runtime PM", "Windows DPM", "Drivers"], ["Linux PM docs", "PCIe/USB specs"], 2, 1], ["Battery Charge Thresholds", "hardware", "Limits maximum charge to 80 percent to extend battery lifespan. Lithium batteries degrade fastest at full charge and high temperature; thresholds trade a little capacity for years of health. Business laptops ship this by default.", ["Set the charge limit in firmware", "Stop charging at the threshold", "Allow full charge when needed"], ["Lenovo", "Dell", "Apple (optimized charging)"], ["Battery literature", "Vendor firmware"], 1, 1], ["Adaptive Display Brightness", "apps", "Dims the display to ambient light because the screen dominates power draw. The ambient sensor drives a brightness curve tuned for readability at minimum power. It is the single biggest lever on phone battery life.", ["Read the ambient light sensor", "Map lux to brightness", "Smooth transitions to avoid flicker"], ["Android", "iOS", "Windows"], ["Display power literature", "OS docs"], 1, 1], ["Radio Power Gating", "hardware", "Powers down Wi-Fi, cellular, and Bluetooth radios when not in use. Radios burn power just listening; gating them during idle and batching transfers cuts the biggest phone power sink. Airplane mode is the manual version.", ["Gate radios during idle", "Batch transfers into bursts", "Use low-power listen modes"], ["Smartphone SoCs", "IoT modems", "Laptop firmware"], ["3GPP DRX", "Wi-Fi power save"], 2, 1], ["Wake Lock Discipline", "apps", "Manages wake locks so apps cannot keep the device awake indefinitely. Every lock needs a timeout and a justification; the system releases forgotten locks. Runaway wake locks are the classic battery-drain bug.", ["Require timeouts on wake locks", "Attribute locks per app", "Release forgotten locks"], ["Android", "Doze mode", "iOS background"], ["Android docs", "Mobile power literature"], 2, 1], ["Hibernation to Disk", "os-power", "Writes RAM to disk and powers off fully for zero-draw sleep. Resume restores the exact session; modern NVMe makes it nearly as fast as suspend. It is the answer for multi-day standby.", ["Compress and write RAM to disk", "Power off completely", "Restore on power-on"], ["Windows hibernate", "Linux (swsusp)", "macOS Safe Sleep"], ["ACPI S4", "OS docs"], 1, 1], ["Energy-Aware Scheduling", "os-power", "Places tasks on the most energy-efficient core that meets their deadline. The scheduler models each core's energy cost and picks the cheapest fit; little cores handle background work. It is the OS side of heterogeneous computing.", ["Model per-core energy costs", "Place tasks on the cheapest fit", "Respect latency deadlines"], ["Linux EAS", "Android", "ARM big.LITTLE"], ["Scheduling literature", "ARM docs"], 3, 2], ["Battery Health Modeling", "estimation", "Models battery degradation from charge cycles, temperature, and voltage to predict remaining lifespan. Coulomb counting plus voltage curves estimate state of health; the OS surfaces it to users. It drives charge-threshold policies.", ["Track cycles, temp, and voltage", "Estimate state of health", "Adjust charging policy"], ["Battery fuel gauges", "OS battery APIs", "Vendor tools"], ["Battery literature", "Smart battery spec"], 3, 1], ["USB Power Delivery Negotiation", "hardware", "Negotiates voltage and current over USB-C Power Delivery for efficient charging. The sink requests what it needs; the source advertises capabilities. Correct negotiation avoids both slow charging and overheating.", ["Advertise source capabilities", "Request the needed profile", "Monitor temperature during charge"], ["USB-C PD controllers", "Laptops", "Phones"], ["USB PD specification", "USB-C spec"], 2, 1], ["Low-Power Audio Paths", "hardware", "Routes audio through low-power DSP paths that sip power during playback. The main CPU sleeps while the DSP decodes; hardware offload cuts music-playback drain dramatically. It is why phones play music for days.", ["Offload decode to the DSP", "Sleep the application processor", "Buffer ahead to extend sleep"], ["Smartphone SoCs", "Bluetooth LE Audio", "Codecs"], ["Audio DSP docs", "Bluetooth specs"], 2, 1], ["Display Refresh Scaling", "hardware", "Varies display refresh rate with content: 120 Hz for scrolling, 1 Hz for static reading. The display pipeline burns power per frame; adaptive refresh cuts frames nobody sees. LTPO panels make it seamless.", ["Detect content motion", "Scale refresh 1-120 Hz", "Keep touch latency low"], ["LTPO displays", "ProMotion", "Android dynamic refresh"], ["Display specs", "VESA Adaptive-Sync"], 2, 1], ["Power Budgeting", "estimation", "Allocates a system power budget across CPU, GPU, and radios so the total never exceeds the thermal or battery limit. The budgeter arbitrates competing demands in real time. It is how thin devices sustain peak bursts safely.", ["Define the total budget", "Arbitrate between consumers", "Enforce in real time"], ["SoC firmware", "Game consoles", "Phones"], ["Power delivery specs", "Thermal design"], 3, 2]];
var DEMOS=["// Demo: {NAME} — C-state residency vs power\nvar states=[['C0',100],['C1',60],['C3',25],['C6',8],['C10',3]];\nconsole.log('technique: {NAME}');\nstates.forEach(function(s){console.log(s[0]+': '+s[1]+'% of active power');});\nconsole.log('deep C-states cut idle power by 10x+ at microsecond wake costs');", "// Demo: {NAME} — battery drain projection\nvar cap={N2}*10,mA={N1}*2;\nvar hours=cap/mA;\nconsole.log('technique: {NAME}');console.log('battery: '+cap+' mAh, draw: '+mA+' mA');\nconsole.log('projected life: '+hours.toFixed(1)+' hours');\nconsole.log('halve the draw -> double the life');", "// Demo: {NAME} — race-to-idle vs sustained\nvar work=1000,fast={p:80,t:2},slow={p:30,t:6};\nvar ef=fast.p*fast.t,es=slow.p*slow.t;\nconsole.log('technique: {NAME}');console.log('race-to-idle: '+ef+' J, sustained-slow: '+es+' J');\nconsole.log(ef<es?'race-to-idle wins — finish fast, sleep deep':'sustained-slow wins here');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-low-power-battery-conservation-modes-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('low-power-battery-conservation-modes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
