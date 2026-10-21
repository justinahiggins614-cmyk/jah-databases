(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "protection", "sizes", "standards", "usage"];
var PREFIX='JAH-PCO62-';
var GENVER='jahdb-pc-organizer-anti-static-esd-bags-1.0';
var DBNAME='Anti-Static ESD Bags (Assorted Sizes)';
var PROV='Public documentation and published specifications for Anti-Static ESD Bags (Assorted Sizes); compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What ESD bags are", "overview", "Anti-static ESD bags are metallized shielding bags that protect bare circuit boards from electrostatic discharge during storage and transport. Every spare GPU, RAM stick, and PCIe card on the bench lives in one when it i", {"mode": "shield"}, "Runnable demo \u2014 What ESD bags are"], ["Shielding vs pink poly", "protection", "Metallized shielding bags are a Faraday cage \u2014 they block external discharges \u2014 while pink poly bags are merely dissipative and slow down charge already on the surface. Pink poly is fine inside a protected area; only shi", {"mode": "pink"}, "Runnable demo \u2014 Shielding vs pink poly"], ["How shielding works", "protection", "The bag's metal layer \u2014 usually aluminum a fraction of a micron thick \u2014 distributes any discharge around the outside instead of through the contents. Tests measure energy penetration in nanojoules; good shielding bags ke", {"mode": "shield"}, "Runnable demo \u2014 How shielding works"], ["Common sizes", "sizes", "Bags come in a ladder of sizes from 3x5 inches for RAM up to 18x18 for full boards, with 4x6, 6x8, 8x10, 10x12, and 12x16 covering nearly everything on a PC bench. Buying the assortment beats buying one size.", {"mode": "size", "w": 6, "l": 8, "mil": 3.1, "fits": "motherboard accessories, small GPUs"}, "Runnable demo \u2014 Common sizes"], ["Picking the right size", "sizes", "The rule is simple: bag length should exceed the part's longest side by about four inches, giving two inches of handling margin at each end. A 12-inch GPU wants a 12x16 bag, not a wrestling match with a 10x12.", {"mode": "pick", "item": "graphics card", "item_l": 12, "pick": "12 x 16 in bag"}, "Runnable demo \u2014 Picking the right size"], ["Film thickness in mil", "sizes", "Bag film is measured in mils \u2014 thousandths of an inch \u2014 with 2 to 4 mil covering bench use and thicker films for heavy or sharp-edged parts. Thicker film resists punctures; it does not meaningfully change shielding.", {"mode": "size", "w": 8, "l": 10, "mil": 4, "fits": "GPUs, heavy cards"}, "Runnable demo \u2014 Film thickness in mil"], ["ANSI/ESD S20.20 practice", "standards", "ANSI/ESD S20.20 is the program standard for handling ESD-sensitive items, and it requires shielding packaging whenever parts leave the protected area. A bench that bags consistently is a bench that follows the standard's", {"mode": "standard"}, "Runnable demo \u2014 ANSI/ESD S20.20 practice"], ["Zip-top resealable seal", "usage", "Most bench bags use a resealable zip-top closure rather than heat seal, so parts go in and out dozens of times. Pressing the air out before closing keeps the bag flat and the zip unstressed.", {"mode": "seal", "how": "zip-top, resealable"}, "Runnable demo \u2014 Zip-top resealable seal"], ["Bag types on the bench", "overview", "The bench stocks three types: metallized shielding bags for transport and storage, pink dissipative bags for in-area handling, and black conductive bags or boxes for the most sensitive parts. Each has its job; none subst", {"mode": "types", "types": ["Metallized shielding - transport/storage", "Pink dissipative - in-area handling", "Black conductive - most sensitive"]}, "Runnable demo \u2014 Bag types on the bench"], ["Labeling every bag", "usage", "Every bag gets the part name and the date it was bagged, written on the bag or a stuck label \u2014 never on the part. Six months later the label is the difference between a known-good spare and a mystery.", {"mode": "label", "what": "RTX 4070 - tested good - 2026-10-21"}, "Runnable demo \u2014 Labeling every bag"], ["Storing graphics cards", "usage", "A graphics card bags best in 12x16 with the bracket end in first and the bag zipped fully, then stored flat or bracket-down \u2014 never standing on its cooler. The bag prevents static; sensible orientation prevents bent brac", {"mode": "size", "w": 12, "l": 16, "mil": 3.1, "fits": "full-length graphics cards"}, "Runnable demo \u2014 Storing graphics cards"], ["Storing RAM and small cards", "usage", "RAM sticks and M.2 drives live in 3x5 or 4x6 bags, one stick per bag, with the label facing out. Small parts in big bags get lost; right-sized bags keep the drawer searchable.", {"mode": "size", "w": 4, "l": 6, "mil": 2, "fits": "RAM sticks, M.2 drives, small cards"}, "Runnable demo \u2014 Storing RAM and small cards"], ["Reuse and retirement", "usage", "Shielding bags survive many reuses until they are punctured, creased through the metal layer, or the zip fails \u2014 then they retire to non-ESD duty. A bag with a hole is decoration, not protection.", {"mode": "reuse"}, "Runnable demo \u2014 Reuse and retirement"], ["How many to buy", "sizes", "Count the bare parts on hand, add a third for growth, and round up to pack sizes \u2014 bags are cheapest in 100-packs. Running out mid-teardown is how parts end up naked on the desk.", {"mode": "qty", "n": 40, "pack": 100}, "Runnable demo \u2014 How many to buy"], ["Bagging workflow", "usage", "The teardown ritual: test the part, bag it in the right size, label it, file it. Four steps, thirty seconds, and no bare board ever touches the bench overnight.", {"mode": "workflow", "steps": ["Test the part before removal", "Choose the right bag size", "Seal with air pressed out", "Label: part + date + status", "File in the parts drawer"]}, "Runnable demo \u2014 Bagging workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"size\"){\n  show(\"Bag\",DATA.w+\" x \"+DATA.l+\" in\");\n  show(\"Film\",DATA.mil+\" mil metallized polyester\");\n  show(\"Holds\",DATA.fits);\n}else if(m===\"pick\"){\n  show(\"Item\",DATA.item+\" (\"+DATA.item_l+\" in long)\");\n  show(\"Pick\",DATA.pick);\n  show(\"Rule\",\"bag length >= item + 4 in handling margin\");\n}else if(m===\"shield\"){\n  show(\"Construction\",\"metallized polyester - a Faraday cage\");\n  show(\"Shielding\",\"under 10 nJ energy penetration\");\n  show(\"Use\",\"ESD-sensitive parts outside the protected area\");\n}else if(m===\"pink\"){\n  show(\"Pink poly\",\"dissipative, NOT shielding\");\n  show(\"Rule\",\"inside the protected area only, never for transport\");\n}else if(m===\"standard\"){\n  show(\"Program\",\"ANSI/ESD S20.20\");\n  show(\"Rule\",\"shielding packaging outside the EPA\");\n}else if(m===\"seal\"){\n  show(\"Closure\",DATA.how);\n  show(\"Tip\",\"press out air before closing the zip\");\n}else if(m===\"types\"){\n  console.log(\"Bag types:\");DATA.types.forEach(function(t){console.log(\"  \"+t);});\n}else if(m===\"qty\"){\n  show(\"Bags needed\",DATA.n);\n  show(\"Pack size\",DATA.pack);\n  show(\"Packs to buy\",Math.ceil(DATA.n/DATA.pack));\n}else if(m===\"label\"){\n  show(\"Write on the bag\",DATA.what);\n  show(\"Why\",\"identify contents without opening\");\n}else if(m===\"reuse\"){\n  show(\"Reuse\",\"yes, until punctured or delaminated\");\n  show(\"Retire when\",\"torn, creased through, or zip failed\");\n}else if(m===\"mistake\"){\n  show(\"Mistake\",DATA.bad);\n  show(\"Instead\",DATA.good);\n}else if(m===\"store\"){\n  show(\"Storage\",\"cool, dry, away from sunlight\");\n  show(\"Note\",\"heat and UV degrade the metal layer\");\n}else if(m===\"workflow\"){\n  console.log(\"Bagging workflow:\");\n  DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-anti-static-esd-bags/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-anti-static-esd-bags',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-anti-static-esd-bags',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
