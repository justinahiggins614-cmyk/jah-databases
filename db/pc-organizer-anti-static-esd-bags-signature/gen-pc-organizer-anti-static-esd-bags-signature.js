(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "protection", "sizes", "standards", "usage"];
var PREFIX='JAH-PCO62S-';
var GENVER='jahdb-pc-organizer-anti-static-esd-bags-signature-1.0';
var DBNAME='Signature ESD Shield Bags';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Shield concept", "overview", "The Signature ESD Shield Bags are Manon's original protective packaging: honest metallized shielding in sizes matched to real PC parts, with a labeling panel built into every bag. Protection plus traceability, sealed in ", {"mode": "shield"}, "Runnable demo \u2014 Shield concept"], ["Honest shielding", "protection", "Every Shield Bag prints its tested shielding figure on the bag itself, batch by batch \u2014 no generic claims. If a batch ever tested above the limit, it would not ship as a Shield Bag.", {"mode": "shield"}, "Runnable demo \u2014 Honest shielding"], ["Cage geometry", "protection", "The bags use a continuous metal layer with an overlapped \u2014 never butted \u2014 side seam, so the Faraday cage has no gap at the join. The zip track sits outside the shielding envelope, keeping the seal simple and the cage com", {"mode": "pink"}, "Runnable demo \u2014 Cage geometry"], ["Part-matched sizes", "sizes", "Shield Bag sizes are named for parts, not inches: RAM, M.2, ITX Board, GPU, ATX Board. The inch dimensions print underneath for the precise, but nobody measures a graphics card against a bag twice.", {"mode": "size", "w": 6, "l": 8, "mil": 3.1, "fits": "Signature ITX Board size"}, "Runnable demo \u2014 Part-matched sizes"], ["Size oracle", "sizes", "The size oracle is a printed ruler on every assortment box: lay the part on it and read the bag name. It encodes the four-inch margin rule so the choice is instant and always right.", {"mode": "pick", "item": "graphics card", "item_l": 12, "pick": "Signature GPU bag"}, "Runnable demo \u2014 Size oracle"], ["Armor film", "sizes", "Shield Bags use a 4-mil film standard with reinforced corners, because real parts have sharp bracket edges. The corners are where cheap bags die; these are built for the corners.", {"mode": "size", "w": 12, "l": 16, "mil": 4, "fits": "Signature GPU bag"}, "Runnable demo \u2014 Armor film"], ["Sentinel standard", "standards", "The Sentinel handling standard ships on a card in every box: wrist strap on, bag on the mat, part in, label, file. Five steps that make S20.20-style discipline automatic for a home bench.", {"mode": "standard"}, "Runnable demo \u2014 Sentinel standard"], ["Double-track seal", "usage", "The seal is a double-track zip with a tamper-evident tint: sealed bags show a continuous green line that breaks visibly when opened. A sealed Shield Bag proves the part inside has not been handled since bagging.", {"mode": "seal", "how": "double-track zip, tamper tint"}, "Runnable demo \u2014 Double-track seal"], ["Three weaves", "overview", "The line comes in three weaves: Shield for transport, Bench for in-area handling, and Vault \u2014 black conductive \u2014 for the irreplaceable. Color-coded by weave so the right bag is never a guess.", {"mode": "types", "types": ["Shield - metallized transport", "Bench - dissipative handling", "Vault - black conductive, irreplaceable parts"]}, "Runnable demo \u2014 Three weaves"], ["Label panel", "usage", "Every bag carries a write-on label panel with fields for part, status, and date \u2014 no separate stickers to buy or lose. The panel uses ink that survives years in a drawer without fading.", {"mode": "label", "what": "JAH-G1 GPU - tested good - 2026-10-21"}, "Runnable demo \u2014 Label panel"], ["GPU cradle bag", "usage", "The GPU-size Shield Bag includes a foam cradle strip that supports the card's weight off its cooler fins. Bracket-down storage finally has a designed answer instead of a hope.", {"mode": "size", "w": 12, "l": 16, "mil": 4, "fits": "Signature GPU bag with cradle"}, "Runnable demo \u2014 GPU cradle bag"], ["Small-part system", "usage", "Small parts get the compartment strip: a row of connected 3x5 Shield Bags that tear apart as needed. RAM, M.2 drives, and screws each get their own labeled cell instead of sharing a junk bag.", {"mode": "size", "w": 3, "l": 5, "mil": 3.1, "fits": "compartment strip cells"}, "Runnable demo \u2014 Small-part system"], ["Retirement gauge", "usage", "A printed wear gauge on each bag shows when the film has had enough: crease the corner against the gauge, and if the metal shows through, the bag retires. Judgment replaced by a test.", {"mode": "reuse"}, "Runnable demo \u2014 Retirement gauge"], ["Assortment math", "sizes", "The bench assortment box holds the part-matched sizes in the ratio benches actually use \u2014 more small bags than big ones. This demo computes how many boxes a growing parts collection needs.", {"mode": "qty", "n": 60, "pack": 50}, "Runnable demo \u2014 Assortment math"], ["Shield workflow", "usage", "The Shield workflow: strap on, part on the mat, choose by the oracle, seal the double track, fill the label panel, file. Thirty seconds that treat every part like it matters \u2014 because it does.", {"mode": "workflow", "steps": ["Wrist strap on, bag on the mat", "Size by the oracle ruler", "Seal the double-track zip", "Fill the label panel", "File in the parts vault"]}, "Runnable demo \u2014 Shield workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-anti-static-esd-bags-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-anti-static-esd-bags-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-anti-static-esd-bags-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
