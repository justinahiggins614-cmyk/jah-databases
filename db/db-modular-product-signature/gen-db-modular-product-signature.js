(function(){'use strict';
/* JAH The Modular Product Universe — real working generator, jahdb-db-modular-product-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MOPRS-";
var SLUG="db-modular-product";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Modular Phone Case", "tier": "Foundations", "concept": "cases do one thing", "mechanism": "rails + add-on modules", "parts": ["case"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "modular: wallet, battery, kickstand"},
  {"kind": "gm", "t": "Stackable Storage", "tier": "Foundations", "concept": "boxes mismatch", "mechanism": "uniform footprint stacks", "parts": ["boxes"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "modular: one size, many heights"},
  {"kind": "gm", "t": "Modular Keychain", "tier": "Foundations", "concept": "keys jangle", "mechanism": "links add/remove tools", "parts": ["links"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "modular: carry only today's tools"},
  {"kind": "gm", "t": "Interlocking Planters", "tier": "Foundations", "concept": "plants outgrow pots", "mechanism": "pots link into walls", "parts": ["planters"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "modular: start 2, grow to 20"},
  {"kind": "gm", "t": "Modular Shelf", "tier": "Foundations", "concept": "needs change", "mechanism": "cubes bolt any arrangement", "parts": ["cubes"], "build": "build", "time": "10h", "level": "beginner", "safety": "anchor tall", "notes": "modular: reconfigure yearly"},
  {"kind": "gm", "t": "Camera Strap System", "tier": "Foundations", "concept": "straps tangle", "mechanism": "quick-release anchors", "parts": ["strap"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "modular: wrist to neck in seconds"},
  {"kind": "gm", "t": "Modular Lunch Box", "tier": "Foundations", "concept": "meals vary", "mechanism": "containers clip together", "parts": ["boxes"], "build": "study", "time": "2h", "level": "beginner", "safety": "food-safe", "notes": "modular: soup day vs salad day"},
  {"kind": "gm", "t": "Tool Wall Modules", "tier": "Foundations", "concept": "tools grow", "mechanism": "panels + hooks rearrange", "parts": ["panels"], "build": "mount", "time": "6h", "level": "beginner", "safety": "none", "notes": "modular: layout evolves"},
  {"kind": "gm", "t": "Modular Backpack (Lite)", "tier": "Foundations", "concept": "trips differ", "mechanism": "pods attach by need", "parts": ["pack"], "build": "sew", "time": "10h", "level": "beginner", "safety": "none", "notes": "modular: day pod vs camera pod"},
  {"kind": "gm", "t": "Lighting Modules", "tier": "Foundations", "concept": "moods change", "mechanism": "pucks link into shapes", "parts": ["pucks"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "modular: tiles become art"},
  {"kind": "gm", "t": "Modular Pet Bed", "tier": "Foundations", "concept": "pets grow", "mechanism": "sections zip together", "parts": ["bed"], "build": "sew", "time": "6h", "level": "beginner", "safety": "none", "notes": "modular: puppy to senior"},
  {"kind": "gm", "t": "Modular Workbench", "tier": "Compounded", "concept": "projects vary", "mechanism": "tops swap: wood, metal, cut", "parts": ["bench"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "modular: top for the task"},
  {"kind": "gm", "t": "Modular Synthesizer (Euro)", "tier": "Compounded", "concept": "sounds evolve", "mechanism": "modules patch freely", "parts": ["modules"], "build": "build", "time": "40h", "level": "intermediate", "safety": "low-voltage", "notes": "modular: VCO→filter→VCA voice"},
  {"kind": "gm", "t": "Modular Closet", "tier": "Compounded", "concept": "clothes change", "mechanism": "cubes + rods reconfigure", "parts": ["closet"], "build": "build", "time": "16h", "level": "intermediate", "safety": "anchor", "notes": "modular: seasons rearrange"},
  {"kind": "gm", "t": "Modular Drone", "tier": "Compounded", "concept": "missions differ", "mechanism": "camera/battery/frame swap", "parts": ["drone"], "build": "build", "time": "30h", "level": "intermediate", "safety": "prop safety", "notes": "modular: survey vs cinema"},
  {"kind": "gm", "t": "Modular Furniture (Couch)", "tier": "Compounded", "concept": "rooms change", "mechanism": "sections rearrange", "parts": ["sections"], "build": "build", "time": "24h", "level": "intermediate", "safety": "none", "notes": "modular: loveseat to sectional"},
  {"kind": "gm", "t": "Modular Greenhouse", "tier": "Compounded", "concept": "gardens grow", "mechanism": "panels add bays", "parts": ["panels"], "build": "build", "time": "30h", "level": "intermediate", "safety": "anchor", "notes": "modular: start 4x6, end 12x20"},
  {"kind": "gm", "t": "Modular E-Bike", "tier": "Compounded", "concept": "rides vary", "mechanism": "battery/motor/wheels swap", "parts": ["bike"], "build": "build", "time": "40h", "level": "intermediate", "safety": "battery safety", "notes": "modular: commuter to cargo"},
  {"kind": "gm", "t": "Modular Kitchen Cart", "tier": "Compounded", "concept": "kitchens small", "mechanism": "carts dock together", "parts": ["cart"], "build": "build", "time": "16h", "level": "intermediate", "safety": "locking casters", "notes": "modular: island when needed"},
  {"kind": "gm", "t": "Modular Audio (Speakers)", "tier": "Compounded", "concept": "rooms differ", "mechanism": "speakers link zones", "parts": ["speakers"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "modular: one to whole home"},
  {"kind": "gm", "t": "Modular Tent System", "tier": "Compounded", "concept": "trips vary", "mechanism": "pods zip by need", "parts": ["tent"], "build": "sew", "time": "20h", "level": "intermediate", "safety": "none", "notes": "modular: solo to family"},
  {"kind": "gm", "t": "Modular Robot Kit", "tier": "Compounded", "concept": "robots grow", "mechanism": "standard bus + modules", "parts": ["kit"], "build": "build", "time": "40h", "level": "intermediate", "safety": "low-voltage", "notes": "modular: sensors plug in"},
  {"kind": "gm", "t": "Modular Home (Concept)", "tier": "Advanced", "concept": "families change", "mechanism": "rooms add like LEGO", "parts": ["modules"], "build": "study", "time": "80h", "level": "advanced", "safety": "pro", "notes": "modular: the house grows up"},
  {"kind": "gm", "t": "Modular Phone (Full)", "tier": "Advanced", "concept": "phones obsolete", "mechanism": "CPU/camera/battery swap", "parts": ["phone"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "modular: upgrade, don't replace"},
  {"kind": "gm", "t": "Modular Exoskeleton", "tier": "Advanced", "concept": "tasks vary", "mechanism": "limb modules assist", "parts": ["exo"], "build": "build", "time": "100h", "level": "advanced", "safety": "pro", "notes": "modular: lift vs walk modes"},
  {"kind": "gm", "t": "Modular Car (Concept)", "tier": "Advanced", "concept": "needs change", "mechanism": "skateboard + bodies swap", "parts": ["car"], "build": "study", "time": "80h", "level": "advanced", "safety": "pro", "notes": "modular: one chassis, many bodies"},
  {"kind": "gm", "t": "Modular Data Center", "tier": "Advanced", "concept": "compute scales", "mechanism": "containers add capacity", "parts": ["containers"], "build": "study", "time": "60h", "level": "advanced", "safety": "pro", "notes": "modular: growth in boxes"},
  {"kind": "gm", "t": "Modular Boat", "tier": "Advanced", "concept": "waters vary", "mechanism": "hull sections join", "parts": ["boat"], "build": "build", "time": "100h", "level": "advanced", "safety": "marine safety", "notes": "modular: 12ft to 20ft"},
  {"kind": "gm", "t": "Modular Stage", "tier": "Advanced", "concept": "shows differ", "mechanism": "decks + truss reconfigure", "parts": ["stage"], "build": "build", "time": "60h", "level": "advanced", "safety": "rigging pro", "notes": "modular: club to festival"},
  {"kind": "gm", "t": "Modular Classroom", "tier": "Advanced", "concept": "classes change", "mechanism": "walls + furniture move", "parts": ["room"], "build": "design", "time": "60h", "level": "advanced", "safety": "pro", "notes": "modular: pedagogy in motion"},
  {"kind": "gm", "t": "Modular Farm Robot", "tier": "Advanced", "concept": "crops rotate", "mechanism": "implements swap", "parts": ["robot"], "build": "build", "time": "100h", "level": "advanced", "safety": "machine safety", "notes": "modular: weed, seed, harvest"},
  {"kind": "gm", "t": "Modular Habitat (Space)", "tier": "Advanced", "concept": "missions differ", "mechanism": "modules dock in orbit", "parts": ["habitat"], "build": "study", "time": "100h", "level": "advanced", "safety": "pro", "notes": "modular: ISS proved it"},
  {"kind": "gm", "t": "Modular Grid Battery", "tier": "Advanced", "concept": "power needs grow", "mechanism": "packs parallel by need", "parts": ["packs"], "build": "install", "time": "40h", "level": "advanced", "safety": "electrical pro", "notes": "modular: outage-proof in steps"},
  {"kind": "gm", "t": "Modular Tiny House", "tier": "Advanced", "concept": "home grows", "mechanism": "modules add rooms", "parts": ["house"], "build": "study", "time": "100h", "level": "advanced", "safety": "pro", "notes": "modular: start 200sqft"}
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

