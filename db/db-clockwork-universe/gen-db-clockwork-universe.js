(function(){'use strict';
/* JAH The Clockwork Universe Database — real working generator, jahdb-db-clockwork-universe-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CU-";
var SLUG="db-clockwork-universe";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Test structures gradually to rated load; keep a clear fall/drop zone during testing.", "Pinch points guarded on moving mechanisms; secure tall builds against tipping.", "Mainspring work with a proper winder; eye protection when handling springs under tension."];
var CITATIONS=["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.", "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.", "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."];
var BANK=[
  {"kind": "gm", "t": "What Makes Clockwork Tick", "tier": "Foundations", "concept": "time needs counting", "mechanism": "escapement meters energy", "parts": ["study"], "build": "read", "time": "4h", "level": "beginner", "safety": "none", "notes": "clockwork: the heartbeat of machines"},
  {"kind": "gm", "t": "Gears: Teeth That Talk", "tier": "Foundations", "concept": "motion needs transfer", "mechanism": "teeth mesh, ratios rule", "parts": ["gears"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "clockwork: ratio = teeth out / teeth in"},
  {"kind": "gm", "t": "Springs: Stored Push", "tier": "Foundations", "concept": "energy needs storing", "mechanism": "coil stores torque", "parts": ["spring"], "build": "study", "time": "2h", "level": "beginner", "safety": "spring snap", "notes": "clockwork: mainspring = battery"},
  {"kind": "gm", "t": "The Pendulum", "tier": "Foundations", "concept": "time needs rhythm", "mechanism": "period depends on length", "parts": ["pendulum"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "clockwork: 1m ≈ 2 seconds"},
  {"kind": "gm", "t": "Winding a Clock", "tier": "Foundations", "concept": "clocks stop", "mechanism": "key winds mainspring", "parts": ["key"], "build": "practice", "time": "1h", "level": "beginner", "safety": "overwind", "notes": "clockwork: stop at resistance"},
  {"kind": "gm", "t": "Reading Gear Ratios", "tier": "Foundations", "concept": "speed vs force", "mechanism": "count teeth, divide", "parts": ["gears"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "clockwork: 8:60 = 7.5x slower, stronger"},
  {"kind": "gm", "t": "The Fusee (History)", "tier": "Foundations", "concept": "springs weaken", "mechanism": "cone evens torque", "parts": ["fusee"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "clockwork: 15th-century cruise control"},
  {"kind": "gm", "t": "Clock Hands & Dials", "tier": "Foundations", "concept": "time needs reading", "mechanism": "12:1 motion work", "parts": ["hands"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "clockwork: the original UI"},
  {"kind": "gm", "t": "Oiling a Movement", "tier": "Foundations", "concept": "friction kills", "mechanism": "tiny oil at pivots", "parts": ["oil"], "build": "practice", "time": "3h", "level": "beginner", "safety": "none", "notes": "clockwork: less is more"},
  {"kind": "gm", "t": "The Cuckoo Call", "tier": "Foundations", "concept": "hours need announcing", "mechanism": "bellows + pipes", "parts": ["pipes"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "clockwork: two notes, endless charm"},
  {"kind": "gm", "t": "Wind-Up Toys", "tier": "Foundations", "concept": "play needs power", "mechanism": "spring + escapement", "parts": ["toy"], "build": "study", "time": "2h", "level": "beginner", "safety": "spring", "notes": "clockwork: the gateway"},
  {"kind": "gm", "t": "Quartz vs Mechanical", "tier": "Foundations", "concept": "battery vs spring", "mechanism": "quartz vibrates 32768Hz", "parts": ["study"], "build": "read", "time": "2h", "level": "beginner", "safety": "none", "notes": "clockwork: why mechanical endures"},
  {"kind": "gm", "t": "Verge Escapement", "tier": "Compounded", "concept": "first escapement", "mechanism": "verge + foliot", "parts": ["movement"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "clockwork: 1300s tech, ±30min/day"},
  {"kind": "gm", "t": "Anchor Escapement", "tier": "Compounded", "concept": "better time", "mechanism": "recoil anchor + pendulum", "parts": ["movement"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "clockwork: longcase revolution"},
  {"kind": "gm", "t": "Deadbeat Escapement", "tier": "Compounded", "concept": "precision matters", "mechanism": "no recoil, clean lock", "parts": ["movement"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "clockwork: regulator grade"},
  {"kind": "gm", "t": "The Tourbillon", "tier": "Compounded", "concept": "gravity errs", "mechanism": "rotating cage averages", "parts": ["tourbillon"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "clockwork: 1801, still wow"},
  {"kind": "gm", "t": "Gear Cutting Basics", "tier": "Compounded", "concept": "gears need teeth", "mechanism": "involute cutters", "parts": ["cutter"], "build": "cut", "time": "16h", "level": "intermediate", "safety": "machine safety", "notes": "clockwork: module = size system"},
  {"kind": "gm", "t": "Building a Wooden Clock", "tier": "Compounded", "concept": "time from timber", "mechanism": "laser-cut + plans", "parts": ["kit"], "build": "build", "time": "30h", "level": "intermediate", "safety": "none", "notes": "clockwork: satisfying tick"},
  {"kind": "gm", "t": "Mainspring Replacement", "tier": "Compounded", "concept": "springs tire", "mechanism": "winder + new spring", "parts": ["spring"], "build": "replace", "time": "6h", "level": "intermediate", "safety": "spring danger", "notes": "clockwork: winder mandatory"},
  {"kind": "gm", "t": "Bushing a Pivot", "tier": "Compounded", "concept": "holes wear oval", "mechanism": "ream + press bushing", "parts": ["tools"], "build": "repair", "time": "8h", "level": "intermediate", "safety": "none", "notes": "clockwork: restores slop"},
  {"kind": "gm", "t": "Striking Trains", "tier": "Compounded", "concept": "chime the hours", "mechanism": "count wheel + hammer", "parts": ["train"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "clockwork: rack vs count wheel"},
  {"kind": "gm", "t": "The Grasshopper", "tier": "Compounded", "concept": "Harrison's genius", "mechanism": "long legs, no oil", "parts": ["movement"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "clockwork: longitude prize tech"},
  {"kind": "gm", "t": "Atmos Clock", "tier": "Compounded", "concept": "wound by weather", "mechanism": "temperature bellows", "parts": ["clock"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "clockwork: 1 degree = 2 days power"},
  {"kind": "gm", "t": "Skeleton Clocks", "tier": "Compounded", "concept": "see the works", "mechanism": "open plates", "parts": ["study"], "build": "read", "time": "4h", "level": "intermediate", "safety": "none", "notes": "clockwork: beauty in mechanism"},
  {"kind": "gm", "t": "Complications: Moonphase", "tier": "Advanced", "concept": "moon matters", "mechanism": "59-tooth wheel", "parts": ["wheel"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "clockwork: 29.5 days per turn"},
  {"kind": "gm", "t": "Perpetual Calendar", "tier": "Advanced", "concept": "dates are hard", "mechanism": "levers know leap years", "parts": ["calendar"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "clockwork: 400-year logic in brass"},
  {"kind": "gm", "t": "Minute Repeater", "tier": "Advanced", "concept": "time in dark", "mechanism": "chimes hours/quarters/minutes", "parts": ["repeater"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "clockwork: the grand complication"},
  {"kind": "gm", "t": "Building a Regulator", "tier": "Advanced", "concept": "precision time", "mechanism": "deadbeat + gridiron", "parts": ["regulator"], "build": "build", "time": "80h", "level": "advanced", "safety": "none", "notes": "clockwork: seconds a week"},
  {"kind": "gm", "t": "Orrery (Planetarium)", "tier": "Advanced", "concept": "planets dance", "mechanism": "geared solar system", "parts": ["orrery"], "build": "build", "time": "100h", "level": "advanced", "safety": "none", "notes": "clockwork: ratios from astronomy"},
  {"kind": "gm", "t": "Clock Restoration", "tier": "Advanced", "concept": "heirlooms tick", "mechanism": "disassemble + restore", "parts": ["clock"], "build": "restore", "time": "40h", "level": "advanced", "safety": "mainspring", "notes": "clockwork: document everything"},
  {"kind": "gm", "t": "Chronometer (Marine)", "tier": "Advanced", "concept": "longitude at sea", "mechanism": "gimbal + detent", "parts": ["chrono"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "clockwork: Harrison's H4"},
  {"kind": "gm", "t": "Atomic Clock (Concept)", "tier": "Advanced", "concept": "ultimate time", "mechanism": "cesium vibration counts", "parts": ["atom"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "clockwork: 9 billion ticks/sec"},
  {"kind": "gm", "t": "Clockwork Computer", "tier": "Advanced", "concept": "compute with gears", "mechanism": "Babbage's engine", "parts": ["engine"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "clockwork: Difference Engine No.2"},
  {"kind": "gm", "t": "Master Clockmaker Path", "tier": "Advanced", "concept": "the craft", "mechanism": "apprentice + practice", "parts": ["path"], "build": "study", "time": "100h", "level": "advanced", "safety": "none", "notes": "clockwork: years to mastery"}
];
var TIPS=["Build one stage and test it before connecting the next.", "Time the real machine and tune to the math.", "Guard every pinch point before demonstrating.", "Level the base before trusting the tower.", "Keep a build log with measurements.", "Test to failure on purpose \u2014 once."];
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

