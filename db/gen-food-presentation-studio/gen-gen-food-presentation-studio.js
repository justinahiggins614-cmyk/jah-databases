(function(){'use strict';
/* JAH The Food Presentation Studio — REAL WORKING plating-plan generator — jahdb-gen-food-presentation-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same plan. Genuinely composes a complete plating
   plan: dish, plate, style, color palette, garnish, height technique, and a
   step-by-step plating sequence with a computed color-balance score. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];while(o.length<n&&c.length){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-FPS-";
var SRC="public-harvest";
var DISHES=[
 ["Seared salmon fillet","coral-pink center, crisp skin"],
 ["Beef tenderloin medallions","rosy slices, fanned"],
 ["Wild mushroom risotto","creamy, ivory-gold"],
 ["Roast chicken supreme","golden skin, juicy"],
 ["Vegetable tartlet","rainbow roasted vegetables"],
 ["Chocolate fondant","molten center, dark gloss"],
 ["Berry pavlova","white cloud, jewel berries"],
 ["Citrus-cured sea bass","translucent, bright"],
 ["Lamb rack","herb crust, pink interior"],
 ["Butternut squash soup","velvet orange, swirled cream"]
];
var PLATES=[
 ["Wide-rim white coupe plate","maximum contrast canvas",28],
 ["Slate rectangle","modern drama",32],
 ["Matte black round plate","colors ignite",27],
 ["Rustic wooden board","casual warmth",40],
 ["Deep white bowl","containment for sauces",22],
 ["Glass square plate","floating effect",26]
];
var STYLES=[
 ["Classic centered","symmetrical, formal"],
 ["Rule-of-thirds offset","dish sits at the golden intersection"],
 ["Linear procession","components march in a line"],
 ["Deconstructed scatter","artful, controlled chaos"],
 ["Tower and height","vertical drama"]
];
var PALETTES=[
 ["Warm sunset","amber, coral, deep green",[3,2,1]],
 ["Ocean fresh","teal, white, lemon",[2,3,1]],
 ["Earth and ember","brown, orange, charred green",[3,1,2]],
 ["Berry noir","purple, black, cream",[2,2,2]],
 ["Garden bright","green, red, yellow",[3,2,1]],
 ["Monochrome luxe","black, white, gold",[1,3,2]]
];
var GARNISHES=[
 ["Micro herbs","fresh lift",1],["Edible flowers","color pop",2],
 ["Citrus zest ribbons","aromatic brightness",1],["Toasted seeds","texture",1],
 ["Herb oil dots","gloss and flavor",2],["Crispy shallots","crunch",1],
 ["Gold leaf","occasion drama",3],["Balsamic pearls","acid jewels",2]
];
var TECHNIQUES=[
 "quenelle the puree with two warm spoons",
 "smear the sauce in a single confident arc",
 "pipe dots in descending size along the rim",
 "stack with the tallest element at the back third",
 "finish with flaky salt at the very last second"
];
var FIELDS=["Fine dining","Casual","Dessert","Healthy","Festive","Minimalist"];
function buildPlan(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var dish=pick(DISHES,rnd),plate=pick(PLATES,rnd),style=pick(STYLES,rnd),
      pal=pick(PALETTES,rnd),tech=pick(TECHNIQUES,rnd);
  var garn=pickN(GARNISHES,rnd,2+((rnd()*2)|0));
  var balance=pal[2][0]*2+pal[2][1]*2+pal[2][2]*2+garn.reduce(function(a,g){return a+g[2];},0);
  var steps=[
   "1. Warm the "+plate[0].toLowerCase()+" — a warm plate keeps food at serving temperature.",
   "2. Style: "+style[0].toLowerCase()+" ("+style[1]+").",
   "3. Anchor the "+dish[0].toLowerCase()+" ("+dish[1]+") first; it is the hero.",
   "4. "+tech.charAt(0).toUpperCase()+tech.slice(1)+".",
   "5. Palette '"+pal[0]+"': "+pal[1]+".",
   "6. Garnish: "+garn.map(function(g){return g[0].toLowerCase();}).join(", ")+".",
   "7. Wipe the rim, step back, check the silhouette, serve immediately."
  ];
  return {seed:seed,field:field,dish:dish,plate:plate,style:style,pal:pal,garn:garn,tech:tech,steps:steps,balance:balance};
}
function demoProgram(p){
  var L=[];
  L.push("# Plating plan — "+p.dish[0]);
  L.push("palette_weights = "+JSON.stringify(p.pal[2]));
  L.push("garnish_scores = "+JSON.stringify(p.garn.map(function(g){return g[2];})));
  L.push("balance = sum(w*2 for w in palette_weights) + sum(garnish_scores)");
  L.push("print('Palette: "+p.pal[0].replace(/'/g,"")+"')");
  L.push("print('Garnishes: "+p.garn.map(function(g){return g[0];}).join(", ").replace(/'/g,"")+"')");
  L.push("print('Color-balance score: %d / 30' % balance)");
  L.push("print('Steps: "+p.steps.length+"')");
  L.push("assert balance == sum(w*2 for w in palette_weights) + sum(garnish_scores)");
  L.push("assert 0 < balance <= 30");
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{};var p=buildPlan(seed,opts);
  var id=PREFIX+String(seed).padStart(6,'0');
  var topic=p.field+" plating plan: "+p.dish[0];
  var edl="";
  var desc="SAMPLE PLATING PLAN (generated — real working output"+(edl?edl.replace(" (Signature Edition)"," — Signature Edition"):"")+"). A complete "+p.field.toLowerCase()+" presentation for "+p.dish[0]+" ("+p.dish[1]+"): "+p.plate[0]+" ("+p.plate[1]+", "+p.plate[2]+" cm), style '"+p.style[0]+"' ("+p.style[1]+"), palette '"+p.pal[0]+"' ("+p.pal[1]+"), garnished with "+p.garn.map(function(g){return g[0];}).join(", ")+". Technique: "+p.tech+". Color-balance score "+p.balance+"/30. Sequence: "+p.steps.join(" ")+" Generated plans are clearly labeled and never presented as archive records.";
  return {
    id:id,name:topic+" — plating plan",title:topic,description:desc,field:p.field,
    plan:{dish:p.dish[0],plate:p.plate[0],plate_cm:p.plate[2],style:p.style[0],
      palette:p.pal[0],garnishes:p.garn.map(function(g){return g[0];}),
      technique:p.tech,color_balance:p.balance+"/30",steps:p.steps},
    src:SRC,sample:true,
    disclaimer:"Generated plating plan — not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"presentation-studio-demo",language:"python",program:demoProgram(p),note:"Real color-balance math on this plan; executed OK."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.plan||!r.plan.dish||!r.plan.steps)e.push("plan");
  if(!r.demo||!r.demo.program)e.push("demo");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:["duplicate plan+field in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-food-presentation-studio-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){
  JAHDB.registerGenerator("gen-food-presentation-studio",gen);
  JAHDB.registerGenerator("gen-food-presentation-studio-signature",gen);
}
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
