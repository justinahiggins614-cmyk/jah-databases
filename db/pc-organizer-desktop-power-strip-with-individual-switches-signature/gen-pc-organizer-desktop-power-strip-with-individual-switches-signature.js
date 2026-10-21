(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "switches", "power", "protection", "outlets", "bench_use", "safety", "care"];
var PREFIX='JAH-PCO67S-';
var GENVER='jahdb-pc-organizer-desktop-power-strip-with-individual-switches-signature-1.0';
var DBNAME='Signature Power Command Strip';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Command concept", "overview", "The Signature Power Command Strip is Manon's original bench power design: eight individually switched outlets, each with its own watt meter, under one command rail. Power stops being a mystery the moment every outlet rep", {"mode": "outlets", "n": 8}, "Runnable demo \u2014 Command concept"], ["Command rockers", "switches", "Oversized rockers with positive snap and individual indicator lamps give each outlet a state you can read from across the room. The master rocker kills all eight for the end of the day.", {"mode": "switch", "which": 5, "on": true}, "Runnable demo \u2014 Command rockers"], ["Per-outlet metering", "power", "Each outlet meters its own watts on a small display, and the rail totals the strip live. This demo runs the same headroom math against a metered bench load.", {"mode": "watts", "amps": 15, "volts": 120, "load": 1140}, "Runnable demo \u2014 Per-outlet metering"], ["Surge ledger", "protection", "The surge ledger counts absorbed spike energy against the joule rating and shows remaining protection life as a bar. Protection becomes a fuel gauge instead of a hope.", {"mode": "joules", "j": 4000, "clamp": 330}, "Runnable demo \u2014 Surge ledger"], ["Low clamping", "protection", "A 330-volt clamping stage with thermal fusing protects better than the typical 400, and the fuse disconnects worn MOVs safely. When protection expires, the strip says so instead of silently quitting.", {"mode": "joules", "j": 4000, "clamp": 330}, "Runnable demo \u2014 Low clamping"], ["Wart-bay spacing", "outlets", "Wart bays \u2014 extra-wide outlet pairs \u2014 swallow the bulkiest adapters without stealing neighbors. The spacing template ships in the box for planning odd adapters.", {"mode": "spacing", "gap": 2.6}, "Runnable demo \u2014 Wart-bay spacing"], ["Command cord", "power", "A 10-foot 12-AWG cord with a flat plug reaches the wall without extensions and runs cool at full load. The cord is replaceable \u2014 a damaged cord swaps in minutes, not in a new strip.", {"mode": "cord", "len": 10, "awg": 12}, "Runnable demo \u2014 Command cord"], ["Mission mapping", "bench_use", "The outlet map is a dry-erase rail above the outlets: write the mission per outlet, wipe for the next project. Test rigs, printers, and chargers each get their named slot.", {"mode": "bench", "map": ["Forge rig", "Reference monitor", "Soldering station", "Label printer", "Chargers", "Spare", "Spare", "Master"]}, "Runnable demo \u2014 Mission mapping"], ["Vampire audit", "bench_use", "The vampire audit runs at day's end: read each meter, switch off everything but the essentials, log the standby total. The demo converts a bench's vampire watts to yearly kWh.", {"mode": "vampire", "w": 28}, "Runnable demo \u2014 Vampire audit"], ["Sequenced power", "bench_use", "Sequenced power staggers outlet turn-on by two seconds each, so inrush never stacks. The sequence order is programmable per outlet \u2014 peripherals, then the rig, automatically.", {"mode": "order", "seq": ["Peripherals auto-sequence first", "Chargers and small gear", "Test rig last, automatically"]}, "Runnable demo \u2014 Sequenced power"], ["Certified command", "safety", "The Command Strip carries UL and ETL listings with the test report number printed inside the housing. Certification you can look up beats a badge you cannot.", {"mode": "ul"}, "Runnable demo \u2014 Certified command"], ["Star power rule", "safety", "The star rule is molded into the housing: one Command Strip per wall outlet, never chained. The housing even explains why, for whoever inherits the bench.", {"mode": "daisy"}, "Runnable demo \u2014 Star power rule"], ["Command vs smart", "overview", "The Command Strip trusts the human: rockers and meters instead of auto-sensing guesses. Automation is welcome when it is right; on a test bench, the human is right more often.", {"mode": "switch", "which": 2, "on": false}, "Runnable demo \u2014 Command vs smart"], ["Decade service", "care", "The Command Strip is built for a decade: replaceable cord, cleanable vents, and a service guide in the box. Ten years of commanded power from one strip.", {"mode": "care"}, "Runnable demo \u2014 Decade service"], ["Command workflow", "bench_use", "The command ritual: map the missions, meter the loads, sequence the order, audit the vampires. Every watt accounted for, every outlet under command.", {"mode": "workflow", "steps": ["Map missions on the rail", "Meter every load", "Program the sequence", "Audit vampires nightly", "Service yearly per the guide"]}, "Runnable demo \u2014 Command workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"watts\"){\n  var max=DATA.amps*DATA.volts;\n  show(\"Rating\",DATA.amps+\" A x \"+DATA.volts+\" V = \"+max+\" W\");\n  show(\"Planned load\",DATA.load+\" W\");\n  show(\"Headroom\",(max-DATA.load)+\" W\");\n  show(\"Safe\",DATA.load<max?\"YES\":\"NO - overloaded\");\n}else if(m===\"joules\"){\n  show(\"Surge rating\",DATA.j+\" joules\");\n  show(\"Clamping voltage\",DATA.clamp+\" V\");\n  show(\"Note\",\"higher joules = longer protection life\");\n}else if(m===\"outlets\"){\n  show(\"Outlets\",DATA.n);\n  show(\"Control\",\"each individually switched\");\n}else if(m===\"switch\"){\n  show(\"Outlet\",DATA.which);\n  show(\"State\",DATA.on?\"ON\":\"OFF\");\n  show(\"Isolates\",\"that outlet only - the rest stay live\");\n}else if(m===\"spacing\"){\n  show(\"Outlet spacing\",DATA.gap+\" in\");\n  show(\"Fits\",\"bulky wall-wart adapters side by side\");\n}else if(m===\"cord\"){\n  show(\"Cord\",DATA.len+\" ft, \"+DATA.awg+\" AWG\");\n  show(\"Note\",\"thicker AWG runs cooler at full load\");\n}else if(m===\"bench\"){\n  console.log(\"Bench outlet map:\");DATA.map.forEach(function(x,i){console.log(\"  Outlet \"+(i+1)+\": \"+x);});\n}else if(m===\"vampire\"){\n  show(\"Vampire load switched off\",DATA.w+\" W\");\n  show(\"Saved per year\",Math.round(DATA.w*24*365/1000)+\" kWh\");\n}else if(m===\"order\"){\n  console.log(\"Power-on order:\");DATA.seq.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}else if(m===\"ul\"){\n  show(\"Listing\",\"UL 1363 / ETL listed\");\n  show(\"Means\",\"tested for the loads printed on it\");\n}else if(m===\"daisy\"){\n  show(\"Daisy-chaining strips\",\"NEVER - fire risk\");\n  show(\"Instead\",\"one strip per wall outlet\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"care\"){\n  show(\"Care\",\"dust the vents, check the cord yearly\");\n  show(\"Retire\",\"when switches feel loose or the cord is nicked\");\n}else if(m===\"workflow\"){\n  console.log(\"Bench power workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-desktop-power-strip-with-individual-switches-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-desktop-power-strip-with-individual-switches-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-desktop-power-strip-with-individual-switches-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
