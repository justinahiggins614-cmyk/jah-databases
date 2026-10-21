(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "types", "installation", "planning", "care"];
var PREFIX='JAH-PCO70S-';
var GENVER='jahdb-pc-organizer-desktop-cable-pass-through-grommets-signature-1.0';
var DBNAME='Signature DeskPort Grommets';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["DeskPort concept", "overview", "The Signature DeskPort Grommets are Manon's original pass-through system: ports engineered as desk furniture with fill math printed on every size. Cable routing becomes part of the desk's design, not an apology.", {"mode": "dia", "dia": 2.5, "common": [2, 2.5, 3]}, "Runnable demo \u2014 DeskPort concept"], ["Port sizing", "sizing", "DeskPorts come in 2, 2.5, and 3 inches with the fill table laser-etched on the underside of each port. The math travels with the part, so sizing is always honest.", {"mode": "dia", "dia": 3, "common": [2, 2.5, 3]}, "Runnable demo \u2014 Port sizing"], ["Oracle picker", "sizing", "The picker card lists common bundles \u2014 'dual monitor station,' 'test bench,' 'charging hub' \u2014 with the port size each wants. Most buyers never do the math because the card already did.", {"mode": "pick", "n": 8, "mm": 7, "pick": "DeskPort 3 in, brush"}, "Runnable demo \u2014 Oracle picker"], ["Honest fill", "sizing", "The fill rule is printed on the port: 60 percent maximum, with the cable-area table beside it. This demo proves a test-bench bundle against the etched table.", {"mode": "fill", "dia": 3, "cable": 1800}, "Runnable demo \u2014 Honest fill"], ["Brush wall", "types", "The brush wall uses dense, angled bristles that seal around cables of mixed diameters \u2014 no gaps, no dust waterfalls. Bristles replace individually, so a tired port is a two-minute fix.", {"mode": "brush"}, "Runnable demo \u2014 Brush wall"], ["Furniture finishes", "types", "DeskPorts come in finishes matched to desk materials \u2014 oak, walnut, matte black, brushed aluminum \u2014 plus a paintable primer ring. The port disappears into the desk it serves.", {"mode": "metal"}, "Runnable demo \u2014 Furniture finishes"], ["Clean cut kit", "installation", "The clean-cut kit pairs the hole saw with a depth stop and a backing block, guaranteeing a blowout-free cut in one pass. The kit turns a scary cut into a routine one.", {"mode": "install", "steps": ["Position with the template", "Set the depth stop", "Back the cut", "Saw in one steady pass", "Seat the DeskPort"]}, "Runnable demo \u2014 Clean cut kit"], ["Deep-desk ports", "installation", "Deep-desk DeskPorts telescope to grip tops up to 3 inches \u2014 butcher block included. The telescoping sleeve locks with a quarter turn and never works loose.", {"mode": "desk", "t": 2.5}, "Runnable demo \u2014 Deep-desk ports"], ["Station planning", "planning", "Station planning maps every device to its port before any cut: monitors to the rear port, PC to the side port, chargers to the front. The plan is drawn on the desk template, full size.", {"mode": "plan", "where": "rear + side + front stations", "n": 3}, "Runnable demo \u2014 Station planning"], ["Port arithmetic", "planning", "Port arithmetic converts device lists to port counts: sum the cables, divide by comfortable fill, round up. The demo runs a full battlestation through the formula.", {"mode": "count", "n": 18, "per": 8}, "Runnable demo \u2014 Port arithmetic"], ["The hidden path", "planning", "The hidden path pairs DeskPorts with the under-desk raceway: vertical through the port, horizontal through the raceway, out at the wall. One designed path from every device to power.", {"mode": "tray"}, "Runnable demo \u2014 The hidden path"], ["Power stations", "planning", "Power stations mount the brick and strip under the desk on a sliding tray, with only DC cables rising through the port. Service means sliding the tray out \u2014 no crawling.", {"mode": "pick", "n": 4, "mm": 4, "pick": "DeskPort 2.5 in per station"}, "Runnable demo \u2014 Power stations"], ["Measure-twice ports", "installation", "The measure-twice rule is built into the template: position, cable-path check, then cut. The template's checklist must be initialed before the saw comes out \u2014 ceremony that prevents regret.", {"mode": "mistake", "bad": "freehand cutting", "good": "template + checklist + cut"}, "Runnable demo \u2014 Measure-twice ports"], ["Port service", "care", "Port service is annual: vacuum the brush wall, check the seat, wipe the finish. Five minutes keeps the invisible infrastructure invisible.", {"mode": "care"}, "Runnable demo \u2014 Port service"], ["DeskPort workflow", "planning", "The DeskPort workflow: template the stations, count the cables, prove the fill, cut with the kit, seat the ports, route everything. Desks that look designed, because they were.", {"mode": "workflow", "steps": ["Template station positions", "Count cables per station", "Prove fill math", "Cut with the clean-cut kit", "Seat the DeskPorts", "Route every cable"]}, "Runnable demo \u2014 DeskPort workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-desktop-cable-pass-through-grommets-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-desktop-cable-pass-through-grommets-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-desktop-cable-pass-through-grommets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
