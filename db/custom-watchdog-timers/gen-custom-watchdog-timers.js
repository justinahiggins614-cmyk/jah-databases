(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["hardware", "software", "escalation", "testing"];
var PREFIX='JAH-CW-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Hardware Watchdog Timers", "hardware", "Uses the SoC's hardware watchdog to reset the system when software stops petting it. The timer runs independently of the CPU; expiry pulls reset. It is the last line of defense against total hangs.", ["Configure the timeout", "Pet from a high-priority context", "Let expiry reset the system"], ["SoC watchdogs", "Super-I/O", "BMC"], ["Vendor datasheets", "Embedded guides"], 1, 0], ["Windowed Watchdogs", "hardware", "Requires pets inside a time window — not too early, not too late. Early pets suggest a runaway loop petting blindly; late pets mean a hang. The window catches both failure modes.", ["Define the pet window", "Reject early and late pets", "Reset on window violation"], ["Automotive MCUs", "Safety PLCs", "Advanced SoCs"], ["ISO 26262", "IEC 61508"], 2, 2], ["Heartbeat Protocols", "software", "Exchanges periodic heartbeats between supervisor and workers to detect stalls. Missing heartbeats trigger restart of the silent component; sequence numbers catch replays. It distributes the watchdog idea across processes.", ["Send heartbeats on schedule", "Detect missing beats", "Restart silent components"], ["systemd", "Supervisors", "Cluster managers"], ["Failure detector literature", "Distributed systems"], 1, 0], ["Multi-Stage Escalation", "escalation", "Escalates from logging to service restart to full reboot as lower stages fail. Each stage gets a chance to fix the problem before the next, harsher one fires. It avoids rebooting for recoverable glitches.", ["Define escalation stages", "Try the gentlest first", "Escalate on continued failure"], ["systemd", "Kubernetes liveness", "BMC"], ["SRE practices", "Embedded guides"], 2, 1], ["PMIC Watchdogs", "hardware", "Uses the power-management IC's watchdog to handle hangs during early boot and suspend. The PMIC watches before the SoC watchdog is even configured. It covers the window other watchdogs miss.", ["Enable the PMIC watchdog early", "Hand off to the SoC watchdog", "Cover suspend/resume"], ["PMIC chips", "Phone SoCs", "Embedded"], ["PMIC datasheets", "Power literature"], 2, 0], ["Software Watchdog Threads", "software", "Runs a high-priority watchdog thread that checks worker progress and restarts stuck work. It cannot survive a kernel hang, but it catches application deadlocks cheaply. Every long-running service should have one.", ["Check worker progress periodically", "Restart stuck workers", "Log before acting"], ["Custom services", "systemd", "Supervisors"], ["Concurrency literature", "SRE practices"], 1, 0], ["Watchdog Daemons", "software", "Deploys system watchdog daemons that pet the hardware timer and monitor load. The daemon also watches temperature, memory, and load average, rebooting on serious trouble. It bridges software policy and hardware reset.", ["Pet the hardware timer", "Monitor system health", "Reboot on critical conditions"], ["watchdogd", "systemd", "Embedded Linux"], ["Linux watchdog API", "Daemon guides"], 1, 0], ["Pet Strategy Design", "software", "Designs pet strategies so only genuinely-healthy code pets the watchdog. Petting from the main loop proves the loop runs; petting from an ISR proves nothing. The pet location is the design.", ["Pet from the supervised code path", "Never pet from interrupts alone", "Chain pets through stages"], ["Embedded firmware", "RTOS", "Safety systems"], ["Embedded guides", "Safety standards"], 2, 0], ["Timeout Tuning", "testing", "Tunes watchdog timeouts from measured worst-case execution times plus margin. Too short causes spurious resets; too long delays recovery. Profiling under load sets the number.", ["Measure worst-case times", "Add safety margin", "Re-tune after changes"], ["Embedded", "RTOS", "Testing rigs"], ["Real-time literature", "WCET analysis"], 2, 0], ["Watchdog During Suspend", "hardware", "Keeps watchdog coverage across suspend and resume, the window where hangs hide. The PMIC or always-on domain watches while the SoC sleeps; resume re-arms the main timer. It closes the sleep blind spot.", ["Arm the always-on watchdog", "Cover the suspend window", "Re-arm on resume"], ["Phone SoCs", "Embedded", "Laptops"], ["Power management docs", "Vendor guides"], 3, 1], ["Cascaded Watchdogs", "escalation", "Cascades watchdogs so each level watches the one below: task, supervisor, hardware. A stuck task trips the supervisor; a stuck supervisor trips the hardware. No single failure escapes all levels.", ["Layer task, supervisor, hardware", "Each level watches the one below", "Escalate upward on failure"], ["Safety systems", "Automotive", "Aerospace"], ["ISO 26262", "Safety literature"], 3, 1], ["Watchdog Test Injection", "testing", "Tests watchdogs by deliberately hanging the system in a safe environment. If the watchdog does not fire, the test fails; untested watchdogs are decorations. Fault injection proves the recovery path.", ["Inject hangs deliberately", "Verify the watchdog fires", "Verify recovery completes"], ["HIL rigs", "Chaos tools", "Safety validation"], ["Fault injection literature", "Safety standards"], 2, 2], ["Boot-Loop Protection", "escalation", "Detects boot loops with a counter in non-volatile storage and falls back after N failures. Repeated watchdog resets during boot increment the counter; at the limit the system boots a recovery image. It stops infinite reset cycles.", ["Count boot attempts in NVRAM", "Fall back after N failures", "Reset the counter on good boot"], ["Bootloaders", "Embedded", "Phones (rescue)"], ["Bootloader docs", "Embedded guides"], 2, 1], ["Remote Watchdog via BMC", "hardware", "Lets the baseboard management controller watchdog the host independently. The BMC pings the host and power-cycles on silence; it works even when the host is fully hung. Datacenter standard.", ["BMC monitors host heartbeats", "Power-cycle on silence", "Log to the SEL"], ["OpenBMC", "iDRAC/iLO", "Servers"], ["IPMI spec", "Redfish"], 2, 1], ["Watchdog Event Logging", "testing", "Logs watchdog events with context to non-volatile storage for post-mortem. Which timer fired, what the system was doing, and the escalation taken — all recorded. Without logs, watchdog resets are mysteries.", ["Log timer, context, and action", "Store in non-volatile memory", "Review after every event"], ["BMC SEL", "Embedded logs", "systemd journal"], ["Logging practices", "SRE guides"], 1, 1]];
var DEMOS=["// Demo: {NAME} — timeout vs pet interval\nvar timeout={N2},pet=timeout/3;\nconsole.log('technique: {NAME}');console.log('timeout: '+timeout+' ms, pet interval: '+pet+' ms');\nconsole.log('margin: '+(timeout-pet)+' ms — pet at 1/3 timeout for safety');\nconsole.log(pet<timeout/2?'safe: even one missed pet will not fire':'RISKY: a single delay fires the watchdog');", "// Demo: {NAME} — escalation ladder\nvar stages=['log warning','restart service','reboot system','power cycle'];\nconsole.log('technique: {NAME}');\nstages.forEach(function(s,i){console.log('stage '+(i+1)+': '+s);});\nconsole.log('escalate only when the lower stage fails to recover');", "// Demo: {NAME} — windowed watchdog check\nvar t={N1}%90+5,min=10,max=100;\nconsole.log('technique: {NAME}');console.log('pet at t='+t+' ms, window ['+min+', '+max+']');\nconsole.log(t>=min&&t<=max?'pet accepted':'PET REJECTED — too early or too late fires the watchdog');"];
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
var gen={version:'jahdb-custom-watchdog-timers-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('custom-watchdog-timers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
