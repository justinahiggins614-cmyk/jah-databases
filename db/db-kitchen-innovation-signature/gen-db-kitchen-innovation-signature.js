(function(){'use strict';
/* JAH The Kitchen Innovation Database — real working generator, jahdb-db-kitchen-innovation-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KIS-";
var SLUG="db-kitchen-innovation";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Chef's Knife (Good)", "tier": "Foundations", "concept": "cutting joy", "mechanism": "8in + sharp", "parts": ["knife"], "build": "study", "time": "2h", "level": "beginner", "safety": "knife safety", "notes": "kitchen: sharp = safe"},
  {"kind": "gm", "t": "Cutting Board (End-Grain)", "tier": "Foundations", "concept": "kind to knives", "mechanism": "end-grain wood", "parts": ["board"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "kitchen: oil monthly"},
  {"kind": "gm", "t": "Cast Iron Skillet", "tier": "Foundations", "concept": "sear everything", "mechanism": "12in + seasoned", "parts": ["skillet"], "build": "season", "time": "4h", "level": "beginner", "safety": "hot handle", "notes": "kitchen: dry + oil"},
  {"kind": "gm", "t": "Instant-Read Thermometer", "tier": "Foundations", "concept": "done how?", "mechanism": "thermapen-fast", "parts": ["thermo"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "kitchen: temp, not time"},
  {"kind": "gm", "t": "Scale (Kitchen)", "tier": "Foundations", "concept": "bake precisely", "mechanism": "0.1g scale", "parts": ["scale"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "kitchen: weight > volume"},
  {"kind": "gm", "t": "Bench Scraper", "tier": "Foundations", "concept": "move + cut", "mechanism": "steel scraper", "parts": ["scraper"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "kitchen: dough's best friend"},
  {"kind": "gm", "t": "Tongs (12in)", "tier": "Foundations", "concept": "grab hot", "mechanism": "spring tongs", "parts": ["tongs"], "build": "study", "time": "1h", "level": "beginner", "safety": "hot", "notes": "kitchen: extension of hand"},
  {"kind": "gm", "t": "Sheet Pans (Half)", "tier": "Foundations", "concept": "roast all", "mechanism": "heavy half-sheets", "parts": ["pans"], "build": "study", "time": "1h", "level": "beginner", "safety": "hot", "notes": "kitchen: warp-resistant"},
  {"kind": "gm", "t": "Dutch Oven", "tier": "Foundations", "concept": "braise + bake", "mechanism": "enameled 5.5qt", "parts": ["oven"], "build": "study", "time": "2h", "level": "beginner", "safety": "heavy hot", "notes": "kitchen: one pot wonder"},
  {"kind": "gm", "t": "Mandoline", "tier": "Foundations", "concept": "even slices", "mechanism": "guard + sharp", "parts": ["mandoline"], "build": "study", "time": "1h", "level": "beginner", "safety": "ALWAYS guard", "notes": "kitchen: glove too"},
  {"kind": "gm", "t": "Microplane", "tier": "Foundations", "concept": "zest + grate", "mechanism": "sharp etched", "parts": ["plane"], "build": "study", "time": "1h", "level": "beginner", "safety": "sharp", "notes": "kitchen: parmesan clouds"},
  {"kind": "gm", "t": "Sous Vide (Immersion)", "tier": "Compounded", "concept": "perfect temp", "mechanism": "circulator + bath", "parts": ["sous"], "build": "cook", "time": "6h", "level": "intermediate", "safety": "food safety", "notes": "kitchen: 130F steak 2h"},
  {"kind": "gm", "t": "Pressure Cooker", "tier": "Compounded", "concept": "fast tender", "mechanism": "electric multi", "parts": ["cooker"], "build": "cook", "time": "4h", "level": "intermediate", "safety": "steam safety", "notes": "kitchen: beans 30min"},
  {"kind": "gm", "t": "Stand Mixer", "tier": "Compounded", "concept": "dough easy", "mechanism": "planetary mixer", "parts": ["mixer"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "kitchen: bread weekly"},
  {"kind": "gm", "t": "Food Processor", "tier": "Compounded", "concept": "chop fast", "mechanism": "11-cup processor", "parts": ["processor"], "build": "study", "time": "2h", "level": "intermediate", "safety": "blade", "notes": "kitchen: pie dough 30s"},
  {"kind": "gm", "t": "High-Speed Blender", "tier": "Compounded", "concept": "smooth everything", "mechanism": "1800W blender", "parts": ["blender"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "kitchen: soup hot safe"},
  {"kind": "gm", "t": "Grain Mill", "tier": "Compounded", "concept": "fresh flour", "mechanism": "stone mill", "parts": ["mill"], "build": "mill", "time": "4h", "level": "intermediate", "safety": "dust", "notes": "kitchen: wheat berries store"},
  {"kind": "gm", "t": "Fermentation Kit", "tier": "Compounded", "concept": "probiotics", "mechanism": "jars + weights", "parts": ["kit"], "build": "ferment", "time": "6h", "level": "intermediate", "safety": "food safety", "notes": "kitchen: 2% salt brine"},
  {"kind": "gm", "t": "Smoker (Electric)", "tier": "Compounded", "concept": "smoke easy", "mechanism": "electric + chips", "parts": ["smoker"], "build": "smoke", "time": "8h", "level": "intermediate", "safety": "fire safety", "notes": "kitchen: 225F low slow"},
  {"kind": "gm", "t": "Pizza Steel", "tier": "Compounded", "concept": "crisp crust", "mechanism": "steel + hot oven", "parts": ["steel"], "build": "bake", "time": "3h", "level": "intermediate", "safety": "hot heavy", "notes": "kitchen: 550F 1h preheat"},
  {"kind": "gm", "t": "Wok + Burner", "tier": "Compounded", "concept": "stir-fry real", "mechanism": "carbon steel + power", "parts": ["wok"], "build": "cook", "time": "4h", "level": "intermediate", "safety": "hot", "notes": "kitchen: season first"},
  {"kind": "gm", "t": "Espresso (Entry)", "tier": "Compounded", "concept": "cafe at home", "mechanism": "machine + grinder", "parts": ["espresso"], "build": "dial", "time": "10h", "level": "intermediate", "safety": "hot pressure", "notes": "kitchen: 18g in, 36g out"},
  {"kind": "gm", "t": "Sourdough Station", "tier": "Compounded", "concept": "bread ritual", "mechanism": "starter + tools", "parts": ["station"], "build": "bake", "time": "10h", "level": "intermediate", "safety": "food safety", "notes": "kitchen: feed the starter"},
  {"kind": "gm", "t": "Sprouting Kit", "tier": "Compounded", "concept": "fresh greens", "mechanism": "jars + seeds", "parts": ["kit"], "build": "grow", "time": "4h", "level": "intermediate", "safety": "food safety", "notes": "kitchen: rinse twice daily"},
  {"kind": "gm", "t": "Combi Steam Oven", "tier": "Advanced", "concept": "bake + steam", "mechanism": "plumbed oven", "parts": ["oven"], "build": "install", "time": "16h", "level": "advanced", "safety": "pro install", "notes": "kitchen: bread oven spring"},
  {"kind": "gm", "t": "Induction Range", "tier": "Advanced", "concept": "control heat", "mechanism": "full induction", "parts": ["range"], "build": "install", "time": "12h", "level": "advanced", "safety": "electrical pro", "notes": "kitchen: magnetic pans"},
  {"kind": "gm", "t": "Walk-In Pantry", "tier": "Advanced", "concept": "store all", "mechanism": "shelves + zones", "parts": ["pantry"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "kitchen: FIFO rotation"},
  {"kind": "gm", "t": "Outdoor Kitchen", "tier": "Advanced", "concept": "cook outside", "mechanism": "grill + prep + sink", "parts": ["kitchen"], "build": "build", "time": "80h", "level": "advanced", "safety": "gas pro", "notes": "kitchen: 10ft clearance"},
  {"kind": "gm", "t": "Root Cellar (Kitchen)", "tier": "Advanced", "concept": "store harvest", "mechanism": "cool + humid", "parts": ["cellar"], "build": "build", "time": "40h", "level": "advanced", "safety": "structural", "notes": "kitchen: 90% humidity"},
  {"kind": "gm", "t": "Charcuterie Chamber", "tier": "Advanced", "concept": "cure meat", "mechanism": "temp + humidity control", "parts": ["chamber"], "build": "build", "time": "20h", "level": "advanced", "safety": "food safety pro", "notes": "kitchen: 55F 75% RH"},
  {"kind": "gm", "t": "Cheese Cave", "tier": "Advanced", "concept": "age cheese", "mechanism": "wine fridge + humid", "parts": ["cave"], "build": "build", "time": "12h", "level": "advanced", "safety": "food safety", "notes": "kitchen: raw milk laws"},
  {"kind": "gm", "t": "Bread Oven (Wood)", "tier": "Advanced", "concept": "real bread", "mechanism": "brick oven", "parts": ["oven"], "build": "build", "time": "60h", "level": "advanced", "safety": "fire safety", "notes": "kitchen: cure fires slowly"},
  {"kind": "gm", "t": "Commercial Range (Home)", "tier": "Advanced", "concept": "pro power", "mechanism": "36in + hood", "parts": ["range"], "build": "install", "time": "20h", "level": "advanced", "safety": "pro + permits", "notes": "kitchen: makeup air needed"},
  {"kind": "gm", "t": "Master Kitchen Design", "tier": "Advanced", "concept": "dream kitchen", "mechanism": "work triangle + zones", "parts": ["design"], "build": "plan", "time": "40h", "level": "advanced", "safety": "pro", "notes": "kitchen: 26ft triangle max"}
];
var TIPS=["Prototype the mechanism in cardboard first.", "Test with the cheapest parts that can work.", "Measure current draw before choosing a battery.", "Leave 20% headroom in every rating.", "Document the wiring before closing the case.", "User-test the interaction early."];
function money(n){return "$"+n.toFixed(2);}
function planDiy(tp,rnd){
  var total=0,i;
  for(i=0;i<tp.mats.length;i++)total+=tp.mats[i][2];
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE PLAN: "+tp.t);
  L.push("");
  L.push("Overview: "+tp.notes+" Estimated hands-on time "+tp.time+" ("+tp.level+" level). Maker tip: "+tip);
  L.push("");
  L.push("Materials ("+tp.mats.length+" items, about "+money(total)+"):");
  for(i=0;i<tp.mats.length;i++)L.push("  - "+tp.mats[i][0]+" ("+tp.mats[i][1]+") ~"+money(tp.mats[i][2]));
  L.push("");
  L.push("Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"));
  L.push("");
  L.push("Steps:");
  for(i=0;i<tp.steps.length;i++)L.push("  "+(i+1)+". "+tp.steps[i]);
  L.push("");
  L.push("Timeline: split "+tp.time+" into "+(tp.steps.length>6?"three":"two")+" sessions; never rush the final fitting and finish.");
  L.push("Safety: "+tp.safety);
  var hiw="This plan works because each stage prepares the next: measure and cut before joining, join before finishing. "+
    tp.notes+" Work the steps in order, and when a step resists, re-measure rather than forcing it. Safety is part of the method: "+tp.safety+".";
  var kp=["About "+money(total)+" in materials ("+tp.mats.length+" items).",
    "Roughly "+tp.time+" of hands-on work ("+tp.level+" level).",
    "Key technique: "+tp.notes.split(".")[0]+".",
    "Tools: "+(tp.tools.length?tp.tools.slice(0,6).join(", "):"basic hand tools")+".",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Materials: "+tp.mats.map(function(m){return m[0]+" ("+m[1]+")";}).join("; "),
    "Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"),
    "Safety gear: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function planGm(tp,rnd){
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE CONCEPT PLAN: "+tp.t);
  L.push("");
  L.push("Concept: "+tp.concept);
  L.push("");
  L.push("Mechanism: "+tp.mechanism);
  L.push("");
  L.push("Parts: "+tp.parts.join(", "));
  L.push("");
  L.push("Validation path: "+tp.build+" Expect about "+tp.time+" of work at "+tp.level+" level. Maker tip: "+tip);
  L.push("Safety: "+tp.safety);
  var hiw="The mechanism is the heart of it: "+tp.mechanism+" Prototype the core interaction first — "+
    "mock up the mechanics in cardboard, breadboard any electronics, and test before enclosing. "+tp.build+" Safety: "+tp.safety+".";
  var kp=["Core mechanism: "+tp.mechanism+".",
    "Key parts: "+tp.parts.slice(0,6).join(", ")+".",
    "About "+tp.time+" of work ("+tp.level+" level).",
    "Prototype the mechanism before the enclosure.",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Parts: "+tp.parts.join(", "),
    "Validation: "+tp.build,
    "Safety: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function demoProgram(tp){
  var L=[];
  L.push("#!/usr/bin/env python3");
  L.push('"""'+String(tp.t).replace(/"/g,"'")+' — generated plan demo.');
  L.push("Property of Justin Addam Higgins (JAH).");
  L.push('"""');
  if(tp.kind==="diy"){
    L.push("MATS="+JSON.stringify(tp.mats.map(function(m){return [m[0],m[2]];})));
    L.push("def main():");
    L.push("    total=sum(c for _,c in MATS)");
    L.push('    print("Plan: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    for n,c in MATS: print("  %-28s $%6.2f" % (n[:28],c))');
    L.push('    print("  %-28s $%6.2f" % ("TOTAL", total))');
    L.push('    print("OK: plan materials total $%.2f" % total)');
  }else{
    L.push("PARTS="+JSON.stringify(tp.parts));
    L.push("def main():");
    L.push('    print("Concept: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    print("Parts (%d):" % len(PARTS))');
    L.push('    for p in PARTS: print("  - "+p)');
    L.push('    print("OK: %d parts listed" % len(PARTS))');
  }
  L.push('if __name__=="__main__": main()');
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var pool=BANK.filter(function(b){return !opts.field||b.tier===opts.field;});
  if(!pool.length)pool=BANK;
  var tp=(typeof opts.topicIndex==="number"&&BANK[opts.topicIndex])?BANK[opts.topicIndex]:pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,"0");
  var plan=tp.kind==="gm"?planGm(tp,rnd):planDiy(tp,rnd);
  var suf=" (Signature Edition)";
  return {
    id:id,t:tp.t+suf,g:tp.tier,name:tp.t+suf,title:tp.t+suf,
    description:"SAMPLE RECORD (generated — clearly labeled sample, not an archive record).\n\n"+plan.description,
    how_it_works:plan.how_it_works,
    key_points:plan.key_points,requirements:plan.requirements,
    standards:STANDARDS,citations:CITATIONS,
    src:"signature-generated-sample",sample:true,
    disclaimer:"Generated sample record — not an archive record. Seeded archive records are the authoritative entries.",
    ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:demoProgram(tp),note:"Working demonstration program generated with this plan."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.src)e.push("src");
  if(!r.demo||!r.demo.program)e.push("demo");
  var d=String(r.description||"");
  if(d.indexOf("Materials")<0&&d.indexOf("Parts")<0)e.push("plan-materials");
  if(d.indexOf("Steps")<0&&d.indexOf("Validation")<0)e.push("plan-steps");
  if(d.indexOf("Safety")<0)e.push("plan-safety");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.g===record.g;});
  return dups.length?{ok:false,errors:["duplicate title+tier in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-"+SLUG+"-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();

