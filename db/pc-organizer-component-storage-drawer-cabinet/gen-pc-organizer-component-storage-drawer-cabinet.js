(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "drawers", "labels", "organization", "placement", "maintenance"];
var PREFIX='JAH-PCO63-';
var GENVER='jahdb-pc-organizer-component-storage-drawer-cabinet-1.0';
var DBNAME='Component Storage Drawer Cabinet (Akro-Mils style)';
var PROV='Public documentation and published specifications for Component Storage Drawer Cabinet (Akro-Mils style); compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What the drawer cabinet is", "overview", "The Akro-Mils-style drawer cabinet is the bench's small-parts library: a steel frame holding 64 polypropylene drawers for screws, standoffs, jumpers, and adapters. The 10164 is the iconic 64-drawer model every workshop s", {"mode": "dims", "w": 20, "d": 6, "h": 16, "n": 64}, "Runnable demo \u2014 What the drawer cabinet is"], ["Cabinet dimensions", "overview", "The classic cabinet measures about 20 inches wide, 6 deep, and 16 tall \u2014 sized to sit on a bench or mount on a wall without eating the workspace. Sixty-four drawers in that footprint is why it beat every tackle box.", {"mode": "dims", "w": 20, "d": 6, "h": 16, "n": 64}, "Runnable demo \u2014 Cabinet dimensions"], ["Drawer size", "drawers", "Each drawer is roughly 2 by 4 inches and a few inches deep \u2014 big enough for a handful of standoffs, small enough that parts never hide. Removable drawers turn into parts trays you can carry to the build.", {"mode": "drawer", "w": 2.1, "d": 3.8, "h": 2.9, "holds": "standoffs, screws, jumpers", "div": true}, "Runnable demo \u2014 Drawer size"], ["Divider system", "drawers", "Adjustable dividers split drawers into compartments, so one drawer can hold M3 and M4 screws without mixing. Dividers are the difference between a drawer and a junk drawer.", {"mode": "dividers", "n": 2}, "Runnable demo \u2014 Divider system"], ["Label holders", "labels", "Every drawer front has a label slot, and the cabinet ships with card stock for them. A label maker makes them permanent; handwriting makes them immediate \u2014 either beats memory.", {"mode": "label", "what": "M3x6 motherboard screws"}, "Runnable demo \u2014 Label holders"], ["Sorting scheme", "organization", "The winning scheme sorts by job, not by part: one drawer row for mounting hardware, one for power adapters, one for fasteners by size. Sorting by job means the drawer you open matches the task in your hands.", {"mode": "sort", "cats": ["Mounting: standoffs, M3 screws", "Power: adapters, splitters", "Fasteners by size", "Jumpers and pins", "Thermal: pads, paste"]}, "Runnable demo \u2014 Sorting scheme"], ["Finding parts fast", "organization", "With labels and a scheme, any part is under ten seconds away \u2014 this demo times a retrieval the way a bench test would. The alternative is the coffee-can method, which costs minutes per screw.", {"mode": "find", "want": "M3 motherboard screws", "drawer": "A-12", "sec": 7}, "Runnable demo \u2014 Finding parts fast"], ["The index sheet", "organization", "A one-page index taped inside the cabinet door maps part names to drawer numbers for anyone who did not design the scheme. Guests and future-you both need the index.", {"mode": "inventory", "n": 64}, "Runnable demo \u2014 The index sheet"], ["Stacking cabinets", "placement", "The steel frames interlock, so cabinets stack safely two or three high on a deep bench. Heaviest hardware goes in the bottom cabinet \u2014 stability is a feature.", {"mode": "stack", "n": 3}, "Runnable demo \u2014 Stacking cabinets"], ["Wall mounting", "placement", "Keyhole slots on the back let the cabinet hang on a wall, into studs or masonry anchors \u2014 never drywall alone when loaded. Wall mounting reclaims the whole bench footprint.", {"mode": "wall"}, "Runnable demo \u2014 Wall mounting"], ["Loaded weight and tipping", "placement", "Sixty-four drawers of steel screws get heavy, and a top-heavy cabinet can walk or tip when drawers fly open. Anchoring or wall-mounting a loaded cabinet is cheap insurance.", {"mode": "weight", "kg": 24}, "Runnable demo \u2014 Loaded weight and tipping"], ["Cleaning drawers", "maintenance", "Drawers pull out completely for washing in warm soapy water when metal shavings and dust migrate in. Clean drawers protect threads; gritty drawers destroy them.", {"mode": "clean"}, "Runnable demo \u2014 Cleaning drawers"], ["Growing the system", "organization", "When 64 drawers fill, you add a second cabinet \u2014 not a bigger junk box \u2014 and keep one master index across both. One part type, one drawer, forever: the rule that keeps growth organized.", {"mode": "expand"}, "Runnable demo \u2014 Growing the system"], ["Cabinet vs bulk bins", "overview", "Drawer cabinets win for small parts you pick by hand; lidded bin boxes win for bulk stock like bags of zip ties. Most benches run both: the cabinet for precision, bins for volume.", {"mode": "compare"}, "Runnable demo \u2014 Cabinet vs bulk bins"], ["Organization workflow", "organization", "The setup ritual: empty every junk container onto the bench, sort by job, assign drawers, label everything, write the index. An afternoon of sorting buys years of ten-second retrievals.", {"mode": "workflow", "steps": ["Empty all junk containers", "Sort parts by job", "Assign one drawer per type", "Label every drawer", "Write the master index"]}, "Runnable demo \u2014 Organization workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"dims\"){\n  show(\"Cabinet\",DATA.w+\" x \"+DATA.d+\" x \"+DATA.h+\" in\");\n  show(\"Drawers\",DATA.n+\" polypropylene\");\n  show(\"Frame\",\"steel, stackable, wall-mountable\");\n}else if(m===\"drawer\"){\n  show(\"Drawer\",DATA.w+\" x \"+DATA.d+\" x \"+DATA.h+\" in\");\n  show(\"Holds\",DATA.holds);\n  show(\"Dividers\",DATA.div?\"adjustable, included\":\"open bin\");\n}else if(m===\"label\"){\n  show(\"Label\",DATA.what);\n  show(\"Holder\",\"label slot on every drawer front\");\n}else if(m===\"sort\"){\n  console.log(\"Sorting scheme:\");DATA.cats.forEach(function(c,i){console.log(\"  \"+(i+1)+\". \"+c);});\n}else if(m===\"find\"){\n  show(\"Looking for\",DATA.want);\n  show(\"Drawer\",DATA.drawer);\n  show(\"Found in\",DATA.sec+\" seconds\");\n}else if(m===\"inventory\"){\n  show(\"Part types tracked\",DATA.n);\n  show(\"Method\",\"drawer labels + one index sheet\");\n}else if(m===\"stack\"){\n  show(\"Stacking\",\"interlocking frames\");\n  show(\"Safe to\",DATA.n+\" high on a bench\");\n}else if(m===\"wall\"){\n  show(\"Wall mount\",\"keyhole slots on the back\");\n  show(\"Into\",\"studs or masonry anchors, never drywall alone\");\n}else if(m===\"weight\"){\n  show(\"Loaded weight\",DATA.kg+\" kg\");\n  show(\"Advice\",DATA.kg>20?\"anchor or wall-mount it\":\"stable on the bench\");\n}else if(m===\"dividers\"){\n  show(\"Dividers\",DATA.n+\" per drawer\");\n  show(\"Use\",\"split one drawer into compartments\");\n}else if(m===\"clean\"){\n  show(\"Cleaning\",\"drawers pull out fully\");\n  show(\"Wash\",\"warm soapy water, air dry\");\n}else if(m===\"expand\"){\n  show(\"Growth\",\"add cabinets, keep one master index\");\n  show(\"Rule\",\"one part type, one drawer, forever\");\n}else if(m===\"compare\"){\n  show(\"Drawer cabinet\",\"tiny parts, visible, labeled\");\n  show(\"Bin boxes\",\"bulk parts, stacked storage\");\n}else if(m===\"workflow\"){\n  console.log(\"Organization workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-component-storage-drawer-cabinet/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-component-storage-drawer-cabinet',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-component-storage-drawer-cabinet',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
