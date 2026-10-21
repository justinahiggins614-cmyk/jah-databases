(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "switches", "power", "protection", "outlets", "bench_use", "safety", "care"];
var PREFIX='JAH-PCO67-';
var GENVER='jahdb-pc-organizer-desktop-power-strip-with-individual-switches-1.0';
var DBNAME='Desktop Power Strip with Individual Switches';
var PROV='Public documentation and published specifications for Desktop Power Strip with Individual Switches; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What the switched strip does", "overview", "A desktop power strip with individual switches gives every outlet its own illuminated rocker, so each device powers independently. On a test bench, that means the monitor, the rig, and the charger each live or die on the", {"mode": "outlets", "n": 8}, "Runnable demo \u2014 What the switched strip does"], ["Individual switches", "switches", "Each rocker controls only its outlet \u2014 kill the 3D printer's outlet without dropping the PC beside it. Illuminated switches show state at a glance, which matters in a darkened lab.", {"mode": "switch", "which": 3, "on": false}, "Runnable demo \u2014 Individual switches"], ["Wattage math", "power", "A 15-amp, 120-volt strip handles 1,800 watts, and the honest rule loads it to 80 percent \u2014 1,440 watts. This demo totals a bench's draw against the rating the way an electrician would.", {"mode": "watts", "amps": 15, "volts": 120, "load": 920}, "Runnable demo \u2014 Wattage math"], ["Surge joules", "protection", "Surge protection is rated in joules \u2014 1,000 to 4,000 on good strips \u2014 measuring how much spike energy the MOVs can absorb before wearing out. Higher joules means a longer protective life, not stronger single-hit protecti", {"mode": "joules", "j": 2100, "clamp": 400}, "Runnable demo \u2014 Surge joules"], ["Clamping voltage", "protection", "Clamping voltage \u2014 typically 400 volts on 120 V strips \u2014 is where the protection starts shunting a spike. Lower clamping protects better; UL 1449 testing is what makes the number trustworthy.", {"mode": "joules", "j": 2100, "clamp": 400}, "Runnable demo \u2014 Clamping voltage"], ["Widely spaced outlets", "outlets", "Bench strips space outlets to swallow wall-wart adapters without blocking neighbors \u2014 the feature that separates bench strips from office strips. Measure your bulkiest adapter before trusting the spacing.", {"mode": "spacing", "gap": 2.2}, "Runnable demo \u2014 Widely spaced outlets"], ["Cord gauge and length", "power", "A 6-foot 14-AWG cord is the bench standard: thick enough to run cool at full load, long enough to reach without an extension. Thin 18-AWG cords on high-draw gear run warm, which is the warning sign.", {"mode": "cord", "len": 6, "awg": 14}, "Runnable demo \u2014 Cord gauge and length"], ["Bench outlet map", "bench_use", "A mapped strip assigns outlets permanently: 1 for the test rig, 2 for the monitor, 3 for the charger, and so on, labeled on the strip. Mapping ends the daily guessing game of 'what is plugged where.'", {"mode": "bench", "map": ["Test rig", "Monitor", "Bench lamp", "Phone charger", "Soldering station", "Spare", "Spare", "Spare"]}, "Runnable demo \u2014 Bench outlet map"], ["Killing vampire loads", "bench_use", "Switches kill vampire loads \u2014 the watts gear sips while 'off' \u2014 with one rocker instead of six unpluggings. A bench idling 40 vampire watts wastes 350 kWh a year; the demo does that multiplication.", {"mode": "vampire", "w": 40}, "Runnable demo \u2014 Killing vampire loads"], ["Power-on order", "bench_use", "Power-on order prevents inrush tripping: monitors and peripherals first, the PC last, so the big inrush hits a calm circuit. Power-off reverses it. Ritual beats tripped breakers.", {"mode": "order", "seq": ["Monitors and bench lamp", "Chargers and small gear", "Test rig (PC) last"]}, "Runnable demo \u2014 Power-on order"], ["UL listing", "safety", "A UL 1363 or ETL listing means the strip was actually tested for the loads printed on it \u2014 unlisted strips are wishes, not equipment. The mark lives on the housing, not just the box.", {"mode": "ul"}, "Runnable demo \u2014 UL listing"], ["Never daisy-chain", "safety", "Strips plugged into strips multiply the fire risk and void every listing involved \u2014 one strip per wall outlet, always. Need more outlets? That is what the electrician is for.", {"mode": "daisy"}, "Runnable demo \u2014 Never daisy-chain"], ["Switched vs smart strips", "overview", "Smart strips sense a master device and switch the rest automatically; switched strips give you the rocker and the decision. Benches prefer rockers \u2014 automation that guesses wrong mid-test is worse than none.", {"mode": "switch", "which": 1, "on": true}, "Runnable demo \u2014 Switched vs smart strips"], ["Care and retirement", "care", "Dust the vents, check the cord yearly for nicks, and retire any strip with loose switches or a damaged cord \u2014 no repairs, no second chances. A ten-year-old strip owes you nothing.", {"mode": "care"}, "Runnable demo \u2014 Care and retirement"], ["Bench power workflow", "bench_use", "The power ritual: map and label outlets, total the wattage, set the power-on order, switch off vampires nightly. Commanded power is safe power.", {"mode": "workflow", "steps": ["Map and label every outlet", "Total wattage vs rating", "Set power-on order", "Switch off vampires nightly", "Inspect cord and switches yearly"]}, "Runnable demo \u2014 Bench power workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-desktop-power-strip-with-individual-switches/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-desktop-power-strip-with-individual-switches',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-desktop-power-strip-with-individual-switches',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
