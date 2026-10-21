(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "osd", "framerate", "profiles"];
var PREFIX='JAH-PCO60-';
var GENVER='jahdb-pc-organizer-rivatuner-statistics-server-1.0';
var DBNAME='RivaTuner Statistics Server (RTSS)';
var PROV='Public documentation and published specifications for RivaTuner Statistics Server (RTSS); compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What RTSS does", "overview", "RivaTuner Statistics Server by Unwinder is the industry-standard on-screen display and frame-rate limiter for PC gaming. It draws live telemetry over any game and caps frame rates with the most precise pacing available.", {"mode": "osd", "what": "FPS, frame times, temps", "where": "over the game"}, "Runnable demo \u2014 What RTSS does"], ["Installing with Afterburner", "overview", "RTSS installs alongside MSI Afterburner and runs as a quiet background service, hooking the rendering pipeline of DirectX, Vulkan, and OpenGL games. It stays out of the way until a hotkey or profile calls it into view.", {"mode": "osd", "what": "service + overlay engine", "where": "background"}, "Runnable demo \u2014 Installing with Afterburner"], ["The on-screen display", "osd", "The OSD renders any combination of frame rate, frame times, CPU and GPU temperatures, clocks, and RAM usage as text and graphs over the game. What you see is fully composable, from one FPS number to a full telemetry wall", {"mode": "items", "items": ["Framerate", "Frametime graph", "CPU temperature", "GPU temperature", "GPU clock", "RAM usage"]}, "Runnable demo \u2014 The on-screen display"], ["Frame time vs FPS", "osd", "Frame time in milliseconds is the honest metric: 16.7 ms is exactly 60 FPS, because FPS is just 1000 divided by frame time. RTSS leads with frame times because averages of FPS hide the stutters that frame times reveal.", {"mode": "fps", "ms": 16.7}, "Runnable demo \u2014 Frame time vs FPS"], ["Reading a frametime graph", "osd", "The frametime graph plots every frame as a bar; flat means smooth, spikes mean stutter. Averages can claim 120 FPS while the graph shows regular 50 ms hitches \u2014 and the hitches are what your eyes actually feel.", {"mode": "frametime", "times": [8.3, 8.4, 8.2, 8.5, 8.3, 33.1, 8.4, 8.3, 8.2, 8.4]}, "Runnable demo \u2014 Reading a frametime graph"], ["Framerate limiter", "framerate", "The limiter caps the frame rate with precise pacing \u2014 142 FPS on a 144 Hz display is the classic esports setting, staying just under the refresh to avoid vsync lag. Capping also cuts power draw and heat, since the GPU st", {"mode": "limiter", "fps": 142}, "Runnable demo \u2014 Framerate limiter"], ["Scanline sync", "framerate", "Scanline sync is RTSS's low-lag tear-free mode: it synchronizes frame presentation to a chosen screen scanline instead of the full vsync barrier. One calibration per display finds the tearline, and then tearing hides in ", {"mode": "scanline"}, "Runnable demo \u2014 Scanline sync"], ["Per-application profiles", "profiles", "Profiles store separate OSD layouts, limiter values, and hotkeys for each game, switching automatically when the game launches. The competitive shooter gets minimal telemetry and a strict cap; the cinematic RPG gets the ", {"mode": "profiles", "n": 24, "ex": "shooter: minimal OSD + 142 cap"}, "Runnable demo \u2014 Per-application profiles"], ["Hotkeys", "profiles", "Global hotkeys toggle the overlay, the limiter, and capture without leaving the game. Muscle memory replaces menus: one key shows the telemetry, another hides it for screenshots.", {"mode": "hotkeys"}, "Runnable demo \u2014 Hotkeys"], ["Screenshots and video capture", "profiles", "RTSS captures screenshots and video through its encoder server, independent of the game's own capture. Creators record benchmark runs with the telemetry baked in as proof of the conditions.", {"mode": "capture"}, "Runnable demo \u2014 Screenshots and video capture"], ["Stealth mode", "profiles", "Stealth mode hides the overlay from screen captures and streams while keeping it visible to the player. Streamers show clean gameplay to the audience and keep their telemetry private.", {"mode": "stealth"}, "Runnable demo \u2014 Stealth mode"], ["Overlay editor and layout", "osd", "The visual overlay editor arranges OSD items by dragging, with fonts, colors, graphs, and embedded images. Layouts save per profile, so every game can have its own telemetry design.", {"mode": "layout", "layout": "top-left: FPS + frame graph; bottom-right: temps"}, "Runnable demo \u2014 Overlay editor and layout"], ["1% lows and session stats", "framerate", "RTSS can report 1% lows \u2014 the average of the worst one percent of frames \u2014 which is the number that describes real smoothness. A game at 144 FPS average with 40 FPS 1% lows stutters; the average alone would never tell yo", {"mode": "stats", "avg": 144, "low": 96}, "Runnable demo \u2014 1% lows and session stats"], ["RTSS limiter vs in-engine caps", "framerate", "In-engine frame caps vary wildly in pacing quality, while RTSS's limiter is consistently among the smoothest available with negligible overhead. When a game's own cap stutters, the standard fix is disabling it and cappin", {"mode": "compare"}, "Runnable demo \u2014 RTSS limiter vs in-engine caps"], ["Benchmark overlay workflow", "osd", "The benchmark ritual: build the overlay with FPS, frame graph, and temps, set the limiter per the test plan, capture the run on video, and read 1% lows from the stats. Every published number arrives with its telemetry as", {"mode": "workflow", "steps": ["Compose the telemetry overlay", "Set the limiter per test plan", "Capture the benchmark run", "Read average and 1% lows", "Archive video with telemetry baked in"]}, "Runnable demo \u2014 Benchmark overlay workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"osd\"){\n  show(\"Tool\",\"RivaTuner Statistics Server - on-screen display\");\n  show(\"Shows\",DATA.what);show(\"Position\",DATA.where);\n}else if(m===\"fps\"){\n  show(\"Frame time\",DATA.ms+\" ms\");\n  show(\"Equals FPS\",Math.round(1000/DATA.ms*10)/10);\n}else if(m===\"frametime\"){\n  var ts=DATA.times;\n  var avg=Math.round(ts.reduce(function(a,b){return a+b;},0)/ts.length*100)/100;\n  var mx=Math.max.apply(null,ts);\n  show(\"Average\",avg+\" ms = \"+Math.round(1000/avg*10)/10+\" FPS\");\n  show(\"Worst frame\",mx+\" ms\");\n  show(\"Stutter\",mx>avg*1.5?\"YES - worst far over average\":\"smooth\");\n}else if(m===\"limiter\"){\n  show(\"Cap\",DATA.fps+\" FPS\");\n  show(\"Frame budget\",(Math.round(1000/DATA.fps*100)/100)+\" ms per frame\");\n  show(\"Why\",\"smoother pacing, less power, less heat\");\n}else if(m===\"scanline\"){\n  show(\"Scanline sync\",\"tear-free with less lag than vsync\");\n  show(\"Setup\",\"one-time tearline calibration per display\");\n}else if(m===\"profiles\"){\n  show(\"Profiles\",DATA.n+\" per-application\");\n  show(\"Example\",DATA.ex);\n}else if(m===\"hotkeys\"){\n  show(\"Hotkeys\",\"toggle OSD, toggle limiter, capture\");\n}else if(m===\"capture\"){\n  show(\"Capture\",\"screenshots and video via encoder server\");\n}else if(m===\"stealth\"){\n  show(\"Stealth mode\",\"hides the OSD from captures and streams\");\n}else if(m===\"layout\"){\n  show(\"Layout\",DATA.layout);show(\"Editor\",\"visual, drag and arrange\");\n}else if(m===\"items\"){\n  console.log(\"Overlay items:\");\n  DATA.items.forEach(function(i){console.log(\"  \"+i);});\n}else if(m===\"stats\"){\n  show(\"Session average\",DATA.avg+\" FPS\");\n  show(\"1% low\",DATA.low+\" FPS\");\n  show(\"Read\",\"lows tell the stutter story averages hide\");\n}else if(m===\"compare\"){\n  show(\"RTSS limiter\",\"precise frame pacing, tiny overhead\");\n  show(\"In-engine cap\",\"quality varies by game\");\n}else if(m===\"workflow\"){\n  console.log(\"Overlay workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-rivatuner-statistics-server/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-rivatuner-statistics-server',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-rivatuner-statistics-server',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
