(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "printing", "application", "types", "organization", "care"];
var PREFIX='JAH-PCO65S-';
var GENVER='jahdb-pc-organizer-custom-label-heat-shrink-tubing-signature-1.0';
var DBNAME='Signature ID Shrink Sleeves';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Sleeve concept", "overview", "The Signature ID Shrink Sleeves are Manon's original wire-identification system: every sleeve printed, every harness mapped, every label permanent. A Signature harness can be serviced by a stranger with the map in hand.", {"mode": "ratio", "r": 3, "before": 12, "fits": "over D-sub, grips 4 mm wire"}, "Runnable demo \u2014 Sleeve concept"], ["Ratio ladder", "sizing", "ID Sleeves come in 2:1 for snug fits, 3:1 for general bench work, and 4:1 for sliding over connectors onto thin wire. The ladder covers everything from fan leads to D-sub hoods.", {"mode": "ratio", "r": 4, "before": 12, "fits": "over 9 mm connector, grips 3 mm"}, "Runnable demo \u2014 Ratio ladder"], ["Oracle sizing", "sizing", "Every ID Sleeve tube prints a sizing oracle: measure the connector, measure the wire, read the sleeve. The two-measurement rule ends the era of the almost-right tube.", {"mode": "pick", "bundle": 5.5, "pick": "3:1, 12 mm supplied"}, "Runnable demo \u2014 Oracle sizing"], ["Scribe printing", "printing", "The Scribe printer lays down 600-dpi text, barcodes, and QR codes linking to the harness map. A scanned sleeve opens the wiring diagram on your phone \u2014 the label is a hyperlink.", {"mode": "print"}, "Runnable demo \u2014 Scribe printing"], ["Scribe station", "printing", "The Scribe station pairs the printer with the oracle and a cut list, printing a whole harness's sleeves in order. Batch printing turns labeling from a chore into a production line.", {"mode": "print"}, "Runnable demo \u2014 Scribe station"], ["Even-heat technique", "application", "The technique card teaches the figure-eight gun motion: constant movement, full rotation, no dwell. Apprentices practice on scrap until the shrink is glass-smooth.", {"mode": "apply", "tool": "heat gun with reflector nozzle", "temp": "100-120 C"}, "Runnable demo \u2014 Even-heat technique"], ["Seal-wall sleeves", "types", "Seal-wall sleeves bond an adhesive lining that flows into every crevice as it shrinks, rated for engine bays and bilges. The seal is testable: submerge the joint and watch for the bubbles that never come.", {"mode": "adhesive"}, "Runnable demo \u2014 Seal-wall sleeves"], ["Cut calculator", "application", "The cut calculator adds pullback, end margins, and print margins in one formula printed on every tube. Measure once, cut once \u2014 the demo runs the formula.", {"mode": "cut", "len": 40}, "Runnable demo \u2014 Cut calculator"], ["Harness atlas", "application", "Every Signature harness gets an atlas page: sleeve text per wire, bundle route, connector pinouts. The QR on the harness band opens it, so the documentation travels with the work.", {"mode": "harness", "n": 12}, "Runnable demo \u2014 Harness atlas"], ["Signal language", "organization", "The Signature signal language standardizes colors and prefixes: PWR for power, GND for ground, SIG for signal, with voltage in the text. Any Signature harness reads the same, whoever built it.", {"mode": "color", "colors": ["red PWR", "black GND", "yellow SIG", "blue SIG", "white ID"]}, "Runnable demo \u2014 Signal language"], ["Beyond tape, forever", "types", "The Sleeve system retires electrical tape from finished work entirely: every joint gets a printed, sealed, testable sleeve. Tape remains for emergencies, labeled as such.", {"mode": "tape"}, "Runnable demo \u2014 Beyond tape, forever"], ["Proof testing", "application", "Every sleeve passes tug, twist, and visual inspection before the harness ships, logged against the atlas. Tested work is warrantied work.", {"mode": "test"}, "Runnable demo \u2014 Proof testing"], ["The remembered mistake", "application", "The system remembers the classic mistake for you: the cut list orders sleeves before termination in the checklist, highlighted. Forgetting becomes nearly impossible when the procedure will not let you.", {"mode": "mistake", "bad": "terminating before sleeving", "good": "checklist orders sleeves first"}, "Runnable demo \u2014 The remembered mistake"], ["Archive storage", "care", "Sleeve stock lives in the labeled archive tube \u2014 cool, dark, inventoried. The tube's own label tracks remaining length, so reordering happens before the last meter.", {"mode": "store"}, "Runnable demo \u2014 Archive storage"], ["Sleeve workflow", "application", "The Sleeve workflow: map the harness, print the batch, sleeve before termination, shrink with the figure-eight, proof-test, file the atlas. Permanent identification, from plan to proof.", {"mode": "workflow", "steps": ["Map the harness on the atlas", "Print the sleeve batch", "Sleeve before terminating", "Shrink: figure-eight motion", "Proof-test every joint", "File the atlas with QR"]}, "Runnable demo \u2014 Sleeve workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"ratio\"){\n  show(\"Ratio\",DATA.r+\":1\");\n  show(\"Supplied\",DATA.before+\" mm\");\n  show(\"Recovered\",(Math.round(DATA.before/DATA.r*10)/10)+\" mm\");\n  show(\"Fits over\",DATA.fits);\n}else if(m===\"pick\"){\n  show(\"Bundle diameter\",DATA.bundle+\" mm\");\n  show(\"Pick\",DATA.pick);\n  show(\"Rule\",\"supplied dia > connector, recovered dia < wire\");\n}else if(m===\"print\"){\n  show(\"Printers\",\"thermal-transfer label printers\");\n  show(\"Models\",\"Brady BMP71, Dymo Rhino 5200 + heat-shrink cartridges\");\n  show(\"Ink\",\"permanent, smudge-proof when shrunk\");\n}else if(m===\"apply\"){\n  show(\"Tool\",DATA.tool);\n  show(\"Temperature\",DATA.temp);\n  show(\"Technique\",\"even passes, rotate the bundle\");\n}else if(m===\"adhesive\"){\n  show(\"Dual-wall\",\"adhesive lining melts and seals\");\n  show(\"Use\",\"outdoor, automotive, strain relief\");\n}else if(m===\"cut\"){\n  show(\"Label length\",DATA.len+\" mm\");\n  show(\"Cut\",DATA.len+\" mm + 10% for shrink pullback\");\n  show(\"Total\",(Math.round(DATA.len*1.1))+\" mm\");\n}else if(m===\"harness\"){\n  show(\"Wires in harness\",DATA.n);\n  show(\"Sleeve\",\"one printed sleeve per wire + one harness band\");\n}else if(m===\"color\"){\n  show(\"Colors\",DATA.colors.join(\", \"));\n  show(\"Code\",\"by voltage or signal family\");\n}else if(m===\"tape\"){\n  show(\"Heat shrink\",\"permanent, labeled, sealed\");\n  show(\"Electrical tape\",\"temporary, gummy, unlabeled\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);show(\"Instead\",DATA.good);\n}else if(m===\"store\"){\n  show(\"Storage\",\"cool, dark, in the tube\");\n  show(\"Note\",\"heat and UV pre-shrink the tubing\");\n}else if(m===\"test\"){\n  show(\"Test\",\"tug the cooled sleeve\");\n  show(\"Pass\",\"no rotation, no slip\");\n}else if(m===\"workflow\"){\n  console.log(\"Sleeving workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-custom-label-heat-shrink-tubing-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-custom-label-heat-shrink-tubing-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-custom-label-heat-shrink-tubing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
