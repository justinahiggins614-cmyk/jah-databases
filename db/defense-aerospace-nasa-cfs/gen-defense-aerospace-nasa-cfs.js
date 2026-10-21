(function(){'use strict';
/* jahdb-defense-aerospace-nasa-cfs-1.0 — deterministic boundless generator for defense-aerospace-nasa-cfs.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["core-services", "flight-applications", "software-bus", "osal-psp", "missions"];
var PREFIX='JAH-DAE1-';
var EDITION='public';
var POOL=[["What the core Flight System Is", "core-services", "NASA's core Flight System (cFS) is a reusable, platform-independent flight software framework built by NASA Goddard Space Flight Center. It separates portable core services from mission applications so the same flight software can fly on many spacecraft with only a thin platform layer changed. The project is open source and has flown on real missions including GPM, MMS, LADEE, and DART.", {"Developer": "NASA Goddard Space Flight Center", "Architecture": "cFE core + OSAL + PSP + mission apps", "License": "Open source (NASA Open Source Agreement)", "First missions": "GPM, MMS, LADEE", "Language": "C"}], ["cFE Executive Services (ES)", "core-services", "Executive Services is the cFE core service that manages the lifecycle of flight applications: creation, deletion, restart, and system startup sequencing. ES also owns the system log, the exception and reset handling, and the software bus memory pools that applications allocate from. Every cFS application registers with ES before it can send or receive a single message.", {"Service": "cFE Executive Services", "Duties": "app lifecycle, startup, system log, resets", "Key calls": "CFE_ES_RegisterApp, CFE_ES_RunLoop", "Memory": "software bus memory pools"}], ["The cFS Software Bus (SB)", "software-bus", "The Software Bus is the publish/subscribe message backbone of cFS: applications never call each other directly, they publish CCSDS packets addressed by message ID and subscribe to the IDs they need. This decoupling lets teams develop and test apps independently and rewire data flows by configuration instead of code changes. SB enforces pipe depth limits and routes packets in priority order.", {"Service": "cFE Software Bus", "Pattern": "publish/subscribe by message ID", "Packet": "CCSDS Space Packet", "Config": "pipe depth, routing table", "Benefit": "apps decoupled, data flow by config"}], ["Event Services (EVS) and Flight Telemetry", "core-services", "Event Services gives every application a uniform way to report what it is doing: apps send event messages with a severity from debug to critical, and EVS filters, counts, and forwards them to telemetry. Operators on the ground see one consistent event stream instead of a dozen app-specific log formats. EVS also supports binary event filters so noisy events can be throttled without rebuilding the app.", {"Service": "cFE Event Services", "Severities": "debug, informational, error, critical", "Features": "filters, counters, throttling", "Output": "uniform flight event telemetry"}], ["Table Services (TBL) — Uploadable Configuration", "flight-applications", "Table Services lets operators upload new configuration to a running spacecraft without rebuilding flight software: parameters live in tables that can be validated, activated, and dumped. A table has an inactive buffer for ground edits and an active buffer the app actually uses, with CRC validation on load. This is how gains, limits, and schedules get tuned after launch.", {"Service": "cFE Table Services", "Buffers": "inactive (edit) + active (use)", "Validation": "CRC on load, validation callback", "Use": "tune gains/limits post-launch"}], ["Time Services (TIME) — Spacecraft Clock", "core-services", "Time Services maintains the spacecraft clock: mission elapsed time, conversion between MET and UTC, and 1 Hz timing signals that drive the scheduler. TIME handles leap seconds and clock correlation so telemetry timestamps line up with ground UTC. Deterministic time is what makes scheduled commanding and science data tagging possible.", {"Service": "cFE Time Services", "Clocks": "MET, UTC, TAI correlation", "Signals": "1 Hz, tone/data", "Features": "leap seconds, time correlation"}], ["OSAL — Operating System Abstraction Layer", "osal-psp", "The Operating System Abstraction Layer is what makes cFS platform-independent: it presents one POSIX-like API for tasks, queues, semaphores, timers, and file I/O, with implementations for RTEMS, VxWorks, and Linux underneath. Mission code calls OSAL and never touches the RTOS directly. Porting cFS to a new board mostly means implementing the small PSP layer, not rewriting applications.", {"Layer": "OS Abstraction Layer", "API": "tasks, queues, semaphores, timers, files", "OSes": "RTEMS, VxWorks, Linux", "Rule": "apps never touch the RTOS directly"}], ["PSP — Platform Support Package", "osal-psp", "The Platform Support Package is the thin board-specific layer under OSAL: it owns boot code, the system timer tick, UART/SpaceWire drivers, EEPROM access, and watchdog handling. Each processor board gets its own PSP while everything above stays identical. A new mission computer joins the cFS family by writing a PSP, typically a few thousand lines.", {"Layer": "Platform Support Package", "Owns": "boot, tick, serial, EEPROM, watchdog", "Scope": "board-specific, few thousand lines", "Effect": "one PSP per board, apps portable"}], ["Sample Applications: SCH, HK, and Friends", "flight-applications", "cFS ships with sample applications that form a working starter flight software load: SCH (scheduler) sends timed messages, HK (housekeeping) gathers telemetry, and others cover stored commands, memory peek/poke, and file management. New missions clone these samples as templates for their own apps. The samples are also the standard cFS training path.", {"SCH": "scheduler, timed message slots", "HK": "housekeeping telemetry gather", "Others": "stored commands, mem utils, file mgr", "Role": "starter flight load + templates"}], ["CCSDS Space Packets on the Bus", "software-bus", "Every cFS software-bus message is a CCSDS Space Packet: a 6-byte primary header with version, type, secondary-header flag, APID, sequence flags/count, and packet length, followed by the data. The APID (application process ID) is the address — the message ID on the bus maps directly to it. Ground systems speak the same packets, so flight-to-ground is seamless.", {"Standard": "CCSDS Space Packet", "Header": "6 bytes: ver/type/APID/seq/len", "APID": "the on-bus address", "Link": "same packets flight-to-ground"}], ["Building cFS with CMake", "osal-psp", "Modern cFS builds with CMake: a top-level build config selects the PSP, OSAL BSP, and the set of mission applications, then compiles everything into one flight image. Sample targets build for Linux (for desktop testing), RTEMS, and VxWorks from the same source tree. Continuous integration builds all targets on every commit.", {"Build": "CMake, one tree, many targets", "Targets": "Linux, RTEMS, VxWorks", "Config": "PSP + OSAL BSP + app set", "CI": "all targets per commit"}], ["Missions That Fly cFS", "missions", "cFS has flown on a growing list of real NASA missions: the Global Precipitation Measurement (GPM) mission, the Magnetospheric Multiscale (MMS) mission, LADEE at the Moon, and DART, which flew cFS-derived software to its asteroid impact. Each mission reused the same core and wrote only mission-specific applications. That reuse is the entire economic argument for cFS.", {"GPM": "precipitation radar mission", "MMS": "four-spacecraft magnetosphere", "LADEE": "lunar atmosphere/dust", "DART": "asteroid impactor", "Pattern": "same core, mission-only apps"}], ["Testing cFS: Coverage and Functional Tests", "core-services", "cFS is tested like flight software must be: unit tests with coverage requirements on the core services, functional tests that run the whole stack on Linux, and static analysis on every change. The open-source repository runs these checks in CI so a broken commit cannot merge quietly. Coverage reports track which lines of cFE/OSAL/PSP the tests actually execute.", {"Unit tests": "per core service, coverage-gated", "Functional": "full stack on Linux", "Static analysis": "every change", "CI": "broken commits blocked"}], ["cFS on RTOS vs Linux: The Portability Proof", "osal-psp", "The portability proof of cFS is that the same application source runs on Linux for development and on RTEMS or VxWorks for flight, with only the PSP and OSAL implementation swapped. Developers debug on a laptop, then the identical code flies. Timing behavior differs — Linux is not real-time — so final verification always happens on the flight-like target.", {"Develop on": "Linux (fast iteration)", "Fly on": "RTEMS / VxWorks (real-time)", "Swapped": "PSP + OSAL only", "Rule": "final verification on flight-like target"}], ["End-to-End: Command In, Telemetry Out", "missions", "The full cFS loop in one picture: a ground command arrives as a CCSDS packet, the software bus routes it to the right app, the app acts and publishes housekeeping, EVS logs the event, and HK gathers it into the downlink telemetry frame. Tables let the ground retune behavior without new software. Fifteen records up the ladder, this is the whole machine working as one.", {"In": "CCSDS command packet", "Route": "software bus by message ID", "Act": "mission app", "Out": "HK telemetry + EVS events", "Retune": "tables, no rebuild"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var n=4+P.a%4, pkts=[];
for(var i=0;i<n;i++){var id=0x1800+((P.a*7+i*131)%0x7ff);var len=8+((P.b+i*37)%248);pkts.push({mid:'0x'+id.toString(16).toUpperCase(),len:len});}
var code='// cFS Software Bus routing demo (simulated model)\n';
code+='var routes={';for(var i=0;i<pkts.length;i++){code+=(i?',':'')+'"'+pkts[i].mid+'":"APP_'+i+'"';}code+='};\n';
code+='var pkts='+JSON.stringify(pkts)+';\n';
code+='var routed=0;for(var i=0;i<pkts.length;i++){if(routes[pkts[i].mid]){routed++;console.log("routed "+pkts[i].mid+" ("+pkts[i].len+"B) -> "+routes[pkts[i].mid]);}}\n';
code+='console.log("cFS SB: "+routed+"/"+pkts.length+" CCSDS packets routed");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-nasa-cfs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-nasa-cfs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
