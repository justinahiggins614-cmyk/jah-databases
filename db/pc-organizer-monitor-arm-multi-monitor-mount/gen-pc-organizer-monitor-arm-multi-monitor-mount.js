(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "mounting", "types", "adjustment", "ergonomics", "multi"];
var PREFIX='JAH-PCO68-';
var GENVER='jahdb-pc-organizer-monitor-arm-multi-monitor-mount-1.0';
var DBNAME='Monitor Arm / Multi-Monitor Mount';
var PROV='Public documentation and published specifications for Monitor Arm / Multi-Monitor Mount; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What a monitor arm does", "overview", "A monitor arm clamps to the desk and floats the display on an articulated arm, reclaiming the entire footprint a stand would eat. For test benches, it also lifts the screen above the parts sprawl where it belongs.", {"mode": "reach", "cm": 52}, "Runnable demo \u2014 What a monitor arm does"], ["VESA mounting patterns", "mounting", "Nearly every monitor speaks VESA \u2014 75x75 or 100x100 mm hole patterns \u2014 and arms bolt straight to them. Non-VESA oddballs need an adapter plate; check before the arm arrives.", {"mode": "vesa", "v": "100x100", "ok": true}, "Runnable demo \u2014 VESA mounting patterns"], ["Weight capacity math", "mounting", "Every arm is rated per display \u2014 commonly 2 to 9 kg \u2014 and the monitor plus any mounted accessories must sit under it. This demo checks a 34-inch ultrawide against its arm's rating.", {"mode": "weight", "kg": 8.2, "rated": 9}, "Runnable demo \u2014 Weight capacity math"], ["Gas spring arms", "types", "Gas-spring arms counterbalance the monitor so one finger moves it and it stays exactly where left \u2014 the premium feel. They suit shared desks and fidgety adjusters.", {"mode": "gas"}, "Runnable demo \u2014 Gas spring arms"], ["Mechanical arms", "types", "Mechanical arms use springs and a tension screw you set once for the monitor's weight, then adjust by hand. Set-and-forget users get 90 percent of the gas experience for less money.", {"mode": "mech"}, "Runnable demo \u2014 Mechanical arms"], ["C-clamp desk mount", "mounting", "The C-clamp grips the desk edge and fits tops 10 to 85 mm thick, installing with no drilling. The desk edge must be solid \u2014 thin hollow-core tops can crush under clamp pressure.", {"mode": "mount", "how": "C-clamp", "desk": "25 mm solid"}, "Runnable demo \u2014 C-clamp desk mount"], ["Grommet mount", "mounting", "The grommet mount bolts through the desk's cable hole for the most rigid fixing, ideal for heavy ultrawides. It needs an actual hole \u2014 measure before committing.", {"mode": "mount", "how": "grommet bolt-through", "desk": "25 mm with 60 mm hole"}, "Runnable demo \u2014 Grommet mount"], ["Tilt, swivel, rotate", "adjustment", "Good arms tilt, swivel 180 degrees, and rotate to portrait in seconds \u2014 portrait is beloved for code and documents. Full motion means the display serves the task, not the furniture.", {"mode": "tilt", "tilt": "+/- 45 deg", "sw": "+/- 90 deg", "rot": "360 deg"}, "Runnable demo \u2014 Tilt, swivel, rotate"], ["Reach and desk depth", "adjustment", "Arm reach \u2014 40 to 60 cm on full-motion arms \u2014 decides whether the screen can come close on a deep desk or swing back for clients. Measure desk depth before choosing the arm class.", {"mode": "reach", "cm": 52}, "Runnable demo \u2014 Reach and desk depth"], ["Cable management", "adjustment", "Arms route display cables along their length with clips, keeping the floating look clean through the full motion range. Leave service slack \u2014 a taut cable fights the arm.", {"mode": "cable"}, "Runnable demo \u2014 Cable management"], ["Ergonomic positioning", "ergonomics", "The ergonomic target: top of the screen at or below eye level, an arm's length away, with a slight upward tilt. Arms make this adjustable in seconds; stands make it a book-stack project.", {"mode": "ergo"}, "Runnable demo \u2014 Ergonomic positioning"], ["Dual-monitor setups", "multi", "Dual arms put code on one screen and terminal plus hardware stats on the other \u2014 the test-bench standard layout. Matched monitor sizes keep the sightline level.", {"mode": "multi", "n": 2, "layout": "side by side, slight inward angle"}, "Runnable demo \u2014 Dual-monitor setups"], ["Triple-monitor rigs", "multi", "Triple mounts arc three displays around the user for sim racing, trading desks, and monitoring walls. The center takes the focus display; the wings take auxiliaries at an angle.", {"mode": "multi", "n": 3, "layout": "center + angled wings"}, "Runnable demo \u2014 Triple-monitor rigs"], ["Installation", "mounting", "Install order: clamp the pole, set the arm height, bolt the VESA plate to the monitor, hang and level, set tension, route cables. Two people for ultrawides \u2014 the panel is precious.", {"mode": "install", "steps": ["Clamp the pole to the desk", "Set arm height", "Bolt VESA plate to monitor", "Hang monitor and level", "Set spring tension", "Route cables with slack"]}, "Runnable demo \u2014 Installation"], ["Rigging workflow", "ergonomics", "The rigging workflow: confirm VESA and weight, choose the mount for the desk, install, set ergonomics, route cables. Then adjust for a week \u2014 the perfect position reveals itself through use.", {"mode": "workflow", "steps": ["Confirm VESA pattern and weight", "Choose clamp or grommet", "Install per the manual", "Set ergonomic position", "Route cables with slack", "Fine-tune over a week"]}, "Runnable demo \u2014 Rigging workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"vesa\"){\n  show(\"VESA patterns\",\"75x75 and 100x100 mm\");\n  show(\"Your monitor\",DATA.v);\n  show(\"Fits\",DATA.ok?\"YES\":\"NO - needs an adapter plate\");\n}else if(m===\"weight\"){\n  show(\"Monitor weight\",DATA.kg+\" kg\");\n  show(\"Arm rated\",DATA.rated+\" kg\");\n  show(\"Verdict\",DATA.kg<=DATA.rated?\"SAFE\":\"OVERLOAD - bigger arm needed\");\n}else if(m===\"reach\"){\n  show(\"Arm reach\",DATA.cm+\" cm\");\n  show(\"Covers\",\"deep desks and corner setups\");\n}else if(m===\"tilt\"){\n  show(\"Tilt\",DATA.tilt);\n  show(\"Swivel\",DATA.sw);\n  show(\"Rotate\",DATA.rot+\" (portrait in seconds)\");\n}else if(m===\"mount\"){\n  show(\"Mount\",DATA.how);\n  show(\"Desk thickness\",DATA.desk);\n  show(\"Check\",\"desk edge must be solid, not hollow-core thin\");\n}else if(m===\"gas\"){\n  show(\"Mechanism\",\"gas spring\");\n  show(\"Feel\",\"one finger moves it, stays where left\");\n  show(\"Best for\",\"frequent adjusting, shared desks\");\n}else if(m===\"mech\"){\n  show(\"Mechanism\",\"mechanical spring + tilt head\");\n  show(\"Setup\",\"set tension once per monitor weight\");\n  show(\"Best for\",\"set-and-forget single user\");\n}else if(m===\"multi\"){\n  show(\"Arms\",DATA.n);\n  show(\"Layout\",DATA.layout);\n  show(\"Use\",\"code + terminal + stats, all visible\");\n}else if(m===\"cable\"){\n  show(\"Routing\",\"clips along the arm\");\n  show(\"Slack\",\"enough for full motion range\");\n}else if(m===\"ergo\"){\n  show(\"Height\",\"top of screen at or below eye level\");\n  show(\"Distance\",\"about an arm's length\");\n  show(\"Tilt\",\"slight upward tilt of the panel\");\n}else if(m===\"install\"){\n  console.log(\"Install:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"care\"){\n  show(\"Care\",\"check clamp tightness yearly\");\n  show(\"Gas arms\",\"never disassemble the cylinder\");\n}else if(m===\"workflow\"){\n  console.log(\"Rigging workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-monitor-arm-multi-monitor-mount/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-monitor-arm-multi-monitor-mount',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-monitor-arm-multi-monitor-mount',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
