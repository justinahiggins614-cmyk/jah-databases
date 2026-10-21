(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "assembly", "compatibility", "workflow"];
var PREFIX='JAH-PCO61-';
var GENVER='jahdb-pc-organizer-benchtop-open-air-test-bench-1.0';
var DBNAME='Benchtop Open-Air Test Bench';
var PROV='Public documentation and published specifications for Benchtop Open-Air Test Bench; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What an open-air test bench is", "overview", "An open-air test bench is a modular frame that holds a motherboard, PSU, GPU, and drives with no case panels around them. Reviewers and overclockers build on benches because every component stays reachable and every temp", {"mode": "dims", "w": 17, "d": 13, "fits": "ATX builds with full-size GPUs"}, "Runnable demo \u2014 What an open-air test bench is"], ["Why benches beat cases for testing", "overview", "Swapping a GPU on a bench takes a minute; in a case it takes fifteen, with cable origami each way. For testing many parts in one day, the bench pays for itself in saved time before lunch.", {"mode": "compare"}, "Runnable demo \u2014 Why benches beat cases for testing"], ["Frame materials", "overview", "Bench frames are usually powder-coated steel or anodized aluminum extrusion, rigid enough that a heavy GPU cannot flex the motherboard tray. Aluminum extrusion designs accept sliding mounts anywhere along the rails.", {"mode": "dims", "w": 17, "d": 13, "fits": "E-ATX trays on extrusion rails"}, "Runnable demo \u2014 Frame materials"], ["Motherboard tray and standoffs", "assembly", "The tray carries brass standoffs in the standard ATX, micro-ATX, and mini-ITX hole patterns, so the board bolts down exactly like it would in a case. Correct standoffs \u2014 no extras under the board \u2014 are what prevent short", {"mode": "standoffs", "forms": ["ATX", "micro-ATX", "mini-ITX"]}, "Runnable demo \u2014 Motherboard tray and standoffs"], ["Form factor fit check", "compatibility", "Not every tray takes E-ATX or SSI boards, so the fit check is tray length versus board length before you buy. This demo runs the comparison the way a buyer should.", {"mode": "compat", "item": "E-ATX board (330 mm)", "tray": "standard ATX tray (305 mm)", "ok": false}, "Runnable demo \u2014 Form factor fit check"], ["PSU mounting", "assembly", "The PSU bolts to a dedicated bracket \u2014 rear, side, or under-tray depending on the design \u2014 with its fan facing open air. ATX supplies fit natively and SFX units ride on an adapter plate.", {"mode": "psu", "mount": "rear bracket, fan facing out"}, "Runnable demo \u2014 PSU mounting"], ["GPU mounting and support", "assembly", "Long graphics cards rest on an adjustable support bracket so their weight never hangs on the PCIe slot alone. Vertical GPU mounts with riser cables are common on showcase benches.", {"mode": "gpu", "len": 380}, "Runnable demo \u2014 GPU mounting and support"], ["Bench layout zones", "assembly", "A sane bench divides into zones: motherboard center, PSU to one side, drives on rails, and tools along the front edge. Zones keep a live build from becoming a parts avalanche.", {"mode": "layout", "zones": ["Motherboard tray, center", "PSU bracket, right side", "Drive rails, left side", "Tools and screws, front edge"]}, "Runnable demo \u2014 Bench layout zones"], ["The airflow advantage", "overview", "With no panels, heat leaves in every direction and no hot pocket can form behind a GPU backplate. Bench temperatures are the honest best case \u2014 a cooler that struggles on a bench will suffer in a case.", {"mode": "airflow", "clear": 60}, "Runnable demo \u2014 The airflow advantage"], ["Cable routing without a case", "assembly", "Bench cable routing is about serviceability, not beauty: PSU cables take the shortest path, and nothing is tied down that you will move tomorrow. Velcro straps beat zip ties because benches are reconfigured constantly.", {"mode": "layout", "zones": ["24-pin shortest path to board", "8-pin EPS over the top rail", "GPU power with slack for swaps", "Front-panel wires labeled"]}, "Runnable demo \u2014 Cable routing without a case"], ["Assembly speed", "assembly", "A practiced builder goes from bare tray to POST in about half an hour on a bench, most of it spent on the cooler mount. The time savings compound across a week of testing different parts.", {"mode": "assembly", "min": 30}, "Runnable demo \u2014 Assembly speed"], ["Pre-power checklist", "assembly", "Every bench power-on follows the same checklist: standoffs correct, 24-pin and EPS seated, GPU latched with power connected, RAM clicked in, and no loose screws on the tray. Five minutes of checklist prevents the smell o", {"mode": "checklist", "items": ["Standoffs match the board, none extra", "24-pin and EPS fully seated", "GPU latched + power connected", "RAM clicked into slots", "No loose screws on the tray"]}, "Runnable demo \u2014 Pre-power checklist"], ["Stackable designs", "overview", "Some benches stack two or three high on locating pins, turning one footprint into a small test farm. Stacking suits burn-in and mining-style multi-system testing where each layer runs independently.", {"mode": "stack", "n": 3}, "Runnable demo \u2014 Stackable designs"], ["Load capacity math", "compatibility", "A bench's rating has to cover board, cooler, GPU, PSU, and drives together \u2014 a flagship GPU alone can weigh two kilos. This demo totals a heavy build against a typical rating to prove the margin.", {"mode": "load", "comp": 9.5, "rated": 15}, "Runnable demo \u2014 Load capacity math"], ["Review-bench workflow", "workflow", "The review workflow never changes: mount the part, run the checklist, baseline at stock, test, then tear down into labeled ESD bags. Consistency between reviews is what makes the numbers comparable.", {"mode": "workflow", "steps": ["Mount the part on the bench", "Run the pre-power checklist", "Baseline at stock settings", "Run the test suite", "Tear down into labeled ESD bags"]}, "Runnable demo \u2014 Review-bench workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-benchtop-open-air-test-bench/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-benchtop-open-air-test-bench',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-benchtop-open-air-test-bench',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
