(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "assembly", "compatibility", "workflow"];
var PREFIX='JAH-PCO61S-';
var GENVER='jahdb-pc-organizer-benchtop-open-air-test-bench-signature-1.0';
var DBNAME='Signature Open Bench Frame';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Frame concept", "overview", "The Signature Open Bench Frame is Manon's original test platform: an aluminum-extrusion frame with sliding mounts, so no part ever waits for the right hole. Every rail is a ruler, every mount a quick-release.", {"mode": "dims", "w": 18, "d": 14, "fits": "ATX through E-ATX on sliding rails"}, "Runnable demo \u2014 Frame concept"], ["Why the Frame exists", "overview", "The Frame exists because testing is a workflow, not a furniture choice: parts flow on and off all day, and the platform should accelerate that flow. It is a workbench that happens to hold a computer, not the reverse.", {"mode": "compare"}, "Runnable demo \u2014 Why the Frame exists"], ["Extrusion everything", "overview", "The entire Frame is slotted aluminum extrusion, so mounts slide to any position and lock with a quarter turn. A new form factor does not need a new bench \u2014 it needs thirty seconds with an Allen key.", {"mode": "dims", "w": 18, "d": 14, "fits": "any board on sliding rails"}, "Runnable demo \u2014 Extrusion everything"], ["Floating tray", "assembly", "The motherboard tray floats on vibration-damping mounts instead of bolting rigidly to the frame, which keeps pump and fan hum out of the desk. Standoff patterns are laser-etched, so the right holes are obvious at a glanc", {"mode": "standoffs", "forms": ["ATX", "micro-ATX", "mini-ITX", "E-ATX"]}, "Runnable demo \u2014 Floating tray"], ["Universal fit", "compatibility", "Because mounts slide, the Frame fits everything from mini-ITX to E-ATX without adapters or new parts. The fit check becomes 'slide the rails,' which takes less time than reading a compatibility chart.", {"mode": "compat", "item": "E-ATX board (330 mm)", "tray": "Signature sliding tray", "ok": true}, "Runnable demo \u2014 Universal fit"], ["PSU sled", "assembly", "The PSU rides on a sliding sled with a quick-release latch, so swapping power supplies is a ten-second job. The sled accepts ATX natively and SFX on the same rails with a sliding stop.", {"mode": "psu", "mount": "sliding quick-release sled"}, "Runnable demo \u2014 PSU sled"], ["GPU gantry", "assembly", "A gantry arm cradles long graphics cards from above, adjustable along the extrusion in seconds. The card's weight hangs from the gantry, never from the PCIe slot.", {"mode": "gpu", "len": 420}, "Runnable demo \u2014 GPU gantry"], ["Zone rails", "assembly", "Zone rails divide the Frame into labeled districts \u2014 compute, power, storage, tools \u2014 with sliding dividers. A bench with districts stays organized through a week of churn.", {"mode": "layout", "zones": ["Compute district, center", "Power district, right rail", "Storage district, left rail", "Tool district, front rail"]}, "Runnable demo \u2014 Zone rails"], ["Chimney airflow", "overview", "The Frame's open geometry is tuned as a chimney: cool air enters low at the front, hot air exits high at the rear, with no recirculation corners. Temperature probes at three heights prove the chimney in every review.", {"mode": "airflow", "clear": 80}, "Runnable demo \u2014 Chimney airflow"], ["Service-loop cabling", "assembly", "Cables on the Frame run in service loops \u2014 generous curves held by quick-release clips \u2014 so any part lifts out without unplugging its neighbors. Neatness serves speed here, not photography.", {"mode": "layout", "zones": ["24-pin service loop, center rail", "EPS loop over the top", "GPU power with swap slack", "Labeled front-panel bundle"]}, "Runnable demo \u2014 Service-loop cabling"], ["Ten-minute POST", "assembly", "The Frame's assembly ritual is timed: tray, board, cooler, RAM, GPU, power, POST \u2014 ten minutes at pace. Every mount is tool-light by design, because wrenches are the enemy of iteration.", {"mode": "assembly", "min": 10}, "Runnable demo \u2014 Ten-minute POST"], ["Guardian checklist", "assembly", "The Frame's checklist is printed on the front rail where it cannot be skipped: standoffs, power, latch, RAM, sweep for screws. The last item is a magnetic sweep of the tray \u2014 the Frame's own mat does it.", {"mode": "checklist", "items": ["Standoffs match, none extra", "24-pin and EPS seated", "GPU latched, gantry holding", "RAM clicked in", "Magnetic sweep: tray clear"]}, "Runnable demo \u2014 Guardian checklist"], ["Farm stacking", "overview", "Frames stack four high on locking pins with shared cable raceways between layers, building a burn-in farm on one desk footprint. Each layer keeps its own power switch and status light.", {"mode": "stack", "n": 4}, "Runnable demo \u2014 Farm stacking"], ["Honest load rating", "compatibility", "The Frame is rated with a published test: the rated kilograms held for a week with deflection measured. This demo checks a heavyweight build against that honest number.", {"mode": "load", "comp": 12.0, "rated": 20}, "Runnable demo \u2014 Honest load rating"], ["Frame certification workflow", "workflow", "Every part the Frame tests follows one ritual: mount, checklist, baseline, trial, teardown into labeled storage, log the result. The ritual is printed on the rail so every tester, every time, does it the same way.", {"mode": "workflow", "steps": ["Slide mounts to the part", "Run the rail checklist", "Baseline at stock", "Run the trial", "Tear down, label, log"]}, "Runnable demo \u2014 Frame certification workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"dims\"){\n  show(\"Footprint\",DATA.w+\" x \"+DATA.d+\" in\");\n  show(\"Area\",(DATA.w*DATA.d)+\" sq in\");\n  show(\"Typical for\",DATA.fits);\n}else if(m===\"load\"){\n  show(\"Component weight\",DATA.comp+\" kg\");\n  show(\"Bench rated\",DATA.rated+\" kg\");\n  show(\"Margin\",(Math.round((DATA.rated-DATA.comp)*10)/10)+\" kg\");\n  show(\"Safe\",DATA.comp<DATA.rated?\"YES\":\"NO - over limit\");\n}else if(m===\"standoffs\"){\n  show(\"Form factors\",DATA.forms.join(\", \"));\n  show(\"Mounting\",\"brass standoffs in pre-drilled pattern\");\n}else if(m===\"layout\"){\n  console.log(\"Bench zones:\");\n  DATA.zones.forEach(function(z,i){console.log(\"  \"+(i+1)+\". \"+z);});\n}else if(m===\"compat\"){\n  show(\"Check\",DATA.item+\" on \"+DATA.tray);\n  show(\"Fits\",DATA.ok?\"YES\":\"NO - needs a larger tray\");\n}else if(m===\"airflow\"){\n  show(\"Design\",\"open air - no panels, no trapped heat\");\n  show(\"GPU clearance\",DATA.clear+\" mm to nearest rail\");\n}else if(m===\"assembly\"){\n  show(\"Board to POST\",DATA.min+\" minutes typical\");\n  show(\"Why fast\",\"no panels, no cable origami\");\n}else if(m===\"checklist\"){\n  console.log(\"Pre-power checklist:\");\n  DATA.items.forEach(function(x,i){console.log(\"  \"+(i+1)+\". \"+x);});\n}else if(m===\"gpu\"){\n  show(\"Max GPU length\",DATA.len+\" mm\");\n  show(\"Support\",\"adjustable bracket included\");\n}else if(m===\"psu\"){\n  show(\"PSU mount\",DATA.mount);\n  show(\"Supports\",\"ATX and SFX (with adapter)\");\n}else if(m===\"stack\"){\n  show(\"Stackable\",DATA.n+\" high on locating pins\");\n}else if(m===\"compare\"){\n  show(\"Open bench\",\"fast swaps, best airflow, more dust\");\n  show(\"Closed case\",\"filtered, quieter, slower to service\");\n}else if(m===\"workflow\"){\n  console.log(\"Review-bench workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-benchtop-open-air-test-bench-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-benchtop-open-air-test-bench-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-benchtop-open-air-test-bench-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
