(function(){'use strict';
/* JAH The Pocket Workshop Database — real working generator, jahdb-gen-pocket-workshop-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PWS-";
var SLUG="gen-pocket-workshop";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Pocket Screwdriver Set", "tier": "Foundations", "concept": "screws everywhere", "mechanism": "bits + driver pen", "parts": ["set"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "workshop: the foundation"},
  {"kind": "gm", "t": "Mini Pliers", "tier": "Foundations", "concept": "grip + bend", "mechanism": "5in pliers", "parts": ["pliers"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: smooth jaws for finish"},
  {"kind": "gm", "t": "Folding Saw", "tier": "Foundations", "concept": "cut wood", "mechanism": "pull-saw folds", "parts": ["saw"], "build": "study", "time": "1h", "level": "beginner", "safety": "blade sharp", "notes": "workshop: pull stroke cuts"},
  {"kind": "gm", "t": "Tape Measure (Pocket)", "tier": "Foundations", "concept": "measure", "mechanism": "16ft compact", "parts": ["tape"], "build": "study", "time": "1h", "level": "beginner", "safety": "tape edge", "notes": "workshop: measure twice"},
  {"kind": "gm", "t": "Hex Key Set", "tier": "Foundations", "concept": "furniture bolts", "mechanism": "folding hex set", "parts": ["keys"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: ball ends angle"},
  {"kind": "gm", "t": "Utility Knife", "tier": "Foundations", "concept": "cut all", "mechanism": "retractable + spare blades", "parts": ["knife"], "build": "study", "time": "1h", "level": "beginner", "safety": "blade sharp", "notes": "workshop: fresh blades"},
  {"kind": "gm", "t": "Mini Level", "tier": "Foundations", "concept": "level hang", "mechanism": "9in torpedo", "parts": ["level"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: 3 vials"},
  {"kind": "gm", "t": "Stud Finder", "tier": "Foundations", "concept": "find studs", "mechanism": "magnetic + electronic", "parts": ["finder"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "workshop: mark edges"},
  {"kind": "gm", "t": "Workshop Headlamp", "tier": "Foundations", "concept": "see work", "mechanism": "300lm + red", "parts": ["headlamp"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: red preserves night"},
  {"kind": "gm", "t": "Gloves (Work)", "tier": "Foundations", "concept": "protect hands", "mechanism": "cut-resistant", "parts": ["gloves"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: fit matters"},
  {"kind": "gm", "t": "Pencil + Notebook", "tier": "Foundations", "concept": "mark + note", "mechanism": "carpenter pencil", "parts": ["pencil"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "workshop: mark the waste side"},
  {"kind": "gm", "t": "Cordless Drill (12V)", "tier": "Compounded", "concept": "drill anywhere", "mechanism": "12V + bits compact", "parts": ["drill"], "build": "build", "time": "8h", "level": "intermediate", "safety": "eye protection", "notes": "workshop: clutch prevents strip"},
  {"kind": "gm", "t": "Multi-Tool (Oscillating)", "tier": "Compounded", "concept": "cut/sand/scrape", "mechanism": "oscillating head", "parts": ["tool"], "build": "build", "time": "10h", "level": "intermediate", "safety": "dust mask", "notes": "workshop: blades per material"},
  {"kind": "gm", "t": "Pocket Soldering", "tier": "Compounded", "concept": "electronics fix", "mechanism": "butane iron pen", "parts": ["iron"], "build": "build", "time": "8h", "level": "intermediate", "safety": "burn/fume", "notes": "workshop: tin the tip"},
  {"kind": "gm", "t": "Mini Clamps", "tier": "Compounded", "concept": "hold work", "mechanism": "4 pack spring", "parts": ["clamps"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "workshop: clamp, don't hold"},
  {"kind": "gm", "t": "Diamond Files", "tier": "Compounded", "concept": "deburr/fit", "mechanism": "needle file set", "parts": ["files"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "workshop: one direction"},
  {"kind": "gm", "t": "Thread Checker", "tier": "Compounded", "concept": "identify bolts", "mechanism": "thread gauge card", "parts": ["gauge"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "workshop: metric vs SAE"},
  {"kind": "gm", "t": "Voltage Tester", "tier": "Compounded", "concept": "live or not", "mechanism": "non-contact tester", "parts": ["tester"], "build": "study", "time": "1h", "level": "intermediate", "safety": "electrical", "notes": "workshop: test before touch"},
  {"kind": "gm", "t": "Pocket Air Pump", "tier": "Compounded", "concept": "inflate", "mechanism": "mini pump + gauge", "parts": ["pump"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "workshop: gauge prevents pop"},
  {"kind": "gm", "t": "Folding Workbench", "tier": "Compounded", "concept": "bench anywhere", "mechanism": "folding + clamp top", "parts": ["bench"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "workshop: 220lb rating"},
  {"kind": "gm", "t": "Pocket Tool Roll", "tier": "Compounded", "concept": "organize", "mechanism": "canvas roll", "parts": ["roll"], "build": "sew", "time": "6h", "level": "intermediate", "safety": "none", "notes": "workshop: shadow board in cloth"},
  {"kind": "gm", "t": "Parts Organizer", "tier": "Compounded", "concept": "screws chaos", "mechanism": "compartment box", "parts": ["box"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "workshop: label everything"},
  {"kind": "gm", "t": "Portable Vise", "tier": "Advanced", "concept": "hold firm", "mechanism": "clamp-on vise", "parts": ["vise"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "workshop: mount to anything"},
  {"kind": "gm", "t": "Micro Lathe", "tier": "Advanced", "concept": "turn small", "mechanism": "benchtop lathe", "parts": ["lathe"], "build": "build", "time": "40h", "level": "advanced", "safety": "machine safety", "notes": "workshop: 0.01mm possible"},
  {"kind": "gm", "t": "Benchtop Mill", "tier": "Advanced", "concept": "mill precise", "mechanism": "mini mill", "parts": ["mill"], "build": "build", "time": "60h", "level": "advanced", "safety": "machine safety", "notes": "workshop: tram the head"},
  {"kind": "gm", "t": "Welding (Pocket Kit)", "tier": "Advanced", "concept": "join metal", "mechanism": "micro torch kit", "parts": ["torch"], "build": "build", "time": "30h", "level": "advanced", "safety": "fire/eye pro", "notes": "workshop: pro training first"},
  {"kind": "gm", "t": "3D Printer (Portable)", "tier": "Advanced", "concept": "print anywhere", "mechanism": "folding printer", "parts": ["printer"], "build": "build", "time": "40h", "level": "advanced", "safety": "burn", "notes": "workshop: 8-12h prints (estimate)"},
  {"kind": "gm", "t": "CNC (Desktop)", "tier": "Advanced", "concept": "mill anywhere", "mechanism": "3018 + upgrades", "parts": ["cnc"], "build": "build", "time": "40h", "level": "advanced", "safety": "dust/eye", "notes": "workshop: feeds and speeds"},
  {"kind": "gm", "t": "Forge (Micro)", "tier": "Advanced", "concept": "shape steel", "mechanism": "coffee-can forge", "parts": ["forge"], "build": "build", "time": "30h", "level": "advanced", "safety": "fire pro", "notes": "workshop: outdoor only"},
  {"kind": "gm", "t": "Anodizing Kit", "tier": "Advanced", "concept": "color metal", "mechanism": "small anodize setup", "parts": ["kit"], "build": "build", "time": "20h", "level": "advanced", "safety": "chemical safety", "notes": "workshop: ventilate"},
  {"kind": "gm", "t": "Powder Coat (Small)", "tier": "Advanced", "concept": "finish durable", "mechanism": "powder + oven", "parts": ["kit"], "build": "build", "time": "30h", "level": "advanced", "safety": "dust/fire", "notes": "workshop: dedicated oven"},
  {"kind": "gm", "t": "Laser (Diode)", "tier": "Advanced", "concept": "engrave anywhere", "mechanism": "diode + enclosure", "parts": ["laser"], "build": "build", "time": "30h", "level": "advanced", "safety": "eye safety — enclosure", "notes": "workshop: never open beam"},
  {"kind": "gm", "t": "Full Pocket Shop", "tier": "Advanced", "concept": "everything", "mechanism": "curated 20-tool kit", "parts": ["kit"], "build": "pack", "time": "20h", "level": "advanced", "safety": "training", "notes": "workshop: skill > tools"},
  {"kind": "gm", "t": "Pocket Caliper", "tier": "Advanced", "concept": "measure precise", "mechanism": "6in digital", "parts": ["caliper"], "build": "study", "time": "2h", "level": "advanced", "safety": "none", "notes": "workshop: 0.01mm anywhere"}
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

