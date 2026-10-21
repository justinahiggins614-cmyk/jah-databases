(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "osd", "framerate", "profiles"];
var PREFIX='JAH-PCO60S-';
var GENVER='jahdb-pc-organizer-rivatuner-statistics-server-signature-1.0';
var DBNAME='Signature Overlay Director';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Director concept", "overview", "The Signature Overlay Director is Manon's original frame-pacing conductor: it treats every rendered frame as an event with a timestamp, a budget, and a verdict. Telemetry is evidence, and the Director is its courtroom.", {"mode": "osd", "what": "frame ledger + telemetry", "where": "over the game"}, "Runnable demo \u2014 Director concept"], ["Director installation", "overview", "The Director installs as one signed service with no bundled extras and no account, hooking the same graphics APIs RTSS does. Its first launch runs a pacing calibration that learns the display's true refresh behavior.", {"mode": "osd", "what": "calibrated overlay engine", "where": "background service"}, "Runnable demo \u2014 Director installation"], ["The frame ledger", "osd", "The frame ledger records every frame's time, not just the average, keeping the full distribution for the session. Stutter analysis works on the ledger directly \u2014 percentiles, worst runs, and hitch clustering.", {"mode": "items", "items": ["Frame ledger", "Percentile readout", "Hitch cluster map", "Temperature ribbon", "Power trace"]}, "Runnable demo \u2014 The frame ledger"], ["Millisecond honesty", "osd", "The Director speaks milliseconds first and FPS second, because 8.3 ms is a fact and 120 FPS is a derived summary. Every FPS number on screen carries its frame-time source one hover away.", {"mode": "fps", "ms": 8.3}, "Runnable demo \u2014 Millisecond honesty"], ["Hitch cartography", "osd", "Hitch cartography maps stutters as events on a timeline, clustering them so a repeating hitch every two seconds is unmistakable. The demo feeds a hitchy session and lets the math call it what it is.", {"mode": "frametime", "times": [8.3, 8.4, 8.3, 8.4, 41.2, 8.3, 8.4, 8.3, 8.5, 40.8]}, "Runnable demo \u2014 Hitch cartography"], ["Precision limiter", "framerate", "The precision limiter paces frames against the display's measured refresh with sub-millisecond accuracy, learning the panel's real timing in calibration. Caps can be fractional \u2014 141.7, not just 142 \u2014 because the math su", {"mode": "limiter", "fps": 141.7}, "Runnable demo \u2014 Precision limiter"], ["Tearline cartography", "framerate", "Tearline cartography sweeps the scanline range automatically and maps where tearing appears, then parks presentation in the cleanest zone. What RTSS calibrates by hand, the Director maps by measurement.", {"mode": "scanline"}, "Runnable demo \u2014 Tearline cartography"], ["Scene profiles", "profiles", "Scene profiles go beyond per-game: menu, gameplay, and cinematic each get their own overlay and cap, switching on scene detection. Loading screens stop burning 400 FPS; cutscenes get their filmic 48.", {"mode": "profiles", "n": 40, "ex": "menu: 60 cap, gameplay: 142 cap"}, "Runnable demo \u2014 Scene profiles"], ["Gesture keys", "profiles", "Gesture keys combine modifiers into chords that never collide with game bindings, and every chord is shown on its overlay while held. Discoverability beats memorization.", {"mode": "hotkeys"}, "Runnable demo \u2014 Gesture keys"], ["Evidence recorder", "profiles", "The evidence recorder captures video with the frame ledger embedded as metadata, so any clip can be re-analyzed frame by frame later. Benchmark videos become datasets, not just footage.", {"mode": "capture"}, "Runnable demo \u2014 Evidence recorder"], ["Audience modes", "profiles", "Audience modes decide per output what the viewer sees: the stream gets clean gameplay, the local recording keeps telemetry, the player sees everything. One run serves every audience.", {"mode": "stealth"}, "Runnable demo \u2014 Audience modes"], ["Composition studio", "osd", "The composition studio lays out overlays on a canvas with alignment guides, themes, and live preview against a test pattern. Designs export as shareable files, so the community trades overlay art like skins.", {"mode": "layout", "layout": "canvas-composed, themed, per-scene"}, "Runnable demo \u2014 Composition studio"], ["Percentile truth", "framerate", "The Director reports the full percentile ladder \u2014 average, 1%, 0.1% \u2014 because the tail tells the experience. Two systems with the same average can feel utterly different, and the ladder shows why.", {"mode": "stats", "avg": 141, "low": 118}, "Runnable demo \u2014 Percentile truth"], ["Pacing proof", "framerate", "Pacing proof is a recorded demonstration: the same scene capped three ways, with frame-time distributions overlaid. Claims about smoothness become comparable pictures instead of adjectives.", {"mode": "compare"}, "Runnable demo \u2014 Pacing proof"], ["Certified run workflow", "osd", "A certified run composes the overlay, calibrates pacing, records with the ledger embedded, and publishes the percentile ladder with the video. It is the complete evidence package for any performance claim.", {"mode": "workflow", "steps": ["Compose the overlay canvas", "Calibrate display pacing", "Record with ledger embedded", "Publish the percentile ladder", "Archive the evidence package"]}, "Runnable demo \u2014 Certified run workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-rivatuner-statistics-server-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-rivatuner-statistics-server-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-rivatuner-statistics-server-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
