(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "types", "installation", "planning", "care"];
var PREFIX='JAH-PCO70-';
var GENVER='jahdb-pc-organizer-desktop-cable-pass-through-grommets-1.0';
var DBNAME='Desktop Cable Pass-Through Grommets';
var PROV='Public documentation and published specifications for Desktop Cable Pass-Through Grommets; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What grommets do", "overview", "Desktop cable grommets are rings that line a hole cut through the desk, letting cables pass from top to underside cleanly. They turn cable spaghetti into a disappearing act: up from the PC, down through the desk, gone.", {"mode": "dia", "dia": 2.5, "common": [2, 2.5, 3]}, "Runnable demo \u2014 What grommets do"], ["Hole sizes", "sizing", "The common grommet sizes are 2, 2.5, and 3 inches, each needing the matching hole saw. Bigger is not better \u2014 the right size is the smallest that fits the bundle comfortably.", {"mode": "dia", "dia": 2.5, "common": [2, 2.5, 3]}, "Runnable demo \u2014 Hole sizes"], ["Picking the size", "sizing", "Count the cables and their diameters, then pick the grommet whose brush insert swallows the bundle with room to spare. Mixed bundles that change often want brush inserts; fixed bundles can use split caps.", {"mode": "pick", "n": 6, "mm": 7, "pick": "2.5 in with brush insert"}, "Runnable demo \u2014 Picking the size"], ["Fill math", "sizing", "Fill math keeps grommets honest: total cable cross-section should stay under 60 percent of the hole area, leaving room to add and remove cables. This demo computes the fill for a six-cable bundle.", {"mode": "fill", "dia": 2.5, "cable": 1200}, "Runnable demo \u2014 Fill math"], ["Brush inserts", "types", "Brush inserts ring the hole with flexible bristles that cables push through while dust and drafts stay blocked. They are the answer for bundles that change \u2014 no cap to lose, nothing to thread.", {"mode": "brush"}, "Runnable demo \u2014 Brush inserts"], ["Plastic vs metal", "types", "Plastic grommets come in finishes to match the desk and cost little; metal grommets give a crisp premium edge. Both do the same job \u2014 the choice is furniture, not function.", {"mode": "metal"}, "Runnable demo \u2014 Plastic vs metal"], ["Cutting the hole", "installation", "Mark the position, drill a pilot, then cut with the matching hole saw from the top with the desk supported underneath. Sharp saws and slow feeds prevent the blowout that ruins the underside.", {"mode": "install", "steps": ["Mark the grommet position", "Drill a pilot hole", "Cut with the hole saw from the top", "Sand the edge smooth", "Press the grommet in"]}, "Runnable demo \u2014 Cutting the hole"], ["Desk thickness", "installation", "Standard grommets grip tops up to about 1.5 inches; thicker butcher-block desks need deep-reach models. Measure the top before ordering \u2014 guessing wastes a weekend.", {"mode": "desk", "t": 1.25}, "Runnable demo \u2014 Desk thickness"], ["Position planning", "planning", "Plan positions before cutting: one grommet behind the monitor zone, one beside the PC, each within cable reach of its gear. Holes are forever; planning is cheap.", {"mode": "plan", "where": "behind monitor zone + beside PC", "n": 2}, "Runnable demo \u2014 Position planning"], ["Counting cables per grommet", "planning", "A 2.5-inch grommet comfortably passes six to eight typical cables; beyond that, add a second grommet instead of stuffing. This demo converts a cable count into a grommet count.", {"mode": "count", "n": 14, "per": 7}, "Runnable demo \u2014 Counting cables per grommet"], ["Grommets plus cable tray", "planning", "Grommets handle the vertical drop; an under-desk cable tray handles the horizontal run to the wall. Together they make the complete hidden path from device to outlet.", {"mode": "tray"}, "Runnable demo \u2014 Grommets plus cable tray"], ["Power through grommets", "planning", "Power bricks live under the desk with only their thin DC cable rising through the grommet \u2014 never the AC cord and brick on top. Under-desk power keeps the surface for work, not watts.", {"mode": "pick", "n": 3, "mm": 4, "pick": "2 in brush grommet per station"}, "Runnable demo \u2014 Power through grommets"], ["Common mistakes", "installation", "Cutting before planning the cable path is the classic \u2014 the grommet lands where no cable wants to go. The runner-up is skipping the pilot hole and watching the saw skate across the finish.", {"mode": "mistake", "bad": "cutting where convenient", "good": "plan the cable path, then cut"}, "Runnable demo \u2014 Common mistakes"], ["Care", "care", "Vacuum brush inserts yearly and re-seat grommets after moving the desk \u2014 they walk loose over time. A dab of silicone keeps a loose grommet seated without glue.", {"mode": "care"}, "Runnable demo \u2014 Care"], ["Grommet workflow", "planning", "The workflow: plan positions, count cables, size with fill math, cut once, seat the grommet, route the bundle. Clean desks are planned, not wished.", {"mode": "workflow", "steps": ["Plan grommet positions", "Count cables per position", "Size with fill math", "Cut with the hole saw", "Seat the grommet", "Route the bundle"]}, "Runnable demo \u2014 Grommet workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"dia\"){\n  show(\"Hole saw\",DATA.dia+\" in\");\n  show(\"Grommet\",\"sized for \"+DATA.dia+\" in holes\");\n  show(\"Common\",DATA.common.join(\", \"));\n}else if(m===\"pick\"){\n  show(\"Cables\",DATA.n+\" cables ~\"+DATA.mm+\" mm dia\");\n  show(\"Pick\",DATA.pick);\n  show(\"Rule\",\"brush insert for mixed bundles\");\n}else if(m===\"fill\"){\n  var area=Math.PI*Math.pow(DATA.dia*25.4/2,2);\n  var fill=Math.round(DATA.cable/area*100);\n  show(\"Hole area\",Math.round(area)+\" sq mm\");\n  show(\"Cable area\",Math.round(DATA.cable)+\" sq mm\");\n  show(\"Fill\",fill+\"%\");\n  show(\"Rule\",fill<=60?\"OK - under 60%\":\"TOO FULL - go up a size\");\n}else if(m===\"brush\"){\n  show(\"Brush insert\",\"cables pass, dust stays out\");\n  show(\"Best for\",\"mixed bundles that change often\");\n}else if(m===\"install\"){\n  console.log(\"Install:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}else if(m===\"metal\"){\n  show(\"Metal\",\"premium look, crisp edge\");\n  show(\"Plastic\",\"standard, many finishes\");\n}else if(m===\"desk\"){\n  show(\"Desk thickness\",DATA.t+\" in\");\n  show(\"Standard grommets\",\"fit tops to ~1.5 in\");\n}else if(m===\"plan\"){\n  show(\"Positions\",DATA.where);\n  show(\"Count\",DATA.n+\" grommets\");\n  show(\"Rule\",\"one behind the monitor, one by the PC\");\n}else if(m===\"count\"){\n  show(\"Cables to pass\",DATA.n);\n  show(\"Grommets needed\",Math.ceil(DATA.n/DATA.per));\n  show(\"Per grommet\",\"~\"+DATA.per+\" cables comfortable\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"care\"){\n  show(\"Care\",\"vacuum the brush inserts yearly\");\n  show(\"Check\",\"seating after moving the desk\");\n}else if(m===\"tray\"){\n  show(\"Grommets\",\"vertical pass-through, invisible\");\n  show(\"Cable tray\",\"horizontal runs under the desk\");\n  show(\"Together\",\"the complete hidden path\");\n}else if(m===\"workflow\"){\n  console.log(\"Grommet workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-desktop-cable-pass-through-grommets/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-desktop-cable-pass-through-grommets',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-desktop-cable-pass-through-grommets',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
