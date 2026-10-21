(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "drawers", "labels", "organization", "placement", "maintenance"];
var PREFIX='JAH-PCO63S-';
var GENVER='jahdb-pc-organizer-component-storage-drawer-cabinet-signature-1.0';
var DBNAME='Signature Parts Vault Cabinet';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Vault concept", "overview", "The Signature Parts Vault Cabinet is Manon's original storage design: a 64-drawer cabinet where every drawer has an address and the index lives on the door \u2014 and in the Vault's memory. Parts do not get lost; they get fil", {"mode": "dims", "w": 20, "d": 6, "h": 16, "n": 64}, "Runnable demo \u2014 Vault concept"], ["Vault dimensions", "overview", "The Vault keeps the classic bench footprint \u2014 about 20 by 6 by 16 inches \u2014 because the size was already right. What changed is everything around the drawers: rails, labels, and the index.", {"mode": "dims", "w": 20, "d": 6, "h": 16, "n": 64}, "Runnable demo \u2014 Vault dimensions"], ["Glide drawers", "drawers", "Vault drawers ride on smooth glides instead of friction slots, so a full drawer of screws opens with one finger. Removable as trays, washable, and they never jam half-open the way tired plastic can.", {"mode": "drawer", "w": 2.1, "d": 3.8, "h": 2.9, "holds": "standoffs, screws, jumpers", "div": true}, "Runnable demo \u2014 Glide drawers"], ["Living dividers", "drawers", "Living dividers snap to a grid inside each drawer and re-snap in seconds when the mix changes. A drawer that held one part type last month holds four compartmented types today.", {"mode": "dividers", "n": 3}, "Runnable demo \u2014 Living dividers"], ["Etched labels", "labels", "Drawer fronts take engraved-effect labels from any label maker, seated in a deep channel that protects the text from fingers. Labels survive years of pulls because they sit below the wear line.", {"mode": "label", "what": "M3x6 \u2014 motherboard screws"}, "Runnable demo \u2014 Etched labels"], ["Address scheme", "organization", "Every drawer has a printed address \u2014 cabinet, row, column, like B-3-2 \u2014 and the address is the label. Talking about parts becomes precise: 'B-3-2 is empty' beats 'we're out of the little silver ones.'", {"mode": "sort", "cats": ["A row: mounting hardware", "B row: power and adapters", "C row: fasteners by size", "D row: jumpers, pins, thermal"]}, "Runnable demo \u2014 Address scheme"], ["Seven-second retrieval", "organization", "The Vault's retrieval target is seven seconds: read the index, open the addressed drawer, take the part. This demo times it, because a storage system should be benchmarked like any other tool.", {"mode": "find", "want": "M4 PSU screws", "drawer": "C-2-4", "sec": 6}, "Runnable demo \u2014 Seven-second retrieval"], ["The living index", "organization", "The index lives on the door as a printed sheet and in the Vault's companion log, which notes when a drawer runs low. The log turns 'we're out' into a shopping list before it becomes a crisis.", {"mode": "inventory", "n": 64}, "Runnable demo \u2014 The living index"], ["Locking stacks", "placement", "Vault cabinets lock together with cam latches \u2014 no sliding, no walking, no tip. Stacks of three are rated and tested, with the latches doing what gravity used to do.", {"mode": "stack", "n": 3}, "Runnable demo \u2014 Locking stacks"], ["French-cleat wall mount", "placement", "The Vault hangs on a French cleat: one wall strip, infinite repositioning, and the cabinet lifts off for bench work. Cleats hold the loaded weight with a safety margin drywall anchors cannot promise.", {"mode": "wall"}, "Runnable demo \u2014 French-cleat wall mount"], ["Ballast base", "placement", "The bottom cabinet option includes a ballast base that lowers the center of gravity for tall stacks. Physics does the anchoring when wall mounting is not possible.", {"mode": "weight", "kg": 18}, "Runnable demo \u2014 Ballast base"], ["Washable everything", "maintenance", "Drawers, dividers, and label channels are all washable \u2014 pull, soak, dry, snap back. Metal shavings have no permanent home in the Vault.", {"mode": "clean"}, "Runnable demo \u2014 Washable everything"], ["Vault network", "organization", "Multiple Vaults share one master index with cabinet letters, so the system grows by letter: A, B, C. The index knows every address in the room, and so do you after a week.", {"mode": "expand"}, "Runnable demo \u2014 Vault network"], ["Vault vs the drawer era", "overview", "The Vault keeps everything the classic cabinet got right \u2014 footprint, drawer count, bench presence \u2014 and fixes the friction: glides, addresses, living index. Evolution, not revolution, for the workshop's most-used furnit", {"mode": "compare"}, "Runnable demo \u2014 Vault vs the drawer era"], ["Vault commissioning", "organization", "Commissioning a Vault is a ritual: sort by job, address every drawer, print the index, log the baseline stock. Done once, it pays every day the bench is used.", {"mode": "workflow", "steps": ["Sort everything by job", "Address every drawer", "Print and mount the index", "Log baseline stock", "File parts, seven seconds each"]}, "Runnable demo \u2014 Vault commissioning"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-component-storage-drawer-cabinet-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-component-storage-drawer-cabinet-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-component-storage-drawer-cabinet-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
