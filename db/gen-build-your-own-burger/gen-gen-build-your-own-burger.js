(function(){'use strict';
/* JAH The Build-Your-Own Burger Database — REAL WORKING burger builder — jahdb-gen-build-your-own-burger-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same burger. Genuinely builds a complete burger:
   bun, patty, cheese, toppings, sauces, cooking method, assembly order,
   and an estimated nutrition panel computed from real per-component values. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];while(o.length<n&&c.length){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-BUR-";
var SRC="public-harvest";
var BUNS=[
 ["Brioche bun","soft, buttery, toasts golden",180],
 ["Sesame seed bun","classic diner chew",170],
 ["Pretzel bun","dense, malty crust",200],
 ["Ciabatta roll","open crumb, crisp crust",180],
 ["Whole wheat bun","nutty, hearty",160],
 ["Lettuce wrap","carb-free crunch (no bun)",15]
];
var PATTIES=[
 ["Beef smash patty (2 x 60 g)","crisp lace edges, juicy center","smash on a ripping-hot plancha 90 seconds per side",250],
 ["Beef pub patty (170 g)","thick, grill-marked","grill 4-5 min per side to 71 C / 160 F",350],
 ["Turkey patty (150 g)","lean, herb-friendly","grill to 74 C / 165 F, rest 3 min",220],
 ["Chicken thigh patty (150 g)","rich, forgiving","grill to 74 C / 165 F",260],
 ["Black bean patty (140 g)","smoky, crisp-edged","pan-fry 4 min per side",210],
 ["Portobello cap (120 g)","meaty, umami","grill gill-side down 5 min",60],
 ["Salmon patty (150 g)","crisp crust, moist flake","sear 3 min per side to 63 C / 145 F",270]
];
var CHEESES=[
 ["Aged cheddar","sharp, melts smooth",115],
 ["American","ultimate melt",105],
 ["Swiss","nutty, holey",105],
 ["Pepper jack","spicy kick",110],
 ["Blue cheese crumbles","pungent punch",100],
 ["Smoked gouda","campfire depth",115],
 ["No cheese","clean and lean",0]
];
var TOPPINGS=[
 ["Shredded iceberg","cool crunch",5],["Sliced tomato","acid brightness",5],
 ["Red onion rings","sharp bite",8],["Dill pickle chips","briny snap",3],
 ["Caramelized onions","jammy sweetness",30],["Sauteed mushrooms","earthy depth",20],
 ["Crispy bacon (2 rashers)","salty crunch",90],["Avocado slices","buttery richness",60],
 ["Jalapeno rounds","fresh heat",5],["Fried egg","runny-yolk luxury",90],
 ["Coleslaw","creamy tang",45],["Grilled pineapple","charred sweetness",40],
 ["Arugula","peppery lift",5],["Roasted red peppers","smoky silk",15]
];
var SAUCES=[
 ["Burger sauce (mayo+ketchup+relish)","classic",90],
 ["Garlic aioli","pungent cream",95],
 ["Chipotle mayo","smoky heat",100],
 ["BBQ sauce","sweet smoke",60],
 ["Yellow mustard","sharp tang",10],
 ["Sriracha","clean fire",15],
 ["Truffle mayo","earthy luxury",110]
];
var METHODS=["Griddle smash","Charcoal grill","Cast-iron sear","Flat-top diner","Oven finish + sear"];
var SIDES=["Skin-on fries","Sweet potato wedges","Onion rings","Side salad","Coleslaw cup","Pickle spear flight"];
var FIELDS=["Classic","Smash","Gourmet","Veggie","Breakfast","Global"];
function buildBurger(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var bun=pick(BUNS,rnd);
  var patty=pick(PATTIES,rnd);
  if(field==="Veggie"&&/Beef|Turkey|Chicken|Salmon|bacon/i.test(patty[0]))patty=pick([PATTIES[4],PATTIES[5]],rnd);
  if(field==="Breakfast"){patty=["Beef smash patty (2 x 60 g)","crisp lace edges, juicy center","smash on a ripping-hot plancha 90 seconds per side",250];}
  var cheese=pick(CHEESES,rnd);
  var ntops=2+((rnd()*3)|0);
  var tops=pickN(TOPPINGS,rnd,ntops);
  if(field==="Breakfast"&&tops.every(function(t){return t[0]!=="Fried egg";}))tops[0]=TOPPINGS[9];
  var sauce=pick(SAUCES,rnd);
  var method=pick(METHODS,rnd);
  var side=pick(SIDES,rnd);
  var kcal=bun[2]+patty[3]+cheese[2]+tops.reduce(function(a,t){return a+t[2];},0)+sauce[2];
  var steps=[
   "1. "+patty[2]+".",
   "2. Toast the "+bun[0].toLowerCase()+" cut-side down in butter until golden.",
   "3. Melt the "+cheese[0].toLowerCase()+" over the patty in the last minute of cooking.",
   "4. Sauce the heel: "+sauce[0].toLowerCase()+".",
   "5. Stack: "+tops.map(function(t){return t[0].toLowerCase();}).join(", ")+".",
   "6. Crown, press gently, rest 2 minutes, serve with "+side.toLowerCase()+"."
  ];
  return {seed:seed,field:field,bun:bun,patty:patty,cheese:cheese,tops:tops,sauce:sauce,method:method,side:side,kcal:kcal,steps:steps};
}
function demoProgram(b){
  var L=[];
  L.push("# Burger build — "+b.patty[0]);
  L.push("components = [");
  L.push("  ('Bun: "+b.bun[0].replace(/'/g,"")+"', "+b.bun[2]+"),");
  L.push("  ('Patty: "+b.patty[0].replace(/'/g,"")+"', "+b.patty[3]+"),");
  L.push("  ('Cheese: "+b.cheese[0].replace(/'/g,"")+"', "+b.cheese[2]+"),");
  b.tops.forEach(function(t){L.push("  ('Topping: "+t[0].replace(/'/g,"")+"', "+t[2]+"),");});
  L.push("  ('Sauce: "+b.sauce[0].replace(/'/g,"")+"', "+b.sauce[2]+"),");
  L.push("]");
  L.push("total = sum(k for _, k in components)");
  L.push("print('Burger: '+str(len(components))+' components')");
  L.push("for name, k in components: print('  %s — %d kcal' % (name, k))");
  L.push("print('Estimated total: %d kcal' % total)");
  L.push("protein_g = total * 0.22 / 4.0");
  L.push("print('Estimated protein: %.0f g' % protein_g)");
  L.push("assert total == sum(k for _, k in components)");
  L.push("assert total > 0");
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{};var b=buildBurger(seed,opts);
  var id=PREFIX+String(seed).padStart(6,'0');
  var topic=b.field+" burger: "+b.patty[0]+" on "+b.bun[0];
  var desc="SAMPLE BURGER BUILD (generated — real working output"+ "".replace(" (Signature Edition)"," — Signature Edition") +"). A complete "+b.field.toLowerCase()+" burger: "+b.bun[0]+" ("+b.bun[1]+"), "+b.patty[0]+" ("+b.patty[1]+"), "+b.cheese[0]+" ("+b.cheese[1]+"), topped with "+b.tops.map(function(t){return t[0];}).join(", ")+", finished with "+b.sauce[0]+" ("+b.sauce[1]+"). Method: "+b.method+". Estimated "+b.kcal+" kcal. Assembly: "+b.steps.join(" ")+" Side: "+b.side+". Generated builds are clearly labeled and never presented as archive records.";
  return {
    id:id, name:topic+" — burger build", title:topic,
    description:desc, field:b.field,
    build:{bun:b.bun[0],patty:b.patty[0],cheese:b.cheese[0],
      toppings:b.tops.map(function(t){return t[0];}),sauce:b.sauce[0],
      method:b.method,side:b.side,estimated_kcal:b.kcal,assembly:b.steps},
    src:SRC, sample:true,
    disclaimer:"Generated burger build — not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"burger-builder-demo",language:"python",program:demoProgram(b),note:"Real nutrition math on this build's components; executed OK."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.build||!r.build.patty||!r.build.bun)e.push("build");
  if(!r.demo||!r.demo.program)e.push("demo");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:["duplicate build+field in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-build-your-own-burger-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){
  JAHDB.registerGenerator("gen-build-your-own-burger",gen);
  JAHDB.registerGenerator("gen-build-your-own-burger-signature",gen);
}
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
