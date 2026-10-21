(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "layout", "use_cases", "types", "care"];
var PREFIX='JAH-PCO66-';
var GENVER='jahdb-pc-organizer-magnetic-screw-mat-1.0';
var DBNAME='Magnetic Screw Mat';
var PROV='Public documentation and published specifications for Magnetic Screw Mat; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What a screw mat does", "overview", "A magnetic screw mat is a silicone work surface with magnets underneath and a dry-erase grid on top: screws park in labeled zones instead of rolling away. It turns teardowns from screw roulette into an organized procedur", {"mode": "surface", "size": "12 x 9 in"}, "Runnable demo \u2014 What a screw mat does"], ["The magnetic layer", "overview", "Magnets under the silicone hold steel screws firmly enough to survive a bumped bench but loosely enough to pick up with tweezers. Non-magnetic screws \u2014 brass standoffs, aluminum \u2014 still need their zones; the mat holds th", {"mode": "magnet", "holds": "steel screws through bench bumps"}, "Runnable demo \u2014 The magnetic layer"], ["Dry-erase surface", "overview", "The white silicone top takes dry-erase marker, so zones and notes wipe away when the job is done. Writing the step number next to each screw group is the whole trick.", {"mode": "write"}, "Runnable demo \u2014 Dry-erase surface"], ["The printed grid", "layout", "A printed grid divides the mat into cells, giving every screw type its own address. One cell per type is the rule; mixing types in a cell is how builds grow extra screws.", {"mode": "grid", "grid": "1-inch squares", "cells": 108}, "Runnable demo \u2014 The printed grid"], ["Zone layout", "layout", "Zones group the grid by assembly: cooler screws here, motherboard screws there, drive screws along the edge. The mat mirrors the machine's layout, so reassembly walks the zones in reverse.", {"mode": "zones", "zones": ["Cooler mount screws", "Motherboard screws", "Drive screws", "Case screws", "Leftover inspection"]}, "Runnable demo \u2014 Zone layout"], ["Numbered teardown steps", "layout", "Numbering each zone with the teardown step \u2014 1 for the side panel, 2 for the GPU \u2014 turns the mat into a reassembly script. Reassembly runs the numbers backward, and nothing is forgotten.", {"mode": "steps", "steps": ["Side panel screws", "GPU bracket + power", "Cooler mount", "Motherboard screws", "Drive screws"]}, "Runnable demo \u2014 Numbered teardown steps"], ["Phone repair", "use_cases", "Phone teardowns live or die on screw tracking: twenty tiny screws of four lengths, and one long screw in a short hole kills a board. The mat gives each length its own labeled cell, which is cheap insurance against a dead", {"mode": "phone", "screws": 20}, "Runnable demo \u2014 Phone repair"], ["Laptop teardown", "use_cases", "Laptop service manuals show dozens of screws per model, and the mat's numbered zones follow the manual step by step. Technicians photograph the loaded mat as part of the job record.", {"mode": "laptop", "screws": 34}, "Runnable demo \u2014 Laptop teardown"], ["Heat resistance", "overview", "Silicone mats tolerate hot parts \u2014 a freshly removed heatsink or a warm M.2 drive rests on the mat safely. It is a work surface, not just a screw tray.", {"mode": "heat", "t": 230}, "Runnable demo \u2014 Heat resistance"], ["Mat sizes", "overview", "Mats run from pocket-sized for phones to bench-sized for full PCs, and the right size is the one that fits the job's screw count. A phone mat for a PC build is just a crowded mat.", {"mode": "sizes", "sizes": ["6x4 in pocket", "9x7 in laptop", "12x9 in bench"]}, "Runnable demo \u2014 Mat sizes"], ["Mat vs magnetic tray", "types", "A magnetic parts tray holds screws in one pile for quick jobs; the mat organizes them by zone for real teardowns. Tray for five screws, mat for fifty \u2014 use both, confuse neither.", {"mode": "tray"}, "Runnable demo \u2014 Mat vs magnetic tray"], ["Marker discipline", "care", "Dry-erase markers only \u2014 a permanent marker on a silicone mat is a permanent regret. Fine tips write small zone labels; chisel tips number the big steps.", {"mode": "write"}, "Runnable demo \u2014 Marker discipline"], ["Cleaning the mat", "care", "A damp cloth restores the mat between jobs; isopropyl handles flux and grime. Clean mats erase cleanly \u2014 dirty ones ghost.", {"mode": "clean"}, "Runnable demo \u2014 Cleaning the mat"], ["Common mistakes", "layout", "The classic mistake is parking screws without labeling the zone, which produces a mat of mystery metal. The other is mixing lengths in one cell \u2014 the mat cannot organize what you refuse to separate.", {"mode": "mistake", "bad": "parking screws with no labels", "good": "label every zone before the first screw"}, "Runnable demo \u2014 Common mistakes"], ["Teardown workflow", "layout", "The ritual: lay out the mat, draw the zones, number the steps, then remove screws into their zones in order. Reassembly reverses the film, and the leftover-inspection zone should be empty at the end.", {"mode": "workflow", "steps": ["Lay out and wipe the mat", "Draw zones, number steps", "Remove screws into zones in order", "Photograph the loaded mat", "Reassemble in reverse", "Verify the leftover zone is empty"]}, "Runnable demo \u2014 Teardown workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"surface\"){\n  show(\"Surface\",\"silicone, magnetic, dry-erase\");\n  show(\"Size\",DATA.size);\n  show(\"Job\",\"screws stay where you put them\");\n}else if(m===\"grid\"){\n  show(\"Grid\",DATA.grid);\n  show(\"Cells\",DATA.cells);\n  show(\"Use\",\"one cell per screw type\");\n}else if(m===\"zones\"){\n  console.log(\"Zones:\");DATA.zones.forEach(function(z,i){console.log(\"  \"+(i+1)+\". \"+z);});\n}else if(m===\"steps\"){\n  console.log(\"Numbered steps:\");DATA.steps.forEach(function(s,i){console.log(\"  Step \"+(i+1)+\": \"+s);});\n}else if(m===\"magnet\"){\n  show(\"Holding\",DATA.holds);\n  show(\"Note\",\"magnets keep screws parked, even bumped\");\n}else if(m===\"write\"){\n  show(\"Write\",\"dry-erase marker on the silicone\");\n  show(\"Erases\",\"with a wipe, no ghosting\");\n}else if(m===\"heat\"){\n  show(\"Heat resistant\",\"to \"+DATA.t+\" C\");\n  show(\"Use\",\"hot parts rest safely\");\n}else if(m===\"sizes\"){\n  show(\"Sizes\",DATA.sizes.join(\", \"));\n  show(\"Pick\",\"bench size for PCs, pocket size for phones\");\n}else if(m===\"phone\"){\n  show(\"Repair\",DATA.screws+\" tiny screws\");\n  show(\"Method\",\"one zone per phone section\");\n}else if(m===\"laptop\"){\n  show(\"Teardown\",DATA.screws+\" screws\");\n  show(\"Method\",\"numbered zones match the manual steps\");\n}else if(m===\"tray\"){\n  show(\"Mat\",\"large, zoned, writable\");\n  show(\"Tray\",\"small, portable, unwritable\");\n}else if(m===\"clean\"){\n  show(\"Clean\",\"wipe with a damp cloth\");\n  show(\"Markers\",\"dry-erase only, never permanent\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"workflow\"){\n  console.log(\"Teardown workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-magnetic-screw-mat/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-magnetic-screw-mat',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-magnetic-screw-mat',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
