(function(){'use strict';
/* JAH The Creative Workshop Planner — real working generator, jahdb-gen-creative-workshop-planner-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CWP-";
var SLUG="gen-creative-workshop-planner";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Kids Craft Party (2h)", "tier": "Foundations", "notes": "age-appropriate tools; allergy check snacks", "mats": [["supplies", "1", 60.0], ["snacks", "1", 25.0]], "tools": ["none"], "steps": ["3 stations", "demo each", "make", "show"], "time": "4h prep", "level": "beginner", "safety": "safety briefing"},
  {"kind": "diy", "t": "Library Maker Session", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 40.0]], "tools": ["none"], "steps": ["theme", "demo", "build", "share"], "time": "3h prep", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Senior Center Art Hour", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 35.0]], "tools": ["none"], "steps": ["simple project", "large tools", "social", "display"], "time": "3h prep", "level": "beginner", "safety": "accessibility — large grips, good light"},
  {"kind": "diy", "t": "Team Building Craft", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 80.0]], "tools": ["none"], "steps": ["icebreaker", "build teams", "compete gently", "share"], "time": "4h prep", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Scout Badge Workshop", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 50.0]], "tools": ["none"], "steps": ["badge reqs", "stations", "sign off", "celebrate"], "time": "5h prep", "level": "beginner", "safety": "badge requirements first"},
  {"kind": "diy", "t": "Homeschool Co-op Class", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 45.0]], "tools": ["none"], "steps": ["lesson", "demo", "make", "journal"], "time": "4h prep", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Birthday Workshop", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 70.0], ["cake", "1", 25.0]], "tools": ["none"], "steps": ["theme", "make", "party", "take home"], "time": "5h prep", "level": "beginner", "safety": "allergy check"},
  {"kind": "diy", "t": "Community Center Intro", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 40.0]], "tools": ["none"], "steps": ["welcome", "project", "help", "gallery"], "time": "3h prep", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "After-School Club", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 50.0]], "tools": ["none"], "steps": ["routine", "project", "free build", "share"], "time": "4h prep", "level": "beginner", "safety": "consistent routine calms chaos"},
  {"kind": "diy", "t": "Family Make Night", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 55.0]], "tools": ["none"], "steps": ["all-ages project", "stations", "together", "photo"], "time": "4h prep", "level": "beginner", "safety": "projects for mixed ages"},
  {"kind": "diy", "t": "Virtual Craft Night", "tier": "Foundations", "notes": "test tech", "mats": [["kits mailed", "1", 120.0], ["platform", "1", 0.0]], "tools": ["none"], "steps": ["ship kits", "demo live", "make together", "show"], "time": "6h prep", "level": "beginner", "safety": "ship early"},
  {"kind": "diy", "t": "Woodworking Basics (Adult)", "tier": "Compounded", "notes": "guards on; first aid kit; dust masks", "mats": [["wood", "1", 120.0], ["tools", "1", 80.0], ["safety", "1", 30.0]], "tools": ["saw"], "steps": ["safety talk", "project", "build", "finish"], "time": "12h prep", "level": "intermediate", "safety": "FULL tool safety briefing"},
  {"kind": "diy", "t": "Sewing 101 Series", "tier": "Compounded", "notes": "supervision", "mats": [["machines", "6", 0.0], ["fabric", "1", 80.0], ["notions", "1", 40.0]], "tools": ["sewing"], "steps": ["4 sessions", "machine basics", "project", "hem"], "time": "16h prep", "level": "intermediate", "safety": "needle safety"},
  {"kind": "diy", "t": "Pottery Hand-Building", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["clay", "1", 60.0], ["tools", "1", 40.0], ["kiln", "1", 0.0]], "tools": ["kiln"], "steps": ["pinch/coil/slab", "make", "dry", "fire"], "time": "16h prep", "level": "intermediate", "safety": "kiln safety — trained operator only"},
  {"kind": "diy", "t": "Printmaking Workshop", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["inks", "1", 50.0], ["blocks", "1", 40.0], ["paper", "1", 30.0], ["press", "1", 0.0]], "tools": ["carving"], "steps": ["design", "carve", "print", "edition"], "time": "12h prep", "level": "intermediate", "safety": "carve away from body"},
  {"kind": "diy", "t": "Jewelry Making Day", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 120.0], ["tools", "1", 60.0]], "tools": ["pliers"], "steps": ["demo", "practice", "project", "finish"], "time": "10h prep", "level": "intermediate", "safety": "eye protection for wire"},
  {"kind": "diy", "t": "Corporate Offsite Make", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 150.0]], "tools": ["none"], "steps": ["brief", "teams", "build", "showcase"], "time": "8h prep", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "School STEAM Day", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 120.0], ["stations", "1", 0.0]], "tools": ["none"], "steps": ["4 stations", "rotate", "demos", "share"], "time": "12h prep", "level": "intermediate", "safety": "station safety captains"},
  {"kind": "diy", "t": "Photography Walk + Edit", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cameras", "1", 0.0], ["software", "1", 0.0]], "tools": ["none"], "steps": ["walk", "shoot", "edit", "share"], "time": "8h prep", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Cooking Class: Basics", "tier": "Compounded", "notes": "allergy list; knife safety", "mats": [["ingredients", "1", 100.0], ["tools", "1", 0.0]], "tools": ["none"], "steps": ["demo", "cook", "eat", "recipes"], "time": "10h prep", "level": "intermediate", "safety": "food safety"},
  {"kind": "diy", "t": "Gardening Workshop", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["plants", "1", 80.0], ["soil", "1", 40.0], ["tools", "1", 30.0]], "tools": ["trowel"], "steps": ["demo", "plant", "take home", "care"], "time": "8h prep", "level": "intermediate", "safety": "sun/heat safety outdoors"},
  {"kind": "diy", "t": "Upcycling Challenge", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 60.0], ["tools", "1", 40.0]], "tools": ["varies"], "steps": ["prompt", "build", "judge", "prize"], "time": "10h prep", "level": "intermediate", "safety": "tool safety per station"},
  {"kind": "diy", "t": "Mural Project (Community)", "tier": "Compounded", "notes": "permission in writing", "mats": [["paint", "1", 150.0], ["supplies", "1", 60.0]], "tools": ["ladder"], "steps": ["design", "grid", "paint", "seal"], "time": "20h prep", "level": "intermediate", "safety": "ladder safety"},
  {"kind": "diy", "t": "Furniture Refinish Weekend", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["pieces", "1", 80.0], ["supplies", "1", 100.0]], "tools": ["sander"], "steps": ["strip", "sand", "finish", "reveal"], "time": "16h prep", "level": "intermediate", "safety": "chemical stripper safety — respirator, gloves"},
  {"kind": "diy", "t": "Festival Demo Booth", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["booth", "1", 180.0], ["demos", "1", 120.0]], "tools": ["none"], "steps": ["plan flow", "staff", "engage", "capture"], "time": "20h prep", "level": "advanced", "safety": "public demo safety — barriers"},
  {"kind": "diy", "t": "Blacksmith Taster", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["forge", "1", 200.0], ["steel", "1", 60.0], ["safety", "1", 50.0]], "tools": ["forge"], "steps": ["safety intense", "forge", "project", "cool"], "time": "20h prep", "level": "advanced", "safety": "PROFESSIONAL ONLY — burns, eye protection, fire watch"},
  {"kind": "diy", "t": "Welding Intro", "tier": "Advanced", "notes": "arc flash, fumes, fire watch", "mats": [["welder", "1", 300.0], ["steel", "1", 80.0], ["safety", "1", 80.0]], "tools": ["welder"], "steps": ["safety", "practice", "project", "inspect"], "time": "24h prep", "level": "advanced", "safety": "CERTIFIED INSTRUCTOR"},
  {"kind": "diy", "t": "Furniture Build (4 Weeks)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["lumber", "1", 300.0], ["hardware", "1", 80.0]], "tools": ["saw"], "steps": ["4 sessions", "cut", "join", "finish"], "time": "40h prep", "level": "advanced", "safety": "full shop safety protocol"},
  {"kind": "diy", "t": "Stained Glass Series", "tier": "Advanced", "notes": "solder fumes ventilate", "mats": [["glass", "1", 150.0], ["tools", "1", 120.0]], "tools": ["soldering"], "steps": ["4 sessions", "cut", "foil", "solder", "finish"], "time": "32h prep", "level": "advanced", "safety": "glass cuts"},
  {"kind": "diy", "t": "Bronze Casting Demo", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foundry", "1", 500.0], ["materials", "1", 200.0]], "tools": ["furnace"], "steps": ["safety", "mold", "pour", "finish"], "time": "40h prep", "level": "advanced", "safety": "PROFESSIONAL FOUNDRY ONLY"},
  {"kind": "diy", "t": "Timber Framing Day", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["timbers", "1", 400.0], ["tools", "1", 150.0]], "tools": ["none"], "steps": ["layout", "cut joints", "raise", "peg"], "time": "40h prep", "level": "advanced", "safety": "raising day — crew safety briefing"},
  {"kind": "diy", "t": "Boat Building Week", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 600.0], ["tools", "1", 200.0]], "tools": ["saw"], "steps": ["loft", "build", "glass", "launch"], "time": "80h prep", "level": "advanced", "safety": "long commitment — crew confirmed"},
  {"kind": "diy", "t": "Maker Faire Booth", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["booth", "1", 200.0], ["demos", "1", 150.0]], "tools": ["none"], "steps": ["plan demos", "staff", "engage", "follow up"], "time": "30h prep", "level": "advanced", "safety": "demo safety for public"},
  {"kind": "diy", "t": "Train-the-Trainer", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 150.0]], "tools": ["none"], "steps": ["curriculum", "practice", "feedback", "certify"], "time": "24h prep", "level": "advanced", "safety": "none"}
];
var TIPS=["Cut everything before you glue anything.", "Dry-fit twice, fasten once.", "Sharp tools are safe tools \u2014 hone before you start.", "Finish scraps first to test color.", "Label your parts as you cut them.", "Take a photo before disassembly for reference."];
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

