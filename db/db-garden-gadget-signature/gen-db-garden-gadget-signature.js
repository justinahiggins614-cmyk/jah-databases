(function(){'use strict';
/* JAH The Garden Gadget Database — real working generator, jahdb-db-garden-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GAGAS-";
var SLUG="db-garden-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Hand Trowel (Great)", "tier": "Foundations", "concept": "planting", "mechanism": "ergonomic + depth marks", "parts": ["trowel"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: one-piece forged"},
  {"kind": "gm", "t": "Soil Moisture Meter", "tier": "Foundations", "concept": "water when?", "mechanism": "probe reads moisture", "parts": ["meter"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: water at 3 dry"},
  {"kind": "gm", "t": "Seed Starting Tray", "tier": "Foundations", "concept": "start indoors", "mechanism": "cells + dome", "parts": ["tray"], "build": "sow", "time": "2h", "level": "beginner", "safety": "none", "notes": "garden: 6 weeks before frost"},
  {"kind": "gm", "t": "Plant Labels", "tier": "Foundations", "concept": "forget varieties", "mechanism": "write + stake", "parts": ["labels"], "build": "make", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: pencil lasts"},
  {"kind": "gm", "t": "Watering Can (Good)", "tier": "Foundations", "concept": "gentle water", "mechanism": "rose head", "parts": ["can"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: rain-like"},
  {"kind": "gm", "t": "Pruners (Bypass)", "tier": "Foundations", "concept": "clean cuts", "mechanism": "bypass + sharp", "parts": ["pruners"], "build": "study", "time": "1h", "level": "beginner", "safety": "blade", "notes": "garden: clean between plants"},
  {"kind": "gm", "t": "Kneeler Pad", "tier": "Foundations", "concept": "knees ache", "mechanism": "thick foam", "parts": ["pad"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: handles help up"},
  {"kind": "gm", "t": "Harvest Basket", "tier": "Foundations", "concept": "carry bounty", "mechanism": "vented basket", "parts": ["basket"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: wash station"},
  {"kind": "gm", "t": "Twine + Clips", "tier": "Foundations", "concept": "support plants", "mechanism": "jute + clips", "parts": ["twine"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: tomato clips"},
  {"kind": "gm", "t": "Row Cover", "tier": "Foundations", "concept": "pests + frost", "mechanism": "fabric shield", "parts": ["cover"], "build": "lay", "time": "2h", "level": "beginner", "safety": "none", "notes": "garden: hoops help"},
  {"kind": "gm", "t": "Compost Thermometer", "tier": "Foundations", "concept": "cooking?", "mechanism": "20in probe", "parts": ["thermo"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "garden: 140F active"},
  {"kind": "gm", "t": "Drip Irrigation Kit", "tier": "Compounded", "concept": "water waste", "mechanism": "drip + timer", "parts": ["kit"], "build": "install", "time": "8h", "level": "intermediate", "safety": "none", "notes": "garden: 90% efficient"},
  {"kind": "gm", "t": "Rain Barrel", "tier": "Compounded", "concept": "free water", "mechanism": "55gal + spigot", "parts": ["barrel"], "build": "install", "time": "4h", "level": "intermediate", "safety": "mosquito screen", "notes": "garden: elevate for pressure"},
  {"kind": "gm", "t": "Soil Test (Lab)", "tier": "Compounded", "concept": "feed right", "mechanism": "lab analysis", "parts": ["test"], "build": "send", "time": "2h", "level": "intermediate", "safety": "none", "notes": "garden: every 3 years"},
  {"kind": "gm", "t": "Cold Frame", "tier": "Compounded", "concept": "extend season", "mechanism": "glass-top box", "parts": ["frame"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "garden: vent on sun"},
  {"kind": "gm", "t": "Greenhouse (Small)", "tier": "Compounded", "concept": "grow year-round", "mechanism": "6x8 kit", "parts": ["house"], "build": "build", "time": "20h", "level": "intermediate", "safety": "anchor", "notes": "garden: vent + shade"},
  {"kind": "gm", "t": "Worm Bin", "tier": "Compounded", "concept": "black gold", "mechanism": "vermicompost bin", "parts": ["bin"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "garden: bedding + scraps"},
  {"kind": "gm", "t": "Compost Tumbler", "tier": "Compounded", "concept": "fast compost", "mechanism": "tumbler + browns", "parts": ["tumbler"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "garden: 3:1 browns"},
  {"kind": "gm", "t": "Hugelkultur Bed", "tier": "Compounded", "concept": "rich soil", "mechanism": "logs + soil mound", "parts": ["bed"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "garden: wood core holds water"},
  {"kind": "gm", "t": "Keyhole Garden", "tier": "Compounded", "concept": "accessible + compost", "mechanism": "round + center basket", "parts": ["garden"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "garden: wheelchair friendly"},
  {"kind": "gm", "t": "Espalier Frame", "tier": "Compounded", "concept": "fruit flat", "mechanism": "trellis + pruning", "parts": ["frame"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "garden: against warm wall"},
  {"kind": "gm", "t": "Mason Bee House", "tier": "Compounded", "concept": "pollination", "mechanism": "tubes + house", "parts": ["house"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "garden: morning sun"},
  {"kind": "gm", "t": "Greenhouse Controller", "tier": "Compounded", "concept": "auto climate", "mechanism": "temp + vent + water", "parts": ["controller"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "garden: 75F day target"},
  {"kind": "gm", "t": "Compost Aerator", "tier": "Compounded", "concept": "turn easy", "mechanism": "corkscrew tool", "parts": ["tool"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "garden: weekly turn"},
  {"kind": "gm", "t": "Aquaponics (Backyard)", "tier": "Advanced", "concept": "fish + plants", "mechanism": "IBC + beds", "parts": ["system"], "build": "build", "time": "40h", "level": "advanced", "safety": "food-safe", "notes": "garden: tilapia + lettuce"},
  {"kind": "gm", "t": "High Tunnel", "tier": "Advanced", "concept": "season extension", "mechanism": "30ft tunnel", "parts": ["tunnel"], "build": "build", "time": "40h", "level": "advanced", "safety": "anchor", "notes": "garden: wind bracing"},
  {"kind": "gm", "t": "Root Cellar Monitor", "tier": "Advanced", "concept": "store harvest", "mechanism": "buried + vents", "parts": ["cellar"], "build": "build", "time": "60h", "level": "advanced", "safety": "structural", "notes": "garden: 35-40F ideal"},
  {"kind": "gm", "t": "Orchard (Small)", "tier": "Advanced", "concept": "fruit years", "mechanism": "5 trees + guilds", "parts": ["orchard"], "build": "plant", "time": "20h", "level": "advanced", "safety": "none", "notes": "garden: chill hours match"},
  {"kind": "gm", "t": "Food Forest", "tier": "Advanced", "concept": "perennial abundance", "mechanism": "layers + guilds", "parts": ["forest"], "build": "plant", "time": "60h", "level": "advanced", "safety": "none", "notes": "garden: 7 layers"},
  {"kind": "gm", "t": "Market Garden", "tier": "Advanced", "concept": "sell produce", "mechanism": "30x50 + systems", "parts": ["garden"], "build": "build", "time": "100h", "level": "advanced", "safety": "business", "notes": "garden: wash station"},
  {"kind": "gm", "t": "Seed Saving Library", "tier": "Advanced", "concept": "adapt seeds", "mechanism": "dry + store + share", "parts": ["library"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "garden: isolation distances"},
  {"kind": "gm", "t": "Greenhouse Climate Controller", "tier": "Advanced", "concept": "serious growing", "mechanism": "12x20 + heat", "parts": ["house"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "garden: thermal mass"},
  {"kind": "gm", "t": "Irrigation (Zoned)", "tier": "Advanced", "concept": "water smart", "mechanism": "zones + sensors", "parts": ["system"], "build": "install", "time": "30h", "level": "advanced", "safety": "none", "notes": "garden: hydrozones"},
  {"kind": "gm", "t": "Master Garden Plan", "tier": "Advanced", "concept": "everything", "mechanism": "design + rotation", "parts": ["plan"], "build": "draw", "time": "20h", "level": "advanced", "safety": "none", "notes": "garden: 4-year rotation"}
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

