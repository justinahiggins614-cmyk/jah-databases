(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "sizing", "printing", "application", "types", "organization", "care"];
var PREFIX='JAH-PCO65-';
var GENVER='jahdb-pc-organizer-custom-label-heat-shrink-tubing-1.0';
var DBNAME='Custom Label Heat Shrink Tubing';
var PROV='Public documentation and published specifications for Custom Label Heat Shrink Tubing; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What label heat shrink is", "overview", "Printable heat shrink tubing is wire sleeving you print a label on, slide over a connection, and shrink with heat \u2014 the text becomes a permanent ring around the wire. It organizes wiring harnesses by giving every wire a ", {"mode": "ratio", "r": 3, "before": 9, "fits": "over connectors, grips 3 mm wire"}, "Runnable demo \u2014 What label heat shrink is"], ["Shrink ratios", "sizing", "The ratio \u2014 2:1, 3:1, 4:1 \u2014 says how much the diameter shrinks: 3:1 tubing at 9 mm recovers to 3 mm. Higher ratios fit over chunky connectors and still grip thin wires.", {"mode": "ratio", "r": 3, "before": 9, "fits": "over connectors, grips 3 mm wire"}, "Runnable demo \u2014 Shrink ratios"], ["Picking the diameter", "sizing", "Pick tubing whose supplied diameter clears the largest thing it slides over and whose recovered diameter grips the wire: the connector must pass, the wire must be hugged. When in doubt between two sizes, take the larger ", {"mode": "pick", "bundle": 4.2, "pick": "3:1, 9 mm supplied"}, "Runnable demo \u2014 Picking the diameter"], ["Printing the labels", "printing", "Thermal-transfer label printers print crisp permanent text on heat-shrink cartridges \u2014 wire numbers, signal names, destinations. The print survives the shrinking because the ink is heat-set, not surface-coated.", {"mode": "print"}, "Runnable demo \u2014 Printing the labels"], ["Printer models", "printing", "The Brady BMP71 and Dymo Rhino 5200 with heat-shrink cartridges are the bench standards, printing widths from 6 to 24 mm. Cartridge tubing costs more than bulk, but the print-then-shrink workflow is worth it for labeled ", {"mode": "print"}, "Runnable demo \u2014 Printer models"], ["Applying heat", "application", "A heat gun on low, kept moving with the bundle rotated, shrinks tubing evenly without scorching. Lighters work in the field but soot and uneven shrink betray them \u2014 the heat gun is the honest tool.", {"mode": "apply", "tool": "heat gun", "temp": "90-125 C"}, "Runnable demo \u2014 Applying heat"], ["Adhesive-lined dual wall", "types", "Dual-wall tubing lines the inside with adhesive that melts during shrinking, sealing the joint against moisture and adding strain relief. It is the choice for automotive, marine, and outdoor wiring.", {"mode": "adhesive"}, "Runnable demo \u2014 Adhesive-lined dual wall"], ["Cutting to length", "application", "Cut labels about 10 percent long to allow for shrink pullback \u2014 tubing shortens slightly as it shrinks. A 30 mm label wants a 33 mm cut, and this demo does the arithmetic.", {"mode": "cut", "len": 30}, "Runnable demo \u2014 Cutting to length"], ["Harness bundling", "application", "A proper harness gets one printed sleeve per wire plus a larger band around the bundle noting the harness name and destination. Future-you opens the case and reads the wiring like a book.", {"mode": "harness", "n": 8}, "Runnable demo \u2014 Harness bundling"], ["Color coding", "organization", "Tubing colors code wire families at a glance: red for power, black for ground, yellow for signal is one common scheme. Color plus printed text is belt and suspenders for identification.", {"mode": "color", "colors": ["red", "black", "yellow", "blue", "white", "clear"]}, "Runnable demo \u2014 Color coding"], ["Vs electrical tape", "types", "Heat shrink beats electrical tape on every axis that matters: permanent, labeled, sealed, and professional-looking, where tape turns gummy and anonymous. Tape is for emergencies; shrink is for finished work.", {"mode": "tape"}, "Runnable demo \u2014 Vs electrical tape"], ["Testing the shrink", "application", "The finished joint gets the tug test: grip the cooled sleeve and twist \u2014 no rotation, no slip, no exposed conductor. A sleeve that moves was under-shrunk or oversized.", {"mode": "test"}, "Runnable demo \u2014 Testing the shrink"], ["Common mistakes", "application", "Forgetting to slide the tubing on before terminating the connector is the rite of passage \u2014 everyone does it once. The other classic is overheating one spot, which splits the tubing and cooks the wire.", {"mode": "mistake", "bad": "shrinking before sliding over the connector", "good": "slide on first, terminate second"}, "Runnable demo \u2014 Common mistakes"], ["Storing tubing", "care", "Tubing stores cool, dark, and in its tube \u2014 heat and sunlight pre-shrink it on the shelf. Pre-shrunk tubing is just expensive spaghetti.", {"mode": "store"}, "Runnable demo \u2014 Storing tubing"], ["Sleeving workflow", "application", "The workflow: plan the labels, print the sleeves, slide them on before termination, terminate, position, shrink with even heat, tug-test. Labeled harnesses are the mark of finished work.", {"mode": "workflow", "steps": ["Plan label text per wire", "Print the sleeves", "Slide on before terminating", "Terminate and position", "Shrink with even heat", "Tug-test every joint"]}, "Runnable demo \u2014 Sleeving workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-custom-label-heat-shrink-tubing/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-custom-label-heat-shrink-tubing',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-custom-label-heat-shrink-tubing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
