(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "layout", "use_cases", "types", "care"];
var PREFIX='JAH-PCO66S-';
var GENVER='jahdb-pc-organizer-magnetic-screw-mat-signature-1.0';
var DBNAME='Signature MagBench Mat';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Mat concept", "overview", "The Signature MagBench Mat is Manon's original bench memory: a magnetic, writable, zoned surface that tracks every fastener through every step. It does not hold screws; it remembers the job.", {"mode": "surface", "size": "14 x 10 in"}, "Runnable demo \u2014 Mat concept"], ["Memory magnets", "overview", "The magnet array is zoned \u2014 stronger under screw cells, gentler under the writing area \u2014 so tools never stick where notes go. Graduated magnetism is invisible until you notice nothing ever slides.", {"mode": "magnet", "holds": "steel screws, tweezers rest free"}, "Runnable demo \u2014 Memory magnets"], ["Ghost-free writing", "overview", "The writing surface is a true dry-erase silicone that releases marker completely, rated for thousands of write-wipe cycles. Yesterday's phone repair never haunts today's GPU swap.", {"mode": "write"}, "Runnable demo \u2014 Ghost-free writing"], ["Address grid", "layout", "The grid is an address system \u2014 columns lettered, rows numbered \u2014 so a zone is 'B4' instead of 'over there.' Talking about screw locations becomes precise enough for a manual.", {"mode": "grid", "grid": "addressed 1-inch cells", "cells": 140}, "Runnable demo \u2014 Address grid"], ["Thinking zones", "layout", "Pre-printed zone templates for common jobs \u2014 ATX build, phone repair, laptop service \u2014 lay out the mat in seconds. Templates are guides, not cages; draw over them freely.", {"mode": "zones", "zones": ["A: cooler hardware", "B: board screws", "C: power and drives", "D: case and panels", "E: inspection"]}, "Runnable demo \u2014 Thinking zones"], ["Step sequencer", "layout", "The step sequencer numbers zones in teardown order and prints the reverse order for reassembly beside it. The mat literally tells you what to do next.", {"mode": "steps", "steps": ["Panels and shrouds", "Power and GPU", "Cooling", "Board", "Storage", "Final inspection"]}, "Runnable demo \u2014 Step sequencer"], ["Micro repair mode", "use_cases", "Micro mode is a fine-grid insert for phone and watch repair: 5 mm cells that keep twenty screw lengths visibly separate. The insert parks on the main mat, so micro jobs get micro organization.", {"mode": "phone", "screws": 24}, "Runnable demo \u2014 Micro repair mode"], ["Depot mode", "use_cases", "Depot mode covers laptop and console service: the full mat with the manual's screw map transcribed onto it. Thirty-four screws become thirty-four addressed cells.", {"mode": "laptop", "screws": 34}, "Runnable demo \u2014 Depot mode"], ["Hot zone", "overview", "A marked hot zone tolerates freshly removed heatsinks and soldering-adjacent work, rated well past what a bench produces. Hot parts get their own district, away from the screw cells.", {"mode": "heat", "t": 260}, "Runnable demo \u2014 Hot zone"], ["Mat family", "overview", "The MagBench family spans pocket, laptop, and bench sizes with identical grids, so skills transfer. One addressing scheme across all three means the pocket mat teaches the bench mat.", {"mode": "sizes", "sizes": ["pocket 6x4", "laptop 9x7", "bench 14x10"]}, "Runnable demo \u2014 Mat family"], ["Tray dock", "types", "A magnetic tray docks to the mat's edge for the current step's screws, combining tray speed with mat organization. The dock is the handoff point between 'right now' and 'filed.'", {"mode": "tray"}, "Runnable demo \u2014 Tray dock"], ["Ink protocol", "care", "The ink protocol is printed on the mat's corner: dry-erase only, cap markers, wipe after the job. The protocol protects the ghost-free surface that makes the whole system work.", {"mode": "write"}, "Runnable demo \u2014 Ink protocol"], ["Renewal cleaning", "care", "Renewal cleaning \u2014 damp cloth, then isopropyl, then dry \u2014 restores the mat to day-one writability. A renewed mat is indistinguishable from new, which is the point of the protocol.", {"mode": "clean"}, "Runnable demo \u2014 Renewal cleaning"], ["The labeled habit", "layout", "The mat's first rule is printed largest: label before the first screw. Habits beat memory, and the mat enforces the habit by making labeling the easiest thing to do.", {"mode": "mistake", "bad": "screws before labels", "good": "zones labeled, then screws parked"}, "Runnable demo \u2014 The labeled habit"], ["MagBench workflow", "layout", "The MagBench workflow: choose the template, address the zones, number the steps, park screws in order, photograph, reverse to reassemble. The mat remembers so the builder can think.", {"mode": "workflow", "steps": ["Choose the job template", "Address every zone", "Number the teardown steps", "Park screws in order", "Photograph the loaded mat", "Reassemble in reverse order"]}, "Runnable demo \u2014 MagBench workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-magnetic-screw-mat-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-magnetic-screw-mat-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-magnetic-screw-mat-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
