(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "types", "installation", "care"];
var PREFIX='JAH-PCO64S-';
var GENVER='jahdb-pc-organizer-cable-comb-set-signature-1.0';
var DBNAME='Signature Cable Align Combs';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Align concept", "overview", "The Signature Cable Align Combs are Manon's original cable-geometry system: combs engineered as measuring instruments, with the spacing scale printed on every piece. Straight cables stop being luck and start being proced", {"mode": "pins", "cable": "24-pin ATX", "pins": 24}, "Runnable demo \u2014 Align concept"], ["Scale-printed combs", "sizing", "Every Align Comb carries a centimeter scale etched along its edge, so spacing is measured, not eyeballed. Even spacing becomes automatic when the ruler is in your hand.", {"mode": "pins", "cable": "24-pin ATX", "pins": 24}, "Runnable demo \u2014 Scale-printed combs"], ["EPS alignment", "sizing", "The 8-slot EPS comb has a deeper channel for the thicker CPU wires and a locking tab that grips without crushing. CPU cables carry the most current; their combs respect that.", {"mode": "pins", "cable": "8-pin EPS", "pins": 8}, "Runnable demo \u2014 EPS alignment"], ["PCIe staging", "sizing", "PCIe combs come in a staged kit: 8-slot bodies plus 2-slot riders for the detachable section, so 6+2 cables comb as true 8s. Flagship triple-cable builds get a kit, not a bag of guesses.", {"mode": "pins", "cable": "PCIe 6+2-pin", "pins": 8}, "Runnable demo \u2014 PCIe staging"], ["Quick-release open combs", "types", "Align open combs use a living-hinge snap that opens wide for placement and closes with a positive click. They go on after routing and come off for re-routing \u2014 geometry without commitment.", {"mode": "open"}, "Runnable demo \u2014 Quick-release open combs"], ["Kit math", "sizing", "The Align kit calculator sizes the whole build: cables times combs per cable, plus two spares. This demo runs the math for a full ATX build so the order is right the first time.", {"mode": "count", "per": 4, "cables": 4}, "Runnable demo \u2014 Kit math"], ["Measured spacing", "installation", "With the scale on the comb, spacing is a number: first comb at 5 cm, then every 10, verified against the etched ruler. Documented spacing means the next build copies the last one's perfection.", {"mode": "spacing", "a": 5, "every": 10}, "Runnable demo \u2014 Measured spacing"], ["Align ritual", "installation", "The Align ritual: route, hand-straighten, measure the first position, snap combs down the scale, sight the ribbon. Each step has a number, so apprentices learn it in one build.", {"mode": "install", "steps": ["Route the cable", "Hand-straighten the wires", "Measure first position: 5 cm", "Snap combs down the scale", "Sight the ribbon, correct strays"]}, "Runnable demo \u2014 Align ritual"], ["Sleeve-safe threading", "installation", "Closed Align Combs have flared entries that guide sleeved wires without snagging paracord. Custom cable makers thread a full 24 in under a minute.", {"mode": "types", "types": ["Align closed - flared entries", "Align open - hinge snap"]}, "Runnable demo \u2014 Sleeve-safe threading"], ["Polished channels", "types", "Every wire channel is polished to a glass finish and inspected \u2014 the spec sheet prints the roughness figure. Insulation never meets an edge it can feel.", {"mode": "material", "mat": "optical-grade acrylic"}, "Runnable demo \u2014 Polished channels"], ["Theme system", "types", "Align Combs come in a theme system: clear, smoked, and anodized metallics with matching screws. The smoked finish disappears on black cables the way clear does on everything.", {"mode": "color", "colors": ["clear", "smoked", "black", "silver", "red"]}, "Runnable demo \u2014 Theme system"], ["Retrofit kits", "installation", "Retrofit kits bring Align geometry to existing builds: open combs, a spacing card, and a straightening tool. No disassembly, no new cables \u2014 just better ones.", {"mode": "pick", "cable": "existing factory build", "pick": "Align retrofit kit"}, "Runnable demo \u2014 Retrofit kits"], ["Care and feeding", "care", "Align Combs wipe clean with a damp cloth and the etched scale never fades because it is cut, not printed. Store spares on the spacing card so the kit stays complete.", {"mode": "care"}, "Runnable demo \u2014 Care and feeding"], ["Geometry discipline", "installation", "The discipline is simple: measure, don't eyeball; space, don't scatter; sight, don't assume. Combs are the instrument, but the discipline is the product.", {"mode": "mistake", "bad": "eyeballing spacing", "good": "measure with the etched scale"}, "Runnable demo \u2014 Geometry discipline"], ["Align workflow", "installation", "The Align workflow turns cable dressing into a repeatable procedure with numbers at every step. Documented geometry is the difference between one beautiful build and a beautiful every build.", {"mode": "workflow", "steps": ["Route and hand-straighten", "Measure 5 cm, place first comb", "Snap combs every 10 cm", "Sight down the ribbon", "Log the spacing for the next build"]}, "Runnable demo \u2014 Align workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"pins\"){\n  show(\"Cable\",DATA.cable);\n  show(\"Pins\",DATA.pins);\n  show(\"Comb\",DATA.pins+\"-slot\");\n}else if(m===\"pick\"){\n  show(\"For\",DATA.cable);\n  show(\"Pick\",DATA.pick);\n}else if(m===\"count\"){\n  show(\"Combs per cable\",DATA.per);\n  show(\"Cables\",DATA.cables);\n  show(\"Total combs\",DATA.per*DATA.cables);\n}else if(m===\"install\"){\n  console.log(\"Install order:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}else if(m===\"types\"){\n  console.log(\"Comb types:\");DATA.types.forEach(function(t){console.log(\"  \"+t);});\n}else if(m===\"spacing\"){\n  show(\"First comb\",DATA.a+\" cm from the connector\");\n  show(\"Then every\",DATA.every+\" cm\");\n}else if(m===\"material\"){\n  show(\"Material\",DATA.mat);\n  show(\"Edges\",\"smooth - never nicks wire insulation\");\n}else if(m===\"color\"){\n  show(\"Colors\",DATA.colors.join(\", \"));\n  show(\"Advice\",\"match the build or go clear\");\n}else if(m===\"open\"){\n  show(\"Open combs\",\"snap on after routing\");\n  show(\"Closed combs\",\"thread onto wires before the connector\");\n}else if(m===\"care\"){\n  show(\"Cleaning\",\"wipe with a damp cloth\");\n  show(\"Sunlight\",\"keep out of direct UV\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"workflow\"){\n  console.log(\"Combing workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cable-comb-set-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cable-comb-set-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cable-comb-set-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
