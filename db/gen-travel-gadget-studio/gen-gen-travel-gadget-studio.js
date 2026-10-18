(function(){'use strict';
/* JAH The Travel Gadget Studio — real working generator, jahdb-gen-travel-gadget-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TGS-";
var SLUG="gen-travel-gadget-studio";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Packing Cube System", "tier": "Foundations", "concept": "chaos in suitcase", "mechanism": "zip cubes categorize", "parts": ["fabric"], "build": "sew", "time": "6h", "level": "beginner", "safety": "none", "notes": "design: cubes by outfit, not category"},
  {"kind": "gm", "t": "Travel Pillow 2.0", "tier": "Foundations", "concept": "necks suffer", "mechanism": "chin-support hybrid", "parts": ["fabric", "valve"], "build": "sew", "time": "8h", "level": "beginner", "safety": "none", "notes": "design: test on a real flight of stairs nap"},
  {"kind": "gm", "t": "Cable Organizer Roll", "tier": "Foundations", "concept": "cables tangle", "mechanism": "elastic loops in roll", "parts": ["fabric"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "design: one loop per cable, labeled"},
  {"kind": "gm", "t": "Toiletry Kit (Leak-Proof)", "tier": "Foundations", "concept": "spills ruin trips", "mechanism": "squeeze bottles + dry bag", "parts": ["bottles"], "build": "pack", "time": "2h", "level": "beginner", "safety": "none", "notes": "design: decant, don't carry full-size"},
  {"kind": "gm", "t": "Laundry Kit (Sink)", "tier": "Foundations", "concept": "laundry piles up", "mechanism": "sink soap + line + clips", "parts": ["soap", "line"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "design: 3 outfits rotate forever"},
  {"kind": "gm", "t": "Document Wallet", "tier": "Foundations", "concept": "papers scatter", "mechanism": "passport + cards + pen folio", "parts": ["leather"], "build": "stitch", "time": "4h", "level": "beginner", "safety": "none", "notes": "design: one grab = all documents"},
  {"kind": "gm", "t": "Travel Door Lock", "tier": "Foundations", "concept": "hotel doors worry", "mechanism": "portable wedge lock", "parts": ["lock"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "design: 30-second install"},
  {"kind": "gm", "t": "Compression Sacks", "tier": "Foundations", "concept": "bulky clothes", "mechanism": "squeeze air out", "parts": ["fabric"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "design: roll, then compress"},
  {"kind": "gm", "t": "Snack Kit", "tier": "Foundations", "concept": "hangry travels", "mechanism": "portion boxes + spork", "parts": ["boxes"], "build": "pack", "time": "1h", "level": "beginner", "safety": "food safety", "notes": "design: protein + salty + sweet"},
  {"kind": "gm", "t": "First-Aid Mini", "tier": "Foundations", "concept": "blisters happen", "mechanism": "moleskin + meds + tape kit", "parts": ["kit"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "design: feet first, then stomach"},
  {"kind": "gm", "t": "Entertainment Kit", "tier": "Foundations", "concept": "delays drag", "mechanism": "book + cards + audio loaded", "parts": ["kit"], "build": "pack", "time": "2h", "level": "beginner", "safety": "none", "notes": "design: offline everything"},
  {"kind": "gm", "t": "Universal Power Kit", "tier": "Compounded", "concept": "outlets differ", "mechanism": "GaN charger + adapters + short cables", "parts": ["charger"], "build": "build", "time": "6h", "level": "intermediate", "safety": "mains — pro", "notes": "design: 65W covers laptop + phone"},
  {"kind": "gm", "t": "Travel Tripod", "tier": "Compounded", "concept": "shaky memories", "mechanism": "pocket tripod + phone mount", "parts": ["tripod"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "design: wraps to rails"},
  {"kind": "gm", "t": "Water Purifier (Travel)", "tier": "Compounded", "concept": "water doubts", "mechanism": "filter + UV bottle", "parts": ["filter"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "design: filter then UV, belt and suspenders"},
  {"kind": "gm", "t": "Portable Safe", "tier": "Compounded", "concept": "valuables worry", "mechanism": "cable-lock bag safe", "parts": ["safe"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "design: lock to fixed furniture"},
  {"kind": "gm", "t": "Travel White-Noise", "tier": "Compounded", "concept": "noise ruins sleep", "mechanism": "pocket speaker + brown noise", "parts": ["speaker"], "build": "build", "time": "4h", "level": "intermediate", "safety": "low-voltage", "notes": "design: brown noise > white for sleep"},
  {"kind": "gm", "t": "Clothesline (Travel)", "tier": "Compounded", "concept": "drying nowhere", "mechanism": "suction + twist line", "parts": ["line"], "build": "build", "time": "2h", "level": "intermediate", "safety": "none", "notes": "design: twist line needs no pegs"},
  {"kind": "gm", "t": "Travel Kitchen Kit", "tier": "Compounded", "concept": "eating out costs", "mechanism": "stove + pot + spork kit", "parts": ["stove"], "build": "build", "time": "8h", "level": "intermediate", "safety": "fuel safety", "notes": "design: one-pot meals"},
  {"kind": "gm", "t": "Sleep Kit (Light+Sound)", "tier": "Compounded", "concept": "hostels glare", "mechanism": "mask + earplugs + pillow", "parts": ["kit"], "build": "pack", "time": "2h", "level": "intermediate", "safety": "none", "notes": "design: contoured mask, no eye pressure"},
  {"kind": "gm", "t": "Travel Workstation", "tier": "Compounded", "concept": "work from anywhere", "mechanism": "laptop stand + keyboard + hub", "parts": ["stand"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "design: ergonomics in a pouch"},
  {"kind": "gm", "t": "Camera Carry System", "tier": "Compounded", "concept": "gear chaos", "mechanism": "modular inserts + quick access", "parts": ["inserts"], "build": "sew", "time": "10h", "level": "intermediate", "safety": "none", "notes": "design: camera never leaves your side"},
  {"kind": "gm", "t": "Travel Guitar (Folding)", "tier": "Compounded", "concept": "music misses you", "mechanism": "detachable neck travel guitar", "parts": ["guitar"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "design: full scale, half size"},
  {"kind": "gm", "t": "Solar Charger Kit", "tier": "Advanced", "concept": "off-grid power", "mechanism": "folding panel + bank + cables", "parts": ["panel"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "design: panel charges bank by day"},
  {"kind": "gm", "t": "Travel Drone Kit", "tier": "Advanced", "concept": "views from above", "mechanism": "folding drone + ND filters", "parts": ["drone"], "build": "fly", "time": "10h", "level": "advanced", "safety": "drone laws", "notes": "design: sub-250g avoids most regs"},
  {"kind": "gm", "t": "Mobile Office (Full)", "tier": "Advanced", "concept": "work anywhere", "mechanism": "laptop + monitor + power", "parts": ["gear"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "design: 2 screens in a backpack"},
  {"kind": "gm", "t": "Travel Medical Kit", "tier": "Advanced", "concept": "remote health", "mechanism": "extended meds + guides", "parts": ["kit"], "build": "pack", "time": "6h", "level": "advanced", "safety": "none", "notes": "design: prescriptions + copies"},
  {"kind": "gm", "t": "Overland Kitchen", "tier": "Advanced", "concept": "cook anywhere", "mechanism": "chuck box + stove + water", "parts": ["box"], "build": "build", "time": "30h", "level": "advanced", "safety": "fuel safety", "notes": "design: everything in one box"},
  {"kind": "gm", "t": "Travel Security Kit", "tier": "Advanced", "concept": "digital theft", "mechanism": "VPN + locks + RFID", "parts": ["kit"], "build": "build", "time": "8h", "level": "advanced", "safety": "none", "notes": "design: layers, not paranoia"},
  {"kind": "gm", "t": "Photography Expedition", "tier": "Advanced", "concept": "pro shots traveling", "mechanism": "full kit + backup + power", "parts": ["gear"], "build": "plan", "time": "20h", "level": "advanced", "safety": "none", "notes": "design: backup bodies save trips"},
  {"kind": "gm", "t": "Long-Term Pack (1 Bag)", "tier": "Advanced", "concept": "live from one bag", "mechanism": "40L + systems + laundry", "parts": ["pack"], "build": "plan", "time": "12h", "level": "advanced", "safety": "none", "notes": "design: 7kg, 3 weeks, done"},
  {"kind": "gm", "t": "Travel With Kids Kit", "tier": "Advanced", "concept": "kids + travel", "mechanism": "entertainment + snacks + comfort", "parts": ["kit"], "build": "pack", "time": "8h", "level": "advanced", "safety": "none", "notes": "design: new toy per flight"},
  {"kind": "gm", "t": "Adventure Medical", "tier": "Advanced", "concept": "far from help", "mechanism": "trauma + meds + comms", "parts": ["kit"], "build": "pack", "time": "10h", "level": "advanced", "safety": "training first", "notes": "design: training beats gear"},
  {"kind": "gm", "t": "Digital Nomad Setup", "tier": "Advanced", "concept": "work forever traveling", "mechanism": "redundant power + connectivity", "parts": ["gear"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "design: two of everything critical"},
  {"kind": "gm", "t": "Travel Hammock (Ultralight)", "tier": "Advanced", "concept": "rest anywhere", "mechanism": "8oz + straps", "parts": ["hammock"], "build": "sew", "time": "8h", "level": "advanced", "safety": "tree safety", "notes": "design: straps protect bark"}
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
  var suf="";
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

