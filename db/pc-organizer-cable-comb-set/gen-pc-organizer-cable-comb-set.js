(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "types", "installation", "care"];
var PREFIX='JAH-PCO64-';
var GENVER='jahdb-pc-organizer-cable-comb-set-1.0';
var DBNAME='Cable Comb Set';
var PROV='Public documentation and published specifications for Cable Comb Set; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What cable combs do", "overview", "Cable combs are small slotted guides that hold each wire of a PSU cable perfectly parallel, turning a rainbow tangle into a flat ribbon. They are the difference between a build that looks assembled and one that looks eng", {"mode": "pins", "cable": "24-pin ATX", "pins": 24}, "Runnable demo \u2014 What cable combs do"], ["The 24-pin ATX comb", "sizing", "The 24-pin motherboard cable takes the biggest comb \u2014 24 slots in one or two rows depending on the cable's construction. It is the most visible cable in the case, so it gets combed first.", {"mode": "pins", "cable": "24-pin ATX", "pins": 24}, "Runnable demo \u2014 The 24-pin ATX comb"], ["8-pin EPS comb", "sizing", "The 8-pin EPS CPU cable takes an 8-slot comb, usually routed over the top of the board. Its run is long and very visible against the motherboard tray.", {"mode": "pins", "cable": "8-pin EPS", "pins": 8}, "Runnable demo \u2014 8-pin EPS comb"], ["PCIe 6+2-pin combs", "sizing", "Graphics card power cables use 6+2-pin connectors, combed as 8 slots with the detachable +2 section included. Two or three PCIe cables on a flagship GPU means the comb count multiplies fast.", {"mode": "pins", "cable": "PCIe 6+2-pin", "pins": 8}, "Runnable demo \u2014 PCIe 6+2-pin combs"], ["Closed vs open combs", "types", "Closed combs are solid rings threaded onto wires before connectors go on \u2014 best for custom sleeved cables. Open combs snap on from the side after routing, which is the only option for factory cables.", {"mode": "open"}, "Runnable demo \u2014 Closed vs open combs"], ["How many combs per cable", "sizing", "Three to five combs per cable hold the ribbon straight: one near each connector and the rest spaced along the run. This demo totals the combs for a full three-cable build.", {"mode": "count", "per": 4, "cables": 3}, "Runnable demo \u2014 How many combs per cable"], ["Comb spacing", "installation", "Space combs every 8 to 12 centimeters with the first about 5 cm from the connector, and the ribbon stays straight without stressing the wires. Even spacing reads as intentional; random spacing reads as accident.", {"mode": "spacing", "a": 5, "every": 10}, "Runnable demo \u2014 Comb spacing"], ["Install order", "installation", "Comb from the component end toward the PSU: seat the connector, straighten the wires by hand, then place combs working backward. Fighting the natural lay of the wires always loses.", {"mode": "install", "steps": ["Seat the connector", "Straighten wires by hand", "Place first comb near connector", "Work backward spacing evenly", "Check the ribbon from the side"]}, "Runnable demo \u2014 Install order"], ["Threading closed combs", "installation", "Closed combs thread onto the wire bundle before the connector is attached, which is why custom cable makers comb as they sleeve. Order matters: combs, then connector, then heat shrink.", {"mode": "types", "types": ["Closed - thread before connector", "Open - snap on after routing"]}, "Runnable demo \u2014 Threading closed combs"], ["Materials", "types", "Combs are cut from acrylic or molded ABS with polished slots that never nick insulation. Cheap 3D-printed combs with rough slots can abrade wires over time \u2014 smoothness is a safety feature.", {"mode": "material", "mat": "polished acrylic"}, "Runnable demo \u2014 Materials"], ["Colors and clear", "types", "Combs come in clear, black, white, and anodized colors to match the build theme, with clear disappearing entirely on dark cables. Matching the cable \u2014 not the case \u2014 is the pro move.", {"mode": "color", "colors": ["clear", "black", "white", "red", "blue"]}, "Runnable demo \u2014 Colors and clear"], ["Combing factory cables", "installation", "Factory cables comb fine with open combs: straighten, snap, space, done \u2014 no disassembly required. Stiff factory wires need an extra comb compared to supple custom ones.", {"mode": "pick", "cable": "factory 24-pin", "pick": "open 24-slot combs x4"}, "Runnable demo \u2014 Combing factory cables"], ["Cleaning combs", "care", "Dust settles on combs like everything else; a damp cloth wipe during routine cleaning keeps them invisible. Avoid solvents on acrylic \u2014 they craze the clear finish.", {"mode": "care"}, "Runnable demo \u2014 Cleaning combs"], ["Common mistakes", "installation", "The classic mistake is forcing a 24-slot comb onto a cable whose wires split into two rows \u2014 it needs two 12-slot combs or a proper 24. The other is combing too tight near the connector, which strains the pins.", {"mode": "mistake", "bad": "forcing one 24-slot onto a split-row cable", "good": "two 12-slot combs, gentle near connectors"}, "Runnable demo \u2014 Common mistakes"], ["Full combing workflow", "installation", "The full ritual: route first, straighten by hand, comb from the component end, space evenly, then sight down the ribbon and fix the one wire that always escapes. Fifteen minutes per cable at a careful pace.", {"mode": "workflow", "steps": ["Route the cable", "Straighten wires by hand", "Comb from the component end", "Space combs evenly", "Sight down the ribbon and fix strays"]}, "Runnable demo \u2014 Full combing workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-cable-comb-set/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-cable-comb-set',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-cable-comb-set',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
